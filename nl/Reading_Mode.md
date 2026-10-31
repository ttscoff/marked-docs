<!-- MT draft for nl — Reading Mode help. Review before publishing. -->
# <%= @title %>

De leesmodus behoudt uw plaats in lange documenten, focust op het huidige blok en laat u blijvende hoogtepunten opslaan.

## Leesmodus openen [entering-reading-mode]

Kies {% appmenu Preview, Reading Mode %} of druk op {% kbd ctrl opt r %}. Als Speed ​​Read actief is, stopt Marked dit voordat de leesmodus wordt geopend.

De huidige alinea, kop, lijstitem, afbeelding, codeblok, tabel of andere leeseenheid krijgt een linkermarkering. Toetsenbordnavigatie beweegt soepel tussen blokken en houdt de huidige eenheid in de buurt van het bovenste derde deel van het voorbeeld. Door handmatig te scrollen wordt de focus opnieuw gericht zonder dat de pagina wordt uitgelijnd.

## Navigatie en hervatten [navigation-and-resume]

Terwijl de leesmodus actief is:

- {% kbd j %} of {% kbd down %}: Ga naar de volgende leeseenheid.
- {% kbd k %} of {% kbd up %}: Ga naar de vorige leeseenheid.
- {% kbd h %}: Markeer de selectie, of schakel een markering op de huidige eenheid in als er geen tekst is geselecteerd.

Marked slaat de huidige leespositie voor elk document op. Wanneer een opgeslagen positie afwijkt van de huidige weergave, biedt het openen van de Leesmodus twee keuzes:

- **Hervatten** keert terug naar de opgeslagen leespositie.
- **Start vanaf hier** gebruikt de leeseenheid die momenteel zichtbaar is in het voorbeeld.

## Focusmodus [focus-mode]

Klik op het gereedschap Focusmodus bovenaan het voorbeeld om elk blok te dimmen, behalve de huidige leeseenheid. De scherpstelmodus volgt de huidige eenheid terwijl u navigeert. Klik nogmaals op het hulpmiddel om de andere blokken te herstellen, of verlaat de leesmodus om de focusmodus automatisch te wissen.

## Hoogtepunten maken en bewerken [creating-and-editing-highlights]

Selecteer tekst en druk op {% kbd h %} om een ​​inline markeringsmarkering te maken. Als er geen selectie is, drukt u op {% kbd h %} om de volledige huidige leeseenheid te markeren, of drukt u er nogmaals op om de markering van die eenheid te verwijderen. De eerste markering vraagt ​​om een ​​handtekening, die Marked gebruikt bij het maken van CriticMarkup. U kunt de handtekening wijzigen in {% prefspane Preview %}.

### Selectiepop-up

Selecteer tekst om de selectiepop-up weer te geven met pictogramknoppen gecentreerd in de rij:

- **Markeerstift** maakt een inline-markering (of **X** verwijdert de laatste automatische markering wanneer automatische markering is ingeschakeld).
- **Opmerking** opent een dialoogvenster waarin u een notitie voor de markering kunt toevoegen of bewerken. Als de selectie nog niet is gemarkeerd, markeert Marked deze eerst.

De pop-up toont ook het aantal geselecteerde woorden wanneer **Woordentelling bij selectie weergeven** is ingeschakeld.

### Markeer opmerkingen [highlight-comments]

Opmerkingen staan ​​los van handtekeningen. Een handtekening kenmerkt het hoogtepunt; een opmerking is uw opmerking erover.

Voeg een opmerking toe of bewerk deze via het selectiepop-uppictogram voor opmerkingen, of houd de Control-toets ingedrukt en klik op een markering en kies **Opmerking toevoegen…** of **Opmerking bewerken…**. Kies **Opmerking verwijderen** om de notitie te verwijderen zonder de markering te verwijderen.

Bij highlights met commentaar wordt een klein indicatiepuntje weergegeven. Wanneer de zijbalk Opmerkingen zichtbaar is (**Voorbeeld > Opmerkingen tonen**), worden de gemarkeerde opmerkingen in de leesmodus daar weergegeven met een verbindingslijn naar de bovenliggende markering, naast CriticMarkup en andere documentopmerkingen.

### Automatische hoogtepunten

Klik op het markeerstiftgereedschap bovenaan het voorbeeld om automatisch tekst te markeren wanneer u deze selecteert. Klik op de markeerstift in de selectiepop-up om de laatste automatische markering ongedaan te maken, of klik nogmaals op het bovenste markeerstiftgereedschap om de automatische markering uit te schakelen.

Inline hoogtepunten geven begin- en eindhandvatten weer wanneer u deze aanwijst of selecteert. Sleep een van beide grepen om het gemarkeerde bereik uit te breiden of te verkleinen. Wijzigingen worden automatisch opgeslagen en hersteld wanneer het document wordt vernieuwd of opnieuw wordt geopend.

Klik op een markering om deze scherp te stellen en druk vervolgens op Delete of Backspace om deze te verwijderen. Houd de Control-toets ingedrukt en klik op een markering en kies **Delen...** om het macOS-deelblad te openen met de documenttitel en gemarkeerde tekst, **Opmerking toevoegen…** / **Opmerking bewerken…** om een ​​notitie bij te voegen, of **Opmerking verwijderen** om de notitie te wissen.

De instelling **Hoogtepunten weergeven wanneer de leesmodus is uitgeschakeld** bepaalt of opgeslagen hoogtepunten zichtbaar blijven nadat u de modus verlaat.

## Hoogtepunten exporteren [exporting-highlights]

Kies **Voorbeeld > Hoogtepunten exporteren…** of klik op het gereedschap Hoogtepunten exporteren in de werkbalk Leesmodus. Formaten: Markdown, HTML (huidige voorbeeldstijl), platte tekst, CSV (Readwise-compatibel, met opmerkingen in de kolom **Opmerking** en handtekeningen in **Handtekening**) en JSON (bevat een veld `comment` bij elke markering).

HTML exportnesten markeren opmerkingen als blokcitaten onder elke gemarkeerde passage.

Het JSON-formaat is het uitwisselingsbestand van Marked. Sla het op naast een Markdown document als `Document.markedhighlights.json`, of voeg het automatisch toe bij het exporteren van een TextBundle.

## Hoogtepunten importeren [importing-highlights]

Kies **Voorbeeld > Hoogtepunten importeren…** en selecteer een JSON-bestand met hoogtepunten Marked. Hoogtepunten worden samengevoegd op ID: nieuwe ID's worden toegevoegd, overeenkomende ID's worden bijgewerkt en uw bestaande hoogtepunten die niet in het bestand staan, blijven bestaan.

Wanneer u een TextBundle opent die `highlights.json` bevat, voegt Marked deze hoogtepunten automatisch samen. Terwijl een TextBundle open is, slaat Marked ook wijzigingen in markeringen en opmerkingen terug naar `highlights.json` in de bundel (zonder `text.md` te wijzigen).

## TextBundle hoogtepunten [textbundle-highlights]

Schakel bij **Opslaan TextBundle** **Include Highlights** in om `highlights.json` in de bundel (of TextPack) in te sluiten. Deel de bundel zodat bijdragers deze binnen Marked kunnen openen en een gecombineerde hoogtepuntenset kunnen behouden.

## CriticMarkup acties [criticmarkup-actions]

Naast het exporteren en importeren van hoogtepunten biedt het menu Voorbeeld twee CriticMarkup acties voor opgeslagen hoogtepunten:

- **Hoogtepunten kopiëren als CriticMarkup** kopieert elke hoogtepunt in de indeling CriticMarkup zonder het bronbestand te wijzigen.
- **Hoogtepunten in document invoegen...** vraagt ​​om bevestiging en verpakt vervolgens ondubbelzinnige overeenkomende brontekst in CriticMarkup. Marked slaat ontbrekende, dubbele of overlappende overeenkomsten over en rapporteert het resultaat.

Met een handtekening en commentaar gebruikt de gegenereerde markup <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>. Bij alleen commentaar gebruikt Marked <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>. Met alleen een handtekening wordt <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code> gebruikt. Zonder een van beide maakt Marked alleen de markering <code>{=<span>=</span>highlighted text==}</code> aan.

## Hoogtepunten afdrukken [printing-highlights]

Hoogtepunten in de leesmodus zijn standaard inbegrepen bij het afdrukken of opslaan als PDF. Gebruik **Inclusief leesmodusmarkeringen** in het afdrukblad om dit voor de huidige uitvoer te wijzigen. De overeenkomende instelling in {% prefspane Export %} bepaalt de standaardwaarde voor toekomstige afdruk- en PDF-taken.
