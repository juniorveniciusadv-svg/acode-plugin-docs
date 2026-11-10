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

### Skill original deste repositório

| Skill | Finalidade |
|---|---|
| `habilidades-profissionais-advocacia` | Soft skills aplicadas: negociação, comunicação com o cliente, ética, organização, delegação, tecnologia, argumentação, adaptação e plano de desenvolvimento |

Texto original, escrito para este repositório. Os temas foram identificados em artigos da Thomson Reuters Brasil, da Esade e da EPD, listados em `habilidades-profissionais-advocacia/references/fontes.md`, sem reprodução do conteúdo deles.

### Anthropic (anthropics/skills)

`academy-guide`, `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`,
`discernment-nudge`, `doc-coauthoring`, `docx`, `frontend-design`, `internal-comms`, `mcp-builder`,
`pdf`, `pptx`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`,
`webapp-testing`, `xlsx`.

Algumas dessas skills trazem scripts (Python, shell, JS) que dependem de ferramentas instaladas no
ambiente, como LibreOffice, Playwright e Node.
