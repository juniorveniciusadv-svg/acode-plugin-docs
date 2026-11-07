"""Consulta de processos na API Pública do DataJud (CNJ).

Funciona igual no Google Colab, no Termux (Debian via proot-distro),
em qualquer computador e no GitHub Actions.

Uso interativo:
    python3 datajud.py

Uso direto:
    python3 datajud.py --tribunal tjsp --numero 0000000-00.0000.8.26.0000

Monitoramento de vários processos (usado pelo GitHub Actions):
    python3 datajud.py --lista processos.txt --dias 7

    Cada linha do arquivo: <sigla_do_tribunal>:<numero_do_processo>
    Ex.: tjsp:00000000000000000000

A chave pública da API é lida da variável de ambiente DATAJUD_API_KEY;
se não existir, o script pede a chave. Obtenha a chave vigente na wiki
oficial do DataJud (página "Acesso" da API Pública). Ela não fica
gravada neste arquivo, porque o CNJ pode alterá-la.
"""

from __future__ import annotations

import argparse
import getpass
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests

URL_BASE = "https://api-publica.datajud.cnj.jus.br/api_publica_{tribunal}/_search"


def obter_chave() -> str:
    chave = os.environ.get("DATAJUD_API_KEY", "").strip()
    if not chave:
        chave = getpass.getpass("Chave pública da API DataJud (APIKey): ").strip()
    if chave.lower().startswith("apikey "):
        chave = chave[7:].strip()
    return chave


def somente_digitos(numero: str) -> str:
    return re.sub(r"\D", "", numero or "")


def consultar(chave: str, tribunal: str, numero: str) -> list[dict]:
    """Retorna a lista de registros (um por grau de jurisdição) do processo."""
    url = URL_BASE.format(tribunal=tribunal.strip().lower())
    headers = {"Authorization": f"APIKey {chave}", "Content-Type": "application/json"}
    corpo = {"query": {"match": {"numeroProcesso": somente_digitos(numero)}}}
    resposta = requests.post(url, headers=headers, json=corpo, timeout=30)
    if resposta.status_code != 200:
        raise RuntimeError(
            f"Erro HTTP {resposta.status_code} em {tribunal}. "
            f"Confira a chave e a sigla do tribunal. Resposta: {resposta.text[:300]}"
        )
    hits = resposta.json().get("hits", {}).get("hits", [])
    return [h.get("_source", {}) for h in hits]


def tabela_movimentos(registro: dict) -> pd.DataFrame:
    """Movimentações do registro, da mais recente para a mais antiga."""
    movs = pd.DataFrame(registro.get("movimentos", []))
    if movs.empty or "dataHora" not in movs:
        return pd.DataFrame(columns=["Data", "Movimentação"])
    movs["_dt"] = pd.to_datetime(movs["dataHora"], errors="coerce", format="mixed", utc=True)
    movs = movs.sort_values("_dt", ascending=False)
    return pd.DataFrame(
        {
            "_dt": movs["_dt"],
            "Data": movs["_dt"].dt.strftime("%d/%m/%Y %H:%M"),
            "Movimentação": movs.get("nome", pd.Series(dtype=str)),
        }
    ).reset_index(drop=True)


def resumo(registro: dict) -> dict:
    assuntos = [a.get("nome") for a in registro.get("assuntos", []) if isinstance(a, dict)]
    return {
        "Processo": registro.get("numeroProcesso"),
        "Grau": registro.get("grau"),
        "Classe": (registro.get("classe") or {}).get("nome"),
        "Órgão julgador": (registro.get("orgaoJulgador") or {}).get("nome"),
        "Ajuizamento": registro.get("dataAjuizamento"),
        "Assuntos": "; ".join(filter(None, assuntos)),
    }


def consulta_unica(chave: str, tribunal: str, numero: str, salvar_csv: bool = True) -> None:
    registros = consultar(chave, tribunal, numero)
    if not registros:
        print("⚠️ Processo não encontrado nesse tribunal (ou sob segredo de justiça).")
        return
    for reg in registros:
        print("\n" + "=" * 60)
        for campo, valor in resumo(reg).items():
            print(f"{campo + ':':<16} {valor}")
        tabela = tabela_movimentos(reg).drop(columns="_dt")
        print(f"\nMovimentações ({len(tabela)}):")
        print(tabela.to_string(index=False) if len(tabela) else "Nenhuma registrada.")
        if salvar_csv and len(tabela):
            arquivo = f"movimentos_{somente_digitos(numero)}_{reg.get('grau', '')}.csv"
            tabela.to_csv(arquivo, index=False, encoding="utf-8-sig")
            print(f"\n💾 Tabela salva em: {arquivo}")


def ler_lista(origem: str) -> list[tuple[str, str]]:
    """Lê pares tribunal:numero de um arquivo ou de texto (uma entrada por linha)."""
    texto = open(origem, encoding="utf-8").read() if os.path.isfile(origem) else origem
    pares = []
    for linha in texto.splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha:
            continue
        if ":" not in linha:
            print(f"Linha ignorada (use sigla:numero): {linha}", file=sys.stderr)
            continue
        tribunal, numero = linha.split(":", 1)
        pares.append((tribunal.strip().lower(), somente_digitos(numero)))
    return pares


def monitorar(chave: str, pares: list[tuple[str, str]], dias: int) -> str:
    """Gera relatório em Markdown com as movimentações dos últimos `dias` dias."""
    limite = datetime.now(timezone.utc) - timedelta(days=dias)
    linhas = [f"# Movimentações dos últimos {dias} dia(s)", ""]
    total = 0
    for tribunal, numero in pares:
        try:
            registros = consultar(chave, tribunal, numero)
        except Exception as erro:  # noqa: BLE001 - relatório deve seguir
            linhas += [f"## {tribunal.upper()} {numero}", f"❌ {erro}", ""]
            continue
        if not registros:
            linhas += [f"## {tribunal.upper()} {numero}", "⚠️ Não encontrado.", ""]
            continue
        for reg in registros:
            tab = tabela_movimentos(reg)
            recentes = tab[tab["_dt"] >= limite]
            info = resumo(reg)
            linhas.append(f"## {tribunal.upper()} {info['Processo']} ({info['Grau']})")
            linhas.append(f"{info['Classe']} · {info['Órgão julgador']}")
            linhas.append("")
            if recentes.empty:
                linhas += ["Sem movimentações novas.", ""]
                continue
            total += len(recentes)
            linhas += ["| Data | Movimentação |", "|---|---|"]
            linhas += [f"| {r.Data} | {r.Movimentação} |" for r in recentes.itertuples()]
            linhas.append("")
    linhas.insert(1, f"**{total}** movimentação(ões) nova(s) em {len(pares)} processo(s).")
    return "\n".join(linhas)


def main() -> None:
    parser = argparse.ArgumentParser(description="Consulta à API Pública do DataJud (CNJ)")
    parser.add_argument("--tribunal", help="sigla do tribunal: tjsp, tjrj, tjmg, trf1, stj...")
    parser.add_argument("--numero", help="número do processo, com ou sem pontuação")
    parser.add_argument("--lista", help="arquivo (ou texto) com linhas sigla:numero")
    parser.add_argument("--dias", type=int, default=7, help="janela do monitoramento")
    parser.add_argument("--saida", help="grava o relatório do monitoramento neste arquivo")
    args, _ = parser.parse_known_args()  # tolera argumentos extras do Colab/Jupyter

    chave = obter_chave()
    if not chave:
        sys.exit("❌ Chave da API não informada.")

    if args.lista:
        relatorio = monitorar(chave, ler_lista(args.lista), args.dias)
        print(relatorio)
        if args.saida:
            with open(args.saida, "a", encoding="utf-8") as f:
                f.write(relatorio + "\n")
        return

    print("=== Consulta DataJud (CNJ) ===")
    tribunal = args.tribunal or input("Sigla do tribunal (ex.: tjsp, tjrj, tjmg, trf1, stj): ")
    numero = args.numero or input("Número do processo (com ou sem pontuação): ")
    try:
        consulta_unica(chave, tribunal, numero)
    except (RuntimeError, requests.RequestException) as erro:
        print(f"❌ {erro}")


if __name__ == "__main__":
    main()
