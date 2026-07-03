<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Questa pagina descrive come spostarsi nelle anteprime lunghe: il [Sommario](#tabella dei contenuti), la [ricerca veloce](#ricerca veloce), i [segnalibri](#segnalibri-e-mini-mappa) e la [minimappa](#minimappa). Per le scorciatoie di scorrimento applicabili ovunque (come {% kbd j %}/{% kbd k %}), vedere [Navigazione tramite tastiera](Interface_Features.html#keyboardnavigation) in [Funzioni interfaccia](Interface_Features.html).

## Sommario

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x larghezza=740px altezza=238px classe=centro

Se il documento contiene intestazioni, nella barra degli strumenti viene visualizzato un pulsante di elenco. Fare clic per espandere il sommario; fai clic su un titolo per passare a quella sezione dell'anteprima. Usa {% kbd j %}/{% kbd k %} (giù/su) per spostarti nell'elenco e {% kbd Enter %} o {% kbd o %} per passare all'intestazione evidenziata.

**Barra filtro:** Con il sommario aperto, premi {% kbd Space %} (barra spaziatrice) per aprire il campo di digitazione successiva. Digita qualsiasi parte del nome del titolo (Marked utilizza la corrispondenza in stile TextMate, ad esempio puoi digitare la prima lettera di ogni parola) e premi Tab ({% kbd ⇥ %}) o la freccia giù ({% kbd ↓ %}) per spostarti nell'elenco filtrato.

Premendo {% kbd cmd T %} si apre (o chiude) anche il sommario.

Se ["Titoli Comprimi sezioni"](Interface_Features.html#collapsibleheadlines) è abilitato in {% prefspane General %}, tenendo premuto il tasto Comando mentre si fa clic su un elemento nel Sommario si comprimerà o espanderà quella sezione, rivelando le sezioni principali secondo necessità.

In modalità a schermo intero, il sommario appare come una barra laterale fissa invece che come un menu a comparsa. Per utilizzare quel layout in un'anteprima in finestra normale, utilizza l'interruttore a schermo intero nella parte inferiore destra del pannello Sommario.

![Attiva/disattiva schermo intero][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x larghezza=740px altezza=238px classe=centro


Per un elenco ridotto di tasti, vedere [Scorciatoie da tastiera](Keyboard_Shortcuts.html#TableofContentsNavigation).

Vedi anche il [Video di navigazione del documento su YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Modalità a schermo intero per il sommario

Quando una finestra di anteprima contrassegnata è a schermo intero, il sommario può rimanere fisso a sinistra per una navigazione costante. Si alterna ancora con {% kbd cmd T %}; fare clic all'esterno del sommario spesso non lo chiuderà in questo layout.

In una finestra normale, fai clic sull'icona nella parte inferiore del pannello TOC per agganciarlo come barra laterale; fare clic sull'icona nella parte superiore della barra laterale per riportarla alla modalità popup.

### Personalizzazione della posizione in cui appare il sommario

Il sommario può essere inserito nel documento esportato utilizzando la [sintassi speciale](Special_Syntax.html#tocplacement) `<!--TOC-->`.

Aggiungi `max#` (ad esempio `<!--TOC max2-->`) per limitare il numero di livelli di intestazione visualizzati.

## Ricerca veloce

**Navigazione veloce** combina il sommario con il filtro focalizzato in modo da poter saltare con una digitazione minima:

- Premi {% kbd f %} nell'anteprima per aprire il sommario con il **campo filtro focalizzato** (stessa idea di aprire il sommario e quindi premere {% kbd Space %}, senza il passaggio aggiuntivo).
- Digitare parte del titolo del titolo; l'elenco filtra in base alle corrispondenze.
- Se rimane solo un titolo, premendo Invio ({% kbd ↩ %}) si passa direttamente ad esso.
- Se rimangono più titoli, premi Tab ({% kbd ⇥ %}) per uscire dal campo filtro, spostati con {% kbd j %}/{% kbd k %} o i tasti freccia, quindi premi {% kbd o %} o Invio ({% kbd ↩ %}) per andare al titolo e chiudere il sommario.
- Tab riporta nuovamente lo stato attivo al campo di ricerca.

> **Promemoria scorciatoia:** Aprendo il sommario e premendo {% kbd Space %} si apre la barra dei filtri, utile ogni volta che il sommario è già visibile.

(I documenti precedenti lo chiamavano "Fast Switcher"; è la stessa funzionalità.)

## Segnalibri e mini mappa {#bookmarks-and-mini-map}

Utilizza il menu di anteprima {% appmenu Gear %} e {% kbd Tab %} ({% kbd ⇥ %}) focalizzando il documento accanto a [cerca](Interface_Features.html#search) per posizionare e rivisitare i segnalibri mentre sfogli.

### Impostazione dei segnalibri

Imposta i segnalibri sulla posizione di scorrimento utilizzando {% kbd shift 1 %}--{% kbd shift 9 %} e torna indietro utilizzando solo {% kbd 1 %}--{% kbd 9 %}. Utilizzare {% kbd n %} e {% kbd p %} per successivo/precedente nell'**ordine dei documenti**; {% kbd shift n %} e {% kbd shift p %} per successivo/precedente in ordine **numerico**.

La modifica dello stile o delle dimensioni della pagina può spostare il punto in cui viene visualizzato un segnalibro. I segnalibri sono intesi come aiuti temporanei alla revisione: non persistono tra le sessioni del documento, ma sopravvivono agli aggiornamenti e alle modifiche dell'anteprima.

**Segnalibri titolo:** Tieni premuto Opzione e premi {% kbd opt 1 %}--{% kbd opt 9 %} per aggiungere ai segnalibri il titolo più vicino alla parte superiore del viewport (o l'ultimo titolo prima della parte superiore).

**Slot libero successivo:** {% kbd cmd D %} (o backtick {% kbd \`\` %}, per gli utenti vim) aggiunge un segnalibro nel successivo slot numerato disponibile.

Premi {% kbd 0 %} per espandere la striscia di segnalibri (titoli dei titoli ove disponibili). Quando la [Mini mappa](#minimap) è abilitata, {% kbd 0 %} la mostra contemporaneamente. Premi nuovamente Esc o {% kbd 0 %} per comprimerlo.

Premi {% kbd x %} due volte ({% kbd xx %}) per cancellare tutti i segnalibri.

Ci sono [altre scorciatoie di anteprima](Keyboard_Shortcuts.html); premi {% kbd h %} nell'anteprima per un elenco in anteprima o {% kbd opt cmd K %} per il riferimento completo.

### Minimappa {#minimappa}

Se la minimappa è abilitata nelle impostazioni {% prefspane Preview %}, {% kbd 0 %} apre una miniatura in scala dell'intero documento lungo la striscia dei segnalibri. Fai clic in un punto qualsiasi della mappa per scorrere l'anteprima completa lì. I segnalibri salvati vengono visualizzati come linee orizzontali con numeri (e intestazioni se pertinenti).

Tieni premuto **Comando** e spostati sulla minimappa per visualizzare una lente di ingrandimento; tieni premuto **Opzione** e trascina per scorrere come se trascinassi la barra di scorrimento.

La mappa si rigenera quando cambia la dimensione o il layout della finestra. Su documenti molto lunghi, premere {% kbd 0 %} una volta potrebbe richiedere alcuni istanti; Marked evita di creare automaticamente la minimappa al caricamento iniziale finché non la richiedi.

Premi {% kbd 0 %} o Esc per chiudere la minimappa.

**Nota sulle prestazioni:** la generazione della mappa può mettere brevemente in pausa l'anteprima su documenti di grandi dimensioni; funziona solo quando la mappa è visibile o dopo un ridimensionamento.

### Panoramica dello zoom (correlato)

Per una panoramica in scala del testo senza la minimappa, vedi [Panoramica zoom](Zoom_Overview.html) ({% kbd z %}).