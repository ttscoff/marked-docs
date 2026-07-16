# <%= @title %>

Marked kann automatisch responsive `<picture>`-Elemente für lokale Bilder erstellen, wenn sich die zugehörigen **Dunkelmodus**- und **Retina**-Dateien neben dem referenzierten Bild befinden. Dabei verwendet Marked dieselben Namenskonventionen wie Apples DocC-Dokumentationskataloge. Die Funktion steht jedoch für **jedes Markdown- oder HTML-Dokument** mit normalen Bildpfaden und Dateierweiterung zur Verfügung.

Siehe auch [DocC-Unterstützung](DocC_Support.html) für Katalogverweise ohne Dateierweiterung in `.docc`-Bundles.

## Bildvarianten aktivieren [enabling-image-variants]

Aktivieren Sie in {% prefspane Apps %} unter den DocC-Einstellungen **Dunkle und @2x-Bildvarianten auflösen** (standardmäßig aktiviert).

Diese Einstellung ist unabhängig von **DocC-Bildverweise auflösen**, die nur innerhalb von `.docc`-Katalogen gilt. Abhängig von Ihrem Projekt können Sie eines, beide oder keines von beiden verwenden.

## Namenskonvention [naming-convention]

Platzieren Sie Variantendateien im **gleichen Ordner** wie das Primärbild. Marked sucht basierend auf dem Basisnamen nach vier Kombinationen:

| Rolle | Beispieldateiname |
|------|------------------|
| Licht (1x) | `icon.png` |
| Dunkel (1x) | `icon~dark.png` |
| Licht (2x) | `icon@2x.png` |
| Dunkel (2x) | `icon~dark@2x.png` |

Die Reihenfolge der Suffixe ist flexibel – `icon@2x~dark.png` und `icon~dark@2x.png` werden gleich behandelt.

Unterstützte Erweiterungen: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` und `pdf`.

## Was umgeschrieben wird [what-gets-rewritten]

Marked durchsucht Ihr Dokument **vor** dem endgültigen Rendern der Vorschau:

- **Markdown:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Wenn mindestens **zwei** übereinstimmende Variantendateien auf der Festplatte vorhanden sind, wird die Referenz durch einen `<picture>`-Block ersetzt. Eine einzige zusätzliche Datei reicht aus – Sie benötigen nicht alle vier Varianten.

Beispielausgabe, wenn helle, dunkle und @2x-Dateien vorhanden sind:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

Die Vorschau (und der HTML-Export) folgt dann der Systemdarstellung des Benutzers für dunkle Varianten und der Gerätepixeldichte für @2x-Assets.

## Was übersprungen wird [what-is-skipped]

Marked schreibt **nicht** um:

- Remote-URLs (`http://`, `https://`, `data:`)
- Verweise, die bereits auf eine `~dark`-Datei zeigen
- `<img>`-Tags, die sich bereits in einem vorhandenen `<picture>`-Element befinden
- Namen ohne Erweiterung wie `![Diagram](diagram)` – verwenden Sie für Referenzen im Katalogstil die [DocC-Unterstützung](DocC_Support.html)

## Live-Vorschau und Dateiüberwachung [live-preview-and-file-watching]

Wenn Marked Varianten erkennt, fügt es **jede vorhandene Variantendatei** zusammen mit dem Hauptdokument zur Überwachungsliste hinzu. Wenn Sie `icon~dark.png` in einem externen Editor speichern, wird das Bild in der Live-Vorschau genauso neu geladen wie beim Bearbeiten von `icon.png`.

## Tipps [tips]

- Verweisen Sie in Ihrer Quelle nach Möglichkeit auf das **helle 1x-Bild** (`icon.png`, nicht `icon~dark.png`). Marked ermittelt die zugehörigen Dateien von diesem Pfad aus.
- Wenn Sie nur über `@2x`-Assets verfügen, fügen Sie mindestens eine weitere Variante hinzu (normalerweise `~dark`), sonst lässt Marked die Referenz unverändert.
- Bei der Variantenauflösung werden Pfade **relativ zum Dokument** verwendet (bei verschachtelten Einbindungen relativ zum Ordner der eingebundenen Datei). Dabei gelten dieselben Basispfadregeln wie für [Dokumente mit mehreren Dateien](Multi-File_Documents.html).

## Verwandte Themen [related-topics]

- [DocC-Unterstützung](DocC_Support.html) – Bildnamen ohne Erweiterung in `.docc`-Katalogen
- [Einstellungen: Apps](Settings_Apps.html) – Einstellungen für DocC- und Bildvarianten
- [Vorschau](Previewing.html) – Live-Vorschau und Dateiaktualisierungen
