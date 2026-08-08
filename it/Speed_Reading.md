<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Speed Read è una modalità di lettura in stile RSVP che visualizza una parola alla volta in una sovrapposizione focalizzata.

## Come funziona la lettura veloce [how-speed-read-works]

La lettura veloce utilizza un metodo chiamato **Rapid Serial Visual Presentation** (RSVP). Invece di muovere gli occhi lungo le righe di testo, le parole appaiono in una posizione fissa. Ciò riduce i movimenti oculari, i cambi di riga e il backtracking che normalmente si verificano durante la lettura, il che può renderlo utile per scremare, rivedere materiale familiare o spostarsi rapidamente nel testo senza perdere la posizione.

Il metodo non è magico e non garantisce una migliore comprensione a velocità molto elevate. La comprensione della lettura dipende ancora dalla complessità della scrittura, dalla familiarità con l'argomento e dall'impostazione del WPM. Per materiale denso o sconosciuto, una velocità moderata è solitamente più efficace che spingere la velocità il più in alto possibile.

La lettera rossa indica il punto di ancoraggio visivo della parola, a volte chiamato **punto di riconoscimento ottimale**. In molte parole, i lettori identificano la parola in modo più efficiente quando il loro sguardo si posa leggermente a sinistra del centro anziché sulla prima lettera. Mantenendo il punto di ancoraggio nello stesso punto ed evidenziandolo, Speed ​​Read offre al tuo occhio un bersaglio coerente. Il risultato è una minore rifocalizzazione tra le parole e un ritmo più costante mentre il testo avanza.

## Velocità di apertura Lettura [opening-speed-read]

Utilizza **Anteprima > Lettura veloce**, la voce **Lettura veloce** nel menu Gear della finestra di anteprima, oppure premi {% kbd ctrl opt S %}. La voce di menu è disponibile quando è attiva una finestra di anteprima del documento Markdown (è disabilitata per le anteprime HTML non elaborate e quando nessun documento è aperto).

All'apertura di Speed ​​Read, viene avviato in uno stato di pausa in modo da poter orientarsi prima dell'inizio della riproduzione.

<controlli video preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Il tuo browser non supporta il video dimostrativo Speed Read.
</video>
<p><em>Sovrapposizione di lettura rapida che mostra i controlli di riproduzione, l'opzione di sincronizzazione e l'accesso alla guida.</em></p>

## Controlli sovrapposti [overlay-controls]

Una volta visibile la sovrapposizione, questi tasti sono disponibili:

| Scorciatoia | Funzione |
| :-- | :-- |
| {% kbd space %} | Riproduci/Pausa |
| {% kbd [ %} | Vai all'inizio del paragrafo (premi di nuovo per il paragrafo precedente) |
| {% kbd ] %} | Vai all'inizio del paragrafo successivo |
| {% kbd left %} | Diminuire la velocità di lettura (WPM) |
| {% kbd right %} | Aumenta la velocità di lettura (WPM) |
| {% kbd esc %} | Uscire da Lettura veloce |

Le parentesi vengono acquisite per la navigazione tra paragrafi e le frecce sinistra/destra vengono acquisite per le modifiche alla velocità, quindi questi tasti non attivano la navigazione in anteprima mentre Lettura veloce è aperta. Puoi anche fare clic sul pulsante circolare **X** nell'angolo in alto a sinistra dell'overlay per chiuderlo.

Altre scorciatoie di navigazione dell'anteprima normale funzionano ancora mentre la lettura veloce è attiva, tra cui `t`/`gg` (in alto), `G`/`b` (in basso) e `,`/`.` (navigazione dell'intestazione). Vedi [Navigazione anteprima](Keyboard_Shortcuts#preview-navigation) per l'elenco completo.

Il sommario può essere utilizzato anche durante la lettura veloce. Premi {% kbd cmd t %} per aprirlo e navigare, oppure premi {% kbd f %} per focalizzare immediatamente la ricerca rapida per navigare nelle intestazioni dei documenti.

## Partendo da una selezione [starting-from-a-selection]

Se nell'anteprima è selezionato del testo quando si avvia la lettura veloce, la riproduzione utilizza il testo selezionato. Se non è attiva alcuna selezione, Speed ​​Read utilizza il testo completo del documento.

## Sincronizzazione con la posizione di scorrimento [syncing-with-scroll-position]

Abilita **Sincronizza lettura veloce con posizione di scorrimento** in {% prefspane Preview %}, oppure usa la casella di controllo nella sovrapposizione Lettura veloce, per mantenere insieme l'anteprima e la posizione di Lettura veloce.

Quando questa opzione è abilitata, la lettura veloce inizia dal contenuto attualmente visibile nella parte superiore dell'anteprima anziché dall'inizio del documento. Man mano che la riproduzione avanza, l'anteprima scorre insieme alle parole visualizzate.

Se chiudi la lettura veloce, scorri l'anteprima e riapri la sovrapposizione, la riproduzione inizia dalla nuova posizione visibile. Se si attiva la casella di controllo della sovrapposizione dopo che Lettura veloce è già aperta, la riproduzione viene ripristinata alla posizione di scorrimento corrente e continua da lì.

## Velocità ricordata [remembered-speed]

Il valore WPM viene salvato automaticamente quando lo si modifica con {% kbd ← %} e {% kbd → %}. La velocità scelta verrà ripristinata la prossima volta che utilizzerai la Lettura veloce.