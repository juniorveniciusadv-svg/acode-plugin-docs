# Skills do projeto

Skills importadas de repositórios públicos, sem alterações de conteúdo. Por estarem em `.claude/skills/`,
o Claude Code as carrega automaticamente como skills do projeto (invocáveis por `/nome-da-skill` ou por
linguagem natural).

As skills jurídicas apoiam o trabalho do advogado e não substituem a revisão, o julgamento e a
responsabilidade profissional. Normas, precedentes, prazos e cálculos devem sempre ser conferidos em
fonte oficial.

## Procedência e licenças

| Origem | Commit importado | Licença | Skills |
|---|---|---|---|
| [Matheus2306/claude-advocacia-brasil](https://github.com/Matheus2306/claude-advocacia-brasil) (plugin `advocacia-brasil` v1.0.0) | `4718a32` | MIT (declarada no `plugin.json`; o repositório não traz arquivo `LICENSE`) | 10 |
| [WrGDev/advogado-skills](https://github.com/WrGDev/advogado-skills) | `3f24714` | MIT (declarada no README; o repositório não traz arquivo `LICENSE`) | 5 |
| [thicazu-png/claude-skills-advocacia](https://github.com/thicazu-png/claude-skills-advocacia) | `bd089da` | MIT, © 2026 Thiago Cazú: ver [`LICENSE-thicazu-claude-skills-advocacia.txt`](LICENSE-thicazu-claude-skills-advocacia.txt) | 10 |
| [anthropics/skills](https://github.com/anthropics/skills) | `2c5958e` | Apache 2.0 (`LICENSE.txt` em cada pasta); componentes de terceiros em [`THIRD_PARTY_NOTICES-anthropic-skills.md`](THIRD_PARTY_NOTICES-anthropic-skills.md) | 19 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (seleção, localizada via skillsclaude.org) | `55d9399` | Conteúdo em CC BY 4.0 (exige atribuição; autor indicado na skill: "renat"); código em MIT: ver [`LICENSE-CONTENT-sickn33-agentic-awesome-skills.txt`](LICENSE-CONTENT-sickn33-agentic-awesome-skills.txt) e [`LICENSE-sickn33-agentic-awesome-skills.txt`](LICENSE-sickn33-agentic-awesome-skills.txt) | 1 |
| [PracticalSwan/agent-skills](https://github.com/PracticalSwan/agent-skills) (seleção) | `6cf6351` | MIT, © 2026 Sithu Win San: ver [`LICENSE-practicalswan-agent-skills.txt`](LICENSE-practicalswan-agent-skills.txt). `spreadsheet-formula-helper` vem de ComposioHQ/awesome-codex-skills (commit `0930e13`), segundo o registro do autor; a licença dessa origem não foi conferida | 2 |

## Catálogo

### Advocacia Brasil (Matheus2306)

| Skill | Finalidade |
|---|---|
| `triagem-estrategia-juridica` | Estruturação do caso, riscos, alternativas e diligências |
| `pesquisa-juridica-brasileira` | Legislação e jurisprudência verificadas em fontes oficiais |
| `organizar-fatos-provas` | Cronologia e matriz probatória |
| `elaborar-peticao-inicial` | Petição inicial completa e checklist de anexos |
| `elaborar-defesa-processual` | Contestação e matriz de impugnação |
| `elaborar-replica-manifestacao` | Réplica e manifestações específicas |
| `elaborar-recurso-juridico` | Cabimento e minuta recursal, contrarrazões e memoriais |
| `execucao-cumprimento-sentenca` | Estratégia executiva ou defensiva e cálculos |
| `revisar-peca-juridica` | Auditoria pré-protocolo por severidade |
| `gerenciar-prazos-providencias` | Controle de prazos internos/externos e providências |

### Advogado Brasileiro (WrGDev)

| Skill | Finalidade |
|---|---|
| `advogado` | Consultoria jurídica generalista |
| `peticao` | Petição inicial conforme o art. 319 do CPC |
| `contrato` | Redação e revisão de contratos |
| `recurso` | Recursos judiciais cíveis, penais e trabalhistas |
| `multa-transito` | Defesa da autuação e recursos à JARI e ao CETRAN |

### Claude Skills Advocacia (thicazu-png)

| Skill | Finalidade |
|---|---|
| `juridico-content-strategy` | Estratégia editorial e calendário de conteúdo jurídico |
| `oab-compliance-review` | Revisão de publicidade e sobriedade profissional |
| `legal-accuracy-review` | Checagem de precisão jurídica e de fontes |
| `multichannel-repurposing` | Adaptação de conteúdo para vários canais |
| `labor-law-business-content` | Conteúdo trabalhista empresarial |
| `digital-law-lgpd-ai-content` | Conteúdo sobre direito digital, LGPD e IA |
| `case-law-to-content` | Jurisprudência transformada em conteúdo |
| `visual-law-legal-design` | Visual Law e legal design |
| `business-tech-contract-review` | Revisão de contratos empresariais e de tecnologia |
| `legal-ops-ai-management` | Gestão de escritório com IA |

### Seleção de sickn33/agentic-awesome-skills

| Skill | Finalidade |
|---|---|
| `advogado-criminal` | Roteiro de pesquisa e verificação em direito penal brasileiro e na Lei Maria da Penha: enquadramento, materialidade e autoria, dosimetria estimada, questões processuais, teses, cenários e resumo para revisão profissional |

Atribuição (CC BY 4.0): skill `advogado-criminal` do repositório sickn33/agentic-awesome-skills, autoria indicada como "renat". Copiada sem modificações.

Não foi importada a `advogado-especialista`, do mesmo repositório, por dois motivos:

- ela se sobrepõe a `advogado` e a `pesquisa-juridica-brasileira`;
- o guia de referência dela tem imprecisão: atribui a competência do ITCMD sempre ao Estado do domicílio do falecido, quando, para imóveis, o imposto cabe ao Estado da situação do bem (CF, art. 155, § 1º, I).

### Seleção de PracticalSwan/agent-skills

| Skill | Finalidade |
|---|---|
| `document-metadata-review` | Verifica metadados, comentários, controle de alterações, links e conteúdo oculto em PDF, DOCX, PPTX e XLSX antes de compartilhar |
| `spreadsheet-formula-helper` | Escreve e corrige fórmulas de Excel e Google Sheets, com exemplos e casos-limite |

Das 253 skills do repositório, só estas duas foram importadas. Ficaram de fora:

- as de programação e de plataformas (Figma, Netlify, Vercel, MongoDB, HuggingFace e outras);
- as 8 duplicadas das da Anthropic;
- a família `avoid-ai-writing`/`humanizer`, calibrada para inglês segundo o próprio autor;
- `writing-guidelines`, que carrega regras de um site externo a cada uso;
- `doc` e `research`, que se sobrepõem a skills já existentes.

### Skills originais deste repositório

| Skill | Finalidade |
|---|---|
| `habilidades-profissionais-advocacia` | Soft skills aplicadas: negociação, comunicação com o cliente, ética, organização, delegação, tecnologia, argumentação, adaptação e plano de desenvolvimento |
| `revisao-formatacao-word` | Revisão editorial e formatação de documentos por estilos do Word, com entrega em quatro partes: texto revisado, especificação de formatação, resumo das alterações e pendências. Texto fornecido pelo dono do repositório. Acrescida da referência `references/padrao-profissional-edicao.md` (fluxo de edição em camadas, revisão de provas e checklist do editor), adaptada dos perfis O*NET 27-3041.00 *Editors* e 43-9081.00 *Proofreaders and Copy Markers* (USDOL/ETA, CC BY 4.0) e usada também por `editor-word-profissional` e `peticao-profissional-visual-law` |
| `peticao-profissional-visual-law` | Petições e manifestações com argumentação em camadas (norma, interpretação, doutrina, jurisprudência, aplicação, refutação, pedidos) e recursos de Visual Law sóbrios e acessíveis, com especificação para Word e checklist de protocolo. Escrita para este repositório |
| `avaliar-ferramenta-ia-juridica` | Avaliação neutra de ferramentas de IA para advocacia (generalistas, jurídicas especializadas, integradas à gestão, automação documental): diligência de sigilo e LGPD, adequação ao direito brasileiro, teste com casos reais anonimizados, custo total e piloto. Estrutura temática de artigo do blog ADVBOX, sem as recomendações comerciais |
| `leitura-pdf-extenso` | Leitura e análise de PDFs com centenas a milhares de páginas (autos completos), com o script `scripts/mapear_autos.py`, que mapeia texto por página, índice provável das peças (ID do PJe, assinatura), páginas para OCR e lotes numerados; leitura dirigida ou integral com fichamento em arquivo e citação de página. Script testado em PDF simulado de 2.100 páginas |
| `primeiros-passos-api-claude` | Guia em português para a primeira chamada à API do Claude (conta, autenticação pela CLI `ant` ou chave, cURL, CLI, Python, TypeScript), com cuidados de sigilo, LGPD, segurança da chave e custos, e recursos beta (cabeçalho `anthropic-beta`, cabeçalhos por endpoint como `managed-agents-2026-04-01`). Resume as páginas oficiais "Comece a usar o Claude" e "Cabeçalhos beta"; para detalhes técnicos, remete à skill `claude-api` |
| `copilot-revisao-codigo` | Guia para solicitar, configurar e personalizar a revisão de código do GitHub Copilot (GitHub.com, IDEs, CLI, API), com níveis de esforço, aprovações, instruções personalizadas, skills e MCP. Resume a documentação oficial do GitHub, fornecida pelo dono do repositório |
| `editor-word-profissional` | Revisão, edição e formatação de arquivos .docx em português brasileiro, com escopo diferenciado (revisão, edição, formatação ou trabalho completo) e trabalho sempre em nova versão. Texto fornecido pelo dono do repositório; **incompleto a partir da seção 3**, aguardando o restante |

Texto original, escrito para este repositório. Os temas foram identificados em artigos da Thomson Reuters Brasil, da Esade e da EPD, listados em `habilidades-profissionais-advocacia/references/fontes.md`, sem reprodução do conteúdo deles.

### Anthropic (anthropics/skills)

`academy-guide`, `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`,
`discernment-nudge`, `doc-coauthoring`, `docx`, `frontend-design`, `internal-comms`, `mcp-builder`,
`pdf`, `pptx`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`,
`webapp-testing`, `xlsx`.

Algumas dessas skills trazem scripts (Python, shell, JS) que dependem de ferramentas instaladas no
ambiente, como LibreOffice, Playwright e Node.
