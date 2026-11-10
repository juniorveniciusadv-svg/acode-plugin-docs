#!/usr/bin/env python3
"""Mapeia um PDF extenso (ex.: autos com milhares de páginas) para leitura por partes.

Uso:
    python3 mapear_autos.py ARQUIVO.pdf --saida PASTA [--lote 50]

Gera, em PASTA:
    paginas.jsonl  - uma linha JSON por página: número, quantidade de caracteres,
                     indicação de página sem texto (precisa de OCR), marcadores
                     detectados (tipo de peça, ID/página do PJe, assinatura, evento,
                     folhas, primeira data) e a primeira linha do texto.
    lotes/         - o texto do PDF dividido em arquivos de N páginas, com o número
                     de cada página marcado ("===== PÁGINA 37 =====").
    indice.md      - índice provável das peças, faixas de páginas sem texto e
                     estatísticas, para orientar a leitura dirigida.

Extrai o texto com `pdftotext` (Poppler) quando disponível, que separa páginas por
form feed; senão usa `pypdf`. Não envia nada para a internet. Não faz OCR: apenas
aponta as páginas que precisam dele.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

MIN_CARACTERES = 30  # abaixo disso, a página provavelmente é imagem sem camada de texto
LINHAS_CABECALHO = 15  # tipo de peça é procurado só nas primeiras linhas da página

TIPOS_PECA = [
    ("peticao inicial", r"peti[cç][aã]o\s+inicial"),
    ("contestacao", r"\bcontesta[cç][aã]o\b"),
    ("reconvencao", r"\breconven[cç][aã]o\b"),
    ("replica", r"\br[eé]plica\b"),
    ("impugnacao", r"\bimpugna[cç][aã]o\b"),
    ("embargos de declaracao", r"embargos\s+de\s+declara[cç][aã]o"),
    ("embargos a execucao", r"embargos\s+[aà]\s+execu[cç][aã]o"),
    ("apelacao", r"\bapela[cç][aã]o\b"),
    ("contrarrazoes", r"\bcontra[- ]?raz[oõ]es\b"),
    ("agravo", r"\bagravo\b"),
    ("recurso especial", r"recurso\s+especial"),
    ("recurso extraordinario", r"recurso\s+extraordin[aá]rio"),
    ("recurso ordinario", r"recurso\s+ordin[aá]rio"),
    ("sentenca", r"\bsenten[cç]a\b"),
    ("acordao", r"\bac[oó]rd[aã]o\b"),
    ("decisao", r"\bdecis[aã]o\b"),
    ("despacho", r"\bdespacho\b"),
    ("laudo", r"\blaudo\b"),
    ("parecer", r"\bparecer\b"),
    ("ata/termo de audiencia", r"(ata|termo)\s+de\s+audi[eê]ncia"),
    ("procuracao", r"\bprocura[cç][aã]o\b"),
    ("certidao", r"\bcertid[aã]o\b"),
    ("mandado", r"\bmandado\b"),
    ("manifestacao", r"\bmanifesta[cç][aã]o\b"),
    ("calculos", r"(mem[oó]ria\s+de\s+c[aá]lculo|planilha\s+de\s+c[aá]lculo|c[aá]lculos?\s+de\s+liquida[cç][aã]o)"),
    ("alvara", r"\balvar[aá]\b"),
    ("oficio", r"\bof[ií]cio\b"),
]
TIPOS_RE = [(nome, re.compile(rx, re.IGNORECASE)) for nome, rx in TIPOS_PECA]

PJE_RE = re.compile(r"Num\.\s*(\d{5,})\s*-\s*P[aá]g\.\s*(\d+)", re.IGNORECASE)
ASSINATURA_RE = re.compile(
    r"Assinado\s+eletronicamente\s+por:?\s*(.+?)\s*-\s*(\d{2}/\d{2}/\d{4})", re.IGNORECASE
)
EVENTO_RE = re.compile(r"\bEvento\s+(\d+)\b", re.IGNORECASE)
FOLHAS_RE = re.compile(r"\bfls?\.\s*(\d{1,5})\b", re.IGNORECASE)
DATA_RE = re.compile(r"\b(\d{2}/\d{2}/\d{4})\b")


def contar_paginas(pdf: Path) -> int:
    if shutil.which("pdfinfo"):
        saida = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=False)
        m = re.search(r"^Pages:\s+(\d+)", saida.stdout, re.MULTILINE)
        if m:
            return int(m.group(1))
    from pypdf import PdfReader

    return len(PdfReader(str(pdf)).pages)


def extrair_paginas(pdf: Path, total: int):
    """Gera (numero_pagina, texto) para cada página, na ordem."""
    if shutil.which("pdftotext"):
        proc = subprocess.run(
            ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"],
            capture_output=True,
            check=False,
        )
        if proc.returncode == 0:
            partes = proc.stdout.decode("utf-8", errors="replace").split("\f")
            # pdftotext termina com um form feed após a última página
            if len(partes) == total + 1 and not partes[-1].strip():
                partes = partes[:-1]
            if len(partes) == total:
                for i, texto in enumerate(partes, start=1):
                    yield i, texto
                return
            print(
                f"Aviso: pdftotext devolveu {len(partes)} partes para {total} páginas; usando pypdf.",
                file=sys.stderr,
            )
    from pypdf import PdfReader

    leitor = PdfReader(str(pdf))
    for i, pagina in enumerate(leitor.pages, start=1):
        try:
            texto = pagina.extract_text() or ""
        except Exception as erro:  # noqa: BLE001 - página corrompida não deve interromper o mapeamento
            print(f"Aviso: falha ao extrair a página {i}: {erro}", file=sys.stderr)
            texto = ""
        yield i, texto


def sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def analisar(numero: int, texto: str) -> dict:
    limpo = texto.strip()
    linhas = [l.strip() for l in limpo.splitlines() if l.strip()]
    cabecalho = sem_acento(" ".join(linhas[:LINHAS_CABECALHO]))
    tipos = [nome for nome, rx in TIPOS_RE if rx.search(cabecalho)]
    registro = {
        "pagina": numero,
        "caracteres": len(limpo),
        "sem_texto": len(limpo) < MIN_CARACTERES,
        "tipos_provaveis": tipos,
        "primeira_linha": linhas[0][:160] if linhas else "",
    }
    if m := PJE_RE.search(texto):
        registro["pje_id"] = m.group(1)
        registro["pje_pagina_doc"] = int(m.group(2))
    if m := ASSINATURA_RE.search(texto):
        registro["assinado_por"] = re.sub(r"\s+", " ", m.group(1))[:120]
        registro["assinado_em"] = m.group(2)
    if m := EVENTO_RE.search(texto):
        registro["evento"] = int(m.group(1))
    if m := FOLHAS_RE.search(texto):
        registro["fls"] = int(m.group(1))
    if m := DATA_RE.search(texto):
        registro["primeira_data"] = m.group(1)
    return registro


def inicio_de_documento(reg: dict, ultimo_pje_id: str | None) -> bool:
    """`ultimo_pje_id` é o ID da última página anterior que tinha ID do PJe (páginas
    sem texto no meio de um documento não devem gerar um falso início)."""
    if reg.get("pje_pagina_doc") == 1:
        return True
    if "pje_id" in reg and ultimo_pje_id is not None and reg["pje_id"] != ultimo_pje_id:
        return True
    return "pje_id" not in reg and not reg["sem_texto"] and bool(reg["tipos_provaveis"])


def faixas(numeros: list[int]) -> list[str]:
    res, inicio, fim = [], None, None
    for n in numeros:
        if inicio is None:
            inicio = fim = n
        elif n == fim + 1:
            fim = n
        else:
            res.append(f"{inicio}" if inicio == fim else f"{inicio}-{fim}")
            inicio = fim = n
    if inicio is not None:
        res.append(f"{inicio}" if inicio == fim else f"{inicio}-{fim}")
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--saida", type=Path, required=True, help="pasta de saída (será criada)")
    ap.add_argument("--lote", type=int, default=50, help="páginas por arquivo de lote (padrão: 50)")
    args = ap.parse_args()

    if not args.pdf.is_file():
        print(f"Arquivo não encontrado: {args.pdf}", file=sys.stderr)
        return 2
    if args.lote < 1:
        print("--lote deve ser maior que zero", file=sys.stderr)
        return 2

    try:
        total = contar_paginas(args.pdf)
    except Exception as erro:  # noqa: BLE001 - PDF corrompido ou protegido por senha
        print(f"Não foi possível abrir o PDF ({erro}). Se estiver protegido por senha, peça a versão sem proteção.", file=sys.stderr)
        return 2
    pasta_lotes = args.saida / "lotes"
    try:
        pasta_lotes.mkdir(parents=True, exist_ok=True)
    except OSError as erro:
        print(f"Não foi possível criar a pasta de saída {args.saida}: {erro}", file=sys.stderr)
        return 2

    registros: list[dict] = []
    lote_atual: list[str] = []
    lote_inicio = 1

    def gravar_lote(fim: int) -> None:
        indice_lote = (lote_inicio - 1) // args.lote + 1
        nome = f"lote-{indice_lote:04d}_p{lote_inicio:05d}-{fim:05d}.txt"
        (pasta_lotes / nome).write_text("".join(lote_atual), encoding="utf-8")

    with open(args.saida / "paginas.jsonl", "w", encoding="utf-8") as jsonl:
        for numero, texto in extrair_paginas(args.pdf, total):
            lote_atual.append(f"===== PÁGINA {numero} =====\n{texto.rstrip()}\n\n")
            reg = analisar(numero, texto)
            registros.append(reg)
            jsonl.write(json.dumps(reg, ensure_ascii=False) + "\n")
            if numero % args.lote == 0 or numero == total:
                gravar_lote(numero)
                lote_atual = []
                lote_inicio = numero + 1

    sem_texto = [r["pagina"] for r in registros if r["sem_texto"]]
    documentos = []
    ultimo_pje_id = None
    for reg in registros:
        if inicio_de_documento(reg, ultimo_pje_id):
            documentos.append(reg)
        if "pje_id" in reg:
            ultimo_pje_id = reg["pje_id"]

    linhas = [
        f"# Índice provável — {args.pdf.name}",
        "",
        f"- Páginas: {total}",
        f"- Páginas sem texto (precisam de OCR): {len(sem_texto)}",
        f"- Inícios de documento detectados: {len(documentos)}",
        f"- Lotes: {(total + args.lote - 1) // args.lote} arquivos de até {args.lote} páginas em `lotes/`",
        "",
        "Detecção automática por padrões de texto: confirmar cada item na página indicada antes de citá-lo.",
        "",
        "## Peças e documentos",
        "",
        "| Página | Tipo provável | ID PJe | Assinado por | Data | Primeira linha |",
        "|---:|---|---|---|---|---|",
    ]
    for d in documentos:
        primeira = d["primeira_linha"].replace("|", "/")
        linhas.append(
            f"| {d['pagina']} | {', '.join(d['tipos_provaveis']) or '—'} | {d.get('pje_id', '—')} | "
            f"{d.get('assinado_por', '—')} | {d.get('assinado_em', d.get('primeira_data', '—'))} | {primeira} |"
        )
    linhas += ["", "## Páginas sem texto (OCR necessário)", ""]
    linhas.append(", ".join(faixas(sem_texto)) if sem_texto else "Nenhuma.")
    (args.saida / "indice.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")

    print(
        f"{total} páginas mapeadas; {len(documentos)} inícios de documento; "
        f"{len(sem_texto)} páginas sem texto. Saída em {args.saida}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
