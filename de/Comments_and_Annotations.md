# <%= @title %>

Marked behandelt Kommentare und Anmerkungen auf besondere Weise.

## Anmerkungsquellen [annotation-sources]

Marked erkennt Kommentare von:

- Markdown-Fußnoten
- CriticMarkup-Kommentare
- Kommentare und Änderungen aus Microsoft Word

## Die Kommentar-Seitenleiste [the-comments-sidebar]

Alle Anmerkungen werden in einer Seitenleiste angezeigt und in der Dokumentvorschau ausgeblendet. Um die Seitenleiste einzublenden, wählen Sie im **Zahnradmenü → Korrekturlesen → Kommentare anzeigen** oder drücken Sie {% kbd ctrl cmd C %}.

![Eine Fußnote in der Kommentar-Seitenleiste][sidebar]

  [sidebar]: images/comment-sidebar-800.jpg @2x width=800

Wenn Sie den Mauszeiger über einen Kommentar in der Seitenleiste bewegen, führt eine Linie zu dessen Position im Dokument. Bei Fußnoten verweist sie auf die Stelle, an der die Fußnote im Text vorkommt. Bei Kommentaren verweist sie auf die ursprüngliche Position des Kommentars, die in der Vorschau auch eine Leerstelle sein kann.

Wenn Sie in der Seitenleiste auf einen Kommentar klicken, hebt eine Animation dessen Position hervor.

Schrift und Gestaltung der Seitenleiste richten sich nach dem aktuellen Stil und können daher je nach Stil unterschiedlich aussehen.
