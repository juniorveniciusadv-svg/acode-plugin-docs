---
name: peticao-profissional-visual-law
description: Planeja, redige e diagrama petições e manifestações processuais brasileiras com argumentação jurídica em camadas e recursos de Visual Law — quadros cronológicos, tabela fato-prova-consequência, quadros de precedentes, fluxogramas e sínteses —, sem sacrificar a formalidade, a fundamentação nem a admissibilidade, e entrega minuta, especificação de formatação para Word e checklist de protocolo. Use quando o usuário pedir uma petição, contestação, réplica, recurso ou memorial "profissional", "visual", "com visual law" ou "com quadros e tabelas", ou quiser converter uma peça existente para esse padrão.
---

# Petição profissional com Visual Law

Produzir peças tecnicamente sólidas cuja apresentação visual facilite a leitura do julgador. O recurso visual serve à compreensão do argumento; nunca substitui a fundamentação, a prova ou o pedido.

## 1. Antes de redigir

Levantar, perguntando apenas o indispensável:

- tipo de peça, juízo/tribunal, classe, número do processo e polo representado;
- prazo, termo inicial e forma de intimação (não calcular prazo final sem esses dados);
- fatos, documentos disponíveis e o que ainda falta provar;
- objetivo prático e pedidos pretendidos;
- normas internas do tribunal ou do escritório sobre formatação, tamanho de arquivo e sistema (PJe, e-SAJ, eproc, Projudi).

Se faltar dado não essencial, usar `[PREENCHER]`; se a falta puder alterar a estratégia, perguntar antes. Para casos complexos, aplicar antes `triagem-estrategia-juridica` e `organizar-fatos-provas`; para fontes, `pesquisa-juridica-brasileira`.

## 2. Plano argumentativo

Montar o plano antes do texto, com uma linha argumentativa central e capítulos que dialoguem entre si:

1. **Norma:** o que determinam a Constituição, a lei e o regulamento aplicáveis (lei + artigo + inciso/parágrafo/alínea).
2. **Interpretação:** como a norma deve ser compreendida (sistemática, teleológica, constitucional).
3. **Doutrina:** como a ciência jurídica estrutura o instituto — sem inventar autor, obra, edição, página ou citação literal; na dúvida, paráfrase identificando o autor ou a corrente.
4. **Jurisprudência:** precedentes qualificados primeiro (controle concentrado, repercussão geral, repetitivos, IRDR/IAC, súmulas), depois o tribunal competente; com número, órgão, relator e data apenas quando verificados.
5. **Aplicação concreta:** "A prova demonstra X. A norma determina Y. A jurisprudência interpreta Y assim. Logo, Z."
6. **Refutação:** a melhor objeção da parte contrária (steelman) e a resposta.
7. **Conclusão e pedidos:** cada tese relevante com consequência processual correspondente (principais, subsidiários, sucessivos, tutelas, provas).

## 3. Estrutura da peça

- endereçamento e qualificação (ou referência às partes já qualificadas);
- **síntese inicial** de até meia página: o que se pede e por quê (o "resumo executivo" do julgador);
- tempestividade, cabimento e preparo, quando pertinentes;
- fatos em ordem lógica, cada um ligado à prova (documento e folha/ID);
- fundamentos por capítulos, na ordem do plano argumentativo;
- tutela provisória, quando cabível (probabilidade, perigo, reversibilidade);
- pedidos numerados e coerentes com os fundamentos;
- provas e requerimentos finais;
- local, data, assinatura e índice de documentos.

## 4. Recursos de Visual Law

Usar somente quando acelerarem a compreensão. Cada recurso deve ter título, fonte (documento/ID) e ser retomado no texto.

| Recurso | Quando usar | Cuidado |
|---|---|---|
| Quadro cronológico | Sequência de fatos ou de atos processuais relevante para a tese (prazos, mora, prescrição) | Datas conferidas com os documentos |
| Tabela fato → prova → consequência jurídica | Vincular cada alegação à prova e ao efeito pretendido | Não afirmar fato sem prova indicada |
| Quadro de precedentes | Mostrar a aderência entre casos e o caso concreto | Só precedentes verificados; indicar distinções |
| Quadro comparativo | Cláusula × lei, cálculo do autor × cálculo correto, decisão × prova | Fonte de cada valor |
| Fluxograma | Procedimento, raciocínio de subsunção ou requisitos cumulativos | Simples; sem substituir a fundamentação |
| Destaques e caixas de síntese | Tese central de cada capítulo, data decisiva, pedido principal | No máximo um destaque por página |
| Imagens e capturas de tela | Trecho de documento, conversa ou laudo essencial | Legíveis, recortadas, com referência ao ID; respeitar sigilo e LGPD |

Regras de sobriedade e acessibilidade:

- linguagem formal e técnica; nada de ícones decorativos, emojis, cores vibrantes ou layout publicitário;
- legível impresso em preto e branco: não transmitir informação só pela cor;
- contraste adequado, fonte sem serifa ou com serifa sóbria, tamanho mínimo equivalente a 12 pt no corpo do texto;
- tabelas com cabeçalho repetido e sem células mescladas desnecessárias;
- texto alternativo em imagens e gráficos quando o documento for gerado digitalmente;
- conferir limites do sistema do tribunal (tamanho de arquivo, PDF pesquisável, imagens) antes do protocolo.

## 5. Formatação para Word

Usar estilos nativos, não formatação manual:

- **Título** (nome da peça), **Título 1** (capítulos), **Título 2** (subcapítulos), **Normal** (corpo), **Citação** (transcrições), **Legenda** (quadros e figuras numerados);
- padrão sugerido, se não houver modelo do escritório: margens 3 cm (esq./sup.) e 2 cm (dir./inf.), corpo 12 pt, espaçamento 1,5, recuo de primeira linha 1,25 cm, citações longas com recuo de 4 cm e 10–11 pt — informar que é sugestão;
- numeração de páginas no rodapé, cabeçalho com processo e partes a partir da segunda página, sumário automático em peças longas;
- quebras de página e de seção em vez de linhas em branco.

Quando o usuário pedir o arquivo `.docx`, usar a skill `docx` (ou equivalente disponível) para gerá-lo e informar apenas o que foi efetivamente aplicado. Para padronização editorial do texto, pode-se combinar com `revisao-formatacao-word`.

## 6. Conferência final

Antes de entregar, verificar:

- a conclusão decorre das premissas? há salto lógico ou argumento circular?
- legislação vigente e jurisprudência verificadas sustentam o que se afirma?
- cada fato tem prova indicada e cada quadro tem fonte?
- cada tese tem pedido correspondente? há pedido sem fundamento?
- os recursos visuais ajudam ou apenas enfeitam? retirar os que não acrescentam;
- competência, legitimidade, interesse, adequação da via, tempestividade e preparo foram enfrentados?

Para auditoria pré-protocolo completa, aplicar `revisar-peca-juridica`.

## Entrega

1. Minuta da peça, com os quadros inseridos no ponto do texto em que são usados.
2. Especificação de formatação para Word.
3. Índice dos recursos visuais (número, título, fonte).
4. Premissas, campos `[PREENCHER]`/`[CONFERIR]` e documentos faltantes.
5. Riscos e objeções previsíveis.
6. Checklist de protocolo.

## Regras absolutas

- Nunca inventar fato, documento, número de processo, precedente, ementa, tese, doutrina ou citação.
- Sinalizar como `[CONFERIR]` toda informação que dependa de verificação em fonte oficial.
- O visual não pode ocultar fragilidade argumentativa: se a tese for fraca, dizê-lo ao advogado.
- A peça é minuta para revisão e responsabilidade do advogado.
