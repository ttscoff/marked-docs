<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Entregue a um agente de LLM um arquivo de skill para que ele abra arquivos e pastas no Marked, vá a uma seção dos Ajustes e altere preferências. O agente usa o [manipulador de URL](URL_Handler.html) do Marked. Não é preciso um plugin nem um servidor separado.

## Baixar o skill [download-the-skill]

{% download "SKILL.md" "Skill de agente para abrir arquivos no Marked e alterar preferências. Salve o arquivo como SKILL.md." %}

O arquivo é Markdown simples, com um cabeçalho curto que o agente lê antes de agir. Você pode entregar o mesmo arquivo a qualquer agente que aceite um skill ou uma instrução permanente.

## Instalar [install-it]

Coloque o arquivo numa pasta com o nome do skill e mantenha o nome `SKILL.md`.

No Cursor, estes dois lugares funcionam:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

O primeiro fica disponível em todos os projetos. O segundo vale só para aquele projeto. Outros agentes podem usar o mesmo texto como instrução do projeto, se não tiverem uma pasta de skills.

Depois de instalado, peça ao agente que abra um arquivo ou uma pasta no Marked. Ele deve executar um comando como este:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Uma pasta usa o mesmo comando. O caminho precisa existir, e espaços e outros caracteres reservados precisam ser codificados com porcentagem. Veja o [manipulador de URL](URL_Handler.html) para o esquema completo, inclusive refresh, Streaming Preview e callbacks.

## Preferências [preferences]

O skill também cobre dois comandos de preferências:

`pref`
: Abre os Ajustes numa seção nomeada. O nome na URL permanece em inglês, por exemplo `Preview` ou `Style`. Não altera nenhum valor.

`defaults`
: Define uma preferência que o Marked já armazena e recarrega as pré-visualizações abertas. Passe `refresh=0` para deixar as pré-visualizações como estão. O agente deve ler as preferências atuais antes de gravar uma, porque uma chave desconhecida é ignorada.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Relacionado [related]

[Usando o Marked com codificação agentiva](Using_Marked_with_Agentic_Coding.html) explica como acompanhar uma pasta de planos e notas enquanto um agente as escreve. O [utilitário de linha de comando](Command_Line_Utility.html) oferece o mesmo tipo de acesso a partir do shell, sem um agente.
