# <%= @title %>

{% apponly div %}
*Für die neueste Version dieser Dokumentation besuchen Sie die [Online-Version][help].*
{% endapponly %}

**Sehen Sie sich unbedingt die wachsende Sammlung von [Marked-Tutorial-Videos](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ) an.**

## Was ist Markdown?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown ist eine grundlegende Auszeichnungssprache, die einfache Symbole verwendet und es Ihnen ermöglicht, HTML (und den Export in andere Formate) mit einfacher Syntax wie `*kursiv*` und `**fett**` zu schreiben. Markdown wurde von John Gruber erfunden und entwickelt sich rasant zum De-facto-Standard für Web-Publishing, Notizen und sogar Buchveröffentlichungen. Es lässt Sie ohne einen Haufen Symbolleisten und Formatierungsgefummel schreiben, sodass Sie einfach Wörter auf die Seite bringen und Ihre Prozessoren (wie Marked) das Styling und die Formatierung übernehmen lassen können.

Marked funktioniert mit GitHub Flavored Markdown, CommonMark (GFM), Kramdown und MultiMarkdown und kann Syntax aus mehreren Varianten für die Vorschau konvertieren (es kann auch so erweitert werden, dass es mit fast jedem Prozessor funktioniert, den Sie benötigen, einschließlich Textile, reStructuredText, Wikitext und mehr). Ich gehe davon aus, dass Sie – da Sie hier sind – wissen, was mindestens eine dieser Auszeichnungssprachen ist. Wenn nicht, sollten Sie bei John Grubers [Markdown Basics][daringfireball] beginnen und sich [MarkdownGuide.org][mdguide] ansehen. Marked enthält im Hilfemenü eine vollständige Anleitung zur Markdown-Syntax.

Sie können den [Markdown Dingus](x-marked-3://dingus) verwenden, um mit den verschiedenen Markdown-Varianten zu experimentieren, die Marked unterstützt.

## Was ist Marked?

Marked ist eine Live-Markdown-Vorschau-App für macOS – eine editorunabhängige (Multi)Markdown-Vorschau-Anwendung, die eine Datei auf Änderungen überwacht und die Vorschau bei jedem Speichern aktualisiert. Durch die Trennung und Automatisierung der Formatierungsdetails können Sie sich mehr auf das Schreiben und weniger auf die Präsentation konzentrieren, während Sie gleichzeitig Ihr Endprodukt im Auge behalten.

Für Setup-Workflows und editorspezifische Schnellstarts siehe [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html). Für eine kürzere Produktübersicht besuchen Sie [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked funktioniert mit jeder lokal zugänglichen Datei, einschließlich iCloud-Dokumenten. Ziehen Sie einfach ein Textdokument aus der Symbolleiste eines beliebigen Editors auf Marked, und es wird als HTML-Vorschau gerendert, beginnt mit der Verfolgung von Änderungen und aktualisiert die Vorschau, während Sie schreiben. Es kann sogar [mehrteilige Dokumente](Multi-File_Documents.html) mit einer einfachen „Include“-Syntax oder aus Scrivener-, Leanpub- und mmd_merge-Indexformaten kompilieren.

Marked verfügt über zusätzliche Funktionen, einschließlich Wortzahl und anderer Dokumentstatistiken, der Möglichkeit, über anderen Anwendungen zu schweben oder im Hintergrund abzudunkeln, und es kann Ihre Arbeit in einer Vielzahl von gut gestalteten Stilen anzeigen. Es kann Dokumente als Druck oder PDF, Word-Dokument, vollständiges HTML-Dokument (einschließlich Stilen und Bildern) ausgeben oder den HTML-Quellcode oder RTF-Daten mit einem Tastendruck in Ihre Zwischenablage kopieren. Marked verfügt außerdem über ein grundlegendes AppleScript-Wörterbuch und einen [URL-Handler](URL_Handler.html), die die Integration in Ihren Workflow erleichtern.

Ach ja, und es funktioniert mit einer Menge Ihrer Lieblings-Apps: Texteditoren von Vim und Emacs bis Sublime Text und TextMate, Markdown-Editoren wie MultiMarkdown Composer, Byword und iA Writer, sogar mit Apps, die Sie vielleicht nicht erwarten, wie Ulysses, Scrivener, VoodooPad, MarsEdit und mehr.

## Anwendungsbeispiele

Marked verwandelt jeden Texteditor in einen Markdown-fähigen Editor. Ihre Vorschau ist immer verfügbar und wird aktualisiert, während Sie arbeiten.

* Wenn Ihr Lieblingseditor keine Live-Markdown-Vorschau bietet, öffnen Sie das Dokument, an dem Sie arbeiten, in Marked und lassen Sie das Fenster an die Seite schweben, um ein voll funktionsfähiges Markdown-Schreiberlebnis zu erhalten.
* Schreiben oder bloggen Sie gerne in MacVim oder einem anderen terminalbasierten Editor? Jetzt haben Sie eine synchronisierte Markdown-Vorschau, während Sie arbeiten.
* Marked bietet außerdem Anzeigefunktionen, die über jede bestehende Markdown-Vorschau hinausgehen, und kann an deren Stelle verwendet werden, um vollständige Wortzahlen und Dokumentstatistiken sowie Schreibvorschläge bereitzustellen und sogar Fehler in Ihrer Markdown-Formatierung hervorzuheben.
* Sie können Marked auch ohne Editor verwenden. Ziehen Sie Markdown-Dateien einfach auf das Symbol, um sie in der Vorschau anzuzeigen, zu drucken und in PDF, DOC, RTF oder HTML-Quellcode zu exportieren. Marked kann auch **`.rtf`- und `.rtfd`-Dateien** als Quelldokumente öffnen ([RTF- und RTFD-Unterstützung](RTF_Support.html)).
* In Apps, die automatisch speichern, werden Sie feststellen, dass die Vorschau ohne jegliche Hilfe mit Ihrem Schreiben Schritt hält. Verwenden Sie es mit jedem Editor … oder mit *allen* Ihren Editoren.
* Sie schreiben ein Buch? Marked kann mehrere Dateien für eine vollständige Vorschau Ihrer Arbeit kompilieren und diese enthaltenen Dateien sogar auf Änderungen überwachen, wobei das Hauptdokument bei jedem Speichern aktualisiert wird. Es kann sogar einen ganzen Ordner auf Änderungen überwachen und die Vorschau automatisch auf die Datei umschalten, die Sie gerade aktualisieren. Wenn Sie fertig sind, können Sie in den Formaten EPUB, DOCX oder TextBundle veröffentlichen.
* Sie arbeiten mit einer KI-Programmierplattform? Öffnen Sie einen Plan- oder Dokumentationsordner in Marked, und wann immer sich eine Markdown-Datei in diesem Ordner ändert, wird Marked sie anzeigen und automatisch zu dem Punkt der letzten Bearbeitung scrollen. Marked zeigt Mermaid-Diagramme an und kann mit allen Arten von erweiterter Syntax umgehen. Behalten Sie den Überblick über Pläne und Dokumentationen, während Sie arbeiten, ohne zwischen Dateien wechseln zu müssen.
