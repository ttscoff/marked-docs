# Markdownifier [markdownifier]

De Markdownifier is een tool die automatisch inhoud van webpagina's extraheert en deze converteert naar een schoon Markdown-formaat. Het verwerkt op intelligente wijze webinhoud om u alleen de betekenisvolle tekst en structuur te geven, waarbij advertenties, navigatie-elementen en andere rommel worden weggefilterd.

![Markdownify URL][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Hoe het werkt [how-it-works]

De Markdownifier maakt gebruik van geavanceerde algoritmen voor inhoudsextractie om:

1. **Ophalen en analyseren** webpagina-inhoud
2. **Identificeer de tekst en structuur van het hoofdartikel**
3. **Schoon en formatteer** de inhoud in de juiste Markdown
4. **Filter uit** advertenties, navigatie en andere niet-inhoudelijke elementen
5. **Behoud** belangrijke opmaak, zoals kopteksten, lijsten en links

## De Markdownifier openen [opening-the-markdownifier]

Om toegang te krijgen tot de Markdownifier, open je {% appmenu File, New, Markdownify URL (@~k) %}. Voer de URL in die u wilt Markdownify en druk op Return ({% kbd return %}).

## Met behulp van de Markdownifier [using-the-markdownifier]

### Basisgebruik [basic-usage]

1. **Open de Markdownifier** met een van de bovenstaande methoden
2. **Voer een URL in** in het tekstveld
3. **Klik op "Automatisch"** of druk op `Return` om inhoud te extraheren
4. De geëxtraheerde inhoud wordt **automatisch geopend** in een nieuw Marked document

### Handmatige inhoudselectie [manual-content-selection]

Als automatische extractie niet de gewenste inhoud vastlegt:

1. Klik op de knop **"Handmatig"** om de pagina in een webweergave te laden
2. **Navigeer en scroll** om de gewenste inhoud te vinden
3. **Klik op de knop "Inhoud extraheren"** die op de webpagina verschijnt
4. De geselecteerde inhoud wordt geconverteerd naar Markdown en geopend in Marked

### Klembordintegratie [clipboard-integration]

De Markdownifier detecteert automatisch URL's op uw klembord wanneer deze wordt geopend:

- Als er een URL wordt gevonden, wordt deze **vooraf ingevuld** in het URL-veld
- U moet nog steeds op **"Automatisch"** klikken of op `Return` drukken om het te verwerken
- Dit voorkomt onbedoelde verwerking van klembord-URL's

## Inhoudsverwerking [content-processing]

### Automatische inhoudvalidatie [automatic-content-validation]

De Markdownifier valideert op intelligente wijze de geëxtraheerde inhoud om ervoor te zorgen dat deze betekenisvolle tekst bevat:

- **Verwijdert metadata** (YAML frontmatter, MultiMarkdown headers)
- **Verwijdert linkdefinities** en links in referentiestijl
- **Filtert** zelfstandige URL's en navigatie-elementen
- **Comprimeert witruimte** voor nauwkeurige lengtebepaling
- **Vereist minimaal 200 tekens** aan daadwerkelijke inhoud

Als de geëxtraheerde inhoud te kort is of voornamelijk uit navigatie/advertenties lijkt te bestaan, valt de Markdownifier automatisch terug naar de handmatige selectiemodus.

### Inhoudsopmaak [content-formatting]

De geëxtraheerde inhoud wordt geformatteerd als schoon Markdown met:

- **Bronlink** bovenaan: `[source](original-url)`
- **H1-titelinvoeging** indien nodig
- **Bewaarde lijsten** (geordend en ongeordend)
- **Bijgehouden links** en nadrukopmaak
- **Schone paragrafen** met de juiste spatiëring

## Veiligheidsvoorzieningen [safety-features]

### Crashpreventie [crash-prevention]

De Markdownifier bevat verschillende veiligheidsmaatregelen om crashes te voorkomen:

- **Blokkeert problematische URL's** (advertentienetwerken, trackingservices, crypto-gerelateerde inhoud)
- **Filtert beschadigde afbeeldingen** die weergaveproblemen kunnen veroorzaken
- **Schakelt geavanceerde webfuncties uit** die instabiliteit kunnen veroorzaken
- **Automatisch crashherstel** met terugval in veilige modus

### Privacybescherming [privacy-protection]

- **Privé-browsingmodus** voorkomt tracking en cookies
- **Geen plug-ins of Java**-uitvoering vanwege de veiligheid
- **Beperkt JavaScript** met crypto-API-blokkering
- **Bronnenfiltering** blokkeert tracking en advertentie-inhoud

## Problemen oplossen [troubleshooting]

### Inhoud niet geëxtraheerd [content-not-extracted]

Als automatische extractie mislukt:

1. **Probeer handmatige selectie** met de knop "Handmatig".
2. **Controleer of de site JavaScript vereist** - sommige sites moeten handmatig worden geladen
3. **Controleer of de URL** toegankelijk is en artikelinhoud bevat
4. **Zoek naar betaalmuren of inlogvereisten** die de toegang kunnen blokkeren

### WebView-problemen [webview-issues]

Als de webweergave instabiel wordt:

1. De Markdownifier gaat **automatisch naar de veilige modus**
2. **JavaScript wordt uitgeschakeld** om crashes te voorkomen
3. **Gebruik de knop "Converteren"** in plaats van handmatige selectie
4. **Sluit en open** de Markdownifier om te resetten

### Ontbrekende inhoud [missing-content]

Als er belangrijke inhoud ontbreekt in de extractie:

1. Het **automatische algoritme** heeft dit mogelijk weggefilterd
2. **Gebruik handmatige selectie** om de gewenste specifieke inhoud te kiezen
3. **Controleer de bron HTML** om te zien of de inhoud dynamisch wordt geladen
4. **Probeer een andere URL** als de site een complexe structuur heeft

## Tips voor de beste resultaten [tips-for-best-results]

### URL-selectie [url-selection]

- **Gebruik artikel-URL's** in plaats van startpagina's of categoriepagina's
- **Vermijd URL's met trackingparameters** indien mogelijk

### Inhoudskwaliteit [content-quality]

- **Langere artikelen** halen over het algemeen beter uit dan korte berichten
- **Goed gestructureerde inhoud** met de juiste kopjes werkt het beste
- **Vermijd sites met zwaar JavaScript** voor automatische extractie

### Handmatige selectie [manual-selection]

- **Wacht tot de pagina volledig is geladen** voordat u deze uitpakt
- **Blader door de inhoud** om er zeker van te zijn dat alles is geladen
- **Beweeg over gebieden** om het kleinste blauwe vak te selecteren dat alle inhoud bevat die u wilt extraheren
- **Klik** wanneer u de gewenste inhoud heeft gevonden

## Geavanceerde functies [advanced-features]

### Batchverwerking [batch-processing]

Terwijl de Markdownifier één URL tegelijk verwerkt, kunt u:

- **Meerdere URL's in de wachtrij plaatsen** door de Markdownifier meerdere keren te openen
- **Gebruik Services-integratie** om URL's van andere applicaties te verwerken
- **Kopieer de geëxtraheerde inhoud** en plak deze in bestaande Marked documenten

### Integratie met Marked [integration-with-marked]

Geëxtraheerde inhoud wordt geopend over Marked met:

- **Automatische bestandsnaamgeving** op basis van de titel van het artikel
- **Behoud van bron-URL** in de metadata van het document
- **Volledige Marked mogelijkheden** voor lezen en exporteren)

## Technische details [technical-details]

### Ondersteunde inhoudstypen [supported-content-types]

- **HTML artikelen** met standaard opmaak
- **Blogposts** en nieuwsartikelen
- **Documentatie** en helppagina's
- **Forumberichten** en discussie-inhoud

### Beperkingen [limitations]

- **Voor sites met een betaalmuur** is mogelijk inloggen en handmatige extractie vereist
- **Sites met veel JavaScript** vereisen mogelijk handmatige selectie
- **Dynamische inhoud** die wordt geladen nadat de pagina is geladen, wordt mogelijk gemist, maar met handmatige extractie kan deze worden vastgelegd
- **Complexe lay-outs** kunnen ongewenste navigatie-elementen bevatten

De Markdownifier is ontworpen om de extractie van webinhoud zo eenvoudig en betrouwbaar mogelijk te maken, terwijl er terugvalopties worden geboden voor complexe of problematische websites.