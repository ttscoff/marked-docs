# <%= @title %>

Os mapas do FerventMind (`.fvmd`) abrem no Marked. O Marked descompacta o pacote. Se houver um `text.md` dentro, esse arquivo é a visualização. Se não houver, o Marked monta um esboço a partir de `map.xml`.

## Esboço a partir do mapa [outline-from-the-map]

O texto de cada tópico vira títulos até o nível definido por **Headings through level** (2 por padrão). Tópicos mais profundos viram marcadores aninhados, de modo que as tarefas nesses níveis mantêm a caixa de lista. As notas viram o corpo da seção. Uma tarefa concluída vira uma caixa marcada, e uma tarefa parcial mostra a porcentagem. As imagens são os arquivos em `assets/`, sem uma legenda com o nome do arquivo.

## Mostrar só os tópicos visíveis [display-only-visible-topics]

**Display only visible topics**, em {% prefspane Apps %} sob *FerventMind*, ignora os tópicos dentro de um ramo dobrado quando o Marked monta esse esboço. Não altera um `text.md` que o aplicativo já tenha salvo.

## Incluir um mapa [including-a-map]

Incluir um `.fvmd` usa **FerventMind files** sob **Embed as Mermaid mind maps:** em {% prefspane Apps %}. Ativado produz um diagrama Mermaid da árvore visível ou completa, conforme a caixa acima. Desativado incorpora o `preview.png` do mapa. Consulte [Incorporando mapas mentais e contornos](Embedding_Mind_Maps_and_Outlines.html).

## Abrir no editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) abre o FerventMind.
