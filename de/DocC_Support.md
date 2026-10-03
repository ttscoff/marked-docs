# <%= @title %>

Marked versteht [Apple DocC](https://www.swift.org/documentation/docc/)-Dokumentationskataloge (`.docc`-Bundles). Wenn Sie Markdown in der Vorschau anzeigen, das sich innerhalb oder neben einem Katalog befindet, kann Marked **erweiterungslose** Bildverweise auf Dateien im Ordner `Resources` des Katalogs auflösen – einschließlich der Varianten `~dark` und `@2x`.

Für normale Markdown-Dokumente, die **Pfade mit Dateierweiterungen** (`images/icon.png`) verwenden, siehe [Bildvarianten](Image_Variants.html). Diese Funktion funktioniert überall; die DocC-Auflösung ist katalogspezifisch.

## DocC-Auflösung aktivieren [enabling-docc-resolution]

Aktivieren Sie in {% prefspane Apps %} **DocC-Bildverweise auflösen** (standardmäßig aktiviert).

Die DocC-Erkennung wird ausgeführt, wenn Marked einen übergeordneten `.docc`-Katalog des geöffneten Dokuments findet. Es ist kein spezielles URL-Schema und keine Xcode-Integration erforderlich – öffnen Sie den Markdown des Katalogs genauso wie jede andere Datei.

## Erweiterungslose Referenzen [extensionless-references]

In einem DocC-Katalog verweisen Autoren normalerweise auf Bilder **ohne** einen Pfad oder eine Erweiterung:

```markdown
![Order flow](OrderStateTransitions)
```

Marked löst `OrderStateTransitions` in `Resources/OrderStateTransitions.png` (oder einen anderen unterstützten Typ) auf, wenn diese Datei im Katalog vorhanden ist.

Referenzen, die bereits einen Pfad und eine Erweiterung enthalten – `images/chart.png` – werden stattdessen [Bildvarianten](Image_Variants.html) überlassen und durch die DocC-Auflösung nicht neu geschrieben.

## Dunkelmodus und Retina-Varianten [dark-mode-and-retina-variants]

DocC-Kataloge liefern oft mehrere Dateien pro Bild:

| Rolle | Beispiel in `Resources/` |
|------|-----------|
| Hell (1x) | `diagram.png` |
| Dunkel (1x) | `diagram~dark.png` |
| Hell (2x) | `diagram@2x.png` |
| Dunkel (2x) | `diagram~dark@2x.png` |

Wenn mehr als eine Variante vorhanden ist, gibt Marked das gleiche responsive `<picture>`-Markup aus, das unter [Bildvarianten](Image_Variants.html) beschrieben wird. Ein einzelner Dateiverweis wird weiterhin in einen normalen `<img>`- oder `![](Resources/...)`-Pfad aufgelöst.

## HTML und Markdown [html-and-markdown]

Die DocC-Auflösung gilt während des Include-Durchlaufs von Marked:

- **Markdown-Quellen** – `![alt](ImageName)`-Referenzen
- **HTML-Quellen** – `<img src="ImageName">` ohne Erweiterung

Beide werden vor dem Rendern der Vorschau aktualisiert.

## Dateiüberwachung [file-watching]

Aufgelöste Bilder im Katalogordner `Resources` werden zur Beobachtungsliste von Marked hinzugefügt. Durch die externe Bearbeitung einer Variantendatei wird die Vorschau ohne manuelle Aktualisierung aktualisiert.

## Verwandte Themen [related-topics]

- [Bildvarianten](Image_Variants.html) – `~dark`- und `@2x`-Erkennung für Pfade mit Dateierweiterungen in jedem Projekt
- [Xcode-Playgrounds](Xcode_Playgrounds.html) – Vorschau von Swift-Playground-Kommentaren
- [Einstellungen: Anwendungen](Settings_Apps.html) – DocC- und Bildvarianteneinstellungen
