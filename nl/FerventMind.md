# <%= @title %>

FerventMind-kaarten (`.fvmd`) openen in Marked. Marked pakt het pakket uit en toont de `text.md` die FerventMind heeft bewaard.

## Markdown in de kaart [markdown-in-the-map]

Hoe die Markdown wordt geschreven, stel je in FerventMind in onder **Settings > Files And Export**, in de groep **Markdown**. Marked toont het bestand zoals het is opgeslagen.

![FerventMind Files And Export][fm-export]

**Headings** bepaalt hoeveel niveaus koppen blijven. **Visible topics only** slaat onderwerpen in een ingeklapte tak over. **Notes** en **Task checkboxes** bepalen of notities en taken in die Markdown worden geschreven. Deze keuzes gelden voor Markdown-export, Copy As en de Markdown-kopie die in elke kaart wordt bewaard voor apps zoals Marked. Een kaart kan ze vervangen onder **Definitions • MAP**.

Heeft een oudere kaart geen `text.md`, dan maakt Marked een overzicht uit `map.xml`: de titel is kop 1, het volgende niveau is kop 2, en diepere onderwerpen worden geneste opsommingen. Notities worden de tekst van de sectie. Een afgeronde taak wordt een aangevinkt vak, en een gedeeltelijke taak toont het percentage. Afbeeldingen zijn de bestanden onder `assets/`, zonder een bijschrift met de bestandsnaam.

## Een kaart invoegen [including-a-map]

Een `.fvmd` invoegen gebruikt **FerventMind files** onder **Embed as Mermaid mind maps:** in {% prefspane Apps %}. Aan maakt een Mermaid-diagram van de kaart. Uit voegt de `preview.png` van de kaart in. Zie [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

## Openen in de editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) start FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
