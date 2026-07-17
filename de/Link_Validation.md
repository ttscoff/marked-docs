# <%= @title %>

Die Linkvalidierung ruft das Ziel einer URL auf und prüft es auf Fehler. So vermeiden Sie defekte und ungültige Links in veröffentlichten Dokumenten – besonders hilfreich ist das für Blogger.

## Einzelne Links validieren [validating-single-links]

![][1]

   [1]: images/validate_single.png @2x width=832px height=267px class=center

Klicken Sie in der Vorschau auf einen Link und halten Sie ihn gedrückt, bis er blinkt. Lassen Sie ihn dann los, um das Link-Aktionsmenü zu öffnen. Wählen Sie „Link validieren“, um den Test auszuführen. Die Ergebnisse werden im Popup angezeigt.

## Validierung aller Links [validating-all-links]

![][2]

   [2]: images/screenshots/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Wählen Sie im Zahnradmenü oder im Kontextmenü „Alle Links validieren“ (Tastaturkurzbefehl {% kbd ctrl cmd L %}). Alle externen Links im Dokument werden geprüft und die Ergebnisse in einem Popup angezeigt. Wenn Sie dort auf einen Link klicken, scrollt Marked zum entsprechenden Link im Dokument und hebt ihn hervor.

Mit der Schaltfläche „Gültige ausblenden“ oben im Popup können Sie gültige URLs ausblenden. Dann werden nur URLs angezeigt, die einen Fehlerstatus zurückgegeben haben.

Mit der Esc-Taste blenden Sie die Validierungsergebnisse aus. Über {% kbd ctrl cmd L %} oder das Zahnradmenü können Sie sie erneut anzeigen.

## Automatische Validierung [validating-automatically]

Aktivieren Sie unter den Vorschau-Einstellungen (oder unten im Popup zur Linkvalidierung) „URLs beim Aktualisieren automatisch validieren“. Beim Laden des Dokuments werden die enthaltenen Links im Hintergrund geprüft. Ein Dialog erscheint nur, wenn Fehler vorliegen.

Um das Popup zu deaktivieren, schalten Sie die Option in den Einstellungen aus oder deaktivieren Sie das Kontrollkästchen unten im Popup-Fenster.
