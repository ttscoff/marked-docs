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

Bike.app-overzichten worden opgeslagen als eigen HTML-bestanden (`.bike`). U kunt een `.bike` bestand rechtstreeks in Marked openen: het document wordt weergegeven als Markdown met de bestandsnaam (minus extensie) als de hoofdkop (H1), kopitems op het hoogste niveau als H2, geneste koppen als vetgedrukte lijstitems en taken als selectievakjes in de stijl van GitHub. Wanneer een `.bike` bestand wordt opgenomen via de include-syntaxis, bepaalt de instelling "Insluiten als Zeemeermindiagram" voor Fiets (in Apps → Mindmaps/Overzichten) of het een Zeemeermin-mindmap wordt (met de bestandsnaam als hoofdknooppunt) of een geneste Markdown-lijst (geen H1).

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

Fiets `.bike` bestanden zijn HTML met een root `<ul>` en `<li>` items. Items kunnen `data-type="heading"` hebben (hoogste niveau → H2 wanneer geopend of in lijstmodus; genest → vetgedrukt) of `data-type="task"` (GitHub selectievakjes; voltooid wanneer `data-done` een tijdstempel heeft, of `data-checked` / `data-completed` waar is). Inline-opmaak en links in knooppunttekst worden geconverteerd naar Markdown. Bij het insluiten als een Mermaid-mindmap wordt de bestandsnaam (minus extensie) gebruikt als het enkele hoofdknooppunt en zijn de labels in platte tekst opgemaakt voor de Mermaid-mindmap-syntaxis.