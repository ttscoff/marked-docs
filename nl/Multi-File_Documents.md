# <%= @title %>

Met Marked zijn verschillende syntaxis mogelijk om het ene bestand in het andere op te nemen.

## Marked Syntaxis [marked-syntax]

U kunt externe bestanden in één voorbeelddocument opnemen door de speciale syntaxis `<<[path/file]` aan het begin van een regel te gebruiken. De regel moet boven en onder blanco regels bevatten en er wordt aangenomen dat het pad relatief is ten opzichte van het hoofddocument, tenzij het begint met een schuine streep (`/`) of een tilde (`~`). Slash (hoofdmap) en tilde (thuismap) kunnen worden gebruikt om absolute paden naar bestanden te definiëren. Er is geen pad nodig als de externe bestanden zich in dezelfde map bevinden als het hoofddocument. Plaats gewoon de bestandsnaam (hoofdlettergevoelig en inclusief extensie) tussen vierkante haakjes.

U kunt de metadatakoppen "Include Base" of "Transclude Base" gebruiken om de basislocatie voor opgenomen bestanden te wijzigen, bijvoorbeeld:

Basis transcluderen: ~/Desktop

*Merk op dat wanneer u documenten met bijgevoegde bestanden bekijkt, u "I" (shift-i) kunt typen om te zien welk bijgevoegde bestand zich in het zichtbare gebied bevindt. Als u op Return drukt terwijl het opgenomen bestandspad wordt weergegeven, wordt het opgenomen bestand geopend in de standaardeditor.*

Met deze functie kunt u grote documenten/boeken samenstellen met behulp van meerdere bestanden (bijvoorbeeld een bestand voor elk hoofdstuk) en vervolgens de documentvolgorde in één indexbestand opgeven. Het maakt niet uit hoe de bestanden worden genoemd of hoe de mappen zijn georganiseerd; het bestand dat u opent in Marked wordt beschouwd als de index en de bestanden die daarin worden vermeld, worden opgenomen. Een voorbeeld van een indexbestand voor een driedelig document:

Mappenstructuur:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Index.md:

# Documenttitel

## Sectie 1

<<[secties/sectie1.md]

## Sectie 2

<<[secties/sectie2.md]

## Sectie 3

<<[secties/sectie3.md]

Als u Index.md opent in Marked, wordt de inhoud weergegeven met alle drie de meegeleverde bestanden uitgevouwen. Alle opgenomen bestanden worden gecontroleerd op wijzigingen. In tegenstelling tot het geopende document in Marked is het bijhouden van opgenomen bestanden afhankelijk van Spotlight om updates te verkrijgen en moet het in een door Spotlight geïndexeerde map op uw schijf staan.

Je kunt ook codefragmenten en onbewerkte html of tekst toevoegen met [variations of this syntax](Special_Syntax.html#includingcode).

De uiteindelijke HTML export van een document met include bevat HTML opmerkingen met het relatieve pad van het opgenomen bestand aan het begin en einde van de geïmporteerde tekst.

**Opmerking:** hoe meer bestanden er in een document zitten, hoe langzamer de totale compileertijd van de preview zal zijn. Marked probeert het proces te optimaliseren en in de cache op te slaan, maar verwacht enige weergavevertragingen naarmate uw document groter wordt.

## MultiMarkdown Syntaxis transcluderen

U kunt ook de syntaxis `<!--MKPH0-->` gebruiken, gebaseerd op de nieuwere MultiMarkdown-specificatie. Marked herkent `Transclude Base: path` in MMD metadata en gebruikt deze als basis voor bestandstransclusie.

Transclude Base wordt alleen herkend in het bovenliggende document, niet in aanvullende meegeleverde documenten. Alle geneste insluitingen moeten paden hebben die zijn gebaseerd op de initiële Transclude Base, of op basis van de locatie van het bovenliggende document.

De afgeschermde codesyntaxis die MultiMarkdown biedt voor het opnemen van bestanden zonder verwerking, werkt niet in Marked. Gebruik hiervoor de `<<(file)` (codeblok) of `<<{file}` (onbewerkte) syntaxis.

## IA Writer Block-syntaxis

Marked 2.5.11+ ondersteunt de IA Writer [Content Block][ia] syntaxis. Dit is een verwijzing die begint met een schuine streep (`/`) op zijn eigen regel. Het kan een codevoorbeeld, een afbeelding, een markdown-bestand of een CSV-bestand zijn. Alles wordt op de juiste manier afgehandeld op basis van de extensie van het opgenomen bestand, en CSV's zullen indien mogelijk [converted into Markdown][csv] tabellen zijn.

In IA writer worden de meegeleverde bestanden in de iCloud-container geplaatst en vereisen deze niet altijd "echte" paden. In Marked moet deze syntaxis worden gebruikt met een pad, absoluut of relatief, tenzij er al opgenomen bestanden bestaan ​​in dezelfde map als het bestand waarvan u een voorbeeld bekijkt. De eerste schuine streep wordt genegeerd, dus als het een absoluut pad is, begin dan met twee schuine strepen.

Een codefragment in dezelfde map als het document waarvan u een voorbeeld bekijkt:

/fragment.h

Relatief pad naar een submap genaamd "images":

/images/image.png "optionele titel"

Absoluut pad naar de map Documenten:

//Gebruikers/gebruikersnaam/Documenten/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Hoe overzichten, mindmaps en CSV-gegevens worden geconverteerd

Wanneer u bepaalde bestandstypen opneemt met `<<[path]` of IA Writer-bloksyntaxis, converteert Marked ze in plaats van de onbewerkte bestandsinhoud in te voegen. Het gedrag van het overzicht en de mindmap is afhankelijk van de bestandsextensie en uw [Settings: Apps → Mind Maps/Outlines][mindmaps] voorkeuren. CSV/TSV-bestanden worden altijd geconverteerd naar Markdown tabellen (zie [Creating Tables using CSV files][csv]).

| Formaat | Extensie | Wanneer "Insluiten als zeemeermin" **aan** staat | Wanneer **uit** |
|--------|------------|--------------------------------|--------------|
| **iGedachten X** | .itmz | Zeemeermin mindmapdiagram (opruimboom) | Voorbeeldafbeelding van de .itmz |
| **MindManager** | .mmap | Zeemeermin mindmapdiagram | Geneste Markdown lijst |
| **Vrije geest** | .mm | Zeemeermin mindmapdiagram | Geneste Markdown lijst |
| **OPML** | .opml | Zeemeermin mindmapdiagram | Geneste Markdown lijst |
| **OmniOutliner** | .ooverzicht | Zeemeermin mindmapdiagram | Geneste Markdown lijst |
| **Fiets** | .fiets | Zeemeermin mindmap (bestandsnaam als rootnode) | Geneste Markdown lijst (geen documenttitel) |
| **CSV/TSV** | .csv, .tsv | Markdown tabel ||
| **RTF / RTFD** | .rtf, .rtfd | Markdown via RTF conversie (zie [RTF and RTFD Support](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown via PDF conversie wanneer geopend als hoofddocument (zie [PDF Support](PDF_Support.html)) ||

Elk overzichts-/mindmapformaat heeft zijn eigen selectievakje onder *Mind Maps/Outlines* (Mindmaps, OPML bestanden, Fietsoverzichten, OmniOutliner-overzichten). Als u een indeling uitschakelt, wordt alleen het 'uit'-gedrag voor dat type gebruikt. Zie [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html) voor formaatdetails en [Settings: Apps][mindmaps] om deze opties te wijzigen. Zie [Creating Tables using CSV files][csv] voor details over CSV-conversie.

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Boekformaten

Marked ondersteunt ook indexbestanden in formaten als [Leanpub][lp], [GitBook][gb] en mmd\_merge (MultiMarkdown). Bestanden die zijn opgenomen in de indexen van boekformaten worden gecontroleerd op wijzigingen en het resultaat is een volledig voorbeeld van uw gecompileerde document, net als het voorbeeld van "Index.md" hierboven.

### Leanpub

Als u de optie inschakelt in {% prefspane Apps %} onder Leanpub/GitBook-ondersteuning, worden bestanden met de naam "Book.txt" automatisch behandeld als Leanpub-indexbestanden. Het oudere "frontmatter:"-formaat wordt ook herkend.

[Leanpub documentation.][lpdocs]

Leanpub Book.txt voorbeeld:

voorzaak:
    Dankbetuigingen.txt
    Voorwoord.txt
    Introductie.txt
    hoofdzaak:
    Markdown.txt
    Voorbeeldboeken.txt
    Afbeeldingen.txt invoegen


### mmd_merge

Voor mmd\_merge vereist Marked dat de eerste regel "#merge" is (een speciale Marked trigger voor mmd\_merge, behandeld als commentaar en genegeerd door andere processors).

[mmd_merge documentation.][mmdm]

mmd_merge voorbeeld:

#samenvoegen
    metadata.txt
    Hoofdstuk-1.md
        sub-hoofdstuk-1-1.md
        sub-hoofdstuk-1-2.md
    Hoofdstuk-2.md
        sub-hoofdstuk-2-1.md
        sub-hoofdstuk-2-2.md
    FAQ.md
    Dankbetuigingen.md

### GitBook

GitBook-opmaak gebruikt een Markdown lijst om de structuur en de inhoudsopgave te maken. Als GitBook-ondersteuning is ingeschakeld in de {% prefspane Apps %} onder Leanpub/GitBook-ondersteuning, zal een bestand met de naam SUMMARY.md worden gelezen en automatisch worden geconverteerd naar het mmd_merge-formaat, waardoor een volledig voorbeeld van uw GitBook-document mogelijk is.

[GitBook documentation.][gbdocs]

GitBook SUMMARY.md voorbeeld:

# Samenvatting

* [Part I](part1/README.md)
        * [Writing is nice](part1/writing.md)
        * [GitBook is nice](part1/gitbook.md)
    * [Part II](part2/README.md)
        * [We love feedback](part2/feedback_please.md)
        * [Better tools for authors](part2/better_tools.md)

GitBook staat toe dat ankers worden gebruikt in de inhoudsopgave SUMMARY.md, maar Marked zal deze negeren en het basisdocument slechts één keer opnemen.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Functies voor het bekijken van documenten met meerdere bestanden

![Included File Boundaries][2]

   [2]: images/includeboundaries.png @2x width=859px height=239px class=center

Wanneer u een document bekijkt dat de bijgevoegde bestanden bevat, kunt u twee functies gebruiken om te helpen bepalen welk bestand u bekijkt.

* **Toetsenbord:** Als u op {% kbd shift I %} drukt, wordt kort een pop-up weergegeven met de titel van het bestand dat momenteel zichtbaar is op de schuifpositie van het voorbeeld.
    * Als u op {% kbd Return %} drukt en vervolgens {% kbd I %} volgt, wordt het weergegeven bestand bewerkt met uw externe editor.
* **Muis:** Door "Toon grenzen van opgenomen bestanden" te selecteren in het tandwielmenu ({% kbd ctrl cmd B %}) wordt een gekleurde balk aan de linkerkant van het voorbeeld toegevoegd, gesegmenteerd om het begin en einde van de opgenomen bestanden weer te geven. Het toont ook geneste omvat. Als u over een gedeelte van deze balk beweegt, wordt de naam weergegeven van het bestand dat het vertegenwoordigt, en als u erop klikt, wordt dat bestand geopend in de door u gekozen editor.