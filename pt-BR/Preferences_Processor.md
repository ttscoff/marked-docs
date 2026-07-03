<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Processor %}:

![Configurações: Processador][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Processo Markdown com

Processador Markdown padrão. O processador Discount é preferido para usuários do GitHub, MultiMarkdown é ideal para escritores. Marcado compensa algumas diferenças entre sintaxe. Consulte __Help->Referência de Markdown__ para obter informações adicionais.

Regras personalizadas
: use o botão Regras Personalizadas para abrir o editor de Regras Personalizadas, permitindo determinar opções de processamento e transformações de documentos com base em critérios. Consulte a [documentação do processador personalizado](Custom_Processor.html) para obter detalhes.

Novos documentos usam custom
: selecione pré-processador e/ou processador para ativar automaticamente o processamento de regras em novos documentos. Se você estiver usando regras personalizadas, provavelmente desejará que ambas estejam ativadas.

###HTML

Gere IDs nas manchetes
: Gere IDs de cabeçalho com base no conteúdo da tag h1-h6.

Use IDs de notas de rodapé aleatórios
: gere IDs de notas de rodapé aleatórios para evitar conflitos quando vários documentos forem exibidos em uma página.

Processar Markdown dentro do HTML
: por padrão, o Markdown dentro das tags HTML geralmente é ignorado. Esta opção força Marked a continuar o processamento nos elementos do bloco. Observe que algumas marcações podem causar problemas.


### Renderização

Manter quebras de linha em parágrafos
: Respeite as quebras de linha no texto do parágrafo, substituindo por quebras rígidas em vez de concatenar com a linha anterior.

Renderizar caixas de seleção do GitHub
: Renderize `- [ ]` e `- [x]` para criar caixas de seleção em listas. As caixas de seleção são renderizadas para visualização, mas não funcionam em Marcado.

\#Texto é tag
: Permite que hashtags (`#` imediatamente seguidas de texto sem espaço) sejam interpretadas como tags, não como títulos. Esta funcionalidade é padrão para usuários do Bear.
: __Style tags__ faz com que as tags sejam exibidas com formatação de "cápsula" para distingui-las do texto. Quando ativado, as tags podem ser mostradas/ocultadas usando {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Text está com tag habilitada][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Renderizar `==highlight==` e `~~delete~~`
: Se esta opção estiver habilitada, o texto `==highlight==` será renderizado como uma tag HTML `<mark>`, que aparecerá como um destaque amarelo, a menos que seja modificado de outra forma por um estilo. Além disso, a sintaxe `~~delete~~` será renderizada com uma tag `<del>`.

: Se __Render as CriticMarkup__ estiver ativado, a sintaxe `==highlight==` e `~~delete~~` será convertida em CriticMarkup, que pode então ser exibida nas visualizações original, de marcação e editada.

Renderizar `~text~` como sublinhado
: Se esta opção estiver habilitada, `~text~` cercado por tis únicos será renderizado como sublinhado. Isso entra em conflito com a sintaxe MultiMarkdown para subscrito e está desabilitado por padrão.