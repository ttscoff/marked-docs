# <%= @title %>

Bekijk de [Markdown Dingus](x-marked-3://dingus?processor=kramdown) om te experimenteren met de Kramdown-processor.

## Wat is Kramdown? [what-is-kramdown]

Kramdown is een snelle, pure Ruby Markdown-superset-converter die de originele Markdown-syntaxis uitbreidt met functies die te vinden zijn in andere implementaties zoals Maruku, PHP Markdown Extra en Pandoc. Het biedt een strikte syntaxis met duidelijke regels, terwijl de compatibiliteit met de meeste Markdown documenten behouden blijft.

## Belangrijkste kenmerken [key-characteristics]

- **Snelle en pure Ruby**: volledig geschreven in Ruby voor prestaties en draagbaarheid
- **Strikte syntaxis**: biedt duidelijke regels en duidelijke specificaties
- **Verbeterde functies**: bevat veel extensies die niet voorkomen in standaard Markdown
- **Jekyll-integratie**: standaard Markdown processor voor de Jekyll statische sitegenerator
- **Uitgebreid**: ondersteunt elementen op zowel blok- als spanniveau met uitgebreide aanpassingen

## Grote verschillen met standaard Markdown [major-differences-from-standard-markdown]

### 1. **Verbeterde elementen op blokniveau** [1-enhanced-block-level-elements]

**Definitielijsten**

- Kramdown ondersteunt definitielijsten (niet in standaard Markdown)
- Gebruikt `:` om termen van definities te scheiden

```afwaardering
Termijn 1
: Definitie 1

Termijn 2
: Definitie 2a
: Definitie 2b
```

**Tabellen**

- Volledige tabelondersteuning met kopteksten, uitlijning en opmaak
- Uitgebreider dan de standaard Markdown tabelsyntaxis

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Wiskundeblokken**

- Ondersteuning voor wiskundige uitdrukkingen met behulp van LaTeX-syntaxis
- Zowel inline als blokwiskundeondersteuning

```afwaardering
Inline wiskunde: $E = mc^2$

Blok wiskunde:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Geavanceerde tekstopmaak** [2-advanced-text-markup]

**Voetnoten**

- Volledige voetnootondersteuning met automatische nummering
- Voetnoten in referentiestijl met `[^1]` syntaxis

```afwaardering
Dit is een zin met een voetnoot[^1].

[^1]: This is the footnote content.
```

**Afkortingen**

- Ondersteuning voor afkortingen in HTML-stijl
- Automatische uitbreiding van gedefinieerde afkortingen

```afwaardering
*[HTML]: HyperText-opmaaktaal
*[CSS]: trapsgewijze stijlbladen

Dit maakt gebruik van HTML en CSS.
```

**Typografische symbolen**

- Automatische conversie van veelgebruikte typografische karakters
- Slimme aanhalingstekens, em-streepjes, ellipsen, enz.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Kenmerklijsten en extensies** [3-attribute-lists-and-extensions]

**Attributenlijstdefinities (ALD's)**

- Definieer herbruikbare attributensets
- Ondersteuning voor ID's, klassen en aangepaste attributen

```afwaardering
{:ref-name: #myid .my-class title="Mijn titel"}

Een paragraaf met attributen.
{: #para-één.highlight}
```

**Inline kenmerklijsten (IAL's)**

- Voeg attributen toe aan specifieke elementen
- Ondersteuning op zowel blokniveau als spanniveau

```markdown
This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Extensies**

- Custom uitbreidingssysteem voor extra functionaliteit
- Ingebouwde extensies voor opmerkingen en opties

```afwaardering
{::commentaar}
Deze tekst wordt door kramdown volledig genegeerd.
{:/opmerking}

{::options key="val" /}
```

### 4. **Verbeterde ondersteuning voor codeblokken** [4-enhanced-code-block-support]

**Taalspecificatie**

- Automatische syntaxisaccentuering voor omheinde codeblokken
- Ondersteuning voor veel programmeertalen

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**Standaardcodeblokken**

- Verbeterde verwerking van ingesprongen codeblokken
- Betere integratie met andere blokelementen

### 5. **Strengere parseerregels** [5-stricter-parsing-rules]

**Lijnwikkeling**

- Ondersteuning voor hard-wrapped inhoud (luie syntaxis)
- Duidelijke regels voor wanneer lijnomloop is toegestaan
- Niet aanbevolen voor leesbaarheid, maar ondersteund voor compatibiliteit

**Tabbladverwerking**

- Er wordt uitgegaan van tabstops bij veelvouden van vier
- Tabs zijn alleen toegestaan aan het begin van regels voor inspringing
- Mag niet worden voorafgegaan door spaties

**Blokgrenzen**

- Duidelijke regels voor wanneer elementen moeten beginnen/eindigen op blokgrenzen
- Consistent gedrag bij verschillende elementtypen

### 6. **Geavanceerde ondersteuning voor links en afbeeldingen** [6-advanced-link-and-image-support]

**Automatische koppelingen**

- Verbeterde automatische linkdetectie
- Betere verwerking van URL's en e-mailadressen

**Referentielinks**

- Verbeterde verwerking van referentielinks
- Betere conflictoplossing voor meerdere definities

**Afbeeldingskenmerken**

- Ondersteuning voor afbeeldingskenmerken via IAL's
- Breedte, hoogte, alternatieve tekst en andere HTML-attributen

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **HTML Integratie** [7-html-integration]

**HTML Blokken**

- Betere afhandeling van HTML binnen Markdown
- Ondersteuning voor HTML attributen en verwerking
- Flexibeler dan standaard Markdown HTML afhandeling

**HTML Spanwijdten**

- Inline HTML met attribuutondersteuning
- Betere integratie met de syntaxis Markdown

### 8. **Wiskundige uitdrukkingen** [8-mathematical-expressions]

**Inline wiskunde**

- `$...$` syntaxis voor inline wiskundige uitdrukkingen
- LaTeX-compatibele syntaxis

**Blok Wiskunde**

- `$$...$$` syntaxis voor blokwiskundige uitdrukkingen
- Ondersteuning voor complexe vergelijkingen en formules

## Kramdown versus andere Markdown smaken [kramdown-vs-other-markdown-flavors]

| Kenmerk | Kramdown | CommonMark (GFM) | GitHub Gearomatiseerd | MeerdereMarkdown | Standaard |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Doorhalen | Nee | Ja | Nee | Nee | Nee |
| Takenlijsten | Nee | Nee | Ja | Ja | Nee |
| Omheinde code | Ja | Ja | Ja | Ja | Nee |
| Wiskunde | Ja | Nee | Ja | Ja | Nee |
| Voetnoten | Ja | Ja | Ja | Ja | Nee |
| Definitielijsten | Ja | Nee | Nee | Ja | Nee |
| Afkortingen | Ja | Nee | Nee | Nee | Nee |
| Attributenlijsten | Ja | Nee | Nee | Nee | Nee |
| Typografie | Ja | Nee | Nee | Ja | Nee |

## Belangrijkste voordelen van Kramdown [key-advantages-of-kramdown]

1. **Uitgebreide functieset**: bevat veel extensies die niet in andere implementaties voorkomen
2. **Jekyll-integratie**: Naadloze integratie met de statische sitegenerator van Jekyll
3. **Ruby Ecosystem**: Pure Ruby-implementatie met goede Ruby-toolingondersteuning
4. **Uitbreidbaarheid**: Custom uitbreidingssysteem voor extra functionaliteit
5. **Kenmerkondersteuning**: uitgebreid attributensysteem voor HTML uitvoeraanpassing
6. **Wiskundige ondersteuning**: ingebouwde ondersteuning voor LaTeX-wiskundige uitdrukkingen
7. **Strikte parsering**: duidelijke, ondubbelzinnige parseringsregels

## Veelvoorkomende gebruiksscenario's [common-use-cases]

**Jekyll-sites**

- Standaardprocessor voor het genereren van statische sites door Jekyll
- Uitstekend geschikt voor documentatie- en blogsites

**Technische documentatie**

- Wiskundige ondersteuning voor wetenschappelijk en technisch schrijven
- Kenmerklijsten voor geavanceerde HTML aanpassingen

**Academisch schrijven**

- Voetnootondersteuning voor citaten en referenties
- Wiskundige uitdrukkingen voor formules en vergelijkingen

**Contentbeheer**

- Uitbreidingen voor aangepaste functionaliteit
- Attributenlijsten voor metadata en styling

## Bronnen [resources]

- [Kramdown Syntax Documentation](https://kramdown.gettalong.org/syntax.html)
- [Kramdown Converter Documentation](https://kramdown.gettalong.org/converter.html)
- [Jekyll Integration Guide](https://jekyllrb.com/docs/configuration/markdown/)
- [Kramdown GitHub Repository](https://github.com/gettalong/kramdown)

## Migratie van standaard Markdown [migration-from-standard-markdown]

De meeste standaard Markdown documenten werken zonder aanpassingen met Kramdown. Om te profiteren van de functies van Kramdown:

1. **Definitielijsten toevoegen**: converteer woordenlijsten en termenlijsten
2. **Gebruik attribuutlijsten**: voeg ID's, klassen en aangepaste attributen toe
3. **Voetnoten implementeren**: verwijzingen tussen haakjes converteren

## Beste praktijken [best-practices]

1. **Vermijd luie syntaxis**: vertrouw niet op hard-wrapping voor de leesbaarheid
2. **Gebruik attribuutlijsten**: maak gebruik van IAL's voor styling en metadata
3. **Consistente inspringing**: Gebruik waar mogelijk spaties in plaats van tabs

---

*Deze documentatie heeft betrekking op Kramdown 2.5.1. Raadpleeg voor de meest actuele informatie altijd de officiële documentatie op [kramdown.gettalong.org](https://kramdown.gettalong.org/).*