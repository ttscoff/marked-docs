<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked enthält eine macOS-**Share-Erweiterung**, die im systemweiten Teilen-Menü erscheint. Damit senden Sie Dateien oder markierten Text an Marked, ohne die App zu wechseln oder URLs manuell zu kopieren.

Die Share-Erweiterung ist **in Marked 3 enthalten**. Sie laden und installieren sie nicht separat. Sie ist in den Direct-, Mac-App-Store-, Marked-Pro- und Setapp-Builds enthalten.

## Funktionsweise

Wenn Sie im Teilen-Menü **Marked** wählen, öffnet sich Marked sofort. Es gibt kein Zwischenfenster zum Bearbeiten.

### Datei teilen

Wählen Sie in **Finder** (oder einer anderen App, die Dateien teilt) **Teilen → Marked**.

Marked erhält den Dateipfad und öffnet die Datei über denselben `x-marked-3://open`-URL-Handler wie anderswo. Die Datei öffnet sich in Marked wie ein Dokument, das Sie auf das Dock-Symbol gezogen oder mit {% appmenu File, Open... ({{cmd}}O) %} geöffnet haben.

Unterstützt werden Datei-URLs, lokale Dateien und Web-URLs, wenn die sendende App sie bereitstellt.

### Markierten Text teilen

Markieren Sie Text in einer App wie **TextEdit**, **Safari** oder **Mail** und wählen Sie **Teilen → Marked**.

Marked legt den Text in die Zwischenablage und öffnet eine **temporäre Vorschau** über den Handler `x-marked-3://paste`. Das entspricht der ungespeicherten Vorschau von {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Sie können sie später mit {% appmenu File, Save Transient Preview %} speichern.

Klartext, HTML, RTF und Markdown werden unterstützt, wenn die Quell-App sie bereitstellt.

Details zu den zugrunde liegenden Befehlen finden Sie unter [URL Handler](URL_Handler.html).

## Teilen-Menü verwenden

### Aus Finder

1. Klicken Sie mit der rechten Maustaste auf eine Markdown- oder Textdatei (oder wählen Sie sie und klicken Sie in der Finder-Symbolleiste auf **Teilen**).
2. Wählen Sie im Teilen-Menü **Marked**.

Wenn **Marked** nicht sichtbar ist, siehe [Share-Erweiterung aktivieren](#enable-the-share-extension) unten.

### Aus Textauswahl

1. Markieren Sie den Text, den Sie in der Vorschau sehen möchten.
2. Öffnen Sie das **Teilen**-Menü der App (Menüleiste, Symbolleiste oder Kontextmenü).
3. Wählen Sie **Marked**.

Marked startet (oder kommt in den Vordergrund) mit einer Vorschau des geteilten Inhalts.

## Share-Erweiterung aktivieren

Marked muss in `/Applications` (oder Ihrem üblichen Programme-Ordner) installiert und mindestens einmal gestartet worden sein, bevor macOS die Share-Erweiterung anzeigt.

### Marked in Systemeinstellungen aktivieren

1. Öffnen Sie **Systemeinstellungen**.
2. Gehen Sie zu **Allgemein → Anmeldeobjekte und Erweiterungen** (auf manchen macOS-Versionen **Datenschutz und Sicherheit → Erweiterungen**).
3. Klicken Sie auf **Erweiterungen** (oder auf **ⓘ** neben Erweiterungen).
4. Wählen Sie **Teilen** (oder **Sharing**).
5. Aktivieren Sie **Marked**.

### Marked zum Teilen-Menü einer App hinzufügen

Auch wenn die Erweiterung systemweit aktiv ist, legt jede App fest, welche Ziele im Teilen-Menü erscheinen:

1. Öffnen Sie eine App mit Teilen-Unterstützung (Finder und TextEdit eignen sich zum Testen).
2. Öffnen Sie das **Teilen**-Menü.
3. Wählen Sie **Erweiterungen bearbeiten…** (auf älteren macOS-Versionen ggf. **Mehr…** oder **Erweiterungsvorgaben…**).
4. Aktivieren Sie unter **Teilen** **Marked**.
5. Ziehen Sie **Marked** optional weiter nach oben, damit es leichter erreichbar ist.

Die Änderungen gelten in den meisten Apps sofort.

## Wenn Marked nicht unter Teilen erscheint

W> Die Share-Erweiterung ist ab Marked 3.1.9 verfügbar. Stellen Sie sicher, dass Sie mindestens diese Version verwenden.

Gehen Sie diese Schritte der Reihe nach durch:

1. **Marked einmal starten** nach Installation oder Update. Beenden und öffnen Sie Marked erneut nach einem Upgrade.
2. **Prüfen Sie, ob die Erweiterung aktiviert ist** in den Systemeinstellungen wie oben beschrieben.
3. **Passen Sie das Teilen-Menü** in der App an, aus der Sie teilen. macOS blendet selten genutzte Ziele aus, bis Sie sie aktivieren.
4. **Mehrere Marked-Kopien:** Sind Direct- und Mac-App-Store-Build installiert, registriert nur die laufende Kopie ihre Erweiterung. Entfernen oder benennen Sie die andere Kopie um und starten Sie die gewünschte.
5. **Mac neu starten**, wenn die Erweiterung nach einem Update weiter fehlt. macOS cached die Registrierung von Share-Erweiterungen.
6. **Marked neu installieren** nach `/Applications`, wenn Sie einen manuell aus Xcode oder einem Image kopierten Build testen. Die Share-Erweiterung muss in `Marked.app/Contents/PlugIns/` eingebettet sein.

## Tipps

- Die Share-Erweiterung eignet sich für schnelle Vorschauen von Web-Ausschnitten, E-Mail-Absätzen oder Notizen ohne neue Datei.
- Für ganze Seiten oder komplexe Browser-Auswahlen bieten die [Browsererweiterungen](Using_the_Browser_Extensions.html) oft mehr Kontrolle (Abschnittsauswahl, Markdownify URL usw.).
- Geteilte Dateien öffnen sich wie normale Marked-Dokumente mit Dateiüberwachung. Geteilter Text öffnet sich als temporäre Vorschau, bis Sie speichern.
