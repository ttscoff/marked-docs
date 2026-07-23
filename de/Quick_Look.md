# <%= @title %>

**Marked Quick Look** ist eine eigene App aus dem Mac App Store, die eine Quick-Look-Vorschau-Erweiterung für Markdown- und Klartextdateien hinzufügt. Drücken Sie im Finder die Leertaste (oder nutzen Sie Quick Look überall, wo macOS es unterstützt), um eine gestaltete HTML-Vorschau statt des rohen Quelltexts zu sehen.

Marked Quick Look ist **nicht in Marked 3 enthalten**. Es ist ein separater Kauf (**9,99 $** im Mac App Store). <!-- MAS link: add App Store URL here when available -->

I> Marked Quick Look und Marked 3 sind unabhängige Produkte. Der Kauf von Marked installiert die Quick-Look-Erweiterung nicht, und der Kauf von Marked Quick Look enthält keine Marked-Lizenz. Die Vorschau bietet eine optionale Schaltfläche **In Marked öffnen**, sofern Marked installiert ist.

## Was Sie erhalten [what-you-get]

Marked Quick Look registriert eine **Quick-Look-Vorschau-Erweiterung**, die `.md`-, `.markdown`-, `.mmd`- und viele Klartextdateien mit demselben optischen Feinschliff rendert, für den Marked bekannt ist:

- **Apex-Verarbeitung** – angetrieben von [Apex](https://github.com/ApexMarkdown/apex), einem quelloffenen Markdown-Prozessor, der CommonMark, GitHub Flavored Markdown, MultiMarkdown, Kramdown und einen **Unified**-Modus unterstützt, der Funktionen mehrerer Varianten kombiniert
- **Marked-Vorschaustile** – neun integrierte Designs (GitHub als Standard) plus Import von eigenem CSS
- **Syntaxhervorhebung**, **MathJax** und **Mermaid**-Diagramme (mitgelieferte Skripte; keine Internetverbindung nötig)
- **CriticMarkup** in der Markup-Ansicht
- **In Marked öffnen** – von Quick Look zur vollständigen Marked-Vorschau springen, wenn Marked installiert ist

W> Quick-Look-Vorschauen sind schreibgeschützt. Eingebundene Dateien (`<<[file]`, `{{file}}` und ähnliche Syntax) werden in Quick Look **nicht** aufgelöst. Sie erscheinen als hervorgehobene Platzhalter (`Included file: path`), damit Sie sehen, wo Inhalt eingefügt würde. Öffnen Sie das Dokument in Marked, um mehrteilige Dokumente vollständig zu rendern.

## Installation [installation]

1. Installieren Sie **Marked Quick Look** aus dem Mac App Store.
2. **Starten Sie die App einmal** aus `/Applications`. Damit wird die Quick-Look-Erweiterung bei macOS registriert.
3. Drücken Sie im Finder die **Leertaste** auf einer Markdown-Datei, um sie in der Vorschau zu sehen.

Die Container-App enthält ein **Einstellungsfenster** ({% kbd cmd %},{% kbd , %}), in dem Sie den Apex-Prozessormodus, den Vorschaustil, das Design der Syntaxhervorhebung sowie Schalter für MathJax und Mermaid wählen.

## Apex und Markdown-Varianten [apex-and-markdown-flavors]

Marked Quick Look verwendet für alles Rendern [Apex](https://github.com/ApexMarkdown/apex). Apex wird als eigenständiger Prozessor entwickelt und ist außerdem in Marked 3 eingebettet.

Wählen Sie in den Einstellungen einen **Apex-Modus** passend zu Ihrem Schreibstil:

| Modus | Am besten für |
| --- | --- |
| **Unified** (Standard) | gemischte Markdown-Funktionen über Varianten hinweg |
| **CommonMark** | striktes CommonMark |
| **GFM** | GitHub Flavored Markdown |
| **MultiMarkdown** | Metadaten, Transklusion, Fußnoten |
| **Kramdown** | Erweiterungen im Kramdown-Stil |

Der Unified-Modus ist für die meisten Dokumente die beste Voreinstellung. Wechseln Sie den Modus, wenn eine Datei für einen bestimmten Prozessor geschrieben wurde und etwas unerwartet gerendert wird.

## In Marked öffnen [open-in-marked]

Ist Marked 3 installiert, kann die Quick-Look-Vorschau eine Schaltfläche **In Marked öffnen** in der Symbolleiste anzeigen. Klicken Sie darauf, um die Datei an Marked zu übergeben – für Live-Vorschau, Export, Korrekturlesen und die vollständige Auflösung eingebundener Dateien.

Ist Marked nicht installiert, erscheint die Schaltfläche deaktiviert.

## Quick-Look-Konflikte beheben [troubleshooting-quick-look-conflicts]

macOS erlaubt mehreren Apps, Quick-Look-Vorschau-Erweiterungen für Markdown zu registrieren. Nur eine Erweiterung bearbeitet jede Vorschau, und **das Plugin einer anderen App kann Vorrang** vor Marked Quick Look haben.

### Erkennen, welche Erweiterung aktiv ist [how-to-tell-which-extension-is-active]

Vorschauen von Marked Quick Look enthalten eine **In Marked öffnen**-Symbolleiste, sofern diese Option aktiviert ist. Sehen Sie ein anderes Layout, rohen Quelltext in Festbreitenschrift oder das Aussehen einer anderen App, gewinnt vermutlich ein anderer Quick-Look-Handler.

### Vorrang von Marked Quick Look wiederherstellen [restore-marked-quick-look-precedence]

Führen Sie nach dem Installieren oder Aktualisieren oder nach dem Zurücksetzen des Quick-Look-Caches diese Schritte aus:

1. **Starten Sie Marked Quick Look** einmal aus `/Applications` (oder aus Xcode, wenn Sie einen Entwicklungs-Build testen).
2. Registrieren und bevorzugen Sie die Erweiterung im Terminal:

```bash
pluginkit -a "/Applications/Marked Quick Look.app/Contents/PlugIns/MarkedQuickLookPreview.appex"
pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview
```

3. Setzen Sie die Quick-Look-Dienste zurück:

```bash
killall quicklookd QuickLookUIService 2>/dev/null
```

4. Drücken Sie erneut die **Leertaste** auf einer `.md`-Datei.

So leeren Sie zwischengespeicherte Vorschauen:

```bash
qlmanage -r cache
```

### Eine konkurrierende Erweiterung vorübergehend deaktivieren [temporarily-disable-a-conflicting-extension]

Um zu bestätigen, dass eine andere App Marked Quick Look überschreibt, deaktivieren Sie deren Erweiterung mit `pluginkit -e ignore -i BUNDLE_ID`, zeigen Sie eine Datei in der Vorschau an und stellen Sie sie dann mit `pluginkit -e default -i BUNDLE_ID` wieder her.

Beispiel – die Markdown-Erweiterung von **Folder Quick Look** deaktivieren:

```bash
pluginkit -e ignore -i studio.appahead.AA7.Markdown-Quick-Look-Extension
```

### Häufig konkurrierende Apps [common-conflicting-apps]

Diese Apps (und weitere) registrieren Quick-Look-Vorschau-Erweiterungen, die `.md`-Dateien bearbeiten können:

| App | Bundle-ID (Vorschau-Erweiterung) |
| --- | --- |
| **Folder Quick Look** | `studio.appahead.AA7.Markdown-Quick-Look-Extension` |
| **QLMarkdown** | `org.sbarex.QLMarkdown.QLExtension` |
| **Peek** | `com.bigzlabs.peek.peekextension` |
| **Highland Pro** | `com.quoteunquoteapps.highland.pro.qlplugin` |
| **Bear** | `net.shinyfrog.bear.Bear-Quicklook-Extension` |
| **Ulysses** | `com.soulmen.ulysses-setapp.quicklookextension` (Setapp) / `com.soulmen.ulysses.quicklookextension` |
| **Drafts** | `com.agiletortoise.Drafts-OSX.Drafts-OSX-QuickLookPreview` |
| **Scrivener** | `com.literatureandlatte.scrivener3.ScrivQuickLook` |
| **Black Ink** | `com.red-sweater.blackink2.quicklook` |

W> **iA Writer** weist `.md`-Dateien bei Installation seinen eigenen UTI (`net.ia.markdown`) zu. Marked Quick Look 1.0.2+ verarbeitet diesen UTI. **Folder Quick Look**, **QLMarkdown** und **Peek** sind ebenfalls häufige Konfliktquellen.

Registrierte Vorschau-Erweiterungen auflisten:

```bash
pluginkit -m -D -p com.apple.quicklook.preview -A -v | grep -i MarkedQuickLook
```

W> Suchen Sie nicht mit grep nach `markdown`, um Marked Quick Look zu prüfen. Seine Bundle-ID ist `com.brettterpstra.MarkedQuickLook.preview` und enthält das Wort „markdown“ nicht. Ein `grep -i markdown` kann leer bleiben, obwohl Marked Quick Look installiert und aktiviert ist. Um andere Markdown-Handler aufzulisten, führen Sie den vollständigen `pluginkit`-Befehl ohne grep aus oder greppen Sie nach einer bestimmten Bundle-ID aus der Tabelle oben.

Mit `+` markierte Erweiterungen sind ausdrücklich aktiviert; verwenden Sie `pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview`, um Marked Quick Look nach vorn zu holen.

### Immer noch nur Klartext? [still-seeing-plain-text]

Zeigt die Vorschau **ungestalteten Quelltext in Festbreitenschrift**, greift macOS auf den integrierten **Text.qlgenerator** zurück, weil keine Vorschau-Erweiterung zum UTI der Datei passte.

1. Bestätigen Sie die Registrierung mit `pluginkit ... | grep -i MarkedQuickLook` (nicht `markdown`).
2. Prüfen Sie den zugewiesenen UTI der Datei: `mdls -name kMDItemContentType -name kMDItemContentTypeTree /path/to/file.md`
3. Prüfen Sie **Console.app** auf Fehler von `MarkedQuickLookPreview`.
4. Installieren Sie Marked Quick Look erneut nach `/Applications` und starten Sie es einmal.

Eine vollständige Schritt-für-Schritt-Checkliste finden Sie im [Fehlerbehebungs-Leitfaden zu Marked Quick Look](https://github.com/ttscoff/MarkedQuickLook/blob/main/TROUBLESHOOTING.md).

### Entwicklungs-Builds [development-builds]

Debug-Builds aus Xcode liegen in DerivedData und **registrieren sich nicht automatisch**. Führen Sie die Container-App **Marked Quick Look** nach jedem sauberen Build aus Xcode aus (Cmd+R) und führen Sie dann die Befehle `pluginkit -a` und `pluginkit -e use` erneut mit dem DerivedData-Pfad zu Ihrer `.appex` aus.

## Verwandte Themen [related-topics]

- [Dateien öffnen](Opening_Files.html) – wie Marked Dokumente öffnet und überwacht
- [Mehrteilige Dokumente](Multi-File_Documents.html) – Include-Syntax und vollständige Auflösung in Marked
- [Markdown-Prozessor](Choosing_a_Processor.html) – Prozessoroptionen in Marked 3
- [Share-Erweiterung](Share_Extension.html) – Dateien über das Teilen-Menü des Systems an Marked senden
