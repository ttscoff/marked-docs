# <%= @title %>

[VoodooPad][vp] bundelt elke pagina in één databasebestand. Sleep de `.vpdoc` naar Marked om een ​​voorbeeld te bekijken van de pagina die momenteel het meest vooraan staat in VoodooPad; gebruik {% kbd cmd S %} in VoodooPad wanneer je Marked nodig hebt om te herladen vanaf schijf.

Marked bekijkt het document op schijf en wisselt het voorbeeld wanneer u binnen VoodooPad van pagina wisselt.

## Ingesloten afbeeldingen [embedded-images]

Wanneer u naar afbeeldingen verwijst met Markdown of HTML en de binaire levens **in** de VoodooPad-database, kan Marked deze extraheren voor de preview. Afbeeldingen die alleen **aliassen** zijn (bestanden die door verwijzing zijn binnengesleept) worden niet in de bundel opgeslagen. Wijs naar afbeeldingen met absolute paden of paden relatief ten opzichte van de `.vpdoc` op schijf, zodat Marked deze kan omzetten.

[vp]: https://www.voodoopad.com/
