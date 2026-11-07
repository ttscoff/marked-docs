# <%= @title %>

Visualizza i tuoi documenti a modo *tuo*.

## Uso di stili personalizzati [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Il modo più semplice per esplorare gli Stili personalizzati è tramite la
[Galleria degli stili personalizzati][2]. Da lì puoi sfogliare gli stili
disponibili in azione, installarli con un clic e persino
[inviare le tue creazioni][6] per l'inclusione.

Per aggiungere fogli di stile personalizzati dal tuo disco locale a Marked,
usa {% prefspane Style %}. I nuovi stili verranno aggiunti ai menu a discesa
nelle impostazioni della finestra e su ogni finestra, e verranno nominati in
base al nome del file CSS aggiunto. Conserva i tuoi file CSS personalizzati
in un luogo sicuro sul disco. Se vengono spostati, verranno rimossi da
Marked finché non li aggiungi di nuovo dalla nuova posizione. È consigliabile
chiudere i documenti aperti e rimuovere lo stile dalle Impostazioni prima di
eliminare o rinominare un file CSS usato da Marked. Non succede nulla di
grave se non lo fai, ma eviti un po' di confusione.

Aggiungi Stili personalizzati utilizzando il Gestore Stili con il pulsante
Aggiungi, oppure trascinando uno o più file CSS nel pannello Impostazioni.

## Gestire gli stili con il Gestore Stili [managing-styles-with-the-style-manager]

Avviando il Gestore Stili hai un unico posto in cui curare tutti i temi
predefiniti e personalizzati. Fai clic sul pulsante **Gestisci Stili…** nel
pannello {% prefspane Style %},
oppure trascina semplicemente i file CSS sulla finestra delle preferenze:
Marked li importerà, aprirà il Gestore Stili e selezionerà per te la riga
appena aggiunta. Trascinare i file CSS direttamente sulla finestra del
Gestore Stili funziona altrettanto bene; quando trascini più file, vedrai la
sovrapposizione aggiornarsi in "Add N Custom Styles" così è chiaro che stai
importando un gruppo di file.

![][img-style-manager]

All'interno del Gestore Stili troverai una tabella ordinabile che unisce
stili predefiniti e personalizzati. Ogni riga offre:

- Una casella di controllo **Abilitato** che aggiunge/rimuove immediatamente
  lo stile dal menu Stile, dal popup Stile predefinito e dalle scorciatoie
  da tastiera. Disattivare lo stile attualmente in uso passa
  automaticamente alla voce disponibile successiva.
- Una colonna **Nome** che puoi modificare direttamente in linea; le
  modifiche vengono salvate e si propagano a ogni menu. Fai clic sul nome
  dello stile per modificarlo sul posto.
- Una colonna **Origine** che indica se lo stile è Predefinito, Personalizzato
  o Duplicato.
- Una serie di pulsanti **Azioni** che comprende **Modifica** (apre il file
  CSS nel tuo editor), **Duplica** (crea una copia e un nuovo file CSS sul
  disco), **Mostra** (visualizza il file nel Finder) ed **Elimina** (con
  opzioni per rimuovere solo il riferimento o spostare il file CSS nel
  Cestino).

Le righe si riordinano trascinandole, e l'ordine determina sia il menu
Stile sia le assegnazioni delle scorciatoie `⌘/#`, così puoi letteralmente
trascinare gli stili nelle posizioni che preferisci. Puoi anche trascinare
file CSS esterni in posizioni specifiche; l'indicatore di rilascio
determina dove verrà inserito il nuovo stile.

### Anteprima dal vivo [live-preview]

Il pannello a destra contiene un'anteprima che mostra lo stile selezionato
all'interno di un documento HTML completo, con un ampio insieme di
intestazioni, elenchi, tabelle, blocchi di codice, ecc. L'anteprima
utilizza il CSS effettivo presente sul disco, quindi le modifiche apportate
nel tuo editor esterno si aggiornano istantaneamente. Una casella di
controllo attiva/disattiva l'anteprima in Modalità Scura.

Puoi trovare altri stili da utilizzare (o come esempi per crearne di tuoi)
[su GitHub][1] (guarda gli [esempi][2] per uno sguardo veloce a cosa è
disponibile). Consulta [Creare CSS personalizzati][3] per dettagli e
consigli.

## CSS aggiuntivo [additional-css]

In {% prefspane Style %}, troverai un'opzione denominata CSS aggiuntivo con un
pulsante etichettato "Edit CSS". Facendo clic su questo pulsante si apre
una finestra in cui puoi aggiungere regole CSS universali che verranno
applicate a tutti gli stili. Nota che la specificità delle regole può
essere importante quando si sovrascrive parte dello stile predefinito di
Marked. Il corpo principale del documento è racchiuso in un div con id
"#wrapper". Anteporre un selettore con questo può facilitare le
sovrascritture, ad esempio:

    #wrapper img { width: 100%; height: auto; }

Il CSS in questo campo viene **aggiunto al tema attivo**. Non sostituisce
uno Stile personalizzato completo: un foglio di stile scritto solo per
questo campo è volutamente parziale, e caricarlo tramite il Gestore Stili
come tema lascerebbe senza stile tutto ciò che non copre.

Marked **riscrive** i selettori del CSS aggiuntivo prima dell'iniezione. Le
classi body iniziali come `.mkprinting` vengono unite a `body` invece di essere
annidate sotto `#wrapper`, quindi le regole di stampa in questo campo
dovrebbero usare `body.mkprinting #wrapper …` (vedi [Creare CSS
personalizzati](Writing_Custom_CSS.html#additional-css-settings) per le
regole complete di riscrittura). Non c'è alcun limite di dimensione né
controllo di validità sul campo: un CSS non valido semplicemente non ha
effetto.

Il CSS in questo campo verrà applicato a ogni documento, indipendentemente
dallo Stile utilizzato, inclusa l'esportazione HTML quando gli stili sono
inclusi. Se vuoi applicare CSS personalizzato in base a corrispondenze
condizionali, usa le azioni Imposta Stile, Inserisci File CSS o Inserisci
CSS in {% prefspane Processor %}
Regole personalizzate.

## Esportazione in Stampa e PDF [print-and-pdf-export]

Marked inserisce un blocco `@media print` integrato (`mkprintstyles`) in ogni anteprima.
Imposta valori predefiniti come una base di **10pt** su `html`, `body` e
`#wrapper` (oppure la dimensione da **Dimensione carattere personalizzata per
esportazione/stampa** in {% prefspane Export %} quando questa opzione è attiva), e
normalizza il testo dei paragrafi con `p { font-size: 1em; }` e `li p { font-size: 1em; }`, così le regole
valide solo su schermo come `p { font-size: 1.1429em; }` non ingrandiscono il testo del corpo
nei PDF e nelle stampe.

L'esportazione in PDF può utilizzare il media **print** o **screen** sulla
WebView nascosta usata per la generazione. I temi predefiniti utilizzano
generalmente il media print; gli **stili personalizzati** e i documenti
[Fountain](Fountain_for_Screenwriters.html) usano spesso il media screen,
così il layout corrisponde all'anteprima. Ciò significa che le regole
`@media print { ... }` non vengono sempre applicate durante l'esportazione in PDF.

Per uno stile affidabile in PDF e nell'Anteprima Stampa/PDF, anteponi ai
selettori la classe `mkprinting` che Marked aggiunge a `<body>` durante
l'esportazione (vedi [Scrivere CSS
personalizzati](Writing_Custom_CSS.html#printstyles) per dettagli ed
esempi). In un file di **Stile personalizzato** puoi usare semplicemente
`.mkprinting`. In **CSS aggiuntivo**, usa la forma qualificata con body `body.mkprinting #wrapper …`,
perché quel campo riscrive i selettori. Puoi anche combinare entrambe le
forme con `@media print` quando ti serve coprire entrambi i percorsi.

Per impostare dimensioni diverse da quelle predefinite di stampa di Marked,
aggiungi regole esplicite nel tuo CSS personalizzato (o nel CSS aggiuntivo).
Usa `!important` quando devi sovrascrivere gli stili di stampa iniettati da
Marked, ad esempio:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Le regole senza `!important` potrebbero essere sovrascritte da regole
successive in `mkprintstyles` o da altri selettori non qualificati nel tuo foglio
di stile che si applicano comunque in stampa. Inserire le modifiche
specifiche per la stampa in regole `@media print` e/o `.mkprinting` / `body.mkprinting` (anziché
solo in regole per schermo) rende più semplice comprendere il comportamento
dell'anteprima e dell'esportazione.

## Monitorare le modifiche al CSS [watching-css-changes]

Puoi selezionare una casella nella sezione Stili Personalizzati di
{% prefspane Style %}
per far sì che Marked monitori il file CSS attivo, oltre al file Markdown
che stai modificando. Quando vengono rilevate modifiche in uno dei due
file, l'anteprima si aggiorna. Questo è utile per modificare gli stili
personalizzati senza dover aggiornare continuamente e può essere usato
anche per semplici attività di sviluppo web.

È utile anche per alcuni lavori di base di web design e per sperimentare
con il CSS (come la creazione di stili personalizzati). Carica un file
Markdown contenente tutto il markup che vuoi stilizzare, crea uno stile
personalizzato e osserva l'anteprima aggiornarsi in tempo reale mentre lo
modifichi.

## Scrivere CSS personalizzati [writing-custom-css]

Se hai familiarità con il CSS, puoi creare i tuoi fogli di stile da usare
in Marked. Consulta [Scrivere CSS personalizzati][3] per i dettagli. Ogni
volta che crei qualcosa di nuovo, valuta di [inviarlo][6] alla
[galleria][2] per condividerlo con altri utenti. Assicurati di coprire le
basi elencate nella guida e di includere il commento con i metadati in
cima al file.

### Stili personalizzati automatici con StyleStealer [automatic-custom-styles-with-stylestealer]

Puoi persino generare automaticamente uno stile basato su un sito web
esistente utilizzando [Style Stealer][4]. Questo ti permette di caricare
una pagina web e catturare gli stili calcolati per tutti i principali
elementi presenti in Markdown, per poi salvarli come stile personalizzato.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Gestisci gli Stili personalizzati (rinomina, riordina, duplica ed elimina)
dal [Gestore Stili](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
