# <%= @title %>

Rendering-Geschwindigkeit und Leistung von Marked können je nach Einstellungen und Art des Dokumentinhalts stark schwanken. Mehrere Faktoren können langsames Rendern oder lange Verzögerungen verursachen:

* **Time Machine.** Wenn Time Machine ausgeführt wird und auf Ihrem System viel Festplattenaktivität auftritt, reagiert Marked möglicherweise langsamer auf Änderungen in Ihrem Dokument. Die Verarbeitungsgeschwindigkeit wird dadurch nicht beeinflusst, lediglich die Reaktionszeit.
* **Ein Markdown-Dokument mit viel HTML rendern.** Das dauert grundsätzlich länger. Discount kommt damit etwas besser zurecht als MultiMarkdown; wenn Sie also viel HTML haben, können Sie den Standardprozessor wechseln (**Haken:** Sie verlieren Fußnoten und einige andere MultiMarkdown-Funktionen).
* **Viele eingebundene Dateien.** Ob Code-Includes oder eine Index-/Merge-Datei – alle Teile einzusammeln kostet Marked einen Moment. Dasselbe gilt für große Scrivener-Dokumente. Daran lässt sich wenig ändern; Marked gibt sein Bestes, um mit der von Ihnen gewählten Dokumentstruktur Schritt zu halten.
* **Zustand der Festplatte.** Ist Ihre Festplatte fast voll, der Spotlight-Index beschädigt oder wurden die Zugriffsrechte länger nicht repariert, erkennt Marked die Änderungen an der überwachten Datei möglicherweise schwerer. Das Laufwerk zu optimieren und die Zugriffsrechte zu reparieren hilft oft, und ein neu aufgebauter Spotlight-Index behebt viele Marked-Probleme.
