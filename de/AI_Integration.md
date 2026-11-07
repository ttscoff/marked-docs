# <%= @title %>

Übergeben Sie einem LLM-Agenten eine Skill-Datei, damit er Dateien und Ordner in Marked öffnet, einen Bereich der Einstellungen aufruft und Optionen ändert. Der Agent nutzt Markeds [URL-Handler](URL_Handler.html). Ein eigenes Plugin oder einen eigenen Server brauchen Sie nicht.

## Skill herunterladen [download-the-skill]

{% download "SKILL.md" "Agenten-Skill zum Öffnen von Dateien in Marked und zum Ändern von Einstellungen. Speichern Sie die Datei als SKILL.md." %}

Die Datei besteht aus reinem Markdown mit einem kurzen Kopfbereich, den der Agent liest, bevor er tätig wird. Sie können dieselbe Datei jedem Agenten geben, der Skills oder dauerhafte Anweisungen annimmt.

## Skill installieren [install-it]

Legen Sie die Datei in einen Ordner, der nach dem Skill benannt ist, und behalten Sie den Dateinamen `SKILL.md` bei.

Für Cursor kommt jeder dieser beiden Speicherorte infrage:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

Der erste steht in jedem Projekt zur Verfügung, der zweite gilt nur für das jeweilige Projekt. Andere Agenten können denselben Text als Projektanweisung verwenden, wenn sie keinen Skill-Ordner haben.

Bitten Sie den Agenten nach der Installation, eine Datei oder einen Ordner in Marked zu öffnen. Er sollte einen Befehl wie diesen ausführen:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Für einen Ordner gilt derselbe Befehl. Der Pfad muss existieren, und Leerzeichen sowie andere reservierte Zeichen müssen prozentkodiert sein. Das vollständige Schema mit refresh, Streaming-Vorschau und Callbacks steht unter [URL-Handler](URL_Handler.html).

## Einstellungen [preferences]

Der Skill deckt außerdem zwei Befehle für Einstellungen ab:

`pref`
: Öffnet einen bestimmten Bereich der Einstellungen. In der URL steht sein englischer Name, etwa `Preview` oder `Style`. Der Befehl ändert keinen Wert.

`defaults`
: Setzt eine Einstellung, die Marked ohnehin speichert, und lädt danach offene Vorschauen neu. Mit `refresh=0` bleiben die Vorschauen unberührt. Der Agent sollte die aktuellen Einstellungen lesen, bevor er eine davon ändert, denn ein unbekannter Schlüssel wird ignoriert.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Verwandt [related]

[Marked beim agentenbasierten Programmieren](Using_Marked_with_Agentic_Coding.html) beschreibt, wie Marked einen Ordner mit Plänen und Notizen überwacht, während ein Agent sie schreibt. Das [Kommandozeilenwerkzeug](Command_Line_Utility.html) bietet dieselbe Art von Zugriff aus der Shell, ganz ohne Agenten.
