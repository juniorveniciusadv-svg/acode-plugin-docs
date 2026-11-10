# Questionário de segurança para fornecedores de IA jurídica

## Sumário

1. Como usar
2. Identificação do fornecedor
3. Blocos 1 a 10: contrato e uso de dados; infraestrutura e segurança; controles administrativos; isolamento por processo ou cliente; precisão e verificação; operação e custos; integração; personalização; encerramento e portabilidade; perguntas próprias do escritório
4. Matriz de pontuação
5. Sinais de alerta
6. Fonte e licença

## 1. Como usar

1. Enviar ao fornecedor e exigir respostas **por escrito**, com indicação da cláusula ou do documento que comprova cada uma.
2. Revisar as respostas com o responsável por TI e com o sócio ou advogado responsável.
3. Pontuar na matriz (seção 4) e verificar os sinais de alerta (seção 5).
4. Pilotar em escopo controlado, com critérios definidos, antes de decidir (ver o passo 6 da skill).

A coluna "Resposta esperada" indica o mínimo aceitável para uso com dados de clientes.

## 2. Identificação do fornecedor

- Razão social, CNPJ ou registro estrangeiro, sede e forma societária.
- Ano de fundação e controle societário.
- Encarregado de dados (DPO) e canal de contato.
- Modelos de IA de terceiros que a solução utiliza.

## Bloco 1 — Contrato e uso de dados

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 1.1 | O contrato proíbe usar entradas e saídas do escritório para treinar ou aprimorar modelos? | Sim, por escrito |
| 1.2 | Em qual cláusula está essa proibição? | Referência exata |
| 1.3 | Há planos ou modos (gratuito, teste, beta) em que a proibição não vale? | Não, ou divulgação completa |
| 1.4 | Os dados são compartilhados com provedores de modelos, suboperadores ou parceiros? Quais? | Lista completa de suboperadores |
| 1.5 | Qual o prazo padrão de retenção de prompts e respostas? | Prazo definido; opção de retenção zero preferível |
| 1.6 | É possível configurar retenção zero para assuntos sensíveis? | Sim, para processos sigilosos |
| 1.7 | Há termo de tratamento de dados (DPA) com papéis de controlador e operador definidos, conforme a LGPD? | Sim |
| 1.8 | Qual o prazo e a forma de eliminação dos dados ao fim do contrato? | Compromisso específico |

## Bloco 2 — Infraestrutura e segurança

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 2.1 | Possui relatório de auditoria independente (por exemplo, SOC 2 Tipo II) e certificações como ISO/IEC 27001? | Sim; relatório disponível sob confidencialidade |
| 2.2 | Onde os dados são armazenados e processados? Há transferência internacional? | Locais informados; mecanismo de transferência compatível com a LGPD (art. 33 — conferir a regulamentação vigente da ANPD) |
| 2.3 | É possível restringir armazenamento e processamento a uma região? | Sim, para clientes com essa exigência |
| 2.4 | Criptografia em trânsito e em repouso: quais padrões? | Padrões atuais de mercado, informados |
| 2.5 | Autenticação: há login único (SSO) e autenticação em dois fatores? | Sim |
| 2.6 | Como trata dados pessoais sensíveis e dados de crianças e adolescentes? | Controles específicos descritos |
| 2.7 | Qual o processo de resposta a incidentes e o prazo para avisar o cliente? | Prazo compatível com as obrigações do escritório perante a ANPD e os titulares |
| 2.8 | Houve incidente de segurança nos últimos 24 meses? | Divulgação completa |
| 2.9 | Quais os compromissos de continuidade do serviço e recuperação de desastres? | Metas de tempo de recuperação informadas |

## Bloco 3 — Controles administrativos

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 3.1 | Há controle de acesso por perfil e por usuário? | Sim, granular |
| 3.2 | É possível liberar recursos e conectores só para grupos específicos? | Sim |
| 3.3 | Há registro de atividades (quem fez o quê e quando), com prazo de guarda? | Sim, com exportação |
| 3.4 | As permissões de conectores são configuráveis por ação (ler, enviar, alterar, excluir)? | Sim; enviar e alterar exigem aprovação |
| 3.5 | O escritório pode impor padrões, como "nenhum envio sem aprovação humana"? | Sim |
| 3.6 | Há recursos de prevenção de vazamento de dados? | Recursos listados |
| 3.7 | O acesso de quem sai do escritório pode ser revogado na hora? | Sim |

## Bloco 4 — Isolamento por processo ou cliente

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 4.1 | Há áreas de trabalho por processo ou cliente, com dados isolados? | Sim |
| 4.2 | É possível criar barreiras de informação entre equipes ou clientes? | Recurso descrito |
| 4.3 | Cada sessão registra a qual processo ou cliente se refere? | Sim, consultável |
| 4.4 | Os dados de um caso encerrado podem ser arquivados ou eliminados sob pedido? | Sim, por caso |
| 4.5 | Se surgir conflito de interesses, é possível retirar os dados do caso conflitado? | Procedimento descrito |

## Bloco 5 — Precisão e verificação

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 5.1 | A ferramenta busca em bases jurídicas brasileiras confiáveis (legislação oficial, tribunais, bases contratadas)? | Bases listadas, com cobertura e atualização |
| 5.2 | Cada citação traz referência verificável (link para a fonte oficial, número, página)? | Sim |
| 5.3 | Há recurso de verificação de citações ou conferência de trechos literais? | Recurso descrito |
| 5.4 | Quando não encontra fonte, a ferramenta reconhece a lacuna ou inventa? | Comportamento descrito; deve reconhecer |
| 5.5 | Quais modelos de IA estão por trás e com que frequência mudam? | Modelos e periodicidade informados |
| 5.6 | Como o fornecedor mede o acerto em tarefas jurídicas brasileiras? | Metodologia, amostra e período |
| 5.7 | Quais são as falhas conhecidas e como são mitigadas? | Divulgação honesta |

## Bloco 6 — Operação e custos

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 6.1 | Prazo de implantação? | Prazo definido |
| 6.2 | Níveis de suporte e acordos de nível de serviço? | Definidos |
| 6.3 | Modelo de preço (por usuário, por uso, licença) e reajuste? | Transparência total |
| 6.4 | Treinamento oferecido? | Descrito |
| 6.5 | Escritórios clientes que podem dar referência? | Contatos ou casos |

## Bloco 7 — Integração

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 7.1 | Com quais sistemas integra hoje (gestão processual, documentos, e-mail, agenda)? | Lista |
| 7.2 | Suporta padrões abertos de integração (por exemplo, MCP) e API documentada? | Sim, preferível |
| 7.3 | Integra com o provedor de identidade do escritório? | Sim |

## Bloco 8 — Personalização

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 8.1 | O escritório pode criar fluxos, modelos e skills próprios sem depender do fornecedor? | Sim, preferível |
| 8.2 | Esses fluxos podem ser exportados em formato aberto (por exemplo, Markdown)? | Sim, preferível |

## Bloco 9 — Encerramento e portabilidade

| Nº | Pergunta | Resposta esperada |
|---|---|---|
| 9.1 | Prazo de eliminação dos dados após o encerramento? | Compromisso específico |
| 9.2 | É possível exportar todos os dados, configurações, modelos e registros? | Sim |
| 9.3 | Há recursos que dificultem a migração? | Divulgação honesta |

## Bloco 10 — Perguntas próprias do escritório

- [ ] Integra com o sistema de gestão processual que o escritório usa?
- [ ] Atende às exigências de clientes de setores regulados (financeiro, saúde, setor público)?
- [ ] Atende a cláusulas de clientes que restringem o uso de IA?

## 4. Matriz de pontuação

| Bloco | Peso sugerido | Nota (1 a 5) | Ponderada |
|---|---|---|---|
| 1. Contrato e uso de dados | 20% | | |
| 2. Infraestrutura e segurança | 20% | | |
| 3. Controles administrativos | 15% | | |
| 4. Isolamento por processo ou cliente | 15% | | |
| 5. Precisão e verificação | 15% | | |
| 6. Operação e custos | 5% | | |
| 7. Integração | 5% | | |
| 8. Personalização | 3% | | |
| 9. Encerramento e portabilidade | 2% | | |
| **Total** | **100%** | | |

Ajustar os pesos às prioridades do escritório. Contencioso tende a pesar mais isolamento e registros; consultivo empresarial, integração e personalização. Como referência, média ponderada abaixo de 3 indica ferramenta imatura para dados de clientes, qualquer que seja o marketing.

## 5. Sinais de alerta

Interromper a avaliação se:

- o fornecedor se recusar a garantir por contrato que não treina modelos com os dados do escritório;
- a retenção de dados não puder ser desligada nem para casos sigilosos;
- não houver termo de tratamento de dados (DPA) nem informação sobre suboperadores e transferência internacional;
- não houver isolamento por processo ou cliente;
- houver incidente de segurança recente não resolvido;
- as citações não trouxerem fonte verificável;
- o fornecedor não aceitar responder por escrito.

## 6. Fonte e licença

Adaptado ao contexto brasileiro (LGPD, sigilo profissional, bases jurídicas nacionais) a partir de "Vendor Security Questionnaire — Legal AI Tools", do projeto master-claude-for-legal (github.com/sboghossian/master-claude-for-legal), Copyright (c) 2026 HAQQ Legal AI and contributors, licenciado sob MIT. O aviso de licença está em `.claude/skills/LICENSE-master-claude-for-legal.txt`. Foram retiradas as referências específicas dos EUA (HIPAA, bases norte-americanas) e acrescentados itens de LGPD. Não é aconselhamento jurídico; submeter à revisão do escritório antes de adotar como padrão.
