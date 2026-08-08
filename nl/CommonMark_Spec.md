# <%= @title %>

Bekijk de [Markdown Dingus](x-marked-3://dingus?processor=commonmark) om te experimenteren met de CommonMark (GFM)-processor.


## Wat is CommonMark? [what-is-commonmark]

CommonMark is een sterk gespecificeerde, zeer compatibele implementatie van Markdown. Het is gemaakt om de dubbelzinnigheden en inconsistenties in de oorspronkelijke Markdown-specificatie van John Gruber aan te pakken, wat leidde tot uiteenlopende implementaties op verschillende platforms en tools.

## Waarom CommonMark bestaat [why-commonmark-exists]

De oorspronkelijke Markdown-specificatie van John Gruber was op veel gebieden opzettelijk dubbelzinnig, wat leidde tot verschillende interpretaties door verschillende implementaties. Dit zorgde voor problemen waarbij hetzelfde Markdown document anders zou worden weergegeven op verschillende platforms (GitHub, StackOverflow, Reddit, enz.).

CommonMark biedt:

- **Ondubbelzinnige specificaties** voor alle Markdown syntaxis
- **Uitgebreid testpakket** om consistent gedrag te garanderen
- **Duidelijke prioriteitsregels** voor conflicterende syntaxis
- **Gedetailleerd parseeralgoritme** dat consistent kan worden geïmplementeerd

## Belangrijkste verschillen met standaard Markdown [key-differences-from-standard-markdown]

### 1. **Strengere parseerregels** [1-stricter-parsing-rules]

CommonMark dwingt consistenter parseergedrag af:

**Lege regels vóór blokelementen**

- CommonMark vereist lege regels vóór koppen, blokcitaten en lijsten
- Standaard Markdown staat dit vaak toe zonder witregels

```markdown
Text
# Heading
```

*CommonMark: vereist een lege regel vóór de kop*

*Standaard Markdown: Vaak toegestaan ​​zonder lege regel*

### 2. **Lijstitem parseren** [2-list-item-parsing]

**Inspringvereisten**

- CommonMark heeft specifieke regels voor het inspringen van lijstitems
- Sublijsten moeten consistent worden ingesprongen (meestal vier spaties)
- Standaard Markdown implementaties variëren hierop

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Lijstvervolg**

- CommonMark heeft duidelijke regels voor wanneer lijstitems 'los' versus 'strak' zijn
- Losse lijsten verpakken items in `<p>` tags, strakke lijsten niet

### 3. **Afhandeling van codeblokken** [3-code-block-handling]

**Omheinde codeblokken**

- CommonMark standaardiseert de syntaxis van omheinde codeblokken met backticks of tildes
- Vereist consistente inkepingen en sluitingsmarkeringen


    ```language
    code here
    ```


**Ingesprongen codeblokken**

- CommonMark vereist lege regels vóór ingesprongen codeblokken
- Standaard Markdown staat ze vaak toe zonder witregels

### 4. **Link en beeldverwerking** [4-link-and-image-processing]

**Referentielinkvoorrang**

- CommonMark heeft duidelijke regels waarvoor referentiedefinitie voorrang heeft
- Meerdere definities voor dezelfde referentie worden consistent verwerkt

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Link-parseervolgorde**

- CommonMark verwerkt links vóór nadruk
- Dit heeft invloed op de manier waarop geneste syntaxis wordt geïnterpreteerd

### 5. **Nadruk en sterke nadruk** [5-emphasis-and-strong-emphasis]

**Geneste nadrukregels**

- CommonMark heeft specifieke algoritmen voor het verwerken van geneste `*` en `_` markeringen
- Voorkomt dubbelzinnige ontleding van complexe nadrukpatronen

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Scheidingstekenverwerking**

- CommonMark gebruikt een "delimiter stack"-algoritme voor consistente parsering van accenten
- Standaard Markdown implementaties variëren in hun aanpak

### 6. **HTML Blokverwerking** [6-html-block-processing]

**HTML Blokkeerdetectie**

- CommonMark heeft 7 verschillende soorten HTML blokken met specifieke regels
- Elk type stelt andere eisen aan start-/eindvoorwaarden

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Afhandeling van lijnonderbrekingen** [7-line-break-handling]

**Harde lijnonderbrekingen**

- CommonMark vereist twee spaties aan het einde van de regel voor harde onderbrekingen
- Enkele regeleinden worden zachte regeleinden (genegeerd in HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Entiteits- en karakterreferenties** [8-entity-and-character-references]

**Numerieke karakterreferenties**

- CommonMark ondersteunt zowel decimale als hexadecimale numerieke referenties
- Standaard Markdown ondersteuning varieert

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## CommonMark-parseeralgoritme [commonmark-parsing-algorithm]

CommonMark gebruikt een parseerbenadering in twee fasen:

### Fase 1: Blokstructuur [phase-1-block-structure]

1. **Lijnverwerking**: elke regel wordt geanalyseerd op markeringen op blokniveau
2. **Containerblokken**: Blockquotes, lijsten en andere containers worden geïdentificeerd
3. **Bladblokken**: Koppen, codeblokken en paragrafen worden verwerkt
4. **Referentielinks**: linkdefinities worden verzameld voor later gebruik

### Fase 2: Inline-structuur [phase-2-inline-structure]

1. **Inline verwerking**: Tekst binnen blokken wordt geparseerd voor inline elementen
2. **Emphasis Parsing**: Gebruikt scheidingstekenstapelalgoritme voor consistente nadruk
3. **Linkresolutie**: referentielinks worden opgelost met behulp van verzamelde definities
4. **Entiteitsverwerking**: tekenreferenties worden geconverteerd naar daadwerkelijke tekens

## Voordelen van CommonMark [benefits-of-commonmark]

1. **Voorspelbaar gedrag**: Dezelfde invoer levert altijd dezelfde uitvoer op
2. **Platformoverschrijdende compatibiliteit**: Werkt consistent met verschillende tools
3. **Uitgebreid testen**: Uitgebreid testpakket garandeert betrouwbaarheid
4. **Duidelijke documentatie**: Gedetailleerde specificatie elimineert giswerk
5. **Toekomstbestendig**: goed gedefinieerde uitbreidingspunten voor nieuwe functies

## Implementatieopmerkingen [implementation-notes]

CommonMark is ontworpen om:

- **Voldoet aan de specificaties**: volgt exact de officiële CommonMark-specificaties
- **Testgestuurd**: voldoet aan de officiële CommonMark-testsuite
- **Uitbreidbaar**: kan worden uitgebreid met extra functies terwijl de compatibiliteit behouden blijft
- **Snel**: geoptimaliseerde parseeralgoritmen voor prestaties

## Bronnen [resources]

- [CommonMark Specification](https://spec.commonmark.org/0.31.2/)
- [CommonMark Test Suite](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Online testtool
- [CommonMark Discussion Forum](https://talk.commonmark.org/)

---

*Deze documentatie heeft betrekking op CommonMark 0.31.2 (28-01-2024). Raadpleeg voor de meest actuele informatie altijd de officiële specificatie.*