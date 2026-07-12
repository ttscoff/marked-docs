# <%= @title %>

Speed Read ist ein Lesemodus im RSVP-Stil, der jeweils ein Wort in einem fokussierten Overlay anzeigt.

## So funktioniert Speed Read

Speed Read verwendet eine Methode namens **Rapid Serial Visual Presentation** (RSVP). Anstatt Ihren Blick über Textzeilen zu bewegen, erscheinen die Wörter an einer festen Position. Dadurch werden die Augenbewegungen, Zeilenwechsel und Rücksprünge reduziert, die normalerweise beim Lesen auftreten – das eignet sich zum Überfliegen, zum Wiederholen von vertrautem Material oder zum schnellen Durchgehen von Texten, ohne den Überblick zu verlieren.

Die Methode ist keine Zauberei und garantiert kein besseres Verständnis bei sehr hohen Geschwindigkeiten. Das Leseverständnis hängt weiterhin von der Komplexität des Textes, Ihrer Vertrautheit mit dem Thema und der WPM-Einstellung ab. Bei dichtem oder unbekanntem Material ist eine mäßige Geschwindigkeit in der Regel effektiver als eine möglichst hohe Geschwindigkeit.

Der rote Buchstabe markiert den visuellen Ankerpunkt des Wortes, der manchmal auch **optimaler Erkennungspunkt** genannt wird. Bei vielen Wörtern erkennen Leser das Wort am effizientesten, wenn ihr Blick leicht links von der Mitte landet und nicht auf dem ersten Buchstaben. Indem dieser Ankerpunkt an der gleichen Stelle bleibt und hervorgehoben wird, gibt Speed Read Ihrem Auge ein konsistentes Ziel. Das Ergebnis ist weniger Neufokussierung zwischen den Wörtern und ein gleichmäßigerer Rhythmus, während der Text fortschreitet.

## Speed Read öffnen

Verwenden Sie **Vorschau > Speed Read**, den Eintrag **Speed Read** im Zahnradmenü des Vorschaufensters, oder drücken Sie {% kbd ctrl opt S %}. Der Menüpunkt ist verfügbar, wenn ein Markdown-Vorschaufenster aktiv ist (er ist für Rohvorschauen von HTML deaktiviert und wenn kein Dokument geöffnet ist).

Wenn Speed Read geöffnet wird, startet es im angehaltenen Zustand, sodass Sie sich vor Beginn der Wiedergabe orientieren können.

<video controls preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Ihr Browser unterstützt das Speed-Read-Demovideo nicht.
</video>
<p><em>Speed-Read-Overlay mit Wiedergabesteuerung, Synchronisierungsoption und Hilfezugriff.</em></p>

## Overlay-Steuerelemente

Sobald das Overlay sichtbar ist, sind diese Tasten verfügbar:

| Tastenkombination | Funktion |
| :-- | :-- |
| {% kbd space %} | Wiedergabe/Pause |
| {% kbd [ %} | Zum Absatzanfang springen (erneut drücken, um zum vorherigen Absatz zu gelangen) |
| {% kbd ] %} | Zum Anfang des nächsten Absatzes springen |
| {% kbd left %} | Lesegeschwindigkeit (WPM) verringern |
| {% kbd right %} | Lesegeschwindigkeit (WPM) erhöhen |
| {% kbd esc %} | Speed Read beenden |

Die eckigen Klammern werden für die Absatznavigation abgefangen und die Links-/Rechts-Pfeiltasten für Geschwindigkeitsänderungen, sodass diese Tasten keine Vorschau-Navigation auslösen, solange Speed Read geöffnet ist. Sie können auch auf die kreisförmige Schaltfläche **X** in der oberen linken Ecke des Overlays klicken, um es zu schließen.

Andere normale Tastenkombinationen für die Vorschau-Navigation funktionieren weiterhin, während Speed Read aktiv ist, einschließlich `t`/`gg` (Anfang), `G`/`b` (Ende) und `,`/`.` (Überschriften-Navigation). Die vollständige Liste finden Sie unter [Vorschau-Navigation](Keyboard_Shortcuts#preview-navigation).

Das Inhaltsverzeichnis kann auch verwendet werden, während Speed Read aktiv ist. Drücken Sie {% kbd cmd t %}, um es zu öffnen und darin zu navigieren, oder drücken Sie {% kbd f %}, um sofort die Schnellsuche zu fokussieren und in den Überschriften des Dokuments zu navigieren.

## Mit einer Auswahl starten

Wenn beim Starten von Speed Read in der Vorschau Text ausgewählt ist, verwendet die Wiedergabe den ausgewählten Text. Wenn keine Auswahl aktiv ist, verwendet Speed Read den vollständigen Dokumenttext.

## Synchronisierung mit der Scroll-Position

Aktivieren Sie **Speed Reading mit Scroll-Position synchronisieren** unter {% prefspane Preview %} oder verwenden Sie das Kontrollkästchen im Speed-Read-Overlay, um die Vorschau und die Speed-Read-Position zusammenzuhalten.

Wenn diese Option aktiviert ist, beginnt Speed Read mit dem aktuell oben in der Vorschau sichtbaren Inhalt und nicht am Anfang des Dokuments. Während die Wiedergabe fortschreitet, scrollt die Vorschau zusammen mit den angezeigten Wörtern.

Wenn Sie Speed Read schließen, durch die Vorschau scrollen und das Overlay erneut öffnen, beginnt die Wiedergabe an der neuen sichtbaren Position. Wenn Sie das Kontrollkästchen im Overlay aktivieren, nachdem Speed Read bereits geöffnet ist, wird die Wiedergabe auf die aktuelle Scroll-Position zurückgesetzt und von dort aus fortgesetzt.

## Gespeicherte Geschwindigkeit

Der WPM-Wert wird automatisch gespeichert, wenn Sie ihn mit {% kbd ← %} und {% kbd → %} ändern. Ihre gewählte Geschwindigkeit wird bei der nächsten Verwendung von Speed Read wiederhergestellt.
