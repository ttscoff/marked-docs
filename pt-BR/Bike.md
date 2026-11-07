# <%= @title %>

Arraste um esboço do [Bike][bike] (`.bike`) para o Marked para vê-lo como uma lista Markdown aninhada, com as linhas de título em negrito e as tarefas como caixas de seleção.

## Abrir um esboço do Bike [opening-a-bike-outline]

O Marked converte o esboço quando você abre o arquivo:

- Linhas marcadas como título viram itens de lista em **negrito**.
- Tarefas viram caixas de seleção no estilo do GitHub. Uma tarefa fica marcada quando o Bike grava um horário de conclusão ou a marca como feita.
- Links e formatação no texto da linha permanecem Markdown.

Abrir um arquivo `.bike` usa sempre essa lista. O esboço não vira um diagrama Mermaid.

## Incluir um esboço do Bike [including-a-bike-outline]

Um arquivo `.bike` também pode ser incluído em outro documento Markdown. Consulte [Incorporar mapas mentais e esboços](Embedding_Mind_Maps_and_Outlines.html).

Em {% prefspane Apps %}, em *Mind Maps and Outlines*, **Bike outlines** vale para os arquivos incluídos:

- **Ativado** (o padrão) — um diagrama Mermaid. O nome do arquivo, sem `.bike`, é o nó raiz.
- **Desativado** — a mesma lista Markdown aninhada de quando você abre o arquivo, sem título do documento.

Diagramas Mermaid precisam de MultiMarkdown, CommonMark (GFM) ou Kramdown. Eles não são desenhados com o processador Discount.

[bike]: https://www.hogbaysoftware.com/bike/
