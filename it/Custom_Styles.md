<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Visualizza i tuoi documenti *a modo tuo*.

## Utilizzo di stili personalizzati

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Il modo più semplice per esplorare gli stili personalizzati è tramite
[Galleria stili personalizzati] [2]. Da lì puoi sfogliare il file
stili disponibili in azione, installali con un semplice clic
pulsante e persino [invia le tue creazioni] [6] per
inclusione.

Per aggiungere fogli di stile personalizzati dal tuo disco locale a Marked,
usa lo {% prefspane Style %}. Verranno aggiunti nuovi stili
i menu a discesa in Impostazioni finestra e su ciascuna finestra,
e verrà denominato in base al nome file di base del file CSS
aggiunto. Archivia i tuoi file CSS personalizzati in un posto sicuro sul tuo
guidare. Se si spostano sul tuo disco, verranno rimossi da
Contrassegnati finché non li aggiungi di nuovo dalla nuova posizione. Lo è
una buona idea chiudere i documenti aperti e rimuovere lo stile
da Impostazioni prima di eliminare o rinominare un file CSS utilizzato da
Contrassegnato. Non romperà nulla se non lo fai, ma salva
una certa confusione.

Aggiungi stili personalizzati utilizzando la Gestione stili con il pulsante Aggiungi o trascinando uno o più file CSS nelle Impostazioni
riquadro.

## Gestire gli stili con il Gestore stili

L'avvio di Gestione stili ti offre un unico posto in cui curare ogni integrato
e tema personalizzato. Fai clic sul pulsante **Gestisci stili…** nella {% prefspane Style %}
riquadro,
o semplicemente rilascia i file CSS nella finestra delle preferenze --- Marked li importerà,
apri Gestione stili e seleziona la riga appena aggiunta per te. Trascinando CSS
funziona anche i file direttamente nella finestra Gestione stili; quando più file
vengono trascinati vedrai l'aggiornamento della sovrapposizione ad "Aggiungi N stili personalizzati", quindi è chiaro
stai importando un batch.

![][img-style-manager]

All'interno di Gestione stili troverai una tabella ordinabile che unisce built-in e
stili personalizzati. Ogni riga offre:

- Una casella di controllo **Abilitata** che aggiunge/rimuove immediatamente lo stile dallo Stile
  menu, popup Stile predefinito e scorciatoie da tastiera. Disabilitare attualmente
  lo stile attivo passa automaticamente alla successiva voce disponibile.
- Una colonna **Nome** che puoi modificare in linea; i cambiamenti persistono e si propagano a tutti
  menù. Fare clic sul nome dello stile per modificarlo sul posto.
- Una colonna **Sorgente** che indica Incorporato, Personalizzato o Duplicato.
- Uno stack di **Azioni** con pulsanti per **Modificare** (apre il file CSS nel tuo file
  editor), **Duplica** (crea una copia e un nuovo file CSS su disco), **Rivela**
  (mostra il file nel Finder) e **Elimina** (con opzioni per rimuovere il riferimento o
  spostare il file CSS nel Cestino).

Le righe vengono riordinate tramite trascinamento e l'ordine guida anche il menu Stile
le `⌘/#` assegnazioni di scorciatoie, così puoi letteralmente trascinare gli stili negli slot
vuoi. Puoi anche trascinare file CSS esterni in posizioni specifiche; la goccia
L'indicatore determina dove viene inserito il nuovo stile.

### Anteprima dal vivo

Il riquadro di destra contiene un'anteprima che esegue il rendering dello stile selezionato
all'interno di un documento HTML completo con un set completo di intestazioni, elenchi, tabelle, blocchi di codice, ecc
l'anteprima utilizza il CSS effettivo sul disco, quindi le modifiche apportate nell'editor esterno si aggiornano immediatamente. Una casella di controllo attiva/disattiva l'anteprima della modalità oscura.

Puoi trovare stili aggiuntivi da utilizzare (o come esempi per
creando il tuo) [su GitHub] [1] (vedi [esempi] [2] per
una rapida occhiata a cosa c'è). Vedi [Creazione di CSS personalizzati][3]
per dettagli e suggerimenti.

## CSS aggiuntivi

Sotto {% prefspane Style %} troverai un'opzione
intitolato CSS aggiuntivo con un pulsante denominato "Modifica CSS".
Facendo clic su questo pulsante si apre una finestra in cui è possibile aggiungere
regole CSS universali che verranno applicate a tutti gli stili. Nota
che la specificità delle regole può essere importante quando
sovrascrivendo alcuni degli stili predefiniti di Marked. Il corpo principale
del documento è racchiuso in un div con l'id "#wrapper".
Prefissare un selettore con questo può consentire una maggiore semplicità
sovrascrive, ad esempio:

    #wrapper img {larghezza: 100%; altezza: automatica; }

I CSS in questo campo verranno applicati a ogni documento, no
non importa quale stile sta utilizzando. Se vuoi applicare custom
CSS basato su corrispondenze condizionali, utilizza Imposta stile, Inserisci
File CSS o Inserisci azioni CSS in {% prefspane Processor %}
Regole personalizzate.

## Stampa ed esporta in PDF

Marked inserisce un blocco `@media print` incorporato (`mkprintstyles`) su ogni
anteprima. Imposta valori predefiniti come una base **10pt** su `html`, `body` e
`#wrapper` (o la dimensione da **Dimensione carattere personalizzata per esportazione/stampa** in
{% prefspane Export %} quando l'opzione è abilitata) e normalizza il paragrafo
testo con `p { font-size: 1em; }` e `li p { font-size: 1em; }` così
le regole solo sullo schermo come `p { font-size: 1.1429em; }` non gonfiano il testo del corpo
nei PDF e nell'output stampato.

L'esportazione PDF utilizza i supporti di stampa sul WebView nascosto utilizzato per la generazione, quindi
`@media print { ... }` le regole nel tuo foglio di stile si applicano allo stesso modo di for
stampa.

Per impostare dimensioni diverse dalle impostazioni di stampa predefinite di Marked, aggiungi regole esplicite
all'interno di `@media print` nel tuo CSS personalizzato (o nel CSS aggiuntivo). Utilizzare
`!important` quando è necessario sovrascrivere gli stili di stampa inseriti da Marked --- per
esempio:

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
```

Le regole senza `!important` potrebbero perdere contro le regole successive in `mkprintstyles` o contro
altri selettori non qualificati nel tuo foglio che si applicano ancora alla stampa. Mettere
le modifiche di sola stampa in `@media print` (anziché solo nelle regole dello schermo) vengono mantenute
il comportamento di anteprima ed esportazione è più facile da ragionare.

## Guardare le modifiche CSS

Puoi selezionare una casella nella sezione Stili personalizzati del {% prefspane Style %}
per fare in modo che Marked guardi il file CSS attivo
oltre al file Markdown che stai modificando. Quando
vengono rilevate modifiche su uno dei file, verrà visualizzata l'anteprima
aggiornamento. Ciò è utile per modificare stili personalizzati senza
costantemente aggiornato e può essere utilizzato anche per semplici web
compiti di sviluppo.

Ciò è utile anche per alcuni lavori di web design di base e CSS
sperimentazione (come la creazione di stili personalizzati). Carica un
File Markdown contenente tutto il markup a cui desideri applicare lo stile
per, crea uno stile personalizzato e guarda l'anteprima dal vivo
cambia mentre lo modifichi.

## Scrittura di CSS personalizzati

Se hai familiarità con i CSS, puoi creare il tuo stile
fogli da utilizzare in Marked. Vedi [Scrittura di CSS personalizzati][3] per
dettagli. Ogni volta che crei qualcosa di nuovo, pensaci
[inviandolo] [6] alla [galleria] [2] per condividerlo con altri
utenti. Assicurati di coprire le nozioni di base elencate nella guida e
includere il commento sui metadati in alto.

### Stili personalizzati automatici con StyleStealer

Puoi anche generare automaticamente uno stile basato su un file
sito Web esistente utilizzando [Style Stealer] [4]. Ciò ti consente di caricare una pagina Web e acquisire gli stili calcolati per tutti gli elementi principali trovati in Markdown, quindi salvarli in uno stile personalizzato.

![Stile Stealer][stylestealer]

  [stylestealer]: immagini/style-stealer-800.jpg @2x width=800


Gestisci gli stili personalizzati (rinomina, riordina, duplica ed elimina) da [Gestione stili](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center