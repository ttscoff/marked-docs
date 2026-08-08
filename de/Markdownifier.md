# Markdownifier [markdownifier]

Der Markdownifier ist ein Tool, das automatisch Inhalte aus Webseiten extrahiert und in das saubere Markdown-Format konvertiert. Er verarbeitet Webinhalte intelligent, liefert Ihnen genau den aussagekräftigen Text samt Struktur und filtert Werbung, Navigationselemente und anderen Ballast heraus.

![Markdownify URL][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Wie es funktioniert [how-it-works]

Der Markdownifier verwendet erweiterte Algorithmen zur Inhaltsextraktion und kann:

1. Webseiteninhalte **abrufen und analysieren**
2. Den **Haupttext des Artikels** und dessen Struktur identifizieren
3. Den Inhalt **bereinigen und formatieren**, bis sauberes Markdown entsteht
4. Werbung, Navigation und andere Nicht-Inhalts-Elemente **herausfiltern**
5. Wichtige Formatierungen wie Überschriften, Listen und Links **erhalten**

## Den Markdownifier öffnen [opening-the-markdownifier]

Um auf den Markdownifier zuzugreifen, öffnen Sie {% appmenu Ablage, Neu, URL in Markdown umwandeln (@~k) %}. Geben Sie die URL ein, die Sie umwandeln möchten, und drücken Sie die Eingabetaste ({% kbd return %}).

## Den Markdownifier verwenden [using-the-markdownifier]

### Grundlegende Verwendung [basic-usage]

1. **Öffnen Sie den Markdownifier** mit einer der oben genannten Methoden
2. **Geben Sie eine URL ein** in das angezeigte Textfeld
3. **Klicken Sie auf „Automatisch“** oder drücken Sie `Return`, um Inhalte zu extrahieren
4. Der extrahierte Inhalt wird **automatisch** in einem neuen Marked-Dokument geöffnet

### Manuelle Inhaltsauswahl [manual-content-selection]

Wenn die automatische Extraktion nicht den gewünschten Inhalt erfasst:

1. Klicken Sie auf die Schaltfläche **„Manuell“**, um die Seite in einer Webansicht zu laden
2. **Navigieren und scrollen**, um den gewünschten Inhalt zu finden
3. **Klicken Sie auf die Schaltfläche „Inhalt extrahieren“**, die über der Webseite angezeigt wird
4. Der ausgewählte Inhalt wird in Markdown konvertiert und in Marked geöffnet.

### Zwischenablage-Integration [clipboard-integration]

Der Markdownifier erkennt beim Öffnen automatisch URLs in Ihrer Zwischenablage:

- Wenn eine URL gefunden wird, wird diese im URL-Feld **vorab ausgefüllt**
- Sie müssen noch auf **„Automatisch“** klicken oder `Return` drücken, um die Verarbeitung zu starten
- Dies verhindert die versehentliche Verarbeitung von Zwischenablage-URLs

## Inhaltsverarbeitung [content-processing]

### Automatische Inhaltsvalidierung [automatic-content-validation]

Der Markdownifier validiert extrahierte Inhalte intelligent, um sicherzustellen, dass sie aussagekräftigen Text enthalten:

- **Entfernt Metadaten** (YAML-Frontmatter, MultiMarkdown-Header)
- **Entfernt Linkdefinitionen** und Links im Referenzstil
- **Filtert** eigenständige URLs und Navigationselemente heraus
- **Komprimiert Leerraum** für eine genaue Längenbewertung
- **Erfordert mindestens 200 Zeichen** des tatsächlichen Inhalts

Wenn der extrahierte Inhalt zu kurz ist oder hauptsächlich aus Navigation/Werbung zu bestehen scheint, greift der Markdownifier automatisch auf den manuellen Auswahlmodus zurück.

### Inhaltsformatierung [content-formatting]

Der extrahierte Inhalt wird als sauberes Markdown formatiert mit:

- **Quellenlink** oben: `[source](original-url)`
- **H1-Titeleinfügung** bei Bedarf
- **Erhaltene Listen** (geordnet und ungeordnet)
- **Beibehaltene Links** und Hervorhebungsformatierung
- **Saubere Absätze** mit richtigem Abstand

## Sicherheitsfunktionen [safety-features]

### Absturzsicherung [crash-prevention]

Der Markdownifier enthält mehrere Sicherheitsmaßnahmen, um Abstürze zu verhindern:

- **Blockiert problematische URLs** (Werbenetzwerke, Tracking-Dienste, kryptobezogene Inhalte)
- **Filtert beschädigte Bilder**, die zu Rendering-Problemen führen können
- **Deaktiviert erweiterte Webfunktionen**, die zu Instabilität führen können
- **Automatische Wiederherstellung nach einem Absturz** mit Fallback im abgesicherten Modus

### Datenschutz [privacy-protection]

- **Privater Browsermodus** verhindert Tracking und Cookies
- **Keine Plugins oder Java**-Ausführung aus Sicherheitsgründen
- **Eingeschränktes JavaScript** mit Krypto-API-Blockierung
- **Ressourcenfilterung** blockiert Tracking und Anzeigeninhalte

## Fehlerbehebung [troubleshooting]

### Inhalt nicht extrahiert [content-not-extracted]

Wenn die automatische Extraktion fehlschlägt:

1. **Versuchen Sie es mit der manuellen Auswahl** über die Schaltfläche „Manuell“.
2. **Überprüfen Sie, ob die Website JavaScript erfordert** – einige Websites müssen manuell geladen werden
3. **Prüfen Sie die URL** – sie muss erreichbar sein und Artikelinhalt enthalten
4. **Suchen Sie nach Paywalls oder Anmeldeanforderungen**, die den Zugriff blockieren könnten

### WebView-Probleme [webview-issues]

Wenn die Webansicht instabil wird:

1. Der Markdownifier wechselt **automatisch in den abgesicherten Modus**
2. **JavaScript wird deaktiviert**, um Abstürze zu verhindern
3. **Verwenden Sie die Schaltfläche „Konvertieren“** anstelle der manuellen Auswahl
4. **Schließen und erneut öffnen** kann helfen, um den Markdownifier zurückzusetzen

### Fehlender Inhalt [missing-content]

Wenn wichtige Inhalte in der Extraktion fehlen:

1. Der **automatische Algorithmus** hat sie möglicherweise herausgefiltert
2. **Verwenden Sie die manuelle Auswahl**, um den gewünschten Inhalt auszuwählen
3. **Prüfen Sie den HTML-Quelltext**, um zu sehen, ob der Inhalt dynamisch geladen wird
4. **Versuchen Sie es mit einer anderen URL**, wenn die Site eine komplexe Struktur hat

## Tipps für beste Ergebnisse [tips-for-best-results]

### URL-Auswahl [url-selection]

- **Verwenden Sie Artikel-URLs** anstelle von Startseiten oder Kategorieseiten
- **Vermeiden Sie nach Möglichkeit URLs mit Tracking-Parametern**

### Inhaltsqualität [content-quality]

- **Längere Artikel** werden im Allgemeinen besser extrahiert als kurze Beiträge
- **Gut strukturierter Inhalt** mit richtigen Überschriften funktioniert am besten
- **Vermeiden Sie Websites mit hohem JavaScript-Anteil** für die automatische Extraktion

### Manuelle Auswahl [manual-selection]

- **Warten Sie, bis die Seite vollständig geladen ist**, bevor Sie sie extrahieren
- **Scrollen Sie durch den Inhalt**, um sicherzustellen, dass alles geladen ist
- **Bewegen Sie den Mauszeiger über Bereiche**, um das kleinste blaue Feld auszuwählen, das den gesamten Inhalt enthält, den Sie extrahieren möchten
- **Klicken**, wenn Sie den gewünschten Inhalt gefunden haben

## Erweiterte Funktionen [advanced-features]

### Stapelverarbeitung [batch-processing]

Während der Markdownifier jeweils eine URL verarbeitet, gibt es zusätzlich diese Möglichkeiten:

- **Stellen Sie mehrere URLs in die Warteschlange**, indem Sie den Markdownifier mehrmals öffnen
- Die **Dienste-Integration** nutzen, um URLs aus anderen Anwendungen zu verarbeiten
- **Kopieren Sie den extrahierten Inhalt** und fügen Sie ihn in vorhandene Marked-Dokumente ein

### Integration mit Marked [integration-with-marked]

Extrahierter Inhalt wird in Marked geöffnet, mit:

- **Automatischer Dateibenennung** basierend auf dem Artikeltitel
- **Beibehaltung der Quell-URL** in den Dokumentmetadaten
- **Vollständige Marked-Funktionen** zum Lesen und Exportieren

## Technische Details [technical-details]

### Unterstützte Inhaltstypen [supported-content-types]

- **HTML-Artikel** mit Standard-Markup
- **Blogbeiträge** und Nachrichtenartikel
- **Dokumentation** und Hilfeseiten
- **Forumbeiträge** und Diskussionsinhalte

### Einschränkungen [limitations]

- **Paywall-Websites** erfordern möglicherweise eine Anmeldung und eine manuelle Extraktion
- **JavaScript-lastige Websites** erfordern möglicherweise eine manuelle Auswahl
- **Dynamischer Inhalt**, der nach dem Laden der Seite geladen wird, wird möglicherweise übersehen, kann aber durch manuelle Extraktion erfasst werden
- **Komplexe Layouts** können unerwünschte Navigationselemente enthalten

Der Markdownifier soll die Extraktion von Webinhalten so einfach und zuverlässig wie möglich machen und gleichzeitig Fallback-Optionen für komplexe oder problematische Websites bieten.
