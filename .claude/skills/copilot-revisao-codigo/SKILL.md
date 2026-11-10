---
name: copilot-revisao-codigo
description: Guia de referência para solicitar, configurar e personalizar a revisão de código do GitHub Copilot (Copilot code review) — no GitHub.com, VS Code, Visual Studio, GitHub Mobile, Xcode, IDEs JetBrains, GitHub CLI e API REST —, incluindo revisões automáticas, nova revisão após push, níveis de esforço e custos, aprovações, instruções personalizadas, skills e servidores MCP, ambiente de execução e firewall. Use quando o usuário perguntar como pedir ou configurar uma revisão do Copilot em um pull request ou em alterações locais.
---

# Revisão de código do GitHub Copilot

Apoiar o usuário a usar a revisão de código do GitHub Copilot. O conteúdo resume a documentação oficial do GitHub (ver "Fonte" ao final). Recursos, nomes de botões, preços e configurações mudam com frequência: ao orientar uma decisão que dependa de custo, plano ou configuração, recomendar a conferência da página oficial atual.

## Regras

- Não afirmar que uma revisão foi solicitada, aprovada ou configurada sem evidência da ferramenta usada (por exemplo, retorno de uma ferramenta MCP do GitHub, do `gh` ou da API).
- Antes de solicitar uma revisão em nome do usuário, avisar que ela consome créditos de IA da conta e confirmar, salvo pedido expresso.
- Distinguir revisão que apenas comenta de revisão que aprova (ver "Aprovações").
- Lembrar que comentários do Copilot são sugestões a avaliar, não ordens.

## O que a revisão faz

- Analisa o código e deixa comentários, muitas vezes com alterações sugeridas aplicáveis em poucos cliques.
- Classifica cada comentário com severidade **Alta**, **Média** ou **Baixa**.
- Por padrão, deixa uma revisão do tipo **Comentário** (não "Aprovar" nem "Solicitar alterações"), que não conta para as aprovações obrigatórias do PR.
- Usa GitHub Actions para seus recursos agênticos e roda em ambiente efêmero.
- Pode estar disponível a membros de organização sem licença Copilot, se um administrador habilitar.
- Respostas que o usuário escreve aos comentários do Copilot ficam visíveis para pessoas, mas o Copilot não as lê nem responde.

## Como solicitar, por ambiente

### GitHub.com (pull request)

1. Abrir ou criar o pull request.
2. Em **Reviewers/Revisores**, na barra lateral, clicar em **Request/Solicitar** ao lado de **Copilot**.
3. Aguardar (normalmente menos de 30 segundos) e ler os comentários.
4. Aplicar sugestões individualmente ou em lote num único commit, se forem adequadas.
5. Opcional: com Copilot code review e Copilot cloud agent habilitados, usar **Fix with Copilot/Corrigir com Copilot** num comentário para que o agente implemente a correção, em novo PR ou em commit no mesmo PR.

### GitHub CLI

- Ao criar o PR: `gh pr create --reviewer @copilot` (ou selecionar "Copilot (AI)" no prompt interativo de revisores).
- Em PR existente: `gh pr edit NUMERO-DO-PR --add-reviewer @copilot` (o número pode ser omitido se a branch do PR estiver em checkout).

### API REST

Solicitar `copilot-pull-request-reviewer[bot]` como revisor pelo endpoint de solicitação de revisores de pull request. Em ambientes com ferramentas MCP do GitHub, pode haver ferramenta própria para pedir revisão do Copilot.

### VS Code

- **Trecho selecionado:** selecionar o código → botão direito → **Generate Code/Gerar Código** → **Review/Revisão**. Os comentários aparecem no painel **Comments** e embutidos no editor.
- **Alterações não confirmadas:** na visão **Source Control**, passar o mouse sobre **Changes** e clicar no botão de revisão do Copilot para alterações não confirmadas. Os comentários aparecem nos arquivos e na aba **Problems**.
- Sugestões: **Apply and Go to Next** (aplica, sem commit automático) ou **Discard and Go to Next**.

### Visual Studio (17.14 ou posterior)

Na janela **Git Changes**, clicar em **Review changes with Copilot** (ícone de comentário com brilho). Um link mostra a quantidade de comentários; é possível navegar, ajustar o código, ignorar comentários ou limpar todos pelo **X** ao lado do link.

### GitHub Mobile

Abrir o PR → seção **Reviews** → **Request Reviews** → adicionar Copilot → **Done**.

### Xcode (extensão GitHub Copilot Chat 0.41.0 ou posterior)

Abrir o chat do Copilot (**Editor → GitHub Copilot → Open Chat**) → botão **Code Review** → **Review Staged Changes** ou **Review Unstaged Changes** → escolher arquivos → **Continue**. Os comentários aparecem em pop-ups, com **Accept**/**Dismiss** para sugestões.

### IDEs JetBrains

Com a extensão GitHub Copilot atualizada e login feito: janela **Commit** → **Copilot: Review Code Changes** (ícone de lupa com brilho). Os comentários podem ser aplicados ou descartados (**Discard**).

## Revisões automáticas e nova revisão

- Por padrão, a revisão é pedida manualmente em cada PR; é possível configurar revisão automática de todos os PRs.
- Após novos pushes, o Copilot não revisa de novo automaticamente, salvo se a revisão automática estiver ativa com a opção **Review new pushes** no conjunto de regras.
- Nova revisão manual: botão de sincronizar (re-request) ao lado do Copilot em **Reviewers**.
- Ao revisar de novo, o Copilot pode repetir comentários já resolvidos ou marcados com polegar para baixo.

## Níveis de esforço e custo

| Nível | Uso | Custo médio aproximado indicado pelo GitHub |
|---|---|---|
| **Lite** | Problemas evidentes: bugs, segurança, estilo | ~US$ 0,25 por revisão |
| **Balanced** | Lógica complexa, código sensível, mudanças entre serviços | ~US$ 1,50 por revisão |
| **Max** | Máximo escrutínio, vários modelos de alto raciocínio | ~US$ 10 por revisão |

O custo real varia com o tamanho do PR e os valores podem mudar; conferir a página de consumo estimado. O nível pode ser escolhido no PR antes de solicitar, definido como padrão nas configurações do usuário e, para revisões automáticas, pelos proprietários da organização ou administradores do repositório.

## Aprovações

- Toda revisão traz, no comentário de visão geral, uma avaliação sobre se o PR está pronto para aprovação; isso, sozinho, não conta para a mesclagem.
- Se as aprovações estiverem habilitadas (desligadas por padrão; configuráveis nos níveis empresa, organização e repositório), o Copilot pode enviar uma revisão de aprovação que satisfaz a regra de aprovação obrigatória.
- Novos commits após a aprovação a descartam.
- Administradores podem restringir, por caminhos de arquivo, quais aprovações do Copilot contam.

## Personalização por instruções

| Arquivo | Alcance |
|---|---|
| `.github/copilot-instructions.md` | Diretrizes de revisão para todo o repositório |
| `AGENTS.md` (raiz) | Contexto do projeto: padrões intencionais, áreas que exigem mais escrutínio, boas práticas |
| `.github/instructions/**/*.instructions.md` | Instruções específicas por caminho |
| `CLAUDE.md`, `GEMINI.md`, `REVIEW.md` | Também lidos, se existirem |

As instruções, instruções de agente e skills são lidas da **branch do PR** (a que contém as alterações), não da branch base, o que permite testar mudanças nelas no próprio PR.

Exemplo de `.github/copilot-instructions.md` (adaptado):

```text
Ao realizar uma revisão de código, responda em português.
Ao realizar uma revisão de código, aplique as verificações do arquivo /security/security-checklist.md.
Ao realizar uma revisão de código, priorize a legibilidade e evite operadores ternários aninhados.
```

## Skills e servidores MCP

- **Skills** do Copilot ficam em `.github/skills` (não em `.claude/skills`). Para orientar revisões, usar nome e descrição focados em revisão, por exemplo um diretório `code-review`.
- **Servidores MCP** são configurados nas configurações do Copilot do repositório; o servidor MCP do GitHub e o do Playwright vêm habilitados por padrão.
- O Copilot tende a usar esse contexto quando as skills têm foco em revisão, quando instruções o mandam usar um contexto MCP específico, ou quando a descrição do PR menciona itens acessíveis por MCP (chaves de issue, IDs de incidente).
- Cada comentário traz, ao final, a atribuição da skill ou servidor MCP usado; os logs da sessão de revisão mostram as ferramentas chamadas.
- A opção **Allow Copilot to use MCP tools when reviewing pull requests** vem ligada; desligar se os servidores MCP devem servir só ao cloud agent.

## Ambiente de execução e firewall

- `.github/workflows/copilot-setup-steps.yml`: se já existir para o cloud agent, também é usado pela revisão.
- `.github/workflows/copilot-code-review.yml`: configura o ambiente da revisão de forma independente; se existir, prevalece sobre o anterior.
- Regras de firewall (domínios e URLs acessíveis) podem ser definidas para a revisão nos níveis de organização e repositório, separadamente das do cloud agent, na aba de acesso à internet.

## Feedback

Avaliar cada comentário com polegar para cima ou para baixo, no GitHub ou na IDE; o GitHub usa esse retorno para melhorar o produto.

## Fonte

Documentação oficial do GitHub, página "Usando o GitHub Copilot para revisão de código" (docs.github.com, versão em português), conforme o texto fornecido pelo usuário em 10/11/2026. A documentação do GitHub é a fonte autoritativa; em caso de divergência, prevalece a versão atual da página oficial.
