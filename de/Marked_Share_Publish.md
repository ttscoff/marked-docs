# <%= @title %>

**Marked Share** ist Markeds Online-Veröffentlichungsdienst unter [share.markedapp.com](https://share.markedapp.com). Sie verbinden Ihren Mac einmalig und veröffentlichen anschließend das vorderste Dokument als **TextPack** mit Bildern und wahlweise den Hervorhebungen aus dem Lesemodus. Wer den Link hat, kann das Dokument im Web ansehen.

Die vollständige Web-Dokumentation mit Details zu Hervorhebungs-Sets, Leser-Rezensionen, Passwörtern und der API-Referenz finden Sie in der [Marked Share-Dokumentation](https://share.markedapp.com/docs).

Diese Funktion ist etwas anderes als die macOS-**Share-Erweiterung** (das Teilen-Menü des Systems). Wie Sie Dateien oder Textauswahlen aus anderen Apps an Marked senden, steht unter [Share-Erweiterung](Share_Extension.html).

## Konto verbinden [connect-your-account]

Bevor Sie zum ersten Mal veröffentlichen, verbinden Sie Marked mit Ihrem Share-Konto:

1. Wählen Sie {% appmenu Ablage, Veröffentlichen, Konto verbinden… %}.
2. Marked öffnet Ihren Standardbrowser zur Anmeldung bei [share.markedapp.com](https://share.markedapp.com).
3. Sobald Sie die Verbindung bestätigt haben, kehrt der Browser mit einem sicheren Anmeldelink zu Marked zurück. Prüfen Sie die im Dialog angezeigte Kontobezeichnung.

Marked legt den API-Token und den Geräteschlüssel im Schlüsselbund von macOS auf diesem Mac ab. Zugangsdaten landen weder in Protokollen noch in Absturzberichten.

Zum Trennen wählen Sie {% appmenu Ablage, Veröffentlichen, Konto trennen… %}. Veröffentlichte Dokumente bleiben online; den Zugriff widerrufen Sie bei Bedarf jederzeit in den [Marked Share-Einstellungen](https://share.markedapp.com/settings).

## Dokument veröffentlichen [publish-a-document]

Ist ein Dokument in der Vorschau geöffnet, wählen Sie {% appmenu Ablage, Veröffentlichen, Veröffentlichen… %}.

Beim ersten Veröffentlichen eines Dokuments zeigt Marked ein Dialogblatt mit Optionen:

- **Titel** – erscheint auf Share (standardmäßig der Dokumentname ohne Dateiendung).
- **Sichtbarkeit** – Privat, Nicht gelistet oder Öffentlich. Neue Veröffentlichungen sind standardmäßig **Nicht gelistet** (über den Link erreichbar, aber nicht öffentlich aufgeführt). Dokumente, die zu öffentlichen Sammlungen hinzugefügt werden, werden automatisch auf **Öffentlich** gesetzt.
- **Sammlung** – wählt eine vorhandene Sammlung, in der das Dokument erscheinen soll; mit **Neue Sammlung erstellen…** legen Sie eine im Browser an.
- **Lesestil** – Editorial, Manuscript, Swiss, Contrast, Typewriter oder **Keine**. Wenn möglich, übernimmt Marked den Vorschaustil des Dokuments. Share behandelt die Angabe als Vorschlag; Lesende können sie überschreiben. Mit **Keine** veröffentlichen Sie ohne Stilvorschlag.
- **Hervorhebungen und Kommentare einschließen** – bettet die Hervorhebungen des Lesemodus in das TextPack ein. Standardmäßig aktiv, wenn das Dokument Hervorhebungen enthält.
- **Remix durch andere erlauben** – ist die Option aktiv, können Lesende auf Share eine eigene Fassung des Dokuments anlegen.

Marked baut das TextPack im Hintergrund (Markdown, Assets und optional `highlights.json`), lädt es hoch und merkt sich die Share-URL auf diesem Mac.

### In Sammlung veröffentlichen [publish-to-collection]

Um ein Dokument direkt in einer bestimmten Sammlung zu veröffentlichen, wählen Sie {% appmenu Ablage, Veröffentlichen, In Sammlung veröffentlichen %} und darin Ihre Sammlung aus dem Untermenü.

Über das Menü können Sie auch direkt **Neue Sammlung erstellen…**, **Sammlungen verwalten…** oder **Domains verwalten…** aufrufen, um Ihre Sammlungen auf [share.markedapp.com](https://share.markedapp.com) zu konfigurieren.

### Bestehende Veröffentlichung aktualisieren [update-an-existing-publish]

Sobald ein Dokument mit Share verknüpft ist, heißt der Menüpunkt **Veröffentlichtes Dokument aktualisieren** statt **Veröffentlichen…**. Damit laden Sie eine neue TextPack-Fassung hoch. Marked schickt den Inhalts-Hash des Servers mit, sodass gleichzeitige Änderungen von einem anderen Mac oder aus dem Web erkannt werden.

Hat jemand anderes das Dokument auf Share zuerst aktualisiert, fragt Marked, ob Sie mit der Fassung dieses Macs **Überschreiben**, das Dokument **Im Web öffnen** oder **Abbrechen** möchten.

## Auf Micro.blog veröffentlichen [post-to-microblog]

Wenn Sie Ihr Micro.blog-Konto in den [Marked Share-Einstellungen](https://share.markedapp.com/settings) verbunden haben, können Sie veröffentlichte Dokumente direkt auf Micro.blog syndizieren:

1. Veröffentlichen Sie das Dokument zuerst auf Marked Share.
2. Wählen Sie {% appmenu Ablage, Veröffentlichen, Auf Micro.blog veröffentlichen… %}.
3. Wählen Sie das Beitragsformat:
   - **Vollständiges Dokument** – überträgt den gesamten Markdown-Inhalt in Ihren Blog.
   - **Zusammenfassung mit Link** – veröffentlicht einen kurzen Auszug mit Link zu Ihrem Marked Share-Dokument.
4. Klicken Sie auf **Veröffentlichen**. Marked überträgt den Beitrag und bietet an, den Link direkt zu kopieren oder den Beitrag im Browser zu öffnen.

Bereits veröffentlichte Dokumente können Sie auch per Rechtsklick im Fenster **Veröffentlichte Dokumente** auf Micro.blog übertragen.

## Nach dem Veröffentlichen [after-publishing]

Ist die Veröffentlichung abgeschlossen, bestätigt Marked den Erfolg und bietet an:

- **Share-Link kopieren** – {% appmenu Ablage, Veröffentlichen, Share-Link kopieren %}
- **Im Web öffnen** – {% appmenu Ablage, Veröffentlichen, Im Web öffnen %}

Diese Befehle gelten für das vorderste Dokument, sofern dafür eine Veröffentlichung hinterlegt ist.

## Fenster „Veröffentlichte Dokumente“ [published-documents-window]

Mit {% appmenu Ablage, Veröffentlichen, Veröffentlichte Dokumente… %} öffnen Sie eine Liste der Dokumente, die von diesem Mac veröffentlicht und aus Ihrem Share-Konto synchronisiert wurden. Zu jedem Eintrag stehen Ihnen zur Verfügung:

- **Suchen** – durchsucht Titel, lokale Dateipfade und Dokumentinhalte über das Suchfeld oben im Fenster, mit Textauszügen während der Eingabe.
- **Öffnen** – ruft die lokale Datei auf, solange Marked sie noch auf dem Datenträger findet.
- **Aus Marked Share importieren…** – lädt das TextPack herunter, wenn keine lokale Datei existiert, damit Sie es lokal sichern und bearbeiten können.
- **Im Web öffnen** oder **Share-Link kopieren** – öffnet den Web-Link des Dokuments oder kopiert ihn.
- **Auf Micro.blog veröffentlichen…** / **Auf Micro.blog öffnen** – überträgt das Dokument auf Micro.blog oder öffnet einen bestehenden syndizierten Beitrag.
- **Vergessen** – entfernt die lokale Verknüpfung von diesem Mac, ohne das Dokument online zu löschen.

Solange Sie verbunden sind, aktualisiert sich die Liste aus Share. Sind Sie offline oder nicht verbunden, zeigt Marked die zwischengespeicherten Einträge und fordert Sie gegebenenfalls auf, die Verbindung wiederherzustellen.

## Was sich veröffentlichen lässt [what-you-can-publish]

Veröffentlichen können Sie jedes Dokument, das Marked darstellen kann, darunter:

- gespeicherte Markdown- und Textdateien
- temporäre Vorschauen (Zwischenablage, Streaming oder ungespeicherte Dokumente)
- TextBundles und andere unterstützte Formate

Pro Dokumentfenster läuft immer nur eine Veröffentlichung; während des Hochladens ist der Menüpunkt deaktiviert.

## Tipps [tips]

- Beim Veröffentlichen kommen die Bilder mit, auf die die Vorschau verweist. Sehr große Pakete werden unter Umständen schon vor dem Hochladen abgewiesen; verringern Sie in dem Fall die eingebetteten Assets.
- Die im TextPack exportierten Hervorhebungen liegen in Markeds JSON-Format für Hervorhebungen vor. Wie Sie Hervorhebungen anlegen und exportieren, steht unter [Lesemodus](Reading_Mode.html).
- Marked Share ist in den Direct-, Mac-App-Store-, Setapp- und Marked-Pro-Builds enthalten. Für das Veröffentlichen ist kein separates Abonnement nötig.
