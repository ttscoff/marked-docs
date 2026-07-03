<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>


Contrassegnato ti dà il pieno controllo con regole personalizzate, testo
trasformazioni e la possibilità di eseguire i propri comandi o eseguire
diversi processori in base alle proprietà dei file corrispondenti.


## Utilizzo di preprocessori/processori personalizzati

Per aggiungere processori personalizzati, vai su {% prefspane Processor %}
e fai clic su **Regole personalizzate**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


Nell'editor delle regole (noto anche come "Conductor"), puoi aggiungere contenuti personalizzati
regole che hanno criteri per abbinare i file in base al nome file,
percorso, corrispondenze nel contenuto, metadati e persino se
altri file esistono nello stesso albero del documento
aperto. Quando viene soddisfatta una regola, le azioni definite per il
vengono eseguite su quel file.

> Sotto il campo Processore, le caselle di controllo in "Nuovo
> i documenti utilizzano personalizzato:" determina se le regole vengono testate
> affatto per le fasi Preprocessore e Processore. In generale,
> lasciali selezionati, ma se vuoi sovrascriverli completamente
> qualsiasi processore personalizzato, impostalo qui.

![Editor delle regole][2]

  [2]: images/CustomRules-800.jpg @2x larghezza=800

Per creare una nuova regola, usa il `+`
pulsante in fondo all'elenco delle regole a sinistra. Dai il
governare un nome e impostarlo come preprocessore o processore.

I tre punti accanto a una regola indicano Preprocessore, Processore e Abilitato. È possibile evidenziare solo uno tra Preprocessore o Processore ed è possibile fare clic sui punti per modificare gli stati della regola.

Preprocessore
: viene eseguito dopo l'elaborazione iniziale del file, quando Marked aggiunge i file inclusi, gestisce le preferenze di stile come i ritorni a capo di GitHub, ecc., ma prima della fase di elaborazione. A questo punto il documento è ancora Markdown grezzo ed è possibile apportare modifiche al contenuto da passare al processore. Se nessun processore personalizzato corrisponde o non viene eseguita alcuna azione Esegui processore in un processore personalizzato corrispondente, verrà eseguito il processore predefinito.

Processore
: Un processore personalizzato sostituisce il processore integrato definito in {% prefspane Processor %}. Può gestire tutte le azioni eseguibili da un preprocessore e aggiunge le azioni Esegui comando ed Esegui processore. Ciò consente di eseguire un comando personalizzato, ad es. Pandoc oppure esegui un diverso processore integrato sui file che corrispondono ai criteri.

Tutte le tabelle nell'editor delle regole personalizzate possono essere riordinate in base a
trascinando e rilasciando, in modo da poter influenzare l'ordine in cui
vengono eseguite le regole, l'ordine dei criteri nel predicato
editor e l'ordine delle azioni da eseguire in sequenza.

### Editor dei predicati

![Editor del predicato][predicato]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Una volta aggiunta una regola, utilizzare l'editor dei predicati per definirla
criteri che determineranno se la regola viene eseguita per a
dato file. Utilizzare il menu a discesa sul lato sinistro per selezionare a
criterio, quindi utilizzare i campi comparatore e valore per creare
il predicato.

- _filename_ corrisponde solo al nome del file
- _extension_ corrisponde solo all'estensione del file
- _path_ corrisponde al percorso POSIX (Unix) completo del file
- _tree_ cerca corrispondenze di nomi di file ovunque nel file
  albero delle directory del file
- _text_ corrisponde al contenuto testuale nel file. Usa avanti
  barra attorno al valore del testo per renderlo normale
  ricerca di espressioni.
- _fileIncludes_ verifica se il file contiene inclusi
  file (utilizzando uno qualsiasi dei file [Marked's include
  sintassi](Multi-File_Documents.html)).
- _metaType_ verifica se il file include YAML,
  Metadati MultiMarkdown o Pandoc
- _metadata.X_ verifica chiavi di metadati specifiche come autore,
  data, titolo, ecc.

Per abbinare tutti i file (ovvero un processore personalizzato che sempre
funziona), impostare da `filename` a `contains` `*`. L'asterisco lo farà
agire come un carattere jolly e abbinare tutti i file.

[Aggiungi un predicato] [aggiungi predicato]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Fare clic sul segno più (+) sulla riga del predicato per aggiungere un altro predicato. Tieni premuto Opzione mentre fai clic su + per aggiungere un gruppo booleano che può essere impostato su Tutti (AND) o Qualsiasi (OR).

### Azioni

Utilizza il pulsante *+ Azione* per aggiungere azioni alla regola.

![Aggiungi un'azione][addizione]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Le azioni disponibili includono:

Imposta stile
: imposta lo stile per l'anteprima. Qualsiasi stile integrato o stile personalizzato aggiunto è disponibile.

Esegui comando
: accetta un comando da riga di comando, inclusi eventuali argomenti, e passerà il contenuto del file su STDIN. Il comando dovrebbe restituire l'output risultante su STDOUT.

> **Sandboxing per Mac App Store**: la versione di Marked per Mac App Store (MAS) viene eseguita in un ambiente sandbox che limita l'esecuzione di file binari esterni. Se devi utilizzare processori esterni come Pandoc nella versione MAS, devi copiare il file binario nell'app bundle. Per fare ciò:
>
> 1. Fare clic con il pulsante destro del mouse su Marked.app → Mostra contenuto pacchetto
> 2. Vai a Contenuti/Risorse/
> 3. Crea una cartella `bin` se non esiste
> 4. Copia il tuo codice binario (ad esempio, `pandoc`) in questo
> cartella `bin`
> 5. Rendilo eseguibile: `chmod +x` il binario
> 6. Nell'azione Esegui comando, fare riferimento ad esso come:
>
> `YOUR_BINARY_NAME [arguments]`
> Oppure utilizza il percorso completo:
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Nota**: gli script con shebang esterni (come gli script Python che puntano a `/opt/homebrew/bin/python`) verranno automaticamente eseguiti tramite interpreti di sistema quando copiati nel bundle. La versione MAS potrebbe ancora avere problemi nell'esecuzione di file binari che in realtà sono script Python o Ruby invece di file binari.
> Dovrai ricopiare i file binari dopo ogni aggiornamento dell'app, poiché gli aggiornamenti sostituiscono l'intero pacchetto. In alternativa, utilizza **Aiuto->Crossgrade** per ottenere la versione non sandbox che non presenta tali restrizioni.

Esegui script incorporato
: modifica uno script completo nell'editor di codice integrato. Come Run Command, questo dovrebbe ricevere input su STDIN e restituire output su STDOUT.

Imposta metadati
: aggiunge o imposta metadati. Fornire una chiave e un valore. Se la chiave esiste, il suo valore verrà aggiornato, altrimenti verrà aggiunto. Il tipo di metadati utilizzati verrà determinato automaticamente dal contenuto del file (o dal risultato di un'azione di conversione dei metadati).
: Se non vengono trovati metadati esistenti, i metadati verranno aggiunti in formato MultiMarkdown all'interno di un commento HTML. Marked può leggere questi metadati, ma non verranno visualizzati nell'anteprima, indipendentemente dal processore utilizzato.

Elimina metadati
: elimina i metadati in base alla relativa chiave.

Elimina i metadati
: elimina tutti i metadati. Influisce sui metadati YAML, MultiMarkdown e Pandoc.

Converti Meta YAML in MMD
: converte un blocco di metadati YAML nella parte superiore del file in metadati in stile MultiMarkdown.

Converti MMD Meta in YAML
: converte un blocco di metadati MultiMarkdown in YAML.

Cerca e sostituisci
: esegue una ricerca e sostituzione nel contenuto del file.
: se la stringa di ricerca è racchiusa tra barre (ad esempio `/Project \w+/`), verrà trattata come un'espressione regolare. Puoi utilizzare `$1`, `$2`, ecc. per includere gruppi di corrispondenza nella stringa di sostituzione.
: Il campo di sostituzione supporta alcune sequenze di escape (una barra rovesciata seguita da): `\n` inserisce una nuova riga, `\t` inserisce un carattere di tabulazione, `\\` inserisce una barra rovesciata letterale, `\$` inserisce un simbolo di dollaro letterale (invece di un gruppo di corrispondenza)
: Qualsiasi altra sequenza `\X` viene trattata solo come `X` (la barra rovesciata viene eliminata), quindi `\e` diventa `e`. Un \ finale senza alcun carattere viene conservato come una barra rovesciata letterale.
: utilizzare `[%key]` nella stringa di sostituzione per inserire un valore dai metadati del documento, dalle variabili di ambiente o dal contesto (ad esempio `[%title]`, `[%MARKED_PATH]`). Sono disponibili le chiavi impostate da azioni precedenti nella stessa regola o da una regola precedente. Le chiavi non corrispondenti vengono sostituite con una stringa vuota.

Inserisci il titolo H1
: inserisce un H1 nel documento. Questo può essere estratto dai metadati o dal nome del file.

Intestazioni dei turni
: regola i livelli dell'intestazione, da -5 a +5. Ad esempio, se lo imposti su -1, tutti gli H1 diventeranno H2, gli H2 diventeranno H3, ecc. Impostalo su un numero positivo per aumentare i livelli di intestazione di tale importo.

Normalizza le intestazioni
: questa azione garantirà, se possibile, che ci sia un solo H1 nel documento e regolerà tutti i livelli di intestazione in modo che siano in ordine semantico e non saltino livelli, ad es. da H2 a H4. Se il documento originale è ordinato semanticamente fin dall'inizio, ciò perfezionerà bene la gerarchia.

Inserisci il sommario
: inserisce un sommario. Il TOC può andare dopo il primo H1, il primo H2, oppure all'inizio del file (verrà inserito dopo eventuali metadati).

Inserisci file
: inserisce un file di testo selezionato in un dato punto del documento. Questo può avvenire dopo il primo H1, il primo H2, in alto, in basso o dopo una corrispondenza testuale (usa `/pattern/` per cercare un'espressione regolare).

Inserisci testo
: fornisce un editor popup con il quale è possibile incorporare il testo direttamente nell'azione. Le opzioni di posizionamento sono le stesse di _Inserisci file_.
: utilizzare `[%key]` ovunque nel testo inserito per estrarre valori dai metadati del documento, dalle variabili di ambiente o dal contesto contrassegnato (ad esempio `[%author]`, `[%MARKED_PATH]`). Funziona indipendentemente dal processore utilizzato, quindi non è necessario MultiMarkdown per la sostituzione dei metadati. Sono inclusi i valori di azioni precedenti nella stessa regola (come **Imposta metadati**) o di una regola precedente. Le chiavi non corrispondenti vengono sostituite con una stringa vuota.

Inserisci il file CSS
: inserisce un file CSS selezionato nel documento. Questo verrà caricato dopo qualsiasi selezione di stile e può essere utilizzato per sovrascrivere gli stili esistenti o aggiungerne di nuovi.

Inserisci CSS
: offre un editor CSS popup in cui puoi aggiungere il tuo CSS direttamente all'azione. Questo CSS verrà inserito nella parte superiore del documento, dopo eventuali stili esistenti. L'ordine degli stili inseriti corrisponderà all'ordine delle azioni nella regola.

Inserisci il file JavaScript
: inserisce un file JavaScript selezionato alla fine del documento. Tieni presente che devi utilizzare un'azione *Inserisci JavaScript* con un [hook di aggiornamento](#updatehook) se desideri che lo script si ricarichi ad ogni aggiornamento.

Inserisci JavaScript dall'URL
: utilizzalo per inserire un tag `<script>` collegato a un CDN o altro URL remoto alla fine del documento. Tieni presente che devi utilizzare un'azione *Inserisci JavaScript* con un [hook di aggiornamento](#updatehook) se desideri che lo script si ricarichi ad ogni aggiornamento.

Inserisci JavaScript
: fornisce un editor JavaScript popup con il quale è possibile incorporare JavaScript personalizzato direttamente nell'azione. Questo verrà inserito alla fine del documento e l'ordine di JavaScript eseguito dalla regola sarà determinato dalla sequenza delle azioni, con l'ultima azione aggiunta per ultima.
: Tieni presente che devi utilizzare un [hook di aggiornamento](#updatehook) se desideri che gli script vengano eseguiti con ogni aggiornamento.

URL di collegamento automatico
: Converti qualsiasi URL semplice in `<url>`, che genererà un collegamento ipertestuale in qualsiasi processore.

Esegui collegamento
: esegui un collegamento Apple. Qualsiasi esecuzione di scorciatoia dovrebbe ricevere input da STDIN e restituire output alla fine (Stop e Return Output). Se desideri eseguire azioni che non modificano il testo, imposta l'input su una variabile, esegui le azioni e quindi restituisci la variabile di testo originale alla fine.

Esegui il servizio di sistema
: esegui qualsiasi servizio di sistema in `~/Library/Services`. Il servizio dovrebbe accettare input e restituire output.

Esegui il flusso di lavoro di Automator
: esegui qualsiasi file Automator `.workflow`. L'input verrà passato su STDIN e l'output è previsto su STDOUT.

Continua
: Per impostazione predefinita, una volta che una regola viene soddisfatta, l'elaborazione verrà interrotta (separatamente per preprocessori e processori, in modo che un preprocessore e un processore possano corrispondere). Questa azione imporrà la continuazione della corrispondenza delle regole dopo che la regola ha eseguito le sue azioni.

### Aggiorna Hook

Marked non esegue un aggiornamento completo con ogni aggiornamento, quindi se
hai script che eseguono il rendering di parti del DOM di cui hanno bisogno
per eseguire la funzione di rendering utilizzando l'API Hook di Marked.

L'esempio seguente utilizza Sirena, cosa che in realtà non usi mai
che devi fare, poiché la Sirena è ora inclusa per impostazione predefinita. Ma
ecco come lo faresti se lo includessi manualmente.

Aggiungi un'azione **Inserisci JavaScript** e nella sezione "Modifica JS"
finestra, inizializzare lo script e aggiungere l'hook:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Ciò farà sì che `mermaid.run()` venga eseguito ogni volta
Marked esegue un aggiornamento parziale.

### Regole di prova

Il pulsante _Regole di prova_ sotto l'elenco Regole aprirà a
finestra di dialogo in cui puoi selezionare qualsiasi file Markdown e lo sarà
testato contro tutte le tue regole. Regole che otterranno la corrispondenza
evidenziato con una linguetta verde sul lato sinistro. Durante l'abbinamento
contro un file apparirà un pulsante X che può essere utilizzato per
cancella il test e deseleziona le righe.

## Trascina e rilascia

La finestra di Conductor supporta il trascinamento della selezione migliorato
funzionalità che rilevano in modo intelligente i tipi di file e
fornire azioni appropriate in base al file trascinato. Il
l'implementazione include un sistema di sovrapposizione divisa per il testo
file che consente agli utenti di scegliere tra testare il file
contro le regole o aggiungendolo come azione.

![Trascina e rilascia nelle regole personalizzate][trascina]

[drag]: images/draganddropconductor.jpg @2x width=800

### Rilevamento del tipo di file

Il sistema rileva automaticamente diversi tipi di file e
mostra i messaggi in sovrapposizione appropriati:

- **File CSS** (`.css`): mostra la sovrapposizione "Inserisci file CSS"
- **File JavaScript** (`.js`, `.javascript`): mostra "Inserisci
  JS File"
- **File script** (qualsiasi file eseguibile)): mostra "Esegui
  "Comando" in sovrapposizione
- **File di testo**: mostra la sovrapposizione divisa
- **File eseguibili**: mostra la sovrapposizione "Esegui comando".
- **Estensioni sconosciute**: per impostazione predefinita viene visualizzato il tipo "testo" e viene visualizzato
  sovrapposizione divisa

## Registro processore personalizzato

Se ottieni risultati strani e vuoi dare un'occhiata a cosa sta succedendo, il registro delle regole personalizzate ti mostrerà quali regole vengono eseguite e in quale ordine. Utilizza **Aiuto->Mostra registro regole personalizzate** per aprirlo.

![Registro regole personalizzate][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Esecuzione di più comandi

Una regola può avere più comandi in sequenza. L'uscita di
ogni comando verrà passato al successivo. Se vuoi avere
un comando restituisce qualcosa contemporaneamente a quello di Marked
aggiornamenti in anteprima, assicurati di restituire il contenuto originale
a STDOUT per l'elaborazione del comando successivo o built-in
processore.

Ad esempio, se desideri che un comando aggiorni un PDF
documento utilizzando Pandoc, basta passare il percorso del file originale
(dalle variabili d'ambiente) a Pandoc con apposito
opzioni della riga di comando, quindi ripetere il contenuto STDIN
fuori a STDOUT.

## Bypassando dinamicamente i processori personalizzati

Se un processore personalizzato restituisce "NOCUSTOM" su STDOUT, contrassegnato
terminerà il processore personalizzato e tornerà al file
processore interno predefinito. Ciò ti consente di creare un file
processore personalizzato che può decidere se è necessario o meno
esegui utilizzando le [variabili d'ambiente](#variabili d'ambiente)
di seguito, il nome file o l'estensione del documento, la corrispondenza del contenuto
o altra logica.

Se invece di `NOCUSTOM` ritorna un processore personalizzato
`MULTIMARKDOWN` o `DISCOUNT` (o `GFM`), `KRAMDOWN`, o
`COMMONMARK`, verrà utilizzato il processore interno
proprio quel documento. Questa modifica non influirà sull'impostazione predefinita
processore impostato in Impostazioni.

## Variabili d'ambiente

L'azione Esegui comando ha un editor di ambiente in cui tu
puoi impostare le tue variabili di ambiente che saranno
disponibile per il comando o lo script. Oltre a questi
variabili personalizzate, Marked ne include alcune proprie.

Marked esegue il processore personalizzato nella propria shell, il che significa
le variabili di ambiente standard non vengono passate automaticamente.
Puoi utilizzare le variabili di ambiente di Marked per aumentare il tuo
possedere nei tuoi script. Marked crea le seguenti variabili
disponibile per l'uso negli script di shell:

**MARKED_ORIGIN**
: la posizione (directory di base) del file di lavoro principale (la cartella del testo di lavoro, Scrivener o file indice).

**PERCORSO**
: Contrassegnato imposta un percorso che include le cartelle eseguibili predefinite e aggiunge la directory nel `MARKED_ORIGIN` sopra. I valori predefiniti sono: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Puoi aggiungerne uno tuo impostando la variabile PATH secondo necessità e aggiungendo o sovrascrivendo il percorso di Marked (ad esempio `PATH=/usr/local/yourfolder:$PATH`).

**CASA**
: la directory home dell'utente che ha effettuato l'accesso. Python e altri script che si basano sull'impostazione della variabile HOME lo rileveranno automaticamente, ma è disponibile per altri usi nei tuoi script.

**MARKED_EXT**
: l'estensione del file primario in fase di elaborazione. Questa variabile consente di creare script di processi diversi in base al tipo di file visualizzato. Ad esempio, se `$MARKED_EXT == "md"` esegui il tuo processore Markdown preferito, ma se `$MARKED_EXT == "textile"` esegui un processore Textile.

**MARKED_PATH**
: questo è il percorso UNIX completo del file principale aperto in Marked al momento del caricamento.

**MARKED_INCLUDES**
: un elenco tra virgolette e separato da virgole dei file che Marked ha incluso nel testo passato utilizzando le varie [include sintassi](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: verrà impostato su "PROCESS" o "PREPROCESS", consentendoti di utilizzare un singolo script per gestire entrambe le fasi in base a questa variabile.

**MARKED_CSS_PATH**
: il percorso completo del foglio di stile corrente

### Variabili di ambiente dei metadati

Quando l'azione Esegui comando viene eseguita in Marked's
Sistema conduttore, i metadati del documento vengono automaticamente
estratti e resi disponibili come variabili di ambiente al file
comando.

#### Come funziona

1. **Estrazione dei metadati**: il sistema estrae i metadati dal documento utilizzando il metodo `extractMetaDataFromString:` esistente, che supporta:
   - Introduzione YAML (`---` blocchi)
   - Metadati MultiMarkdown (chiave: linee di valore)
   - Metadati Pandoc (`%` cartigli)
   - Metadati dei commenti HTML (`<!-- key: value -->`)

2. **Normalizzazione chiave**: le chiavi dei metadati sono normalizzate per essere utilizzate come variabili di ambiente:
   - Convertito in minuscolo
   - Tutti i caratteri non alfanumerici vengono rimossi
   - Spazi e caratteri speciali vengono eliminati

3. **Formato variabile d'ambiente**: ogni chiave di metadati diventa una variabile d'ambiente con il prefisso `MD_`:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Esempio

Dato un documento con questi metadati:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

Sarebbero disponibili le seguenti variabili di ambiente
comandi:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Utilizzo nei comandi

Ora puoi utilizzare queste variabili di ambiente nella tua corsa
Azioni di comando:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Azioni supportate

Questa funzionalità della variabile metadati-ambiente è
disponibile in:

- Azioni **Esegui comando**
- Azioni **Esegui script incorporato**

I metadati vengono estratti automaticamente dal documento
contenuto e reso disponibile a qualsiasi comando o script che
attraversa queste azioni.

## Abilitazione e disabilitazione

I processori personalizzati possono essere attivati e disattivati
singoli documenti utilizzando {% kbd opt cmd C %}. Tu
può anche attivare un preprocessore o un processore per un documento
automaticamente [utilizzando i metadati](#perdocument) nella parte superiore
il documento.

Gli stati attuali dei responsabili del trattamento per ciascun documento sono
visualizzati come indicatori luminosi (visibili solo quando è installato un processore
è abilitato) a sinistra degli elementi della barra degli strumenti in basso
barra degli strumenti destra dell'anteprima.

### Preprocessore

Se imposti le regole del preprocessore, queste vengono eseguite dopo Marked
gestisce qualsiasi attività specifica di Mark, come l'inclusione di attività esterne
documenti e codice, ma prima di eseguire il processore
(interno o personalizzato). Questo ti dà la possibilità di eseguire il rendering
variabili del modello personalizzato, gestire le sostituzioni o iniettare
i tuoi contenuti con qualsiasi altro mezzo.

Marked imposta una variabile di ambiente per il funzionamento
directory (`MARKED_ORIGIN`) nella directory principale del file
file in anteprima. Puoi usarlo per cambiare il funzionamento
directory di uno script e includere file con percorsi relativi
al documento originale. Ad esempio, in Ruby puoi
utilizzare:

	Dir.chdir(ENV['MARKED_ORIGIN'])

Se abilitato, il preprocessore personalizzato può essere attivato e
disattivato per i singoli documenti che utilizzano
{% kbd ctrl opt cmd C %}.

#### Processore/Pre-processore per documento [per documento]

È inoltre possibile impostare processori personalizzati in base al documento
utilizzando il formato dei metadati per [Per-Documento
impostazioni](Per-Document_Settings.html).

È possibile specificare se utilizzare le impostazioni personalizzate del processore e
sovrascrivere l'impostazione predefinita per un documento utilizzando [Per-Document
impostazioni](Per-Document_Settings.html) (`Custom Processor:`
e `Custom Preprocessor:`). Qualsiasi impostazione diversa da "true"
o "sì" disabiliterà il pre/processore personalizzato.

Utilizzo di esempio:

    Processore personalizzato: vero
    Preprocessore personalizzato: falso

Come notato nel [Per-Document
Impostazioni](Per-Document_Settings.html#hidingmeta) pagina, you
può circondare questi metadati con marcatori di commenti HTML da nascondere
da GitHub e altri processori che non lo rimuovono
dall'uscita:

    <!--
    Processore personalizzato: vero
    Preprocessore personalizzato: vero
    -->

## Utilizzo di un processore Markdown alternativo

Qualsiasi versione Markdown che puoi eseguire il rendering dalla riga di comando può
essere utilizzato con Marked. Deve essere in grado di ricevere input
STDIN, che equivale a "convogliare" il tuo Markdown ad esso
riga di comando, ad esempio `cat myfile.md | myprocessor`. Ne ha bisogno
per restituire l'HTML risultante su STDOUT, che ogni
processore con cui abbia mai lavorato lo fa per impostazione predefinita.

Usa `which YOUR_PROCESSOR` nel Terminale per determinare il percorso
nell'eseguibile, quindi incollarlo nel percorso Esegui comando
campo o semplicemente trascinare l'eseguibile nella finestra Regole personalizzate
con la regola a cui vuoi aggiungere l'azione selezionata.

Se il tuo processore richiede argomenti sulla riga di comando,
dovrai inserire anche quelli nel campo. Alcuni
i processori necessitano di trattini per funzionare su STDIN e/o STDOUT,
ad es. `-o - -` spesso segnala l'ingresso da STDIN, l'uscita a
STDOUT. Consulta la documentazione del tuo processore per i dettagli.

Ho testato la funzionalità Processore personalizzato con Pandoc,
Kramdown, contrassegnato (sconto), MultiMarkdown 6, Maruku e
vari altri gusti.

### Una nota su Pandoc e Sandboxing

Pandoc (e alcuni altri strumenti da riga di comando) non verranno eseguiti
la versione Mac App Store (sandbox) di Marked.
Se hai bisogno di eseguire Pandoc, usa **Aiuto->Crossgrade** per ottenere un file
licenza gratuita per la versione diretta (Paddle). Questo è vero
di qualsiasi processore che riscontra problemi di sandboxing: se contrassegnato
non è possibile eseguirlo a causa di problemi di autorizzazioni MAS, lo farà
offrire i passaggi per eseguire il crossgrade. Se riscontri problemi
e questo non sta accadendo, contattami tramite il
[sito di supporto](https://support.markedapp.com/questions/add).

### Pandoc come elaboratore del markdown dell'esercito svizzero

[Pandoc](https://pandoc.org/) è di gran lunga il più flessibile
strumento multiuso per gestire una serie di formati di markup. Di
aggiungendo un argomento `-f` con uno dei seguenti, Pandoc può
essere il tuo processore personalizzato per uno qualsiasi di:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

E un sacco di altri. Vedi il [Pandoc
documentazione](https://pandoc.org/MANUAL.html) per ulteriori informazioni
informazioni. Per utilizzare uno di questi come formato di input, basta aggiungere il file
quanto segue nel campo Esegui comando:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc è perfetto per scrivere uno script che utilizza il file
`$MARKED_EXT` variabile d'ambiente per determinare quale formato
per eseguire Pandoc o utilizzare una serie di regole con
corrispondenze di estensione. Se l'estensione è `md`, usa
`pandoc -f gfm` o `pandoc -f markdown_mmd` (o semplicemente return
`NOCUSTOM` su STDOUT per utilizzare il processore predefinito). Ma se lo è
`textile`, esegui `pandoc -f textile` all'interno dello script. E se
è `wiki`, usa uno dei processori di markup wiki. Ottieni
l'idea.

Come sapranno gli appassionati di Pandoc, Pandoc può anche gestire
ampia bibliografia e scenari LaTeX. La maggior parte delle funzionalità
a cui puoi accedere tramite la riga di comando sono disponibili solo
utilizzando argomenti di passaggio in Marked.

## Utilizzo dei tessuti

Alcune persone hanno chiesto come far funzionare il settore tessile
Contrassegnato. È necessario avere a disposizione un convertitore tessile
la riga di comando. Ci sono alcune opzioni, incluso Pandoc
(vedi sopra), ma se non hai già installato Pandoc,
altre due opzioni sono RedCloth per Ruby e Textile per Perl
(richiede l'installazione degli Strumenti per sviluppatori). Installa
l'uno o l'altro:

1. Installa Textile da
   <https://github.com/bradchoate/text-textile> **O**
   `sudo gem install RedCloth` nel Terminale
2. Utilizzare `which textile` o `which redcloth` per determinare il
   percorso da utilizzare nelle impostazioni del percorso del processore personalizzato

Ora Marked è un anteprima tessile per te!

## Utilizzo di AsciiDoc

1. Installa [AsciiDoctor](http://asciidoctor.org/).
2. Abilita una regola personalizzata in {% prefspane Processor %} per abbinare i tuoi file AsciiDoc.
3. Impostare la regola come processore e aggiungere un'azione Esegui comando
    1. Determina il percorso verso `asciidoc`, che sarà
       qualcosa come `/usr/bin/asciidoc` o
       `/opt/local/bin/asciidoc`. In caso di dubbi, utilizzare
       `which asciidoc` per individuare
    2. Inserisci `[PATH To asciidoc] --backend html5 -o - -` come
       il comando (il - alla fine invia l'output come
       STDOUT)

Questo invia il documento corrente a STDIN e visualizza il file
HTML generato come STDOUT.

Vedi [questo succo](https://gist.github.com/mojavelinux/6324279)
da [Dan Allen](https://gist.github.com/mojavelinux) per
ulteriori informazioni.