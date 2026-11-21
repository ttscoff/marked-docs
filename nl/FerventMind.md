# <%= @title %>

FerventMind-kaarten (`.fvmd`) openen in Marked. Marked pakt het pakket uit. Staat er een `text.md` in, dan is dat bestand het voorbeeld. Zo niet, dan maakt Marked een overzicht uit `map.xml`.

## Overzicht uit de kaart [outline-from-the-map]

Onderwerptekst wordt koppen tot het niveau van **Headings through level** (standaard 2). Diepere onderwerpen worden geneste opsommingen, zodat taken op die niveaus hun lijstvakje houden. Notities worden de tekst van de sectie. Een afgeronde taak wordt een aangevinkt vak, en een gedeeltelijke taak toont het percentage. Afbeeldingen zijn de bestanden onder `assets/`, zonder een bijschrift met de bestandsnaam.

## Alleen zichtbare onderwerpen [display-only-visible-topics]

**Display only visible topics**, in {% prefspane Apps %} onder *FerventMind*, slaat onderwerpen in een ingeklapte tak over wanneer Marked dat overzicht bouwt. Een `text.md` die de app al heeft bewaard, blijft zoals hij is opgeslagen.

## Een kaart invoegen [including-a-map]

Een `.fvmd` invoegen gebruikt **FerventMind files** onder **Embed as Mermaid mind maps:** in {% prefspane Apps %}. Aan maakt een Mermaid-diagram van de zichtbare of volledige boom, volgens het vakje hierboven. Uit voegt de `preview.png` van de kaart in. Zie [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

## Openen in de editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) start FerventMind.
