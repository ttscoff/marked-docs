<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>


Gemarkeerd geeft u volledige controle met aangepaste regels, tekst
transformaties, en de mogelijkheid om uw eigen opdrachten uit te voeren of uit te voeren
verschillende processors op basis van overeenkomende bestandseigenschappen.


## Aangepaste preprocessors/processors gebruiken

Om aangepaste processors toe te voegen, gaat u naar {% prefspane Processor %}
en klik op **Aangepaste regels**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


In de Regeleditor (ook wel "Dirigent" genoemd) kunt u aangepaste regels toevoegen
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

![Regeleditor][2]

  [2]: images/CustomRules-800.jpg @2x width=800

Gebruik de `+` om een nieuwe regel te maken
knop onderaan de linkerregellijst. Geef de
regel een naam en stel deze in als preprocessor of processor.

De drie stippen naast een regel geven Preprocessor, Processor en Ingeschakeld aan. Er kan slechts één van Preprocessor of Processor worden gemarkeerd en u kunt op stippen klikken om de status van de regel te wijzigen.

Preprocessor
: Wordt uitgevoerd nadat het bestand voor het eerst is verwerkt, wanneer Marked de opgenomen bestanden toevoegt, stijlvoorkeuren verwerkt zoals GitHub-nieuwe regels, enz., maar vóór de verwerkingsfase. Het document is op dit moment nog steeds een onbewerkte Markdown en u kunt wijzigingen in de inhoud aanbrengen om door te geven aan de verwerker. Als er geen aangepaste processor overeenkomt, of als er geen actie Processor uitvoeren wordt uitgevoerd in een overeenkomende aangepaste processor, wordt de standaardprocessor uitgevoerd.

Verwerker
: Een aangepaste processor vervangt de ingebouwde processor die is gedefinieerd in {% prefspane Processor %}. Het kan alle acties verwerken die een preprocessor ook kan, en voegt de acties Run Command en Run Processor toe. Hiermee kunt u een aangepaste opdracht uitvoeren, b.v. Pandoc, of voer een andere ingebouwde processor uit op bestanden die aan de criteria voldoen.

Alle tabellen in de Custom Rules-editor kunnen opnieuw worden geordend op
slepen en neerzetten, zodat u de volgorde kunt beïnvloeden
regels worden uitgevoerd, de volgorde van de criteria in het predikaat
editor en de volgorde van de acties die achtereenvolgens moeten worden uitgevoerd.

### Predikaateditor

![Predikaateditor][predicate]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Zodra een regel is toegevoegd, gebruikt u de predicaateditor om deze te definiëren
criteria die bepalen of de regel wordt uitgevoerd voor a
gegeven bestand. Gebruik de vervolgkeuzelijst aan de linkerkant om een te selecteren
criterium en gebruik vervolgens de comparator- en waardevelden om te bouwen
het predikaat.

- _Bestandsnaam_ komt alleen overeen met de bestandsnaam van het bestand
- _Extension_ komt alleen overeen met de extensie van het bestand
- _Path_ komt overeen met het volledige POSIX (Unix) pad van het bestand
- _Tree_ zoekt naar overeenkomsten met bestandsnamen waar dan ook in het
  directorystructuur van het bestand
- _Text_ komt overeen met de tekstinhoud in het bestand. Gebruik vooruit
  schuine strepen rond de tekstwaarde om er een normale waarde van te maken
  expressie zoeken.
- _Bestand bevat_ test of het bestand opgenomen bevat
  bestanden (met behulp van een van [Marked's include
  syntaxis](Multi-File_Documents.html)).
- _Metadata type_ test of het bestand YAML bevat,
  MultiMarkdown- of Pandoc-metagegevens
- _Metadata:_ velden (bijvoorbeeld _Metadata: Auteur_,
  _Metadata: Datum_, _Metadata: Titel_) testen op specifiek
  metagegevenssleutels. Elke metagegevenssleutel verschijnt in de vervolgkeuzelijst als
  _Metadata:_ gevolgd door de veldnaam.
- _Handmatig ingeschakeld_ komt overeen wanneer die regel is omgedraaid
  aan voor het huidige voorbeeldvenster (zie [Handmatig ingeschakeld
  regels](#manuallyenabled) hieronder). Combineer het met andere
  criteria in een groep Alles (AND), zodat de regel alleen wordt uitgevoerd wanneer
  u meldt zich aan en het bestand voldoet aan uw overige voorwaarden.

Om alle bestanden te matchen (d.w.z. een aangepaste processor die altijd
wordt uitgevoerd), stelt u _Bestandsnaam_ in op `contains` `*`. Het sterretje wel
fungeren als een jokerteken en matchen alle bestanden.

[Voeg een predikaat toe][voeg predikaat toe]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Klik op het plusteken (+) op de predikaatrij om nog een predikaat toe te voegen. Houd Option ingedrukt terwijl u op de + klikt om een ​​Booleaanse groep toe te voegen die kan worden ingesteld op Alles (AND) of Willekeurig (OR).

### Handmatig ingeschakelde regels [handmatig ingeschakeld]

Sommige regels mogen niet worden uitgevoerd op elk bestand dat overeenkomt met hun
criteria. Voeg een **Handmatig ingeschakeld** criterium toe wanneer je wilt
een regel die alleen wordt uitgevoerd nadat u deze voor de huidige hebt ingeschakeld
voorbeeld.

Gebruik de knop **Handmatig toevoegen** onder het predikaat
editor om dit criterium in te voegen. Elke regel kan dit bevatten
slechts één keer. Indien aanwezig, verschijnt de regel in het {% appmenu
Preview, Enable Custom Rule %} submenu voor dat voorbeeld
venster.

**Voorbeeldgebruiksscenario:** U hanteert een regel die injecteert
druk CSS af, verwijder opmerkingen en verschuift koptekstniveaus
PDF-export. Je wilt die transformatie niet bij iedereen
bespaar tijdens het tekenen, maar je wilt het wel op aanvraag. Geef de
regel normale criteria voor het matchen van bestanden plus **Handmatig ingeschakeld**,
schakel het vervolgens vanuit het Preview-menu (of een triggersnelkoppeling)
wanneer u klaar bent om de afdruklay-out te proefdrukken.

#### Snelkoppeling activeren

Wanneer een geselecteerde regel **Handmatig ingeschakeld** bevat, a
Het veld **Triggersnelkoppeling** verschijnt naast **Handmatig toevoegen
Ingeschakeld**. Klik op de recorder en druk vervolgens op de toets
combinatie die je wilt. Die snelkoppeling schakelt de regel voor de
voorste gemarkeerd voorbeeld (inschakelen indien uitgeschakeld, uitschakelen indien ingeschakeld). De
De snelkoppeling wordt bij de regel opgeslagen en blijft bij elke lancering bestaan.
Wis het veld om de snelkoppeling te verwijderen.

![Trigger-snelkoppelingsrecorder in de dirigent][handmatige snelkoppeling]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Overschrijvingen per voorbeeld in het menu Voorbeeld

Twee submenu's van het Preview-menu regelen de overschrijvingen voor de actieven
alleen voorbeeld. Instellingen worden opgeslagen per [view](#multiview) wanneer
meerdere vensters tonen hetzelfde bestand.

**Aangepaste regel inschakelen**
: Geeft een overzicht van elke ingeschakelde regel die een **Handmatig
  ingeschakeld** criterium. Vink een regel aan om deze hiervoor in te schakelen
  voorbeeld; verwijder het vinkje om het uit te schakelen. Het voorbeeld wordt vernieuwd
  onmiddellijk.

**Aangepaste regel negeren**
: Lijst met procesfaseregels. Kies er een om deze te *vastzetten*: tijdens
  de procesfase, wordt alleen die regel geëvalueerd (anders
  Procesregels worden overgeslagen). Kies **Geen (automatisch)** voor
  terug te keren naar de normale regelafstemming. Dit is handig als u
  u een specifieke processorpijplijn hiervoor wilt forceren
  voorbeeld bekijken zonder de algemene aangepaste regels te wijzigen.

#### Knop Overschrijven in de voorbeeldwerkbalk

Wanneer een voorbeeld ten minste één handmatig ingeschakelde regel heeft of een
vastgezet Procesoverschrijving, verschijnt er onderaan een vertakkingspictogram
werkbalk (links van de export- en ladeknoppen).
Het gevulde, accentgekleurde pictogram betekent dat overschrijvingen actief zijn;
het overzichtspictogram betekent dat overschrijvingen zijn opgeschort.

![Knop voor het overschrijven van aangepaste regels in de voorbeeldwerkbalk][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Klik op de knop om overschrijvingen hiervoor op te schorten of opnieuw in te schakelen
voorbeeld bekijken zonder de vinkjes voor handmatige regels te verwijderen of
vastgezette procesregel. Uitgestelde overschrijvingen worden hersteld wanneer
je klikt opnieuw. Dit is sneller dan het uitschakelen van regels in het
menu wanneer u het normale voorbeeld wilt vergelijken met uw
pijpleiding overbruggen.

### Acties

Gebruik de knop *+ Actie* om acties aan de regel toe te voegen.

![Voeg een actie toe][toevoeging]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Beschikbare acties zijn onder meer:

Stijl instellen
: stel de stijl voor het voorbeeld in. Elke ingebouwde stijl of aangepaste stijl die u heeft toegevoegd, is beschikbaar.

Voer opdracht uit
: Hiervoor is een opdrachtregelopdracht nodig, inclusief eventuele argumenten, en wordt de inhoud van het bestand doorgegeven aan STDIN. De opdracht moet de resulterende uitvoer op STDOUT retourneren.

> **Mac App Store Sandboxing**: De Mac App Store (MAS)-versie van Marked draait in een sandbox-omgeving die de uitvoering van externe binaire bestanden beperkt. Als u externe processors zoals Pandoc in de MAS-versie moet gebruiken, moet u het binaire bestand naar de app-bundel kopiëren. Om dit te doen:
>
> 1. Klik met de rechtermuisknop op Marked.app → Pakketinhoud tonen
> 2. Navigeer naar Inhoud/Bronnen/
> 3. Maak een map `bin` als deze niet bestaat
> 4. Kopieer uw binaire bestand (bijvoorbeeld `pandoc`) hiernaar
> map `bin`
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
: voegt metagegevens toe of stelt deze in. Geef een sleutel en een waarde op. Als de sleutel bestaat, wordt de waarde ervan bijgewerkt, zo niet, dan wordt deze toegevoegd. Het type metadata dat wordt gebruikt, wordt automatisch bepaald door de inhoud van het bestand (of het resultaat van een metadataconversieactie).
: Als er geen bestaande metagegevens worden gevonden, worden de metagegevens in MultiMarkdown-indeling toegevoegd aan een HTML-opmerking. Marked kan deze metagegevens lezen, maar deze verschijnen niet in uw voorbeeld, ongeacht welke processor wordt gebruikt.

Metagegevens verwijderen
: verwijder metagegevens op basis van de sleutel.

Metagegevens strippen
: verwijder alle metagegevens. Heeft invloed op YAML-, MultiMarkdown- en Pandoc-metagegevens.

Converteer YAML-meta naar MMD
: Converteert een YAML-metagegevensblok bovenaan het bestand naar metagegevens in MultiMarkdown-stijl.

Converteer MMD-meta naar YAML
: Converteert een MultiMarkdown-metagegevensblok naar YAML.

Zoeken en vervangen
: Voer een zoek- en vervangingsactie uit op de inhoud van het bestand.
: Als de zoekreeks tussen schuine strepen staat (bijvoorbeeld `/Project \w+/`), wordt deze behandeld als een reguliere expressie. U kunt `$1`, `$2`, etc. gebruiken om overeenkomstgroepen op te nemen in de vervangende tekenreeks.
: Het vervangingsveld ondersteunt enkele escape-reeksen (een backslash gevolgd door): `\n` voegt een nieuwe regel in, `\t` voegt een tabteken in, `\\` voegt een letterlijke backslash in, `\$` voegt een letterlijk dollarteken in (in plaats van een matchgroep)
: Elke andere reeks `\X` wordt behandeld als slechts `X` (de backslash wordt verwijderd), dus `\e` wordt `e`. Een afsluitende \ zonder teken erna wordt bewaard als een letterlijke backslash.
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
: Gebruik `[%key]` ergens in de ingevoegde tekst om waarden op te halen uit documentmetagegevens, omgevingsvariabelen of gemarkeerde context (bijvoorbeeld `[%author]`, `[%MARKED_PATH]`). Dit werkt ongeacht welke processor je gebruikt, je hebt dus geen MultiMarkdown nodig voor metadatavervanging. Waarden uit eerdere acties in dezelfde regel (zoals **Metagegevens instellen**) of uit een voorgaande regel zijn opgenomen. Ongeëvenaarde sleutels worden vervangen door een lege string.

CSS-bestand invoegen
: injecteert een geselecteerd CSS-bestand in het document. Dit wordt geladen na elke stijlselectie en kan worden gebruikt om bestaande stijlen te overschrijven of nieuwe toe te voegen.

CSS invoegen
: Biedt een pop-up CSS-editor waar u uw eigen CSS rechtstreeks aan de actie kunt toevoegen. Deze CSS wordt bovenaan het document geïnjecteerd, na eventuele bestaande stijlen. De volgorde van de geïnjecteerde stijlen komt overeen met de volgorde van de acties in de regel.

JavaScript-bestand invoegen
: injecteert een geselecteerd JavaScript-bestand aan het einde van het document. Houd er rekening mee dat u de actie *Insert JavaScript* moet gebruiken met een [update hook](#updatehook) als u wilt dat het script bij elke update opnieuw wordt geladen.

JavaScript invoegen vanaf URL
: Gebruik dit om een `<script>`-tag in te voegen die is gekoppeld aan een CDN of een andere externe URL aan het einde van het document. Houd er rekening mee dat u de actie *Insert JavaScript* moet gebruiken met een [update hook](#updatehook) als u wilt dat het script bij elke update opnieuw wordt geladen.

JavaScript invoegen
: Biedt een pop-up JavaScript-editor waarmee u aangepast JavaScript rechtstreeks in de actie kunt insluiten. Dit wordt aan het einde van het document ingevoegd en de volgorde waarin JavaScript door de regel wordt uitgevoerd, wordt bepaald door de volgorde van de acties, waarbij de laatste actie als laatste wordt toegevoegd.
: Merk op dat u een [update hook](#updatehook) moet gebruiken als u wilt dat scripts bij elke update worden uitgevoerd.

Zelf-link-URL's
: Converteer alle kale URL's naar `<url>`, waardoor in elke processor een hyperlink wordt gegenereerd.

Snelkoppeling uitvoeren
: voer een Apple-snelkoppeling uit. Elke Shortcut-run moet input van STDIN gebruiken en aan het einde de output retourneren (Stop en Return Output). Als u acties wilt uitvoeren die de tekst niet wijzigen, stelt u de invoer in op een variabele, voert u uw acties uit en voert u aan het einde de originele tekstvariabele uit.

Voer Systeemservice uit
: Voer een systeemservice uit in `~/Library/Services`. De dienst moet input accepteren en output retourneren.

Voer de Automator-workflow uit
: Voer een Automator `.workflow`-bestand uit. Invoer wordt doorgegeven op STDIN en uitvoer wordt verwacht op STDOUT.

Regel uitvoeren
: voer de acties van een andere aangepaste regel uit vanaf de huidige regel.
  Kies de doelregel in de pop-up. De aangeroepen regel
  draait in dezelfde fase (Preprocessor of Process) zonder
  het opnieuw evalueren van het predikaat, waardoor het nuttig wordt
  herbruikbare "ingrediënt"-regels.

  **Voorbeeld van gebruik:** Definieer een kleine regel met de naam 'Strip
  HTML-opmerkingen" met de actie Zoeken en vervangen, en geef
  het is een **Handmatig ingeschakeld** criterium, zodat het nooit wordt uitgevoerd
  automatisch. Voeg in uw hoofdregel voor boekverwerking toe
  **Run Regel**-acties op volgorde: eerst 'Normaliseer headers',
  vervolgens 'HTML-opmerkingen verwijderen' en vervolgens een Run-opdracht die aanroept
  Pandoc. U houdt elke stap onderhoudbaar zonder duplicatie
  acties over regels heen.

  **Nesten:** Een regel die wordt aangeroepen door **Run Rule** kan niet worden aangeroepen
  een andere regel. Als de doelregel een **Run Rule** bevat
  actie, die actie wordt overgeslagen; alle andere acties in de
  doelregel wordt nog steeds uitgevoerd. U kunt meerdere **Runregel** toevoegen
  acties aan één enkele regel en ze worden in volgorde uitgevoerd.

  Een regel kan zichzelf niet aanroepen en Marked detecteert cycli
  (bijvoorbeeld Regel A die Regel B aanroept en die Regel A aanroept)
  en slaat de geneste oproep over. Zie de [Aangepaste regels
  Log](#customprocessorlog) voor het overslaan van berichten.

Ga door
: Zodra een regel is gekoppeld, stopt de verwerking standaard (afzonderlijk voor preprocessors en processors, zodat één preprocessor en één processor kunnen matchen). Deze actie zorgt ervoor dat het matchen van regels doorgaat nadat de regel zijn acties heeft uitgevoerd.

### Hook bijwerken

Marked voert niet bij elke update een volledige vernieuwing uit, dus als
je hebt scripts die delen van de DOM weergeven die ze nodig hebben
om hun renderfunctie uit te voeren met behulp van Marked's Hook API.

In het onderstaande voorbeeld wordt gebruik gemaakt van Mermaid, wat je eigenlijk nooit doet
hoeft te doen, omdat Zeemeermin nu standaard is inbegrepen. Maar
hier ziet u hoe u het zou doen als u het handmatig zou opnemen.

Voeg een actie **Javascript invoegen** toe en in "JS bewerken"
venster, initialiseer het script en voeg de hook toe:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Dit zorgt ervoor dat `mermaid.run()` elke keer wordt uitgevoerd
Gemarkeerd voert een gedeeltelijke update uit.

### Testregels

De knop _Testregels_ onder de lijst Regels opent een
dialoogvenster waarin u elk Markdown-bestand kunt selecteren en dat zal het zijn
getest op basis van al uw regels. Regels die overeenkomen, krijgen
gemarkeerd met een groen tabblad aan de linkerkant. Bij het matchen
tegen een bestand verschijnt een X-knop die hiervoor kan worden gebruikt
Wis de test en verwijder de markering van de rijen.

## Slepen en neerzetten

Het Conductor-venster ondersteunt verbeterd slepen en neerzetten
mogelijkheden die op intelligente wijze bestandstypen detecteren en
zorg voor passende acties op basis van het gesleepte bestand. De
de implementatie omvat een gesplitst overlay-systeem voor tekst
bestanden waarmee gebruikers kunnen kiezen tussen het testen van het bestand
tegen de regels in of voeg het toe als actie.

![Slepen en neerzetten in aangepaste regels][slepen]

[drag]: images/draganddropconductor.jpg @2x width=800

### Detectie van bestandstype

Het systeem detecteert automatisch verschillende bestandstypen en
toont de juiste overlay-berichten:

- **CSS-bestanden** (`.css`): Toont de overlay "CSS-bestand invoegen".
- **JavaScript-bestanden** (`.js`, `.javascript`): Toont "Invoegen
  JS-bestand"-overlay
- **Scriptbestanden** (elk uitvoerbaar bestand)): Toont "Run
  Commando'-overlay
- **Tekstbestanden**: toont gesplitste overlay
- **Uitvoerbare bestanden**: toont de overlay "Opdracht uitvoeren".
- **Onbekende extensies**: standaard ingesteld op "tekst" en wordt weergegeven
  gesplitste overlay

## Aangepast processorlogboek [customprocessorlog]

Als u vreemde resultaten krijgt en wilt zien wat er aan de hand is, kunt u in het logboek met aangepaste regels zien welke regels in welke volgorde worden uitgevoerd. Gebruik **Help->Logboek met aangepaste regels weergeven** om het te openen. Aangeroepen **Run Rule**-acties en overgeslagen geneste oproepen worden hier ook geregistreerd.

![Aangepast regellogboek][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Meerdere opdrachten uitvoeren

Een regel kan meerdere opdrachten achter elkaar bevatten. De output van
elke opdracht wordt doorgegeven aan de volgende. Als je wilt hebben
een commando voert iets uit op hetzelfde moment als dat van Marked
preview-updates, zorg ervoor dat u de originele inhoud teruggeeft
naar STDOUT voor het verwerken van de volgende opdracht of ingebouwd
verwerker.

Als u bijvoorbeeld een opdracht wilt hebben om een PDF bij te werken
document met Pandoc, geef gewoon het originele bestandspad door
(van omgevingsvariabelen) naar Pandoc met passend
opdrachtregelopties en echo vervolgens de STDIN-inhoud terug
naar STDOUT.

## Aangepaste processors dynamisch omzeilen

Als een aangepaste processor "NOCUSTOM" retourneert op STDOUT, gemarkeerd
zal de aangepaste processor beëindigen en terugvallen op de
standaard interne processor. Hiermee kunt u een
aangepaste processor die kan beslissen of dit wel of niet nodig is
uitvoeren met behulp van de [omgevingsvariabelen](#environmentvariables)
hieronder de bestandsnaam of extensie van het document, overeenkomende inhoud
of andere logica.

Als in plaats van `NOCUSTOM` een aangepaste processor terugkeert
`MULTIMARKDOWN` of `DISCOUNT` (of `GFM`), `KRAMDOWN`, of
`COMMONMARK`, dan wordt die interne processor gebruikt
alleen dat document. Deze wijziging heeft geen invloed op de standaardwaarde
processor ingesteld in Instellingen.

## Omgevingsvariabelen

De actie Commando uitvoeren heeft een omgevingseditor waarin u
kunt uw eigen omgevingsvariabelen instellen
beschikbaar voor de opdracht of het script. Naast deze
aangepaste variabelen, Marked bevat enkele eigen variabelen.

Marked draait de aangepaste processor in zijn eigen shell, dat wil zeggen
standaard omgevingsvariabelen worden niet automatisch doorgegeven.
U kunt de omgevingsvariabelen van Marked gebruiken om uw
eigen in uw scripts. Marked maakt de volgende variabelen
beschikbaar voor gebruik in uw shellscripts:

**MARKED_ORIGIN**
: De locatie (basismap) van uw primaire werkbestand (de map met de werktekst, Scrivener of indexbestand).

**PAD**
: Gemarkeerd stelt een pad in dat standaard uitvoerbare mappen bevat en voegt de map in `MARKED_ORIGIN` hierboven toe. De standaardwaarden zijn: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. U kunt uw eigen variabele toevoegen door de PATH-variabele naar wens in te stellen en het pad van Marked toe te voegen of te overschrijven (bijvoorbeeld `PATH=/usr/local/yourfolder:$PATH`).

**HUIS**
: De thuismap van de ingelogde gebruiker. Python en andere scripts die afhankelijk zijn van de ingestelde HOME-variabele zullen dit automatisch oppikken, maar het is beschikbaar voor ander gebruik in uw scripts.

**MARKED_EXT**
: De extensie van het primaire bestand dat wordt verwerkt. Met deze variabele kunt u verschillende processen scripten op basis van het type bestand dat wordt bekeken. Als `$MARKED_EXT == "md"` bijvoorbeeld de Markdown-processor van uw voorkeur uitvoert, maar als `$MARKED_EXT == "textile"` een textielprocessor wordt uitgevoerd.

**MARKED_PATH**
: Dit is het volledige UNIX-pad naar het hoofdbestand dat in Marked is geopend op het moment dat het wordt geladen.

**MARKED_INCLUDES**
: Een door komma's gescheiden lijst met aanhalingstekens van de bestanden die Marked heeft opgenomen in de tekst die wordt doorgegeven met behulp van de verschillende [syntaxis opnemen](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: Dit wordt ingesteld op "PROCESS" of "PREPROCESS", waardoor u één enkel script kunt gebruiken om beide fasen af te handelen op basis van deze variabele.

**MARKED_CSS_PATH**
: het volledige pad naar het huidige stylesheet

### Omgevingsvariabelen metagegevens

Wanneer de actie Run Command wordt uitgevoerd in Marked's
Dirigentsysteem, documentmetagegevens worden automatisch uitgevoerd
geëxtraheerd en beschikbaar gesteld als omgevingsvariabelen voor de
commando.

#### Hoe het werkt

1. **Metagegevensextractie**: het systeem extraheert metagegevens uit het document met behulp van de bestaande `extractMetaDataFromString:`-methode, die het volgende ondersteunt:
   - YAML voorwerk (`---` blokken)
   - MultiMarkdown-metagegevens (sleutel: waarderegels)
   - Pandoc-metadata (`%` titelblokken)
   - HTML-commentaarmetadata (`<!-- key: value -->`)

2. **Sleutelnormalisatie**: Metagegevenssleutels worden genormaliseerd voor gebruik als omgevingsvariabelen:
   - Geconverteerd naar kleine letters
   - Alle niet-alfanumerieke tekens worden verwijderd
   - Spaties en speciale tekens zijn verwijderd

3. **Omgevingsvariabele indeling**: elke metagegevenssleutel wordt een omgevingsvariabele met het voorvoegsel `MD_`:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Voorbeeld

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

#### Gebruik in opdrachten

U kunt deze omgevingsvariabelen nu in uw run gebruiken
Commandoacties:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Ondersteunde acties

Deze variabele functionaliteit voor metadata naar omgeving is dat wel
verkrijgbaar in:

- **Run Command**-acties
- **Voer ingebedde scriptacties uit**

De metadata worden automatisch uit het document gehaald
inhoud en beschikbaar gemaakt voor elk commando of script dat
loopt door deze acties heen.

## In- en uitschakelen

De aangepaste processors kunnen voor worden in- en uitgeschakeld
individuele documenten met {% kbd opt cmd C %}. Jij
kan ook een preprocessor of processor inschakelen voor een document
automatisch [met metadata](#perdocument) bovenaan
het document.

De huidige statussen van de verwerkers per document zijn
weergegeven als indicatielampjes (alleen zichtbaar als er een processor
is ingeschakeld) links van de werkbalkitems onderaan
rechterwerkbalk van het voorbeeld.

### Preprocessor

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

#### Per document Processor/Pre-processor [per document]

Aangepaste processors kunnen ook per document worden ingesteld
met behulp van het metadataformaat voor [Per-Document
instellingen](Per-Document_Settings.html).

U kunt opgeven of u aangepaste processorinstellingen wilt gebruiken
overschrijf de standaardwaarde voor een document met [Per-Document
instellingen](Per-Document_Settings.html) (`Custom Processor:`
en `Custom Preprocessor:`). Elke andere instelling dan "true"
of "ja" zal de aangepaste pre/processor uitschakelen.

Voorbeeldgebruik:

    Aangepaste processor: waar
    Aangepaste preprocessor: false

Zoals vermeld in de [Per-Document
Instellingen](Per-Document_Settings.html#hidingmeta) pagina, jij
kan deze metadata omringen met HTML-commentaarmarkeringen om te verbergen
het van GitHub en andere processors die het niet verwijderen
van de uitvoer:

    <!--
    Aangepaste processor: waar
    Aangepaste preprocessor: waar
    -->

## Een alternatieve Markdown-processor gebruiken

Elke Markdown-smaak die u vanaf de opdrachtregel kunt weergeven, kan dat
worden gebruikt met gemarkeerd. Het moet input kunnen krijgen
STDIN, wat hetzelfde is als uw Markdown erop "doorsturen".
opdrachtregel, d.w.z. `cat myfile.md | myprocessor`. Het heeft nodig
om de resulterende HTML op STDOUT terug te geven, die elke
processor waarmee ik ooit heb gewerkt, doet dit standaard.

Gebruik `which YOUR_PROCESSOR` in Terminal om het pad te bepalen
naar het uitvoerbare bestand en plak dat vervolgens in het Run Command-pad
veld, of sleep het uitvoerbare bestand gewoon naar het venster Aangepaste regels
met de geselecteerde regel waaraan u de actie wilt toevoegen.

Als uw processor argumenten op de opdrachtregel vereist,
U moet deze ook in het veld invoeren. Sommigen
processors hebben koppeltekens nodig om te functioneren op STDIN en/of STDOUT,
bijv. `-o - -` signaleert vaak invoer van STDIN, uitvoer naar
STDOUT. Raadpleeg de documentatie van uw processor voor meer informatie.

Ik heb de Custom Processor-functie getest met Pandoc,
Kramdown, gemarkeerd (korting), MultiMarkdown 6, Maruku, en
diverse andere smaken.

### Een opmerking over Pandoc en Sandboxing

Pandoc (en enkele andere opdrachtregelprogramma's) kunnen niet worden uitgevoerd
de Mac App Store-versie (sandbox) van Marked.
Als u Pandoc moet uitvoeren, gebruikt u **Help->Crossgrade** om een
gratis licentie voor de directe (Paddle) versie. Dit is waar
van elke processor die problemen ondervindt bij het sandboxen: indien gemarkeerd
kan het niet uitvoeren vanwege MAS-machtigingsproblemen, maar dat zal wel gebeuren
bieden de stappen om te crossgraden. Als u problemen ondervindt
en dit gebeurt niet, neem dan contact met mij op via de
[ondersteuningssite](https://support.markedapp.com/questions/add).

### Pandoc als afprijzingsprocessor van het Zwitserse leger

[Pandoc](https://pandoc.org/) is veruit het meest flexibel
Universele tool voor het verwerken van een reeks opmaakformaten. Door
door een `-f`-argument toe te voegen met een van de volgende opties, kan Pandoc dit doen
wees uw aangepaste verwerker voor:

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
documentatie](https://pandoc.org/MANUAL.html) voor meer
informatie. Om een van deze als invoerformaat te gebruiken, voegt u gewoon de
volgende in uw Run Command-veld:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc is perfect voor het schrijven van een script dat gebruikmaakt van de
`$MARKED_EXT` omgevingsvariabele om te bepalen welk formaat
om Pandoc te doorlopen, of om een reeks regels mee te gebruiken
uitbreiding wedstrijden. Als de extensie `md` is, gebruik dan
`pandoc -f gfm` of `pandoc -f markdown_mmd` (of gewoon terug
`NOCUSTOM` op STDOUT om de standaardprocessor te gebruiken). Maar als dat zo is
`textile`, voer `pandoc -f textile` uit binnen het script. En als
het is `wiki`, gebruik een van de wiki-opmaakprocessors. Jij krijgt
het idee.

Zoals Pandoc-liefhebbers weten, kan Pandoc dit ook aan
uitgebreide bibliografie en LaTeX-scenario's. De meeste functies
u kunt toegang krijgen via de opdrachtregel en zijn alleen beschikbaar
door passerende argumenten te gebruiken in Marked.

## Textiel gebruiken

Een paar mensen hebben gevraagd hoe ze textiel kunnen laten werken
Gemarkeerd. U dient een Textielconverter bij de hand te hebben
de opdrachtregel. Er zijn een paar opties, waaronder Pandoc
(zie hierboven), maar als Pandoc nog niet is geïnstalleerd,
twee andere opties zijn RedCloth voor Ruby en Textile voor Perl
(vereist dat de ontwikkelaarstools zijn geïnstalleerd). Installeren
het een of het ander:

1. Installeer Textiel vanaf
   <https://github.com/bradchoate/text-textile> **OF**
   `sudo gem install RedCloth` in Terminal
2. Gebruik `which textile` of `which redcloth` om de waarde te bepalen
   pad dat moet worden gebruikt in de aangepaste processorpadinstellingen

Nu is Marked een textielpreviewer voor jou!

## AsciiDoc gebruiken

1. Installeer [AsciiDoctor](http://asciidoctor.org/).
2. Schakel een aangepaste regel in {% prefspane Processor %} in, zodat deze overeenkomt met uw AsciiDoc-bestanden.
3. Stel de Regel in op Processor en voeg een Run Command-actie toe
    1. Bepaal het pad naar `asciidoc`, wat zal zijn
       zoiets als `/usr/bin/asciidoc` of
       `/opt/local/bin/asciidoc`. Als u het niet zeker weet, gebruik dan
       `which asciidoc` om te lokaliseren
    2. Voer `[PATH To asciidoc] --backend html5 -o - -` in als
       het commando (de - aan het einde verzendt de uitvoer als
       STDOUT)

Hierdoor wordt het huidige document naar STDIN verzonden en wordt het bestand weergegeven
gegenereerde HTML als STDOUT.

Zie [deze kern](https://gist.github.com/mojavelinux/6324279)
van [Dan Allen](https://gist.github.com/mojavelinux) voor
meer informatie.