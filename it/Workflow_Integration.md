<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

##AppleScript

Marked include un [dizionario AppleScript](AppleScript_Support.html) completo per l'apertura di file, il controllo dell'anteprima (ricaricamento, scorrimento, evidenziazioni, scorrimento automatico, lettura veloce), la lettura delle statistiche, l'impostazione dei processori, la copia di HTML o RTF, la modifica degli stili di anteprima e l'esportazione in Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF e OPML. **Titoli di anteprima/sommario** tramite AppleScript è [documentato come lavoro in corso](AppleScript_Support.html#table-of-contents-work-in-progress) e non è ancora affidabile.

È possibile scegliere come target l'applicazione, una finestra specifica o un documento. I comandi dell'applicazione includono **apri anteprima streaming**, **anteprima appunti** e **chiudi tutto**. I comandi del documento includono **ottieni statistiche** e **stampa con profilo**. I comandi di esportazione accettano un **profilo** di esportazione facoltativo o un record **`with`** per opzioni come anteprima **stile**, **pageSize** e **margini**. Ad esempio:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Vedi [Supporto AppleScript](AppleScript_Support.html) per l'elenco dei comandi, la abbreviazione dei margini, le note sulla sandbox e i suggerimenti per il debug.

L'integrazione AppleScript consente inoltre ad applicazioni come Tags.app di funzionare direttamente all'interno di Marked.

{% note %}
## Scorciatoie

Contrassegnato include [Azioni scorciatoie] native su macOS 13 o versioni successive. Utilizza **Apri ed esporta file** per flussi di lavoro dal Finder a PDF, **Esporta documento** per tutto ciò che è già aperto in Contrassegnato o **Imposta stile anteprima** per modificare i temi prima dell'esportazione. Le azioni di esportazione accettano **profili**, anteprima **stili** e opzioni come **dimensione pagina**, **margini** e **dimensione carattere** (stessa semantica dei record AppleScript `with`).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## Gestore URL

Il [gestore URL contrassegnato] [urlhandler] consente un'integrazione estesa semplicemente chiamando gli URL, da AppleScript o con un comando di base `open` in uno script di shell.

## Pacchetto bonus contrassegnato

Il Marked Bonus Pack è una raccolta di script, comandi e servizi. Alcuni funzionano con più editor, altri sono specifici per determinati editor. I Servizi generalmente funzioneranno con qualsiasi editor che disponga delle capacità necessarie. Il resto è organizzato in cartelle in base all'applicazione con cui lavorano.

Puoi scaricare il Bonus Pack e trovare le istruzioni per installarlo e utilizzarlo in questo [articolo della knowledge base](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html