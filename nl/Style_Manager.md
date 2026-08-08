# <%= @title %>

De Style Manager biedt een gecentraliseerde interface voor het beheren van al uw
ingebouwde en Custom stijlen. Het geeft je volledige controle over welke
Stijlen verschijnen in menu's, hun volgorde, sneltoetsen en meer.

## De Stijlmanager openen [opening-the-style-manager]

Om de Stijlmanager te openen, klikt u op de knop **Stijlen beheren…** in het {% prefspane Style %}
deelvenster, of gebruik {% appmenu Style, Manage Styles (~@$m) %}. U kunt CSS-bestanden ook rechtstreeks naar het voorkeurenvenster slepen --- Marked
importeert ze, opent de Stijlmanager en selecteert de nieuw toegevoegde rij voor
jij.

![Style Manager][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## De stijltabel [the-style-table]

De Stijlmanager geeft al uw stijlen weer in een sorteerbare tabel die door elkaar kan worden gemengd
ingebouwde en aangepaste stijlen naadloos. Elke rij in de tabel bevat er meerdere
kolommen:

### Selectievakje ingeschakeld [enabled-checkbox]

Met het selectievakje **Ingeschakeld** wordt de stijl onmiddellijk aan de stijl toegevoegd of verwijderd
menu, pop-up Standaardstijl en sneltoetsen. Wanneer u een stijl uitschakelt,
het is verborgen in de menu's, maar blijft in de Stijlmanager staan, zodat u het eenvoudig opnieuw kunt inschakelen.

Als u de momenteel actieve stijl uitschakelt, schakelt Marked automatisch over naar de
volgende beschikbare ingeschakelde stijl.

### Naamkolom [name-column]

In de kolom **Naam** wordt de weergavenaam van de stijl weergegeven. U kunt deze naam bewerken
inline door er direct op te klikken; veranderingen blijven bestaan en verspreiden zich naar elk menu
waar de stijl verschijnt. Dit is vooral handig voor aangepaste stijlen waarbij u
wil misschien een meer beschrijvende naam dan de bestandsnaam.

Ingebouwde stijlen hebben vergrendelde namen die niet kunnen worden bewerkt. Om een
naam van de ingebouwde stijl, dupliceer deze eerst om een bewerkbare kopie te maken.

### Bronkolom [source-column]

De kolom **Bron** geeft aan waar de stijl vandaan komt:

- **Ingebouwd**: stijlen die bij Marked worden geleverd en in de applicatie worden opgeslagen
  bundel
- **Custom**: stijlen die u heeft toegevoegd vanuit CSS-bestanden op uw schijf
- **Gedupliceerd**: stijlen die zijn gemaakt door een andere stijl te dupliceren (ofwel ingebouwd
  of op maat)

### Actiekolom [actions-column]

Elke rij bevat een **Acties**-stapel met knoppen voor het beheren van die stijl:

**Bewerken**: Opent het CSS-bestand in uw standaardeditor. Ingebouwde stijlen kunnen dat niet zijn
rechtstreeks bewerkt: u moet ze eerst dupliceren om een bewerkbare kopie te maken.

**Duplicaat**: Creëert een kopie van de stijl en een nieuw CSS-bestand op schijf. De
duplicaat verschijnt direct onder de originele stijl in de tabel. Dit is
de aanbevolen manier om ingebouwde stijlen aan te passen.

**Onthullen**: Toont het CSS-bestand in Finder, zodat u het bestand gemakkelijk kunt vinden
jouw rit. Deze knop is alleen beschikbaar voor aangepaste stijlen met een bestandspad.

**Verwijderen**: verwijdert de stijl uit Marked. Voor aangepaste stijlen krijgt u een waarde
de optie om alleen de referentie te verwijderen (het CSS-bestand behouden) of te verplaatsen
het CSS-bestand naar de prullenbak. Ingebouwde stijlen kunnen niet worden verwijderd, maar dat kan wel
uitgeschakeld.

**Herstellen**: voor ingebouwde stijlen herstelt deze knop de stijl naar de oorspronkelijke stijl
standaardstatus als deze is gewijzigd. Deze knop is alleen zichtbaar voor
ingebouwde stijlen.

## Stijlen opnieuw ordenen [reordering-styles]

Rijen kunnen opnieuw worden gerangschikt via slepen en neerzetten. Sleep eenvoudigweg een stijlrij naar een nieuwe
positie in de tafel. De volgorde die u hier instelt, zorgt voor:

- De stijlmenuvolgorde in de menu's van Marked
- Sneltoetstoewijzingen (`⌘1`–`⌘9` voor de eerste negen ingeschakelde stijlen,
  `⌥⌘1`–`⌥⌘0` voor de volgende tien, enzovoort)

Sleep stijlen naar de gewenste sneltoetsen
bezetten.

## Stijlen toevoegen [adding-styles]

Er zijn verschillende manieren om nieuwe aangepaste stijlen toe te voegen aan de Stijlmanager:

### Knop Toevoegen [add-button]

Klik op de knop **Nieuwe stijl toevoegen** om een bestandskiezer te openen
waar u een of meer CSS-bestanden kunt selecteren om te importeren. Geselecteerde bestanden zullen zijn
toegevoegd aan de Stijlmanager en standaard ingeschakeld.

### Slepen en neerzetten [drag-and-drop]

U kunt CSS-bestanden rechtstreeks naar het venster Stijlmanager slepen. Wanneer je sleept
bestanden over het venster heen, verschijnt er een overlay met de tekst "Voeg een Custom stijl toe" (of
"Voeg N Custom stijlen toe" voor meerdere bestanden). Zet de bestanden neer om ze te importeren.

U kunt ook CSS-bestanden naar specifieke posities in de tabel slepen: de drop
indicator laat zien waar de nieuwe stijl zal worden ingevoegd, zodat u controle heeft
zowel import als positionering in één handeling.

Als u CSS-bestanden naar het {% prefspane Style %} voorkeurenpaneel sleept, gebeurt dat ook
importeer ze en open automatisch de Stijlmanager.

## Live voorbeeld [live-preview]

Het rechterdeelvenster van de Stijlmanager toont een live voorbeeld van de geselecteerde
stijl. Het voorbeeld geeft een uitgebreid voorbeelddocument weer met kopjes,
lijsten, tabellen, codeblokken, blockquotes en andere veel voorkomende Markdown elementen,
allemaal gestileerd met de daadwerkelijke CSS van de geselecteerde stijl.

Het voorbeeld gebruikt het CSS-bestand rechtstreeks vanaf de schijf, dus alle wijzigingen die u in uw
externe editor wordt onmiddellijk bijgewerkt in de preview. Dit maakt het gemakkelijk om
bekijk uw wijzigingen in realtime terwijl u aangepaste stijlen ontwikkelt.

### Voorbeeld van donkere modus [dark-mode-preview]

Met een selectievakje boven het voorbeeld kunt u schakelen tussen de lichte en donkere modus
voorvertoningen. Dit is handig om te testen hoe stijlen er in beide weergavemodi uitzien.
vooral als u stijlen maakt die zich aanpassen aan het uiterlijk van het systeem.

## Sneltoetsen [keyboard-shortcuts]

De Stijlmanager geeft een legenda weer onder de tabel die laat zien hoe toetsenbord
snelkoppelingen zijn toegewezen. De eerste negen ingeschakelde stijlen ontvangen {% kbd cmd 1 %} door
{% kbd cmd 9 %} ({% kbd cmd 0 %} is gereserveerd), de volgende tien ontvangen {% kbd opt cmd 1 %} tot en met {% kbd opt cmd 0 %}, enzovoort. U kunt de toegewezen sneltoetsen zien in het pop-upmenu Stijl in elk voorbeeld.

## Uitgeschakelde stijlen filteren [filtering-disabled-styles]

Met een selectievakje onder aan het venster kunt u uitgeschakelde instellingen weergeven of verbergen
stijlen. Als dit selectievakje niet is aangevinkt, worden alleen ingeschakelde stijlen weergegeven, wat het gemakkelijker maakt
focus op en herschik uw actieve stijlen. Indien aangevinkt, alle stijlen (ingeschakeld en uitgeschakeld)
worden getoond, zodat u uw volledige stijlcollectie kunt beheren.

## Ingebouwde stijlen herstellen [restoring-builtin-styles]

De knop **Alle ingebouwde stijlen herstellen** onder aan het venster
herstelt alle ingebouwde stijlen naar hun standaardstatus. Dit is handig als je dat hebt
ingebouwde stijlen heeft uitgeschakeld en deze opnieuw wilt inschakelen, of als u deze opnieuw wilt instellen
eventuele wijzigingen die zijn aangebracht aan ingebouwde stijlen.

## Tips [tips]

- **Ordenen op frequentie**: sleep uw meest gebruikte stijlen naar boven om ze weer te geven
  ze de gemakkelijkste sneltoetsen ({% kbd cmd 1 %}, {% kbd cmd 2 %}, etc.)

- **Uitschakelen in plaats van verwijderen**: in plaats van stijlen te verwijderen die u niet gebruikt,
  schakel ze uit. Ze blijven uit de buurt, maar blijven beschikbaar als dat nodig is
  ze later.

- **Gebruik duplicaat voor experimenten**: dupliceer een stijl voordat u een hoofdstijl maakt
  verandert zodat u altijd kunt terugkeren naar het origineel.

- **Voorbeeld tijdens bewerken**: Houd de Stijlmanager geopend tijdens het bewerken van CSS
  bestanden om te zien hoe uw wijzigingen in realtime worden bijgewerkt in het voorbeeldvenster.

- **Batchimport**: u kunt meerdere CSS-bestanden tegelijk selecteren wanneer u de
  Knop Toevoegen of sleep meerdere bestanden om ze allemaal in één actie te importeren.


