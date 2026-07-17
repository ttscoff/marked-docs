<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Lo strumento da riga di comando `mk` fornisce un facile accesso alle funzionalità di Marked dal terminale, consentendo l'automazione del flusso di lavoro e l'integrazione con script di shell e altri strumenti da riga di comando.

## Installazione [installation]

Il modo consigliato per installare `mk` è con Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Se non usi Homebrew, scarica e installa il pacchetto firmato:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

Dopo aver scaricato `mk.pkg`, fai doppio clic su di esso e segui le istruzioni del programma di installazione.

## Utilizzo di base [basic-usage]

### Apertura dei file [opening-files]

Apri un file di markdown in Contrassegnato dalla riga di comando:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Streaming di contenuti da STDIN [streaming-content-from-stdin]

Trasmetti i contenuti direttamente all'anteprima di streaming di Marked:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

La finestra Anteprima streaming si aprirà e visualizzerà il contenuto in tempo reale mentre viene trasmesso da altri comandi.

## Riferimento ai comandi [command-reference]

### Operazioni sui file [file-operations]

**`mk [file]`** — Apri un file markdown in Marked

**`mk [file] --raise`** — Apri il file e alza la finestra sopra tutte le altre

### STDIN e streaming [stdin-and-streaming]

**`mk`** o **`mk -`**: leggi da STDIN e apri l'anteprima dello streaming

**`mk --stream`**: apre la finestra di anteprima dello streaming senza leggere STDIN

### Gestione dell'anteprima [preview-management]

**`mk --refresh`** — Aggiorna la finestra di anteprima in primo piano

**`mk --refresh all`** — Aggiorna tutte le finestre di anteprima aperte

**`mk --refresh file.md`** — Aggiorna l'anteprima per un file specifico (se aperto)

### Preferenze [preferences]

**`mk --pref`** — Apri le preferenze selezionate (pagina Generale)

**`mk --pref Advanced`** — Apre le preferenze su una pagina specifica

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Imposta le preferenze dell'utente (sono consentite più coppie)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Gestione dello stile [style-management]

**`mk --style NAME`** — Imposta lo stile di anteprima per le finestre aperte

**`mk --add-style FILE`** — Aggiungi un file CSS come stile personalizzato a Marked

```bash
mk --add-style ~/Styles/custom.css
```

### Esecuzione JavaScript [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`**: esegui JavaScript nella finestra in primo piano

**`mk --dojs "SCRIPT" all`** — Esegui JavaScript in tutte le finestre

**`mk --dojs "SCRIPT" file.md`** — Esegui JavaScript in file specifici

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Estrazione e importazione di contenuti [content-extraction-and-import]

**`mk --extract URL`** — Estrai il contenuto dall'URL e aprilo in Marked

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`**: apre la finestra Importa URL (facoltativamente con URL)

**`mk --stylestealer [URL]`** — HUD Open Style Stealer (facoltativo con URL)

### Comandi di utilità [utility-commands]

**`mk --paste`** — Crea un nuovo documento dagli appunti

**`mk --preview TEXT`**: visualizza l'anteprima del testo direttamente in un nuovo documento

**`mk --dingus`** — Apri Markdown Dingus per testare i processori

**`mk --help`** o **`mk -h`**: mostra le informazioni sull'utilizzo

**`mk --version`** o **`mk -v`**: mostra le informazioni sulla versione

## Esempi [examples]

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Integrazione [integration]

### Alias della shell [shell-aliases]

Aggiungi al tuo `~/.zshrc` o `~/.bash_profile`:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Script [scripts]

Usa `mk` negli script di shell per l'automazione:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Flussi di lavoro [workflows]

Combina con altri strumenti:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

##Sorgente aperta

Lo strumento da riga di comando `mk` è open source e disponibile su GitHub:

**https://github.com/ttscoff/mk**

Puoi:
- Visualizza il codice sorgente
- Contribuire ai miglioramenti
- Segnalare problemi
- Crea dal codice sorgente, se necessario

Lo strumento è scritto in Swift e può essere compilato utilizzando Xcode. Vedi [README](https://github.com/ttscoff/mk) per le istruzioni di costruzione.

##Versione

Controlla la versione `mk` installata con:

```bash
mk --version
```

## Funzionalità correlate [open-source]

- Consulta [Gestore URL](URL_Handler) per ulteriori informazioni sullo schema URL di Marked
- Vedi [Anteprima in streaming](Streaming_Preview) per i dettagli sulla funzione di anteprima in streaming
- Vedere [Integrazione del flusso di lavoro](Workflow_Integration) per esempi di automazione