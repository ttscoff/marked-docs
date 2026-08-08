<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Trasformare il tuo Markdown in un documento finito.

## Esporta dopo l'anteprima [export-after-preview]

L'anteprima di Marked è la base per l'esportazione: ciò che vedi nella finestra di anteprima è ciò che ottieni in PDF, DOCX, EPUB e altri formati (impostazioni specifiche dell'esportazione del modulo come margini, intestazioni e impaginazione). Imposta prima il tuo stile e correggi le bozze in anteprima, quindi esporta quando il documento è pronto. Vedi [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html) per il flusso di lavoro di anteprima completo.

## Il pannello Esporta [drawer]

![Pannello di esportazione][pannello di esportazione]

Il **Pannello di esportazione** è un pannello in stile Spotlight gestito da tastiera che fornisce un accesso rapido a tutte le opzioni di esportazione. Aprilo facendo clic sull'icona di esportazione nella barra di stato o premendo {% kbd shift cmd e %}.

![Pulsante Esporta][expbut]

Il pannello Esporta ti consente di salvare il tuo documento come HTML, PDF a pagina singola, PDF impaginato, pacchetto RTF o file Microsoft Word DOC o DOCX. Puoi anche salvare in un nuovo file Markdown (le funzionalità specifiche di Marked verranno renderizzate e i relativi risultati inclusi), un documento aperto (ODT) o come OPML per l'utilizzo in altre applicazioni.

## Copia HTML [copyhtml]

Utilizza la funzione Copia HTML per inserire il codice sorgente HTML per la tua anteprima negli appunti senza problemi. Puoi selezionarlo dal menu a forma di ingranaggio o semplicemente premere {% kbd shift cmd C %}. L'HTML copiato sarà uno snippet pronto per l'inserimento in un blog, forum o documento HTML.

Non è necessario essere nella vista sorgente per copiare. Con l'anteprima focalizzata (fai clic su di essa), digita semplicemente {% kbd shift cmd C %} e vedrai un messaggio popup che ti informa che la fonte è negli appunti.

## Salva HTML [save-html]

![][exporthtmlaccessorio]



Il comando Salva HTML, accessibile dal menu a forma di ingranaggio o semplicemente digitando **{% kbd cmd S %}**, ti consentirà di salvare un documento completo pronto per la condivisione o la pubblicazione.

Puoi facoltativamente includere uno qualsiasi degli stili di Marked (o uno dei tuoi [stili personalizzati] [personalizzato]) nell'esportazione, offrendoti un documento pronto con la formattazione necessaria già incorporata.

Inoltre, puoi scegliere di incorporare qualsiasi immagine locale inclusa nel documento all'interno dell'HTML esportato, consentendoti di avere un documento autonomo che può essere ospitato ovunque senza la necessità di spostare le immagini con esso. Funziona solo con immagini a cui si fa riferimento sull'unità locale con percorsi relativi o assoluti. Evita di utilizzare i percorsi `file:///` se desideri utilizzare questa funzionalità.

## Esporta Markdown in PDF su Mac [export-markdown-to-pdf-on-mac]

Anteprima Stampa/PDF ({% kbd cmd P %}) farà apparire una finestra di dialogo di stampa standard. Ogni stile di anteprima in Marked ha i propri stili di stampa associati che rimuovono gli sfondi, modificano le dimensioni del testo e forniscono bordi. L'anteprima verrà stampata in base allo stile attualmente selezionato.

Nella finestra di dialogo di stampa sono prominenti i pulsanti PDF e Anteprima. PDF ti offrirà una varietà di opzioni per l'esportazione in PDF (in base alle applicazioni disponibili) e Anteprima esporterà una versione PDF direttamente su Preview.app dove potrai salvarla o inviarla tramite e-mail.

La stampa su PDF utilizzando questo metodo includerà l'impaginazione. Quando si stampa su carta o PDF, le interruzioni di pagina possono essere inserite manualmente utilizzando la [sintassi `<!--BREAK-->`][interruzione] o impostando le opzioni in {% prefspane Export %} per utilizzare le intestazioni di livello uno e/o livello due come divisori di sezione.

Esiste anche la preferenza per trasformare i righelli orizzontali (`<hr>`) in interruzioni di pagina durante la stampa. In questo modo la riga creata dal tag verrà sostituita con un'interruzione di pagina, rimuovendola dall'output finale. L'anteprima non è influenzata da questa impostazione.

![Margini di stampa][printmargins]

I margini della pagina possono essere impostati in {% prefspane Export %} e influenzeranno l'output di stampa e PDF impaginato.

Puoi sovrascrivere le impostazioni dei margini per documento utilizzando la chiave dei metadati `Margins:`. I valori vengono interpretati come punti; i suffissi di unità come `px`, `pt` e `em` vengono ignorati. Utilizza due numeri per i margini verticale e orizzontale (`10 20`) o quattro numeri per superiore, destro, inferiore e sinistro (`10, 20, 10, 20` o `10 20 10 20`). I margini dei metadati sovrascrivono le impostazioni {% prefspane Export %}.

### Intestazioni e piè di pagina [headers-and-footers]

Le intestazioni e i piè di pagina definiti in {% prefspane Export %} appariranno nella parte superiore e inferiore di qualsiasi pagina stampata o salvata in PDF impaginato e nell'esportazione DOCX. Puoi inserire qualsiasi testo in alto a sinistra, in alto al centro, in alto a destra, in basso a sinistra, in basso al centro e in basso a destra. Il testo centrale è allineato al centro della pagina. Le seguenti variabili verranno sostituite nelle stringhe, se utilizzate:

    %title = Titolo del documento
    %data = Data corrente
    %time = Ora corrente
    %page = Numero della pagina corrente
    %totale = Numero totale di pagine
    %path = Percorso del file system del documento
    %filename = Solo il nome del file del documento
    %basename = Il nome del file senza estensione
    %logo/%image = Un logo impostato nell'immagine nelle preferenze Intestazione/Piè di pagina
    %%(testo) = Testo da stampare solo sulla prima pagina
    %h1/h2/h3/h4/h5/h6 = Titoli delle sezioni basati sulle intestazioni Markdown
    %sep(X) = Testo da inserire tra i titoli delle sezioni se esiste una sottosezione

**Stampa e impaginato PDF** risolvi `%h1`--`%h6` utilizzando l'impaginazione di Marked, quindi ogni pagina mostra la gerarchia delle intestazioni visibile su quella pagina. Anche le variabili di metadati `%sep(X)` e `%md_*` sono supportate nell'output di stampa/PDF.

**Esportazione DOCX** incorpora `%logo`/`%image` nell'intestazione o nel piè di pagina di Word (ridimensionato a circa 50 px di altezza, corrispondente all'anteprima di stampa). I segnaposto di intestazione diventano campi Word **STYLEREF** che fanno riferimento agli stili `Heading 1`--`Heading 6` esportati. Word aggiorna questi campi quando il documento viene aperto, in base al layout e alle interruzioni di pagina di Word, non all'impaginazione di anteprima di Marked. `%md_*` Le variabili dei metadati vengono sostituite una volta al momento dell'esportazione, come nella stampa/PDF. `%sep(X)` non viene convertito in intestazioni/piè di pagina DOCX.

`%title` utilizzerà qualsiasi informazione "Titolo:" definita nelle intestazioni dei metadati MultiMarkdown, altrimenti tornerà al nome file senza l'estensione del file. Per definire un titolo utilizzando i metadati MMD, inserire quanto segue nella prima riga del documento:

    Titolo: il titolo del documento

Segui la riga con una riga vuota (o qualsiasi altro metadato che desideri definire, seguito da una riga vuota).

Puoi anche utilizzare qualsiasi chiave di metadati MMD come variabile prefissandola con `%md_` e combinando le parole della chiave come una stringa minuscola. Ad esempio, se il tuo documento ha una chiave di metadati nella parte superiore come:

    Scimmia funky: la scimmia più funky

Quindi utilizzare `%md_funkymonkey` in un campo di intestazione inserirà "La scimmia più divertente" nel documento esportato nella posizione di quell'intestazione. I documenti che non contengono quella particolare chiave lasceranno il campo vuoto, consentendoti di aggiungere selettivamente intestazioni basate sui metadati.

Vedi [Formati di data e ora](Exporting.html#dateandtimeformats) per i codici di formato `%date` e `%time`.

L'impostazione "Offset numerazione pagine" può essere utilizzata per regolare il numero da cui iniziano i numeri di pagina. Ad esempio, se hai un sommario sulla prima pagina e desideri che la numerazione inizi sulla seconda pagina come pagina 1, imposta l'offset su -1. La pagina 2 sarà ora la pagina 1 nell'intestazione/piè di pagina (`%page`) e il totale delle pagine (`%total`) verrà modificato di conseguenza.

Puoi anche specificare un carattere di intestazione/piè di pagina per un documento specifico utilizzando i metadati MMD nella parte superiore del file:

    Carattere dell'intestazione: Mensch

Tieni presente che se utilizzi il nome di una famiglia di caratteri, verrà selezionato un carattere predefinito. È possibile specificare una variazione utilizzando il nome di sistema del font. Ad esempio, nel caso di Helvetica Neue Ultralight, utilizzeresti "Header Font: HelveticaNeueUltralight".

Inoltre, puoi specificare una dimensione del carattere di intestazione/piè di pagina per documento con i metadati:

    Dimensione carattere intestazione: 10

### Formati di data e ora [dateandtimeformats]

I campi **Formato data** e **Formato ora** in {% prefspane Export %} controllano il modo in cui `%date` e `%time` vengono visualizzati nelle intestazioni e nei piè di pagina. Entrambi i campi utilizzano codici di formato in stile strftime: un `%` seguito da una lettera. Il testo letterale (come `-`, `:` o spazi) viene copiato così com'è.

**Esempi**

    %m-%d-%Y → 20-06-2026 (formato data predefinito di Marked)
    %I:%M %p → 15:45 (formato orario predefinito di Marked)
    %Y-%m-%d → 20/06/2026
    %B %d, %Y → 20 giugno 2026
    %a %H:%M → venerdì 15:45

**Codici formato comuni**

| Codice | Esempio | Descrizione |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Anno a quattro cifre |
| `%y` | 26| Anno a due cifre |
| `%m` | 06| Mese (01--12) |
| `%B` | Giugno | Nome completo del mese |
| `%b` | Giu | Nome abbreviato del mese |
| `%d` | 20| Giorno del mese (01--31) |
| `%e` | 20| Giorno del mese (riempito con spazio) |
| `%A` | Venerdì | Nome completo del giorno della settimana |
| `%a` | Ven | Nome abbreviato del giorno della settimana |
| `%H` | 15| Ora, 24 ore (00--23) |
| `%I` | 03| Ora, 12 ore (01--12) |
| `%M` | 45| Minuto (00--59) |
| `%S` | 07| Secondo (00--59) |
| `%p` | PM | AM o PM |
| `%x` | (locale) | Data preferita dal locale |
| `%X` | (locale) | Orario preferito dalla località |
| `%c` | (locale) | Data e ora preferite dalla lingua |

**PDF stampati e impaginati** supportano lo stile strftime completo impostato sopra, oltre a codici aggiuntivi come `%j` (giorno dell'anno), `%U`/`%W` (numero della settimana), `%z` (offset del fuso orario) e `%Z` (nome del fuso orario). Vedi la [Specifica strftime di Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) per un riferimento completo.

**Esportazione DOCX** supporta i codici elencati nella tabella sopra. I codici meno comuni possono essere ignorati o trasmessi senza modifiche.

Utilizza **Ripristina formati predefiniti** in {% prefspane Export %} per ripristinare a `%m-%d-%Y` e `%I:%M %p`.

### Intestazioni e piè di pagina per documento [per-document-headers-and-footers]

Puoi specificare intestazioni e piè di pagina in base al documento utilizzando i metadati MultiMarkdown nella parte superiore del documento:

    Stampa intestazione a sinistra: %title
    Centro intestazione stampa: %basename
    Stampa intestazione destra: %date
    Stampa piè di pagina a destra: %pagina/%totale

Questi sovrascriveranno qualsiasi impostazione nelle preferenze. Tieni presente che se utilizzi un processore diverso da MultiMarkdown e non vuoi che le intestazioni vengano visualizzate nel documento stesso, puoi utilizzare i commenti HTML, assicurandoti di lasciare una riga vuota prima della chiusura del commento:

    <!--
    Stampa intestazione a sinistra: %title
    Centro intestazione stampa: %basename
    Stampa intestazione destra: %date

    -->

## Salva PDF [save-pdf]

Questa opzione salva l'anteprima direttamente in un file PDF sul tuo disco. Il tuo documento verrà visualizzato nella sua interezza, senza interruzioni di pagina. Per includere l'impaginazione nell'output, utilizzare le opzioni Stampa/PDF nel [Pannello di esportazione](#cassetto).

## Opzioni di esportazione RTF [rtfexportoptions]

Marked può esportare dati RTF (Rich Text Format) direttamente negli appunti. Basta scegliere il comando Copia Rich Text dal menu a forma di ingranaggio.

Marked può anche salvare il file come file **RTFD** (Rich Text Format). Il formato RTFD è un formato bundle che include un file RTF e tutte le immagini incorporate nel documento.

## Esportazione DOCX [docx-export]

L'esportazione come DOCX creerà un documento Microsoft Word valido, con elementi come titoli, intestazioni/piè di pagina, enfasi, elenchi, ecc., tutti mappati su stili Word validi. Ciò significa che puoi applicare facilmente il tuo tema in Word.

Vedere [Lavorare con DOCX][DOCX] per ulteriori dettagli sull'importazione e l'esportazione di Word.

## Esporta Markdown in EPUB [export-markdown-to-epub]

Marked può esportare documenti EPUB validi al 100% e accessibili al 100%. Seleziona il tipo di esportazione EPUB, specifica i metadati come titolo, autore e data e, facoltativamente, aggiungi una foto di copertina. Il file salvato sarà leggibile in qualsiasi visualizzatore EPUB.

I metadati necessari per l'esportazione EPUB possono essere inclusi nel file stesso, che si tratti di un documento Markdown, di un file Scrivener (include una pagina `metadata`) o di un altro formato di libro. Le chiavi da utilizzare sono:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

La chiave Immagine di copertina può includere un percorso relativo al documento di base o un percorso assoluto. Sono accettabili file PNG o JPG.

Se il titolo non è impostato, verrà utilizzato per impostazione predefinita il nome file del documento originale e, se l'autore non è impostato, verrà utilizzato per impostazione predefinita il nome completo dell'utente macOS.

La data sarà sempre impostata sulla data corrente e al momento non può essere modificata con i metadati. Tuttavia, può essere modificato al momento del salvataggio, purché la formattazione (ISO) rimanga intatta.

### Pubblicazione su Amazon Kindle (KDP) [publishing-to-amazon-kindle-kdp]

EPUB è un formato aperto utilizzato da molte app e negozi di lettura (Apple Books, Kobo e altri), non solo Kindle. Se stai pubblicando tramite [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), esporta EPUB da Marked e carica il file su KDP. Amazon lo converte nel proprio formato di consegna Kindle (KFX) per i lettori.

KDP accetta diversi formati di manoscritti, inclusi EPUB e DOCX (che Marked può anche esportare). Consulta i [formati di eBook supportati](https://kdp.amazon.com/en_US/help/topic/G200634390) e la [guida alla formattazione dei manoscritti di eBook](https://kdp.amazon.com/en_US/help/topic/G200645680) di Amazon per i requisiti.

**MOBI non è obbligatorio.** KDP non accetta più caricamenti MOBI per nuovi titoli (inclusi libri a layout fisso, a partire da marzo 2025). Marked non esporta MOBI e non è necessario un file "Kindle" o Mobipocket separato per KDP. Se preferisci gli strumenti di layout di Amazon, puoi anche preparare un libro con [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), che produce file KPF.

Prima del caricamento, potresti voler controllare come apparirà il tuo EPUB sui dispositivi Kindle utilizzando [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuito di Amazon. Si tratta di un software opzionale di terze parti di Amazon, non parte di Marked.

## Esporta profili [export-profiles]

I profili di esportazione ti consentono di salvare e passare rapidamente tra diversi set di preferenze di esportazione. Ciò è particolarmente utile se esporti regolarmente documenti per scopi diversi, ad esempio un profilo per PDF pronti per la stampa con margini e intestazioni specifici e un altro per HTML pronto per il Web con stili incorporati.

### Utilizzo dei profili di esportazione [using-export-profiles]

Quando avvii Marked per la prima volta, viene creato automaticamente un profilo "Predefinito" con le impostazioni di esportazione correnti. Puoi visualizzare e selezionare i profili nelle finestre di dialogo di esportazione (Esportazione PDF, Salva HTML, ecc.) utilizzando il menu a comparsa del profilo nella parte superiore della finestra di dialogo.

**Creazione di un nuovo profilo:**

1. Modifica le impostazioni di esportazione in {% prefspane Export %} o in qualsiasi finestra di dialogo di esportazione
2. Nella finestra di dialogo di esportazione, fai clic sul menu a comparsa del profilo e scegli "Aggiungi profilo..."
3. Inserisci un nome per il tuo profilo (ad esempio, "Qualità di stampa" o "Esportazione Web")
4. Le impostazioni correnti vengono salvate come quel profilo

**Caricamento di un profilo:**

- Seleziona un profilo dal menu a comparsa in qualsiasi finestra di dialogo di esportazione
- Tutte le impostazioni di esportazione verranno aggiornate immediatamente per corrispondere ai valori salvati del profilo

**Salvataggio delle modifiche a un profilo:**

- Dopo aver apportato modifiche alle impostazioni di esportazione, accanto al popup del profilo viene visualizzato un pulsante "Salva".
- Fai clic su "Salva" per aggiornare il profilo corrente con le modifiche
- Il pulsante è abilitato solo quando sono presenti modifiche non salvate

**Gestione dei profili:**

- Scegli "Gestisci profili..." dal menu a comparsa del profilo per aprire la finestra di gestione del profilo
- Da lì puoi:
  - **Rinomina** i profili facendo doppio clic sul nome
  - **Duplica** un profilo per crearne uno nuovo basato su di esso
  - **Elimina** profili (il profilo "Default" non può essere eliminato)
  - Visualizza tutti i profili disponibili in un elenco

### Cosa catturano i profili di esportazione [what-export-profiles-capture]

I profili di esportazione salvano tutte le preferenze relative all'esportazione, tra cui:

- **Impostazioni PDF**: dimensioni della pagina, margini, intestazioni/piè di pagina, caratteri, interruzioni di pagina, sommario
- **Esportazione HTML**: incorporamento di stili, incorporamento di immagini, evidenziazione della sintassi, rendering matematico
- **Elaborazione markdown**: disposizione del testo, formattazione dei collegamenti, regole del processore
- **CriticMarkup**: tipo di esportazione e opzioni di elaborazione
- **Evidenziazione della sintassi**: rilevamento della lingua ed evidenziazione delle preferenze
- **Rendering matematico**: integrazione MathJax/KaTeX e numerazione delle equazioni
- **Gestione delle immagini**: opzioni di incorporamento, comportamento di copia, impostazioni del percorso
- **Tipografia**: Sillabazione, vedove/orfani, dimensioni dei caratteri
- **Comportamento di esportazione**: preferenze di denominazione dei file, risoluzione dei conflitti

I profili funzionano con tutti i tipi di esportazione: Markdown, HTML, PDF continuo, PDF impaginato, EPUB, DOCX, ODT, TextBundle, RTF e OPML.

### Archiviazione del profilo [profile-storage]

I profili sono archiviati nella cartella Supporto applicazioni in:

    ~/Library/Application Support/Marked/ExportProfiles.plist

Ciò significa che i tuoi profili persistono anche se ripristini le preferenze dell'app e sopravvivono agli aggiornamenti dell'app. Puoi eseguire il backup di questo file per preservare i tuoi profili tra le installazioni.

### Suggerimenti per l'utilizzo dei profili di esportazione [tips-for-using-export-profiles]

- **Crea profili per flussi di lavoro comuni**: se esporti regolarmente per la stampa anziché per il web, crea profili separati per ciascuno
- **Utilizza nomi descrittivi**: i nomi dei profili come "Stampa - Lettera" o "Web - Stili incorporati" chiariscono lo scopo di ciascun profilo
- **Salva frequentemente**: il pulsante "Salva" viene visualizzato ogni volta che apporti modifiche: fai clic su di esso per conservare le modifiche
- **Inizia da profili esistenti**: utilizza "Duplica" nella finestra di gestione per creare variazioni di profili esistenti anziché iniziare da zero

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_With_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center