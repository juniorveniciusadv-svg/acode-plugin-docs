# Modelo de pedido: cronologia e padrões em documentos volumosos

Roteiro para pedir ao Claude cronologia, análise de padrões e identificação de provas a partir de um grande volume de documentos (autos, documentos do cliente, e-mails, planilhas). Adaptado ao processo brasileiro a partir do guia "Track discovery timelines and analyze patterns", da galeria de casos de uso da Claude Academy (Anthropic). O guia original trata do *discovery* norte-americano, que não tem equivalente direto no Brasil; aqui ele foi convertido para autos, instrução probatória e documentos do caso.

## 1. Estrutura do pedido (três blocos)

**Bloco 1 — Contexto do caso**

- Quem o escritório representa e qual é o polo (autor, réu, terceiro).
- Tipo de ação ou disputa, juízo e fase processual.
- Partes e pessoas relevantes (sem dados pessoais desnecessários).
- Volume e tipos de documentos: autos em PDF, contratos, e-mails, planilhas, atas, laudos.
- Período coberto pelos fatos.

**Bloco 2 — Entregas pedidas**

- Cronologia com referência a cada documento (página do PDF, ID do PJe, folhas ou nome do arquivo).
- Padrões e divergências: mudanças de escopo sem aditivo formal, atrasos recorrentes, versões conflitantes, comunicações que contradizem documentos formais.
- As provas mais fortes e as mais frágeis de cada lado.
- Pessoas-chave para depoimento pessoal ou prova testemunhal, com o que cada uma pode esclarecer.
- Lacunas: documentos mencionados que não estão nos autos, períodos sem registro.

**Bloco 3 — Formato**

- Pedir expressamente **memorando jurídico**, em seções e com referência ao documento em cada afirmação. Sem esse pedido, a saída tende a ser informal.
- Indicar destinatário (sócio, colega, cliente) e nível de formalidade, ou o modelo do escritório.
- Se o resultado for um arquivo, pedir `.docx` e usar a skill `docx`. Para diagramação, combinar com `revisao-formatacao-word`.

## 2. Perguntas de acompanhamento úteis

- "Extraia as passagens dos e-mails que tratam de atraso, agrupadas por marco do contrato, com citação literal e referência."
- "Condense a análise em uma página para o sócio responsável, com conclusão, três provas principais e riscos."
- "Aprofunde as alterações de escopo feitas sem aditivo: data, quem pediu, quem aceitou e onde está o registro."
- "Liste os fatos alegados pela parte contrária que nenhum documento sustenta."

## 3. Conferência antes de usar em peça ou comunicação ao cliente

- [ ] Cada referência (página, ID, folhas, nome do arquivo) confere com o índice dos autos ou do acervo.
- [ ] Cada data confere com o documento de origem e com a cronologia do processo.
- [ ] Cada citação literal confere palavra por palavra.
- [ ] Nenhum evento-chave ficou de fora (comparar com o índice e com o relato do cliente).
- [ ] O que não pôde ser confirmado está marcado `[CONFERIR]`.

O Claude acelera a revisão, mas não substitui a conferência do advogado.

## 4. Sigilo

- Antes de enviar, anonimizar ou retirar dados especialmente sensíveis (segredo comercial, dados pessoais sensíveis, dados de menores, processos em segredo de justiça), ou trabalhar só com a parte não sigilosa.
- Se os documentos estiverem em serviços conectados (por exemplo, conectores de e-mail ou de armazenamento em nuvem), conectar apenas as pastas e caixas necessárias ao caso.
- Verificar os termos de uso e de privacidade aplicáveis à conta e ao plano. Para escolher ferramentas, ver a skill `avaliar-ferramenta-ia-juridica`.

## Fonte

Claude Academy (Anthropic), guia "Track discovery timelines and analyze patterns" (https://academy.claude.com/use-cases/track-discovery-timelines-and-analyze-patterns), consultado em 10/11/2026, e lição "Claude in action: use-cases by role" do curso Claude 101. Conteúdo resumido e adaptado ao contexto brasileiro, sem reprodução do texto original.
