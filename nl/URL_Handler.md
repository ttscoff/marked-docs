# <%= @title %>

De URL-handler van Marked biedt aanvullende script- en workflowmogelijkheden. U kunt bijvoorbeeld een URL opnemen in de notities van een andere applicatie, die een bestand opent in Marked wanneer erop wordt geklikt. U kunt verschillende acties uitvoeren, zoals hieronder vermeld.

## Het URL-schema

Het URL-schema van Marked is `x-marked`, aangeroepen met opties als `x-marked://open?file=/Users/username/Desktop/report.md`.

U kunt Marked 3 specifiek targeten door `x-marked-3` te gebruiken in plaats van `x-marked`. De methoden en parameters zijn precies hetzelfde als `x-marked`, maar alleen Marked 3 reageert op `x-marked-3`.

## Bellen vanaf de opdrachtregel/scripts

Het aanroepen van de url-handler vanaf de opdrachtregel of een script kan worden gedaan met behulp van macOS [<!--MKPH0--> command](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/):

open 'x-gemarkeerd://open?file=bestandsnaam.md'
	open 'x-marked://refresh?file=bestandsnaam.md'

### Bellen op de achtergrond

U kunt de opdracht `open` aanroepen met de vlag `-g` om het resultaat op de achtergrond uit te voeren zonder de focus te wijzigen. Om de opdracht op de achtergrond uit te voeren en het venster naar boven te brengen zonder de focus te stelen:

open -g 'x-marked://open?file=bestandsnaam.md&raise=true'

## Optionele parameters

### x-succes

Elke opdracht kan een queryparameter **x-success** leveren. Stel dit in op een url die moet worden aangeroepen na het uitvoeren van de opdracht. Bijvoorbeeld: `x-marked://open/?file=filename.md&x-success=ithoughts:`. U kunt ook een bundel-ID opgeven (zoals `com.googlecode.iterm`) om een ​​toepassing te openen die geen URL-schema heeft.

### salarisverhoging

Een **raise**-parameter kan worden doorgegeven met elk commando dat een `file`-parameter accepteert of alle vensters beïnvloedt. Nadat de actie is uitgevoerd, zullen de betrokken vensters boven alle andere vensters (alle applicaties) verschijnen voordat ze terugkeren of een callback uitvoeren.

"x-gemarkeerd://refresh?file=bestandsnaam.md&raise=true"

### snellezen

Een **speedread**-parameter kan worden doorgegeven met URL-handleropdrachten waarmee een voorbeelddocument wordt geopend (`open`, `paste`, `preview` en `stream`). Stel `speedread=1` in om Speed ​​Read automatisch te starten zodra het doelvoorbeeld gereed is.

Voorbeelden:

x-marked://open?file=/Users/gebruikersnaam/Desktop/report.md&speedread=1

x-marked://preview?text=Sommige%20text&speedread=1

x-gemarkeerd://paste?speedread=1

# Beschikbare opdrachten

De volgende opdrachten zijn beschikbaar voor de `x-marked` URL-handler.

## stijl toevoegen

Voeg een nieuwe aangepaste stijl toe aan Marked.

##### Parameters:

**css**: URL-gecodeerde CSS-tekst om naar een aangepaste stijl te schrijven. Vereist tenzij een parameter **file** wordt doorgegeven.

**bestand**: volledig pad (POSIX) naar een CSS-bestand om toe te voegen aan Marked. Vereist tenzij een **css**-parameter wordt doorgegeven.

**naam**: de naam van de stijl die moet worden gegenereerd.

Met de parameter **css** wordt deze gebruikt als bestandsnaam bij het schrijven naar schijf, met toevoeging ".css", en als naam van het menu-item. Dit is vereist voor de parameter **css** en optioneel voor **bestand** (de bestandsnaam wordt gebruikt alsof de parameter naam leeg is).

x-marked://addstyle?name=Mijn+nieuwe+stijl&css=...

x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Als u een naam opneemt bij de bestandsparameter, krijgt het menu-item die naam in plaats van de bestandsnaam. Als u dezelfde naam opnieuw gebruikt met een ander pad, wordt het menu-item bijgewerkt met het nieuwe pad in plaats van dat er een tweede item met dezelfde naam wordt toegevoegd.

## standaardinstellingen

Stel gebruikersinstellingen in. Accepteert een lijst met sleutels en waarden als queryparameters. Alleen bestaande sleutels worden ingesteld. Als de voorkeurswijziging vernieuwing vereist, worden alle vensters automatisch vernieuwd, tenzij `refresh=0` wordt doorgegeven.

Gebruik 1 voor waar en 0 voor onwaar voor Booleaanse waarden.

##### Parameters:

**vernieuwen** _(optioneel)_: indien ingesteld op 0, wordt het automatisch vernieuwen van geopende voorbeeldvensters uitgeschakeld

* Standaard: 1 (waar)

##### Voorbeeld:

x-marked://defaults?syntaxisHighlight=1&includeMathJax=0

De `defaults` methode is grotendeels zo ontworpen dat de ontwikkelaar links naar esoterische functies kan toevoegen die anders misschien niet beschikbaar zouden zijn in Instellingen. Er kunnen echter enkele standaardopties zijn die u bij het automatiseren wilt omschakelen. Enkele veel voorkomende instellingen die u mogelijk wilt beheren tijdens automatisering:

syntaxisHighlight
: syntaxisaccentuering in- of uitschakelen

omvattenMathJax
: interne MathJax-verwerking in- of uitschakelen

verwerker
: stel in op `multimarkdown` of `mmd` om de processor te wijzigen in MultiMarkdown, `discount` of `gfm` om de Kortingsprocessor te gebruiken

h1IsPageBreak, h1IsPageBreak, breakBeforeFootnotes
: Automatische pagina-einden bij het exporteren vóór koptekstniveaus 1 en 2, en voetnoten.


## dingus

Open de Markdown Dingus voor het testen van verschillende Markdown processors.

x-gemarkeerd://dingus

##### Parameters:

**processor** (optioneel): Geef op welke processor standaard moet worden geselecteerd. Geldige waarden:

- `multimarkdown` - MultiMarkdown processor
- `commonmark` - CommonMark (GFM)-processor
- `discount` of `discount (gfm)` - Kortingsprocessor
- `kramdown` - Kramdown-processor

Voorbeelden:

- `x-marked://dingus?processor=kramdown` - Opent met Kramdown geselecteerd
- `x-marked://dingus?processor=commonmark` - Opent met CommonMark (GFM) geselecteerd

*Opmerking:* Hiermee wordt het venster Markdown Dingus geopend, waarin u verschillende Markdown processors (MultiMarkdown, CommonMark (GFM), Discount en Kramdown) naast elkaar kunt testen en vergelijken. Perfect om te experimenteren met de syntaxis van Markdown en om processorverschillen te begrijpen.

## stijlstealer / stelen

Open de Style Stealer-HUD. Handig als u CSS van een livepagina wilt vastleggen of een handmatige inhoudextractiesessie wilt uitvoeren zonder deze via de gebruikersinterface te starten.

Synoniemen: x-marked://stylestealer … , x-marked://steal …

##### Parameters:

**url** _(optioneel)_: Een URL die vooraf moet worden ingevuld in het venster Style Stealer. Als u dit weglaat, wordt de HUD blanco geopend.

Voorbeelden:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify

Open het venster 'URL importeren' (Content Extractor), zodat u de Markdownifier-pijplijn handmatig kunt uitvoeren. Hierdoor wordt de extractie **niet** automatisch uitgevoerd — dat wordt afgehandeld door de onderstaande opdracht `extract`.

Synoniemen: x-marked://importurl … , x-marked://markdownify …

##### Parameters:

**url** _(optioneel)_: Vult het import-URL-veld vooraf in. Als u dit weglaat, wordt het venster geopend met een leeg veld, waarin u wacht totdat u een link kunt plakken.
**html** _(optioneel, alleen markdownify)_: Indien opgegeven op `x-marked://markdownify`, moet dit URL-gecodeerd onbewerkt HTML zijn. Marked converteert de HTML naar Markdown met dezelfde regels als het Klembordvoorbeeld en opent het in een tijdelijk document, alsof u die HTML in een Klembordvoorbeeldvenster had geplakt.

Voorbeelden:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## Doen

Voer een JavaScript-opdracht uit in een documentvenster. De volledige JavaScript-API van Marked is [documented here](https://markedapp.com/help/jsapi/).

##### Parameters:

**js** _(vereist)_: queryreeks die een JavaScript-opdracht bevat

* Accepteert padparameters die verwijzen naar namen van bestanden, of "alles"
* Paden opgesplitst door / doorzoeken meerdere bestanden
* Gedeeltelijke bestandsnamen vormen de beste match

x-gemarkeerd://do/bestandsnaam1/bestandsnaam2?js=...
		x-gemarkeerd://do/all?js=...

**bestand**: queryparameter die door komma's gescheiden paden/bestandsnamen bevat

x-gemarkeerd://do?file=bestandsnaam1,bestandsnaam2&js=...

Werkt op het voorste venster als er geen bestandsnaam is opgegeven (of "all" niet is doorgegeven)

## hulp

Open het interne helpsysteem Marked, waarbij u eventueel een onderwerp opgeeft. Dit is voornamelijk voor intern gebruik, maar toegankelijk via URL. Een URL naar een bepaalde sectie kan worden gekopieerd door met de rechtermuisknop op het bladwijzerpictogram rechts van een kop te klikken en __Kopieer link__ te selecteren. **Marked 3** in-app hulp en zoeken gebruiken het `x-marked-3` schema voor deze links, zodat macOS ze opent in Marked 3 wanneer Marked 2 ook is geïnstalleerd; de onderstaande voorbeelden gebruiken dat formulier.

##### dingus

Open de Markdown Dingus voor het testen van verschillende Markdown processors.

x-gemarkeerd://dingus

######## Parameters:

**processor** (optioneel): Geef op welke processor standaard moet worden geselecteerd. Geldige waarden:

- `multimarkdown` - MultiMarkdown processor
- `commonmark` - CommonMark (GFM)-processor
- `discount` of `discount (gfm)` - Kortingsprocessor
- `kramdown` - Kramdown-processor

Voorbeelden:

- `x-marked://dingus?processor=kramdown` - Opent met Kramdown geselecteerd
- `x-marked://dingus?processor=commonmark` - Opent met CommonMark (GFM) geselecteerd

*Opmerking:* Hiermee wordt het venster Markdown Dingus geopend, waarin u verschillende Markdown processors (MultiMarkdown, CommonMark (GFM), Discount en Kramdown) naast elkaar kunt testen en vergelijken. Perfect om te experimenteren met de syntaxis van Markdown en om processorverschillen te begrijpen.

##### Parameters:

**pagina** _(optioneel)_: De exacte titel van een bestaande pagina, met optionele ankerhash

x-marked-3://help?page=Document_Statistics

Spaties worden vervangen door onderstrepingstekens, volgens de Marked naamgevingsconventie voor helpbestanden. Bij het opgeven van een anker mag een dubbele punt (:) worden gebruikt in plaats van een hekje (#).

Het doel kan alleen op pad worden gespecificeerd (zonder queryreeks):

x-marked-3://help/Keyword_Highlighting:editingkeywords


## extract

Extraheer inhoud uit een web-URL en open deze als een nieuw document in Marked.

x-gemarkeerd://extract?url=https://example.com

##### Parameters:

**url** _(vereist)_: de web-URL waaruit inhoud moet worden gehaald. Moet beginnen met `http://` of `https://`

**venster** _(optioneel)_: Naam voor het venster

**id** _(optioneel)_: Naamruimte-ID

**basis** _(optioneel)_: Basis-URL voor relatieve links

**raise** _(optioneel)_: Stel in op `true` om het venster na het openen omhoog te brengen

**manual** _(optioneel)_: Stel in op `true` om het handmatige extractievenster van Style Stealer te openen in plaats van automatische extractie uit te voeren.

- Wanneer `manual=true`, Marked de Style Stealer opent, het URL-veld vooraf invult (indien aanwezig), eventuele automatische Open-dialoogvensters onderdrukt en u interactief stijlen/inhoud kunt selecteren en extraheren voordat u deze opslaat.
- Wanneer dit wordt weggelaten of `false`, voert Marked de automatische extractor uit (Markdownifier) ​​en wordt het resultaat direct geopend als een nieuw tijdelijk document.

##### Voorbeelden:

x-gemarkeerd://extract?url=https://news.ycombinator.com

x-gemarkeerd://extract?url=https://github.com&window=GitHub&raise=true

x-gemarkeerd://extract?url=https://example.com/article&manual=true

x-gemarkeerd://extract?url=https://blog.example.com/post-title

*Opmerking:* Deze opdracht maakt gebruik van de inhoudextractieservice van Marked om webpagina's op te halen, schone inhoud te extraheren met behulp van Leesbaarheid, te converteren naar de indeling Markdown en het resultaat te openen in een nieuw tijdelijk document. De geëxtraheerde inhoud bevat metagegevens (titel, bron-URL, datum) en is opgemaakt als schoon Markdown. Perfect voor het snel vastleggen en bewerken van webinhoud.

## open

Opent het opgegeven document in Marked.

x-marked://open?file=/Users/gebruikersnaam/Desktop/report.md

##### Parameters:

**bestand** *(vereist)*: het volledige POSIX-pad naar het te openen document, of een door komma's gescheiden lijst met paden

**speedread** *(optioneel)*: Stel in op `1` om Speed ​​Read automatisch te starten na het openen.

`open` accepteert ook een pad waarvan de componenten in één enkele URL worden gecombineerd

x-gemarkeerd://open/~/nvALT2.2

Als het opgegeven bestandspad niet bestaat of niet kan worden geopend, zal Marked nog steeds op de voorgrond verschijnen. Als u zonder de parameter *file* of met een lege waarde draait, wordt eenvoudigweg Marked geopend.

Marked zal ook bestanden openen als alleen het pad van een bestand wordt aangeroepen op de URL-handler, b.v. `x-marked:///Users/username/Desktop/report.md`.

## plakken

Maak een nieuw document van de huidige inhoud van het klembord.

x-gemarkeerd: // plakken

##### Parameters:

**speedread** *(optioneel)*: Stel in op `1` om Speed ​​Read automatisch te starten na het openen van het klembordvoorbeeld.

*Opmerking:* Hiermee wordt een tijdelijk document gemaakt met behulp van de opdracht "Voorbeeld klembord". Alle tekst op uw klembord wordt toegevoegd aan een nieuw, leeg document, dat vervolgens wordt geopend in Marked. Als het wordt gesloten zonder op te slaan, wordt het weggegooid.

## voorbeeld

Bekijk een voorbeeld van de opgegeven tekst in een nieuw document.

x-marked://preview?text=Sommige%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parameters:

**tekst** *(vereist)*: de tekst die in het voorbeeld moet worden ingevoegd. Percentagegecodeerde tekst wordt ongecodeerd voordat het document wordt bekeken.

**speedread** *(optioneel)*: Stel in op `1` om Speed ​​Read automatisch te starten na het openen van de voorbeeldtekst.

## stroom

Open een voorbeeldvenster voor het streamingklembord.

x-gemarkeerd://stream

##### Parameters:

**speedread** *(optioneel)*: Stel in op `1` om Speed ​​Read automatisch te starten na het openen van het streamingvoorbeeld.

*Opmerking:* Hiermee wordt een tijdelijk document gemaakt met behulp van de opdracht "Voorbeeld klembord". De doorgegeven tekst wordt toegevoegd aan een nieuw, leeg document, dat vervolgens wordt geopend in Marked. Als het wordt gesloten zonder op te slaan, wordt het weggegooid.

## vernieuwen

Vernieuw een documentvoorbeeld of alle geopende voorbeelden.

##### Parameters:

**bestand**: queryparameter die door komma's gescheiden paden/bestandsnamen bevat (bestanden moeten momenteel geopend zijn in Marked). Als u aanroept zonder `file` parameter of `?file=all` worden alle geopende vensters vernieuwd.

De parameter *file* kan gedeeltelijk zijn. Marked ververst alle geopende vensters met een gedeeltelijke overeenkomst in de *bestandsnaam* (niet het volledige pad). Als u "all" doorgeeft, worden alle vensters vernieuwd.

x-gemarkeerd://refresh

x-marked://refresh?file=/Gebruikers/gebruikersnaam/Desktop/report.md

x-gemarkeerd://refresh?file=report.md

Indien aangeroepen zonder `file` parameter maar met documentpaden gespecificeerd in de URL, zullen paden gesplitst door / meerdere bestanden doorzoeken, en zullen gedeeltelijke bestandsnamen de beste overeenkomst vormen.

x-gemarkeerd://refresh/bestandsnaam1/bestandsnaam2

## stijl

Stel de voorbeeldstijl (CSS) in voor een of meer documenten.

##### Parameters:

**css** _(vereist)_: queryreeks die de naam of het pad van een stijl bevat. Stijlen moeten standaard aanwezig zijn in het stijlmenu van Marked of in handmatig toegevoegde aangepaste stijlen.

* Accepteert padparameters die verwijzen naar namen van bestanden, of "alles"
* Paden opgesplitst door / doorzoeken meerdere bestanden
* Gedeeltelijke bestandsnamen vormen de beste match

x-gemarkeerd://stijl/bestandsnaam1/bestandsnaam2?css=...
		x-gemarkeerd://stijl/all?css=...

**bestand**: queryparameter die door komma's gescheiden paden/bestandsnamen bevat

x-gemarkeerd://stijl?bestand=bestandsnaam1,bestandsnaam2&css=...

Deze methode werkt op het voorste venster als er geen bestandsnaam is opgegeven (of "all" niet is doorgegeven).


