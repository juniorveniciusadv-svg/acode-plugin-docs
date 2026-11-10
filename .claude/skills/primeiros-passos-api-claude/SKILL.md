---
name: primeiros-passos-api-claude
description: Guia em português para começar a usar a API do Claude — criar conta no Claude Console, autenticar pela CLI `ant` ou por chave de API, fazer a primeira chamada à Messages API (cURL, CLI, Python, TypeScript e outros SDKs) e cuidar de segurança, sigilo profissional e LGPD antes de enviar dados de clientes. Use quando o usuário quiser fazer a primeira chamada à API, configurar a autenticação ou entender o passo a passo inicial; para detalhes técnicos avançados (ferramentas, streaming, cache, modelos e preços), use a skill `claude-api`.
---

# Primeiros passos com a API do Claude

Conduzir o usuário da criação da conta até a primeira resposta da API, explicando cada passo em linguagem acessível. Para dúvidas técnicas além do básico, carregar a skill `claude-api`, que é a referência completa e atualizada.

## Regras

- Comandos, versões, nomes de modelo e o cabeçalho `anthropic-version` mudam: confirmar na documentação oficial atual antes de afirmar que um valor é o vigente. Os valores abaixo vêm da página oficial na versão consultada (ver "Fonte").
- Nunca pedir que o usuário cole a chave de API no chat, nem gravá-la em arquivo versionado (Git). A chave fica em variável de ambiente ou em gerenciador de segredos.
- Não afirmar que uma chamada funcionou sem ver a resposta da API.

## 1. Antes de começar

1. Criar uma conta no **Claude Console** (platform.claude.com) ou entrar na conta existente.
2. Escolher a forma de autenticação:
   - **CLI `ant`** (recomendada para uso no próprio computador): faz login pelo navegador e os SDKs passam a usar as credenciais automaticamente.
   - **Chave de API**: indicada para servidores e automações.

### Opção A — CLI `ant`

Instalar:

```bash
# macOS (Homebrew)
brew install anthropics/tap/ant

# Go 1.26.10 ou posterior
go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest
export PATH="$PATH:$(go env GOPATH)/bin"
```

No Linux/WSL, baixar o binário da versão desejada na página de releases do repositório `anthropics/anthropic-cli` no GitHub.

Entrar:

```bash
ant auth login
```

### Opção B — Chave de API

1. Criar a chave em **Settings → API keys** no Claude Console.
2. Definir a variável de ambiente lida pelos SDKs e pela CLI:

```bash
export ANTHROPIC_API_KEY="sua-chave-aqui"
```

## 2. Primeira chamada

### Pela CLI

```bash
ant messages create \
  --model claude-opus-5-5 \
  --max-tokens 1000 \
  --message '{
    role: user,
    content: "Quais termos devo pesquisar para encontrar as decisões mais recentes do STJ sobre dano moral?"
  }'
```

### Por cURL (com chave de API)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2026-10-21" \
  -d '{
    "model": "claude-opus-5-5",
    "max_tokens": 1000,
    "messages": [
      {"role": "user", "content": "Quais termos devo pesquisar para encontrar as decisões mais recentes do STJ sobre dano moral?"}
    ]
  }'
```

Com login pela CLI, trocar o cabeçalho `x-api-key` por `Authorization: Bearer $(ant auth print-credentials --access-token)`.

### Por Python

```bash
mkdir claude-quickstart && cd claude-quickstart
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic
```

```python
import anthropic

client = anthropic.Anthropic()  # lê ANTHROPIC_API_KEY ou as credenciais do `ant`

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Quais termos devo pesquisar para encontrar as decisões mais recentes do STJ sobre dano moral?"}],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
```

### Por TypeScript

```bash
mkdir claude-quickstart && cd claude-quickstart
npm init -y && npm pkg set type=module
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const message = await client.messages.create({
  model: "claude-opus-5-5",
  max_tokens: 1000,
  messages: [{ role: "user", content: "Quais termos devo pesquisar para encontrar as decisões mais recentes do STJ sobre dano moral?" }],
});

for (const block of message.content) {
  if (block.type === "text") console.log(block.text);
}
```

Executar com `npx tsx quickstart.ts`. Há SDKs oficiais também para C#, Go, Java, PHP e Ruby; os exemplos estão na página oficial e na skill `claude-api`.

### Como ler a resposta

A API devolve um JSON com, entre outros campos:

- `content`: lista de blocos; o texto da resposta está nos blocos `type: "text"`;
- `stop_reason`: por que a resposta terminou (`end_turn` = concluiu normalmente; `max_tokens` = atingiu o limite, aumentar `max_tokens`);
- `usage`: tokens de entrada e de saída, base da cobrança.

## 3. Cuidados para uso em escritório de advocacia

- **Sigilo profissional e LGPD:** antes de enviar documentos ou dados de clientes, avaliar a necessidade, minimizar e anonimizar dados pessoais e sensíveis, e verificar os termos de uso, de retenção e de privacidade aplicáveis à conta e ao plano contratado.
- **Chave de API é segredo:** quem a tiver pode gerar cobranças na conta. Definir data de expiração, revogar chaves expostas e não compartilhá-las por e-mail ou mensagem.
- **Custos:** o uso é cobrado por tokens; acompanhar o consumo no Claude Console e definir limites de gasto.
- **Revisão humana:** respostas da API são rascunhos; citações, dispositivos e precedentes devem ser conferidos nas fontes oficiais (skill `pesquisa-juridica-brasileira`).

## 4. Próximos passos

- Conversas de vários turnos, prompt de sistema e motivos de parada: página "Trabalhando com a Messages API".
- Comparação de modelos por capacidade e custo: "Visão geral dos modelos".
- Ferramentas, saídas estruturadas e gestão de contexto: "Visão geral dos recursos".
- Autenticação e expiração de chaves: "Autenticação".

Para qualquer desses tópicos, carregar a skill `claude-api`.

## Fonte

Documentação oficial da Anthropic, página "Comece a usar o Claude" (https://platform.claude.com/docs/pt-BR/get-started), conforme o texto fornecido pelo usuário em 10/11/2026. Os exemplos foram resumidos e a pergunta de exemplo foi adaptada ao contexto jurídico; comandos, versões e nomes de modelo seguem a página consultada. Em caso de divergência, prevalece a versão atual da documentação oficial.
