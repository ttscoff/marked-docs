# <%= @title %>

Mindmaps en overzichten kunnen in uw Markdown preview worden ingesloten met behulp van [Marked's include syntax][include] of de [IA Writer block syntax][ia]. Het gedrag is afhankelijk van het bestandsformaat en de instelling "Kaarten insluiten als zeemeermindiagrammen" in {% prefspane Apps %} onder *Mind Maps/Outlines*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Ondersteunde formaten [supported-formats]

### iThoughts X (.itmz) [ithoughts-x-itmz]

iThoughts mindmapbestanden zijn zip-archieven met kaartgegevens en een optionele voorbeeldafbeelding.

### MindManager (.mmap) [mindmanager-mmap]

MindManager-bestanden zijn zip-archieven die `Document.xml` bevatten. Uitgepakte MindManager-pakketten (een map met `Document.xml`) en directe paden naar `Document.xml` worden ook ondersteund.

### FreeMind (.mm) [freemind-mm]

FreeMind mindmapbestanden gebruiken de extensie `.mm` en slaan gegevens op als XML. Marked detecteert het FreeMind-formaat door te controleren of de bestandsinhoud begint met `<map`; Als dat niet het geval is (bijvoorbeeld een codefragment), wordt het bestand als platte tekst opgenomen. FreeMind-bestanden worden ondersteund voor het insluiten van Mermaid-mindmaps.

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) is een XML-formaat voor hiërarchische overzichten, dat veel wordt gebruikt door outliners en feedlezers. iThoughts en andere apps kunnen exporteren naar OPML. Marked converteert de meegeleverde OPML bestanden naar zeemeermin-mindmapdiagrammen.

### Fiets (.bike) [bike-bike]

Zie [Bike](Bike.html) voor het openen van een `.bike`-bestand. Ingevoegde Bike-overzichten volgen het selectievakje **Bike outlines**: aan tekent een Mermaid-mindmap (de bestandsnaam zonder `.bike` is de hoofdknoop); uit tekent een geneste Markdown-lijst zonder documenttitel.

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

Zie [Tree Outliner](Tree_Outliner.html). Het selectievakje **Tree Outliner outlines** regelt zowel het openen als het invoegen van een `.treeoutline`-bestand. Aan tekent een Mermaid-mindmap met de documenttitel als hoofdknoop. Uit stelt koppen en lijsten samen; **Headings through level** in de groep *Tree Outliner* bepaalt hoe diep de koppen gaan.

## Kaarten insluiten als zeemeermindiagrammen [embed-maps-as-mermaid-diagrams]

Indien **ingeschakeld** (standaard), converteert Marked de meegeleverde mindmaps en overzichten naar [Mermaid](https://mermaid.js.org/) diagrammen:

**iThoughts, MindManager, FreeMind, OPML & Bike** — Weergegeven als Mermaid-mindmapdiagrammen met de overzichtelijke boomstructuur. Voor iThoughts en MindManager wordt vorminformatie (rond, rechthoekig, zeshoek, etc.) behouden waar beschikbaar. FreeMind (`.mm`) en OPML gebruiken hetzelfde mindmapformaat. Fietscontouren (`.bike`) gebruiken de meegeleverde bestandsnaam (minus extensie) als het hoofdknooppunt van de mindmap. Knooppuntlabels zijn platte tekst (koppelingen worden koppelingstekst; taken worden weergegeven als voorvoegsels ☐ / ☑). Zeemeermin is standaard opgenomen in elk Markdown voorbeeld.

**Beperking:** Het insluiten van mindmaps (zeemeermindiagrammen) werkt niet met de kortingsparser. Gebruik MultiMarkdown, CommonMark (GFM) of Kramdown voor previews van mindmaps.

Wanneer **uitgeschakeld**:

- **iThoughts** — De ingebouwde voorbeeldafbeelding (`preview.png`) van het .itmz-bestand is ingesloten als een base64-afbeelding. De alt-tekst van de afbeelding gebruikt de bestandsnaam.
- **MindManager** — Het overzicht is ingesloten als een geneste Markdown lijst.
- **FreeMind** — Het overzicht is ingesloten als een geneste Markdown lijst.
- **OPML** — Het overzicht is ingesloten als een geneste Markdown lijst (geen mindmap).
- **Fiets** — De omtrek is ingesloten als een geneste Markdown lijst (geen H1); Kopitems op het hoogste niveau worden H2, geneste koppen zijn vetgedrukt en taken worden GitHub selectievakjes.

## Syntaxis opnemen [include-syntax]

Gebruik dezelfde syntaxis als voor andere bestandsindelingen:

<<[pad/naar/kaart.itmz]
	<<[pad/naar/kaart.mmap]
	<<[pad/naar/kaart.mm]
	<<[pad/naar/overzicht.opml]
	<<[pad/naar/overzicht.fiets]
	<<[path/to/outline.treeoutline]

Of met iA Writer-bloksyntaxis:

/pad/naar/map.itmz

Paden kunnen relatief zijn ten opzichte van het hoofddocument of absoluut (beginnend met `/` of `~`). Zie [Multi-File Documents](Multi-File_Documents.html) voor details.

## OPML Conversie [opml-conversion]

OPML bestanden gebruiken geneste `<outline>` elementen met een `text` attribuut. Wanneer "Insluiten als zeemeermindiagram" is ingeschakeld (zie [Settings: Apps](Settings_Apps.html)), produceert de conversie een zeemeermin-mindmap met hetzelfde formaat als iThoughts en MindManager:

- Onderliggende contouren van `<body>` worden het hoogste niveau (of onderliggende contouren van een "Outline"-root als er meerdere items op het hoogste niveau zijn)
- Geneste contouren definiëren de hiërarchie
- Ontbrekend of leeg `text` wordt weergegeven als `(unnamed)`
- Tekst is opgeschoond; speciale karakters zijn ontsnapt voor Mermaid

## Fietsconversie [bike-conversion]

Bike-bestanden `.bike` zijn HTML met een hoofd-`<ul>` en `<li>`-items. In de lijstmodus is elke regel een lijstonderdeel: regels met `data-type="heading"` zijn vet, en regels met `data-type="task"` zijn GitHub-selectievakjes (voltooid wanneer `data-done` een tijdstempel heeft, of wanneer `data-checked` / `data-completed` waar is). Opmaak en koppelingen in de knooptekst worden Markdown. Een geopend `.bike`-bestand gebruikt altijd deze lijst. Wanneer een ingevoegd bestand als Mermaid-mindmap wordt ingesloten, is de bestandsnaam (zonder extensie) de enige hoofdknoop en zijn de labels platte tekst voor de Mermaid-mindmap-syntaxis.
