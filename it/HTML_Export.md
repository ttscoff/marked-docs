# <%= @title %>

Marked esporta HTML dalla tua **anteprima live** --- lo stesso output visualizzato a schermo. Usa l'esportazione HTML quando ti serve uno snippet da incollare in un blog o in un CMS, oppure un file `.html` autonomo con stili e immagini incorporati, che puoi aprire in qualsiasi browser o ospitare ovunque.

Il flusso di lavoro tipico è **prima l'anteprima, poi l'esportazione HTML**: apri o compila il documento in Marked, scegli un tema, rileggi nell'anteprima live, quindi esporta quando il markup ti sembra corretto.

## Due modi per ottenere HTML [two-ways-to-get-html]

### Copia HTML (snippet) [copy-html-snippet]

**Copia HTML** mette il codice sorgente HTML dell'anteprima negli appunti --- pronto da incollare in WordPress, Ghost, Squarespace, un forum, un modello di email o qualsiasi app che accetti frammenti HTML.

* Menu Gear → **Copia HTML**, oppure {% kbd shift cmd C %} con l'anteprima attiva
* Copia l'**HTML del corpo renderizzato** (non un documento completo con wrapper `<html>`)
* Opzionale: attiva **Incorpora immagini durante la copia HTML** in {% prefspane Export %} per codificare in Base64 le immagini locali come URL `data:` nel sorgente incollato

Copia HTML è ideale quando la destinazione ha già un proprio foglio di stile e ti serve solo il markup del contenuto.

### Salva HTML (file) [save-html-file]

**Salva HTML** scrive su disco un file `.html` completo.

* Esporta → **Salva HTML**, {% kbd cmd S %}, oppure **HTML** dal [pannello di esportazione](Exporting.html#drawer) ({% kbd shift cmd e %})
* Scegli nome file e posizione nella finestra di salvataggio
* Configura le opzioni di esportazione nell'accessorio della finestra di dialogo (vedi sotto)

Salva HTML è ideale per archiviare, condividere un file autonomo o aprire il risultato direttamente in un browser.

## Opzioni di Salva HTML [save-html-options]

La finestra di dialogo Salva HTML include un selettore di profilo di esportazione e queste opzioni:

![Opzioni Salva HTML][savehtml]

**Includi stile nell'output**

Se selezionata, Marked incorpora il CSS del tema di anteprima scelto in un blocco `<style>` all'interno del file esportato. Scegli un tema integrato qualsiasi oppure uno [Stile personalizzato](Custom_Styles.html) dal menu degli stili accanto alla casella. L'output è un documento HTML completo con `<!DOCTYPE html>`, `<head>` e un div `#wrapper` attorno al contenuto --- corrispondente a ciò che hai visto in anteprima.

Se deselezionata, Marked salva un documento HTML minimale con solo il contenuto renderizzato (senza il CSS del tema di Marked). Usa questa opzione quando vuoi HTML grezzo da incollare o importare in un altro sistema che fornisce già il proprio stile.

**Incorpora immagini locali per HTML autonomo**

Quando **Includi stile nell'output** è attiva, puoi anche incorporare le immagini locali come URL Base64 `data:` all'interno del file HTML. Il risultato è un unico file che puoi inviare via email, caricare o ospitare senza una cartella `images/` separata.

* Funziona con immagini referenziate tramite **percorsi relativi o assoluti** sul disco locale
* Evita gli URL `file:///` --- non possono essere incorporati in modo affidabile
* Le immagini remote (http/https) restano come URL esterni, a meno che tu non le scarichi prima
* L'incorporamento in Base64 può produrre file di grandi dimensioni; usalo quando la portabilità conta più della dimensione del file

**Includi JavaScript per l'evidenziazione della sintassi**

Quando l'evidenziazione della sintassi è attiva in {% prefspane Preview %}, questa opzione aggiunge il CSS e il JavaScript di highlight.js da una CDN, così i blocchi di codice mantengono i loro colori nel file esportato. L'HTML esportato richiede una connessione a Internet per caricare le risorse dalla CDN.

**Includi link CDN per MathJax o KaTeX**

Quando [MathJax](MathJax.html) o KaTeX sono attivi per l'anteprima, puoi includere gli script CDN corrispondenti nell'HTML salvato, così le equazioni vengono renderizzate in un browser. Come per l'evidenziazione della sintassi, questo richiede l'accesso alla rete quando si visualizza il file, a meno che tu non ospiti gli script tu stesso.

**Tipo di esportazione CriticMarkup**

I documenti con [CriticMarkup](CriticMarkup.html) possono scegliere se l'esportazione mostra il testo modificato, il testo originale o il markup completo.

**Profilo di esportazione**

Seleziona un [profilo di esportazione](Exporting.html#export-profiles) salvato per ripristinare in un solo passaggio le impostazioni di esportazione HTML preferite (stili incorporati, immagini, evidenziazione della sintassi, formule matematiche).

## Applicare stili con temi integrati e personalizzati [styling-with-built-in-and-custom-themes]

Lo **stile di anteprima** determina l'aspetto dell'HTML quando **Includi stile nell'output** è selezionata:

1. Scegli uno stile dal menu degli stili della finestra di anteprima (oppure imposta uno stile predefinito in {% prefspane Style %}).
2. Rivedi tipografia, intestazioni, blocchi di codice e immagini nell'anteprima live.
3. Salva l'HTML con lo stesso stile selezionato nella finestra di esportazione.

Ogni tema integrato di Marked --- Swiss, GitHub, Manuscript e gli altri --- può essere incorporato. Gli [Stili personalizzati](Custom_Styles.html) e gli stili dello [Style Manager](Custom_Styles.html) funzionano allo stesso modo.

Il **CSS aggiuntivo** da {% prefspane Style %} viene incluso nell'esportazione HTML quando gli stili sono incorporati. L'`<body>` esportato riceve la classe `mk-has-additional-css`, così i selettori CSS aggiuntivi riscritti da Marked corrispondono correttamente. Vedi [Creare CSS personalizzato](Writing_Custom_CSS.html#additional-css-settings).

I> Alcuni CSS validi solo in anteprima (posizionamento fisso, trucchi legati al viewport, inversione della Modalità scura `@media screen`) potrebbero non tradursi uno a uno al di fuori di Marked. Apri il file salvato in un browser per verificare prima di pubblicarlo.

Per indicazioni sulla scrittura, vedi [Creare CSS personalizzato](Writing_Custom_CSS.html).

## Metadati e intestazioni MultiMarkdown [metadata-and-multimarkdown-headers]

I metadati MultiMarkdown all'inizio del file sorgente possono influire sull'esportazione HTML:

* **`Title:`** --- usato per l'elemento `<title>` quando si salva un documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- inietta tag aggiuntivi nell'`<head>` esportato (script, tag link, meta tag)
* Le altre chiavi di metadati vengono elaborate in base al [processore Markdown](Choosing_a_Processor.html) in uso

Se usi metadati per le impostazioni di esportazione ma non vuoi che le chiavi siano visibili negli altri output, racchiudile in commenti HTML --- Marked trova ed elabora i metadati commentati ovunque nel documento. Vedi [Impostazioni per singolo documento](Per-Document_Settings.html).

## Documenti multi-file [multi-file-documents]

Per libri e raccolte di capitoli, usa i [Documenti multi-file](Multi-File_Documents.html). Marked visualizza in anteprima il documento unito ed esporta un unico file HTML a partire dal risultato compilato. I file inclusi vengono contrassegnati con commenti HTML che ne mostrano il percorso di origine --- utile per verificare quale capitolo ha contribuito a quale sezione.

## Incollare in altre applicazioni [pasting-into-other-applications]

| Destinazione | Approccio consigliato |
| :-- | :-- |
| Blog / CMS con tema proprio | **Copia HTML** (snippet, senza CSS di Marked incorporato) |
| Sito statico o archivio | **Salva HTML** con **Includi stile nell'output** |
| Email o condivisione file (un allegato) | **Salva HTML** con **Incorpora immagini locali** |
| WordPress, Ghost, Notion, ecc. | **Copia HTML**; attiva **Incorpora immagini durante la copia HTML** se l'editor non risolve i percorsi locali |
| Ulteriore modifica in un editor di codice | **Salva HTML** senza stile incorporato, oppure copia lo snippet e racchiudilo manualmente |

[Copia testo formattato](Exporting.html#rtfexportoptions) (menu Gear) è un'alternativa quando l'app di destinazione accetta testo formattato invece del sorgente HTML.

## Argomenti correlati [related-topics]

* [Esportazione](Exporting.html) --- pannello di esportazione, profili e altri formati
* [Esportazione EPUB](EPUB_Export.html) --- output ebook con CSS incorporato
* [Anteprima Markdown live su Mac](Live_Markdown_Preview_on_Mac.html) --- flusso di anteprima prima dell'esportazione
* [Stili personalizzati](Custom_Styles.html) e [Impostazioni: Esportazione](Settings_Export.html)
* [Impostazioni specifiche per HTML](HTML_Specific_Settings.html) --- opzioni del processore per l'output HTML
* [Esportazione via AppleScript](AppleScript_Support.html) --- automatizza la copia e il salvataggio HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
