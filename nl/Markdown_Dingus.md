# <%= @title %>

De Markdown Dingus is een gespecialiseerd testhulpmiddel dat hierbij helpt
u begrijpt hoe verschillende Markdown-verwerkers met uw gegevens omgaan
inhoud. Het biedt een interface met drie panelen waar u kunt
bewerk Markdown, bekijk de gegenereerde HTML bron en bekijk de
tegelijkertijd een voorbeeld weergegeven.

De Dingus deelt een handling op laag niveau met die van Marked
preview, zoals speciale behandeling van afgeschermde codeblokken.
Het voert __niet__ [Custom Rules](Custom_Processor.html) uit
(Dirigent). Het gebruikt de meeste standaardinstellingen en negeert instellingen
zoals "GitHub nieuwe regels" en "GitHub selectievakjes", dus de
resultaat kan afwijken van wat u ziet in een normale Marked
voorbeeld.

## Custom Regels zijn niet van toepassing

De Dingus is een __processor-sandbox__: uw Markdown gaat
rechtstreeks naar de ingebouwde processor van uw keuze (MultiMarkdown,
CommonMark (GFM), Discount of Kramdown). [Custom Rules](Custom_Processor.html)
voer daar nooit uit - geen voorbewerkingsacties, regels zoeken/vervangen,
shell-opdrachten, tekst/bestand invoegen of andere Conductor-stappen.

In een normaal voorbeeld kunnen Custom Regels de Markdown wijzigen
Stel vóór het renderen stijlen in, injecteer CSS of JavaScript, en
meer. Niets van dat alles gebeurt wanneer u in de Dingus bewerkt.
Het wijzigen van de Custom regels terwijl de Dingus open is, gebeurt niet
werk de preview bij.

De Dingus __kan__ dezelfde [preview CSS styles](Custom_Styles.html) gebruiken
als het hoofdvenster (via het stijlmenu in het uitvoerpaneel).
Dat is slechts schijn; het is niet hetzelfde als het uitvoeren van Custom
Regels.

__Open in Dingus__ vanuit een voorbeeld laadt het document
huidige Markdown buffer. Als Custom Regels al actief waren wanneer
dat bestand is geopend in Marked, u kunt de effecten ervan zien in
de tekst (bijvoorbeeld tekst die door een regel is ingevoegd), maar de
Dingus past de regels niet opnieuw toe terwijl u typt. Om Custom te testen
Regels, gebruik een standaard Marked voorbeeld of sla op vanuit de Dingus
en open het bestand met __Open in Marked__.

## Wat is een "Dingus"?

Een "dingus" is een term die is ontleend aan webontwikkeling
verwijst naar een eenvoudige testtool of sandbox-omgeving. De
Met Markdown Dingus kun je experimenteren met de syntaxis van Markdown en
zie meteen hoe verschillende processors het interpreteren.

## Toegang tot de Dingus

De Markdown Dingus is toegankelijk via
[<!--MKPH0-->][2]. Het is bijzonder
handig wanneer u:

* Nieuwe Markdown syntaxis leren
* Problemen met weergave oplossen
* Kiezen tussen verschillende processors
* Schrijven van documentatie die voor meerdere doeleinden moet werken
  systemen

## Indeling met drie panelen

![][1]

Het venster Dingus is verdeeld in drie gesynchroniseerde vensters:

### 1. Markdown Invoer (linkerdeelvenster)

* __Syntaxisaccentuering__: uw Markdown is gemarkeerd met
  kleuren om structuur duidelijk te maken
* __Live bewerken__: typ en zie de wijzigingen direct doorgevoerd
  in de andere ruiten
* __Groot lettertype__: 21pt Menlo-lettertype voor comfortabel bewerken

__Vervolgkeuzelijst Opties__ (rechtsboven in het linkerdeelvenster): The
Met het menu **Opties** kunt u schakelen tussen:

* __Laat regelnummers zien__: Toont een rugmarge aan de linkerkant met
  één regelnummer per alinea (omhulde regels tellen als één
  lijn).
* __Onzichtbare tonen weergeven__: Toont spaties als middenpunten (·), tabs als
  een pijl naar rechts (→) en nieuwe regels als regelterugloop
  symbool (↵) in lichtgrijs, zodat u verdwaalde dieren kunt zien
  witruimte.
* __Gremlins markeren__: Zet een lichtrode achtergrond op
  niet-ASCII-tekens (bijvoorbeeld gekrulde aanhalingstekens, emoji) en een donkere
  rode achtergrond op problematische onzichtbare karakters (bijv.
  spaties met een breedte van nul). Normale tab- en nieuweregeltekens zijn dat wel
  niet gemarkeerd.

Uw keuzes worden opgeslagen en hersteld de volgende keer dat u opent
de Dingus.

__Zoekbalk__: Druk op **⌘F** om de zoekbalk onder de te tonen
Label "Markdown Invoer". U kunt zoeken en vervangen in de
editor, gebruik **⌘G** voor Zoek Volgende en **⇧⌘G** voor Zoeken
Vorige en vervang één of alle overeenkomsten. Druk op de sluiting
of nogmaals **⌘F** om de zoekbalk te verbergen.

### 2. HTML Bron (middelste deelvenster)

* __Generated HTML__: Zie precies wat HTML is geselecteerd
  verwerker creëert
* __Syntaxis gemarkeerd__: HTML heeft een kleurcode voor het gemak
  lezen

### 3. Gerenderd voorbeeld (rechterdeelvenster)

* __Live Preview__: bekijk hoe uw Markdown er wanneer zal uitzien
  weergegeven
* __Emoji-ondersteuning__: GitHub-stijl emoji's zoals `:zzz:` zijn
  omgezet naar afbeeldingen
* __Automatisch scrollen__: scrolt automatisch om uw
  huidige bewerkingspositie

## Bewerken in de Dingus

Het Markdown Invoerpaneel bevat slimme bewerkingsfuncties
maak schrijven Markdown sneller en natuurlijker.

### Slimme nieuwe regel (Return-sleutel)

Als u op Return drukt, past u zich aan de huidige regel aan:

* __Lijsten__: op een lijstregel (`-`, `*` , `+` of `1.` ),
  voegt een nieuw lijstitem in met de juiste markering. Genummerd
  lijsten gaan verder met het volgende nummer.
* __Blockquotes__: Op een regel die begint met `>`, wordt een
  nieuwe blockquote-regel.
* __Codehekken__: Op een lijn met drie of meer backticks
  (bijv. ` ``` `), voegt een lege regel in tussen de opening
  en hekken sluiten.
* __Andere regels__: Voegt een normale nieuwe regel in.

### Karakterkoppeling

Wanneer u een openingsteken typt, wordt de editor automatisch weergegeven
voegt het slotteken in en plaatst de cursor ertussen
zij. Ondersteunde paren: `"` `'` `(` `[` `` ` `` `<` .

* __Met selectie__: Plaatst de geselecteerde tekst in het paar.
* __Zonder selectie__: Voegt het paar met de cursor in
  tussen hen.
* __Type-over__: als het volgende teken al het
  scheidingsteken sluiten; als u het nogmaals typt, wordt de cursor voorbij verplaatst
  in plaats van een duplicaat in te voegen.
- __Spatie in leeg paar__: Als de cursor tussen een leeg paar staat (bijvoorbeeld `(|)`), vervangt het typen van een spatie het afsluitende teken door een spatie.

### Sneltoetsen

| Sneltoets | Actie |
|:---------------------|:----------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
| **⌘F** | Toon of verberg de zoekbalk in het Markdown Invoervenster |
| **⌘G** | Zoek volgende (wanneer de zoekbalk zichtbaar is) |
| **⇧⌘G** | Zoek vorige (wanneer de zoekbalk zichtbaar is) |
| **⌘B** | Vet: selectie omsluiten in `**` of `**\|**` invoegen met de cursor tussen |
| **⌘I** | Cursief: selectie omsluiten in `_` of `_\|_` invoegen met cursor tussen |
| **⇧⌘L** | Cycluslijstmarkering (ongeordend ↔ geordend) |
| **Tabblad** | Regel- of lijstitem inspringen |
| **Shift+Tab** | Regel- of lijstitem uitspringen |
| **⌃⌘→** | Regel- of lijstitem inspringen (hetzelfde als Tab) |
| **⌃⌘←** | Regel- of lijstitem uitspringen (hetzelfde als Shift+Tab) |
| **⌃⌘↑** | Alinea naar boven verplaatsen (paragraaf inclusief nieuwe regel knippen, één regel naar boven plakken) |
| **⌃⌘↓** | Alinea naar beneden verplaatsen (paragraaf inclusief nieuwe regel knippen, één regel naar beneden plakken) |
| **⌘K** | Een Markdown-link invoegen of omsluiten: selectie omsluiten als `[text]()` en de cursor in de URL plaatsen, of `[]()` invoegen met de cursor tussen de haakjes als er geen selectie is |
| **F6** | Magische referentielink: selectie omsluiten als `[text][n]` en een `[n]: `-definitie aan het einde van het document toevoegen; wanneer de cursor op een bestaande referentie staat, springt tussen inline markering en definitie |
| **F7** | Magische voetnoot: `[^n]` invoegen bij de cursor (of na het huidige woord) en een bijbehorende `[^n]: `-definitie aan het einde van het document toevoegen; wanneer de cursor op een bestaande voetnoot staat, springt tussen markering en definitie |
| **⌘U** | Uitvoervenster schakelen (Bron/Voorbeeld) |
| **⌥⌘↑** | Selectie uitbreiden: woord → binnenste/buitenste scheidingstekens → zin → alinea → aaneengesloten blok (zoals een tabel of codeblok) → omsluitende lijst/blokquote/codeblok → document |
| **⌥⌘↓** | Contractselectie terug naar beneden via dezelfde niveaus naar de oorspronkelijke cursorpositie |

Tab/Shift+Tab (en ⌃⌘←/⌃⌘→) respecteren de lijststructuur en
blockquotes: ze laten lijstitems inspringen/uitspringen en voegen or toe
verwijder `>` uit blockquote-regels. Paragraaf omhoog/omlaag verplaatsen
selecteert de gehele paragraaf onder de cursor (inclusief de bijbehorende paragraaf).
achterliggende nieuwe regel), knipt het en plakt het boven of onder de
aangrenzende alinea, zodat alinea's niet samenvloeien.

### Magische links en voetnoten (F6 / F7)

De Dingus-editor kan __referentielinks__ en
__voetnoten__ voor u maken, wijst automatisch het volgende beschikbare nummer toe
en voegt de bijbehorende definitie aan het einde van het document toe.

* __F6 (magische referentielink)__: Met geselecteerde tekst wordt de
  selectie omsloten als `[text][n]` en wordt aan het einde van het document een nieuwe
  `[n]: `-regel toegevoegd, zodat u de URL kunt typen. Voor het maken van een
  nieuwe referentielink is een selectie vereist. Staat de cursor al
  op een referentielink of de definitie ervan, dan springt **F6**
  tussen inline markering en definitie (of maakt de definitie aan als die ontbreekt).
* __F7 (magische voetnoot)__: Voegt een genummerde voetnootmarkering
  `[^n]` in bij de cursor---of na het huidige woord wanneer de cursor daarin staat---en voegt `[^n]: ` toe met de
  geselecteerde tekst als voetnoottekst wanneer er een selectie is. Staat de cursor op een bestaande voetnootmarkering
  of definitie, dan springt **F7** tussen beide.

Referentie- en voetnootnummers worden automatisch gekozen, zodat u geen ID's
handmatig hoeft bij te houden. Geen van beide sneltoetsen werkt
in omheinde of ingesprongen codeblokken.

### Slim URL plakken

Wanneer u plakt, bevat het klembord een URL van het formulier
`protocol://...` zonder spaties:

* __Met een selectie__: de selectie wordt omgezet in een
  Markdown link: `[selected text](url)` .
* __Zonder selectie__: de URL wordt ingevoegd als een
  zelfkoppeling: `<url>` .

Dit maakt het gemakkelijk om gekopieerde URL's om te zetten in links zonder
handmatig typen.

### Slimme selectie (⌥⌘↑ / ⌥⌘↓)

De Dingus editor ondersteunt __semantische selectie-uitbreiding__:

* __⌥⌘↑__ begint bij het dakje en breidt de selectie uit
  via:
	- het huidige woord
	- binnenste en buitenste afgebakende inhoud (aanhalingstekens, haakjes,
   haakjes en afgeschermde codeblokken)
	- de huidige zin
	- de huidige paragraaf
	- het aaneengesloten, niet-lege lijnenblok (bijvoorbeeld a
   hele tabel of codeblok met meerdere regels zonder lege regels)
	- het omsluitende lijstitem, blockquote of codeblok
	- het gehele document
* __⌥⌘↓__ loopt terug naar beneden door dezelfde niveaus tot het
  keert terug naar de oorspronkelijke cursorpositie.

Elke druk gaat altijd naar een strikt grotere of kleinere waarde
selectie, zodat u nooit "no-op"-toetsaanslagen krijgt terwijl u werkt
uitbreiden of krimpen.

## De Dingus gebruiken als editor

De Dingus is niet bedoeld om een volledige tekst te vervangen
editor, maar het kan erg handig zijn voor __snelle bewerkingen met een
live preview__, vooral als je precies wilt zien hoe
veranderingen zullen opleveren. Al het tekstbewerkingsgedrag
beschreven in [Editing in the Dingus][3] is hier van toepassing.

### Een bestand openen/een nieuw bestand maken

* __Maak een nieuw bestand in de Dingus__
	- Kies __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Wanneer u hierom wordt gevraagd, kiest u __Dingus__ om een nieuw, niet-opgeslagen bestand te starten
   Dingus document.
	- Nieuwe Dingus documenten worden geopend met geselecteerde voorbeeldinhoud;
   begin gewoon met typen om het te vervangen.
* __Open een bestaand bestand in de Dingus__
	- Gebruik __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), of
   terwijl het venster Dingus actief is, klikt u op __Open…__ in de status
   balk. De opdracht opent dan indien nodig het venster Dingus
   toont het paneel Openen.
	- Kies een ondersteund bestand met platte tekst/Markdown; zijn
   inhoud zal de huidige Dingus buffer vervangen.
* __Open een Marked voorbeelddocument in de Dingus__
	- Gebruik in een normaal voorbeeldvenster __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E).
	- De Markdown van het huidige document wordt in de Dingus geladen
   zodat u kunt experimenteren zonder het originele bestand aan te raken
   totdat u ervoor kiest om op te slaan. Custom Regels worden niet toegepast
   de Dingus; zie [Custom Rules do not apply](#custom-rules-do-not-apply).

### Een bestand opslaan

* __Wijzigingen in het huidige bestand opslaan__
	- Klik in het venster Dingus op __Opslaan__ in de statusbalk,
   of gebruik
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Als het Dingus document nog niet is opgeslagen, dan is dat het geval
   gevraagd om een locatie en bestandsnaam; daarna, ⌘S
   werkt hetzelfde bestand bij.
* __Opslaan als / dupliceren naar een nieuw bestand__
	- Gebruik __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	- Dit opent altijd een dialoogvenster __Opslaan als__ en schrijft de
   huidige Dingus inhoud naar een nieuw bestand zonder te overschrijven
   het origineel.

### Voorbeeld bekijken over Marked

* __Open het Dingus document als een volledig Marked voorbeeld__
	- Klik op __Open in Marked__ in de statusbalk van Dingus, of gebruik

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Als het Dingus document niet is opgeslagen of niet-opgeslagen wijzigingen bevat,
   u wordt gevraagd eerst op te slaan; dan opent Marked een
   standaardvoorbeeld voor dat bestand.

Met deze opdrachten kunt u de Dingus behandelen als een
lichtgewicht editor voor snelle oplossingen en experimenten dus
ga naar een volledig Marked voorbeeld of naar uw gewone editor wanneer
je bent klaar voor uitgebreidere bewerkingen.

## Processorselectie

Gebruik de vervolgkeuzelijst bovenaan om tussen verschillende te schakelen
Markdown verwerkers:

* __MultiMarkdown__: Volledig uitgeruste processor met tabellen,
  voetnoten en wiskundige ondersteuning
* __CommonMark (GFM)__: standaard, snelle processor volgens de
  CommonMark-specificatie
* __Korting__: GitHub Gearomatiseerd Markdown met taak
  lijsten en tabellen
* __Kramdown__: geavanceerde processor met extra functies
  zoals IAL's en typografie

## Waarom de Dingus gebruiken?

### Processorverschillen begrijpen

Verschillende Markdown-processors verwerken de syntaxis anders. De
Dingus helpt u:

* __Uitvoer vergelijken__: zie precies hoe elke processor wordt weergegeven
  dezelfde Markdown
* __Debug-problemen__: Identificeer waarom bepaalde syntaxis dat niet is
  werkt zoals verwacht
* __Leer syntaxis__: begrijp de subtiele verschillen
  tussen processorimplementaties

### Testen voordat u schrijft

Voordat u zich aan een bepaalde Markdown stijl in uw
documenten:

* __Validate Syntaxis__: zorg ervoor dat uw Markdown wordt weergegeven
  correct
* __Kies processors__: bepaal welke processor het beste werkt
  voor uw inhoud
* __Experimenteer veilig__: Probeer een nieuwe syntaxis zonder dat dit gevolgen heeft
  uw werkelijke documenten

## Veelvoorkomende gebruiksscenario's

### Verschillen in tabelsyntaxis

Sommige processors gaan anders met de tabelsyntaxis om. De Dingus
laat u zien welke processor uw tafel het beste ondersteunt
opmaakbehoeften.

### Voetnootondersteuning

Niet alle processors ondersteunen voetnoten. Gebruik de Dingus om
controleer of de syntaxis van de voetnoot werkt met de door u gekozen processor.

### Wiskundige en speciale tekens

Test hoe verschillende processors met wiskunde omgaan
uitdrukkingen en speciale typografische karakters.

## Tips voor effectief gebruik

1. __Begin eenvoudig__: begin met basis Markdown en geleidelijk
   complexiteit toevoegen
2. __Test Edge Cases__: Probeer ongebruikelijke syntaxiscombinaties
   begrijp de processorlimieten
3. __Vergelijk Side-by-Side__: Schakel tussen processors
   verschillen duidelijk zien
4. __Gebruik echte inhoud__: Kopieer daadwerkelijke inhoud van uw
   documenten om scenario's uit de echte wereld te testen

De Dingus is een krachtig hulpmiddel voor iedereen die dat wil
begrijp de nuances van verschillende Markdown implementaties
en ervoor zorgen dat hun inhoud correct wordt weergegeven in verschillende
platforms en verwerkers.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus

