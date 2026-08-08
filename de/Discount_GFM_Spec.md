# <%= @title %>

Probieren Sie [Markdown Dingus](x-marked-3://dingus?processor=discount) aus, um mit dem Discount-Prozessor zu experimentieren.

## Was ist Discount-GFM? [what-is-discount-gfm]

Discount GFM (GitHub Flavored Markdown) ist ein C-basierter Markdown-Prozessor, der die erweiterte Markdown-Syntax von GitHub implementiert. Er basiert auf der ursprünglichen Discount-Bibliothek, wurde jedoch um GitHub-spezifische Funktionen wie Tabellen, Aufgabenlisten, durchgestrichenen Text und die automatische Verlinkung von URLs erweitert.

## Hauptmerkmale [key-characteristics]

- **C-basierte Leistung**: Schnelle, native C-Implementierung mit optimaler Leistung
- **GitHub-Kompatibilität**: Implementiert die Markdown-Erweiterungen von GitHub für maximale Kompatibilität
- **Leichtgewichtig**: Minimale Abhängigkeiten und geringer Platzbedarf
- **Erweiterbar**: Unterstützt verschiedene Markdown-Erweiterungen und benutzerdefinierte Optionen
- **HTML5-Unterstützung**: Erzeugt eine moderne HTML5-Ausgabe mit korrektem semantischem Markup

## Wesentliche Unterschiede zu Standard-Markdown [major-differences-from-standard-markdown]

### 1. **Erweiterungen von GitHub Flavored Markdown** [1-github-flavored-markdown-extensions]

**Tabellen**

- Volle Unterstützung für Tabellen im GitHub-Stil mit Ausrichtungsoptionen
- Kopfzeilen, Trennlinien und Datenzeilen mit korrekter HTML-Tabellenstruktur
- Spaltenausrichtung mithilfe von Doppelpunkten (`:`) in den Trennlinien

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Aufgabenlisten**

- Unterstützung für Kontrollkästchen im GitHub-Stil in Listen
- Interaktive Kontrollkästchen (gerendert als HTML-Eingabeelemente)
- Unterstützt sowohl markierte als auch nicht markierte Kontrollkästchen

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Durchgestrichener Text**

- In doppelte Tilden (`~~`) eingeschlossener Text wird durchgestrichen
- Verwendet HTML-Tags vom Typ `<del>` für semantisches Markup
- Unterstützt mehrere Tilden zur Hervorhebung

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Erweiterte Codeblock-Unterstützung** [2-enhanced-code-block-support]

**Abgegrenzte Codeblöcke**

- Dreifache Backticks (```` ``` ````) für Codeblöcke
- Sprachangabe für die Syntaxhervorhebung
- Keine Einrückung erforderlich (im Gegensatz zu Standard-Markdown)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatische Spracherkennung**

- Unterstützung für viele Programmiersprachen
- Korrekte Syntaxhervorhebung, sofern unterstützt
- Fallback auf Klartext für nicht unterstützte Sprachen

### 3. **Automatische URL-Verknüpfung** [3-automatic-url-linking]

**Automatische URL-Verlinkung**

- Automatische Umwandlung von URLs in anklickbare Links
- Unterstützung für die Protokolle http, https und ftp
- E-Mail-Adressen werden automatisch in `mailto:`-Links umgewandelt

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Intelligente Link-Erkennung**

- Erkennt URLs ohne explizites Markup
- Verarbeitet verschiedene URL-Formate und Protokolle
- Konfigurierbare Link-Sicherheitsoptionen

### 4. **Erweiterte Listenfunktionen** [4-advanced-list-features]

**Alphabetische Listen**

- Geordnete Listen mit alphabetischen Markierungen (a, b, c usw.)
- Automatische fortlaufende Nummerierung mit Buchstaben
- Korrekte HTML-Ausgabe mit `<ol type="a">`

```markdown
a. First item
b. Second item
c. Third item
```

**Erweiterte Listenverarbeitung**

- Bessere Handhabung verschachtelter Listen
- Verbesserte Abstände und Einrückungen
- Unterstützung für gemischte Listentypen

### 5. **Unterstützung für Fußnoten** [5-footnotes-support]

**Fußnoten im Referenzstil**

- Automatische Nummerierung der Fußnoten
- Referenzlinks mit der Syntax `[^1]`
- Fußnotendefinitionen am Ende des Dokuments

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Automatische Fußnotenverarbeitung**

- Erzeugt die korrekte HTML-Fußnotenstruktur
- Verknüpfungen zwischen Referenzen und Definitionen
- Fortlaufende Nummerierung im gesamten Dokument

### 6. **HTML-Integration** [6-html-integration]

**HTML5-Unterstützung**

- Vollständige HTML5-Tag-Erkennung
- Korrekte semantische Markup-Generierung
- Moderne HTML-Struktur und -Attribute

**Rohe HTML-Blöcke**

- Unterstützung für HTML innerhalb von Markdown
- Korrektes Maskieren und Bereinigen
- Integration mit der Markdown-Syntax

### 7. **Erweiterte Hervorhebungsregeln** [7-enhanced-emphasis-rules]

**Gelockerte Hervorhebung**

- Einzelne Unterstriche (`_`) erzeugen innerhalb von Wörtern keine Hervorhebung
- Besser für die Dokumentation von Code und technischen Inhalten geeignet
- Verhindert unerwünschte Hervorhebung in Bezeichnern

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Mehrere Hervorhebungsstufen**

- Unterstützung für Fett-, Kursiv- und kombinierte Hervorhebung
- Entspricht den standardmäßigen Markdown-Hervorhebungsregeln
- Korrekte HTML-Ausgabe mit den Tags `<strong>` und `<em>`

### 8. **Erstellung eines Inhaltsverzeichnisses** [8-table-of-contents-generation]

**Automatisches Inhaltsverzeichnis**

- Erzeugt ein Inhaltsverzeichnis aus Überschriften
- Hierarchische Struktur basierend auf Überschriftenebenen
- Konfigurierbare TOC-Generierungsoptionen

**Überschriften-ID-Generierung**

- Automatische ID-Generierung für Überschriften
- Ankerlinks für eine einfache Navigation
- Konsistente ID-Formatierung

## Discount GFM im Vergleich zu anderen Markdown-Varianten [discount-gfm-vs-other-markdown-flavors]

| Funktion | Discount | CommonMark (GFM) | Kramdown | MultiMarkdown | Standard |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tabellen | Ja | Nein | Ja | Ja | Nein |
| Durchgestrichen | Ja | Nein | Nein | Ja | Nein |
| Aufgabenlisten | Ja | Nein | Nein | Ja | Nein |
| Abgegrenzte Codeblöcke | Ja | Ja | Ja | Ja | Nein |
| Mathematik | Nein | Nein | Ja | Ja | Nein |
| Fußnoten | Ja | Nein | Ja | Ja | Nein |
| Definitionslisten | Nein | Nein | Ja | Ja | Nein |
| Abkürzungen | Nein | Nein | Ja | Nein | Nein |
| Attributlisten | Nein | Nein | Ja | Nein | Nein |
| Erweiterungen | Begrenzt | Nein | Ja | Ja | Nein |
| Typografie | Grundlegend | Nein | Ja | Nein | Nein |
| Autolinks | Ja | Nein | Nein | Nein | Nein |
| Alphabetische Listen | Ja | Nein | Nein | Nein | Nein |

## Hauptvorteile von Discount GFM [key-advantages-of-discount-gfm]

1. **GitHub-Kompatibilität**: Perfekt für Inhalte, die unter GitHub funktionieren müssen
2. **Leistung**: Schnelle C-basierte Implementierung
3. **Einfachheit**: Fokussiert auf Kernfunktionen ohne Komplexität
4. **Zuverlässigkeit**: Stabile, gut getestete Implementierung
5. **Standardkonformität**: Entspricht der Markdown-Spezifikation von GitHub
6. **Leichtgewichtig**: Minimaler Ressourcenverbrauch und minimale Abhängigkeiten

## Häufige Anwendungsfälle [common-use-cases]

**GitHub-Dokumentation**

- README-Dateien und Projektdokumentation
- GitHub-Seiten und -Wikis
- Issue- und Pull-Request-Beschreibungen

**Technisches Schreiben**

- Code-Dokumentation und Tutorials
- API-Dokumentation
- Technische Spezifikationen

**Inhaltsverwaltung**

- Blogbeiträge und Artikel
- Dokumentationswebsites
- Wissensdatenbanken

**Gemeinsame Bearbeitung**

- Teamdokumentation
- Projektplanungsunterlagen
- Besprechungsnotizen und Protokolle

## Konfigurationsoptionen [configuration-options]

Discount GFM unterstützt verschiedene Konfigurationsmöglichkeiten:

- **Automatische Verlinkung**: Automatische URL-Erkennung aktivieren/deaktivieren
- **Fußnoten**: Fußnotenverarbeitung steuern
- **Inhaltsverzeichnis**: Einstellungen für die TOC-Generierung
- **HTML-Sicherheit**: Links validieren und bereinigen
- **Strenger Modus**: Erweiterte Parsing-Regeln
- **Typografische Anführungszeichen**: Anführungszeichen automatisch umwandeln

## Implementierungsdetails [implementation-details]

**Parser-Optionen**

- `kGHMarkdownAutoLink`: Automatische URL-Verknüpfung aktivieren
- `kGHMarkdownFootnotes`: Fußnotenverarbeitung aktivieren
- `kGHMarkdownTOC`: Inhaltsverzeichnisgenerierung aktivieren
- `kGHMarkdownSafeLinks`: Links auf sichere Protokolle beschränken
- `kGHMarkdownNoHTMLTags`: HTML-Tag-Verarbeitung deaktivieren

**Ausgabefunktionen**

- Semantisches HTML5-Markup
- Richtige Überschriftenhierarchie
- Barrierefreie Tabellenstrukturen
- Saubere, gültige HTML-Ausgabe

## Bewährte Vorgehensweisen [best-practices]

1. **Verwenden Sie Tabellen sparsam**: Tabellen sind leistungsstark, können aber komplex in der Pflege sein
2. **Aufgabenlisten nutzen**: Ideal für Projektmanagement und Dokumentation
3. **Autolinks nutzen**: Lassen Sie den Prozessor die URL-Konvertierung automatisch durchführen
4. **Mit Überschriften strukturieren**: Verwenden Sie die richtige Überschriftenhierarchie, damit das Inhaltsverzeichnis besser erzeugt wird
5. **Auf GitHub testen**: Überprüfen Sie die Kompatibilität mit dem Rendering von GitHub

## Migration von Standard-Markdown [migration-from-standard-markdown]

Die meisten Dokumente in Standard-Markdown funktionieren ohne Änderungen mit Discount GFM. So nutzen Sie die GFM-Funktionen:

1. **Tabellen hinzufügen**: Konvertieren Sie Daten in das Tabellenformat von GitHub
2. **Aufgabenlisten verwenden**: Ersetzen Sie gegebenenfalls Aufzählungspunkte durch Kontrollkästchen
3. **Durchgestrichen aktivieren**: Verwenden Sie `~~text~~` für durchgestrichene Inhalte
4. **Autolinks nutzen**: Entfernen Sie das manuelle Link-Markup für einfache URLs
5. **Überschriften strukturieren**: Stellen Sie die richtige Überschriftenhierarchie für die Erzeugung des Inhaltsverzeichnisses sicher

## Ressourcen [resources]

- [Spezifikation von GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Dokumentation der Discount-Bibliothek](https://www.pell.portland.or.us/~orc/Code/discount/)
- [GitHub-Markdown-Leitfaden](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown-Kurzreferenz](https://www.markdownguide.org/cheat-sheet/)

---

*Diese Dokumentation behandelt Discount GFM in der von Marked implementierten Form. Die aktuellsten Informationen finden Sie in der offiziellen Spezifikation von GitHub Flavored Markdown.*
