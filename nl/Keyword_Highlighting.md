# <%= @title %>

Het opvangen van lastige woordenstroom en het onder de aandacht brengen van belangrijke zinnen.

## Trefwoorden markeren [highlighting-keywords]

Door trefwoorden te markeren in Marked kunt u veelvoorkomende zinsdelen opvangen die u misschien wilt vermijden, alternatieve termen zoeken of deze gewoon markeren voor algemene doeleinden. De lijst met trefwoorden die bij elke categorie passen, kan worden bewerkt in de {% prefspane Proofing %}.

Schakel markeren in met {% kbd shift cmd H %} vanuit het tandwielmenu ({% appmenu {{gear}}, Highlight Keywords %}), of open de zoekwoordenlade met behulp van het markeerstiftpictogram linksonder (bij het tandwielmenu). De lade kan ook worden geopend met de sneltoets {% kbd shift cmd K %}. Het accentueren wordt automatisch ingeschakeld wanneer de lade wordt geopend en kan worden in- en uitgeschakeld met de schakelaar aan de linkerkant van de lade.

## De zoekwoordenlade [the-keyword-drawer]

![Keyword Drawer][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

De trefwoordenlade die wordt onthuld bij het inschakelen van markering biedt snelle toegang tot markeringsopties, inclusief de mogelijkheid om individuele markeringstypen in en uit te schakelen. De verticale rij gekleurde labels aan de linkerkant komt overeen met de highlights in de tekst. Als u op een label klikt, worden de hoogtepunten voor dat zoekwoordtype gewijzigd.

Links van elk label staat een doelpictogram. Als u hierop klikt, begint het document naar het volgende exemplaar van de markering in documentvolgorde te scrollen. Rechts van het label staat een telling die het totale aantal hoogtepunten voor dat type weergeeft.

Via het toetsenbord navigeer je snel door de highlights. Als u `[` en `]` typt, gaat u in eerste instantie vooruit en achteruit door alle hoogtepunten. Als u op een doelpictogram klikt, schakelen `[` en `]` over naar het navigeren door alleen dat type markering. `{` (Shift-[) en `}` (Shift-]) navigeren altijd door alle hoogtepunten, ongeacht het laatst aangeklikte doel.

Als er op een gemarkeerd woord of zinsdeel wordt geklikt, wordt dat type het doel voor navigatie en met behulp van `[` of `]` wordt vanaf dat punt in het document genavigeerd.

## Trefwoorden bewerken [editing-keywords]

![Proofreading Settings][proofprefs]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

Standaard gebruikt Marked de [Plain English Campaign's](http://www.plainenglish.co.uk) lijst met veelgebruikte woorden en zinsdelen. Je kunt deze eenvoudig aanvullen of vervangen door ze te bewerken in de {% prefspane Proofing %}. Elk veld is vrije tekst en elke regel wordt geïnterpreteerd als een zoekterm. Gebruik `*` aan het begin van een zin of woord om voorafgaande tekst te matchen, en `?` om een ​​enkel teken als jokerteken te gebruiken.

Reguliere expressies kunnen worden gebruikt door de expressie te omringen met schuine strepen:

/\\S*?ly/

Het bovenstaande komt overeen met alle woorden die eindigen op "ly" voor markering. De syntaxis voor reguliere expressies in de trefwoordmarkering van Marked is [same as JavaScript](http://www.regular-expressions.info/javascript.html).

## Tijdelijke trefwoorden [temporary-keywords]

U kunt ook tijdelijke trefwoorden toevoegen aan de trefwoordenlade door het kladblok te bewerken. Net als in de {% prefspane Proofing %} velden voegt u één trefwoord of woordgroep per regel toe, reguliere expressies toegestaan ​​(omgeven door schuine strepen). Na het bewerken van tijdelijke trefwoorden, zorg ervoor dat u op de knop "Bijwerken" klikt (of druk op {% kbd cmd return  %}) om de wijzigingen op te slaan en ze gemarkeerd te zien in uw document.

Reguliere expressies werken ook in het tijdelijke trefwoordveld; u hoeft de tekst alleen maar te omringen met schuine strepen (`/my expression\b/`).

Tijdelijke trefwoorden zijn bedoeld voor situaties waarin de dichtheid van trefwoorden belangrijk is. Hiermee kunt u snel zien hoe vaak u de doelwoorden hebt gebruikt, waarbij hun locaties in het document worden gemarkeerd. Het aantal overeenkomsten voor de tijdelijke trefwoorden wordt prominent weergegeven in de lade.

Zie ook de opdracht ["Visualize Word Repetition"][wordrep] om overmatig gebruikte woorden in uw tekst te vinden.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Passieve stem [passive-voice]

Marked wijst op het gebruik van "passieve stem" in Engelse tekst. Als [defined by Wikipedia][passive]:

> het grammaticale onderwerp drukt het thema of de patiënt van het hoofdwerkwoord uit – dat wil zeggen de persoon of het ding dat de actie ondergaat of waarvan de toestand is veranderd.

Passieve stem is niet slecht, zoals je kunt lezen over [in posts by linguist Geoffrey K. Pullum][gkp]. Marked wijst passages aan met passieve stem, maar de beslissing over hun geldigheid is aan jou.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Verdubbelde woorden [doubled-words]

Dubbele woorden (bijvoorbeeld 'de de') worden automatisch oranje gemarkeerd wanneer 'Trefwoordaccentuering' is ingeschakeld. Dit is momenteel niet configureerbaar, maar zou handig moeten zijn voor proeflezen.