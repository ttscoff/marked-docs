# <%= @title %>

Marked biedt standaardinstellingen voor het verbeteren van de typografie en de exportlay-out, en biedt tevens eindige controle over de opties als u meer maatwerk nodig heeft.

## Typografie [typography]

### Afbreking en weduwen [hyphenation-and-widows]

Met de optie _Automatisch afbreken in alinea's_ kan Marked bepalen waar een regel het beste kan worden afgebroken om de "vod" van een alinea te verbeteren. Dit is vooral handig bij het gebruik van een stijl met uitgelijnde uitlijning, maar kan ook de leesstroom in langere alinea's verbeteren.

De optie _Voorkom weduwen in koppen en paragrafen_, indien ingeschakeld, forceert onderbrekingen in koppen en paragrafen om te voorkomen dat losse, korte woorden vanzelf op een regel terechtkomen.

Marked verbindt koppen automatisch met het volgende element, om zwevende koppen te voorkomen bij het exporteren naar een gepagineerd formaat (PDF, afdrukken).

### Leestekens [punctuation-marks]

Als uw processor is ingesteld op MultiMarkdown, heeft u de mogelijkheid om "slimme interpunctie" in of uit te schakelen met behulp van de optie _Genereer typografisch correcte aanhalingstekens en interpunctie_. Indien ingeschakeld, worden dubbele en enkele aanhalingstekens omgezet in "gekrulde" aanhalingstekens, worden apostrofs vervangen door typografisch correcte symbolen en worden andere automatische aanpassingen uitgevoerd.

### Voetnootmarkeringen [footnote-markers]

In de sectie Lay-out en typografie van {% prefspane Style %} is _Omring voetnootmarkeringen met vierkante haakjes_ standaard ingeschakeld bij gebruik van de MultiMarkdown processor, en worden voetnootmarkeringen in het document gemaakt die worden omgeven door vierkante haakjes (bijvoorbeeld "[1]"). Om het maken van vierkante haakjes uit te schakelen, schakelt u deze optie uit.

## Overzichtsmodus [outline-mode]

De overzichtsmodus geeft elk bestand met een hiërarchische reeks kopteksten weer als een APA- of decimale omtrek. De standaardinstelling is de APA-stijl, maar dit kan worden uitgeschakeld.

In de {% prefspane Style %} onder "Lay-out en typografie" kunt u bestandsnaamextensies toevoegen waarvoor de overzichtsmodus automatisch is ingeschakeld. Dit is vooral handig voor OPML en ondersteunde mindmapbestanden (zoals iThoughtsX en MindNode). De extensie mag alleen het alfanumerieke gedeelte van de bestandsnaam zijn dat na het laatste puntteken verschijnt.

Schakel de standaard overzichtsmodus in met het selectievakje _Gebruik APA-stijl_. Dit kan tijdelijk worden omgeschakeld vanuit het tandwielmenu van een documentvenster.


## Poëzie [poetry]

De optie _Stijl woordelijke codeblokken als poëzie_ in de {% prefspane Style %} zorgt ervoor dat blokken die met 4 of meer spaties zijn ingesprongen, worden weergegeven met de "poëzie"-stijl van het thema. Dit is meestal een niet-syntaxis gemarkeerde, cursieve sectie.

Regeleinden worden standaard in deze blokken bewaard, dus het biedt een gemakkelijke manier om poëzie en lyrische secties op te nemen in een document waarvoor verder geen codeblokken nodig zijn.

> Deze instelling voegt een bodyklasse "poëzie" toe die kan worden gebruikt in aangepaste thema's om codeblokken en andere elementen vorm te geven wanneer de "poëziemodus" is ingeschakeld.

## Codeblokverpakking [code-block-wrapping]

Met _Toestaan ​​dat thema's tekst binnen codeblokken laten lopen_ kan de voorbeeldstijl bepalen hoe codeblokken moeten worden opgemaakt. Als u deze optie uitschakelt, worden alle codeblokken gedwongen een horizontale overloop te scrollen in plaats van deze in te wikkelen, ongeacht de huidige voorbeeldstijl.

## Werken op volledig scherm [working-full-screen]

Wanneer u Marked gebruikt in de modus Volledig scherm (Control-Command-F), wilt u wellicht de breedte van de weergegeven tekst beperken om een ​​gecentreerde kolom met leesbare inhoud te creëren. Het selectievakje _Beperk tekstbreedte in voorbeeld_ activeert een schuifregelaar waarmee u de maximale breedte van de weergegeven inhoud kunt definiëren. Dit heeft ook invloed op de weergave op niet volledig scherm.

