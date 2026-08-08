# <%= @title %>

Opties in de {% prefspane Export %}:

(Zie [Exporting](Exporting.html) voor meer info)

![Settings: Export][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Profiel exporteren [export-profile]

Profiel exporteren
: selecteer een opgeslagen profiel in het pop-upmenu. Profielen slaan een volledige set exportvoorkeuren op, zodat u snel kunt schakelen tussen workflows (bijvoorbeeld afdrukken PDF versus web HTML). Zie [Export Profiles](Exporting.html#export-profiles).

Nieuw
: een nieuw profiel maken op basis van de huidige instellingen.

Beheer
: open profielbeheer om profielen te hernoemen, dupliceren of verwijderen.

### Afdrukken/PDF [printpdf]

Schakel links/highlights uit bij het exporteren van PDF of afdrukken
: verwijdert de opmaak (onderstreping en kleur) van koppelingen tijdens het afdrukken.

Neem de URL op als tekstannotatie
: Bij het afdrukken of exporteren van PDF verschijnt de URL voor een link na de gekoppelde tekst.

Vervang horizontale regels door pagina-einden
: Zet horizontale regels in het document om in pagina-einden (hierdoor worden voetnoten bovendien op een nieuwe pagina geforceerd).

Afbeeldingen insluiten tijdens het kopiëren van HTML
: Indien ingeschakeld, zal het kopiëren van HTML naar het klembord scannen naar lokale afbeeldingen en Base64 codeert deze zodat ze als gegevens-URL's in de broncode kunnen worden opgenomen.

Achtergrondkleuren en afbeeldingen afdrukken
: Standaard wordt Marked afgedrukt/exporteren met een witte achtergrond. Als u achtergrondkleuren en afbeeldingen van aangepaste thema's wilt opnemen, schakelt u deze optie in.

Voorkom verweesde krantenkoppen
: deze optie voorkomt dat de koppen voor het volgende gedeelte onder aan een pagina verschijnen zonder daaropvolgende inhoud.

Sluit eerste H1 uit
: negeer de eerste kop van niveau één in het document wanneer u H1's als pagina-einden gebruikt.

Gebruik eerste H1 als reservetitel
: Wanneer u apps zoals Bear of de streaming preview gebruikt, kunt u met deze optie de bestandsnaam overschrijven met de inhoud van de eerste H1 in het document. Als er metadata voor "titel" is opgegeven, heeft dat altijd voorrang.

Voeg eerder pagina-einden toe
: Gebruik kopteksten van niveau 1/2 als sectieverdelers en begin ze altijd op een nieuwe pagina. Selecteer 'Voetnoten' om altijd een pagina-einde toe te voegen vóór voetnoten in het document.

Geef pagina-einden aan in het voorbeeld
: Geef een licht onderbroken lijn weer waar onderbrekingen worden ingevoegd met de syntaxis <!\--BREAK\--> of door de opties voor automatisch afbreken in de exportinstellingen aan te vinken.

Custom lettergrootte voor exporteren/afdrukken
: Indien ingesteld, wordt alle tekst geschaald op basis van de geselecteerde puntinstelling (standaard ingesteld op een basis van 10 punten).

Marges
: Definieer afdrukmarges (opgegeven in punten) voor boven, onder, links en rechts.

Inhoudsopgave afdrukken
: Automatische inhoudsopgave opnemen in print/PDF.

Pagina-einde na
: automatisch naar een nieuwe pagina gaan na een ingevoegde inhoudsopgave.

Inhoudsopgave niveaumarkeringen
: gebruik de vervolgkeuzelijsten om de lijstitemmarkering in te stellen voor elk inspringingsniveau in een inhoudsopgave.

### Kop- en voetteksten [headers-and-footers]

Configureer lettertype, logo, kop-/voettekstvelden, datum- en tijdnotaties, opname van de eerste pagina, offset van paginanummering en randen. Tijdelijke aanduidingen voor velden zijn `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` en andere.

Zie [Headers and Footers](Exporting.html#headers-and-footers) in [Exporting](Exporting.html) voor verwijzing naar tijdelijke aanduidingen en voorbeelden. Zie [Date and Time Formats](Exporting.html#dateandtimeformats) voor `%date` en `%time` formaatcodes.

Opnemen op eerste pagina
: Als de optie voor kop- en/of voettekst niet is aangevinkt, wordt de eerste pagina niet met het opgegeven type afgedrukt.

Datumformaat
: strftime-stijl formatstring voor `%date` in kop- en voetteksten. Zie [Date and Time Formats](Exporting.html#dateandtimeformats).

Tijdformaat
: strftime-stijl formatstring voor `%time` in kop- en voetteksten. Zie [Date and Time Formats](Exporting.html#dateandtimeformats).

Verschuiving van paginanummering
: wordt gebruikt om aan te passen bij welk nummer de paginanummers beginnen. Als u bijvoorbeeld een inhoudsopgave op de eerste pagina hebt en wilt dat de nummering op de tweede pagina begint, stelt u de verschuiving in op -1. Pagina 2 wordt nu pagina 1 en het totaal aantal pagina's wordt dienovereenkomstig aangepast.

Grens
: Druk een horizontale lijn af onder de koptekst en/of boven de voettekst.

Standaardformaten herstellen
: Datum- en tijdnotatiereeksen opnieuw instellen op de standaardwaarden van Marked (`%m-%d-%Y` en `%I:%M %p`). Zie [Date and Time Formats](Exporting.html#dateandtimeformats).