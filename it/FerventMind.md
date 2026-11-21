# <%= @title %>

Le mappe di FerventMind (`.fvmd`) si aprono in Marked. Marked decomprime il pacchetto. Se all'interno c'è un `text.md`, quel file è l'anteprima. Altrimenti Marked costruisce una struttura a partire da `map.xml`.

## Struttura ricavata dalla mappa [outline-from-the-map]

Il testo di ogni argomento diventa un titolo fino al livello impostato da **Headings through level** (2 per impostazione predefinita). Gli argomenti più profondi diventano elenchi puntati annidati, così le attività di quei livelli conservano la casella di elenco. Le note diventano il corpo della sezione. Un'attività completata diventa una casella selezionata, e un'attività parziale mostra la sua percentuale. Le immagini sono i file in `assets/`, senza una didascalia con il nome del file.

## Mostra solo gli argomenti visibili [display-only-visible-topics]

**Display only visible topics**, in {% prefspane Apps %} sotto *FerventMind*, salta gli argomenti dentro un ramo chiuso quando Marked costruisce quella struttura. Non modifica un `text.md` già salvato dall'applicazione.

## Includere una mappa [including-a-map]

Includere un `.fvmd` usa **FerventMind files** sotto **Embed as Mermaid mind maps:** in {% prefspane Apps %}. Attivo produce un diagramma Mermaid dell'albero visibile o completo, in base alla casella precedente. Disattivo incorpora il `preview.png` della mappa. Vedi [Incorporamento di mappe mentali e contorni](Embedding_Mind_Maps_and_Outlines.html).

## Apri nell'editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) avvia FerventMind.
