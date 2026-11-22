# <%= @title %>

Le mappe di FerventMind (`.fvmd`) si aprono in Marked. Marked decomprime il pacchetto e mostra il `text.md` salvato da FerventMind.

## Markdown nella mappa [markdown-in-the-map]

Come viene scritto quel Markdown si imposta in FerventMind, in **Settings > Files And Export**, nel gruppo **Markdown**. Marked mostra il file così come è stato salvato.

![FerventMind Files And Export][fm-export]

**Headings** imposta quanti livelli restano titoli. **Visible topics only** salta gli argomenti dentro un ramo chiuso. **Notes** e **Task checkboxes** decidono se note e attività vengono scritte in quel Markdown. Queste scelte valgono per l'esportazione Markdown, per Copy As e per la copia Markdown salvata in ogni mappa per app come Marked. Una mappa può sostituirle in **Definitions • MAP**.

Se una mappa più vecchia non ha un `text.md`, Marked costruisce una struttura a partire da `map.xml`: il titolo è il titolo 1, il livello successivo è il titolo 2 e gli argomenti più profondi diventano elenchi puntati annidati. Le note diventano il corpo della sezione. Un'attività completata diventa una casella selezionata, e un'attività parziale mostra la sua percentuale. Le immagini sono i file in `assets/`, senza una didascalia con il nome del file.

## Includere una mappa [including-a-map]

Includere un `.fvmd` usa **FerventMind files** sotto **Embed as Mermaid mind maps:** in {% prefspane Apps %}. Attivo produce un diagramma Mermaid a partire dalla mappa. Disattivo incorpora il `preview.png` della mappa. Vedi [Incorporamento di mappe mentali e contorni](Embedding_Mind_Maps_and_Outlines.html).

## Apri nell'editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) avvia FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
