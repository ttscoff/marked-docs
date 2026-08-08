# <%= @title %>

Marked funktioniert mit [Obsidian][obsidian-app]-Notizen auf zwei Arten: Öffnen Sie einen **Vault-Ordner** für automatische Nachverfolgung oder verwenden Sie das **Community-Plugin** für eine engere Synchronisierung.

Die integrierte Vorschau von Obsidian ist ideal, wenn Sie die App nie verlassen. Wählen Sie Marked, wenn Sie einen Export in Veröffentlichungsqualität, erweitertes Korrekturlesen, benutzerdefinierte CSS-Designs oder denselben Live-Vorschau-Workflow für mehrere Editoren wünschen. Einen vollständigen Vergleich finden Sie unter [Marked im Vergleich zur Obsidian-Vorschau](Marked_vs_Obsidian_Preview.html).

## Einen gesamten Vault öffnen [open-an-entire-vault]

Ziehen Sie den **Vault-Ordner** (das Verzeichnis, das den versteckten Konfigurationsordner von Obsidian im Vault-Stammverzeichnis enthält) auf Marked im Dock. Marked überwacht diesen Baum, behält die **zuletzt bearbeitete** Notiz in der Vorschau und aktualisiert sie, wenn Sie in Obsidian speichern.

Fügen Sie für Vault-spezifische Standardeinstellungen (Stil, Prozessor, Basis-URL für Bilder usw.) eine [Eigene Regel](http://support.markedapp.com) hinzu, die den Pfaden unter diesem Vault entspricht.

## Obsidian-Callout-Syntax [obsidian-callout-syntax]

Wenn der MultiMarkdown-Prozessor ausgeführt wird, konvertiert Marked gängige **Callouts im Obsidian-Stil** (das `> [!note]`-Muster) in stilisierte Blockmarkierungen, sodass sie mit dem Rest Ihrer Vorschau übereinstimmen.

## Marked 3 Obsidian-Plugin [marked-3-obsidian-plugin]

Das [Marked 3 Obsidian plugin][plugin] kann die aktuelle Notiz oder den gesamten Vault mit Befehlen oder Hotkeys öffnen, sodass das Marked-Fenster verfolgt, was Sie bearbeiten. Verwenden Sie die Befehlspalette (**⌘P**) und suchen Sie nach **Marked** oder weisen Sie Hotkeys in den **Hotkeys**-Einstellungen von Obsidian zu.

### Installation über Community-Plugins [installing-from-community-plugins]

Öffnen Sie in Obsidian **Einstellungen → Community-Plugins**, suchen Sie nach **Marked** und installieren Sie **Open in Marked**.

### Manuelle Installation des Plugins [manually-installing-the-plugin]

Wenn Sie lieber von GitHub installieren möchten:

1. Laden Sie `main.js` und `manifest.json` vom [neuesten Release][plugin-releases] auf GitHub herunter (oder erstellen Sie sie aus dem [Marked3-obsidian][plugin]-Repository).
2. Erstellen Sie in Ihrem Vault den Plugin-Ordner unter `plugins/` im Konfigurationsverzeichnis von Obsidian im Stammverzeichnis des Vaults. Der Ordnername muss mit der Plugin-`id` in `manifest.json` übereinstimmen (den vollständigen Pfad finden Sie in der [Plugin-README][plugin]).
3. Kopieren Sie `main.js` und `manifest.json` in diesen Ordner.
4. Öffnen Sie in Obsidian **Einstellungen → Community-Plugins**, deaktivieren Sie bei Bedarf den **Eingeschränkten Modus** und aktivieren Sie **Open in Marked**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest
