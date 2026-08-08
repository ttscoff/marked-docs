# <%= @title %>

Opties in de {% prefspane Apps %}:

(Zie [Additional App Support](Additional_Application_Support.html))

![Settings: Apps][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Algemene instellingen [general-settings]

Teksteditor
: Selecteer een teksteditor om het huidige document te ontvangen wanneer u {% kbd cmd E %} typt.

Bewerk nieuwe bestanden automatisch
: Wanneer u de opdracht "Nieuw bestand" gebruikt, wordt met deze optie automatisch het gemaakte bestand geopend in de door u gekozen externe editor.

Links naar tekstbestanden moeten worden geopend in:
: Bepaal het gedrag van Marked wanneer een link waarop in een voorbeeldvenster wordt geklikt, naar een lokaal tekstbestand leidt.

Afbeeldingseditor
: Selecteer een applicatie die u wilt openen wanneer u met de rechtermuisknop op een lokale afbeelding klikt en "Afbeelding bewerken" selecteert.

Afbeeldingsannotatie/opmaakeditor
: Selecteer een applicatie die u wilt openen wanneer u met de rechtermuisknop op een lokale afbeelding klikt en "Afbeelding annoteren" is geselecteerd.

Als er geen editor is gekozen, presenteert Marked een menu met geïnstalleerde applicaties wanneer u bewerkt of annoteert. Het menu bevat veelgebruikte Markdown-, afbeeldings- en annotatiehulpmiddelen die u op uw Mac kunt vinden, een **Andere…**-optie om een ​​app te kiezen uit `/Applications`, en **Gebruik deze app altijd** (standaard ingeschakeld) om uw keuze als standaard op te slaan. Gebruik de knop Wissen (cirkel met een X) naast elk Kies-besturingselement in {% prefspane Apps %} om een ​​selectie te verwijderen en terug te keren naar de kiezer.

### Applicatiespecifieke instellingen [application-specific-settings]

Toon standaard opmerkingen en annotaties
: Indien aangevinkt, worden aantekeningen gemaakt in de documenten Scrivener, Fountain, Word en CriticMarkup gemarkeerd weergegeven in het voorbeeld. Haal het vinkje weg om volledig te verbergen. Deze kunnen ook worden omgeschakeld tijdens het lezen van een document vanuit het menu {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%}.
: Wanneer opmerkingen zijn ingeschakeld, verschijnen opmerkingen en voetnoten in een zijbalk. Als u de muisaanwijzer op een opmerking plaatst, wordt naar de plaats in het document verwezen waar deze voorkomt.

#### DocC [docc]

[(Info on DocC Support)](DocC_Support.html)

Los DocC-afbeeldingsreferenties op
: Los in een `.docc` documentatiecatalogus extensieloze `![](ImageName)` verwijzingen op naar afbeeldingen in de catalogus `Resources` map, inclusief `~dark` en `@2x` varianten.

Los donkere en @2x afbeeldingsvarianten op
: Voor lokale afbeeldingen met een bestandsextensie (`images/icon.png`), detecteert u begeleidende `~dark` en `@2x` bestanden in dezelfde map en verzendt u responsieve `<picture>` markup. Werkt in elk Markdown of HTML document, niet alleen in DocC-catalogi. Zie [Image Variants](Image_Variants.html).

#### Haakmarkering [hookmark]

Los hook:// URL's op in afbeeldingen en links
: Marked kan URL's lezen die door Hookmark zijn gemaakt en deze omzetten in hun pad op schijf.

#### Leanpub/GitBook [leanpubgitbook]

Schakel Leanpub-ondersteuning in
: Interpreteer bestanden met de naam `Book.txt` als indexbestanden en hanteer de speciale Leanpub-syntaxis.

Schakel GitBook-ondersteuning in
: Interpreteer bestanden met de naam `SUMMARY.md` als indexbestanden voor GitBook-documentatie.

#### Markdownifier [markdownifier]

Gebruik inlinelinks
: Markdown documenten gemaakt door de Markdownifier zullen inline gebruiken in plaats van referentielinks.

#### MarsBewerken [marsedit]

Voeg de berichttitel toe als Markdown header (h1)
: Gebruik de titel van het geselecteerde bericht als Markdown header.

Toon metadata als tabel
: Indien ingeschakeld, worden metagegevens zoals categorieën en titels weergegeven als een Markdown tabel in het voorbeeld.

#### Mappen [folders]

Bekijk alleen een voorbeeld van deze extensies
: Bij het openen van een map zoekt Marked naar het meest recent gewijzigde document, standaard met extensies zoals `md`, `mmd` en `html`. De lijst hier overschrijft de standaard.

#### Scrivener [scrivener]

[(Info on Scrivener Support)](Scrivener_Support.html)

Voeg documenttitels toe als Markdown kopteksten
: Parseer de titel van pagina's en geneste pagina's om hiërarchische Markdown headers te maken.

Voeg compileermetagegevens (titel, auteur) toe als deze ontbreken
: Wanneer een Scrivener-project geen `metadata` document of bestaande MultiMarkdown header heeft, zet u Titel en Auteur vóór de compileerinstellingen van het project (`Settings/compile.xml`).

Open .scriv-bestanden in Scrivener wanneer geopend in Marked
: Wanneer een Scrivener document wordt geopend in Marked, wordt het automatisch ook geopend in Scrivener.

#### Woord [word]

Wijzigingen bijhouden omzetten <-> CriticMarkup
: Indien ingeschakeld, wordt het bijhouden van wijzigingen in Word-documenten geconverteerd naar CriticMarkup bij het importeren, en wordt CriticMarkup geconverteerd naar het bijhouden van wijzigingen in Word bij het exporteren van DOCX bestanden.

#### Mindmaps/overzichten [MindMapsOutlines]

Insluiten als zeemeermin-mindmaps
: Elk selectievakje bestuurt één inbegrepen formaat. Wanneer **aan** wordt het opgenomen bestand geconverteerd naar een Mermaid-mindmapdiagram (opgeruimde boomstructuur). Wanneer **uit**, gebruikt Marked het alternatief voor dat formaat.
: **Mindmaps** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Indien ingeschakeld: Mindmap voor zeemeermin. Indien uitgeschakeld: iThoughts sluit de voorbeeldafbeelding in; MindManager en FreeMind converteren naar geneste Markdown lijsten.
: **OPML bestanden** (.opml). Indien ingeschakeld: Mindmap voor zeemeermin. Indien uitgeschakeld: geneste Markdown lijst.
: **OmniOutliner-omtrekken** (.ooutline). Indien ingeschakeld: Mindmap voor zeemeermin. Indien uitgeschakeld: geneste Markdown lijst (of checklist indien van toepassing).
: **Fietscontouren**. Indien ingeschakeld: Mindmap voor zeemeermin. Indien uitgeschakeld: geneste Markdown lijst.