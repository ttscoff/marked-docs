# <%= @title %>

Extraheer en steel stijlen van elke website.

## Wat is de stijlstealer? [what-is-the-style-stealer]

De Style Stealer is een tool waarmee u CSS-stijlen van elke website kunt extraheren en deze kunt toepassen op uw Markdown documenten als [Custom Styles](Custom_Styles.html). Het is perfect voor:

- **Bloggers** die de stijl van hun favoriete websites willen matchen
- **Schrijvers** die documenten moeten maken die passen bij een specifiek merk of publicatie
- **Ontwikkelaars** die snel willen prototypen met bestaande ontwerpsystemen
- **Iedereen** die de look en feel van een goed ontworpen website wil vastleggen

> De Style Stealer is afhankelijk van een site die relatief goed ingedeeld is met duidelijke opmaakverdelingen. Het zal niet op elke site werken, maar het zou op de meeste sites goed moeten werken.

> Voor de beste resultaten voert u een pagina in die zoveel mogelijk tekstinhoud bevat. Als u bijvoorbeeld stijlen uit een blog wilt extraheren, opent u rechtstreeks naar een artikel of bericht, niet naar de hoofdindexpagina.

## Hoe de Stijlstealer te gebruiken [how-to-use-the-style-stealer]

### Stap 1: Open de Stijlstealer [step-1-open-the-style-stealer]

Ga naar de Stijlstealer via **Help** → **Stijlstealer**.

### Stap 2: Voer een URL in [step-2-enter-a-url]

Voer in het URL-veld het adres in van de website waarvan u stijlen wilt extraheren. De Style Stealer werkt met elke publiek toegankelijke website. Als de site zich achter een betaalmuur bevindt, moet u mogelijk inloggen om de inhoud te kunnen extraheren.

![Style Stealer Preview][preview]

  [preview]: images/style-stealer-preview.jpg @2x width=800

### Stap 3: Laden en navigeren [step-3-load-and-navigate]

Klik op **Uitpakken** of druk op {% kbd return  %} om de website te laden. Eenmaal geladen, kunt u:

- **Navigeer** door de site met Command+klik op links
- **Beweeg** over inhoudsgebieden om ze gemarkeerd te zien
- **Klik** op het hoofdinhoudsgebied waaruit u stijlen wilt extraheren

Het hoofdinhoudsgebied dat u selecteert mag alleen koppen, alinea's, lijsten, enz. bevatten. Selecteer geen inhoudsgebied dat menu's, zijbalken of andere overbodige inhoud bevat. Vaak bevindt een kop zich in een andere container dan de reguliere alinea-inhoud. Probeer in deze gevallen eerst de kleinste container te selecteren die beide nog bevat. Als de resultaten slecht zijn, klikt u nogmaals op **Extract** en selecteert u opnieuw alleen de container die de alinea's bevat.

### Stap 4: Stijlen extraheren [step-4-extract-styles]

Wanneer u op het inhoudsgebied klikt, worden de stijlen die op dat gebied van toepassing zijn, geëxtraheerd. Het voorbeeld wordt opnieuw geladen met een algemene pagina waarop alle algemene HTML-elementen worden weergegeven en hoe de geëxtraheerde stijlen daarop worden toegepast.

U kunt deze Custom stijl vervolgens opslaan in uw Custom CSS-map voor gebruik in elk document. Klik op de knop **Opslaan** of druk op {% kbd cmd S %} om op te slaan. De stijl krijgt een naam op basis van het domein van de URL die u heeft ingevoerd.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## Wat wordt geëxtraheerd [what-gets-extracted]

De Style Stealer legt een uitgebreide reeks stijlen vast, waaronder:

### Typografie [typography]

- **Lettertypefamilies** en -groottes voor alle kopniveaus (H1-H6)
- **Paragraaf**-styling inclusief lijnhoogte en -afstand
- **Tekstkleuren** en achtergrondkleuren
- **Lettertypegewichten** en stijlen (vet, cursief, etc.)

### Indeling en afstand [layout-and-spacing]

- **Marges en opvulling** voor alle elementen
- **Rand**-stijlen en kleuren
- **Achtergrondkleuren** inclusief lichaamsachtergronden voor donkere thema's

### Interactieve elementen [interactive-elements]

- **Linkstijlen** inclusief hover- en bezochte staten
- **Knoop** en vormgeving van vormelementen
- **Lijst** stijl (opsommingstekens, cijfers, inspringing)

### Speciale kenmerken [special-features]

- **Eerste alinea** stijl
- **Blockquote**-opmaak
- **Code** en vooraf opgemaakte tekststijl
- **Tabel**-styling
- **Custom lettertypen** en weblettertypen

## Geavanceerde functies [advanced-features]

### Mediablokkering [media-blocking]

De Style Stealer blokkeert automatisch media-inhoud (video's, afbeeldingen, audio) om crashes te voorkomen en zich te concentreren op tekststijl. Dit zorgt voor een soepel extractieproces, zelfs op websites met veel media.

### Pseudo-Selector-ondersteuning [pseudo-selector-support]

De tool legt CSS-pseudo-selectors vast, zoals:

- `:hover` statussen voor links en knoppen
- `:visited` linkstatussen
- `:first-child` alineastijl
- `::first-letter` voor sierdoppen

### Slim filteren [smart-filtering]

De Style Stealer filtert op intelligente wijze het volgende eruit:

- Standaard browserstijlen
- Onnodige leveranciersvoorvoegsels
- Conflicterende of overbodige regels
- Stijlen die tekst onleesbaar maken

### Foutopsporingsmodus [debug-mode]

Schakel de debug-modus in de Style Stealer in om gedetailleerd logboekregistratie van het extractieproces te bekijken. Dit is handig bij het oplossen van problemen of bij het begrijpen welke stijlen worden vastgelegd.

## Tips voor de beste resultaten [tips-for-best-results]

### Kies het juiste inhoudsgebied [choose-the-right-content-area]

- Klik op het **hoofdinhoudsgebied** van de pagina, niet op de kopteksten, zijbalken of voetteksten
- Zoek naar het gebied dat de artikeltekst, blogpost of hoofdinhoud bevat
- Vermijd gebieden met veel JavaScript of dynamische inhoud

### Behandel donkere thema's [handle-dark-themes]

De Style Stealer legt automatisch de achtergrondkleuren van het lichaam vast, waardoor deze perfect is voor het extraheren van donkere themastijlen. Het voorbeeld laat zien hoe uw inhoud eruit ziet met de geëxtraheerde donkere stijl.

### Lettertypeoverwegingen [font-considerations]

- **Weblettertypen** worden vastgelegd en opgenomen in de geëxtraheerde stijlen
  - Lettertypen die worden geladen vanaf een externe URL (bijvoorbeeld Google Fonts) behouden die URL. Lettertypen die vanuit gegevens-URL's worden geladen, worden gedupliceerd in het gegenereerde stylesheet.
- **Systeemlettertypen** vallen netjes terug op verschillende systemen
- **Lettertype laden** kan even duren in het voorbeeld

### Je stijlen testen [testing-your-styles]

Na het opslaan van geëxtraheerde stijlen:

1. Pas ze toe op een testdocument
2. Controleer hoe ze eruit zien met uw daadwerkelijke inhoud
3. Breng aanpassingen aan door:
   1. Open het {% prefspane Style %}
   2. Selecteer de nieuwe stijl in de tabel Custom Stijlen
   3. Klik op Onthullen om het bestand in Finder weer te geven
   4. Open het bestand in een gewone teksteditor (TextEdit werkt in platte tekstmodus) en breng indien nodig aanpassingen aan

## Problemen oplossen [troubleshooting]

### Website wordt niet geladen [website-wont-load]

- Controleer of de URL correct en openbaar toegankelijk is
- Sommige sites kunnen geautomatiseerde toegang blokkeren
- Probeer een andere pagina op dezelfde site

### Stijlen zien er anders uit [styles-look-different]

- De geëxtraheerde stijlen zijn gebaseerd op de specifieke inhoud die u heeft geselecteerd
- Sommige sites gebruiken complexe CSS die mogelijk niet perfect vertaalt
- Gebruik aanvullende CSS of bewerk het stylesheet om fijne aanpassingen te maken

### Ontbrekende stijlen [missing-styles]

- Zorg ervoor dat u het hoofdinhoudsgebied heeft geselecteerd en geen zijbalk of koptekst
- Sommige stijlen kunnen via JavaScript worden toegepast en worden niet vastgelegd
- Controleer de debug-console voor gedetailleerde extractie-informatie

## Sneltoetsen [keyboard-shortcuts]

- {% kbd return  %} - URL laden voor extractie
- {% kbd cmd S %} - Sla de geëxtraheerde stijl op in een Custom Style CSS-bestand
- {% kbd cmd  %}-Klik - Navigeer door koppelingen terwijl u een voorbeeld bekijkt

## Integratie met Custom stijlen [integration-with-custom-styles]

Geëxtraheerde stijlen worden opgeslagen in uw Custom CSS-map en kunnen:

- **Toegepast** op elk document via het menu Stijl
- **Gewijzigd** met behulp van een teksteditor
- **Gedeeld** met anderen door het CSS-bestand te kopiëren
- **Gecombineerd** met andere aangepaste stijlen

Met de Style Stealer kunt u eenvoudig een bibliotheek met prachtige stijlen opbouwen, geïnspireerd op de best ontworpen websites op internet.