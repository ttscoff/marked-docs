# <%= @title %>

Probieren Sie [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) aus, um mit dem MultiMarkdown-Prozessor zu experimentieren.

## Was ist MultiMarkdown? [what-is-multimarkdown]

MultiMarkdown ist ein erweiterter Markdown-Prozessor für vollständige Dokumente statt nur für Webseitenfragmente. Er ergänzt die ursprüngliche Markdown-Syntax um Funktionen zur Konvertierung in mehrere Ausgabeformate, darunter HTML, LaTeX, PDF, ODF und Microsoft Word-Dokumente.

## Hauptmerkmale [key-characteristics]

- **Dokumentorientiert**: Für vollständige Dokumente entwickelt, nicht nur für Webausschnitte
- **Multiformat-Ausgabe**: Konvertiert in HTML, LaTeX, PDF, ODF, RTF und Word
- **Inhalt vor Darstellung**: Konzentriert sich auf Struktur und Bedeutung des Dokuments
- **Plattformübergreifend**: Funktioniert auf jedem Betriebssystem mit jedem Texteditor
- **Erweiterbar**: Umfangreicher Funktionsumfang für komplexe Dokumentanforderungen
- **Version 5**: Vollständige Neufassung mit verbesserter Leistung und Zuverlässigkeit

## Philosophie und Designziele [philosophy-and-design-goals]

MultiMarkdown folgt dem Prinzip, dass **Inhalt wichtiger ist als Präsentation**. Der Schwerpunkt liegt auf der Darstellung der Bedeutung von Dokumenten (das ist eine Liste, das ist eine Tabelle usw.) und nicht auf der Vorgabe von Schriftarten, Farben oder Stilen.

Ziel ist es, für 80 % der Dokumente verwendbar zu sein, die 80 % der Menschen schreiben, sodass es für Romane, Abschlussarbeiten, technische Dokumentationen und die meisten anderen schriftlichen Inhalte geeignet ist.

## Hauptfunktionen und Erweiterungen [major-features-and-extensions]

### 1. **Metadaten-Unterstützung** [1-metadata-support]

- Dokumentmetadaten oben in den Dateien
- Titel, Autor, Datum und benutzerdefinierte Variablen
- Automatische Einbindung in Ausgabe-Kopfzeilen

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content [document-content]
```

**Metadatenvariablen**

- Verwenden Sie im gesamten Dokument Metadatenwerte
- Syntax: `[%variable_name]`
- Automatische Ersetzung während der Verarbeitung

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Erweiterte Tabellen** [2-advanced-tables]

**Vollständige Tabellenunterstützung**

- Kopfzeilen, Ausrichtung und komplexe Tabellenstrukturen
- Unterstützung für Tabellenüberschriften und Beschriftungen
- Querverweise auf Tabellen

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Tabellenfunktionen**

- Spaltenausrichtung mit Doppelpunkten
- Tabellenüberschriften und Beschriftungen
- Querverweise mit `[Table 1]`
- Unterstützung komplexer Tabellenstrukturen

### 3. **Fußnoten und Zitate** [3-footnotes-and-citations]

**Fußnoten**

- Fußnoten im Referenzstil mit der Syntax `[^1]`
- Automatische Nummerierung und Verlinkung
- Unterstützung für Inline-Fußnoten

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Zitierunterstützung**

- Formatierung wissenschaftlicher Zitate
- Erstellung von Bibliografien
- Unterstützung verschiedener Zitierstile

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

Anschließend folgt die Beschreibung der Referenz, die in der Bibliografie verwendet wird.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

In der HTML-Ausgabe sind Zitate nicht von Fußnoten zu unterscheiden.

Sie müssen keine Fundstelle angeben (z. B. S. 23). Falls Sie eine verwenden, gelten keine besonderen Regeln für deren Inhalt. Um die Fundstelle wegzulassen, verwenden Sie vor dem Zitat einfach ein leeres Paar eckiger Klammern:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

Für das Format des Zitierschlüssels (z. B. Doe:2006) gelten keine Regeln. Ihm muss jedoch ein `#` vorangestellt werden, so wie Fußnoten ein `^` verwenden.

### 4. **Querverweise** [4-cross-references]

**Automatische Querverweise**

- Verlinkung mit Überschriften, Tabellen, Abbildungen und Gleichungen
- Automatische Erzeugung von Bezeichnern
- Unterstützung für benutzerdefinierte Bezeichner

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1 [section-2-1]
```

**Referenztypen**

- Überschriften: `[Section 1]`, `[Heading Title]`
- Tabellen: `[Table 1]`, `[Table: Caption]`
- Abbildungen: `[Figure 1]`, `[Figure: Caption]`
- Gleichungen: `[Equation 1]`

### 5. **Definitionslisten** [5-definition-lists]

**Begriffsdefinitionspaare**

- Unterstützung für Definitionslisten
- Mehrere Definitionen pro Begriff
- Korrekte HTML-Ausgabe mit `<dl>`

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Abgegrenzte Codeblöcke** [6-fenced-code-blocks]

**Sprachspezifische Codeblöcke**

- Dreifache Backticks mit Sprachangabe
- Unterstützung für Syntaxhervorhebung
- Automatische Spracherkennung

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Codeblockfunktionen**

- Sprachangabe für die Syntaxhervorhebung
- Unterstützung für viele Programmiersprachen
- Korrekte HTML-Ausgabe mit `<pre><code>`

### 7. **Mathe-Unterstützung** [7-math-support]

**Mathematische Ausdrücke**

- LaTeX-kompatible mathematische Syntax
- Unterstützt Mathematik sowohl inline als auch in Blöcken
- Integration mit LaTeX-Ausgabe

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Bild- und Linkattribute** [8-image-and-link-attributes]

**Erweiterte Links und Bilder**

- Unterstützung für HTML-Attribute
- Breite, Höhe, Alternativtext und mehr
- Bessere Integration mit Ausgabeformaten

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transklusion** [9-transclusion]

**Dateieinbindung**

- Andere Dateien in Dokumente einfügen
- Unterstützung für verschachtelte Includes
- Automatische Pfadauflösung

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Transklusionsfunktionen**

- Dateieinbindung mit `{{filename}}`
- Unterstützung für relative und absolute Pfade
- Unterstützung für verschachtelte Transklusion
- Manifestgenerierung für enthaltene Dateien

### 10. **CriticMarkup-Integration** [10-criticmarkup-integration]

**Änderungsverfolgung**

- Unterstützung für die CriticMarkup-Syntax
- Verfolgt Hinzufügungen, Löschungen und Kommentare
- Funktionen zur kollaborativen Bearbeitung

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Inhaltsverzeichnis** [11-table-of-contents]

**Automatische TOC-Generierung**

- Platzhalter `{{TOC}}` für das Inhaltsverzeichnis
- Hierarchische Struktur basierend auf Überschriften
- Anpassbare Erzeugung des Inhaltsverzeichnisses

```markdown
# Document Title [document-title]

{{TOC}}

## Section 1 [section-1]
Content here...

## Section 2 [section-2]
More content...
```

### 12. **Abkürzungen** [12-abbreviations]

**HTML-Stil-Abkürzungen**

- Abkürzungen zur automatischen Erweiterung definieren
- Unterstützung für Tooltips und Erklärungen
- Korrekte HTML-Ausgabe mit `<abbr>`

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 im Vergleich zu anderen Markdown-Varianten [multimarkdown-v5-vs-other-markdown-flavors]

| Funktion | MultiMarkdown v5 | CommonMark (GFM) | Discount | Kramdown | Standard |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tabellen | Ja | Nein | Ja | Ja | Nein |
| Durchgestrichen | Ja | Nein | Ja | Nein | Nein |
| Aufgabenlisten | Ja | Nein | Ja | Nein | Nein |
| Abgegrenzte Codeblöcke | Ja | Ja | Ja | Ja | Nein |
| Mathematik | Ja | Nein | Nein | Ja | Nein |
| Fußnoten | Ja | Nein | Ja | Ja | Nein |
| Definitionslisten | Ja | Nein | Nein | Ja | Nein |
| Abkürzungen | Ja | Nein | Nein | Ja | Nein |
| Attributlisten | Ja | Nein | Nein | Ja | Nein |
| Erweiterungen | Ja | Nein | Begrenzt | Ja | Nein |
| Typografie | Ja | Nein | Grundlegend | Ja | Nein |
| Autolinks | Ja | Nein | Ja | Nein | Nein |
| Querverweise | Ja | Nein | Nein | Nein | Nein |
| Zitate | Ja | Nein | Nein | Nein | Nein |
| Transklusion | Ja | Nein | Nein | Nein | Nein |
| Metadaten | Ja | Nein | Nein | Nein | Nein |

## Hauptvorteile von MultiMarkdown v5 [key-advantages-of-multimarkdown-v5]

1. **Dokumentorientiert**: Entwickelt für vollständige Dokumente, nicht nur für Webausschnitte
2. **Multiformat-Ausgabe**: Konvertieren in HTML, LaTeX, PDF, ODF, RTF und Word
3. **Akademische Unterstützung**: Zitate, Fußnoten und Querverweise
4. **Professionelle Funktionen**: Metadaten, Transklusion und erweiterte Formatierung
5. **Plattformübergreifend**: Funktioniert auf jedem Betriebssystem
6. **Zukunftssicher**: Das reine Textformat gewährleistet langfristige Kompatibilität
7. **Erweiterbar**: Umfangreicher Funktionsumfang für komplexe Dokumentanforderungen

## Häufige Anwendungsfälle [common-use-cases]

**Akademisches Schreiben**

- Abschlussarbeiten, Dissertationen und Forschungsarbeiten
- Zitierverwaltung und Erstellung von Bibliografien
- Querverweise und Fußnoten

**Technische Dokumentation**

- API-Dokumentation und Benutzerhandbücher
- Technische Spezifikationen und Handbücher
- Codedokumentation mit Syntaxhervorhebung

**Veröffentlichung**

- Bücher, Artikel und Berichte
- Multiformat-Ausgabe für verschiedene Plattformen
- Professionelle Dokumentformatierung

**Inhaltsverwaltung**

- Dokumentationswebsites
- Wissensdatenbanken und Wikis
- Gemeinsame Schreibprojekte

## Bewährte Vorgehensweisen [best-practices]

1. **Metadaten verwenden**: Nutzen Sie den YAML-Metadatenblock für Dokumentinformationen
2. **Mit Überschriften strukturieren**: Verwenden Sie die richtige Überschriftenhierarchie für die Erzeugung des Inhaltsverzeichnisses
3. **Querverweise nutzen**: Verwenden Sie automatische Verlinkungen für eine bessere Navigation
4. **Mit Transklusion organisieren**: Teilen Sie große Dokumente in überschaubare Dateien auf
5. **Ausgabe testen**: Überprüfen Sie die Formatierung in verschiedenen Ausgabeformaten
6. **Zitate verwenden**: Implementieren Sie ordnungsgemäße akademische Zitierpraktiken

## Migration von anderen Markdown-Varianten [migration-from-other-markdown-flavors]

Die meisten Dokumente in Standard-Markdown funktionieren ohne Änderungen mit MultiMarkdown. So nutzen Sie die Funktionen von MMD:

1. **Metadaten hinzufügen**: Fügen Sie einen YAML-Metadatenblock mit Dokumentinformationen hinzu
2. **Querverweise verwenden**: Ersetzen Sie manuelle Links durch automatische Verweise
3. **Zitate implementieren**: Fügen Sie die richtige Formatierung für akademische Zitate hinzu
4. **Struktur mit Transklusion**: Teilen Sie große Dokumente in kleinere Dateien auf
5. **Tabellen verwenden**: Nutzen Sie erweiterte Tabellenfunktionen zur Darstellung von Daten

## Ressourcen [resources]

- [MultiMarkdown-Benutzerhandbuch](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [MultiMarkdown-Syntaxleitfaden](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [MultiMarkdown-Repository auf GitHub](https://github.com/fletcher/MultiMarkdown-5)
- [MultiMarkdown-Dokumentation](https://fletcher.github.io/MultiMarkdown-5/)

---

*Diese Dokumentation behandelt MultiMarkdown v5.1.0. Aktuelle Informationen finden Sie in der offiziellen MultiMarkdown-Dokumentation unter [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*
