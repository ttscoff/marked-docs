# <%= @title %>

Bekijk de [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) om te experimenteren met de MultiMarkdown processor.

## Wat is MultiMarkdown? [what-is-multimarkdown]

MultiMarkdown is een uitgebreide Markdown-processor die is ontworpen om met volledige documenten te werken in plaats van alleen met webpaginafragmenten. Het breidt de originele Markdown syntaxis uit met functies die conversie naar meerdere uitvoerformaten mogelijk maken, waaronder HTML, LaTeX, PDF, ODF en Microsoft Word-documenten.

## Belangrijkste kenmerken [key-characteristics]

- **Documentgericht**: ontworpen voor volledige documenten, niet alleen voor webfragmenten
- **Uitvoer in meerdere formaten**: converteert naar HTML, LaTeX, PDF, ODF, RTF en Word
- **Inhoud boven presentatie**: richt zich op documentstructuur en betekenis
- **Platformoverschrijdend**: werkt op elk besturingssysteem en met elke teksteditor
- **Uitbreidbaar**: uitgebreide functieset voor complexe documentvereisten
- **Versie 5**: volledig herschreven met verbeterde prestaties en betrouwbaarheid

## Filosofie en ontwerpdoelen [philosophy-and-design-goals]

MultiMarkdown volgt het principe dat **inhoud belangrijker is dan presentatie**. De nadruk ligt op het weergeven van de betekenis van documenten (dit is een lijst, dat is een tabel, enz.) in plaats van op het dicteren van lettertypen, kleuren of stijl.

Het doel is om bruikbaar te zijn voor 80% van de documenten die 80% van de mensen schrijven, waardoor het geschikt wordt voor romans, scripties, technische documentatie en de meeste andere geschreven inhoud.

## Belangrijkste functies en uitbreidingen [major-features-and-extensions]

### 1. **Metadata-ondersteuning** [1-metadata-support]

- Documentmetagegevens bovenaan bestanden
- Titel, auteur, datum en aangepaste variabelen
- Automatische opname in uitvoerheaders

```afwaardering
titel: Mijn document
auteur: John Doe
datum: 15-01-2024
gewoonte: waarde

<!-- Een lege regel beëindigt de metadata -->
Inhoud
---

# Documentinhoud
```

**Metagegevensvariabelen**

- Gebruik metadatawaarden in het hele document
- Syntaxis: `[%variable_name]`
- Automatische vervanging tijdens verwerking

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Geavanceerde tabellen** [2-advanced-tables]

**Volledige tafelondersteuning**

- Kopteksten, uitlijning en complexe tabelstructuren
- Ondersteuning voor tabelbijschriften en labels
- Kruisverwijzingen naar tabellen

```afwaardering
| Kop 1 | Kop 2 | Kop 3 |
| :------- | :------: | -------: |
| Links |  Centrum |    Juist |
| Uitgelijnd | Uitgelijnd |  Uitgelijnd |

Tabel: Voorbeeldtabel met uitlijning
```

**Tabelfuncties**

- Kolomuitlijning met dubbele punten
- Tabelbijschriften en labels
- Kruisverwijzingen met `[Table 1]`
- Ondersteuning voor complexe tabelstructuren

### 3. **Voetnoten en citaten** [3-footnotes-and-citations]

**Voetnoten**

- Voetnoten in referentiestijl met `[^1]` syntaxis
- Automatische nummering en koppeling
- Ondersteuning voor inline voetnoten

```afwaardering
Dit is een zin met een voetnoot[^1].

[^1]: This is the footnote content.
```

**Citatieondersteuning**

- Academische citatieopmaak
- Bibliografie generatie
- Ondersteuning voor verschillende citatiestijlen

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

En hieronder volgt de beschrijving van de referentie die moet worden
gebruikt in de bibliografie.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

In de uitvoer van HTML zijn citaten niet te onderscheiden van voetnoten.

U bent niet verplicht een locator te gebruiken (bijv. p. 23), en er zijn geen speciale regels over wat u als locator kunt gebruiken als u ervoor kiest er een te gebruiken. Als je de locator liever weglaat, gebruik dan gewoon een lege reeks vierkante haken vóór de bronvermelding:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

Er zijn geen regels voor het citatiesleutelformaat dat u gebruikt (bijvoorbeeld Doe:2006), maar het moet worden voorafgegaan door een `#`, net zoals voetnoten `^` gebruiken.

### 4. **Kruisverwijzingen** [4-cross-references]

**Automatische kruisverwijzingen**

- Link naar kopjes, tabellen, figuren en vergelijkingen
- Automatische labelgeneratie
- Ondersteuning voor aangepaste labels

```afwaardering
Zie [Tabel 1] voor details.
Raadpleeg [Paragraaf 2.1] voor meer informatie.

## Sectie 2.1
```

**Referentietypen**

- Koppen: `[Section 1]`, `[Heading Title]`
- Tabellen: `[Table 1]`, `[Table: Caption]`
- Cijfers: `[Figure 1]`, `[Figure: Caption]`
- Vergelijkingen: `[Equation 1]`

### 5. **Definitielijsten** [5-definition-lists]

**Termdefinitieparen**

- Ondersteuning voor definitielijsten
- Meerdere definities per term
- Juiste HTML `<dl>` uitvoer

```afwaardering
Termijn 1
: Definitie 1

Termijn 2
: Definitie 2a
: Definitie 2b
```

### 6. **Omheinde codeblokken** [6-fenced-code-blocks]

**Taalspecifieke codeblokken**

- Drievoudige backticks met taalspecificatie
- Ondersteuning voor syntaxisaccentuering
- Automatische taaldetectie

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Codeblokfuncties**

- Taalspecificatie voor syntaxisaccentuering
- Ondersteuning voor veel programmeertalen
- Juiste HTML `<pre><code>` uitvoer

### 7. **Wiskundige ondersteuning** [7-math-support]

**Wiskundige uitdrukkingen**

- LaTeX-compatibele wiskundige syntaxis
- Zowel inline als blokwiskundeondersteuning
- Integratie met LaTeX-uitvoer

```afwaardering
Inline wiskunde: $E = mc^2$

Blok wiskunde:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Afbeelding- en linkkenmerken** [8-image-and-link-attributes]

**Verbeterde links en afbeeldingen**

- Ondersteuning voor HTML-attributen
- Breedte, hoogte, alternatieve tekst en meer
- Betere integratie met uitvoerformaten

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusie** [9-transclusion]

**Bestandsopname**

- Neem andere bestanden op in documenten
- Ondersteuning voor geneste omvat
- Automatische padresolutie

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Transclusiefuncties**

- Bestand opnemen met `<!--MKPH0-->`
- Ondersteuning voor relatieve en absolute paden
- Geneste transclusieondersteuning
- Manifestgeneratie voor opgenomen bestanden

### 10. **CriticMarkup Integratie** [10-criticmarkup-integration]

**Wijzigingen bijhouden**

- Ondersteuning voor CriticMarkup syntaxis
- Houd toevoegingen, verwijderingen en opmerkingen bij
- Samenwerkingsfuncties voor bewerken

```afwaardering
Dit is {>>verwijderde tekst<<} en dit is {++toegevoegde tekst++}.

Dit is een {~~verwijdering~>vervanging~~}.
```

### 11. **Inhoudsopgave** [11-table-of-contents]

**Automatische TOC-generatie**

- `<!--MKPH0-->` tijdelijke aanduiding voor inhoudsopgave
- Hiërarchische structuur op basis van kopjes
- Customiseerbare TOC-generatie

```afwaardering
# Documenttitel

{{TOC}}

## Sectie 1
Inhoud hier...

## Sectie 2
Meer inhoud...
```

### 12. **Afkortingen** [12-abbreviations]

**HTML-Stijlafkortingen**

- Definieer afkortingen voor automatische uitbreiding
- Ondersteuning voor tooltips en uitleg
- Juiste HTML `<abbr>` uitvoer

```afwaardering
*[HTML]: HyperText-opmaaktaal
*[CSS]: trapsgewijze stijlbladen

Dit maakt gebruik van HTML en CSS.
```

## MultiMarkdown v5 versus andere Markdown smaken [multimarkdown-v5-vs-other-markdown-flavors]

| Kenmerk | MultiMarkdown v5 | CommonMark (GFM) | Korting | Kramdown | Standaard |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tabellen | Ja | Nee | Ja | Ja | Nee |
| Doorhalen | Ja | Nee | Ja | Nee | Nee |
| Takenlijsten | Ja | Nee | Ja | Nee | Nee |
| Omheinde code | Ja | Ja | Ja | Ja | Nee |
| Wiskunde | Ja | Nee | Nee | Ja | Nee |
| Voetnoten | Ja | Nee | Ja | Ja | Nee |
| Definitielijsten | Ja | Nee | Nee | Ja | Nee |
| Afkortingen | Ja | Nee | Nee | Ja | Nee |
| Attributenlijsten | Ja | Nee | Nee | Ja | Nee |
| Extensies | Ja | Nee | Beperkt | Ja | Nee |
| Typografie | Ja | Nee | Basis | Ja | Nee |
| Automatische koppelingen | Ja | Nee | Ja | Nee | Nee |
| Kruisverwijzingen | Ja | Nee | Nee | Nee | Nee |
| Citaties | Ja | Nee | Nee | Nee | Nee |
| Transclusie | Ja | Nee | Nee | Nee | Nee |
| Metagegevens | Ja | Nee | Nee | Nee | Nee |

## Belangrijkste voordelen van MultiMarkdown v5 [key-advantages-of-multimarkdown-v5]

1. **Documentgericht**: ontworpen voor volledige documenten, niet alleen voor webfragmenten
2. **Uitvoer in meerdere formaten**: converteren naar HTML, LaTeX, PDF, ODF, RTF en Word
3. **Academische ondersteuning**: citaten, voetnoten en kruisverwijzingen
4. **Professionele functies**: Metagegevens, transclusie en geavanceerde opmaak
5. **Platformoverschrijdend**: Werkt op elk besturingssysteem
6. **Toekomstbestendig**: het formaat voor platte tekst garandeert compatibiliteit op de lange termijn
7. **Uitbreidbaar**: uitgebreide functieset voor complexe documentvereisten

## Veelvoorkomende gebruiksscenario's [common-use-cases]

**Academisch schrijven**

- Scripties, proefschriften en onderzoekspapers
- Citatiebeheer en genereren van bibliografieën
- Kruisverwijzingen en voetnoten

**Technische documentatie**

- API-documentatie en gebruikershandleidingen
- Technische specificaties en handleidingen
- Codedocumentatie met syntaxisaccentuering

**Publiceren**

- Boeken, artikelen en rapporten
- Uitvoer in meerdere formaten voor verschillende platforms
- Professionele documentopmaak

**Contentbeheer**

- Documentatiewebsites
- Kennisbanken en wiki's
- Gezamenlijke schrijfprojecten

## Beste praktijken [best-practices]

1. **Gebruik metadata**: gebruik YAML voorwerk voor documentinformatie
2. **Structuur met koppen**: gebruik de juiste kophiërarchie voor het genereren van inhoudsopgaven
3. **Maak gebruik van kruisverwijzingen**: gebruik automatische koppelingen voor betere navigatie
4. **Organiseren met Transclusie**: Verdeel grote documenten in beheersbare bestanden
5. **Testuitvoer**: Controleer de opmaak in verschillende uitvoerformaten
6. **Gebruik citaten**: implementeer de juiste academische citatiepraktijken

## Migratie van andere Markdown smaken [migration-from-other-markdown-flavors]

De meeste standaard Markdown werkt zonder wijzigingen met MultiMarkdown. Om te profiteren van de MMD-functies:

1. **Metagegevens toevoegen**: Voeg YAML voorwerk toe voor documentinformatie
2. **Gebruik kruisverwijzingen**: vervang handmatige koppelingen door automatische verwijzingen
3. **Citaten implementeren**: voeg de juiste academische citatieopmaak toe
4. **Structuur met transclusie**: Verdeel grote documenten in kleinere bestanden
5. **Maak gebruik van tabellen**: gebruik geavanceerde tabelfuncties voor gegevenspresentatie

## Bronnen [resources]

- [MultiMarkdown User's Guide](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [MultiMarkdown Syntax Guide](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [MultiMarkdown GitHub Repository](https://github.com/fletcher/MultiMarkdown-5)
- [MultiMarkdown Documentation](https://fletcher.github.io/MultiMarkdown-5/)

---

*Deze documentatie heeft betrekking op MultiMarkdown v5.1.0. Raadpleeg voor de meest actuele informatie altijd de officiële MultiMarkdown documentatie op [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*