# <%= @title %>

Met Marked kunnen bepaalde attributen van een document worden ingesteld in het MultiMarkdown metadataformaat (hieronder gedetailleerd). U kunt deze gebruiken om kenmerken en stijlen te definiëren die alleen van invloed zijn op dat document, zonder de standaardinstellingen te wijzigen.

De meeste MultiMarkdown headers worden genegeerd door het voorbeeld, maar de volgende zijn toegestaan ​​en hebben invloed op de weergave. U kunt andere metagegevens opnemen die in de uiteindelijke uitvoer moeten worden weergegeven. Marked negeert alleen de sleutels die hieronder niet worden vermeld. Als u opslaat als HTML en *geen* een sjabloon toevoegt, worden met Marked alle metagegevenssleutels weergegeven zoals verwacht.

## Metagegevensformaat [metadata-format]

Metagegevens worden bovenaan het Markdown-bestand ingevoerd of onmiddellijk na eventuele YAML-headers. Ze bestaan ​​uit een sleutel, gevolgd door een dubbele punt, optionele spaties of tabs en de waarde:

Voorbeeldmetagegevens: voorbeeldsleutel

Meerdere metagegevens moeten op hun eigen regels staan, maar zonder regeleinden ertussen. De laatste metadata-invoer moet worden gevolgd door een lege regel vóór het begin van de documenttekst.

Ten eerste: dit is de eerste metadata-invoer
	Ten tweede: dit is de tweede inzending
	Ten derde: de laatste metadata-invoer

# Het begin van de documenttekst

## Marked metadatasleutels

### Metagegevens verbergen voor andere verwerkers [hidingmeta]

**Opmerking:** Als u een aangepaste processor gebruikt of u Markdown rechtstreeks naar een bron plaatst die deze metagegevens niet verwerkt, kunt u deze nog steeds gebruiken door HTML commentaarmarkeringen toe te voegen voor en na de metagegevens. In tegenstelling tot MultiMarkdown en andere processors, zal Marked deze tags overal in het document lokaliseren en ze verwerken/verwijderen uit de uitvoer. Het volgende in de koptekst levert dus de gewenste resultaten op in Marked, maar wordt nergens anders weergegeven:

<!--
	Marked Stijl: Mijn Custom stijl
	Custom Processor: waar
	-->

*Zorg ervoor dat de metadatasleutel aan het begin van de regel begint, zonder spaties of tabs, en plaats niets anders op de regel na de waarde.*

### Stijlen per document

Met de toets "Marked Style:" wordt een voorbeeldstijl voor het document ingesteld. De waarde kan de naam zijn van een standaardstijl of een naam of pad voor elke [Custom Style](Custom_Styles.html) die u in de instellingen hebt gedefinieerd. Als deze sleutel wordt gevonden en overeenkomt met een stijl die Marked kent, zal die stijl worden gebruikt voor het voorbeeld telkens wanneer het document dat de sleutel bevat, wordt geladen.

**Voorbeeld**

Marked Stijl: oprechte burger

### Taal van citaten

Standaard gebruikt Marked aanhalingstekens in Engelse stijl. U kunt dit per document wijzigen met de toets "Quotes Language:". Beschikbare talen zijn:

* Nederlands
* Engels
* Frans
* Duits
* zeekoeten
* Zweeds

**Voorbeeld**

Citaten Taal: Frans

Creëert Franstalige “aanhalingstekens.”

### Basiskopniveau

U kunt het headerniveau instellen vanaf waar Marked begint te tellen met de toets "Base Header Level:". Dit moet een getal van 1 tot en met 6 zijn, en zal de manier wijzigen waarop "#"-headers worden weergegeven. Als u het headerniveau instelt op 3, wordt wat normaal gesproken een header van het eerste niveau (h1) zou zijn, weergegeven als een header van het derde niveau (h3), en worden daaropvolgende headers in de hiërarchie met 2 omhoog geschoven.

**Voorbeeld**

Basiskopniveau: 3

# Deze kop wordt weergegeven als een h3

## Deze kop zal een h4 zijn

Rendert als:

<h3>Deze kop wordt weergegeven als een h3</h3>

<h4>Deze kop zal een h4 zijn</h4>

### Custom Verwerkers

Zoals beschreven in [Custom Processor](Custom_Processor.html#preprocessor), kunt u een aangepaste processor en aangepaste preprocessor in- of uitschakelen met behulp van metagegevens:

Custom Processor: waar
    Custom Preprocessor: onwaar

"true" of "false" zet de pre/processor aan en uit.

De waarde "Processor" kan worden ingesteld op "multimarkdown" of "discount" om het gebruik van de ene of de andere interne processor te forceren. Deze instelling per document zal de standaardinstelling in {% prefspane Processor %} niet wijzigen.

### Kopteksten/voetteksten afdrukken

U kunt de instellingen in {% prefspane Export %} voor het afdrukken van kop- en voetteksten overschrijven met behulp van de volgende toetsen:

printkop links:
	midden printkop:
	printkop rechts:
	voettekst links afdrukken:
	voettekst midden afdrukken:
	voettekst rechts afdrukken:

Deze kunnen [print variables](Exporting.html#headers-and-footers) bevatten zoals `%title`, `%page`, `%total`, enz., evenals verwijzingen naar andere metagegevens die `%md_[key without spaces]` gebruiken.

### Afdrukmarges

Stel de paginamarges in voor afdrukken en gepagineerde PDF uitvoer met de toets `Margins:`. Waarden zijn in punten; achtervoegsels zoals `px`, `pt` en `em` worden genegeerd. Geef twee cijfers op voor de verticale en horizontale marges, of vier cijfers voor boven, rechts, onder en links:

Marges: 10 20
	Marges: 10, 20, 10, 20

Marges metagegevens overschrijven de {% prefspane Export %} instellingen en de margevelden in het exportpaneel PDF.

### JavaScript invoegen

Deze methode specificeert gegevens die zijn opgenomen in de `<head>` tag van het document. Marked negeert de meeste waarden voor deze sleutel, behalve bij uitvoer van volledige documenten, maar respecteert scripts die op deze manier zijn opgenomen. Scripttags die hier worden gedefinieerd, staan ​​niet in de header, maar worden toegevoegd vóór de afsluitende tag `</body>`. jQuery is al geladen en u kunt hiervan profiteren in alle scripts die u injecteert.

**Voorbeeld**

XHTML Koptekst: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

-of-

XHTML Koptekst: <script src="myfancyscript.js"></script>

