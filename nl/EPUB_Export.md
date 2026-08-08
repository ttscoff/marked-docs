# <%= @title %>

Marked exporteert volledig compatibele EPUB-bestanden vanuit uw Markdown-voorbeeld --- opgemaakt met dezelfde ingebouwde en aangepaste thema's die u op het scherm gebruikt, en leesbaar in **Apple Books**, **Kobo** en andere standaard EPUB-lezers.

De typische workflow is **eerst een voorbeeld bekijken, EPUB seconde** exporteren: open of compileer uw document in Marked, kies een thema, proeflezen in de live preview en exporteer vervolgens wanneer het boek klaar is.

## Een EPUB exporteren [exporting-an-epub]

Open de [Export Panel](Exporting.html#drawer) ({% kbd shift cmd e %}) of gebruik **Opslaan als** in het tandwielmenu en kies **EPUB**.

In het dialoogvenster EPUB voor opslaan kunt u het volgende instellen:

* **Titel** --- standaard ingesteld op MultiMarkdown metadata of de bestandsnaam
* **Auteur** --- standaard uw macOS-gebruikersnaam; de laatste auteur die u invoert, wordt onthouden voor de volgende export
* **Datum** --- ISO-formaat; bewerkbaar op tijd besparen
* **Omslagafbeelding** --- optioneel PNG of JPG; Marked genereert een standaard omslagvoorbeeld als er geen is ingesteld

Marked sluit lokale afbeeldingen in de EPUB in en kan afbeeldingen op afstand downloaden, zodat het voltooide bestand op zichzelf staat. Geëxporteerde EPUBs worden gevalideerd als goed opgemaakte XHTML voordat ze worden opgeslagen, waardoor bestanden worden geproduceerd die voldoen aan de EPUB-normen voor distributie en toegankelijkheid.

Zie [Export Profiles](Exporting.html#export-profiles) om EPUB metadata op te slaan en instellingen te exporteren voor herhaald gebruik.

## Styling met ingebouwde thema's [styling-with-built-in-themes]

De **voorbeeldstijl** die voor uw document is geselecteerd, bepaalt de weergave EPUB. Elk ingebouwd Marked thema --- Zwitsers, GitHub, Manuscript en de rest --- kan worden toegepast op EPUB export.

1. Kies een stijl in het stijlmenu van het voorbeeldvenster (of stel een standaard in {% prefspane Style %}).
2. Bekijk typografie, koppen, codeblokken en afbeeldingen in de live preview.
3. Exporteren naar EPUB --- Marked bundelt de CSS van het thema in het EPUB pakket.

Marked past ook exportspecifieke CSS toe bovenop uw voorbeeldthema, zodat elementen zoals voetnoten, tabellen en syntaxisgemarkeerde codeblokken correct worden weergegeven in e-readers. Documenten in de overzichtsmodus gebruiken exportstijlen die voor de overzichten zijn geoptimaliseerd; [Leanpub](Multi-File_Documents.html) `Book.txt` indexen gebruiken automatisch een Leanpub-georiënteerde exportstijl.

I> EPUB lezers negeren bepaalde web-only CSS (vaste positionering, viewport-trucs, enz.). Wat u ziet in de preview van Marked is het doel, maar de layout-engines van e-readers kunnen de spatiëring en lettertypen vereenvoudigen. Test het in Apple Books of uw doellezer voordat u het publiceert.

## Styling met aangepaste thema's [styling-with-custom-themes]

[Custom Styles](Custom_Styles.html) werkt op dezelfde manier voor EPUB als voor preview en PDF:

* Voeg CSS-bestanden toe in {% prefspane Style %} of de [Style Manager](Custom_Styles.html).
* Selecteer het aangepaste thema voordat u exporteert.
* Marked sluit uw stylesheet in in de geëxporteerde EPUB.

Tips voor EPUB-vriendelijke aangepaste CSS:

* Houd lay-outs vloeiend --- gebruik relatieve eenheden en `max-width: 100%` op afbeeldingen (`#wrapper img { max-width: 100%; }` is een goede basislijn).
* Vermijd `@media print` regels voor e-boekstijl; EPUB gebruikt de hoofdschermstijlen plus het exportstijlblad van Marked.
* [Dark Mode](Previewing.html) inversie in preview gebruikt `@media screen` queries; de meeste EPUB-lezers gebruiken het lichte stylesheet, tenzij de reader-app zijn eigen donkere thema toepast.
* Gebruik [Additional CSS](Custom_Styles.html) in Stijlinstellingen om alle thema's in één keer aan te passen (bijvoorbeeld een uniforme lettergrootte voor alle exports).

Voor richtlijnen bij het schrijven, zie [Creating Custom CSS](Writing_Custom_CSS.html).

## Syntaxisaccentuering en wiskunde [syntax-highlighting-and-math]

Als **Inclusief syntaxisaccentuering in export** is ingeschakeld in {% prefspane Export %}, blokkeert code de export met dezelfde syntaxiskleuren als uw voorbeeld. Wiskunde weergegeven met [MathJax](MathJax.html) is opgenomen in de EPUB, zoals van toepassing voor ondersteuning van e-readers.

## Metagegevens in uw bronbestand [metadata-in-your-source-file]

U kunt EPUB metadata instellen in het document in plaats van in het opslagdialoogvenster. Gebruik toetsen in MultiMarkdown-stijl bovenaan een Markdown-bestand (of op een Scrivener-metagegevenspagina):

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` accepteert een pad relatief aan het document of een absoluut pad. PNG en JPG worden ondersteund. Dialoogwaarden overschrijven of vullen ontbrekende metagegevens in tijdens het exporteren.

## Boeken met meerdere bestanden [multi-file-books]

Voor lange werken compileert u hoofdstukken met [Multi-File Documents](Multi-File_Documents.html) --- indexbestanden, Scrivener exports, Leanpub `Book.txt` of indexen in GitBook-stijl. Marked bekijkt de meegeleverde bestanden, bekijkt een voorbeeld van het volledige boek en exporteert één EPUB uit de gecompileerde HTML.

Koppen in het gecompileerde document worden de EPUB [table of contents](Document_Navigation.html) voor navigatie in Apple Books en andere lezers.

## Lezen en publiceren [reading-and-publishing]

Geëxporteerde EPUBs worden rechtstreeks geopend in **Apple Books** (dubbelklik op het bestand of gebruik **Bestand → Toevoegen aan bibliotheek**). Ze werken ook in Kobo, Thorium, Calibre en de meeste EPUB 3-compatibele apps.

### Apple-boeken [apple-books]

Sleep een geëxporteerde `.epub` naar de Boeken-app of voeg deze toe via **Bestand → Importeren**. Custom typografie en albumhoezen uit uw Marked thema worden doorgevoerd. Gebruik Apple Books op Mac, iPad of iPhone om de lay-out te verifiëren voordat u deze deelt.

### Kindle Direct Publishing (KDP) [kindle-direct-publishing-kdp]

EPUB is een geaccepteerd uploadformaat voor [Kindle Direct Publishing](https://kdp.amazon.com/). Exporteer vanuit Marked en upload het bestand `.epub`; Amazon converteert het voor Kindle-bezorging. KDP accepteert ook [DOCX](Working_With_DOCX.html). Zie Amazon's [supported eBook formats](https://kdp.amazon.com/en_US/help/topic/G200634390) voor de huidige vereisten.

**MOBI is niet vereist** voor nieuwe KDP-titels. Marked exporteert MOBI niet.

Optioneel: bekijk een voorbeeld van de Kindle-indeling met de gratis [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) van Amazon voordat je uploadt.

## Verwant [related]

* [HTML Export](HTML_Export.html) --- standalone HTML met ingebedde stijlen en afbeeldingen
* [Exporting](Exporting.html) --- exportpaneel, profielen en andere formaten
* [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) --- bekijk een voorbeeld van de workflow vóór het exporteren
* [Custom Styles](Custom_Styles.html) en [Custom Style Generator](Custom_Style_Generator.html)
* [Multi-File Documents](Multi-File_Documents.html) --- boeken- en hoofdstukindexen
* [AppleScript export](AppleScript_Support.html) --- automatiseer de export van EPUB