# <%= @title %>

Probieren Sie [Markdown Dingus](x-marked-3://dingus?processor=kramdown) aus, um mit dem Kramdown-Prozessor zu experimentieren.

## Was ist Kramdown? [what-is-kramdown]

Kramdown ist ein schneller, vollständig in Ruby geschriebener Konverter für eine Obermenge von Markdown. Er erweitert die ursprüngliche Markdown-Syntax um Funktionen aus anderen Implementierungen wie Maruku, PHP Markdown Extra und Pandoc. Kramdown bietet eine strenge Syntax mit eindeutigen Regeln und bleibt zugleich mit den meisten Markdown-Dokumenten kompatibel.

## Hauptmerkmale [key-characteristics]

- **Schnell und vollständig in Ruby geschrieben**: Bietet hohe Leistung und Portabilität
- **Strenge Syntax**: Bietet eindeutige Regeln und klare Spezifikationen
- **Erweiterte Funktionen**: Enthält viele Erweiterungen, die nicht im Standard-Markdown enthalten sind
- **Jekyll-Integration**: Standardmäßiger Markdown-Prozessor des statischen Website-Generators Jekyll
- **Umfassend**: Unterstützt Elemente auf Block- und Inline-Ebene sowie weitreichende Anpassungen

## Wesentliche Unterschiede zu Standard-Markdown [major-differences-from-standard-markdown]

### 1. **Erweiterte Elemente auf Blockebene** [1-enhanced-block-level-elements]

**Definitionslisten**

- Kramdown unterstützt Definitionslisten (anders als Standard-Markdown)
- Verwendet `:`, um Begriffe von Definitionen zu trennen

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tabellen**

- Vollständige Tabellenunterstützung mit Kopfzeilen, Ausrichtung und Formatierung
- Umfassender als die grundlegende Markdown-Tabellensyntax

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Matheblöcke**

- Unterstützung für mathematische Ausdrücke mit LaTeX-Syntax
- Unterstützt Mathematik sowohl inline als auch in Blöcken

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Erweiterte Textmarkierung** [2-advanced-text-markup]

**Fußnoten**

- Vollständige Fußnotenunterstützung mit automatischer Nummerierung
- Fußnoten im Referenzstil mit der Syntax `[^1]`

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abkürzungen**

- Unterstützung für Abkürzungen im HTML-Stil
- Automatische Erweiterung definierter Abkürzungen

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Typografische Symbole**

- Automatische Konvertierung gängiger typografischer Zeichen
- Typografische Anführungszeichen, Gedankenstriche, Auslassungspunkte usw.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Attributlisten und Erweiterungen** [3-attribute-lists-and-extensions]

**Attributlistendefinitionen (ALDs)**

- Wiederverwendbare Attributsätze definieren
- Unterstützung für IDs, Klassen und benutzerdefinierte Attribute

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Inline-Attributlisten (IALs)**

- Attribute an bestimmte Elemente anfügen
- Unterstützung sowohl auf Block- als auch auf Span-Ebene

```markdown
This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Erweiterungen**

- Benutzerdefiniertes Erweiterungssystem für zusätzliche Funktionen
- Integrierte Erweiterungen für Kommentare und Optionen

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Erweiterte Codeblock-Unterstützung** [4-enhanced-code-block-support]

**Sprachspezifikation**

- Automatische Syntaxhervorhebung für abgegrenzte Codeblöcke
- Unterstützung für viele Programmiersprachen

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**Standard-Codeblöcke**

- Verbesserte Handhabung eingerückter Codeblöcke
- Bessere Integration mit anderen Blockelementen

### 5. **Strengere Parsing-Regeln** [5-stricter-parsing-rules]

**Zeilenumbruch**

- Unterstützung für hart umbrochene Inhalte („Lazy Syntax“)
- Klare Regeln dafür, wann Zeilenumbrüche zulässig sind
- Aus Gründen der Lesbarkeit nicht empfohlen, aber aus Kompatibilitätsgründen unterstützt

**Tab-Handhabung**

- Setzt Tabulatorstopps bei Vielfachen von vier voraus
- Tabulatoren sind zum Einrücken nur am Zeilenanfang zulässig
- Davor dürfen keine Leerzeichen stehen

**Blockgrenzen**

- Klare Regeln dafür, wann Elemente an Blockgrenzen beginnen/enden müssen
- Konsistentes Verhalten über verschiedene Elementtypen hinweg

### 6. **Erweiterte Link- und Bildunterstützung** [6-advanced-link-and-image-support]

**Automatische Links**

- Verbesserte automatische Linkerkennung
- Besserer Umgang mit URLs und E-Mail-Adressen

**Referenzlinks**

- Verbesserte Verarbeitung von Referenzlinks
- Bessere Konfliktlösung für mehrere Definitionen

**Bildattribute**

- Unterstützung für Bildattribute durch IALs
- Breite, Höhe, Alternativtext und andere HTML-Attribute

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **HTML-Integration** [7-html-integration]

**HTML-Blöcke**

- Bessere Handhabung von HTML innerhalb von Markdown
- Unterstützung für HTML-Attribute und -Verarbeitung
- Flexibler als die standardmäßige Verarbeitung von HTML in Markdown

**Inline-HTML**

- Inline-HTML mit Attributunterstützung
- Bessere Integration mit der Markdown-Syntax

### 8. **Mathematische Ausdrücke** [8-mathematical-expressions]

**Inline-Mathematik**

- Syntax `$...$` für eingebettete mathematische Ausdrücke
- LaTeX-kompatible Syntax

**Mathematische Blöcke**

- Syntax `$$...$$` für mathematische Ausdrücke in Blöcken
- Unterstützung für komplexe Gleichungen und Formeln

## Kramdown im Vergleich zu anderen Markdown-Varianten [kramdown-vs-other-markdown-flavors]

| Funktion | Kramdown | CommonMark (GFM) | GitHub Flavored Markdown | MultiMarkdown | Standard |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Durchgestrichen | Nein | Ja | Nein | Nein | Nein |
| Aufgabenlisten | Nein | Nein | Ja | Ja | Nein |
| Abgegrenzte Codeblöcke | Ja | Ja | Ja | Ja | Nein |
| Mathematik | Ja | Nein | Ja | Ja | Nein |
| Fußnoten | Ja | Ja | Ja | Ja | Nein |
| Definitionslisten | Ja | Nein | Nein | Ja | Nein |
| Abkürzungen | Ja | Nein | Nein | Nein | Nein |
| Attributlisten | Ja | Nein | Nein | Nein | Nein |
| Typografie | Ja | Nein | Nein | Ja | Nein |

## Hauptvorteile von Kramdown [key-advantages-of-kramdown]

1. **Umfassender Funktionsumfang**: Enthält viele Erweiterungen, die in anderen Implementierungen nicht zu finden sind
2. **Jekyll-Integration**: Nahtlose Integration mit dem statischen Site-Generator von Jekyll
3. **Ruby-Ökosystem**: Reine Ruby-Implementierung mit guter Unterstützung durch Ruby-Werkzeuge
4. **Erweiterbarkeit**: Benutzerdefiniertes Erweiterungssystem für zusätzliche Funktionen
5. **Attributunterstützung**: Umfangreiches Attributsystem für die HTML-Ausgabeanpassung
6. **Mathematische Unterstützung**: Integrierte Unterstützung für mathematische LaTeX-Ausdrücke
7. **Strenges Parsing**: Klare, eindeutige Parsing-Regeln

## Häufige Anwendungsfälle [common-use-cases]

**Jekyll-Sites**

- Standardprozessor für statische Websites mit Jekyll
- Hervorragend für Dokumentationen und Blogs geeignet

**Technische Dokumentation**

- Mathe-Unterstützung für wissenschaftliches und technisches Schreiben
- Attributlisten für erweiterte HTML-Anpassungen

**Akademisches Schreiben**

- Fußnotenunterstützung für Zitate und Referenzen
- Mathematische Ausdrücke für Formeln und Gleichungen

**Inhaltsverwaltung**

- Erweiterungen für benutzerdefinierte Funktionen
- Attributlisten für Metadaten und Stil

## Ressourcen [resources]

- [Kramdown-Syntaxdokumentation](https://kramdown.gettalong.org/syntax.html)
- [Kramdown-Konverterdokumentation](https://kramdown.gettalong.org/converter.html)
- [Jekyll-Integrationsleitfaden](https://jekyllrb.com/docs/configuration/markdown/)
- [Kramdown-Repository auf GitHub](https://github.com/gettalong/kramdown)

## Migration von Standard-Markdown [migration-from-standard-markdown]

Die meisten Standard-Markdown-Dokumente funktionieren mit Kramdown ohne Änderungen. So nutzen Sie die Funktionen von Kramdown:

1. **Definitionslisten hinzufügen**: Glossare und Begriffslisten umwandeln
2. **Attributlisten verwenden**: Fügen Sie IDs, Klassen und benutzerdefinierte Attribute hinzu
3. **Fußnoten implementieren**: Verweise in Klammern umwandeln

## Bewährte Vorgehensweisen [best-practices]

1. **„Lazy Syntax“ vermeiden**: Verlassen Sie sich zugunsten der Lesbarkeit nicht auf harte Zeilenumbrüche
2. **Attributlisten verwenden**: Nutzen Sie IALs für Stile und Metadaten
3. **Konsistente Einrückung**: Verwenden Sie nach Möglichkeit Leerzeichen anstelle von Tabulatoren

---

*Diese Dokumentation behandelt Kramdown 2.5.1. Aktuelle Informationen finden Sie in der offiziellen Dokumentation unter [kramdown.gettalong.org](https://kramdown.gettalong.org/).*
