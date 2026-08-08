<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked esporta HTML dalla tua **anteprima live** --- lo stesso output renderizzato che vedi sullo schermo. Utilizza l'esportazione HTML quando hai bisogno di uno snippet da incollare in un blog o CMS oppure in un file `.html` autonomo con stili e immagini incorporati che puoi aprire in qualsiasi browser o host ovunque.

Il flusso di lavoro tipico è **prima l'anteprima, poi l'esportazione dell'HTML**: apri o compila il tuo documento in Marked, scegli un tema, correggi le bozze nell'anteprima live, quindi esporta quando il markup sembra corretto.

## Due modi per ottenere HTML [two-ways-to-get-html]

### Copia HTML (snippet) [copy-html-snippet]

**Copia HTML** inserisce il codice sorgente HTML dell'anteprima negli appunti, pronto per essere incollato in WordPress, Ghost, Squarespace, un forum, un modello di posta elettronica o qualsiasi app che accetti frammenti HTML.

* Menu ingranaggio → **Copia HTML** o {% kbd shift cmd C %} con l'anteprima focalizzata
* Copia il **HTML del corpo renderizzato** (non un documento completo con wrapper `<html>`)
* Facoltativo: attiva **Incorpora immagini durante la copia di HTML** in {% prefspane Export %} per codificare in Base64 le immagini locali come URL `data:` nell'origine incollata

Copia HTML è l'ideale quando la tua destinazione ha già un proprio foglio di stile e hai solo bisogno del markup del contenuto.

### Salva HTML (file) [save-html-file]

**Salva HTML** scrive un file `.html` completo sul disco.

* Esporta → **Salva HTML**, {% kbd cmd S %} o **HTML** dal [Pannello Esporta](Exporting.html#drawer) ({% kbd shift cmd e %})
* Scegli il nome del file e la posizione nella finestra di dialogo di salvataggio
* Configura le opzioni di esportazione nella finestra di dialogo accessoria (vedi sotto)

Salva HTML è ideale per archiviare, condividere un file autonomo o aprire il risultato direttamente in un browser.

## Salva le opzioni HTML [save-html-options]

La finestra di dialogo Salva HTML include un selettore di profili di esportazione e queste opzioni:

![Salva opzioni HTML][savehtml]

**Includi stile nell'output**

Se selezionato, Marked incorpora il CSS del tema di anteprima selezionato in un blocco `<style>` all'interno del file esportato. Scegli un tema integrato o [Stile personalizzato](Custom_Styles.html) dal menu Stile accanto alla casella di controllo. L'output è un documento HTML completo con `<!DOCTYPE html>`, `<head>` e un div `#wrapper` attorno al tuo contenuto --- corrispondente a ciò che hai visualizzato in anteprima.

Se deselezionato, Marked salva un documento HTML minimo solo con il contenuto renderizzato (nessun CSS del tema Marked). Utilizzalo quando desideri che l'HTML non elaborato venga incollato o importato in un altro sistema che fornisce il proprio stile.

**Incorpora immagini locali per HTML autonomo**

Quando **Includi stile nell'output** è abilitato, puoi anche incorporare immagini locali come URL Base64 `data:` all'interno del file HTML. Il risultato è un singolo file che puoi inviare via email, caricare o ospitare senza una cartella `images/` separata.

* Funziona con immagini a cui fanno riferimento **percorsi relativi o assoluti** sul tuo disco locale
* Evita URL `file:///` --- non possono essere incorporati in modo affidabile
* Le immagini remote (http/https) rimangono come URL esterni a meno che non le scarichi prima
* L'incorporamento Base64 può produrre file di grandi dimensioni; usalo quando la portabilità conta più della dimensione del file

**Includi l'evidenziazione della sintassi JavaScript**

Quando l'evidenziazione della sintassi è abilitata in {% prefspane Preview %}, questa opzione aggiunge highlight.js CSS e JavaScript da un CDN in modo che i blocchi di codice mantengano i loro colori nel file esportato. L'HTML esportato necessita di una connessione Internet per il caricamento delle risorse CDN.

**Includi collegamento CDN MathJax o KaTeX**

Quando [MathJax](MathJax.html) o KaTeX è abilitato per l'anteprima, puoi includere gli script CDN corrispondenti nell'HTML salvato in modo che le equazioni vengano visualizzate in un browser. Come l'evidenziazione della sintassi, ciò richiede l'accesso alla rete durante la visualizzazione del file, a meno che non si ospitino personalmente gli script.

**Tipo di esportazione CriticMarkup**

I documenti con [CriticMarkup](CriticMarkup.html) possono scegliere se l'esportazione mostra il testo modificato, il testo originale o il markup completo.

**Esporta profilo**

Seleziona un [Profilo di esportazione](Exporting.html#export-profiles) salvato per ripristinare le tue impostazioni di esportazione HTML preferite (stili incorporati, immagini, evidenziazione della sintassi, matematica) in un solo passaggio.

## Stile con temi integrati e personalizzati [styling-with-built-in-and-custom-themes]

Lo **stile di anteprima** determina l'aspetto HTML quando è selezionato **Includi stile nell'output**:

1. Scegli uno stile dal menu Stile della finestra di anteprima (o imposta uno stile predefinito in {% prefspane Style %}).
2. Controlla la tipografia, i titoli, i blocchi di codice e le immagini nell'anteprima dal vivo.
3. Salva HTML con lo stesso stile selezionato nella finestra di dialogo di esportazione.

Ogni tema Marked integrato --- Swiss, GitHub, Manuscript e il resto --- può essere incorporato. [Stili personalizzati](Custom_Styles.html) e gli stili di [Gestione stili](Custom_Styles.html) funzionano allo stesso modo.

I> Alcuni CSS di sola anteprima (posizionamento fisso, trucchi del viewport, inversione della modalità oscura `@media screen`) potrebbero non essere tradotti uno a uno al di fuori di Marked. Apri il file salvato in un browser per verificarlo prima della pubblicazione.

Per indicazioni sulla creazione, vedere [Creazione di CSS personalizzati](Writing_Custom_CSS.html).

## Metadati e intestazioni MultiMarkdown [metadata-and-multimarkdown-headers]

I metadati MultiMarkdown nella parte superiore del file sorgente possono influire sull'esportazione HTML:

* **`Title:`** --- utilizzato per l'elemento `<title>` durante il salvataggio di un documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- inserisce tag aggiuntivi nel `<head>` esportato (script, tag di collegamento, meta tag)
* Altre chiavi di metadati vengono elaborate in base al tuo [processore Markdown](Choosing_a_Processor.html)

Se utilizzi i metadati per le impostazioni di esportazione ma non vuoi che le chiavi siano visibili in altri output, inseriscile nei commenti HTML --- Marked trova ed elabora i metadati commentati ovunque nel documento. Vedere [Impostazioni per documento](Per-Document_Settings.html).

## Documenti multifile [multi-file-documents]

Per libri e raccolte di capitoli, utilizzare [Documenti multi-file](Multi-File_Documents.html). Marked visualizza l'anteprima del documento unito ed esporta un file HTML dal risultato compilato. I file inclusi sono contrassegnati con commenti HTML che mostrano i loro percorsi di origine --- utili quando si controlla quale capitolo ha contribuito a quale sezione.

## Incollare in altre applicazioni [pasting-into-other-applications]

| Destinazione | Approccio suggerito |
| :-- | :-- |
| Blog/CMS con un proprio tema | **Copia HTML** (snippet, nessun CSS contrassegnato incorporato) |
| Sito statico o archivio | **Salva HTML** con **Includi stile nell'output** |
| E-mail o condivisione di file (un allegato) | **Salva HTML** con **Incorpora immagini locali** |
| WordPress, Ghost, Nozione, ecc. | **Copia HTML**; abilitare **Incorpora immagini durante la copia di HTML** se l'editor non risolve i percorsi locali |
| Ulteriore modifica in un editor di codice | **Salva HTML** senza stile incorporato oppure copia lo snippet e inseriscilo manualmente |

[Copia Rich Text](Exporting.html#rtfexportoptions) (menu a forma di ingranaggio) è un'alternativa quando l'app di destinazione accetta testo formattato anziché origine HTML.

## Argomenti correlati [related-topics]

* [Esportazione](Exporting.html) --- esporta pannello, profili e altri formati
* [Esportazione EPUB](EPUB_Export.html) --- output di ebook con CSS incorporato
* [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html) --- anteprima del flusso di lavoro prima dell'esportazione
* [Stili personalizzati](Custom_Styles.html) e [Impostazioni: Esporta](Settings_Export.html)
* [Impostazioni specifiche HTML](HTML_Specific_Settings.html) --- opzioni del processore per l'output HTML
* [Esportazione AppleScript](AppleScript_Support.html) --- automatizza la copia e il salvataggio di HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r