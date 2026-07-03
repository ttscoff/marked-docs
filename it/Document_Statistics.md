<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tieni traccia mentre scrivi.

## Conteggio parole e statistiche dei documenti

![][1]

   [1]: images/WordCount.jpg @2x larghezza=840px altezza=61px classe=centro

Il conteggio delle parole si trova nella barra di stato in basso e può essere abilitato e disabilitato da {% prefspane General %} sotto la barra di stato. Puoi visualizzare ulteriori statistiche nella finestra di anteprima o sorgente dal menu a forma di ingranaggio, facendo clic sul conteggio delle parole o digitando Opzione-Comando-S ({% kbd opt cmd S %}). Tieni premuto il tasto Opzione ({% kbd opt  %}) mentre fai clic per visualizzare le statistiche di leggibilità e tieni premuto Opzione-Comando ({% kbd opt cmd %}) per aprire il pannello Statistiche avanzate.

Se viene selezionato del testo, la visualizzazione del conteggio delle parole e il popup di paragrafi/frasi/caratteri si aggiorneranno con le informazioni solo per la selezione.

## Conteggio parole per la selezione

![Popup conteggio parole sulla selezione del testo][2]

   [2]: images/wordcountforselection.jpg @2x larghezza=749px altezza=144px classe=centro

Quando selezioni il testo nell'anteprima, il conteggio delle parole nella parte inferiore della finestra mostrerà le statistiche solo per il testo selezionato.

Se "Mostra conteggio parole per selezione" è abilitato in {% prefspane Preview %}, verrà visualizzato un piccolo popup accanto al cursore per mostrare il conteggio di parole/righe/caratteri per il testo selezionato. Questo viene eliminato semplicemente allontanando il mouse dal popup.

La funzione di zoom è utile per selezionare e ottenere rapidamente i conteggi di porzioni di testo più grandi. Digita {% kbd z %} per rimpicciolire ed effettuare la selezione.

## Statistiche di leggibilità

![Barra delle statistiche di leggibilità][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x larghezza=1089px altezza=111px classe=centro

Ulteriori statistiche di Flesch/Kincaid e dell'indice della nebbia sono disponibili con {% kbd opt shift cmd S %}.

### Informazioni sulla leggibilità

**Facilità di lettura di Flesch:** i punteggi più alti indicano materiale più facile da leggere; i numeri più bassi indicano i passaggi più difficili da leggere.

**90,0--100,0**: studente medio di 11 anni
**60.0--70.0**: studenti dai 13 ai 15 anni
**0.0--30.0**: laureati

**Livello di voto Flesch-Kincaid:** il numero di anni di istruzione generalmente richiesti per comprendere questo testo.

**Indice di nebbia Gunning:** misura la leggibilità della scrittura inglese. L'indice stima gli anni di istruzione formale necessari per comprendere il testo in prima lettura. Un indice di nebbia pari a 12 richiede il livello di lettura di un liceale statunitense (circa 18 anni).

## Statistiche avanzate

![Popup Statistiche Avanzate][avv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Selezionando Statistiche avanzate dal menu a forma di ingranaggio ---- o premendo {% kbd cmd I %} --- verrà visualizzato un pannello contenente statistiche del documento più avanzate, tra cui la lunghezza media di parole e frasi e la complessità media delle parole.

### Statistiche avanzate mobili

![Finestra informazioni mobile][mobile]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Premendo {% kbd shift cmd I %} si aprirà un pannello mobile contenente tutte le statistiche dettagliate e le informazioni sulla leggibilità. Questo pannello può rimanere in primo piano quando passi al tuo editor, così puoi vedere le tue statistiche aggiornate ogni volta che salvi, indipendentemente dal fatto che l'anteprima sia visibile o meno. Premendo l'icona `<` si riporterà in primo piano l'anteprima contrassegnata associata. Se tieni premuta l'opzione e fai clic sullo stesso pulsante, si aprirà il file Markdown nel tuo editor di testo predefinito (impostato in {% prefspane Apps %}).

### Obiettivi di parole

Se hai un obiettivo specifico per il conteggio delle parole mentre scrivi, puoi aggiungere una chiave di metadati "obiettivo:" nella parte superiore del documento e Marked monitorerà i tuoi progressi, visualizzando un indicatore di completamento nel pannello Statistiche dettagliate ({% kbd cmd I %}) e nelle Statistiche mobili ({% kbd shift cmd I %}).

![][conteggioparoleobiettivo]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualizza la ripetizione delle parole

Selezionando Visualizza ripetizione parole dal menu a forma di ingranaggio (o premendo {% kbd ctrl cmd W %}) passerai a una vista speciale che rimuove gli elementi non di testo ed evidenzia le parole ripetute nel documento. Le parole ripetute vengono evidenziate in rosa chiaro e il passaggio del mouse su una parola evidenziata renderà più luminose le parole corrispondenti in tutto il documento. Facendo clic su una parola evidenziata si oscurerà lo sfondo e si "bloccherà" l'evidenziazione per un'ulteriore revisione.

![Ripetizione di parole][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

Puoi utilizzare la funzione "zoom" (digita "z") anche in questa modalità, consentendoti di evidenziare una parola ripetuta, quindi scansionare rapidamente l'intero documento per vedere dove sono concentrate le ripetizioni.

Le parole vengono confrontate in base alla loro "radice", il che significa che "parte", "parzialmente" e "parti" saranno considerate parole ripetute. Ciò tiene conto delle sillabe e della coniugazione durante il controllo della densità di ripetizione.

**Ambito**

L'ambito del controllo di ripetizione può essere modificato nella barra degli strumenti inferiore del documento e può essere impostato su Documento o Paragrafo. La modalità documento è predefinita; selezionando Paragrafo vengono conteggiate solo le ripetizioni all'interno di ciascun blocco di testo. Le ripetizioni verranno comunque evidenziate nell'intero documento, ma conteggiate solo se una parola appare più di una volta all'interno di un singolo paragrafo.

**Ignorando le parole**

Puoi escludere temporaneamente una parola e tutte le sue varie coniugazioni e pluralizzazioni facendo clic-Opzione sulla parola evidenziata. Le parole temporaneamente ignorate appariranno nell'angolo in basso a destra dell'anteprima. Facendo clic su una parola nell'elenco delle parole ignorate verrà ripristinata la visualizzazione.

Per ignorare permanentemente le parole, puoi modificare un elenco in {% prefspane Proofing %} nella scheda Ignora ripetizioni. Le parole (o le radici delle parole) aggiunte una per riga in questo elenco verranno sempre ignorate. Per aggiungere automaticamente una parola a questo elenco, fai clic su Opzione-Maiusc nella visualizzazione della ripetizione delle parole.

**Uscita dalla modalità Ripetizione parole**

Puoi chiudere la visualizzazione della ripetizione delle parole utilizzando l'icona Chiudi accanto al selettore dell'ambito nella barra degli strumenti in basso o premendo Esc.