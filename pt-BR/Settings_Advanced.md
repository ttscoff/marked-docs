<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Advanced %}:

![Configurações: Avançado][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

Metadados YAML e Pandoc
: - __Ignore:__ Deixa exatamente como existe no documento, útil se o seu processador ou pré-processador realmente usa o YAML.
: - __Remover antes da renderização__: O bloco YAML é removido
: - __Treat as MMD metadata:__ Converte o bloco de metadados YAML ou Pandoc para o formato MultiMarkdown.

Remover cabeçalhos de metadados MultiMarkdown
: se estiver ativado, os metadados do MultiMarkdown na parte superior do documento serão removidos antes da renderização.
: isso pode ser útil se você estiver usando um processador não MultiMarkdown que, de outra forma, exibiria os metadados no documento renderizado. Os metadados ainda são lidos antes da remoção, portanto a sintaxe específica do Marcado ainda será reconhecida.

Imagens hospedadas em cache
: Marcado não armazena imagens em cache na visualização por padrão, porque observa essas imagens em busca de alterações e as atualiza instantaneamente. Se estiver usando imagens referenciadas por meio de um URL da Web, você poderá ativar o cache dessas imagens para acelerar a renderização em conexões mais lentas.

Analise estatísticas de legibilidade
: Se você preferir não ter [estatísticas](Document_Statistics.html) calculadas, isso desativará esse processamento. Isso pode fornecer algumas melhorias de desempenho em documentos muito grandes. A contagem de caracteres, palavras e frases continuará funcionando.

Use o Find Pasteboard em todo o sistema
: Esta opção permitirá que o Marked escolha qualquer termo de pesquisa que você usou recentemente em outro editor, e qualquer coisa pesquisada no Marked se tornará a pesquisa em outros aplicativos também. Desativá-lo faz com que a pesquisa do Marked funcione de forma independente.

Use {% kbd cmd E %} para localizar com seleção
: Por padrão, {% kbd cmd E %} abre o editor padrão. Se esta opção estiver habilitada, {% kbd cmd E %} funcionará como na maioria dos aplicativos de edição de texto, usando o texto selecionado para Localizar, e Abrir no Editor pode ser acionado com {% kbd opt cmd E %}.

Modo de depuração
: habilita o log de depuração. Use-o para sua própria solução de problemas e ao relatar um problema. Selecione __Help->Open Debug Log__ para visualizar a atividade.
: Definir como _Todos_ mostrará mensagens informativas, avisos e mensagens de erro. Você também pode configurá-lo para mostrar apenas erros ou erros e avisos.

Backup de configurações
: você pode fazer backup de suas configurações em um arquivo JSON que pode ser usado para restaurar configurações ou portá-las para uma nova máquina.