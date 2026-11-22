# <%= @title %>

Os mapas do FerventMind (`.fvmd`) abrem no Marked. O Marked descompacta o pacote e mostra o `text.md` que o FerventMind salvou.

## Markdown no mapa [markdown-in-the-map]

Como esse Markdown é escrito é definido no FerventMind, em **Settings > Files And Export**, no grupo **Markdown**. O Marked mostra o arquivo como foi salvo.

![FerventMind Files And Export][fm-export]

**Headings** define quantos níveis continuam títulos. **Visible topics only** ignora os tópicos dentro de um ramo dobrado. **Notes** e **Task checkboxes** decidem se notas e tarefas são escritas nesse Markdown. Essas escolhas valem para a exportação Markdown, para Copy As e para a cópia Markdown guardada em cada mapa para aplicativos como o Marked. Um mapa pode substituí-las em **Definitions • MAP**.

Se um mapa antigo não tiver `text.md`, o Marked monta um esboço a partir de `map.xml`: o título é o título 1, o nível seguinte é o título 2 e os tópicos mais profundos viram marcadores aninhados. As notas viram o corpo da seção. Uma tarefa concluída vira uma caixa marcada, e uma tarefa parcial mostra a porcentagem. As imagens são os arquivos em `assets/`, sem uma legenda com o nome do arquivo.

## Incluir um mapa [including-a-map]

Incluir um `.fvmd` usa **FerventMind files** sob **Embed as Mermaid mind maps:** em {% prefspane Apps %}. Ativado produz um diagrama Mermaid a partir do mapa. Desativado incorpora o `preview.png` do mapa. Consulte [Incorporando mapas mentais e contornos](Embedding_Mind_Maps_and_Outlines.html).

## Abrir no editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) abre o FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
