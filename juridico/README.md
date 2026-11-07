# Kit Jurídico: DataJud, Termux, Colab e GitHub Actions

Roteiro prático com links clicáveis. O mesmo script (`datajud.py`) funciona em todos os ambientes.

| Ambiente | Quando usar |
|---|---|
| **Google Colab** | Aprender e testar com dados públicos, sem instalar nada |
| **Termux (Android)** | Dados sigilosos e uso offline: tudo fica no aparelho |
| **GitHub Actions** | Monitoramento automático diário, sem celular ou computador ligado |

> **Chave da API:** a chave pública vigente fica na wiki oficial do DataJud:
> <https://datajud-wiki.cnj.jus.br/api-publica/acesso>.
> Ela não fica gravada nos arquivos porque o CNJ pode alterá-la.

---

## Etapa 1: Google Colab (1 clique)

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juniorveniciusadv-svg/acode-plugin-docs/blob/ccr-3b8c9989-psikde/juridico/DataJud_Consulta.ipynb)

1. Abra o link acima e entre com sua conta Google.
2. Toque em ▶️ na **célula 1** e depois na **célula 2**.
3. Informe a chave, a sigla do tribunal (`tjsp`, `tjrj`, `tjmg`, `trf1`, `stj`...) e o número do processo.

⚠️ O Colab roda nos servidores do Google: use apenas dados públicos.

---

## Etapa 2: Termux (1 comando)

Cole no Termux:

```bash
curl -fsSLo ~/setup-termux.sh https://raw.githubusercontent.com/juniorveniciusadv-svg/acode-plugin-docs/ccr-3b8c9989-psikde/juridico/setup-termux.sh && bash ~/setup-termux.sh
```

O comando instala o Debian, o Python, o Pandas e o Requests (se já estiverem instalados, ele só confere), baixa o `datajud.py` e cria os atalhos abaixo. Feche e reabra o Termux depois.

| Atalho | Efeito |
|---|---|
| `datajud` | Consulta um processo |
| `juridico` | Entra no Debian, com Python e Pandas |
| `exit` | Sai do Debian |

---

## Etapa 3: monitoramento automático (GitHub Actions)

O monitoramento consulta seus processos todo dia útil e mostra as movimentações novas na aba **Actions**.

> ⚠️ **Use um repositório PRIVADO.** Em repositório público, o resultado das execuções fica visível para qualquer pessoa. Este repositório é público, por isso o monitoramento não está ativado aqui.

1. **Crie um repositório privado:** <https://github.com/new>. Marque **Private** e dê um nome, como `monitor-processos`.
2. **Copie dois arquivos** para o repositório novo, mantendo estes caminhos:
   - [`datajud.py`](https://raw.githubusercontent.com/juniorveniciusadv-svg/acode-plugin-docs/ccr-3b8c9989-psikde/juridico/datajud.py) → `juridico/datajud.py`
   - [`monitor-datajud.yml`](https://raw.githubusercontent.com/juniorveniciusadv-svg/acode-plugin-docs/ccr-3b8c9989-psikde/juridico/monitor-datajud.yml) → `.github/workflows/monitor-datajud.yml`

   No GitHub: **Add file → Create new file**, digite o caminho completo no nome e cole o conteúdo.
3. **Cadastre dois secrets** (Settings → Secrets and variables → Actions → New repository secret):

   | Nome | Conteúdo |
   |---|---|
   | `DATAJUD_API_KEY` | A chave pública da wiki do DataJud |
   | `DATAJUD_PROCESSOS` | Um processo por linha, no formato `sigla:numero` |

   Exemplo do conteúdo de `DATAJUD_PROCESSOS` (números fictícios):

   ```
   tjsp:0000000-00.0000.8.26.0000
   trf1:0000000-00.0000.4.01.0000
   ```
4. **Teste:** aba **Actions** → **Monitor DataJud** → **Run workflow**. Depois, abra a execução para ver o relatório.

A partir daí, a rotina roda sozinha de segunda a sexta, às 07h17 (horário de Brasília).

---

## Etapa 4: aplicativos de estudo e organização (Play Store)

| App | Para quê | Link |
|---|---|---|
| Obsidian | Segundo cérebro: teses e julgados em Markdown | [Play Store](https://play.google.com/store/apps/details?id=md.obsidian) |
| AnkiDroid | Repetição espaçada: precedentes, prazos, sintaxe | [Play Store](https://play.google.com/store/apps/details?id=com.ichi2.anki) |
| Zotero | Bibliografia doutrinária e PDFs anotados | [Play Store](https://play.google.com/store/apps/details?id=org.zotero.android) |

---

## Etapa 5: quando tiver um computador

VS Code, Docker, Ollama (IA local), n8n e Docling exigem Windows, Mac ou Linux. O `datajud.py` roda lá sem alteração.

---

## Uso do script por linha de comando

```bash
python3 datajud.py                                   # interativo
python3 datajud.py --tribunal tjsp --numero 0000000-00.0000.8.26.0000
python3 datajud.py --lista processos.txt --dias 7    # vários processos
```

A API Pública do DataJud devolve apenas metadados públicos (classe, assuntos, órgão julgador, movimentações). Processos em segredo de justiça não aparecem.
