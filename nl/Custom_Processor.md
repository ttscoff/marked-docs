# <%= @title %>


Marked geeft je volledige controle met Custom Regels, tekst
transformaties, en de mogelijkheid om uw eigen opdrachten uit te voeren of uit te voeren
verschillende processors op basis van overeenkomende bestandseigenschappen.


## Gebruik van Custom preprocessors/processors [using-custom-preprocessorsprocessors]

Om Custom processors toe te voegen, gaat u naar {% prefspane Processor %}
en klik op **Custom Regels**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


In de Regeleditor (ook wel "Conductor" genoemd) kunt u aangepaste regels toevoegen
regels die criteria hebben om bestanden te matchen op basis van bestandsnaam,
pad, overeenkomsten in de inhoud, metadata en zelfs of
andere bestanden bestaan in dezelfde boom als het document
geopend. Wanneer aan een regel wordt voldaan, worden de acties gedefinieerd voor de
regel worden uitgevoerd op dat bestand.

> Onder het veld Processor staan de selectievakjes in "Nieuw
> documenten gebruiken custom:" bepalen of regels worden getest
> helemaal niet voor preprocessor- en processorfasen. Over het algemeen
> laat deze aangevinkt, maar als je deze volledig wilt overschrijven
> eventuele aangepaste processors, stel dat hier in.

![Rules Editor][2]

  [2]: images/CustomRules-800.jpg @2x width=800

Gebruik de `+` om een nieuwe regel te maken
knop onderaan de linkerregellijst. Geef de
regel een naam en stel deze in als preprocessor of processor.

De drie stippen naast een regel geven Preprocessor, Processor en Ingeschakeld aan. Er kan slechts één van Preprocessor of Processor worden gemarkeerd en u kunt op stippen klikken om de status van de regel te wijzigen.

Preprocessor
: Wordt uitgevoerd nadat het bestand voor het eerst is verwerkt, wanneer Marked de opgenomen bestanden toevoegt, stijlvoorkeuren afhandelt zoals GitHub nieuwe regels, enz., maar vóór de verwerkingsfase. Het document is op dit moment nog steeds onbewerkt Markdown en u kunt wijzigingen in de inhoud aanbrengen om door te geven aan de verwerker. Als er geen Custom Processor overeenkomt, of als er geen actie Processor uitvoeren wordt uitgevoerd in een overeenkomende Custom Processor, wordt de standaardprocessor uitgevoerd.

Verwerker
: Een Custom Processor vervangt de ingebouwde processor die is gedefinieerd in {% prefspane Processor %}. Het kan alle acties verwerken die een preprocessor ook kan, en voegt de acties Run Command en Run Processor toe. Hiermee kunt u een aangepaste opdracht uitvoeren, b.v. Pandoc, of voer een andere ingebouwde processor uit op bestanden die aan de criteria voldoen.

Alle tabellen in de Custom Regeleditor kunnen opnieuw worden geordend op
slepen en neerzetten, zodat u de volgorde kunt beïnvloeden
regels worden uitgevoerd, de volgorde van de criteria in het predikaat
editor en de volgorde van de acties die achtereenvolgens moeten worden uitgevoerd.

### Predikaateditor [predicate-editor]

![Predicate Editor][predicate]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Zodra een regel is toegevoegd, gebruikt u de predicaateditor om deze te definiëren
criteria die bepalen of de regel wordt uitgevoerd voor a
gegeven bestand. Gebruik de vervolgkeuzelijst aan de linkerkant om een te selecteren
criterium en gebruik vervolgens de comparator- en waardevelden om te bouwen
het predikaat.

- _bestandsnaam_ komt alleen overeen met de bestandsnaam van het bestand
- _extension_ komt alleen overeen met de extensie van het bestand
- _path_ komt overeen met het volledige POSIX (Unix) pad van het bestand
- _tree_ zoekt naar overeenkomsten met bestandsnamen waar dan ook in het
  directorystructuur van het bestand
- _text_ komt overeen met de tekstinhoud in het bestand. Gebruik vooruit
  schuine strepen rond de tekstwaarde om er een normale waarde van te maken
  expressie zoeken.
- _fileIncludes_ test of het bestand 'included' bevat
  bestanden (met een van [Marked's include
  syntaxes](Multi-File_Documents.html)).
- _metaType_ test of het bestand YAML bevat,
  MultiMarkdown, of Pandoc-metagegevens
- _metadata.X_ tests voor specifieke metadatasleutels zoals auteur,
  datum, titel, enz.

Om alle bestanden te matchen (d.w.z. een Custom Processor die altijd
wordt uitgevoerd), stelt u `filename` in op `contains` `*`. Het sterretje wel
fungeren als een jokerteken en matchen alle bestanden.

[Add a predicate][addpredicate]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Klik op het plusteken (+) op de predikaatrij om nog een predikaat toe te voegen. Houd Option ingedrukt terwijl u op de + klikt om een ​​Booleaanse groep toe te voegen die kan worden ingesteld op Alles (AND) of Willekeurig (OR).

### Acties [manuallyenabled]

Gebruik de knop *+ Actie* om acties aan de regel toe te voegen.

![Add an action][addaction]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Beschikbare acties zijn onder meer:

Stijl instellen
: stel de stijl voor het voorbeeld in. Elke ingebouwde stijl of Custom stijl die u heeft toegevoegd, is beschikbaar.

Voer opdracht uit
: Hiervoor is een opdrachtregelopdracht nodig, inclusief eventuele argumenten, en wordt de inhoud van het bestand doorgegeven aan STDIN. De opdracht moet de resulterende uitvoer op STDOUT retourneren.

> **Mac App Store Sandboxing**: de Mac App Store (MAS)-versie van Marked draait in een sandbox-omgeving die de uitvoering van externe binaire bestanden beperkt. Als u externe processors zoals Pandoc in de MAS-versie moet gebruiken, moet u het binaire bestand naar de app-bundel kopiëren. Om dit te doen:
>
> 1. Klik met de rechtermuisknop op Marked.app → Pakketinhoud tonen
> 2. Navigeer naar Inhoud/Bronnen/
> 3. Maak een map `bin` als deze niet bestaat
> 4. Kopieer uw binaire bestand (bijvoorbeeld `pandoc`) naar dit
> `bin` map
> 5. Maak het uitvoerbaar: `chmod +x` het binaire bestand
> 6. Verwijs in de actie Opdracht uitvoeren ernaar als:
>
> `YOUR_BINARY_NAME [arguments]`
> Of gebruik het volledige pad:
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Opmerking**: Scripts met externe shebangs (zoals Python-scripts die naar `/opt/homebrew/bin/python` verwijzen) worden automatisch uitgevoerd via systeeminterpreters wanneer ze naar de bundel worden gekopieerd. De MAS-versie kan nog steeds problemen ondervinden bij het uitvoeren van binaire bestanden die eigenlijk Python- of Ruby-scripts zijn in plaats van binaire bestanden.
> U moet de binaire bestanden na elke app-update opnieuw kopiëren, omdat updates de hele bundel vervangen. U kunt ook **Help->Crossgrade** gebruiken om de versie zonder sandbox te verkrijgen, die dergelijke beperkingen niet kent.

Voer het ingebedde script uit
: bewerk een volledig script in de ingebouwde code-editor. Net als Run Command moet dit invoer op STDIN vragen en uitvoer op STDOUT retourneren.

Metagegevens instellen
: Voegt metagegevens toe of stelt deze in. Geef een sleutel en een waarde op. Als de sleutel bestaat, wordt de waarde ervan bijgewerkt, zo niet, dan wordt deze toegevoegd. Het type metadata dat wordt gebruikt, wordt automatisch bepaald door de inhoud van het bestand (of het resultaat van een metadataconversieactie).
: Als er geen bestaande metagegevens worden gevonden, worden de metagegevens toegevoegd in het MultiMarkdown-formaat binnen een HTML-opmerking. Marked kan deze metagegevens lezen, maar deze verschijnen niet in uw voorbeeld, ongeacht welke processor wordt gebruikt.

Metagegevens verwijderen
: verwijder metagegevens op basis van de sleutel.

Metagegevens strippen
: verwijder alle metagegevens. Heeft invloed op YAML, MultiMarkdown en Pandoc-metagegevens.

Converteer YAML Meta naar MMD
: Converteert een YAML metadatablok bovenaan het bestand naar metadata in MultiMarkdown-stijl.

Converteer MMD Meta naar YAML
: Converteert een MultiMarkdown metadatablok naar YAML.

Zoeken en vervangen
: Voer een zoek- en vervangingsactie uit op de inhoud van het bestand.
: Als de zoekreeks tussen schuine strepen staat (bijvoorbeeld `/Project \w+/`), wordt deze behandeld als een reguliere expressie. U kunt `$1`, `$2`, enz. gebruiken om overeenkomstgroepen op te nemen in de vervangende tekenreeks.
: Het vervangingsveld ondersteunt enkele escape-reeksen (een backslash gevolgd door): `\n` voegt een nieuwe regel in, `\t` voegt een tabteken in, `\\` voegt een letterlijke backslash in, `\$` voegt een letterlijk dollarteken in (in plaats van een overeenkomstgroep)
: Elke andere `\X` reeks wordt behandeld als slechts `X` (de backslash wordt verwijderd), dus `\e` wordt `e`. Een afsluitende \ zonder teken erna wordt bewaard als een letterlijke backslash.
: Gebruik `[%key]` in de vervangende tekenreeks om een ​​waarde in te voegen uit documentmetagegevens, omgevingsvariabelen of context (bijvoorbeeld `[%title]`, `[%MARKED_PATH]`). Sleutels die zijn ingesteld door eerdere acties in dezelfde regel of door een voorgaande regel zijn beschikbaar. Ongeëvenaarde sleutels worden vervangen door een lege string.

Titel H1 invoegen
: Voegt een H1 in het document in. Dit kan uit de metadata of de bestandsnaam worden gehaald.

Verschuif kopteksten
: Koptekstniveaus aanpassen, van -5--+5. Als u dit bijvoorbeeld instelt op -1, worden alle H1's H2's, H2's worden H3's, enz. Stel dit in op een positief getal om de headerniveaus met dat bedrag te verhogen.

Normaliseer kopteksten
: Deze actie zorgt er, indien mogelijk, voor dat er slechts één H1 in het document staat en past alle koptekstniveaus aan zodat ze in een semantische volgorde staan en geen niveaus overslaan, bijvoorbeeld van H2 tot H4. Als het originele document überhaupt semantisch geordend is, zal dit de hiërarchie goed verfijnen.

Inhoudsopgave invoegen
: een inhoudsopgave invoegen. De inhoudsopgave kan na de eerste H1, de eerste H2 of bovenaan het bestand worden geplaatst (wordt ingevoegd na eventuele metagegevens).

Bestand invoegen
: Voegt een geselecteerd tekstbestand in op een bepaald punt in het document. Dit kan na de eerste H1, eerste H2, boven, onder of na een tekstovereenkomst zijn (gebruik `/pattern/` om naar een reguliere expressie te zoeken).

Tekst invoegen
: Biedt een pop-upeditor waarmee u tekst rechtstreeks in de actie kunt insluiten. Positioneringsopties zijn hetzelfde als bij _Insert File_.
: Gebruik `[%key]` ergens in de ingevoegde tekst om waarden op te halen uit documentmetagegevens, omgevingsvariabelen of Marked context (bijvoorbeeld `[%author]`, `[%MARKED_PATH]`). Dit werkt ongeacht welke processor je gebruikt, je hebt dus geen MultiMarkdown nodig voor vervanging van metadata. Waarden uit eerdere acties in dezelfde regel (zoals **Metagegevens instellen**) of uit een voorgaande regel zijn opgenomen. Ongeëvenaarde sleutels worden vervangen door een lege string.

CSS-bestand invoegen
: injecteert een geselecteerd CSS-bestand in het document. Dit wordt geladen na elke stijlselectie en kan worden gebruikt om bestaande stijlen te overschrijven of nieuwe toe te voegen.

CSS invoegen
: Biedt een pop-up CSS-editor waar u uw eigen CSS rechtstreeks aan de actie kunt toevoegen. Deze CSS wordt bovenaan het document geïnjecteerd, na eventuele bestaande stijlen. De volgorde van de geïnjecteerde stijlen komt overeen met de volgorde van de acties in de regel.

JavaScript-bestand invoegen
: injecteert een geselecteerd JavaScript-bestand aan het einde van het document. Houd er rekening mee dat u een actie *Insert JavaScript* moet gebruiken met een [update hook](#updatehook) als u wilt dat het script bij elke update opnieuw wordt geladen.

JavaScript invoegen vanaf URL
: Gebruik dit om een `<script>`-tag in te voegen die is gekoppeld aan een CDN of een andere externe URL aan het einde van het document. Houd er rekening mee dat u een actie *Insert JavaScript* moet gebruiken met een [update hook](#updatehook) als u wilt dat het script bij elke update opnieuw wordt geladen.

JavaScript invoegen
: Biedt een pop-up JavaScript-editor waarmee u aangepast JavaScript rechtstreeks in de actie kunt insluiten. Dit wordt aan het einde van het document ingevoegd en de volgorde waarin JavaScript door de regel wordt uitgevoerd, wordt bepaald door de volgorde van de acties, waarbij de laatste actie als laatste wordt toegevoegd.
: Houd er rekening mee dat u een [update hook](#updatehook) moet gebruiken als u wilt dat scripts bij elke update worden uitgevoerd.

Zelf-link-URL's
: Converteer alle kale URL's naar `<url>`, waardoor in elke processor een hyperlink wordt gegenereerd.

Snelkoppeling uitvoeren
: voer een Apple-snelkoppeling uit. Elke Shortcut-run moet input van STDIN gebruiken en aan het einde de output retourneren (Stop en Return Output). Als u acties wilt uitvoeren die de tekst niet wijzigen, stelt u de invoer in op een variabele, voert u uw acties uit en voert u aan het einde de originele tekstvariabele uit.

Voer Systeemservice uit
: Voer een systeemservice uit in `~/Library/Services`. De dienst moet input accepteren en output retourneren.

Voer de Automator-workflow uit
: Voer een Automator `.workflow` bestand uit. Invoer wordt doorgegeven op STDIN en uitvoer wordt verwacht op STDOUT.

Ga door
: Zodra een regel is gekoppeld, stopt de verwerking standaard (afzonderlijk voor preprocessors en processors, zodat één preprocessor en één processor kunnen matchen). Deze actie zorgt ervoor dat het matchen van regels doorgaat nadat de regel zijn acties heeft uitgevoerd.

### Hook bijwerken [actions]

Marked voert niet bij elke update een volledige vernieuwing uit, dus als
je hebt scripts die delen van de DOM weergeven die ze nodig hebben
om hun renderfunctie uit te voeren met behulp van de Hook API van Marked.

In het onderstaande voorbeeld wordt gebruik gemaakt van Mermaid, wat je eigenlijk nooit doet
hoeft te doen, omdat Zeemeermin nu standaard is inbegrepen. Maar
hier ziet u hoe u het zou doen als u het handmatig zou opnemen.

Voeg een actie **Javascript invoegen** toe en in "JS bewerken"
venster, initialiseer het script en voeg de hook toe:

```javascript
zeemeermin.initialize({ startOnLoad: true });

Marked.hooks.register('update', functie() {
    zeemeermin.run();
});
```

Dit zorgt ervoor dat `mermaid.run()` elke keer wordt uitgevoerd
Marked voert een gedeeltelijke update uit.

### Testregels [updatehook]

De knop _Testregels_ onder de lijst Regels opent een
dialoogvenster waarin u elk Markdown-bestand kunt selecteren en dat zal het zijn
getest op basis van al uw regels. Regels die overeenkomen, krijgen
gemarkeerd met een groen tabblad aan de linkerkant. Bij het matchen
tegen een bestand verschijnt een X-knop die hiervoor kan worden gebruikt
Wis de test en verwijder de markering van de rijen.

## Slepen en neerzetten [drag-and-drop]

Het Conductor-venster ondersteunt verbeterd slepen en neerzetten
mogelijkheden die op intelligente wijze bestandstypen detecteren en
zorg voor passende acties op basis van het gesleepte bestand. De
de implementatie omvat een gesplitst overlay-systeem voor tekst
bestanden waarmee gebruikers kunnen kiezen tussen het testen van het bestand
tegen de regels in of voeg het toe als actie.

![Drag and Drop in Custom Rules][drag]

[drag]: images/draganddropconductor.jpg @2x width=800

### Detectie van bestandstype [file-type-detection]

Het systeem detecteert automatisch verschillende bestandstypen en
toont de juiste overlay-berichten:

- **CSS-bestanden** (`.css`): toont de overlay "CSS-bestand invoegen"
- **JavaScript-bestanden** (`.js`, `.javascript`): Toont "Invoegen
  JS-bestand"-overlay
- **Scriptbestanden** (elk uitvoerbaar bestand)): Toont "Run
  Commando'-overlay
- **Tekstbestanden**: toont gesplitste overlay
- **Uitvoerbare bestanden**: toont de overlay "Opdracht uitvoeren".
- **Onbekende extensies**: standaard ingesteld op "tekst" en wordt weergegeven
  gesplitste overlay

## Custom Processorlogboek [customprocessorlog]

Als u vreemde resultaten krijgt en wilt zien wat er aan de hand is, kunt u in het Custom Regellogboek zien welke regels in welke volgorde worden uitgevoerd. Gebruik **Help->Toon Custom Regellogboek** om het te openen.

![Custom Rules Log][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Meerdere opdrachten uitvoeren [executing-multiple-commands]

Een regel kan meerdere opdrachten achter elkaar bevatten. De output van
elke opdracht wordt doorgegeven aan de volgende. Als je wilt hebben
een commando voert iets uit op hetzelfde moment als dat van Marked
preview-updates, zorg ervoor dat u de originele inhoud teruggeeft
naar STDOUT voor het verwerken van de volgende opdracht of ingebouwd
verwerker.

Als u bijvoorbeeld een opdracht wilt bijwerken met een PDF
document met Pandoc, geef gewoon het originele bestandspad door
(van omgevingsvariabelen) naar Pandoc met passend
opdrachtregelopties en echo vervolgens de STDIN-inhoud terug
naar STDOUT.

## Aangepaste processors dynamisch omzeilen [dynamically-bypassing-custom-processors]

Als een aangepaste processor "NOCUSTOM" retourneert op STDOUT, Marked
zal de aangepaste processor beëindigen en terugvallen op de
standaard interne processor. Hiermee kunt u een
aangepaste processor die kan beslissen of dit wel of niet nodig is
uitvoeren met de [environment variables](#environmentvariables)
hieronder de bestandsnaam of extensie van het document, overeenkomende inhoud
of andere logica.

Als in plaats van `NOCUSTOM` een Custom Processor terugkeert
`MULTIMARKDOWN` of `DISCOUNT` (of `GFM`), `KRAMDOWN`, of
`COMMONMARK`, dan wordt die interne processor gebruikt
alleen dat document. Deze wijziging heeft geen invloed op de standaardwaarde
processor ingesteld in Instellingen.

## Omgevingsvariabelen [environmentvariables]

De actie Commando uitvoeren heeft een omgevingseditor waarin u
kunt uw eigen omgevingsvariabelen instellen die dat zullen zijn
beschikbaar voor de opdracht of het script. Naast deze
vrije variabelen bevat Marked enkele eigen variabelen.

Marked voert de aangepaste processor uit in zijn eigen shell, dat wil zeggen
standaard omgevingsvariabelen worden niet automatisch doorgegeven.
U kunt de omgevingsvariabelen van Marked gebruiken om uw
eigen in uw scripts. Marked maakt de volgende variabelen
beschikbaar voor gebruik in uw shellscripts:

**MARKED_ORIGIN**
: De locatie (basismap) van uw primaire werkbestand (de map met de werktekst, Scrivener of indexbestand).

**PAD**
: Marked stelt een pad in dat standaard uitvoerbare mappen bevat en voegt de map in `MARKED_ORIGIN` hierboven toe. De standaardinstellingen zijn: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. U kunt uw eigen variabele toevoegen door de PATH-variabele naar wens in te stellen en het pad van Marked toe te voegen of te overschrijven (bijvoorbeeld `PATH=/usr/local/yourfolder:$PATH`).

**HUIS**
: De thuismap van de ingelogde gebruiker. Python en andere scripts die afhankelijk zijn van de ingestelde HOME-variabele zullen dit automatisch oppikken, maar het is beschikbaar voor ander gebruik in uw scripts.

**MARKED_EXT**
: De extensie van het primaire bestand dat wordt verwerkt. Met deze variabele kunt u verschillende processen scripten op basis van het type bestand dat wordt bekeken. Als `$MARKED_EXT == "md"` bijvoorbeeld de Markdown-processor van uw voorkeur uitvoert, maar als `$MARKED_EXT == "textile"` een textielprocessor draait.

**MARKED_PATH**
: Dit is het volledige UNIX-pad naar het hoofdbestand dat is geopend in Marked op het moment dat het wordt geladen.

**MARKED_INCLUDES**
: Een door komma's gescheiden lijst met aanhalingstekens van de bestanden die Marked heeft opgenomen in de tekst die wordt doorgegeven met behulp van de verschillende [include syntaxes](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: Dit wordt ingesteld op "PROCESS" of "PREPROCESS", waardoor u één enkel script kunt gebruiken om beide fasen af te handelen op basis van deze variabele.

**MARKED_CSS_PATH**
: het volledige pad naar het huidige stylesheet

### Omgevingsvariabelen metagegevens [metadata-environment-variables]

Wanneer de actie Opdracht uitvoeren wordt uitgevoerd in Marked's
Dirigentsysteem, documentmetagegevens worden automatisch uitgevoerd
geëxtraheerd en beschikbaar gesteld als omgevingsvariabelen voor de
opdracht.

#### Hoe het werkt [how-it-works]

1. **Metagegevensextractie**: het systeem extraheert metagegevens uit het document met behulp van de bestaande `extractMetaDataFromString:`-methode, die het volgende ondersteunt:
   - YAML voorwerk (`---` blokken)
   - MultiMarkdown metadata (sleutel: waarderegels)
   - Pandoc-metadata (`%` titelblokken)
   - HTML metagegevens van reacties (`<!-- key: value -->`)

2. **Sleutelnormalisatie**: Metagegevenssleutels worden genormaliseerd voor gebruik als omgevingsvariabelen:
   - Geconverteerd naar kleine letters
   - Alle niet-alfanumerieke tekens worden verwijderd
   - Spaties en speciale tekens zijn verwijderd

3. **Omgevingsvariabel formaat**: Elke metadatasleutel wordt een omgevingsvariabele met het `MD_` voorvoegsel:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Voorbeeld [example]

Gegeven een document met deze metadata:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

De volgende omgevingsvariabelen zouden beschikbaar zijn
commando's:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Gebruik in opdrachten [usage-in-commands]

U kunt deze omgevingsvariabelen nu in uw Run gebruiken
Commandoacties:

``` bash
# Druk de documenttitel af
echo "Bezig met verwerken: $MD_title"

# Gebruik metadata in voorwaardelijke logica
if [ "$MD_status" = "Concept" ]; dan
    echo "Document heeft nog steeds de conceptstatus"
fi

# Geef metadata door aan andere tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata auteur="$MD_author" \
  --metadata date="$MD_date" \
  -o uitvoer.pdf

# Gebruik metadata voor bestandsnaamgeving
if [ -n "$MD_title" ]; dan
    output_file="${MD_title// /_}.html"
anders
    output_file = "uitvoer.html"
fi
```

#### Ondersteunde acties [supported-actions]

Deze variabele functionaliteit voor metadata naar omgeving is dat wel
verkrijgbaar in:

- **Run Command**-acties
- **Voer ingebedde scriptacties uit**

De metadata worden automatisch uit het document gehaald
inhoud en beschikbaar gemaakt voor elk commando of script dat
loopt door deze acties heen.

## In- en uitschakelen [enabling-and-disabling]

De aangepaste processors kunnen voor worden in- en uitgeschakeld
individuele documenten met behulp van {% kbd opt cmd C %}. Jij
kan ook een preprocessor of processor inschakelen voor een document
automatisch [using metadata](#perdocument) bovenaan
het document.

De huidige statussen van de verwerkers per document zijn
weergegeven als indicatielampjes (alleen zichtbaar als er een processor
is ingeschakeld) links van de werkbalkitems onderaan
rechterwerkbalk van het voorbeeld.

### Preprocessor [preprocessor]

Als u preprocessorregels instelt, worden deze na Marked uitgevoerd
handelt alle Marked-specifieke taken af, zoals het opnemen van externe taken
documenten en code, maar voordat deze de processor uitvoert
(intern of op maat). Dit geeft je de kans om te renderen
aangepaste sjabloonvariabelen, vervangingen afhandelen of injecteren
uw eigen inhoud op een andere manier.

Marked stelt een omgevingsvariabele in voor de werking
map (`MARKED_ORIGIN`) naar de bovenliggende map van het
bestand waarvan een voorbeeld wordt bekeken. Hiermee kunt u de werking wijzigen
directory van een script en neem bestanden op met relatieve paden
naar het originele document. In Ruby kan dat bijvoorbeeld
gebruik:

Dir.chdir(ENV['MARKED_ORIGIN'])

Indien ingeschakeld, kan de aangepaste preprocessor worden ingeschakeld en
uitgeschakeld voor individuele documenten met behulp van
{% kbd ctrl opt cmd C %}.

#### Per document Processor/Pre-processor [per document] [perdocument]

Custom Processoren kunnen ook per document worden ingesteld
met behulp van het metadataformaat voor [Per-Document
settings](Per-Document_Settings.html).

U kunt opgeven of u aangepaste processorinstellingen wilt gebruiken
overschrijf de standaardwaarde voor een document met [Per-Document
settings](Per-Document_Settings.html) (`Custom Processor:`
en `Custom Preprocessor:`). Elke andere instelling dan "true"
of "ja" zal de aangepaste pre/processor uitschakelen.

Voorbeeld gebruik:

Custom Processor: waar
    Custom Preprocessor: onwaar

Zoals opgemerkt op de [Per-Document
Settings](Per-Document_Settings.html#hidingmeta) pagina, jij
kan deze metadata omringen met HTML commentaarmarkeringen om te verbergen
het van GitHub en andere processors die het niet verwijderen
van de uitvoer:

<!--
    Custom Processor: waar
    Custom Preprocessor: waar
    -->

## Met behulp van een alternatieve Markdown processor [using-an-alternative-markdown-processor]

Elke Markdown-smaak die u vanaf de opdrachtregel kunt weergeven, kan dat
worden gebruikt met Marked. Het moet input kunnen krijgen
STDIN, wat hetzelfde is als uw Markdown erop "doorsturen".
opdrachtregel, d.w.z. `cat myfile.md | myprocessor`. Het heeft nodig
om de resulterende HTML op STDOUT terug te geven, die elke
processor waarmee ik ooit heb gewerkt, doet dit standaard.

Gebruik `which YOUR_PROCESSOR` in Terminal om het pad te bepalen
naar het uitvoerbare bestand en plak dat vervolgens in het Run Command-pad
veld, of sleep het uitvoerbare bestand naar het venster Custom Regels
met de geselecteerde regel waaraan u de actie wilt toevoegen.

Als uw processor argumenten op de opdrachtregel vereist,
U moet deze ook in het veld invoeren. Sommige
processors hebben koppeltekens nodig om te functioneren op STDIN en/of STDOUT,
bijv. `-o - -` signaleert vaak invoer van STDIN, uitvoer naar
STDOUT. Raadpleeg de documentatie van uw processor voor meer informatie.

Ik heb de Custom Processorfunctie getest met Pandoc,
Kramdown, gemarkeerd (korting), MultiMarkdown 6, Maruku, en
diverse andere smaken.

### Een opmerking over Pandoc en Sandboxing [a-note-about-pandoc-and-sandboxing]

Pandoc (en enkele andere opdrachtregelprogramma's) kunnen niet worden uitgevoerd
de Mac App Store-versie (sandbox) van Marked.
Als u Pandoc moet uitvoeren, gebruik dan **Help->Crossgrade** om een
gratis licentie voor de directe (Paddle) versie. Dit is waar
van elke processor die problemen ondervindt met sandboxen: if Marked
kan het niet uitvoeren vanwege MAS-machtigingsproblemen, maar dat zal wel gebeuren
bieden de stappen om te crossgraden. Als u problemen ondervindt
en dit gebeurt niet, neem dan contact met mij op via de
[support site](https://support.markedapp.com/questions/add).

### Pandoc als Markdown-processor van het Zwitserse leger [pandoc-as-swiss-army-markdown-processor]

[Pandoc](https://pandoc.org/) is veruit het meest flexibel
Universele tool voor het verwerken van een reeks opmaakformaten. Door
door een `-f` argument toe te voegen met een van de volgende opties, kan Pandoc dit doen
uw Custom Verwerker zijn voor:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

En nog een heleboel anderen. Zie de [Pandoc
documentation](https://pandoc.org/MANUAL.html) voor meer informatie
informatie. Om een van deze als invoerformaat te gebruiken, voegt u gewoon de
het volgende in uw Run Command-veld:

/usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc is perfect voor het schrijven van een script dat gebruikmaakt van de
`$MARKED_EXT` omgevingsvariabele om te bepalen welk formaat
om Pandoc te doorlopen, of om een reeks regels mee te gebruiken
uitbreiding wedstrijden. Als de extensie `md` is, gebruik dan
`pandoc -f gfm` of `pandoc -f markdown_mmd` (of gewoon retourneren
`NOCUSTOM` op STDOUT om de standaardprocessor te gebruiken). Maar als dat zo is
`textile`, voer `pandoc -f textile` uit binnen het script. En als
het is `wiki`, gebruik een van de wiki-opmaakprocessors. Jij krijgt
het idee.

Zoals Pandoc-liefhebbers weten, kan Pandoc dit ook aan
uitgebreide bibliografie en LaTeX-scenario's. De meeste functies
u kunt toegang krijgen via de opdrachtregel en zijn alleen beschikbaar
door het doorgeven van argumenten in Marked.

## Textiel gebruiken [using-textile]

Een paar mensen hebben gevraagd hoe ze textiel kunnen laten werken
Marked. U dient een Textielconverter bij de hand te hebben
de opdrachtregel. Er zijn een paar opties, waaronder Pandoc
(zie hierboven), maar als Pandoc nog niet is geïnstalleerd,
twee andere opties zijn RedCloth voor Ruby en Textile voor Perl
(vereist dat de ontwikkelaarstools zijn geïnstalleerd). Installeren
het een of het ander:

1. Installeer Textiel vanaf
   <https://github.com/bradchoate/text-textile> **OF**
   `sudo gem install RedCloth` in Terminal
2. Gebruik `which textile` of `which redcloth` om de
   pad dat moet worden gebruikt in de Custom Processorpadinstellingen

Nu is Marked een textielpreviewer voor jou!

## AsciiDoc gebruiken [using-asciidoc]

1. Installeer [AsciiDoctor](http://asciidoctor.org/).
2. Schakel een Custom regel in {% prefspane Processor %} in, zodat deze overeenkomt met uw AsciiDoc-bestanden.
3. Stel de Regel in op Processor en voeg een Run Command-actie toe
    1. Bepaal het pad naar `asciidoc`, dat zal zijn
       zoiets als `/usr/bin/asciidoc` of
       `/opt/local/bin/asciidoc`. Als u het niet zeker weet, gebruik dan
       `which asciidoc` om te lokaliseren
    2. Voer `[PATH To asciidoc] --backend html5 -o - -` in als
       het commando (de - aan het einde verzendt de uitvoer als
       STDOUT)

Hierdoor wordt het huidige document naar STDIN verzonden en wordt het bestand weergegeven
gegenereerd HTML als STDOUT.

Zie [this gist](https://gist.github.com/mojavelinux/6324279)
van [Dan Allen](https://gist.github.com/mojavelinux) voor
meer informatie.