<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

La flessibilità è fondamentale.

## Menù ingranaggio

![][4]

   [4]: images/gearmenu.jpg @2x larghezza=740px altezza=235px classe=centro

Il menu Gear fornisce la maggior parte delle funzionalità presenti nella barra dei menu, oltre ad alcune funzioni specifiche dell'anteprima. Basta fare clic sull'ingranaggio in basso a destra nella finestra per accedere a queste funzioni.

## Resta sempre aggiornato

![][5]

   [5]: images/KeepOnTopPin.jpg @2x larghezza=740px altezza=345px classe=centro

L'icona del lucchetto in basso a sinistra porterà la finestra di anteprima in primo piano e la manterrà lì (mobile) quando si passa ad altre applicazioni. Puoi impostare una trasparenza sulla finestra in {% prefspane General %} che consentirà alla finestra di sbiadire quando si utilizzano altre applicazioni.

Questa funzione può anche essere attivata con {% kbd shift-opt-cmd-f %}.

## Impostazioni predefinite a livello di finestra

In {% prefspane General %} puoi utilizzare "Mantieni le nuove finestre in primo piano" per impostare le nuove finestre in modo che rimangano sempre sopra le altre finestre e/o impostare le finestre in modo che vengano visualizzate in primo piano quando il documento associato viene aggiornato. Le finestre impostate per essere attivate durante l'aggiornamento non "ruberanno il focus" dal tuo editor, si alzeranno solo per essere visibili senza diventare attive.

## Visualizza sorgente

![][6]

   [6]: images/view_source.jpg @2x larghezza=740px altezza=345px classe=centro

Puoi passare dalla visualizzazione di anteprima a quella del codice sorgente con il pulsante nell'angolo in alto a destra. Questa visualizzazione può essere attivata anche con U.

## Cerca

![][7]

   [7]: images/SearchBarFull.jpg @2x larghezza=818px altezza=195px classe=centro

È possibile accedere alla barra di ricerca con {% kbd cmd F %} e consente di cercare nell'anteprima una parola o una frase. Una volta eseguita la ricerca, puoi utilizzare {% kbd cmd G %} e {% kbd shift cmd G %} per spostarti avanti e indietro tra risultati aggiuntivi.

Le caselle di controllo sul lato destro della barra di ricerca ti consentono di restringere la ricerca in base alla distinzione tra maiuscole e minuscole, solo parole intere ed espressioni regolari. Oltre alla ricerca con espressioni regolari, le ricerche con caratteri jolly (*?) funzionano sempre, anche quando l'opzione regex è disattivata.

Puoi anche racchiudere un termine o una frase di ricerca tra barre per interpretarlo automaticamente come un'espressione regolare (ad esempio "/term.+?\b/").


Utilizza la funzione di ricerca in combinazione con l'aggiunta ai segnalibri per salvare le posizioni non appena le trovi. Premi Tab ({% kbd ⇥ %}) per mettere a fuoco il documento, quindi digita Shift-[1-9] per impostare un segnalibro su quel numero. Puoi tornare al segnalibro semplicemente digitando il numero (senza il tasto Maiusc) o utilizzando n/p per spostarti tra i segnalibri nell'ordine dei documenti. N/P navigherà in ordine numerico. Per i segnalibri, il sommario, la minimappa e la ricerca rapida delle intestazioni, vedere [Navigazione del documento](Document_Navigation.html). Consulta la sezione [Navigazione in anteprima](Keyboard_Shortcuts.html#previewnavigation) per ulteriori opzioni oppure digita "?" in qualsiasi momento nell'anteprima.

> **Nota:** la ricerca non può estendersi tra elementi, il che significa che una stringa di ricerca non può continuare tra un paragrafo e un titolo, tra gli elementi dell'elenco, ecc.

Puoi attivare o disattivare le caselle di controllo "Parole intere", "Maiuscole e minuscole" e "Regex" utilizzando rispettivamente {% kbd ctrl shift 1 %}, {% kbd 2 %} e {% kbd 3 %}.

### Ricerca avanzata ###

È possibile utilizzare i caratteri jolly in una ricerca non regex. `*` corrisponderà a qualsiasi serie di caratteri diversi dallo spazio e `?` corrisponderà a qualsiasi singolo carattere.

Avviare una ricerca con `*` la renderà una ricerca con selettore jQuery. Puoi utilizzare qualsiasi selettore jQuery e tutti gli elementi corrispondenti verranno evidenziati e navigabili con {% kbd cmd G %} e {% kbd shift cmd G %}. Per limitare l'ambito di una ricerca testuale a un determinato tipo di elemento, aggiungere i termini di ricerca tra virgolette doppie dopo la definizione del selettore:

    *h2"Alice"

Questo è l'equivalente di `*h2:contains(Alice)`

## Navigazione del documento (TOC, segnalibri, mini mappa)

La pagina [Navigazione documento](Document_Navigation.html) copre il sommario (inclusa l'apertura del filtro con {% kbd Space %}), la ricerca rapida con {% kbd f %}, i segnalibri e la minimappa.

## Navigazione tramite tastiera

È possibile navigare rapidamente nella finestra di anteprima utilizzando le scorciatoie da tastiera. Usa {% kbd j %} e {% kbd k %} per muoverti su e giù e tieni premuto Shift ({% kbd J %}/{% kbd K %}) per muoverti più velocemente. {% kbd t %} e {% kbd b %} si sposteranno nella parte superiore e inferiore del documento (così come {% kbd gg %} e {% kbd G %}, per i fan di Vim). {% kbd u %} e {% kbd d %} si sposteranno di 1/2 pagina su e giù.

### Salto di intestazione

Premendo i tasti virgola ({% kbd , %}) e punto ({% kbd . %}) si salterà avanti e indietro tra le intestazioni del documento. Tenendo premuto Shift ({% kbd shift  %}) salterai solo tra le intestazioni di livello 1 e 2.


##Schermo intero

La modalità a schermo intero può essere attivata dal menu Anteprima o digitando {% kbd ctrl cmd F %}.

## Facendo clic su collegamenti esterni

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Facendo clic su un collegamento esterno nell'anteprima del documento, questo verrà aperto nel browser predefinito. Se fai clic e tieni premuto, quando rilasci Marked ti verranno fornite tre opzioni: puoi copiare l'URL del collegamento negli appunti, convalidare il collegamento o aprire il collegamento nel browser predefinito. Basta fare clic in un punto qualsiasi dell'anteprima per chiudere la finestra. Questa funzione può essere disabilitata in {% prefspane Preview %} ("Abilita popover di collegamento").

Guarda un [video di panoramica su YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Titoli comprimibili ##

Quando "Sezioni comprimi titoli" è abilitato in {% prefspane Preview %}, facendo clic sui titoli si comprimerà la sezione tra quel titolo e quello successivo allo stesso livello. Le sottosezioni all'interno di quella sezione sono nascoste. Facoltativamente, puoi limitare questo comportamento a {% kbd cmd %} clic.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Tenendo premuto {% kbd opt  %} mentre si fa clic (o {% kbd cmd %}-clic) si espanderanno/comprimeranno tutte le sezioni secondarie sotto l'intestazione cliccata. Tenendo premuto il tasto {% kbd shift  %} (Maiusc) mentre si fa clic si comprimeranno tutte le altre sezioni allo stesso livello, rivelando solo la sezione cliccata.

Le sezioni compresse sono contrassegnate da un'evidenziazione gialla a destra del titolo e il cursore indicherà cosa accadrà quando si fa clic sull'elemento.

Se viene apportata una modifica che deve essere visibile o si fa clic su una sezione del sommario che si trova attualmente all'interno di una sezione compressa, le sezioni principali necessarie verranno espanse per rivelarla.

Puoi comprimere/espandere tutte le sezioni di un documento contemporaneamente con "Comprimi tutte le sezioni" ({% kbd opt cmd left  %}) ed "Espandi tutte le sezioni" ({% kbd opt cmd right  %}).

Per ulteriori dettagli, vedere il [video di navigazione del documento su YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

## Indicatori/interruttori personalizzati del processore ##

![][indicatori]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Quando il processore personalizzato e/o il preprocessore sono abilitati, nella barra degli strumenti vengono visualizzati gli indicatori luminosi. Questi possono essere usati per vedere se il processore è acceso o meno per il documento corrente (l'indicatore verrà evidenziato) e facendo clic su di essi si alternerà l'uso rispettivamente del preprocessore e del processore personalizzati.

## Scorri per modificare

La funzione "scorri per modificare" di Marked tiene traccia delle differenze tra l'ultimo aggiornamento e l'ultimo, cercando di trovare il punto in cui hai apportato le modifiche più recenti. Marked ne tiene sempre traccia e nell'anteprima viene visualizzata una piccola linea rossa per mostrare la posizione della prima modifica rilevata. In {% prefspane Preview %}, puoi attivare "Scorri fino alla prima modifica" e quando un'anteprima si aggiorna, la visualizzazione scorrerà delicatamente fino a quella posizione.

Con "Scorri fino alla prima modifica" disattivato, puoi comunque premere il tasto "e" in qualsiasi momento nell'anteprima per andare all'ultimo punto di modifica memorizzato.

## Scorrimento automatico

Consulta la pagina dedicata [Autoscroll](Autoscroll.html). Quando si utilizza lo scorrimento automatico come teleprompter, [la sintassi speciale può inserire pause](Special_Syntax.html#pauses).

## Panoramica dello zoom

Vedi la pagina [Panoramica Zoom](Zoom_Overview.html) ({% kbd z %} nell'anteprima; funziona anche in Ripetizione di parole con {% kbd ctrl cmd w %}).

## Riferimento al ribasso

![][11]

   [11]: images/markdown_reference.jpg @2x larghezza=1148px altezza=267px classe=centro

Seleziona Riferimento Markdown dal menu {% appmenu Help %} per visualizzare una guida che fluttua sulle altre finestre. Questo è utile per coloro che stanno ancora imparando la sintassi di Markdown. Puoi aprire questo pannello tramite la tastiera usando {% kbd opt cmd M %}.

## Scorciatoie da tastiera globali

In {% prefspane General %}, puoi designare una scorciatoia da tastiera personalizzata per attivare Segnato e una per sollevare solo la finestra anteriore in alto senza uscire dall'editor.