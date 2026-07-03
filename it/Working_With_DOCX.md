<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked offre un ampio supporto per lavorare con i file Microsoft Word. Il flusso di lavoro tipico è **prima l'anteprima, poi l'esportazione di DOCX**: apri o guarda il tuo Markdown in Marked, perfeziona gli stili e la correzione di bozze nell'anteprima dal vivo, quindi esporta in Word quando il documento è pronto.

## Apertura di file DOCX

Marked può leggere un file DOCX e convertirlo in un formato pulito
Ribasso. Elementi di stile validi come titoli ed elenchi lo faranno
essere convertiti nel loro equivalente Markdown.

Il rilevamento delle modifiche e i commenti verranno convertiti in
CriticMarkup. I momenti salienti verranno convertiti in `<mark>` tag,
con i colori ove opportuno.

## Esportazione di file DOCX

Utilizza la palette Esporta per generare un file DOCX dal tuo
Ribasso. Nella finestra di dialogo di salvataggio è possibile specificare un file built-in
stili --- questo stile può essere facilmente modificato in Word semplicemente da
aprendo il selettore del tema e selezionando un nuovo tema.

### Intestazioni e piè di pagina

Se configuri intestazioni e piè di pagina in {% prefspane Export %}, verranno inclusi nel DOCX esportato. I segnaposto standard come `%title`, `%date`, `%page` e `%total` vengono sostituiti al momento dell'esportazione. `%logo` e `%image` incorporano il logo dalle preferenze Intestazione/Piè di pagina. `%md_*` Le variabili dei metadati si risolvono dai metadati MultiMarkdown del documento. `%h1`--`%h6` diventano campi Word **STYLEREF** legati agli stili di intestazione esportati; Word li riempie quando apri il documento. Vedi [Esportazione](Exporting.html#headers-and-footers) per l'elenco completo delle variabili e le differenze tra DOCX e il comportamento di stampa/PDF.

## Monitoraggio delle modifiche

La sintassi CriticMarkup in un documento Markdown verrà convertita
al rilevamento delle modifiche di Word quando esportato in DOCX. Commenti
verranno apportati i successivi inserimenti, cancellazioni e sostituzioni
vengono visualizzati nella colonna di destra in Word durante il rilevamento delle modifiche
è abilitato.

Quando si importa un file DOCX in Marked, verrà modificato il tracciamento
essere convertito in CriticMarkup e `<mark>` tag come
appropriato.

## Matematica

Le equazioni MathJax e Katex visualizzate nel documento verranno convertite in MathML per la visualizzazione in Word. Questa conversione non è perfetta, ma nella maggior parte dei casi restituirà un blocco matematico valido nel documento Word. Questo vale solo per l'esportazione: i blocchi matematici nei documenti Word non verranno convertiti durante l'importazione.

## Aggiunta di stili di esportazione personalizzati

Puoi aggiungere i tuoi stili di esportazione includendo un modello e un file stili.xml in `~/Library/Application Support/Marked/Custom Word Styles/`. Per crearli:

1. Apri un file DOCX generato da Mark in Word
2. Modifica gli stili nell'editor di stili per ciascun elemento, selezionando "Aggiungi al modello" per ciascuno di essi.
3. Salvare il file DOCX.
4. Genera un modello andando su **Progettazione** nella barra in alto e dal menu a discesa *Modello* a sinistra, fai clic su **Salva modello corrente**. Nominalo come vuoi che appaia nel menu Stile contrassegnato e salvalo in `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, dove `STYLENAME` è il nome del tuo stile.
5. Vai al Finder e individua il file DOCX che hai salvato da Word. Duplicalo e rinomina la copia in `FILENAME.zip` e fai doppio clic per decomprimerlo.
6. Nel documento decompresso, vedrai una cartella "word" contenente un file stili.xml. Copia il file stili.xml nella stessa cartella di cui sopra e chiamalo `STYLENAME.xml` (dove `STYLENAME` è il nome del tuo stile). I file `.thmx` e `.xml` dovrebbero avere lo stesso nome di base (solo estensioni diverse).

La prossima volta che esporti un DOCX da Marked, vedrai il tuo nuovo stile nel menu Stile della finestra di dialogo Salva.