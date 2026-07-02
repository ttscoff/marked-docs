# <%= @title %>

Marked bevat native **Shortcuts**-acties (App-intenties) voor het openen van bestanden, het wijzigen van voorbeeldstijlen en het exporteren van documenten. Deze acties verschijnen in de Shortcuts-app wanneer u zoekt naar **Marked** en zijn beschikbaar op **macOS 13 (Ventura)** of hoger.

Voor scriptgebaseerde automatisering met een volledig objectmodel, zie [AppleScript Support](AppleScript_Support.html). Voor URL-gebaseerde workflows vanuit de shell, zie de [URL Handler](URL_Handler.html).

## Acties zoeken

1. Open de app **Snelkoppelingen**.
2. Maak een nieuwe snelkoppeling of bewerk een bestaande.
3. Zoek in de actiebibliotheek naar **Marked**.

Acties zijn gegroepeerd onder **Documenten** en **Exporteren**. Marked registreert ook Siri-zinnen zoals "Exporteer bestand met Marked" en "Openen in Marked" voor snelle snelkoppelingen.

## Actiesoverzicht

| Actie | Doel |
| --- | --- |
| **Bestand openen over Marked** | Open een Markdown- of tekstbestand in een voorbeeldvenster. |
| **Voorbeeldstijl instellen** | Wijzig het voorbeeldthema voor een geopend document (of open eerst een bestand). |
| **Bestand openen en exporteren** | Open een bestand en exporteer het vervolgens naar een ander formaat. |
| **Exportdocument** | Exporteer een geopend document (voorvenster of een specifiek bestand). |
| **Geopende documenten exporteren** | Exporteer elk document dat momenteel geopend is in Marked. |

Alle exportacties retourneren het geëxporteerde bestand (of bestanden) als uitvoer van snelkoppelingen **Bestand**, zodat u ze kunt doorgeven aan de volgende stap (Mail, Finder, een andere app).

## Bestand openen over Marked

**Parameter:** **Bestand** -- het document dat u wilt openen (vanuit Finder, Deelblad of een eerdere stap Snelkoppelingen).

Marked opent het bestand in een voorbeeldvenster. Gebruik dit als u een voorbeeld wilt bekijken of bewerken in Marked voordat u iets anders doet.

## Voorbeeldstijl instellen

**Parameters:**

- **Stijl** -- bekijk een voorbeeld van een stijl uit een kiezer (dezelfde namen als het voorbeeldstijlmenu en Stijlmanager).
- **Bestand** (optioneel) -- een specifiek bestand. Indien dit wordt weggelaten, gebruikt Marked het voordocument. Als het bestand nog niet geopend is, opent Marked het eerst.

Als u een stijl instelt, wordt het voorbeeld opnieuw geladen met dat thema (hetzelfde als wanneer u een stijl kiest in het voorbeeldstijlmenu).

## Exportacties

Exportacties delen dezelfde kernopties:

| Parameter | Beschrijving |
| --- | --- |
| **Formaat** | Markdown, HTML, gepagineerd PDF, doorlopend PDF, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack of OPML. |
| **Profiel** (optioneel) | Een opgeslagen exportprofiel van {% prefspane Export %}. |
| **Stijl** (optioneel) | Voorbeeldstijl die moet worden toegepast vóór het exporteren (volledige voorbeeldherladen). |
| **Paginaformaat** (optioneel) | Naam van paginaformaat afdrukken, zoals `A4` of `Letter`. |
| **Marges** (optioneel) | Marge verkort (zie hieronder). |
| **Lettergrootte** (optioneel) | Basislettergrootte in punten voor PDF export, zoals `14` of `12pt`. |
| **Uitvoerbestand** / **Uitvoermap** (optioneel) | Bestemmingspad. Indien dit wordt weggelaten, schrijft Marked naast het bronbestand met de juiste extensie. |

**Opmerkingen**

- **Gepagineerd PDF** gebruikt dezelfde printlay-outpijplijn als {% appmenu File, Export, Paginated PDF %}. Het is niet beschikbaar voor onbewerkte HTML voorbeelddocumenten.
- **HTML** export gebruikt het gerenderde voorbeeld (wat u ziet in de WebView), niet het onbewerkte Markdown bronbestand.
- **Continu PDF** legt de huidige preview-WebView-indeling vast.
- **Lettergrootte** maakt dezelfde optie voor aangepaste export/afdruklettergrootte mogelijk vanaf {% prefspane Export %}. Het heeft geen invloed op Fountain-documenten.

### Bestand openen en exporteren

Beste voor Finder-workflows: kies een Markdown-bestand, open het in Marked en exporteer het in één stap.

**Parameters:** **Bestand** (vereist), plus de bovenstaande exportopties.

Voorbeeldgebruik: een snelle actie die bestanden uit Finder haalt en **gepagineerd PDF** exporteert met een gekozen profiel en stijl.

### Document exporteren

Exporteer een document dat **al geopend** is over Marked.

**Parameters:**

- **Bestand** (optioneel) -- een specifiek geopend bestand. Indien dit wordt weggelaten, exporteert Marked het voordocument.
- Exportopties en **Uitvoerbestand** zoals hierboven.

Gebruik dit wanneer Marked al actief is en u het huidige voorbeeld wilt exporteren zonder het bestand opnieuw te openen.

### Geopende documenten exporteren

Exporteer **elk** voorbeelddocument dat momenteel geopend is in Marked.

**Parameters:**

- **Formaat** en exportopties (profiel, stijl, paginagrootte, marges, lettergrootte).
- **Uitvoermap** (optioneel) -- map voor geëxporteerde bestanden. Als u dit weglaat, wordt elk bestand naast het brondocument geëxporteerd.

Handig voor batchexport na het bekijken van meerdere hoofdstukken of notities in Marked.

## Marge afkorting

Wanneer **Marges** is ingesteld voor een exportactie, gebruikt u een tekenreeks met één tot vier metingen. Eenheden: `in`, `cm`, `mm`, `pt`, of `"` voor inches. Een getal zonder eenheid wordt behandeld als punten.

| Waarde | Betekenis |
| --- | --- |
| `1in` | Alle kanten |
| `1in 2in` | Boven en onder `1in`, links en rechts `2in` |
| `1in 2in 1in` | Boven `1in`, links en rechts `2in`, onder `1in` |
| `1in 2in 1in 2in` | Boven, rechts, onder, links |

Dit komt overeen met de `margins` sleutel in [AppleScript](AppleScript_Support.html#with-options-properties-record) exportrecords.

## Voorbeeldworkflows

### Finder-bestand naar PDF

1. **Bestand openen en exporteren**
2. **Bestand** - invoer van Share Sheet of Finder Quick Action.
3. **Formaat** -- Gepagineerd PDF.
4. **Stijl** - optioneel thema (bijvoorbeeld Amblin).
5. **Profiel** -- optioneel opgeslagen exportprofiel.
6. **Uitvoerbestand** -- optioneel; laat dit leeg om `filename.pdf` naast de bron te schrijven.

### Exporteer wat open is over Marked

1. **Exportdocument**
2. Laat **Bestand** leeg om het voorvenster te gebruiken.
3. Kies **Formaat** en optioneel profiel of stijl.

### Geopende documenten batchgewijs exporteren

1. **Open documenten exporteren**
2. Kies **Formaat** (bijvoorbeeld EPUB).
3. Stel eventueel **Uitvoermap** in om alle exports in één map te verzamelen.

### Stijl en vervolgens exporteren (twee stappen)

1. **Voorbeeldstijl instellen** - kies een stijl (richt eventueel een specifiek **Bestand**).
2. **Exportdocument** - hetzelfde bestand of voordocument, met het gewenste **Formaat**.

U kunt **Stijl** ook rechtstreeks doorgeven aan een exportactie; Marked past het thema toe en wacht op het opnieuw laden van het voorbeeld voordat het exporteert.

## Paden exporteren en sandboxen

- Als **Uitvoerbestand** of **Uitvoermap** wordt weggelaten, wordt Marked naast het brondocument geschreven.
- Marked kan tussenmappen maken als het exportpad **in de map van het geopende document** ligt.
- Voor exporten buiten de map van het document is een beschrijfbaar pad nodig waartoe Marked toegang heeft (opgeslagen documentlocatie, bladwijzers met veiligheidsreikwijdte of mappen die u hebt toegekend via Open-dialoogvensters).

Zie [AppleScript Support](AppleScript_Support.html#export-paths-and-sandboxing) voor dezelfde sandboxregels.

## Legacy `convert_to` actie

Het AppleScript-woordenboek geeft nog steeds **`convert_to`** weer voor het converteren van Markdown tekst of bestanden zonder een open voorbeeld. De bovenstaande Native Shortcuts-acties hebben de voorkeur: ze openen documenten correct, wachten tot het voorbeeld is geladen en ondersteunen gepagineerde PDF asynchroon export.

Zie [Shortcuts and <!--MKPH0--> in AppleScript Support](AppleScript_Support.html#shortcuts-and-convert_to) voor details over de oudere opdracht.

## Probleemoplossing: acties verschijnen niet in snelkoppelingen

Snelkoppelingenindexen **één** Marked installatie per bundel-ID (`com.brettterpstra.marked`). Het geeft de voorkeur aan de kopie met het **hoogste buildnummer** (`CFBundleVersion`), niet noodzakelijkerwijs de app die u zojuist in Xcode hebt gebouwd.

Als Marked niet verschijnt onder **Apps** in de actiebibliotheek voor snelkoppelingen:

1. Maak een lijst van elke kopie op schijf:
   ```bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Verwijder verouderde kopieën of hernoem ze (bijvoorbeeld een oude `Marked.app` op het bureaublad of in `/Applications` die is gekopieerd van een build **zonder** metagegevens van snelkoppelingen).
3. Voer de build uit waarvan u wilt dat de snelkoppelingen deze gebruiken (Xcode **Run**, of open de `.app` rechtstreeks in DerivedData).
4. Sluit de app **Shortcuts** af en open deze opnieuw.

Een build die snelkoppelingen bevat, bevat `Contents/Resources/Metadata.appintents`. U kunt het volgende verifiëren:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Bij het opstarten registreert Marked `[MKShortcuts] Registering App Intents` in Console.app wanneer de registratie wordt uitgevoerd (macOS 13+).

## Foutopsporing

Schakel **Debug-modus** in {% prefspane Advanced %} in. Marked registreert exportstappen op Info-niveau met het voorvoegsel `[AppleScript]` in Console.app en de logviewer van Marked (de exportpijplijn wordt gedeeld met AppleScript).

## Fouten

Veel voorkomende berichten wanneer een actie mislukt:

- Er is geen Marked document beschikbaar (niets geopend en geen bestand opgegeven).
- Dat bestand is niet geopend in Marked (gebruik **Bestand openen** of **Bestand openen en exporteren**).
- Onbekende exportprofiel- of voorbeeldstijlnaam.
- Er is een time-out opgetreden bij het wachten op het laden of herladen van het voorbeeld.
- Fouten met toestemming voor exportpad of mislukte generatie van gepagineerde PDF.