# <%= @title %>

Marked kan een voorbeeld van hetzelfde bestand bekijken met verschillende ingebouwde Markdown processors. Elk daarvan maakt een andere afweging tussen **schrijfworkflow** (boeken, blogs, GitHub README's) en **uitvoercontrole** (ID's, klassen, metadata). De standaard kies je in {% prefspane Processor %}; Ook kunt u per document de verwerker overschrijven.

Deze pagina vat samen hoe de vier hoofdprocessors verschillen. Voor volledige syntaxisdetails, zie de referentiepagina's onder **Help → Markdown Referentie** (bijv. [MultiMarkdown v5 Specification](MultiMarkdown_v5_Spec.html), [Kramdown Specification](Kramdown_Spec.html), [CommonMark Specification](CommonMark_Spec.html), [Discount GFM Specification](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5) [multimarkdown-v5]

**Best voor:** Lang proza, academisch of technisch schrijven en alles dat afhankelijk is van **metadata**, **citaten** en **MultiMarkdown-specifieke** functies.

Marked wordt geleverd met **MultiMarkdown 5** (zie de [MultiMarkdown User's Guide](https://fletcher.github.io/MultiMarkdown-5/) voor de upstream-documentatie).

### Sterke punten [strengths]

- **Verhalende en referentierijke documenten:** Voetnoten, bibliografie/citaties en tabellen zijn eersteklas.
- **Metadata:** Standaard MultiMarkdown metadatablokken (`Key: Value` headers) plus **transclusie** en andere MMD gemakken beschreven in de v5-handleiding.
- **Metadatavervanging:** Sleutels uit metadata kunnen in de hoofdtekst worden ingevoegd met vervanging in `[%key]`-stijl, zodat titels, auteursreeksen en vergelijkbare waarden gesynchroniseerd blijven met de header.
- **Tabellen, afbeeldingen en kruisverwijzingen:** Afgestemd op de functies gedocumenteerd voor MultiMarkdown 5.

### ID's en handmatige kopjes [ids-and-manual-headings]

- Kop-ID's zijn **genormaliseerd** op een manier die de neiging heeft om **kleine letters, aaneengeschakelde** slugs te produceren (geen spaties - woorden lopen door elkaar).
- Voor **handmatige header-ID's** gebruikt MultiMarkdown de vorm: `## Headline Text [my-id]` (de identificatie tussen haakjes na de koptekst).

### Wanneer moet je iets anders kiezen? [when-to-pick-something-else]

Als je takenlijsten met **GitHub__-smaak en het exacte gedrag van de huidige parser van GitHub nodig hebt, geef je de voorkeur aan **CommonMark (GFM)**. Als je **fijnmazige HTML klassen/ID's** nodig hebt voor willekeurige elementen, overweeg dan **Kramdown**.

---

## Kramdown [kramdown]

**Best voor:** Documenten waar u **precieze controle over de uitvoer van HTML** wilt: aangepaste **klassen**, **ID's** en attributen, zodat uw CSS zich kan richten op specifieke blokken en bereiken.

De [kramdown syntax reference](https://kramdown.gettalong.org/syntax.html) is de gezaghebbende gids.

### Sterke punten [strengths-2]

- **Meestal compatibel** met gewoonten in MultiMarkdown-stijl voor de dagelijkse Markdown, terwijl er eigen extensies worden toegevoegd.
- **Inline en blokattributenlijsten (IAL's):** Voeg `{: #id .class key="value"}` toe aan alinea's, kopteksten, codeblokken, links, afbeeldingen en meer --- ideaal voor sites in Jekyll-stijl en aangepaste stylesheets.
- **Header-ID's:** kramdown normaliseert automatisch gegenereerde header-ID's naar **kleine letters, door koppeltekens gescheiden** woorden (bijv. `my-section-title`). Voor **handmatige ID's** gebruikt u het `{#id}` formulier na de koptekst, bijvoorbeeld: Setext: `My Section {#my-section}` en dan de onderstreping, of ATX: `# My Section {#my-section}` (zie Kramdown's [headers](https://kramdown.gettalong.org/syntax.html#headers) voor de exacte plaatsing en IAL-regels).
- **Definitielijsten, voetnoten, slimme typografie, wiskundeblokken:** Uitgebreide functieset voor het publiceren van pijplijnen die meer nodig hebben dan "gewoon" Markdown.

### Wanneer moet je iets anders kiezen? [when-to-pick-something-else-2]

Als u vertrouwt op **MultiMarkdown-only** metadatavervanging (`[%key]`) of MMD-specifieke citatieworkflows, is **MultiMarkdown** wellicht beter geschikt. Voor **README- en opslagdocumenten** die online moeten overeenkomen met GitHub, is **CommonMark (GFM)** meestal dichterbij.

---

## CommonMark (GitHub Gearomatiseerd Markdown / cmark-gfm) [commonmark-github-flavored-markdown-cmark-gfm]

**Beste voor:** **README-bestanden**, **probleem-/PR-beschrijvingen** en **projectdocumentatie** die het huidige Markdown-gedrag** van **GitHub zo goed mogelijk moet benaderen.

Marked gebruikt een **GFM**-georiënteerde engine (cmark-gfm). De formele specificatie is de [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), gebouwd op [CommonMark](https://commonmark.org/).

### Sterke punten [strengths-3]

- **Meest overeenkomende met GitHub:** Tabellen, doorhalingen, takenlijstitems, afgeschermde codeblokken met taaltags en autolinks gedragen zich als moderne GitHub-weergave.
- **Ondubbelzinnig parseren:** CommonMark definieert blok-/inline-prioriteit en lijstregels nauwkeurig – strenger in sommige randgevallen dan het "klassieke" Markdown.pl-gedrag, maar **voorspelbaarder** zodra u de regels leert.
- **Praktisch voor ingepakte tekst:** Regels voor alinea's en lijsten zijn ontworpen om goed te werken met hard-ingepakt proza ​​(zie de specificaties van de secties over luie voortzettingen en lijsten).

### Kop-ID's [header-ids]

Automatisch gegenereerde kopankers zijn doorgaans **kleine letters en gescheiden door koppeltekens**, wat overeenkomt met de gebruikelijke slugging in GitHub-stijl.

### Wanneer moet je iets anders kiezen? [when-to-pick-something-else-3]

GFM repliceert geen workflows voor **MultiMarkdown metadata**, **kramdown IALs** of **MMD citatie**. Voor boeken, scripties of zware metadata gebruikt u, indien van toepassing, **MultiMarkdown** of **Kramdown**.

---

## Korting [discount]

**Beste voor:** Een **snelle, op C gebaseerde** processor die **klassieke Markdown** en een **oudere functieset met GitHub-smaak** bijhoudt - handig als u gedrag wilt dat dichter bij **originele Markdown** ligt, plus tabellen, voetnoten en gerelateerde extensies zonder het volledige CommonMark-regelboek.

Projectthuis: [Discount](https://www.pell.portland.or.us/~orc/Code/discount/).

### Sterke punten [strengths-4]

- **PHP Markdown Tabellen met extra stijl** en veel extensies (voetnoten, afgeschermde code indien ingeschakeld, enz. --- zie Marked's [Discount GFM Specification](Discount_GFM_Spec.html) voor wat Marked mogelijk maakt).
- **Optionele "GitHub" extra's** in upstream-korting (bijvoorbeeld selectievakjes als deze met de juiste vlaggen zijn gebouwd); Marked documenteert de combinatie die wordt verzonden op de pagina Kortingsspecificaties.
- **SmartyPants-stijl typografie** en andere gemakken beschreven op de Discount-site (hoewel alle meegeleverde processors daadwerkelijk typografische functies bieden).
- Filosofisch dichtbij **John Gruber's Markdown** plus praktische uitbreidingen, in plaats van de volledige CommonMark-testsuite.

### Wanneer moet je iets anders kiezen? [when-to-pick-something-else-4]

Voor **pixel-perfecte pariteit met de huidige github.com** geeft u de voorkeur aan **CommonMark (GFM)**. Voor **MultiMarkdown metadata en citaten** gebruikt u **MultiMarkdown**.

---

## Snelle vergelijking [quick-comparison]

| Zorg | MeerdereMarkdown | Kramdown | CommonMark (GFM) | Korting |
|--------|--------------|--------|----------------|----------|
| **Primair gebruik** | Proza, papieren, boeken | Vormgegeven HTML, Jekyll-achtige sites | README's, GitHub-achtige documenten | Klassieke MD + extensies |
| **Citaties / MMD metadata** | Sterk | Via andere syntaxis | Nee | Nee |
| **Handmatige kop-ID-stijl** | `## Title [id]` | `## Title {: #id }` (IAL) | Spec / GitHub slugregels | Geen |
| **Automatische kop-ID's** | Kleine letters aaneengeschakeld | Kleine letters afgebroken | Kleine letters afgebroken | Met kleine letters en afgebroken |
| **Extra attributen (klassen/id's)** | Beperkte MMD mechanismen | **IAL's** — zeer sterk | Beperkt | Beperkt |

---

## Zie ook [see-also]

- [Settings: Processor](Settings_Processor.html) — standaardprocessor en gerelateerde opties
- [Markdown Dingus](Markdown_Dingus.html) — probeer processors naast elkaar in Marked
- [Custom Processor](Custom_Processor.html) — sluit indien nodig uw eigen gereedschapsketen aan