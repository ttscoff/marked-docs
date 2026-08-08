# <%= @title %>

Houd het bij terwijl u schrijft.

## Aantal woorden en documentstatistieken [word-count-and-document-statistics]

![][1]

   [1]: images/WordCount.jpg @2x width=840px height=61px class=center

Het aantal woorden bevindt zich in de onderste statusbalk en kan worden in- en uitgeschakeld via {% prefspane General %} onder Statusbalk. U kunt verdere statistieken bekijken in het voorbeeld- of bronvenster vanuit het tandwielmenu, door op het aantal woorden te klikken of door Option-Command-S ({% kbd opt cmd S %}) te typen. Houd de Option-toets ({% kbd opt  %}) ingedrukt terwijl u klikt om de leesbaarheidsstatistieken weer te geven, en houd Option-Command ({% kbd opt cmd %}) ingedrukt om het venster Geavanceerde statistieken te openen.

Als tekst is geselecteerd, wordt het aantal woorden weergegeven en wordt de pop-up met alinea's/zinnen/tekens bijgewerkt met informatie die alleen voor de selectie geldt.

## Aantal woorden voor selectie [word-count-for-selection]

![Word count popup on text selection][2]

   [2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

Wanneer u tekst selecteert in het voorbeeld, toont het aantal woorden onder aan het venster alleen statistieken voor de geselecteerde tekst.

Als "Toon aantal woorden voor selectie" is ingeschakeld in {% prefspane Preview %}, zal er een kleine pop-up verschijnen naast de cursor om het aantal woorden/regels/tekens voor de geselecteerde tekst te tonen. Dit wordt eenvoudigweg afgewezen door de muis weg te bewegen van de pop-up.

De zoomfunctie is handig om snel grotere stukken tekst te selecteren en te tellen. Typ {% kbd z %} om uit te zoomen en uw selectie te maken.

## Leesbaarheidsstatistieken [readability-statistics]

![Readability stats bar][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

Aanvullende statistieken van Flesch/Kincaid en de Fog Index zijn beschikbaar met {% kbd opt shift cmd S %}.

### Leesbaarheidsinformatie [readability-information]

**Flesch-leesgemak:** hogere scores duiden op materiaal dat gemakkelijker te lezen is; lagere cijfers markeren passages die moeilijker te lezen zijn.

**90,0--100,0**: gemiddelde 11-jarige student
**60,0--70,0**: 13- tot 15-jarige studenten
**0,0--30,0**: universitair afgestudeerden

**Flesch-Kincaid-niveau:** het aantal jaren onderwijs dat doorgaans nodig is om deze tekst te begrijpen.

**Gunning fog index:** meet de leesbaarheid van Engels schrift. De index schat het aantal jaren formeel onderwijs dat nodig is om de tekst bij een eerste lezing te begrijpen. Een mistindex van 12 vereist het leesniveau van een Amerikaanse middelbare scholier (ongeveer 18 jaar oud).

## Geavanceerde statistieken [advanced-statistics]

![Advanced Statistics popup][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Als u Geavanceerde statistieken selecteert in het tandwielmenu ---- of op {% kbd cmd I %} --- drukt, verschijnt er een paneel met meer geavanceerde documentstatistieken, waaronder de gemiddelde woord- en zinlengte en de gemiddelde woordcomplexiteit.

### Zwevende geavanceerde statistieken [floating-advanced-statistics]

![Floating Info Window][floating]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Als u op {% kbd shift cmd I %} drukt, wordt een zwevend paneel geopend met alle gedetailleerde statistieken en leesbaarheidsinformatie. Dit paneel kan op de voorgrond blijven wanneer u overschakelt naar uw editor, zodat u uw statistieken kunt zien bijwerken elke keer dat u opslaat, ongeacht of het voorbeeld zichtbaar is of niet. Als u op het pictogram `<` drukt, wordt het bijbehorende Marked voorbeeld naar de voorgrond teruggezet. Als u de optie ingedrukt houdt en op dezelfde knop klikt, wordt het bestand Markdown geopend in uw standaardteksteditor (ingesteld in {% prefspane Apps %}).

### Woorddoelen [word-targets]

Als u tijdens het schrijven een specifiek doel voor het aantal woorden hebt, kunt u een metagegevenssleutel "target:" bovenaan uw document toevoegen. Marked zal uw voortgang volgen, waarbij een voltooiingsindicator wordt weergegeven in het paneel Gedetailleerde statistieken ({% kbd cmd I %}) en in de zwevende statistieken ({% kbd shift cmd I %}).

![][targetwordcount]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualiseer woordherhaling [visualizewordrepetition]

Als u Woordherhaling visualiseren selecteert in het tandwielmenu (of door op {% kbd ctrl cmd W %} te drukken), schakelt u over naar een speciale weergave waarin niet-tekstuele elementen worden verwijderd en woorden worden gemarkeerd die in uw document worden herhaald. Herhaalde woorden worden lichtroze gemarkeerd, en als u over een gemarkeerd woord beweegt, worden de overeenkomende woorden in het hele document helderder. Als u op een gemarkeerd woord klikt, wordt de achtergrond donkerder en wordt de markering 'vastgezet' voor verdere beoordeling.

![Word Repetition][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

U kunt in deze modus ook de zoomfunctie (typ "z") gebruiken, zodat u een herhaald woord kunt markeren en vervolgens snel het hele document kunt scannen om te zien waar de herhalingen geconcentreerd zijn.

Woorden worden vergeleken op basis van hun ‘stam’, wat betekent dat ‘deel’, ‘gedeeltelijk’ en ‘delen’ als herhaalde woorden worden beschouwd. Dit houdt rekening met lettergrepen en vervoegingen bij het controleren op herhalingsdichtheid.

**Domein**

De reikwijdte van de herhalingscontrole kan worden gewijzigd in de onderste werkbalk van het document en kan worden ingesteld op Document of Paragraaf. Documentmodus is standaard; Als u Alinea selecteert, telt alleen de herhaling binnen elk tekstblok. Herhalingen worden nog steeds in het hele document gemarkeerd, maar worden alleen geteld als een woord meer dan één keer in één alinea voorkomt.

**Woorden negeren**

U kunt een woord en alle verschillende vervoegingen en meervouden ervan tijdelijk uitsluiten door Option-klikken op het gemarkeerde woord. Tijdelijk genegeerde woorden verschijnen in de rechter benedenhoek van het voorbeeld. Als u op een woord in de lijst met genegeerde woorden klikt, wordt dit teruggezet in de visualisatie.

Om woorden permanent te negeren, kunt u een lijst bewerken in de {% prefspane Proofing %} onder het tabblad Herhalingen negeren. Woorden (of woordstammen) die één per regel in deze lijst worden toegevoegd, worden altijd genegeerd. Om automatisch een woord aan deze lijst toe te voegen, Option-Shift-klik erop in de woordherhalingsvisualisatie.

**Woordherhalingsmodus afsluiten**

U kunt de woordherhalingsweergave sluiten met behulp van het pictogram Sluiten naast de bereikkiezer in de onderste werkbalk of door op Escape te drukken.