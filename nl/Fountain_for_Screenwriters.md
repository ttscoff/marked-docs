# <%= @title %>

[Fountain](http://fountain.io/) is een gespecialiseerde tekstopmaaktaal die is ontworpen voor het schrijven van scenario's. Scenarioschrijvers die schrijven met de syntaxis van Fountain kunnen Marked gebruiken om een ​​voorbeeld van hun werk te bekijken.

Als u een bestand met de extensie ".fountain" opent, wordt automatisch Fountain-ondersteuning voor het venster ingeschakeld. Er wordt een standaard Fountain-stylesheet toegepast voor voorbeeldweergave en export.

U kunt forceren dat elk document wordt verwerkt als Markdown door het tandwielmenu rechtsonder in het voorbeeldvenster te openen en **Verwerken als fontein** te selecteren.

Sectie- en scènekoppen verschijnen in de inhoudsopgave voor snelle navigatie door uw scenario.

## Fragmenten [scrippets]

U kunt ook "scrippets" in een gewoon document gebruiken om afzonderlijke secties te laten verwerken en opmaken met Fountain. Omring eenvoudig uw Fountain-opmaak in het hoofddocument met `[scrippet]` tags:

[script]
    Uw scenariotekst...
    [/script]

U kunt ook standaardtags in Marked-stijl gebruiken:

<!--SCRIPPET-->
    Uw scenariotekst...
    <!--/SCRIPPET-->