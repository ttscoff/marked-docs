<!-- MT draft for it — Reading Mode help. Review before publishing. -->
# <%= @title %>

La modalità di lettura mantiene la tua posizione nei documenti lunghi, focalizza il blocco corrente e ti consente di salvare evidenziazioni persistenti.

## Accesso alla modalità di lettura [entering-reading-mode]

Scegli {% appmenu Preview, Reading Mode %} o premi {% kbd ctrl opt r %}. Se la lettura veloce è in esecuzione, Marked la interrompe prima di accedere alla modalità di lettura.

Il paragrafo, l'intestazione, la voce dell'elenco, l'immagine, il blocco di codice, la tabella o un'altra unità di lettura corrente riceve un contrassegno sinistro. La navigazione tramite tastiera si sposta agevolmente tra i blocchi e mantiene l'unità corrente vicino al terzo superiore dell'anteprima. Lo scorrimento riorienta manualmente il focus senza far scattare la pagina.

## Navigazione e ripresa [navigation-and-resume]

Mentre la modalità lettura è attiva:

- {% kbd j %} o {% kbd down %}: Passa all'unità di lettura successiva.
- {% kbd k %} o {% kbd up %}: Passa all'unità di lettura precedente.
- {% kbd h %}: evidenzia la selezione o attiva/disattiva l'evidenziazione sull'unità corrente quando non è selezionato alcun testo.

Marked salva la posizione di lettura corrente per ciascun documento. Quando una posizione salvata differisce dalla vista corrente, l'accesso alla modalità di lettura offre due scelte:

- **Riprendi** ritorna alla posizione di lettura salvata.
- **Inizia da qui** utilizza l'unità di lettura attualmente visibile nell'anteprima.

## Modalità focus [focus-mode]

Fai clic sullo strumento Modalità messa a fuoco nella parte superiore dell'anteprima per oscurare ogni blocco tranne l'unità di lettura corrente. La modalità Focus segue l'unità corrente durante la navigazione. Fare di nuovo clic sullo strumento per ripristinare gli altri blocchi oppure uscire dalla modalità Lettura per cancellare automaticamente la modalità Focus.

## Creazione e modifica dei momenti salienti [creating-and-editing-highlights]

Seleziona il testo e premi {% kbd h %} per creare un evidenziatore in linea. Senza alcuna selezione, premere {% kbd h %} per evidenziare l'intera unità di lettura corrente oppure premerlo di nuovo per rimuovere l'evidenziazione dell'unità. La prima evidenziazione richiede una firma, che Marked utilizza durante la creazione di CriticMarkup. Puoi modificare la firma in {% prefspane Preview %}.

### Popup di selezione

Seleziona il testo per mostrare il popup di selezione con i pulsanti icona centrati nella riga:

- **Evidenziatore** crea un'evidenziazione in linea (o **X** rimuove l'ultima evidenziazione automatica quando l'evidenziazione automatica è attiva).
- **Commento** apre una finestra di dialogo per aggiungere o modificare una nota per l'evidenziazione. Se la selezione non è ancora evidenziata, Marked la evidenzia per prima.

Il popup mostra anche il conteggio delle parole selezionate quando è abilitato **Mostra conteggio parole nella selezione**.

### Evidenzia i commenti [highlight-comments]

I commenti sono separati dalle firme. Una firma attribuisce l'evidenziazione; un commento è la tua nota a riguardo.

Aggiungi o modifica un commento dall'icona del commento popup di selezione oppure fai clic tenendo premuto il tasto Control su un'evidenziazione e scegli **Aggiungi commento…** o **Modifica commento…**. Scegli **Elimina commento** per rimuovere la nota senza eliminare l'evidenziazione.

Le evidenziazioni con commenti mostrano un piccolo punto indicatore. Quando la barra laterale Commenti è visibile (**Anteprima > Mostra commenti**), i commenti evidenziati in modalità lettura vengono visualizzati lì con una linea di collegamento all'evidenziazione principale, insieme a CriticMarkup e ad altri commenti del documento.

### Evidenziazioni automatiche

Fai clic sullo strumento evidenziatore nella parte superiore dell'anteprima per evidenziare automaticamente il testo mentre lo selezioni. Fai clic sull'evidenziatore nel popup di selezione per annullare l'ultima evidenziazione automatica oppure fai nuovamente clic sullo strumento evidenziatore superiore per disattivare l'evidenziazione automatica.

Le evidenziazioni in linea mostrano le maniglie di inizio e fine quando le punti o le selezioni. Trascina una delle maniglie per estendere o contrarre l'intervallo evidenziato. Le modifiche vengono salvate automaticamente e ripristinate quando il documento viene aggiornato o riaperto.

Fai clic su un'evidenziazione per evidenziarla, quindi premi Elimina o Backspace per rimuoverla. Fai clic tenendo premuto il tasto Control su un'evidenziazione e scegli **Condividi...** per aprire il foglio Condividi di macOS con il titolo del documento e il testo evidenziato, **Aggiungi commento…** / **Modifica commento…** per allegare una nota o **Elimina commento** per cancellare la nota.

L'impostazione **Mostra evidenziazioni quando la modalità di lettura è disattivata** controlla se le evidenziazioni salvate rimangono visibili dopo aver abbandonato la modalità.

## Esportazione dei punti salienti [exporting-highlights]

Scegli **Anteprima > Esporta evidenziazioni…** o fai clic sullo strumento Esporta evidenziazioni nella barra degli strumenti della Modalità lettura. Formati: Markdown, HTML (stile di anteprima corrente), testo normale, CSV (compatibile con Readwise, con commenti nella colonna **Nota** e firme in **Firma**) e JSON (include un campo `comment` su ogni evidenziazione).

HTML esporta i nidi evidenziando i commenti come virgolette sotto ogni passaggio evidenziato.

Il formato JSON è il file di interscambio di Marked. Salvalo accanto a un documento Markdown come `Document.markedhighlights.json` o includilo automaticamente quando esporti un TextBundle.

## Importazione dei punti salienti [importing-highlights]

Scegli **Anteprima > Importa momenti salienti…** e seleziona un file JSON dei momenti salienti Marked. Le evidenziazioni si uniscono per ID: vengono aggiunti nuovi ID, gli ID corrispondenti vengono aggiornati e le evidenziazioni esistenti che non sono nel file rimangono.

Quando apri un TextBundle che contiene `highlights.json`, Marked unisce automaticamente i punti salienti. Mentre un TextBundle è aperto, Marked salva anche le modifiche alle evidenziazioni e ai commenti in `highlights.json` nel pacchetto (senza modificare `text.md`).

## TextBundle in evidenza [textbundle-highlights]

Su **Salva TextBundle**, attiva **Includi evidenziazioni** per incorporare `highlights.json` nel pacchetto (o TextPack). Condividi il pacchetto in modo che i collaboratori possano aprirlo in Marked e conservare un set di evidenziazioni combinato.

## CriticMarkup azioni [criticmarkup-actions]

Separato dall'esportazione e importazione delle evidenziazioni, il menu Anteprima fornisce due azioni CriticMarkup per le evidenziazioni salvate:

- **Copia evidenziazioni come CriticMarkup** copia ogni evidenziazione nel formato CriticMarkup senza modificare il file di origine.
- **Inserisci evidenziazioni nel documento...** richiede conferma, quindi racchiude il testo sorgente corrispondente inequivocabile in CriticMarkup. Marked salta le corrispondenze mancanti, duplicate o sovrapposte e segnala il risultato.

Con una firma e un commento, il markup generato utilizza <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>. Con solo un commento, Marked utilizza <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>. Con solo una firma, utilizza <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>. Senza nessuno dei due, Marked crea solo il marcatore <code>{=<span>=</span>highlighted text==}</code>.

## Evidenziazioni della stampa [printing-highlights]

Le evidenziazioni della modalità di lettura sono incluse durante la stampa o il salvataggio come PDF per impostazione predefinita. Utilizza **Includi evidenziazioni modalità lettura** nel foglio di stampa per modificarlo per l'output corrente. L'impostazione corrispondente in {% prefspane Export %} controlla l'impostazione predefinita per i futuri lavori di stampa e PDF.
