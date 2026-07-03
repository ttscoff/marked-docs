<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Markdown Dingus è uno strumento di test specializzato che aiuta
capisci come i diversi processori Markdown gestiscono il tuo
contenuto. Fornisce un'interfaccia a tre riquadri dove puoi
modifica Markdown, visualizza la sorgente HTML generata e guarda il file
anteprima renderizzata simultaneamente.

Il Dingus condivide alcune manovre di basso livello con Marked
anteprima, come il trattamento speciale dei blocchi di codice recintati.
__non__ esegue [Regole personalizzate](Custom_Processor.html)
(Conduttore). Utilizza la maggior parte delle impostazioni predefinite, ignorando le impostazioni
come "newline GitHub" e "caselle di controllo GitHub", quindi il file
il risultato potrebbe differire da quello che vedi in un normale Marked
anteprima.

## Le regole personalizzate non si applicano

Il Dingus è un __sandbox del processore__: il tuo Markdown va
direttamente al processore integrato scelto (MultiMarkdown,
CommonMark (GFM), Discount o Kramdown). [Regole personalizzate](Custom_Processor.html)
non eseguire mai lì: nessuna azione di preelaborazione, trova/sostituisci regole,
comandi shell, Inserisci testo/file o altri passaggi di Conductor.

In un'anteprima normale, le regole personalizzate possono modificare il markdown
prima del rendering, impostare gli stili, inserire CSS o JavaScript e
di più. Niente di tutto ciò accade quando modifichi in Dingus.
La modifica delle regole personalizzate mentre Dingus è aperto no
aggiorna la sua anteprima.

I Dingus __can__ usano gli stessi [stili CSS di anteprima](Custom_Styles.html)
come finestra principale (tramite il menu Stile nel riquadro di output).
Questa è solo apparenza; non è la stessa cosa che eseguire Custom
Regole.

__Apri in Dingus__ da un'anteprima carica il documento
buffer Markdown corrente. Se le regole personalizzate sono già state eseguite quando
quel file è stato aperto in Marked, potresti vederne gli effetti in
il testo (ad esempio testo inserito da una regola), ma il
Dingus non riapplicherà le regole durante la digitazione. Per testare Custom
Regole, utilizza un'anteprima contrassegnata standard o salva da Dingus
e apri il file con __Apri in contrassegnato__.

## Cos'è un "Dingus"?

Un "dingus" è un termine preso in prestito dallo sviluppo web che
si riferisce a un semplice strumento di test o a un ambiente sandbox. Il
Markdown Dingus ti consente di sperimentare la sintassi di Markdown e
vedere immediatamente come i diversi processori lo interpretano.

## Accesso al Dingus

È possibile accedere al Markdown Dingus da
[{% appmenu Help, Markdown Dingus %}][2]. È particolarmente
utile quando sei:

* Apprendimento della nuova sintassi Markdown
* Risoluzione dei problemi di rendering
* Scelta tra diversi processori
* Scrivere documentazione che deve funzionare su più livelli
  sistemi

## Layout a tre riquadri

![][1]

La finestra Dingus è divisa in tre riquadri sincronizzati:

### 1. Ingresso ribasso (riquadro sinistro)

* __Evidenziazione della sintassi__: il tuo Markdown viene evidenziato con
  colori per rendere chiara la struttura
* __Modifica dal vivo__: digita e visualizza immediatamente le modifiche
  negli altri riquadri
* __Large Font__: carattere Menlo da 21 pt per un editing confortevole

__Menu a discesa Opzioni__ (in alto a destra del riquadro sinistro): il
Il menu **Opzioni** ti consente di attivare/disattivare:

* __Mostra numeri di riga__: Visualizza un margine interno a sinistra con
  un numero di riga per paragrafo (le righe a capo contano come uno
  linea).
* __Mostra invisibili__: mostra gli spazi come punti centrali (·), le tabulazioni come
  una freccia verso destra (→) e il ritorno a capo come ritorno a capo
  simbolo (↵) in grigio chiaro in modo da poter individuare i randagi
  spazi bianchi.
* __Evidenzia gremlins__: inserisce uno sfondo rosso chiaro
  caratteri non ASCII (ad esempio virgolette inglesi, emoji) e un carattere scuro
  sfondo rosso su caratteri invisibili problematici (ad es.
  spazi di larghezza zero). I caratteri normali di tabulazione e di nuova riga lo sono
  non evidenziato.

Le tue scelte verranno salvate e ripristinate alla successiva apertura
il Dingo.

__Barra di ricerca__: premi **⌘F** per mostrare la barra di ricerca sotto il
Etichetta "Inserimento ribasso". Puoi cercare e sostituire nel file
editor, utilizza **⌘G** per Trova successivo e **⇧⌘G** per Trova
Precedente e sostituisci una o tutte le corrispondenze. Premi la chiusura
o ancora **⌘F** per nascondere la barra di ricerca.

### 2. Sorgente HTML (riquadro centrale)

* __HTML generato__: vedi esattamente quale HTML è selezionato
  il processore crea
* __Sintassi evidenziata__: HTML è codificato a colori per una facile comprensione
  lettura

### 3. Anteprima renderizzata (riquadro destro)

* __Anteprima dal vivo__: guarda come apparirà il tuo Markdown quando
  reso
* __Supporto Emoji__: gli emoji in stile GitHub come `:zzz:` sono
  convertito in immagini
* __Scorrimento automatico__: scorre automaticamente per mostrare il tuo
  posizione di modifica corrente

## Modifica nel Dingus

Il riquadro Markdown Input include funzionalità di modifica intelligente
rendi la scrittura di Markdown più veloce e naturale.

### Nuova riga intelligente (tasto di ritorno)

Premendo Invio ci si adatta alla riga corrente:

* __Lists__: su una riga di elenco (`-`, `*`, `+` o `1.`),
  inserisce un nuovo elemento dell'elenco con il contrassegno corretto. Numerato
  gli elenchi continuano con il numero successivo.
* __Blockquotes__: su una riga che inizia con `>` , inserisce un
  nuova riga di virgolette.
* __Recinti di codice__: su una riga con tre o più apici inversi
  (es. ` ``` `), inserisce una riga vuota tra l'apertura
  e chiusura delle recinzioni.
* __Altre righe__: inserisce un normale ritorno a capo.

### Accoppiamento di personaggi

Quando digiti un carattere di apertura, l'editor automaticamente
inserisce il carattere di chiusura e posiziona il cursore tra
loro. Coppie supportate: `"` `'` `(` `[` `` ` `` `<` .

* __Con selezione__: avvolge il testo selezionato nella coppia.
* __Senza selezione__: Inserisce la coppia con il cursore
  tra loro.
* __Type-over__: se il carattere successivo è già il
  delimitatore di chiusura, digitandolo nuovamente si sposta il cursore oltre
  invece di inserire un duplicato.
- __Spazio nella coppia vuota__: se il cursore si trova tra una coppia vuota (es. `(|)`), digitando uno spazio si sostituisce il carattere di chiusura con uno spazio.

### Tasti di scelta rapida

| Scorciatoia | Azione |
|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⌘CA** | Mostra o nascondi la barra di ricerca nel riquadro Input Markdown |
| **⌘G** | Trova successivo (quando è visibile la barra di ricerca) |
| **⇧⌘G** | Trova precedente (quando è visibile la barra di ricerca) |
| **⌘B** | Grassetto: avvolge la selezione in `**` o inserisce `**\|**` con il cursore tra |
| **⌘Io** | Corsivo: avvolgi la selezione in `_` o inserisci `_\|_` con il cursore tra |
| **⇧⌘L** | Indicatore elenco cicli (non ordinato ↔ ordinato) |
| **Tab** | Rientro riga o voce elenco |
| **Maiusc+Tab** | Riga o voce di elenco fuori rientro |
| **⌃⌘→** | Rientra la riga o l'elemento dell'elenco (come Tab) |
| **⌃⌘←** | Riga o elemento di elenco rientrato (come Maiusc+Tab) |
| **⌃⌘↑** | Sposta il paragrafo verso l'alto (taglia il paragrafo includendo il ritorno a capo, incolla una riga verso l'alto) |
| **⌃⌘↓** | Sposta il paragrafo verso il basso (taglia il paragrafo includendo il ritorno a capo, incolla una riga verso il basso) |
| **⌘K** | Inserisci o a capo un collegamento Markdown: avvolgi la selezione come `[text]()` e posiziona il cursore nell'URL oppure inserisci `[]()` con il cursore tra parentesi quando non c'è selezione |
| **⌘U** | Attiva/disattiva il riquadro di output (Origine/Anteprima) |
| **⌥⌘↑** | Espandi la selezione: parola → delimitatori interni/esterni → frase → paragrafo → blocco contiguo (come una tabella o un blocco di codice) → elenco che racchiude/virgolette/blocco di codice → documento |
| **⌥⌘↓** | Selezione del contratto di nuovo attraverso gli stessi livelli fino alla posizione originale del cursore |

Tab/Shift+Tab (e ⌃⌘←/⌃⌘→) rispettano la struttura dell'elenco e
virgolette: rientrano/rientrano gli elementi dell'elenco e aggiungono o
rimuovi `>` dalle righe delle virgolette. Sposta il paragrafo su/giù
seleziona l'intero paragrafo sotto il cursore (compreso il suo
fine riga finale), lo taglia e lo incolla sopra o sotto il file
paragrafo adiacente in modo che i paragrafi non si uniscano.

### Incolla URL intelligente

Quando incolli e gli appunti contengono un URL del modulo
`protocol://...` senza spazi:

* __Con una selezione__: la selezione viene trasformata in a
  Collegamento al ribasso: `[selected text](url)` .
* __Senza selezione__: l'URL viene inserito come a
  collegamento automatico: `<url>` .

Ciò semplifica la trasformazione degli URL copiati in collegamenti senza
digitazione manuale.

### Selezione intelligente (⌥⌘↑ / ⌥⌘↓)

L'editor Dingus supporta l'__espansione della selezione semantica__:

* __⌥⌘↑__ inizia dal cursore ed espande la selezione
  attraverso:
	- la parola corrente
	- contenuto delimitato interno ed esterno (virgolette, parentesi,
   parentesi e blocchi di codice recintati)
	- la frase attuale
	- il paragrafo attuale
	- il blocco contiguo di righe non vuote (ad esempio, a
   intera tabella o blocco di codice su più righe senza righe vuote)
	- l'elemento dell'elenco allegato, la virgoletta o il blocco di codice
	- l'intero documento
* __⌥⌘↓__ torna indietro attraverso gli stessi livelli finché non arriva
  ritorna alla posizione originale del cursore.

Ogni pressione si sposta sempre su un valore strettamente più grande o più piccolo
selezione, in modo da non ricevere mai pressioni di tasti "no-op" mentre
espansione o contrazione.

## Utilizzo di Dingus come editor

Il Dingus non intende sostituire un testo completo
editor, ma può essere molto utile per __modifiche rapide con a
anteprima dal vivo__, soprattutto quando vuoi vedere esattamente come
le modifiche verranno renderizzate. Tutto il comportamento di modifica del testo
descritto in [Modifica in Dingus] [3] si applica qui.

### Apertura di un file/creazione di un nuovo file

* __Crea un nuovo file nel Dingus__
	- Scegli __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Quando richiesto, scegli __Dingus__ per avviarne uno nuovo, non salvato
   Documento Dingus.
	- Nuovi documenti Dingus aperti con contenuto di esempio selezionato;
   basta iniziare a digitare per sostituirlo.
* __Apri un file esistente in Dingus__
	- Utilizzare __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), o
   con la finestra Dingus attiva, fare clic su __Apri…__ nello stato
   barra. Il comando apre quindi la finestra Dingus, se necessario
   mostra il pannello Apri.
	- Scegli qualsiasi file di testo semplice/Markdown supportato; suo
   i contenuti sostituiranno l'attuale buffer Dingus.
* __Apri un documento di anteprima contrassegnato in Dingus__
	- Da una normale finestra di anteprima, usa __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E).
	- Il Markdown del documento corrente viene caricato in Dingus
   così puoi sperimentare senza toccare il file originale
   finché non scegli di salvare. Le regole personalizzate non vengono applicate
   il Dingo; vedere [Le regole personalizzate non si applicano](#custom-rules-do-not-apply).

### Salvataggio di un file

* __Salva le modifiche al file corrente__
	- Nella finestra di Dingus, fai clic su __Salva__ nella barra di stato,
   o utilizzare
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Se il documento Dingus non è stato ancora salvato, lo sarai
   richiesto un percorso e un nome file; dopodiché, ⌘S
   aggiorna lo stesso file.
* __Salva con nome/duplica in un nuovo file__
	- Utilizza __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	- Questo apre sempre una finestra di dialogo __Salva con nome__ e scrive il file
   il contenuto corrente di Dingus in un nuovo file senza sovrascriverlo
   l'originale.

### Anteprima in Marked

* __Apri il documento Dingus come anteprima completa contrassegnata__
	- Fai clic su __Apri in Marked__ nella barra di stato di Dingus oppure utilizza

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Se il documento Dingus non è salvato o presenta modifiche non salvate,
   ti verrà chiesto di salvare prima; quindi Marked apre a
   anteprima standard per quel file.

Usando questi comandi, puoi trattare Dingus come a
editor leggero per soluzioni rapide ed esperimenti, quindi
passa a un'anteprima completa di Marked o al tuo editor normale quando
sei pronto per modifiche più estese.

## Selezione del processore

Utilizza il menu a discesa in alto per passare da uno all'altro
Processori di markdown:

* __MultiMarkdown__: processore completo con tabelle,
  note a piè di pagina e supporto matematico
* __CommonMark (GFM)__: processore standard e veloce secondo il
  Specifica CommonMark
* __Discount__: GitHub Flavored Markdown con attività
  elenchi e tabelle
* __Kramdown__: processore avanzato con funzionalità aggiuntive
  come IAL e tipografia

## Perché usare il Dingus?

### Comprendere le differenze tra i processori

Diversi processori Markdown gestiscono la sintassi in modo diverso. Il
Dingus ti aiuta:

* __Confronta output__: guarda esattamente come viene eseguito il rendering di ciascun processore
  lo stesso Markdown
* __Problemi di debug__: identifica il motivo per cui una certa sintassi non lo è
  funzionando come previsto
* __Impara la sintassi__: comprendi le sottili differenze
  tra le implementazioni del processore

### Testare prima di scrivere

Prima di impegnarti in un particolare stile Markdown nel tuo
documenti:

* __Convalida la sintassi__: assicurati che il tuo Markdown venga visualizzato
  correttamente
* __Scegli processori__: decidi quale processore funziona meglio
  per i tuoi contenuti
* __Sperimenta in modo sicuro__: prova la nuova sintassi senza influire
  i tuoi documenti reali

## Casi d'uso comuni

### Differenze di sintassi delle tabelle

Alcuni processori gestiscono la sintassi delle tabelle in modo diverso. Il Dingo
ti consente di vedere quale processore supporta meglio la tua tabella
esigenze di formattazione.

### Supporto per le note a piè di pagina

Non tutti i processori supportano le note a piè di pagina. Usa il Dingus per
verifica che la sintassi della nota a piè di pagina funzioni con il processore scelto.

### Matematica e caratteri speciali

Testare il modo in cui i diversi processori gestiscono la matematica
espressioni e caratteri tipografici speciali.

## Suggerimenti per un utilizzo efficace

1. __Inizia in modo semplice__: inizia con Markdown di base e gradualmente
   aggiungere complessità
2. __Test Edge Cases__: prova combinazioni di sintassi insolite
   comprendere i limiti del processore
3. __Confronta fianco a fianco__: passa da un processore all'altro
   vedere chiaramente le differenze
4. __Utilizza contenuto reale__: copia il contenuto reale dal tuo
   documenti per testare scenari del mondo reale

Il Dingus è uno strumento potente per chiunque lo desideri
comprendere le sfumature delle diverse implementazioni di Markdown
e garantire che il loro contenuto venga visualizzato correttamente su vari
piattaforme e processori.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus