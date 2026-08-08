# <%= @title %>

Uw Markdown omzetten in een voltooid document.

## Exporteren na voorbeeld [export-after-preview]

Het voorbeeld van Marked is de basis voor de export --- wat u ziet in het voorbeeldvenster is wat u krijgt in PDF, DOCX, EPUB en andere formaten (modulo exportspecifieke instellingen zoals marges, kopteksten en paginering). Stel uw stijl in en proeflees eerst in de voorbeeldweergave en exporteer vervolgens wanneer het document gereed is. Zie [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) voor de volledige voorbeeldworkflow.

## Het exportpaneel [drawer]

![Export Panel][export-panel]

Het **Exportpaneel** is een toetsenbordgestuurd paneel in spotlight-stijl dat snelle toegang biedt tot alle exportopties. Open het door op het exportpictogram in de statusbalk te klikken of door op {% kbd shift cmd e %} te drukken.

![Export Button][expbut]

Met het Exportpaneel kunt u uw document opslaan als HTML, PDF van één pagina, gepagineerd PDF, RTF pakket of een Microsoft Word DOC- of DOCX-bestand. U kunt ook opslaan in een nieuw Markdown bestand (Marked-specifieke functies worden weergegeven en de resultaten ervan inbegrepen), een Open Document (ODT), of als OPML voor gebruik in andere toepassingen.

## Kopieer HTML [copyhtml]

Gebruik de functie HTML kopiëren om de HTML broncode voor uw voorbeeld probleemloos op uw klembord te plaatsen. Je kunt het selecteren in het tandwielmenu, of druk gewoon op {% kbd shift cmd C %}. De gekopieerde HTML zal een fragment zijn dat klaar is om in een blog, forum of HTML document te worden ingevoegd.

U hoeft niet in de bronweergave te zijn om te kopiëren. Met de focus op het voorbeeld (klik erop), typt u gewoon {% kbd shift cmd C %} en u ziet een pop-upbericht waarin u wordt geïnformeerd dat de bron op uw klembord staat.

## Opslaan HTML [save-html]

![][exporthtmlaccessory]



Met de opdracht Save HTML (toegankelijk via het tandwielmenu of door eenvoudigweg **{% kbd cmd S %}**) te typen, kunt u een volledig document opslaan, klaar om te delen of te publiceren.

U kunt optioneel een van de stijlen van Marked (of een van uw [custom styles][custom]) in uw export opnemen, waardoor u een kant-en-klaar document krijgt waarin de benodigde opmaak al is ingesloten.

Bovendien kunt u ervoor kiezen om alle lokale afbeeldingen in het document in te sluiten in de geëxporteerde HTML, zodat u over een zelfstandig document beschikt dat overal kan worden gehost zonder dat u de afbeeldingen ermee hoeft te verplaatsen. Dit werkt alleen met afbeeldingen waarnaar op uw lokale schijf wordt verwezen met relatieve of absolute paden. Vermijd het gebruik van `file:///` paden als u van deze functie gebruik wilt maken.

## Exporteer Markdown naar PDF op Mac [export-markdown-to-pdf-on-mac]

Print/PDF Preview ({% kbd cmd P %}) zal een standaard afdrukdialoogvenster openen. Elke voorbeeldstijl in Marked heeft zijn eigen bijbehorende afdrukstijlen die achtergronden verwijderen, lettergroottes wijzigen en randen aanbrengen. Het voorbeeld wordt afgedrukt op basis van de momenteel geselecteerde stijl.

Prominent in het afdrukdialoogvenster zijn de knoppen PDF en Voorbeeld. PDF biedt u verschillende opties voor het exporteren naar PDF (op basis van uw beschikbare applicaties) en Preview exporteert een PDF-versie rechtstreeks naar Preview.app, waar u deze kunt opslaan of e-mailen.

Afdrukken naar PDF met deze methode omvat paginering. Bij het afdrukken op papier of PDF kunnen pagina-einden handmatig worden ingevoegd met behulp van [<!--MKPH1--> syntax][break] of door opties in te stellen in {% prefspane Export %} om kopteksten van niveau één en/of niveau twee als sectieverdelers te gebruiken.

Er is ook een voorkeur voor het omzetten van horizontale lijnen (`<hr>`) in pagina-einden bij het afdrukken. Als u dit doet, wordt de regel die door de tag is gemaakt, vervangen door een pagina-einde, waardoor deze uit de uiteindelijke uitvoer wordt verwijderd. Het voorbeeld wordt niet beïnvloed door deze instelling.

![Print Margins][printmargins]

Paginamarges kunnen worden ingesteld in {% prefspane Export %} en hebben invloed op de afdruk- en gepagineerde PDF-uitvoer.

U kunt de marge-instellingen per document overschrijven met behulp van de metadatasleutel `Margins:`. Waarden worden geïnterpreteerd als punten; eenheidsachtervoegsels zoals `px`, `pt` en `em` worden genegeerd. Gebruik twee cijfers voor verticale en horizontale marges (`10 20`), of vier cijfers voor boven, rechts, onder en links (`10, 20, 10, 20` of `10 20 10 20`). Marges metagegevens overschrijven {% prefspane Export %} instellingen.

### Kop- en voetteksten [headers-and-footers]

Kop- en voetteksten gedefinieerd in de {% prefspane Export %} verschijnen bovenaan en onderaan elke pagina die wordt afgedrukt of opgeslagen in gepagineerde PDF, en in DOCX export. U kunt elke gewenste tekst linksboven, middenboven, rechtsboven, linksonder, middenonder en rechtsonder plaatsen. Gecentreerde tekst wordt gecentreerd op de pagina uitgelijnd. De volgende variabelen worden bij gebruik in de strings vervangen:

%title = Documenttitel
    %date = Huidige datum
    %tijd = Huidige tijd
    %pleeftijd = Huidig paginanummer
    %totaal = Totaal paginanummer
    %path = Bestandssysteempad naar document
    %filename = Alleen de bestandsnaam van het document
    %basename = De bestandsnaam zonder extensie
    %logo/%image = Een logo dat is ingesteld in het afbeeldingsvak in de koptekst-/voettekstvoorkeuren
    %%(tekst) = Tekst die alleen op de eerste pagina moet worden afgedrukt
    %h1/h2/h3/h4/h5/h6 = Sectietitels gebaseerd op Markdown headers
    %sep(X) = Tekst die tussen sectietitels moet worden geplaatst als er een subsectie bestaat

**Afgedrukt en gepagineerd PDF** `%h1`--`%h6` wordt opgelost met behulp van de paginering van Marked, zodat elke pagina de kophiërarchie weergeeft die zichtbaar is op die pagina. De metadatavariabelen `%sep(X)` en `%md_*` worden ook ondersteund in de uitvoer print/PDF.

**DOCX export** sluit `%logo`/`%image` in de kop- of voettekst van Word in (geschaald naar ongeveer 50px hoog, passend afdrukvoorbeeld). Tijdelijke aanduidingen voor kopteksten worden Word **STYLEREF**-velden die verwijzen naar de geëxporteerde `Heading 1`--`Heading 6` stijlen. Word werkt deze velden bij wanneer het document wordt geopend, op basis van de eigen lay-out en pagina-einden van Word --- en niet de voorbeeldpaginering van Marked. `%md_*` metadatavariabelen worden één keer vervangen tijdens het exporteren, hetzelfde als in print/PDF. `%sep(X)` wordt niet geconverteerd in DOCX kop-/voetteksten.

`%title` zal elke "Titel:"-info gebruiken die is gedefinieerd in MultiMarkdown Metadata-headers, anders zal het terugvallen op de bestandsnaam zonder de bestandsextensie. Om een ​​titel te definiëren met behulp van MMD Metadata, plaatst u het volgende op de eerste regel van het document:

Titel: De titel van uw document

Volg de regel met een lege regel (of andere metagegevens die u wilt definiëren, gevolgd door een lege regel).

U kunt ook elke MMD Metadatasleutel als variabele gebruiken door er `%md_` aan toe te voegen en de woorden van de sleutel te combineren als een tekenreeks in kleine letters. Als uw document bijvoorbeeld bovenaan een metagegevenssleutel heeft, zoals:

Funky Monkey: De meest funky aap

Als u vervolgens `%md_funkymonkey` in een koptekstveld gebruikt, wordt "De meest funky aap" in het geëxporteerde document op de locatie van die koptekst geplaatst. Documenten die die specifieke sleutel niet bevatten, laten het veld leeg, waardoor u selectief kopteksten kunt toevoegen op basis van metagegevens.

Zie [Date and Time Formats](Exporting.html#dateandtimeformats) voor `%date` en `%time` formaatcodes.

De instelling "Paginanummering offset" kan worden gebruikt om aan te passen bij welk nummer de paginanummers beginnen. Als u bijvoorbeeld een inhoudsopgave op de eerste pagina hebt en wilt dat de nummering op de tweede pagina begint als pagina 1, stelt u de verschuiving in op -1. Pagina 2 wordt nu pagina 1 in de kop-/voettekst (`%page`) en het totaal aantal pagina's (`%total`) wordt dienovereenkomstig aangepast.

U kunt ook een kop-/voettekstlettertype voor een specifiek document opgeven door de metagegevens MMD bovenaan het bestand te gebruiken:

Koptekstlettertype: Mensch

Houd er rekening mee dat als u een lettertypefamilienaam gebruikt, er een standaardlettertype wordt geselecteerd. U kunt een variatie opgeven door de systeemnaam van het lettertype te gebruiken. In het geval van Helvetica Neue Ultralight zou u bijvoorbeeld "Header Font: Helvetica NeueUltralight" gebruiken.

Bovendien kunt u per document een lettergrootte voor de kop-/voettekst opgeven met de metagegevens:

Lettergrootte koptekst: 10

### Datum- en tijdformaten [dateandtimeformats]

De velden **Datumnotatie** en **Tijdnotatie** in de {% prefspane Export %} bepalen hoe `%date` en `%time` worden weergegeven in kop- en voetteksten. Beide velden gebruiken formatcodes in strftime-stijl: een `%` gevolgd door een letter. Letterlijke tekst (zoals `-`, `:` of spaties) wordt ongewijzigd gekopieerd.

**Voorbeelden**

%m-%d-%Y → 20-06-2026 (standaard datumnotatie van Marked)
    %I:%M %p → 15:45 (de standaard tijdnotatie van Marked)
    %Y-%m-%d → 20-06-2026
    %B %d, %Y → 20 juni 2026
    %a %H:%M → Vr 15:45

**Gemeenschappelijke formaatcodes**

| Code | Voorbeeld | Beschrijving |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Viercijferig jaartal |
| `%y` | 26 | Tweecijferig jaartal |
| `%m` | 06 | Maand (01--12) |
| `%B` | Juni | Volledige maandnaam |
| `%b` | juni | Afgekorte maandnaam |
| `%d` | 20 | Dag van de maand (01--31) |
| `%e` | 20 | Dag van de maand (met spaties) |
| `%A` | Vrijdag | Volledige naam van de weekdag |
| `%a` | Vr | Afgekorte naam van de weekdag |
| `%H` | 15 | Uur, 24 uur (00--23) |
| `%I` | 03 | Uur, 12 uur (01--12) |
| `%M` | 45 | Minuut (00--59) |
| `%S` | 07 | Tweede (00--59) |
| `%p` | PB | AM of PM |
| `%x` | (land) | Voorkeursdatum van locale |
| `%X` | (land) | Voorkeurstijd van locale |
| `%c` | (land) | Voorkeursdatum en -tijd van de landinstelling |

**Afgedrukt en gepagineerd PDF** ondersteunen de volledige strftime-stijl hierboven, plus aanvullende codes zoals `%j` (dag van het jaar), `%U`/`%W` (weeknummer), `%z` (tijdzone-offset) en `%Z` (tijdzonenaam). Zie de [Open Group strftime specification](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) voor een volledige referentie.

**DOCX export** ondersteunt de codes uit de bovenstaande tabel. Minder gebruikelijke codes kunnen worden genegeerd of ongewijzigd worden doorgegeven.

Gebruik **Standaardformaten herstellen** in {% prefspane Export %} om te resetten naar `%m-%d-%Y` en `%I:%M %p`.

### Kop- en voetteksten per document [per-document-headers-and-footers]

U kunt kop- en voetteksten per document opgeven met behulp van MultiMarkdown-metagegevens helemaal bovenaan het document:

Printkop links: %titel
    Printkopcentrum: %basisnaam
    Printkop rechts: %date
    Voettekst rechts afdrukken: %pleeftijd/%totaal

Deze zullen alle instellingen in de voorkeuren overschrijven. Houd er rekening mee dat als u een andere processor dan MultiMarkdown gebruikt en niet wilt dat uw kopteksten in het document zelf verschijnen, u HTML opmerkingen kunt gebruiken, waarbij u ervoor zorgt dat u een lege regel achterlaat voordat de opmerking wordt gesloten:

<!--
    Printkop links: %titel
    Printkopcentrum: %basisnaam
    Printkop rechts: %date

-->

## Opslaan PDF [save-pdf]

Met deze optie wordt uw voorbeeld rechtstreeks opgeslagen in een PDF bestand op uw schijf. Uw document wordt in zijn geheel weergegeven, zonder pagina-einden. Om paginering in uw uitvoer op te nemen, gebruikt u de Print/PDF opties in [Export Panel](#drawer).

## RTF exportopties [rtfexportoptions]

Marked kan RTF-gegevens (Rich Text Format) rechtstreeks naar uw klembord exporteren. Kies gewoon de opdracht Copy Rich Text in het tandwielmenu.

Marked kan uw bestand ook opslaan als een **RTFD**-bestand (Rich Text Format). De RTFD-indeling is een bundelindeling die een RTF-bestand en eventuele afbeeldingen in het document bevat.

## DOCX exporteren [docx-export]

Exporteren als DOCX zal een geldig Microsoft Word-document creëren, met elementen zoals koppen, kop-/voetteksten, nadruk, lijsten, enz., allemaal toegewezen aan geldige Word-stijlen. Hierdoor past u eenvoudig uw eigen thema toe in Word.

Zie [Working with DOCX][DOCX] voor meer details over het importeren en exporteren van Word.

## Exporteer Markdown naar EPUB [export-markdown-to-epub]

Marked kan 100% geldige, 100% toegankelijke EPUB documenten exporteren. Selecteer het exporttype EPUB, specificeer metagegevens zoals titel, auteur en datum en voeg optioneel een omslagfoto toe. Het opgeslagen bestand is leesbaar in elke EPUB viewer.

De metagegevens die nodig zijn voor de EPUB-export kunnen in het bestand zelf worden opgenomen, of het nu een Markdown-document, Scrivener-bestand (inclusief een `metadata` pagina) of een ander boekformaat is. De te gebruiken sleutels zijn:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

De sleutel Omslagafbeelding kan een pad bevatten dat relatief is aan het basisdocument, of een absoluut pad. PNG- of JPG-bestanden zijn acceptabel.

Als de titel niet is ingesteld, wordt standaard de bestandsnaam van het originele document gebruikt. Als de auteur niet is ingesteld, wordt standaard de volledige naam van uw macOS-gebruiker gebruikt.

De datum wordt altijd ingesteld op de huidige datum en kan momenteel niet worden gewijzigd met metagegevens. Het kan echter worden gewijzigd op het moment van opslaan, zolang de opmaak (ISO) intact blijft.

### Publiceren op Amazon Kindle (KDP) [publishing-to-amazon-kindle-kdp]

EPUB is een open indeling die door veel leesapps en -winkels (Apple Books, Kobo en anderen) wordt gebruikt, niet alleen door Kindle. Als je publiceert via [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), exporteer dan EPUB van Marked en upload dat bestand naar KDP. Amazon converteert het naar zijn eigen Kindle-bezorgformaat (KFX) voor lezers.

KDP accepteert verschillende manuscriptformaten, waaronder EPUB en DOCX (die Marked ook kan exporteren). Zie Amazon's [supported eBook formats](https://kdp.amazon.com/en_US/help/topic/G200634390) en [eBook manuscript formatting guide](https://kdp.amazon.com/en_US/help/topic/G200645680) voor vereisten.

**MOBI is niet vereist.** KDP accepteert niet langer MOBI-uploads voor nieuwe titels (inclusief boeken met een vaste lay-out, vanaf maart 2025). Marked exporteert MOBI niet, en je hebt geen apart "Kindle"- of Mobipocket-bestand nodig voor KDP. Als je de voorkeur geeft aan de lay-outtools van Amazon, kun je ook een boek voorbereiden met [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), waarmee KPF-bestanden worden geproduceerd.

Voordat je gaat uploaden, wil je misschien controleren hoe je EPUB eruit zal zien op Kindle-apparaten met behulp van de gratis [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) van Amazon. Dat is optionele software van derden van Amazon, geen onderdeel van Marked.

## Profielen exporteren [export-profiles]

Met exportprofielen kunt u verschillende sets exportvoorkeuren opslaan en snel schakelen tussen. Dit is vooral handig als u regelmatig documenten exporteert voor verschillende doeleinden, bijvoorbeeld één profiel voor afdrukklare PDFs met specifieke marges en kopteksten, en een ander voor webklare HTML met ingesloten stijlen.

### Exportprofielen gebruiken [using-export-profiles]

Wanneer u Marked voor het eerst start, wordt er automatisch een 'Standaard'-profiel gemaakt met uw huidige exportinstellingen. U kunt profielen zien en selecteren in de exportdialoogvensters (PDF Exporteren, Opslaan HTML, enz.) met behulp van het profielpop-upmenu bovenaan het dialoogvenster.

**Een nieuw profiel aanmaken:**

1. Pas uw exportinstellingen aan in de {% prefspane Export %} of in een exportdialoogvenster
2. Klik in het exportdialoogvenster op het profielpop-upmenu en kies "Profiel toevoegen..."
3. Voer een naam in voor uw profiel (bijvoorbeeld 'Afdrukkwaliteit' of 'Webexport')
4. De huidige instellingen worden als dat profiel opgeslagen

**Een profiel laden:**

- Selecteer een profiel uit het pop-upmenu in een exportdialoogvenster
- Alle exportinstellingen worden onmiddellijk bijgewerkt zodat ze overeenkomen met de opgeslagen waarden van dat profiel

**Wijzigingen aan een profiel opslaan:**

- Nadat u wijzigingen heeft aangebracht in de exportinstellingen, verschijnt er een knop 'Opslaan' naast de profielpop-up
- Klik op "Opslaan" om het huidige profiel bij te werken met uw wijzigingen
- De knop is alleen ingeschakeld als er niet-opgeslagen wijzigingen zijn

**Profielen beheren:**

- Kies "Profielen beheren..." in het profielpop-upmenu om het profielbeheervenster te openen
- Van daaruit kunt u:
  - **Hernoem** profielen door te dubbelklikken op de naam
  - **Dupliceer** een profiel om op basis daarvan een nieuw profiel te maken
  - **Verwijder** profielen (het "Standaard" profiel kan niet worden verwijderd)
  - Bekijk alle beschikbare profielen in een lijst

### Wat exportprofielen vastleggen [what-export-profiles-capture]

Exportprofielen slaan alle exportgerelateerde voorkeuren op, waaronder:

- **PDF Instellingen**: Paginagrootte, marges, kop-/voetteksten, lettertypen, pagina-einden, inhoudsopgave
- **HTML Exporteren**: insluiten van stijl, insluiten van afbeeldingen, accentueren van syntaxis, wiskundige weergave
- **Markdown Verwerking**: tekstterugloop, linkopmaak, processorregels
- **CriticMarkup**: Exporttype en verwerkingsopties
- **Syntaxisaccentuering**: taaldetectie en accentuering van voorkeuren
- **Wiskundige weergave**: MathJax/KaTeX integratie en nummering van vergelijkingen
- **Beeldverwerking**: insluitingsopties, kopieergedrag, padinstellingen
-**Typografie**: woordafbreking, weduwen/wezen, lettergroottes
- **Exportgedrag**: voorkeuren voor bestandsnaamgeving, conflictoplossing

Profielen werken voor alle exporttypen: Markdown, HTML, Continu PDF, Gepagineerd PDF, EPUB, DOCX, ODT, TextBundle, RTF en OPML.

### Profielopslag [profile-storage]

Profielen worden opgeslagen in uw map Applicatieondersteuning op:

~/Bibliotheek/Applicatieondersteuning/Marked/ExportProfiles.plist

Dit betekent dat uw profielen blijven bestaan, zelfs als u de app-voorkeuren opnieuw instelt, en dat ze app-updates overleven. U kunt een back-up van dit bestand maken om uw profielen tijdens installaties te behouden.

### Tips voor het gebruik van exportprofielen [tips-for-using-export-profiles]

- **Maak profielen voor algemene workflows**: als u regelmatig exporteert voor print of web, maak dan voor elk afzonderlijk profielen aan
- **Gebruik beschrijvende namen**: profielnamen zoals "Print - Letter" of "Web - Embedded Styles" maken duidelijk waar elk profiel voor is
- **Regelmatig opslaan**: de knop 'Opslaan' verschijnt telkens wanneer u wijzigingen heeft aangebracht. Klik erop om uw aanpassingen te bewaren
- **Begin met bestaande profielen**: gebruik "Dupliceren" in het beheervenster om variaties op bestaande profielen te maken in plaats van helemaal opnieuw te beginnen

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_With_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center