# <%= @title %>

Marked biedt uitgebreide ondersteuning voor het werken met Microsoft Word-bestanden. De typische workflow is **eerst een voorbeeld bekijken, DOCX seconde** exporteren: open of bekijk uw Markdown in Marked, verfijn stijlen en proeflezen in de live preview en exporteer vervolgens naar Word wanneer het document klaar is.

## DOCX bestanden openen

Marked kan een DOCX bestand lezen en het naar een schoon bestand converteren
Markdown. Geldige stijlelementen zoals koppen en lijsten zijn dat wel
worden geconverteerd naar hun Markdown equivalent.

Het bijhouden van wijzigingen en opmerkingen worden omgezet naar
CriticMarkup. Hoogtepunten worden geconverteerd naar `<mark>` tags,
met kleuren waar nodig.

## DOCX bestanden exporteren

Gebruik het palet Exporteren om een DOCX bestand te genereren van uw
Markdown. In het dialoogvenster Opslaan kunt u een ingebouwd bestand opgeven
stijlen --- deze stijl kan eenvoudig in Word worden gewijzigd door gewoon
de themakiezer openen en een nieuw thema selecteren.

### Kop- en voetteksten

Als u kop- en voetteksten configureert in {% prefspane Export %}, worden deze opgenomen in de geëxporteerde DOCX. Standaard tijdelijke aanduidingen zoals `%title`, `%date`, `%page` en `%total` worden tijdens het exporteren vervangen. `%logo` en `%image` sluiten het logo in vanuit de koptekst-/voettekstvoorkeuren. `%md_*` metadatavariabelen worden omgezet op basis van de MultiMarkdown metadata van het document. `%h1`--`%h6` worden Word **STYLEREF**-velden gekoppeld aan de geëxporteerde kopstijlen; Word vult ze in wanneer u het document opent. Zie [Exporting](Exporting.html#headers-and-footers) voor de volledige lijst met variabelen en verschillen tussen DOCX en print/PDF gedrag.

## Wijzigingen bijhouden

De syntaxis CriticMarkup in een Markdown document wordt geconverteerd
naar Word Change Tracking bij export naar DOCX. Opmerkingen
volgende invoegingen, verwijderingen en vervangingen zullen dat wel doen
verschijnen in de rechterkolom in Word bij het bijhouden van wijzigingen
is ingeschakeld.

Wanneer u een DOCX bestand in Marked importeert, worden wijzigingen bijgehouden
worden geconverteerd naar CriticMarkup en `<mark>` tags als
geschikt.

## Wiskunde

MathJax en Katex-vergelijkingen die in het document worden weergegeven, worden geconverteerd naar MathML voor weergave in Word. Deze conversie is niet perfect, maar levert in de meeste gevallen een geldig wiskundeblok op in het Word-document. Dit geldt alleen voor export --- wiskundeblokken in Word-documenten worden bij het importeren niet geconverteerd.

## Custom exportstijlen toevoegen

U kunt uw eigen exportstijlen toevoegen door een sjabloon en een stijlen.xml-bestand op te nemen in `~/Library/Application Support/Marked/Custom Word Styles/`. Om deze te maken:

1. Open een door Marked gegenereerd DOCX bestand in Word
2. Bewerk de stijlen daar in de Stijleditor voor elk element en selecteer voor elk element "Toevoegen aan sjabloon".
3. Sla het DOCX bestand op.
4. Genereer een sjabloon door naar **Ontwerp** in de bovenste balk te gaan en in de vervolgkeuzelijst *Sjabloon* aan de linkerkant op **Huidige sjabloon opslaan**. Geef het een naam zoals je wilt dat het verschijnt in het stijlmenu Marked en sla het op in `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, waarbij `STYLENAME` de naam van je stijl is.
5. Ga naar Finder en zoek het DOCX bestand dat u vanuit Word hebt opgeslagen. Dupliceer het en hernoem de kopie naar `FILENAME.zip` en dubbelklik erop om het uit te pakken.
6. In het uitgepakte document ziet u een map 'word' met daarin een bestand stijlen.xml. Kopieer dat bestand stijlen.xml naar dezelfde map als hierboven en noem het `STYLENAME.xml` (waarbij `STYLENAME` de naam van je stijl is). De bestanden `.thmx` en `.xml` moeten dezelfde basisnaam hebben (alleen verschillende extensies).

De volgende keer dat u een DOCX uit Marked exporteert, ziet u uw nieuwe stijl in het menu Stijl van het dialoogvenster Opslaan.