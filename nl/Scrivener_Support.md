# <%= @title %>

Gebruik uw twee favoriete schrijfhulpmiddelen samen.

> Marked kan nog steeds Scrivener 2.0-bestanden lezen, maar de ontwikkeling zal zich richten op versie 3 na Marked 2.5.11.

## Scrivener 3.0 Basis [scrivener-30-basics]

Sleep een Scrivener project (.scriv) naar Marked en het zal worden gecompileerd en bekeken. Als u de optie kiest om .scriv-bestanden te openen in Scrivener (hierboven), zal Marked ook Scrivener starten wanneer u het bestand naar Marked sleept.

Net als bij andere documenten worden wijzigingen in Scrivener bestanden live bijgewerkt wanneer ze worden opgeslagen. En als een Scrivener document op de voorgrond staat in Marked, zal {% kbd cmd E %} het in Scrivener voor u openen.

## Bindmiddeldocumenten filteren [filtering-binder-documents]

Wanneer u een Scrivener-project opent in Marked, wordt de voorbeeldinhoud alleen opgebouwd uit de binderdocumenten die u selecteert. Filteren is altijd actief voor `.scriv` bestanden; het filterpaneel is slechts een handige manier om te veranderen wat er is inbegrepen.

Open het paneel vanuit **Proofing > Filter Scrivener Documenten** ({% kbd opt-cmd-f %}). Het menu-item toont een vinkje terwijl het paneel zichtbaar is. Als u het paneel sluit, wordt het filteren niet uitgeschakeld en worden uw selecties niet opnieuw ingesteld.

In het filterpaneel worden de bindmiddelensecties van uw project weergegeven (Concept, Onderzoek en andere bindmiddelen op het hoogste niveau, behalve de Prullenbak). Elke sectie is standaard samengevouwen. Vouw een sectie uit om de documenten en mappen in een overzicht te zien:

- Vink elk **tekstdocument** aan of uit om het op te nemen of uit te sluiten van het voorbeeld.
- Klik op een **map**-rij om alle onderliggende mappen te selecteren of deselecteren. Een streepje in het selectievakje betekent dat slechts enkele nakomelingen zijn geselecteerd.
- Rijen waarvoor **Opnemen in compileren** is uitgeschakeld in Scrivener, worden grijs weergegeven, maar u kunt ze nog steeds controleren om er een voorbeeld van te bekijken in Marked.
- **Afbeeldingen, PDFs en andere niet-tekst** binderitems verschijnen in de lijst, maar kunnen niet worden geselecteerd.
- **Ontbrekende RTF** bestanden verschijnen nog steeds; als u inhoud toevoegt in Scrivener terwijl Marked geopend is, wordt het voorbeeld bij het opslaan bijgewerkt, net als bij elke andere Scrivener wijziging.

Gebruik **Alles selecteren** en **Alles deselecteren** bovenaan het paneel voor het hele project. Elke sectiekop heeft alleen de knoppen **Alle** en **Geen** voor die sectie. **Alles deselecteren** betekent dat er geen documenten zijn gecontroleerd.

Als er niets is geselecteerd, toont het voorbeeld een kort bericht met een link om het filterpaneel te openen (`x-marked://scrivenerfilter`). U kunt die URL in scripts of andere apps gebruiken om het paneel voor het voorste Scrivener document in Marked te vergroten.

Uw selecties van selectievakjes worden per Scrivener project opgeslagen (via de project-ID in het `.scrivx` bestand) en hersteld de volgende keer dat u dat project opent in Marked. De eerste keer dat u een project opent, selecteert Marked alleen **Concept**-mapdocumenten waarvan de vlag **Opnemen in compileren** Ja is (of niet ingesteld, wat Scrivener als Ja behandelt). Onderzoek en andere bindmiddelen beginnen ongecontroleerd; compile-excluded Conceptitems starten ongecontroleerd, maar blijven selecteerbaar in de lijst.

Scrivener 2 projecten tonen alleen de binder **Concept** in het filterpaneel. Scrivener 3 projecten bevatten alle mappen behalve Prullenbak.

Het filterpaneel kan open blijven naast andere tools zoals **Visualiseer Woordherhaling**. Als u een selectievakje wijzigt, wordt het voorbeeld na een korte vertraging opnieuw gecompileerd; als een groot project nog bezig is met compileren, annuleert Marked de lopende import en begint opnieuw met uw nieuwe selectie.

## Markdown headers van Scrivener titels [markdown-headers-from-scrivener-titles]

Marked kan ook hiërarchische Markdown headers voor u maken op basis van de pagina's van uw Scrivener bestand. Om dit in te schakelen, vinkt u gewoon de hierboven weergegeven optie aan.

## MultiMarkdown metagegevens [multimarkdown-metadata]

Als het eerste document in uw map Concept de naam "metadata" heeft, wordt het behandeld als MultiMarkdown metadata aan het begin van het voorbeelddocument. Er wordt geen koptekst ingevoegd voor deze sectie, ongeacht de instelling "Markdown Kopteksten uit Scrivener Titels" (hierboven beschreven), waardoor de MultiMarkdown processor deze als metagegevens kan lezen en overeenkomstige vervangingen en exportopties mogelijk maakt.

U kunt dit bestand YAML-geformatteerd maken als uw processor er een is die YAML verwerkt.

Als u geen `metadata` document gebruikt, kan Marked ook MultiMarkdown-metagegevens uit de compileerinstellingen van uw project (`Settings/compile.xml`) vooraf laten gaan, met dezelfde velden **Titel** en **Auteur** die Scrivener zou exporteren naar MultiMarkdown. Dit is standaard ingeschakeld (voorkeurssleutel `scrivenerCompileMetadata`). Custom metadatavelden worden alleen opgenomen als ze voorkomen in de **MMD Metadata** compilatie-instellingen van het project, niet uit aangepaste velden per document.

## Koppelingen [links]

Voor externe (HTTP) links kunt u de syntaxis van Markdown of de linkopmaak van Scrivener gebruiken. Marked converteert het Scrivener-formaat naar Markdown voordat het wordt verwerkt.

## Opmerkingen [comments]

Marked kan opmerkingen en voetnoten verwerken die inline in het document zijn gemaakt.

## Tafels [tables]

Marked kan basis Scrivener tabellen converteren. Als u echter een tabel in uw uitvoer wilt opnemen, kunt u dit het beste in [MultiMarkdown table format](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables) doen. (Een app met de naam [TableFlip](http://tableflipapp.com/) kan het genereren hiervan een eenvoudige taak maken.)

## Extra Scrivener Functies [additional-scrivener-features]

Naast de basisfuncties voor compileren en previewen ondersteunt Marked ook enkele Scrivener-specifieke conventies. Ten eerste kunt u in uw Scrivener-document "Opmaak behouden" inline of op een blok met zelfstandige tekst gebruiken. Dit wordt in het voorbeeld geconverteerd naar codeblokken.

Marked leest ook _inline_ voetnoten uit Scrivener. Als u een voetnoot in of aan het einde van een alinea invoert, wordt deze in het voorbeeld omgezet naar een MultiMarkdown voetnoot.

## Afbeeldingen gebruiken in uw Scrivener document [using-images-in-your-scrivener-document]

Afbeeldingen kunnen worden ingesloten in het Scrivener document, of er kan naar worden verwezen met de Markdown afbeeldingsyntaxis. De Markdown versie van een afbeeldingstag is `![alt text](path/to/image.ext "optional title/description")`. Referentieformaat kan ook worden gebruikt:

![alt text][img1]

    [img1]: /path/to/image.ext "optional description"

Het basispad voor de uitvoer HTML in het voorbeeld wordt ingesteld op de map die het document Scrivener bevat. Als u afbeeldingen in dezelfde map plaatst als het werkdocument, zijn ze dus rechtstreeks toegankelijk. Als uw Scrivener-document zich in `~/Desktop/TestDoc.scriv` bevindt en u een afbeelding hebt met de naam "testimage.png" in `~/Desktop/testimage.png`, kunt u de afbeelding aan uw document toevoegen met behulp van:

![Test image](testimage.png)

Relatieve paden op basis van de bovenliggende map van het document zullen werken, en absolute paden zullen overal toegang tot afbeeldingen mogelijk maken, maar zijn mogelijk niet zo draagbaar voor HTML uitvoer.

## Beveiligingsopmerking [security-note]

Er wordt een cachemap gemaakt in ~/Library/Application Support/Marked wanneer u uw .scriv-bestand opent in Marked. Dit is geen beveiligde map, dus als uw originele document zich op een gecodeerde schijf bevindt of anderszins beschermd is, houd er dan rekening mee dat de inhoud ervan niet-gecodeerd in de cache zal zijn. Voor beperkte bescherming kunt u ervoor zorgen dat deze cache niet in Spotlight verschijnt door ~/Library/Application Support/Marked toe te voegen aan uw privacy-instellingen in Spotlight.

Zie [Additional app integrations](Additional_Application_Support.html) voor klembordvoorbeeld, wiki-links, scripting en de volledige lijst met handleidingen per app.

