# <%= @title %>

„Dokument befragen“ nutzt **Apple Intelligence** und das in neueren macOS-Versionen integrierte, geräteinterne Sprachmodell, um Ihre Markdown-Vorschau zusammenzufassen und Fragen zu ihrem Inhalt zu beantworten. Die gesamte Verarbeitung läuft auf Ihrem Mac; der Dokumenttext wird für diese Funktion nicht an die Server von Marked oder an KI-Dienste Dritter gesendet.

## Was Apple Intelligence bietet [what-apple-intelligence-provides]

Apple Intelligence ist Apples System für generative Funktionen auf dem Gerät. Marked nutzt das **Foundation Models**-Framework von Apple, um auf dasselbe geräteinterne Modell zuzugreifen, das auch die Schreibwerkzeuge des Systems antreibt – hier direkt in Marked für dokumentbezogene Aufgaben.

Marked sendet den reinen Text Ihres Dokuments (die Markdown-Syntax wird zur Klarheit entfernt) an dieses lokale Modell. Das Modell erzeugt Zusammenfassungen, Gliederungen und Antworten in einem schwebenden Bereich neben Ihrem Vorschaufenster. Da das Modell lokal ausgeführt wird, funktioniert es offline, sobald Apple Intelligence eingerichtet ist und der Download des Systemmodells abgeschlossen ist.

Apple Intelligence eignet sich am besten für Sprachaufgaben wie Zusammenfassungen, Gliederungen, das Extrahieren wichtiger Punkte und das Beantworten von Fragen zu bereitgestelltem Text. Es ist kein allgemeiner Programmierassistent und kein Rechner; sehr lange Dokumente werden abschnittsweise verarbeitet, damit die Ergebnisse innerhalb der Kontextgrenzen des Modells bleiben.

## Systemkompatibilität [system-compatibility]

„Dokument befragen“ wird nur angezeigt, wenn Ihr Mac die Funktion ausführen kann.

**Erforderlich:**

- **macOS 26 (Tahoe)** oder höher
- Ein **Mac mit Apple Intelligence-Unterstützung** (Apple-Silicon-Macs, die die Geräteanforderungen von Apple erfüllen)
- **Apple Intelligence aktiviert** in den Systemeinstellungen

**Nicht unterstützt:**

- Intel-Macs und andere Macs, die für Apple Intelligence nicht infrage kommen
- macOS-Versionen vor Tahoe 26
- Rohe **HTML-Vorschauen** (die Funktion gilt für Markdown- und textbasierte Dokument-Workflows)

Wenn Ihr Mac die Voraussetzungen erfüllt, das Menüelement jedoch fehlt, stellen Sie sicher, dass Apple Intelligence aktiviert ist und dass Sie einen aktuellen Build von Marked ausführen, der diese Funktion enthält. Das Menü wird auf nicht unterstützten Systemen vollständig ausgeblendet und nicht als deaktiviert angezeigt.

## Aktivieren von Apple Intelligence [enabling-apple-intelligence]

1. Öffnen Sie **Systemeinstellungen**.
2. Gehen Sie zu **Apple Intelligence & Siri** (oder **Apple Intelligence**, abhängig von Ihrer macOS-Version).
3. Aktivieren Sie **Apple Intelligence** und führen Sie alle von Apple angeforderten Einrichtungsschritte aus.
4. Warten Sie, bis der Download des Modells auf dem Gerät abgeschlossen ist, wenn Sie dazu aufgefordert werden. Bis das Modell bereit ist, kann Marked den Menüpunkt bereits anzeigen, meldet dann aber, dass Apple Intelligence noch vorbereitet wird.

Marked enthält keine separate Einstellung für diese Funktion. Die Verfügbarkeit richtet sich nach dem von macOS gemeldeten Systemmodellstatus.

## „Dokument befragen“ öffnen [opening-ask-about-document]

Öffnen Sie das Panel mit einer der folgenden Methoden:

- **Vorschau > Dokument befragen…**
- Tastaturkürzel {% kbd shift ctrl cmd I %} (während ein Markdown-Vorschaudokument das aktive Fenster ist)

Das Bedienfeld wird an der linken Seite des Dokumentfensters angedockt. Sie brauchen ein geöffnetes Dokument mit lesbarem Text; bei einem leeren Dokument oder einer reinen HTML-Vorschau erscheint der Befehl nicht.

## Das Fenster „Dokument befragen“ [the-ask-about-document-panel]

Das Panel ist wie eine einfache Chat-Ansicht organisiert:

- **Voreingestellte Aktionen** oben für häufige Aufgaben
- Ein **Antwortbereich** in der Mitte, in dem Zusammenfassungen und Antworten angezeigt werden (mit Streaming, während sie generiert werden)
- Ein **Fragefeld** unten, in das Sie eigene Fragen eingeben, mit den Schaltflächen **Fragen** und **Abbrechen**

Nachdem eine Antwort abgeschlossen ist, kehrt der Fokus zum Fragefeld zurück, sodass Sie ohne Klicken eine weitere Frage stellen können.

### Voreingestellte Aktionen [preset-actions]

| Aktion | Was es tut |
| :-- | :-- |
| **Dokument zusammenfassen** | Erstellt eine kurze, zusammenhängende Zusammenfassung des gesamten Dokuments. Lange Dokumente werden abschnittsweise zusammengefasst und die Teile verbunden. |
| **Auswahl zusammenfassen** | Fasst nur den aktuell in der Vorschau ausgewählten Text zusammen. Wählen Sie zuerst Text aus; sonst bittet Marked Sie, eine Auswahl zu treffen oder „Dokument zusammenfassen“ zu verwenden. |
| **Gliederung** | Erstellt aus Überschriften und Aufzählungspunkten eine hierarchische Gliederung der Dokumentstruktur. |
| **Kernpunkte** | Listet die wichtigsten Aussagen des Dokuments als Aufzählung auf. |

Voreingestellte Aktionen brauchen keinen Text im Fragefeld. Klicken Sie auf eine Schaltfläche und warten Sie auf die Antwort im Bereich darüber.

### Eigene Fragen stellen [asking-your-own-questions]

1. Geben Sie eine Frage in das Feld unten im Panel ein, zum Beispiel „Welches Problem löst dieses Dokument?“ oder „Wer ist die Zielgruppe?“
2. Drücken Sie **Return** oder klicken Sie auf **Fragen**.
3. Lesen Sie die Antwort, während sie im Antwortbereich erscheint.

Bei Fragen zu einer bestimmten Passage **wählen Sie diesen Text in der Vorschau aus**, bevor Sie fragen. Marked sendet die Auswahl als Kontext statt des gesamten Dokuments, wenn eine Auswahl aktiv ist.

Klicken Sie auf **Abbrechen**, um eine laufende Anfrage zu stoppen.

## Beispiele [examples]

### Kurzer Überblick über einen langen Artikel [quick-overview-of-a-long-article]

Öffnen Sie einen längeren Blogbeitrag oder Bericht in Marked, wählen Sie **Vorschau > Dokument befragen…** und klicken Sie auf **Dokument zusammenfassen**. Anhand der Zusammenfassung entscheiden Sie, ob Sie den ganzen Artikel lesen, oder frischen Ihr Gedächtnis auf, wenn Sie länger nicht am Entwurf waren.

### Notizen zu einem ausgewählten Absatz [notes-on-a-selected-paragraph]

Markieren Sie in der Vorschau einen dichten Absatz, öffnen Sie „Dokument befragen“ und klicken Sie auf **Auswahl zusammenfassen**. Nützlich, wenn Sie nur eine kürzere Version eines Abschnitts benötigen.

### Strukturüberprüfung [structural-review]

Klicken Sie bei einem Entwurf mit vielen Überschriften auf **Gliederung**, um zu sehen, ob die Argumentation logisch verläuft, oder auf **Kernpunkte**, bevor Sie ein Dokument weitergeben, um zu prüfen, ob die Hauptgedanken klar sind.

### Gezielte Fragen [targeted-questions]

Wenn keine Auswahl aktiv ist, geben Sie Fragen ein wie:

- „Was sind die drei wichtigsten Empfehlungen?“
- „Erwähnt dieses Dokument die Lizenzierung?“
- „Liste alle genannten Termine oder Fristen auf.“

Stellen Sie bei aktiver Auswahl enger gefasste Fragen wie „Was sagt dieser Absatz über den Leser aus?“ oder „Formuliere diese Idee in einem Satz um“ (das Modell antwortet zur Auswahl; Ihre Quelldatei wird nicht bearbeitet).

## Tipps und Einschränkungen [tips-and-limitations]

- **Datenschutz:** Die Verarbeitung läuft über Apples geräteinternes Modell. Marked liest Ihren Dokumenttext trotzdem lokal, um ihn dem Modell zu übergeben; behandeln Sie sensibles Material entsprechend.
- **Genauigkeit:** Überprüfen Sie wichtige Fakten anhand Ihrer Quelle. KI-Zusammenfassungen können Details auslassen oder mehrdeutige Passagen falsch interpretieren.
- **Länge:** Sehr lange Dokumente werden in Blöcken verarbeitet. Zusammenfassungen und Antworten geben den vollständigen Text nur mittelbar wieder; für ein genaues Ergebnis zu einem Abschnitt wählen Sie diesen zuerst aus.
- **Sprache:** Die Ergebnisse richten sich nach den Sprachfähigkeiten des Apple-Intelligence-Modells auf Ihrem Mac.
- **Ablehnungen:** Das System lehnt möglicherweise einige Anfragen aufgrund der Sicherheitsrichtlinien von Apple ab.

Ist „Dokument befragen“ nicht verfügbar, prüfen Sie in den Systemeinstellungen den Status von Apple Intelligence und stellen Sie sicher, dass Sie ein Markdown-Dokument auf einem unterstützten Mac mit macOS 26 oder höher in der Vorschau haben.
