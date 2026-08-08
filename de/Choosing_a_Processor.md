# <%= @title %>

Marked kann dieselbe Datei mit mehreren integrierten Markdown-Prozessoren in der Vorschau anzeigen. Jeder wägt anders ab zwischen **Schreibworkflow** (Bücher, Blogs, GitHub-READMEs) und **Ausgabekontrolle** (IDs, Klassen, Metadaten). Den Standard wählen Sie unter {% prefspane Processor %}; den Prozessor können Sie auch pro Dokument überschreiben.

Diese Seite fasst zusammen, wie sich die vier Hauptprozessoren unterscheiden. Ausführliche Syntaxdetails finden Sie auf den Referenzseiten unter **Hilfe → Markdown-Referenz** (z. B. [MultiMarkdown-v5-Spezifikation](MultiMarkdown_v5_Spec.html), [Kramdown-Spezifikation](Kramdown_Spec.html), [CommonMark-Spezifikation](CommonMark_Spec.html), [Discount-GFM-Spezifikation](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5) [multimarkdown-v5]

**Am besten geeignet für:** Lange Prosa, akademisches oder technisches Schreiben und alles, was auf **Metadaten**, **Zitate** und **MultiMarkdown-spezifische** Funktionen baut.

Marked wird mit **MultiMarkdown 5** geliefert (die Upstream-Dokumentation finden Sie im [MultiMarkdown-Benutzerhandbuch](https://fletcher.github.io/MultiMarkdown-5/)).

### Stärken [strengths]

- **Erzählende und referenzlastige Dokumente:** Fußnoten, Bibliografie/Zitate und Tabellen sind erstklassig unterstützt.
- **Metadaten:** Standard-MultiMarkdown-Metadatenblöcke (`Key: Value`-Header) plus **Transklusion** und weitere MMD-Annehmlichkeiten aus dem v5-Handbuch.
- **Metadaten-Ersetzung:** Schlüssel aus den Metadaten lassen sich per `[%key]`-Ersetzung in den Textkörper einfügen, sodass Titel, Autorenangaben und ähnliche Werte mit dem Header synchron bleiben.
- **Tabellen, Bilder und Querverweise:** abgestimmt auf die für MultiMarkdown 5 dokumentierten Funktionen.

### IDs und manuelle Überschriften [ids-and-manual-headings]

- Überschriften-IDs werden so **normalisiert**, dass tendenziell **klein geschriebene, verkettete** Slugs entstehen (keine Leerzeichen – die Wörter laufen zusammen).
- Für **manuelle Überschriften-IDs** verwendet MultiMarkdown die Form `## Headline Text [my-id]` (die Kennung in eckigen Klammern nach dem Überschriftentext).

### Wann etwas anderes besser passt [when-to-pick-something-else]

Wenn Sie Aufgabenlisten im **GitHub-Stil** und das exakte Verhalten von GitHubs aktuellem Parser brauchen, nehmen Sie **CommonMark (GFM)**. Wenn Sie **feingranulare HTML-Klassen/-IDs** auf beliebigen Elementen brauchen, ziehen Sie **Kramdown** in Betracht.

---

## Kramdown [kramdown]

**Am besten geeignet für:** Dokumente, bei denen Sie **präzise Kontrolle über die HTML-Ausgabe** möchten – eigene **Klassen**, **IDs** und Attribute, damit Ihr CSS gezielt bestimmte Blöcke und Bereiche ansprechen kann.

Maßgeblich ist die [kramdown-Syntaxreferenz](https://kramdown.gettalong.org/syntax.html).

### Stärken [strengths-2]

- **Weitgehend kompatibel** mit MultiMarkdown-Gewohnheiten für den Markdown-Alltag, ergänzt um eigene Erweiterungen.
- **Inline- und Block-Attributlisten (IALs):** Hängen Sie `{: #id .class key="value"}` an Absätze, Überschriften, Codeblöcke, Links, Bilder und mehr an – ideal für Jekyll-artige Websites und eigene Stylesheets.
- **Überschriften-IDs:** kramdown normalisiert automatisch erzeugte Überschriften-IDs zu **klein geschriebenen, per Bindestrich getrennten** Wörtern (z. B. `my-section-title`). Für **manuelle IDs** nutzen Sie die Form `{#id}` nach dem Überschriftentext – z. B. Setext: `My Section {#my-section}` und darunter die Unterstreichung, oder ATX: `# My Section {#my-section}` (genaue Platzierung und IAL-Regeln in kramdowns [Überschriften](https://kramdown.gettalong.org/syntax.html#headers)).
- **Definitionslisten, Fußnoten, intelligente Typografie, Mathematikblöcke:** umfangreicher Funktionsumfang für Publishing-Pipelines, die mehr als „einfaches“ Markdown brauchen.

### Wann etwas anderes besser passt [when-to-pick-something-else-2]

Wenn Sie auf die **MultiMarkdown-eigene** Metadaten-Ersetzung (`[%key]`) oder MMD-spezifische Zitier-Workflows angewiesen sind, ist **MultiMarkdown** womöglich die bessere Wahl. Für **README- und Repo-Dokumente**, die online mit GitHub übereinstimmen müssen, liegt **CommonMark (GFM)** meist näher.

---

## CommonMark (GitHub Flavored Markdown / cmark-gfm) [commonmark-github-flavored-markdown-cmark-gfm]

**Am besten geeignet für:** **README-Dateien**, **Issue-/PR-Beschreibungen** und **Projektdokumentation**, die möglichst genau dem **aktuellen Markdown-Verhalten von GitHub** entsprechen sollen.

Marked nutzt eine **GFM**-orientierte Engine (cmark-gfm). Die formale Spezifikation ist die [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), die auf [CommonMark](https://commonmark.org/) aufbaut.

### Stärken [strengths-3]

- **Höchste Übereinstimmung mit GitHub:** Tabellen, Durchstreichungen, Aufgabenlisten-Einträge, abgegrenzte Codeblöcke mit Sprach-Tags und Autolinks verhalten sich wie das moderne GitHub-Rendering.
- **Eindeutiges Parsen:** CommonMark definiert Block-/Inline-Vorrang und Listenregeln präzise – in manchen Randfällen strenger als das „klassische“ Verhalten von Markdown.pl, dafür **vorhersehbarer**, sobald man die Regeln kennt.
- **Gut für umgebrochenen Text:** Absatz- und Listenregeln funktionieren gut mit hart umgebrochenem Text (siehe die Abschnitte der Spezifikation zu Lazy Continuations und Listen).

### Überschriften-IDs [header-ids]

Automatisch erzeugte Überschriftenanker sind in der Regel **klein geschrieben und per Bindestrich getrennt**, passend zum üblichen GitHub-Slugging.

### Wann etwas anderes besser passt [when-to-pick-something-else-3]

GFM bildet weder **MultiMarkdown-Metadaten** noch **kramdown-IALs** oder **MMD-Zitier-Workflows** nach. Für Bücher, Dissertationen oder umfangreiche Metadaten nehmen Sie je nach Bedarf **MultiMarkdown** oder **Kramdown**.

---

## Discount [discount]

**Am besten geeignet für:** einen schnellen Workflow nah am **ursprünglichen Markdown**, ohne das vollständige CommonMark-Regelwerk. Discount ist ein **schneller, C-basierter** Prozessor, der sich an **klassischem Markdown** und einem **älteren, an GitHub angelehnten** Funktionsumfang orientiert – praktisch, wenn Sie zusätzlich Tabellen, Fußnoten und verwandte Erweiterungen möchten.

Projektseite: [Discount](https://www.pell.portland.or.us/~orc/Code/discount/).

### Stärken [strengths-4]

- **Tabellen im Stil von PHP Markdown Extra** und viele Erweiterungen (Fußnoten, abgegrenzter Code, wenn aktiviert, usw. – was Marked davon aktiviert, steht in Marks [Discount-GFM-Spezifikation](Discount_GFM_Spec.html)).
- **Optionale „GitHub“-Extras** im Upstream-Discount (z. B. Checkbox-Listen, wenn mit den richtigen Flags gebaut); die ausgelieferte Kombination dokumentiert Marked auf der Discount-Spezifikationsseite.
- **Typografie im SmartyPants-Stil** und weitere Annehmlichkeiten von der Discount-Website (Typografiefunktionen bieten allerdings alle enthaltenen Prozessoren).
- Philosophisch nah an **John Grubers Markdown** plus praktischer Erweiterungen, statt an der vollständigen CommonMark-Testsuite.

### Wann etwas anderes besser passt [when-to-pick-something-else-4]

Für **pixelgenaue Übereinstimmung mit dem heutigen github.com** nehmen Sie **CommonMark (GFM)**. Für **MultiMarkdown-Metadaten und Zitate** nehmen Sie **MultiMarkdown**.

---

## Schneller Vergleich [quick-comparison]

| Kriterium | MultiMarkdown | Kramdown | CommonMark (GFM) | Discount |
|--------|---------------|--------|------------------|----------|
| **Hauptzweck** | Prosa, Aufsätze, Bücher | Gestyltes HTML, Jekyll-artige Websites | READMEs, GitHub-artige Dokumente | Klassisches MD + Erweiterungen |
| **Zitate / MMD-Metadaten** | Stark | Über andere Syntax | Nein | Nein |
| **Stil manueller Überschriften-IDs** | `## Title [id]` | `## Title {: #id }` (IAL) | Spec-/GitHub-Slug-Regeln | Keine |
| **Automatische Überschriften-IDs** | klein, verkettet | klein, per Bindestrich | klein, per Bindestrich | klein, per Bindestrich |
| **Zusätzliche Attribute (Klassen/IDs)** | begrenzte MMD-Mechanismen | **IALs** – sehr stark | begrenzt | begrenzt |

---

## Siehe auch [see-also]

- [Einstellungen: Prozessor](Settings_Processor.html) – Standardprozessor und zugehörige Optionen
- [Markdown Dingus](Markdown_Dingus.html) – Prozessoren in Marked nebeneinander ausprobieren
- [Benutzerdefinierter Prozessor](Custom_Processor.html) – bei Bedarf Ihre eigene Toolchain einbinden
