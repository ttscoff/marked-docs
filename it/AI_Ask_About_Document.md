<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Chiedi informazioni sul documento utilizza **Apple Intelligence** e il modello linguistico integrato nel dispositivo integrato nelle versioni recenti di macOS per riepilogare l'anteprima di Markdown e rispondere a domande sul suo contenuto. Tutta l'elaborazione avviene sul tuo Mac; il testo del documento non viene inviato ai server di Marked o ai servizi AI di terze parti per questa funzionalità.

## Cosa offre Apple Intelligence

Apple Intelligence è il sistema di Apple per le funzionalità generative sul dispositivo. Marked utilizza il framework **Foundation Models** di Apple per accedere allo stesso modello sul dispositivo che alimenta gli strumenti di scrittura del sistema, esposto direttamente all'interno di Marked per attività incentrate sui documenti.

Marked invia il testo normale del documento (sintassi Markdown rimossa per chiarezza) a questo modello locale. Il modello genera riepiloghi, schemi e risposte in un pannello mobile accanto alla finestra di anteprima. Poiché il modello viene eseguito localmente, funziona offline una volta configurata Apple Intelligence e terminato il download del modello di sistema.

Apple Intelligence è la migliore in attività linguistiche come riepilogare, delineare, estrarre punti chiave e rispondere a domande sul testo fornito. Non è un assistente di codifica o un calcolatore generale e i documenti molto lunghi vengono gestiti in sezioni in modo che i risultati rimangano entro i limiti del contesto del modello.

## Compatibilità del sistema

Chiedi informazioni sul documento viene visualizzato solo quando il tuo Mac può eseguire la funzione.

**Obbligatorio:**

- **macOS 26 (Tahoe)** o versione successiva
- Un **Mac con supporto Apple Intelligence** (Mac Apple in silicio che soddisfano i requisiti dei dispositivi Apple)
- **Apple Intelligence attivato** nelle Impostazioni di sistema

**Non supportato:**

- Mac Intel e altri Mac contrassegnati come non idonei per Apple Intelligence
- Versioni macOS precedenti a Tahoe 26
- **Anteprime HTML non elaborate** (la funzionalità è per Markdown e flussi di lavoro di documenti basati su testo)

Se il tuo Mac è idoneo ma manca la voce di menu, conferma che Apple Intelligence è abilitata e che stai utilizzando una build corrente di Marked che include questa funzionalità. Il menu è completamente nascosto sui sistemi non supportati anziché mostrato in uno stato disabilitato.

## Abilitazione dell'intelligenza di Apple

1. Apri **Impostazioni di sistema**.
2. Vai su **Apple Intelligence e Siri** (o **Apple Intelligence**, a seconda della versione di macOS).
3. Attiva **Apple Intelligence** e completa tutti i passaggi di configurazione richiesti da Apple.
4. Attendi il completamento del download del modello sul dispositivo, se richiesto. Fino a quando il modello non sarà pronto, Marked potrebbe mostrare la voce di menu ma visualizzare un messaggio che Apple Intelligence sta ancora preparando.

Contrassegnato non include una preferenza separata per questa funzionalità. La disponibilità segue lo stato del modello di sistema segnalato da macOS.

## Apertura del documento Chiedi informazioni

Apri il pannello utilizzando uno di questi metodi:

- **Anteprima > Chiedi informazioni sul documento…**
- Scorciatoia da tastiera {% kbd shift ctrl cmd I %} (mentre un documento di anteprima Markdown è la finestra attiva)

Il pannello si aggancia al lato sinistro della finestra del documento. Hai bisogno di un documento aperto con testo leggibile; un documento vuoto o un'anteprima solo HTML non offrirà il comando.

## Il pannello Chiedi informazioni sul documento

Il pannello è organizzato come una semplice visualizzazione chat:

- **Azioni preimpostate** in alto per attività comuni
- Un'**area di risposta** al centro in cui vengono visualizzati riepiloghi e risposte (in streaming man mano che vengono generati)
- Un **campo domanda** in basso in cui puoi digitare domande personalizzate, con i pulsanti **Chiedi** e **Annulla**

Una volta completata la risposta, lo stato attivo torna al campo della domanda in modo da poter chiedere un follow-up senza fare clic.

### Azioni preimpostate

| Azione | Cosa fa |
| :-- | :-- |
| **Riepiloga documento** | Produce un breve riassunto coerente del documento completo. I documenti lunghi vengono riepilogati in sezioni e combinati. |
| **Riepiloga la selezione** | Riepiloga solo il testo attualmente selezionato nell'anteprima. Seleziona prima il testo; altrimenti Contrassegnato richiede di effettuare una selezione o utilizzare Riepiloga documento. |
| **Schema** | Costruisce uno schema gerarchico della struttura del documento utilizzando intestazioni e punti elenco. |
| **Punti chiave** | Elenca i punti più importanti del documento sotto forma di elenco puntato. |

Le azioni preimpostate non richiedono testo nel campo della domanda. Fare clic su un pulsante e attendere la risposta nel pannello in alto.

### Fai le tue domande

1. Digita una domanda nel campo nella parte inferiore del pannello, ad esempio "Quale problema risolve questo documento?" o "Chi è il pubblico previsto?"
2. Premi **Invio** o fai clic su **Chiedi**.
3. Leggi la risposta mentre scorre nell'area di risposta.

Per domande su un passaggio specifico, **seleziona il testo nell'anteprima** prima di chiedere. Contrassegnato invia la selezione come contesto anziché l'intero documento quando una selezione è attiva.

Fare clic su **Annulla** per interrompere una richiesta in corso.

## Esempi

### Breve panoramica di un lungo articolo

Apri un lungo post di blog o un report in Contrassegnato, scegli **Anteprima > Chiedi informazioni sul documento…** e fai clic su **Riepiloga documento**. Utilizza il riassunto per decidere se leggere l'intero pezzo o rinfrescarti la memoria dopo un po' di tempo lontano dalla bozza.

### Note su un paragrafo selezionato

Evidenzia un paragrafo denso nell'anteprima, apri Chiedi informazioni sul documento e fai clic su **Riepiloga selezione**. Utile quando hai bisogno solo di una versione più breve di una sezione.

### Revisione strutturale

Fai clic su **Struttura** su una bozza con molti titoli per vedere se l'argomento scorre in modo logico oppure utilizza **Punti chiave** prima di inviare un documento a qualcun altro per verificare che le idee principali siano chiare.

### Domande mirate

Senza alcuna selezione attiva, digita domande come:

- "Quali sono le tre raccomandazioni principali?"
- "Questo documento menziona la licenza?"
- "Elencare eventuali date o scadenze menzionate."

Con una selezione attiva, poni domande più ristrette come "Che cosa presuppone questo paragrafo riguardo al lettore?" o "Riscrivi questa idea in una frase" (il modello risponde sulla selezione; non modifica il file sorgente).

## Suggerimenti e limitazioni

- **Privacy:** L'elaborazione utilizza il modello on-device di Apple. Marked legge comunque il testo del documento localmente per fornire contenuto a quel modello; trattare di conseguenza il materiale sensibile.
- **Precisione:** verifica i fatti importanti confrontandoli con la tua fonte. I riepiloghi AI possono omettere dettagli o interpretare erroneamente passaggi ambigui.
- **Lunghezza:** i documenti estremamente lunghi vengono elaborati in blocchi. I riepiloghi e le risposte riflettono indirettamente il testo completo; per precisione su una sezione, seleziona prima quella sezione.
- **Lingua:** i risultati seguono le funzionalità linguistiche del modello Apple Intelligence di sistema sul tuo Mac.
- **Rifiuti:** Il sistema potrebbe rifiutare alcune richieste in base alle politiche di sicurezza di Apple.

Se Chiedi informazioni sul documento non è disponibile, controlla le Impostazioni di sistema per lo stato di Apple Intelligence e assicurati di visualizzare l'anteprima di un documento Markdown su un Mac supportato con macOS 26 o versioni successive.