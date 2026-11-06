# <%= @title %>

Übergeben Sie einem LLM-Agenten eine Skill-Datei, damit er Dateien und Ordner in Marked öffnet, einen Bereich der Einstellungen aufruft und Einstellungen ändert. Der Agent nutzt Markeds [URL-Handler](URL_Handler.md). Ein zusätzliches Plug-in oder ein Server ist nicht nötig.

## Skill herunterladen [download-the-skill]

{% download "SKILL.md" "Skill für einen Agenten, der Dateien in Marked öffnet und Einstellungen ändert. Speichern Sie die Datei als SKILL.md." %}

Die Datei ist einfaches Markdown mit einem kurzen Kopf, den der Agent liest, bevor er handelt. Dieselbe Datei eignet sich für jeden Agenten, der einen Skill oder eine feste Anweisung annimmt.

## Skill installieren [install-it]

Legen Sie die Datei in einen Ordner, der nach dem Skill benannt ist, und behalten Sie den Dateinamen `SKILL.md` bei.

Für Cursor funktionieren beide Orte:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

Der erste gilt für jedes Projekt. Der zweite gilt nur für dieses Projekt. Andere Agenten können denselben Text als Projektanweisung verwenden, wenn sie keinen Skill-Ordner haben.

Nach der Installation bitten Sie den Agenten, eine Datei oder einen Ordner in Marked zu öffnen. Er sollte einen Befehl wie diesen ausführen:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Ein Ordner verwendet denselben Befehl. Der Pfad muss vorhanden sein, und Leerzeichen sowie andere reservierte Zeichen müssen prozentkodiert werden. Das vollständige Schema, einschließlich refresh, Streaming-Vorschau und Rückrufen, steht im [URL-Handler](URL_Handler.md).

## Einstellungen [preferences]

Der Skill deckt außerdem zwei Befehle für Einstellungen ab:

`pref`
: Öffnet die Einstellungen bei einem Bereich. Der Name in der URL bleibt Englisch, etwa `Preview` oder `Style`. Der Befehl ändert keinen Wert.

`defaults`
: Setzt eine Einstellung, die Marked bereits gespeichert hat, und lädt offene Vorschauen neu. Mit `refresh=0` bleiben die Vorschauen unverändert. Der Agent sollte die aktuellen Einstellungen lesen, bevor er eine schreibt, denn ein unbekannter Schlüssel wird ignoriert.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Siehe auch [related]

[Marked beim agentenbasierten Programmieren](Using_Marked_with_Agentic_Coding.md) beschreibt, wie Marked einen Ordner mit Plänen und Notizen überwacht, während ein Agent sie schreibt. Das [Kommandozeilenwerkzeug](Command_Line_Utility.md) bietet dieselbe Art von Zugriff aus der Shell, ohne Agenten.
