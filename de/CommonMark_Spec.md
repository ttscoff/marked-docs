# <%= @title %>

Probieren Sie [Markdown Dingus](x-marked-3://dingus?processor=commonmark) aus, um mit dem CommonMark-Prozessor (GFM) zu experimentieren.


## Was ist CommonMark? [what-is-commonmark]

CommonMark ist eine genau spezifizierte, hochkompatible Implementierung von Markdown. Sie wurde entwickelt, um die Mehrdeutigkeiten und Inkonsistenzen in John Grubers ursprünglicher Markdown-Spezifikation zu beheben, die zu unterschiedlichen Implementierungen auf verschiedenen Plattformen und in verschiedenen Werkzeugen geführt hatten.

## Warum CommonMark existiert [why-commonmark-exists]

Die ursprüngliche Markdown-Spezifikation von John Gruber war in vielen Bereichen absichtlich mehrdeutig, sodass verschiedene Implementierungen sie unterschiedlich auslegten. Dadurch wurde dasselbe Markdown-Dokument auf verschiedenen Plattformen (GitHub, Stack Overflow, Reddit usw.) unterschiedlich gerendert.

CommonMark bietet:

- **Eindeutige Vorgaben** für die gesamte Markdown-Syntax
- **Umfassende Testsuite**, die konsistentes Verhalten gewährleistet
- **Klare Vorrangregeln** für widersprüchliche Syntax
- **Detaillierten Parsing-Algorithmus**, der sich konsistent implementieren lässt

## Hauptunterschiede zu Standard-Markdown [key-differences-from-standard-markdown]

### 1. **Strengere Parsing-Regeln** [1-stricter-parsing-rules]

CommonMark erzwingt ein konsistenteres Parsing-Verhalten:

**Leerzeilen vor Blockelementen**

- CommonMark erfordert Leerzeilen vor Überschriften, Blockzitaten und Listen
- Standard-Markdown erlaubt diese häufig ohne Leerzeilen

```markdown
Text
# Heading
```

*CommonMark: Erfordert eine Leerzeile vor der Überschrift*

*Standard-Markdown: oft ohne Leerzeile erlaubt*

### 2. **Analyse von Listenelementen** [2-list-item-parsing]

**Einrückungsanforderungen**

- CommonMark hat genaue Regeln für die Einrückung von Listenelementen
- Unterlisten müssen konsistent eingerückt werden (normalerweise 4 Leerzeichen).
- Standardimplementierungen von Markdown weichen hiervon ab

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Listenfortsetzung**

- CommonMark hat klare Regeln dafür, wann Listen „locker“ oder „kompakt“ sind
- Lockere Listen umschließen Elemente mit `<p>`-Tags, kompakte Listen nicht

### 3. **Codeblock-Handhabung** [3-code-block-handling]

**Abgegrenzte Codeblöcke**

- CommonMark standardisiert die Syntax abgegrenzter Codeblöcke mit Backticks oder Tilden
- Erfordert konsistente Einrückungs- und Schlussmarkierungen


    ```language
    code here
    ```


**Eingerückte Codeblöcke**

- CommonMark erfordert Leerzeilen vor eingerückten Codeblöcken
- Standard-Markdown erlaubt sie oft ohne Leerzeilen

### 4. **Link- und Bildverarbeitung** [4-link-and-image-processing]

**Vorrang des Referenzlinks**

- CommonMark hat klare Regeln, nach denen die Referenzdefinition Vorrang hat
- Mehrere Definitionen für dieselbe Referenz werden konsistent behandelt

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Link-Parsing-Reihenfolge**

- CommonMark verarbeitet Links vor der Hervorhebung
- Dies wirkt sich darauf aus, wie verschachtelte Syntax interpretiert wird

### 5. **Hervorhebung und starke Hervorhebung** [5-emphasis-and-strong-emphasis]

**Verschachtelte Hervorhebungsregeln**

- CommonMark verwendet spezielle Algorithmen für verschachtelte `*`- und `_`-Markierungen
- Verhindert mehrdeutiges Parsen komplexer Hervorhebungsmuster

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Trennzeichenverarbeitung**

- CommonMark verwendet einen „Trennzeichenstapel“-Algorithmus für eine konsistente Hervorhebungsanalyse
- Standardimplementierungen von Markdown unterscheiden sich in ihrem Ansatz

### 6. **Verarbeitung von HTML-Blöcken** [6-html-block-processing]

**Erkennung von HTML-Blöcken**

- CommonMark unterscheidet 7 Arten von HTML-Blöcken mit jeweils eigenen Regeln
- Jeder Typ hat unterschiedliche Anforderungen an die Start-/Endbedingungen

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Behandlung von Zeilenumbrüchen** [7-line-break-handling]

**Harte Zeilenumbrüche**

- CommonMark erfordert zwei Leerzeichen am Zeilenende für harte Umbrüche
- Einzelne Zeilenumbrüche werden zu weichen Umbrüchen (in HTML ignoriert)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Entitäts- und Zeichenreferenzen** [8-entity-and-character-references]

**Numerische Zeichenreferenzen**

- CommonMark unterstützt sowohl dezimale als auch hexadezimale numerische Referenzen
- Die Unterstützung in Standardimplementierungen von Markdown variiert

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## CommonMark-Parsing-Algorithmus [commonmark-parsing-algorithm]

CommonMark verwendet einen zweiphasigen Parsing-Ansatz:

### Phase 1: Blockstruktur [phase-1-block-structure]

1. **Zeilenverarbeitung**: Jede Zeile wird auf Markierungen auf Blockebene analysiert
2. **Containerblöcke**: Blockzitate, Listen und andere Container werden identifiziert
3. **Blattblöcke**: Überschriften, Codeblöcke und Absätze werden verarbeitet
4. **Referenzlinks**: Linkdefinitionen werden zur späteren Verwendung gesammelt

### Phase 2: Inline-Struktur [phase-2-inline-structure]

1. **Inline-Verarbeitung**: Text innerhalb von Blöcken wird auf Inline-Elemente analysiert
2. **Hervorhebungsanalyse**: Verwendet den Trennzeichenstapel-Algorithmus für eine konsistente Hervorhebung
3. **Linkauflösung**: Referenzlinks werden anhand gesammelter Definitionen aufgelöst
4. **Entitätsverarbeitung**: Zeichenreferenzen werden in tatsächliche Zeichen umgewandelt

## Vorteile von CommonMark [benefits-of-commonmark]

1. **Vorhersehbares Verhalten**: Dieselbe Eingabe erzeugt immer dieselbe Ausgabe
2. **Plattformübergreifende Kompatibilität**: Funktioniert in verschiedenen Werkzeugen konsistent
3. **Umfassende Tests**: Umfangreiche Testsuite sorgt für Zuverlässigkeit
4. **Klare Dokumentation**: Detaillierte Spezifikationen beseitigen Unklarheiten
5. **Zukunftssicher**: Klar definierte Erweiterungspunkte für neue Funktionen

## Implementierungshinweise [implementation-notes]

CommonMark ist wie folgt konzipiert:

- **Spezifikationskonform**: Entspricht genau der offiziellen CommonMark-Spezifikation
- **Testgesteuert**: Besteht die offizielle CommonMark-Testsuite
- **Erweiterbar**: Kann unter Beibehaltung der Kompatibilität um zusätzliche Funktionen erweitert werden
- **Schnell**: Optimierte Parsing-Algorithmen sorgen für hohe Leistung

## Ressourcen [resources]

- [CommonMark-Spezifikation](https://spec.commonmark.org/0.31.2/)
- [CommonMark-Testsuite](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) – Online-Testtool
- [CommonMark-Diskussionsforum](https://talk.commonmark.org/)

---

*Diese Dokumentation behandelt CommonMark 0.31.2 (28. Januar 2024). Die aktuellsten Informationen finden Sie in der offiziellen Spezifikation.*
