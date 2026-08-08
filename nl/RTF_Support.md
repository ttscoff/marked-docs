# <%= @title %>

Marked kan Rich Text Format (`.rtf`) en RTFD (`.rtfd`) documenten rechtstreeks openen. Sleep een bestand naar Marked of gebruik {% appmenu File, Open... ({{cmd}}O) %}. Het document wordt geconverteerd naar Markdown voor voorbeeldweergave en export.

Dit werkt goed met documenten uit **Pages**, **TextEdit**, **Word** en andere apps die RTF of RTFD opslaan. Marked is nog steeds een **preview**-tool: u bewerkt in de oorspronkelijke toepassing en Marked wordt bijgewerkt wanneer u opslaat.

## Hoe conversie werkt [how-conversion-works]

Marked converteert RTF naar HTML met behulp van de systeemtekstengine en vervolgens naar Markdown. De converter:

- Wijst **grote lettergroottes van alinea's** toe aan kopniveaus (ten opzichte van de meest voorkomende hoofdtekstgrootte in het document)
- Behoudt **vet**, *cursief* en links waar mogelijk
- Extraheert **afbeeldingen** uit RTFD-bundels en ingesloten bijlagen
- Behandelt RTF bestandsnamen **niet** als afbeeldingsbijschriften (zie afbeeldingen hieronder)

Dezelfde conversiepijplijn wordt gebruikt voor het compileren van Scrivener RTF en voor RTF bestanden die in andere documenten zijn opgenomen.

## Live voorbeeld [live-preview]

Wanneer u het bestand RTF of RTFD in een andere toepassing opslaat, detecteert Marked de wijziging en wordt het voorbeeld automatisch vernieuwd.

## Afbeeldingen [images]

RTF definieert geen afzonderlijk "bijschrift"-veld op een manier waarop Cacao wordt geëxporteerd naar HTML. Wat in uw lay-out op een bijschrift lijkt, is meestal **normale tekst** in de volgende alinea, en Marked behoudt dat als hoofdtekst.

Ingesloten afbeeldingen en afbeeldingen in RTFD-bundels (bijvoorbeeld `pastedGraphic.png` in een Pages-export) worden gekopieerd naar een cachemap onder `~/Library/Caches/Marked/Watchers/`. Paden voor voorbeeldafbeeldingen wijzen naar de bestanden in de cache totdat u exporteert.

Marked gebruikt **niet** de bestandsnaam van de afbeelding als alternatieve tekst of een bijschrift met meerdereMarkdown figuren. Je zou `pastedGraphic.png` niet onder de afbeelding moeten zien, tenzij je die tekst in het document hebt getypt.

## Exporteren en andere functies [export-and-other-features]

Na de conversie behandelt Marked het document als andere gecompileerde bronnen (vergelijkbaar met [Scrivener](Scrivener_Support.html) en [DOCX](Working_With_DOCX.html)): export, statistieken en de meeste preview-functies worden uitgevoerd op basis van de gegenereerde Markdown die is opgeslagen in de Watchers-cache.

## Beperkingen [limitations]

De conversiekwaliteit is afhankelijk van de brontoepassing. Algemeen:

- **Koppen** worden afgeleid van de lettergrootte, niet van de omtrekstijlen van Word/Pages
- **Complexe lay-out** (tabellen met meerdere kolommen die alleen worden gebruikt voor positionering, tekstvakken) worden mogelijk niet correct toegewezen aan Markdown
- **Vergelijkingen** in RTF worden niet ondersteund in het voorbeeld (zie [MathJax](MathJax.html) voor Markdown wiskunde)
- **Legacy `.doc`** (binair Word) wordt niet ondersteund; sla eerst op als DOCX of RTF

Voor een eenmalige plakactie zonder een bestand op te slaan, gebruikt u in plaats daarvan [Clipboard Preview](Opening_Files.html#from-the-clipboard).

## Gerelateerde onderwerpen [related-topics]

- [PDF Support](PDF_Support.html) -- open PDF documenten als Markdown bronnen
- [Working with DOCX](Working_With_DOCX.html) -- Word-documenten met het bijhouden van wijzigingen en opmerkingen
- [Opening Files](Opening_Files.html) -- slepen en neerzetten, Recent openen, klembord
- [Exporting](Exporting.html) -- Kopieer Rich Text en sla RTFD op (exporteren), anders dan het openen van RTF als bronbestand