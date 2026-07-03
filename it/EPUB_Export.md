<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked esporta file EPUB completamente conformi dall'anteprima Markdown, con gli stessi temi integrati e personalizzati che usi sullo schermo e leggibili in **Apple Books**, **Kobo** e altri lettori EPUB standard.

Il flusso di lavoro tipico è **prima l'anteprima, poi l'esportazione dell'EPUB**: apri o compila il documento in Marked, scegli un tema, correggi le bozze nell'anteprima live, quindi esporta quando il libro è pronto.

## Esportazione di un EPUB

Apri il [Pannello di esportazione](Exporting.html#drawer) ({% kbd shift cmd e %}) o utilizza **Salva con nome** dal menu a forma di ingranaggio e scegli **EPUB**.

La finestra di dialogo di salvataggio dell'EPUB ti consente di impostare:

* **Titolo** --- per impostazione predefinita vengono utilizzati i metadati MultiMarkdown o il nome del file
* **Autore** --- per impostazione predefinita è il nome utente di macOS; l'ultimo autore inserito verrà ricordato per la successiva esportazione
* **Data** --- Formato ISO; modificabile in fase di salvataggio
* **Immagine di copertina** --- PNG o JPG opzionale; Contrassegnato genera un'anteprima della copertina predefinita quando non ne è impostata alcuna

Marked incorpora immagini locali nell'EPUB e può scaricare immagini remote in modo che il file finito sia autonomo. Gli EPUB esportati vengono convalidati come XHTML ben formati prima del salvataggio, producendo file che soddisfano gli standard EPUB per la distribuzione e l'accessibilità.

Consulta [Esporta profili](Exporting.html#export-profiles) per salvare i metadati EPUB e esportare le impostazioni per un uso ripetuto.

## Stile con temi integrati

Lo **stile di anteprima** selezionato per il tuo documento determina l'aspetto dell'EPUB. Ogni tema Marked integrato (Swiss, GitHub, Manuscript e gli altri) può essere applicato all'esportazione EPUB.

1. Scegli uno stile dal menu Stile della finestra di anteprima (o imposta uno stile predefinito in {% prefspane Style %}).
2. Controlla la tipografia, i titoli, i blocchi di codice e le immagini nell'anteprima dal vivo.
3. Esporta in EPUB --- Contrassegnato raggruppa i CSS del tema nel pacchetto EPUB.

Marked applica anche CSS specifici per l'esportazione sopra il tema di anteprima in modo che elementi come note a piè di pagina, tabelle e blocchi di codice evidenziati dalla sintassi vengano visualizzati correttamente negli e-reader. I documenti in modalità struttura utilizzano stili di esportazione ottimizzati per la struttura; Gli indici [Leanpub](Multi-File_Documents.html) `Book.txt` utilizzano automaticamente lo stile di esportazione orientato a Leanpub.

I> I lettori EPUB ignorano alcuni CSS solo web (posizionamento fisso, trucchi del viewport, ecc.). Quello che vedi nell'anteprima di Marked è l'obiettivo, ma i motori di layout dell'e-reader possono semplificare la spaziatura e i caratteri. Prova su Apple Books o sul tuo lettore di destinazione prima di pubblicare.

## Stile con temi personalizzati

[Stili personalizzati](Custom_Styles.html) funzionano allo stesso modo per EPUB che per anteprima e PDF:

* Aggiungi file CSS in {% prefspane Style %} o [Gestione stili](Custom_Styles.html).
* Seleziona il tema personalizzato prima di esportare.
* Contrassegnato incorpora il tuo foglio di stile nell'EPUB esportato.

Suggerimenti per CSS personalizzati compatibili con EPUB:

* Mantieni i layout fluidi --- usa le unità relative e `max-width: 100%` sulle immagini (`#wrapper img { max-width: 100%; }` è una buona base).
* Evita `@media print` regole per lo stile degli ebook; EPUB utilizza gli stili della schermata principale più il foglio di stile di esportazione di Marked.
* [Modalità oscura](Previewing.html) inversione nell'anteprima utilizza `@media screen` query; la maggior parte dei lettori EPUB utilizza il foglio di stile chiaro a meno che l'app del lettore non applichi il proprio tema scuro.
* Utilizza [CSS aggiuntivo](Custom_Styles.html) nelle impostazioni di Stile per modificare tutti i temi contemporaneamente (ad esempio, dimensione uniforme del carattere del corpo tra le esportazioni).

Per indicazioni sulla creazione, vedere [Creazione di CSS personalizzati](Writing_Custom_CSS.html).

## Evidenziazione della sintassi e matematica

Se **Includi evidenziazione della sintassi nell'esportazione** è abilitato in {% prefspane Export %}, il codice blocca l'esportazione con gli stessi colori della sintassi dell'anteprima. La matematica resa con [MathJax](MathJax.html) è inclusa nell'EPUB come appropriato per il supporto dell'e-reader.

## Metadati nel file sorgente

Puoi impostare i metadati EPUB nel documento anziché nella finestra di dialogo di salvataggio. Nella parte superiore di un file Markdown (o in una pagina di metadati Scrivener), utilizza i tasti in stile MultiMarkdown:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` accetta un percorso relativo al documento o un percorso assoluto. Sono supportati PNG e JPG. I valori della finestra di dialogo sovrascrivono o riempiono i metadati mancanti al momento dell'esportazione.

## Libri multifile

Per lavori lunghi, compila capitoli con [Documenti multi-file](Multi-File_Documents.html) --- file indice, esportazioni Scrivener, Leanpub `Book.txt` o indici in stile GitBook. Gli orologi contrassegnati includono file, visualizzano l'anteprima del libro completo ed esportano un EPUB dall'HTML compilato.

I titoli nel documento compilato diventano l'EPUB [indice dei contenuti](Document_Navigation.html) per la navigazione in Apple Books e altri lettori.

## Leggere e pubblicare

Gli EPUB esportati si aprono direttamente in **Apple Books** (fai doppio clic sul file o utilizza **File → Aggiungi alla libreria**). Funzionano anche con Kobo, Thorium, Calibre e la maggior parte delle app compatibili con EPUB 3.

###Libri Apple

Trascina un `.epub` esportato sull'app Libri o aggiungilo tramite **File → Importa**. La tipografia personalizzata e la copertina del tuo tema Marked vengono portate avanti. Utilizza Apple Books su Mac, iPad o iPhone per verificare il layout prima della condivisione.

### Pubblicazione diretta Kindle (KDP)

EPUB è un formato di caricamento accettato per [Kindle Direct Publishing](https://kdp.amazon.com/). Esporta da Marked e carica il file `.epub`; Amazon lo converte per la consegna Kindle. KDP accetta anche [DOCX](Working_with_DOCX.html). Consulta i [formati di eBook supportati](https://kdp.amazon.com/en_US/help/topic/G200634390) di Amazon per i requisiti attuali.

**MOBI non è richiesto** per i nuovi titoli KDP. Contrassegnato non esporta MOBI.

Facoltativo: visualizzare l'anteprima del layout Kindle con il [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuito di Amazon prima del caricamento.

## Correlato

* [Esportazione HTML](HTML_Export.html) --- HTML autonomo con stili e immagini incorporati
* [Esportazione](Exporting.html) --- esporta pannello, profili e altri formati
* [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html) --- anteprima del flusso di lavoro prima dell'esportazione
* [Stili personalizzati](Custom_Styles.html) e [Generatore di stili personalizzati](Custom_Style_Generator.html)
* [Documenti multi-file](Multi-File_Documents.html) --- libri e indici di capitoli
* [Esportazione AppleScript](AppleScript_Support.html) --- automatizza l'esportazione EPUB