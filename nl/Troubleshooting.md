# <%= @title %>

### Foutopsporingsmodus

U kunt logboekregistratie voor foutopsporing inschakelen door {% prefspane Advanced %} te openen en het selectievakje **Debug Mode** onder aan het venster aan te vinken. Er wordt een vervolgkeuzemenu weergegeven waarin u het gewenste logboekniveau kunt instellen:

- **Alleen fouten**: alleen ernstige fouten worden geregistreerd
- **Fouten en waarschuwingen**: geef bovendien minder dringende waarschuwingen weer
- **Alles**: fouten, waarschuwingen en foutopsporingsberichten op informatieniveau weergeven. Dit is de aanbevolen instelling voor het oplossen van problemen.

{% note %}
TODO: Werkt dit nog steeds?
U kunt deze opties ook bereiken door de {% kbd opt  %}-toets ingedrukt te houden wanneer u {% appmenu Help %} in de menubalk opent.
{% endnote %}

### Het logboek bekijken

Als de **Debug-modus** is ingeschakeld, kunt u het menu {% appmenu Help %} openen en Open Debug Log selecteren. Hierdoor wordt de log van Marked in Console.app geopend, die live wordt bijgewerkt wanneer logberichten worden toegevoegd tijdens het gebruik van Marked.

### Problemen oplossen Custom Regels

[Custom preprocessors and processors](Custom_Processor.html) krijgen hun eigen loginterface. Selecteer {% appmenu Help, Show Custom Rules Log %} om het venster te openen. In dit venster wordt een ingekleurd logboek weergegeven waarin wordt aangegeven welke regels overeenkomen en welke opdrachten ze uitvoeren.

### Een probleem melden

Gebruik {% appmenu Help, Report an Issue %} om een ​​venster te openen dat uw instellingen voor de meest voorkomende sleutels toont, en een sjabloon voor het maken van een bugrapport. Gebruik de knop "Kopiëren naar klembord" om de inhoud van het venster te kopiëren en klik op "Ondersteuningssite openen" om [the new-question form](https://support.markedapp.com/questions/add) te openen waar u uw rapport kunt plakken. Ik probeer binnen 48 uur op meldingen te reageren.