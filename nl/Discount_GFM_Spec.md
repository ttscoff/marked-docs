# <%= @title %>

Bekijk de [Markdown Dingus](x-marked-3://dingus?processor=discount) om te experimenteren met de Kortingsprocessor.

## Wat is Korting GFM? [what-is-discount-gfm]

Discount GFM (GitHub Flavoured Markdown) is een op C gebaseerde Markdown processor die de uitgebreide Markdown syntaxis van GitHub implementeert. Het is gebaseerd op de originele Discount-bibliotheek, maar uitgebreid met GitHub-specifieke functies zoals tabellen, takenlijsten, doorgehaalde tekst en automatische URL-koppeling.

## Belangrijkste kenmerken [key-characteristics]

- **C-gebaseerde prestaties**: snelle, native C-implementatie voor optimale prestaties
- **GitHub Compatibiliteit**: implementeert de Markdown extensies van GitHub voor maximale compatibiliteit
- **Lichtgewicht**: minimale afhankelijkheden en kleine footprint
- **Uitbreidbaar**: ondersteunt verschillende Markdown extensies en aangepaste opties
- **HTML5 Ondersteuning**: Genereert moderne HTML5 uitvoer met de juiste semantische opmaak

## Grote verschillen met standaard Markdown [major-differences-from-standard-markdown]

### 1. **GitHub Gearomatiseerde Markdown Extensies** [1-github-flavored-markdown-extensions]

**Tabellen**

- Volledige ondersteuning voor tabellen in GitHub-stijl met uitlijningsopties
- Kopteksten, scheidingstekens en gegevensrijen met de juiste HTML tabelstructuur
- Kolomuitlijning met dubbele punten (`:`) in scheidingsrijen

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Takenlijsten**

- Ondersteuning voor selectievakjes in GitHub-stijl in lijsten
- Interactieve selectievakjes (weergegeven als HTML invoerelementen)
- Zowel gecontroleerde als niet-gecontroleerde staten worden ondersteund

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Doorgehaalde tekst**

- Tekst tussen dubbele tildes (`~~`) wordt doorgehaald
- Gebruikt HTML `<del>` tags voor semantische opmaak
- Ondersteunt meerdere tildes voor nadruk

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Verbeterde ondersteuning voor codeblokken** [2-enhanced-code-block-support]

**Omheinde codeblokken**

- Drievoudige backticks (```` ``` ````) voor codeblokken
- Taalspecificatie voor syntaxisaccentuering
- Geen inspringing vereist (in tegenstelling tot standaard Markdown)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatische taaldetectie**

- Ondersteuning voor veel programmeertalen
- Juiste syntaxisaccentuering indien ondersteund
- Terugval op platte tekst voor niet-ondersteunde talen

### 3. **Automatische URL-koppeling** [3-automatic-url-linking]

**URL automatisch koppelen**

- Automatische conversie van URL's naar klikbare links
- Ondersteuning voor http-, https- en ftp-protocollen
- E-mailadressen worden automatisch omgezet naar mailto-links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Smart Link-detectie**

- Herkent URL's zonder expliciete opmaak
- Verwerkt verschillende URL-formaten en protocollen
- Configureerbare linkveiligheidsopties

### 4. **Geavanceerde lijstfuncties** [4-advanced-list-features]

**Alfabetische lijsten**

- Geordende lijsten met alfabetische markeringen (a, b, c, etc.)
- Automatische voortgang door het alfabet
- Juiste HTML `<ol type="a">` uitvoer

```markdown
a. First item
b. Second item
c. Third item
```

**Verbeterde lijstverwerking**

- Betere afhandeling van geneste lijsten
- Verbeterde afstand en inkeping
- Ondersteuning voor gemengde lijsttypen

### 5. **Ondersteuning voor voetnoten** [5-footnotes-support]

**Referentievoetnoten**

- Automatische voetnootnummering
- Referentielinks met `[^1]` syntaxis
- Voetnootdefinities aan het einde van het document

```afwaardering
Dit is een zin met een voetnoot[^1].

[^1]: This is the footnote content.
```

**Automatische voetnootverwerking**

- Genereert de juiste HTML voetnootstructuur
- Koppelingen tussen referenties en definities
- Opeenvolgende nummering in het hele document

### 6. **HTML Integratie** [6-html-integration]

**HTML5 Ondersteuning**

- Volledige HTML5 tagherkenning
- Correcte generatie van semantische markeringen
- Moderne HTML structuur en attributen

**Ruwe HTML blokken**

- Ondersteuning voor HTML binnen Markdown
- Goede ontsnapping en ontsmetting
- Integratie met Markdown syntaxis

### 7. **Verbeterde nadrukregels** [7-enhanced-emphasis-rules]

**Ontspannen nadruk**

- Enkele onderstrepingstekens (`_`) creëren geen nadruk in het midden van woorden
- Beter voor het documenteren van code en technische inhoud
- Voorkomt ongewenste nadruk in identifiers

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Meerdere nadrukniveaus**

- Ondersteuning voor vet, cursief en gecombineerde nadruk
- Consistent met standaard Markdown nadrukregels
- Juiste HTML uitvoer met `<strong>` en `<em>` tags

### 8. **Inhoudsopgave genereren** [8-table-of-contents-generation]

**Automatische inhoudsopgave**

- Genereert een inhoudsopgave op basis van koppen
- Hiërarchische structuur op basis van kopniveaus
- Configureerbare opties voor het genereren van TOC's

**Kop-ID genereren**

- Automatische ID-generatie voor rubrieken
- Ankerlinks voor eenvoudige navigatie
- Consistente ID-opmaak

## Korting op GFM versus andere Markdown smaken [discount-gfm-vs-other-markdown-flavors]

| Kenmerk | Korting | CommonMark (GFM) | Kramdown | MeerdereMarkdown | Standaard |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tabellen | Ja | Nee | Ja | Ja | Nee |
| Doorhalen | Ja | Nee | Nee | Ja | Nee |
| Takenlijsten | Ja | Nee | Nee | Ja | Nee |
| Omheinde code | Ja | Ja | Ja | Ja | Nee |
| Wiskunde | Nee | Nee | Ja | Ja | Nee |
| Voetnoten | Ja | Nee | Ja | Ja | Nee |
| Definitielijsten | Nee | Nee | Ja | Ja | Nee |
| Afkortingen | Nee | Nee | Ja | Nee | Nee |
| Attributenlijsten | Nee | Nee | Ja | Nee | Nee |
| Extensies | Beperkt | Nee | Ja | Ja | Nee |
| Typografie | Basis | Nee | Ja | Nee | Nee |
| Automatische koppelingen | Ja | Nee | Nee | Nee | Nee |
| Alfabetische lijsten | Ja | Nee | Nee | Nee | Nee |

## Belangrijkste voordelen van korting GFM [key-advantages-of-discount-gfm]

1. **GitHub Compatibiliteit**: perfect voor inhoud die moet werken op GitHub
2. **Prestaties**: Snelle C-gebaseerde implementatie
3. **Eenvoud**: gericht op de kernfuncties van GitHub zonder complexiteit
4. **Betrouwbaarheid**: Stabiele, goed geteste implementatie
5. **Naleving van normen**: volgt de Markdown-specificatie van GitHub
6. **Lichtgewicht**: minimaal gebruik van bronnen en afhankelijkheden

## Veelvoorkomende gebruiksscenario's [common-use-cases]

**GitHub Documentatie**

- README-bestanden en projectdocumentatie
- GitHub Pagina's en wiki's
- Beschrijvingen van problemen en pull-aanvragen

**Technisch schrijven**

- Codedocumentatie en tutorials
- API-documentatie
- Technische specificaties

**Contentbeheer**

- Blogberichten en artikelen
- Documentatiewebsites
- Kennisbanken

**Gezamenlijk bewerken**

- Teamdocumentatie
- Projectplanningsdocumenten
- Notulen en notulen van vergaderingen

## Configuratieopties [configuration-options]

Korting GFM ondersteunt verschillende configuratiemogelijkheden:

- **Automatisch koppelen**: automatische URL-detectie in-/uitschakelen
- **Voetnoten**: controle over de verwerking van voetnoten
- **Inhoudsopgave**: instellingen voor het genereren van TOC's
- **HTML Veiligheid**: Linkvalidatie en opschoning
- **Strikte modus**: verbeterde parseerregels
- **Smart Quotes**: automatische offerteconversie

## Implementatiedetails [implementation-details]

**Parser-opties**

- `kGHMarkdownAutoLink`: Automatische URL-koppeling inschakelen
- `kGHMarkdownFootnotes`: voetnootverwerking inschakelen
- `kGHMarkdownTOC`: Generatie van inhoudsopgave inschakelen
- `kGHMarkdownSafeLinks`: Beperk koppelingen naar veilige protocollen
- `kGHMarkdownNoHTMLTags`: Schakel HTML tagverwerking uit

**Uitvoerfuncties**

- HTML5 semantische opmaak
- Juiste kophiërarchie
- Toegankelijke tafelstructuren
- Schone, geldige HTML uitvoer

## Beste praktijken [best-practices]

1. **Gebruik tabellen spaarzaam**: Tabellen zijn krachtig, maar kunnen complex zijn om te onderhouden
2. **Maak gebruik van takenlijsten**: ideaal voor projectbeheer en documentatie
3. **Gebruik Autolinks**: laat de processor de URL-conversie automatisch afhandelen
4. **Structuur met koppen**: gebruik de juiste kophiërarchie voor een betere inhoudsopgave
5. **Test op GitHub**: Controleer de compatibiliteit met de weergave van GitHub

## Migratie van standaard Markdown [migration-from-standard-markdown]

De meeste standaard Markdown werkt zonder wijzigingen met Discount GFM. Om te profiteren van de GFM-functies:

1. **Tabellen toevoegen**: gegevens converteren naar tabelindeling in GitHub-stijl
2. **Gebruik takenlijsten**: vervang opsommingstekens door selectievakjes waar nodig
3. **Doorhalen inschakelen**: gebruik `~~text~~` voor doorgestreepte inhoud
4. **Maak gebruik van automatische links**: verwijder handmatige linkmarkeringen voor eenvoudige URL's
5. **Structuurkoppen**: Zorg voor de juiste kophiërarchie voor het genereren van inhoudsopgaven

## Bronnen [resources]

- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [Discount Library Documentation](https://www.pell.portland.or.us/~orc/Code/discount/)
- [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

*Deze documentatie heeft betrekking op Korting GFM zoals geïmplementeerd in Marked. Raadpleeg voor de meest actuele informatie altijd de officiële GitHub Flavoured Markdown specificatie.*