# <%= @title %>

Flexibiliteit is de sleutel.

## Versnellingsmenu [gear-menu]

![][4]

   [4]: images/gearmenu.jpg @2x width=740px height=235px class=center

Het tandwielmenu biedt de meeste functies van de menubalk, plus enkele preview-specifieke functies. Klik gewoon op het tandwiel rechtsonder in het venster om toegang te krijgen tot deze functies.

## Blijf op de hoogte [keep-on-top]

![][5]

   [5]: images/KeepOnTopPin.jpg @2x width=740px height=345px class=center

Het slotpictogram linksonder brengt het voorbeeldvenster naar de voorgrond en houdt het daar (zwevend) wanneer u naar andere applicaties overschakelt. U kunt een transparantie op het venster instellen in de {% prefspane General %}, waardoor het venster vervaagt wanneer u andere toepassingen gebruikt.

Deze functie kan ook worden omgeschakeld met {% kbd shift-opt-cmd-f %}.

## Standaardwaarden voor vensterniveau [window-level-defaults]

In de {% prefspane General %} kunt u "Nieuwe vensters bovenaan houden" gebruiken om nieuwe vensters zo in te stellen dat ze altijd boven andere vensters blijven, en/of vensters zo in te stellen dat ze naar de top stijgen wanneer het bijbehorende document wordt bijgewerkt. Windows die bij de update omhoog gaat, zal de focus niet "stelen" van uw editor, ze zullen alleen zichtbaar worden zonder actief te worden.

## Bron bekijken [view-source]

![][6]

   [6]: images/view_source.jpg @2x width=740px height=345px class=center

Met de knop in de rechterbovenhoek kunt u schakelen tussen voorbeeld- en broncodeweergaven. Deze weergave kan ook worden omgeschakeld met U.

## Zoekopdracht [search]

![][7]

   [7]: images/SearchBarFull.jpg @2x width=818px height=195px class=center

De zoekbalk is toegankelijk met {% kbd cmd F %} en biedt u de mogelijkheid om in het voorbeeld naar een woord of zin te zoeken. Nadat u heeft gezocht, kunt u {% kbd cmd G %} en {% kbd shift cmd G %} gebruiken om vooruit en achteruit door aanvullende resultaten te navigeren.

Met de selectievakjes aan de rechterkant van de zoekbalk kunt u de zoekopdracht verfijnen op basis van hoofdlettergevoeligheid, alleen hele woorden en reguliere expressies. Naast zoeken met reguliere expressies werken zoekopdrachten met jokertekens (*?) altijd, zelfs als de regex-optie is uitgeschakeld.

U kunt een zoekterm of woordgroep ook omringen met schuine strepen, zodat deze automatisch als reguliere expressie wordt geïnterpreteerd (bijvoorbeeld '/term.+?\b/').


Gebruik de zoekfunctie in combinatie met bladwijzers om locaties op te slaan zodra u ze vindt. Druk op Tab ({% kbd ⇥ %}) om de focus op het document te zetten en typ vervolgens Shift-[1-9] om een ​​bladwijzer voor dat nummer in te stellen. U kunt teruggaan naar de bladwijzer door gewoon het nummer te typen (zonder de Shift-toets) of door n/p te gebruiken om er in documentvolgorde doorheen te navigeren. N/P navigeert in numerieke volgorde. Voor bladwijzers, de inhoudsopgave, de minikaart en het snel zoeken in kopteksten, zie [Document Navigation](Document_Navigation.html). Zie de sectie [Preview Navigation](Keyboard_Shortcuts.html#previewnavigation) voor meer opties, of typ "?" op elk gewenst moment in het voorbeeld.

> **Opmerking:** De zoekopdracht kan niet doorlopen tussen elementen, wat betekent dat een zoekreeks niet kan doorgaan tussen een alinea en een kop, tussen lijstitems, enz.

U kunt de selectievakjes 'Hele woorden', 'Hoofdlettergevoelig' en 'Regex' in- of uitschakelen met respectievelijk {% kbd ctrl shift 1 %}, {% kbd 2 %} en {% kbd 3 %}.

### Geavanceerd zoeken ### [advanced-search]

U kunt jokertekens gebruiken bij een niet-regex-zoekopdracht. `*` komt overeen met elke reeks tekens die geen spatie zijn en `?` komt overeen met elk afzonderlijk teken.

Als u een zoekopdracht start met `*`, wordt er een jQuery-selectorzoekopdracht van gemaakt. U kunt elke jQuery-selector gebruiken en alle overeenkomende elementen worden gemarkeerd en navigeerbaar met {% kbd cmd G %} en {% kbd shift cmd G %}. Om de reikwijdte van een tekstzoekopdracht te beperken tot een bepaald elementtype, voegt u de zoektermen tussen dubbele aanhalingstekens toe na de selectordefinitie:

*h2 "Alice"

Dit is het equivalent van `*h2:contains(Alice)`

## Documentnavigatie (TOC, bladwijzers, minikaart) [document-navigation-toc-bookmarks-mini-map]

De [Document Navigation](Document_Navigation.html) pagina bevat de inhoudsopgave (inclusief het openen van het filter met {% kbd Space %}), snel zoeken met {% kbd f %}, bladwijzers en de minikaart.

## Toetsenbordnavigatie [keyboardnavigation]

U kunt snel door het voorbeeldvenster navigeren met behulp van sneltoetsen. Gebruik {% kbd j %} en {% kbd k %} om omhoog en omlaag te bewegen, en houd Shift ({% kbd J %}/{% kbd K %}) ingedrukt om sneller te bewegen. {% kbd t %} en {% kbd b %} worden naar de boven- en onderkant van het document verplaatst (net als {% kbd gg %} en {% kbd G %}, voor Vim-fans). {% kbd u %} en {% kbd d %} gaan een halve pagina omhoog en omlaag.

### Kopbal springen [header-jumping]

Als u op de toetsen komma ({% kbd , %}) en punt ({% kbd . %}) drukt, springt u achteruit en vooruit door alle kopteksten in het document. Als u Shift ({% kbd shift  %}) ingedrukt houdt, springt u alleen tussen de kopteksten van niveau 1 en 2.


## Volledig scherm [full-screen]

De modus Volledig scherm kan worden omgeschakeld via het menu Voorbeeld of door {% kbd ctrl cmd F %} te typen.

## Op externe links klikken [clicking-external-links]

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Als u op een externe link in het voorbeeld van uw document klikt, wordt het in uw standaardbrowser geopend. Als u klikt en vasthoudt, krijgt u bij het loslaten van Marked drie opties: u kunt de URL van de link naar uw klembord kopiëren, de link valideren of de link in uw standaardbrowser openen. Klik gewoon ergens in uw voorbeeld om het venster te sluiten. Deze functie kan worden uitgeschakeld in de {% prefspane Preview %} ("Link-popovers inschakelen").

Zie een [overview video on YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Opvouwbare koppen ## [collapsibleheadlines]

Wanneer "Secties voor koppen samenvouwen" is ingeschakeld in {% prefspane Preview %}, wordt door het klikken op koppen de sectie tussen die kop en de volgende kop op hetzelfde niveau samengevouwen. Subsecties binnen die sectie zijn verborgen. Optioneel kunt u dit gedrag beperken tot {% kbd cmd %}-klikken.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Door {% kbd opt  %} ingedrukt te houden tijdens het klikken (of {% kbd cmd %}-klikken) worden alle onderliggende secties onder de aangeklikte kop uit- of samengevouwen. Als u de {% kbd shift  %} (Shift)-toets ingedrukt houdt terwijl u klikt, worden alle andere secties op hetzelfde niveau samengevouwen, waardoor alleen de aangeklikte sectie zichtbaar wordt.

Samengevouwen secties worden rechts van de titel gemarkeerd met een gele markering en de cursor geeft aan wat er gebeurt als er op het item wordt geklikt.

Als er een bewerking wordt uitgevoerd die zichtbaar moet zijn, of als er op een inhoudsopgavesectie wordt geklikt die zich momenteel in een samengevouwen sectie bevindt, worden de benodigde bovenliggende secties uitgevouwen om deze zichtbaar te maken.

U kunt alle secties in een document in één keer samenvouwen/uitvouwen met de opties "Alle secties samenvouwen" ({% kbd opt cmd left  %}) en "Alle secties uitvouwen" ({% kbd opt cmd right  %}).

Zie de [Document Navigation video on YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2) voor meer details.

## Custom Processorindicatoren/schakelaars ## [custom-processor-indicatorstoggles]

![][indicators]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Wanneer de aangepaste processor en/of preprocessor zijn ingeschakeld, verschijnen er indicatielampjes in de werkbalk. Deze kunnen worden gebruikt om te zien of de processor al dan niet is ingeschakeld voor het huidige document (de indicator wordt gemarkeerd). Als u hierop klikt, wordt het gebruik van respectievelijk de aangepaste preprocessor en processor omgeschakeld.

## Scroll naar Bewerken [scrolltoedit]

De functie 'scrollen om te bewerken' in Marked houdt de verschillen bij tussen de laatste en de laatste update en probeert het punt te vinden waarop u uw meest recente wijzigingen hebt aangebracht. Marked houdt dit altijd bij en er verschijnt een kleine rode lijn in het voorbeeld om u de locatie van de eerste gedetecteerde wijziging te laten zien. In de {% prefspane Preview %} kunt u "Scroll naar eerste bewerking" inschakelen en wanneer een voorbeeld wordt bijgewerkt, wordt de weergave voorzichtig naar die locatie gescrolld.

Als "Scroll naar eerste bewerking" is uitgeschakeld, kunt u in het voorbeeld nog steeds op elk gewenst moment op de "e"-toets drukken om naar het laatst opgeslagen bewerkingspunt te gaan.

## Automatisch scrollen [autoscroll]

Zie de speciale [Autoscroll](Autoscroll.html) pagina. Wanneer u Autoscroll als teleprompter gebruikt, [special syntax can insert pauses](Special_Syntax.html#pauses).

## Zoomoverzicht [zoom-overview]

Zie de [Zoom Overview](Zoom_Overview.html) pagina ({% kbd z %} in de preview; werkt ook in Woordherhaling met {% kbd ctrl cmd w %}).

## Markdown Referentie [markdown-reference]

![][11]

   [11]: images/markdown_reference.jpg @2x width=1148px height=267px class=center

Selecteer Markdown Referentie in het menu {% appmenu Help %} om een ​​gids weer te geven die over uw andere vensters zweeft. Dit is handig voor degenen die de syntaxis van Markdown nog aan het leren zijn. U kunt dit paneel via het toetsenbord openen met {% kbd opt cmd M %}.

## Algemene sneltoetsen [global-keyboard-shortcuts]

In de {% prefspane General %} kunt u een aangepaste sneltoets instellen om Marked te activeren, en één om alleen het voorvenster naar boven te brengen zonder uw editor te verlaten.