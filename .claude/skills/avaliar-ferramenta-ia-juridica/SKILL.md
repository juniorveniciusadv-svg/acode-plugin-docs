---
name: avaliar-ferramenta-ia-juridica
description: Avalia e compara, de forma neutra, ferramentas de inteligência artificial para escritórios de advocacia e departamentos jurídicos — assistentes generalistas, IAs jurídicas especializadas (pesquisa, jurimetria, produção de peças), IAs integradas a sistemas de gestão (intimações, prazos, dados internos) e automação de documentos, contratos e assinatura —, com diligência de sigilo profissional e LGPD, teste com casos reais anonimizados, análise de custo total e plano de piloto. Use quando o usuário perguntar qual IA contratar, pedir comparação entre ferramentas jurídicas, quiser avaliar uma proposta comercial ou montar critérios de escolha.
---

# Avaliação de ferramentas de IA jurídica

Ajudar o advogado a escolher a ferramenta certa para um problema concreto, com base em evidência e não em promessa comercial. O resultado é uma recomendação fundamentada e um piloto mensurável, não a indicação de uma marca.

## Regras

- **Neutralidade:** não recomendar fornecedor por reputação, publicidade ou conteúdo produzido pelo próprio fornecedor. Materiais de fornecedor são fonte de alegações a verificar, não de conclusões.
- **Dados mutáveis:** preços, planos, recursos, integrações e políticas de dados mudam com frequência. Conferir no site e nos termos atuais do fornecedor, com data de acesso, antes de afirmar. Marcar `[CONFERIR]` o que não for verificado.
- **Alegações de desempenho** (precisão, economia de tempo, número de decisões na base) são declarações do fornecedor até prova em contrário: pedir metodologia, amostra e período, ou medir no piloto.
- **Conformidade:** não declarar que uma ferramenta está em conformidade com a LGPD ou com as normas da OAB. Indicar o que foi verificado e o que falta.

## 1. Definir o problema antes da ferramenta

Identificar a tarefa e o resultado esperado. A categoria decorre da tarefa:

| Tarefa | Categoria provável | Pergunta-chave |
|---|---|---|
| Rascunho, resumo, organização de ideias, revisão de linguagem | Assistente generalista (Claude, ChatGPT, Gemini, Copilot) | O resultado passará por revisão humana integral? |
| Pesquisa de jurisprudência, jurimetria, tendências de tribunais | IA jurídica especializada de pesquisa | A base cobre os tribunais e o período de que o escritório precisa, com link para o inteiro teor oficial? |
| Produção de petições, contratos e recursos | IA jurídica de redação | Usa os modelos e o padrão do escritório? Cita fontes verificáveis? |
| Leitura de intimações, prazos, tarefas, dados de processos e financeiro | IA integrada ao sistema de gestão | Lê os dados onde eles já estão, ou exige copiar e colar? Quem confere o prazo? |
| Modelos, ciclo de vida de contratos, assinatura eletrônica | Automação documental, CLM, assinatura | Fecha o ciclo com a gestão (gera, envia, registra o retorno)? Qual o nível de certificação da assinatura? |

Se a tarefa for de alto risco (prazo, cálculo, tese em peça a protocolar), a ferramenta só apoia: a conferência humana continua obrigatória.

## 2. Diligência de segurança, sigilo e LGPD

Levantar por escrito, com o documento do fornecedor que comprova cada resposta:

- **Uso dos dados:** os dados do escritório são usados para treinar modelos? Há opção contratual de exclusão? Quanto tempo ficam retidos? Podem ser apagados sob pedido?
- **Contrato:** há termo de tratamento de dados (DPA) com papéis de controlador e operador definidos? Lista de suboperadores? Prazo de comunicação de incidentes?
- **Localização:** onde os dados são armazenados e processados? Há transferência internacional? Se houver, sob qual mecanismo previsto na LGPD (art. 33 — conferir a redação e a regulamentação vigentes da ANPD)?
- **Segurança:** criptografia em trânsito e em repouso, controle de acesso por usuário, autenticação forte, registro de atividades, certificações e auditorias independentes informadas.
- **Saída:** é possível exportar todos os dados em formato aberto ao encerrar o contrato?
- **Sigilo profissional:** a inviolabilidade do sigilo é dever do advogado (Estatuto da Advocacia, Lei 8.906/1994, e Código de Ética e Disciplina da OAB — conferir dispositivos e eventuais orientações recentes da OAB sobre uso de IA). Avaliar se o arranjo permite cumprir esse dever, inclusive para processos em segredo de justiça.
- **Ferramentas gratuitas ou de uso pessoal:** em regra inadequadas para dados de clientes, salvo termos que garantam não uso para treinamento e controle de retenção.

## 3. Adequação ao Direito brasileiro

- A ferramenta conhece legislação, jurisprudência e terminologia brasileiras atuais, ou foi construída sobretudo com conteúdo estrangeiro?
- Indica a fonte de cada citação, com link para a fonte oficial (Planalto, tribunais, Diário Oficial)?
- Como trata vigência, alterações legislativas e precedentes superados?
- Ferramentas estrangeiras de revisão contratual podem ter bom desempenho em inglês e baixo em contratos regidos pela lei brasileira: testar com contratos nacionais.

## 4. Teste com casos reais

Antes de contratar, montar um teste curto e comparável:

1. Selecionar de 10 a 20 casos reais **anonimizados**, representativos da tarefa, com resposta correta conhecida (gabarito do próprio escritório).
2. Submeter os mesmos casos a cada ferramenta candidata, nas mesmas condições.
3. Medir:

| Métrica | Como medir |
|---|---|
| Acerto | Respostas corretas ÷ total, contra o gabarito |
| Alucinação | Citações de lei, súmula ou julgado inexistentes ou deturpadas (conferir uma a uma na fonte oficial) |
| Rastreabilidade | Percentual de afirmações com fonte verificável |
| Erro crítico | Prazo errado, valor errado, parte errada, pedido omitido |
| Tempo líquido | Tempo da ferramenta mais o tempo de conferência humana, comparado ao trabalho sem a ferramenta |

4. Um único erro crítico em tarefa de prazo ou valor desclassifica o uso sem conferência humana integral.

Para conferir citações, usar `pesquisa-juridica-brasileira` e, se disponível, uma skill de validação de fontes.

## 5. Integração e custo total

- **Integração:** cada etapa manual de copiar e colar entre sistemas consome o tempo que a IA deveria economizar e aumenta o risco de vazamento ou erro. Verificar integrações nativas e API.
- **Custo total:** licenças por usuário, consumo por uso (tokens, créditos, documentos), implantação, treinamento, tempo de conferência e custo de saída (dependência do fornecedor).
- **Combinação:** muitas vezes a melhor solução combina categorias (por exemplo, um assistente generalista para apoio, uma base especializada para pesquisa e a automação da gestão para prazos). Evitar sobreposição paga de funções.

## 6. Decisão e piloto

1. Matriz comparativa com pesos definidos **antes** do teste:

| Critério | Peso | Ferramenta A | Ferramenta B | Observação |
|---|---|---|---|---|
| Segurança, sigilo e LGPD | | | | |
| Adequação ao Direito brasileiro | | | | |
| Qualidade medida no teste | | | | |
| Integração com a rotina | | | | |
| Custo total | | | | |

2. Piloto de 30 a 60 dias com um grupo pequeno, métricas definidas e um responsável.
3. Política interna de uso: tarefas permitidas e proibidas, dados que podem ou não ser inseridos, revisão humana obrigatória, registro de uso nas entregas relevantes. Para estruturar a governança, pode-se combinar com `legal-ops-ai-management`.
4. Reavaliação ao fim do piloto: manter, ajustar ou descontinuar.

## Entrega

1. Problema e categoria de ferramenta indicada.
2. Quadro de diligência (segurança, sigilo, LGPD) por candidata, com a fonte de cada resposta e a data de acesso.
3. Resultado do teste ou roteiro do teste a aplicar.
4. Matriz comparativa e recomendação condicionada às premissas.
5. Riscos, pendências `[CONFERIR]` e plano de piloto.

## Fonte temática

A taxonomia de categorias e os critérios de escolha foram organizados a partir do artigo "Ferramentas de IA para Advogados: Tipos, usos e como escolher", de Eduardo Koetz (blog ADVBOX, 27/08/2026), fornecido pelo usuário. O artigo é de fornecedor e promove os próprios produtos; esta skill usa apenas a estrutura temática, não reproduz o texto e não incorpora as recomendações comerciais.
