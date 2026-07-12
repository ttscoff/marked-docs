# <%= @title %>

Rufen Sie den Korrekturlesemodus über das Zahnradmenü auf. Hierbei handelt es sich um eine experimentelle Funktion, die in erster Linie für Redakteure konzipiert ist, die Texte von anderen erhalten und Kommentare abgeben und Feedback geben müssen.

Der Korrekturlesemodus friert Dokumentaktualisierungen ein und verhindert so, dass Anmerkungen und Notizen verloren gehen, wenn das Dokument aktualisiert wird. In der oberen Leiste wird eine rote Anzeige angezeigt, um Sie daran zu erinnern, dass der Korrekturlesemodus aktiv ist.

Tastaturnavigation, Lesezeichen und Schlüsselworthervorhebung sind beim Korrekturlesen alle Funktionen.

## Anmerkungen

Wenn Sie im Korrekturlesemodus Text im Dokument auswählen, wird ein Popup generiert, in dem Sie aus mehreren verschiedenen Hervorhebungstypen auswählen können. Klicken Sie auf die Art der Hervorhebung, die Sie dem Text hinzufügen möchten, oder brechen Sie den Vorgang ab, indem Sie auf die Schaltfläche „Abbrechen“ klicken oder einfach außerhalb des Popups klicken.

## Notizen

![Annotations][1]

[1]: images/Annotating.jpg class=center

Sobald eine Hervorhebung hinzugefügt wurde, können Sie kurze Notizen hinzufügen, indem Sie auf die Hervorhebung klicken. Das Popup enthält nun ein Textfeld, in das Sie beliebige Notizen eingeben können, die für den hervorgehobenen Text relevant sind. Notizen können gelöscht und bearbeitet werden, indem Sie auf eine Markierung klicken, die bereits eine Notiz enthält.

Notizen werden **nur** exportiert, wenn sie in HTML gespeichert werden. Die Markierungen bleiben in den meisten Exportformaten erhalten, einschließlich RTF und PDF.

## Rechtschreibprüfung

Im Korrekturlesemodus können Sie über das Zahnradmenü auf die systemweite Rechtschreibprüfung zugreifen: {% appmenu {{gear}}, Korrekturlesen, Alle Rechtschreibfehler hervorheben %}. Dies ist bei großen Dokumenten langsam und es wird eine Warnung angezeigt, die Sie darauf hinweist, wenn der Vorgang etwa 30 Sekunden dauert. Da die Rechtschreibprüfung in der Webvorschau von Marked nicht funktioniert, ist ein „Hack“ implementiert, damit dies funktioniert, und dieser geht nicht schnell.

Sobald die Rechtschreibprüfung ausgeführt wurde, können Sie das Bedienfeld „Rechtschreibvermutungen“ öffnen, um die Grammatikprüfung zu aktivieren und Vorschläge zur Fehlerbehebung anzuzeigen. Marked *können* diese nicht direkt bearbeiten, Sie müssen zu Ihrem Originaldokument zurückkehren, um die Ergebnisse nutzen zu können.

*Verknüpfungen:* {% kbd ctrl opt cmd S %} führt die Rechtschreibprüfung aus. {% kbd ctrl opt cmd N %} wechselt zum nächsten Fehler im Dokument und {% kbd ctrl opt cmd G %} zeigt das Ratefenster an.