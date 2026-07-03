<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked include azioni **Scorciatoie** native (Intent app) per l'apertura di file, la modifica degli stili di anteprima e l'esportazione di documenti. Queste azioni vengono visualizzate nell'app Scorciatoie quando cerchi **Contrassegnato** e sono disponibili su **macOS 13 (Ventura)** o versioni successive.

Per l'automazione basata su script con un modello a oggetti completo, consulta [Supporto AppleScript](AppleScript_Support.html). Per i flussi di lavoro basati su URL dalla shell, vedere [Gestore URL](URL_Handler.html).

## Trovare azioni

1. Apri l'app **Scorciatoie**.
2. Crea un nuovo collegamento o modificane uno esistente.
3. Cerca **Marked** nella libreria delle azioni.

Le azioni sono raggruppate in **Documenti** e **Esporta**. Marked registra anche frasi Siri come "Esporta file con Marked" e "Apri in Marked" per scorciatoie rapide.

## Panoramica delle azioni

| Azione | Scopo |
| --- | --- |
| **Apri file in Contrassegnato** | Apri un Markdown o un file di testo in una finestra di anteprima. |
| **Imposta stile anteprima** | Cambia il tema di anteprima per un documento aperto (o apri prima un file). |
| **Apri ed esporta file** | Apri un file, quindi esportalo in un altro formato. |
| **Esporta documento** | Esporta un documento aperto (finestra frontale o un file specifico). |
| **Esporta documenti aperti** | Esporta tutti i documenti attualmente aperti in Marked. |

Tutte le azioni di esportazione restituiscono il file (o i file) esportati come output di scorciatoie **File** in modo da poterli passare al passaggio successivo (Mail, Finder, un'altra app).

## Apri il file in Contrassegnato

**Parametro:** **File** -- il documento da aprire (dal Finder, dal foglio di condivisione o da un passaggio precedente delle scorciatoie).

Contrassegnato apre il file in una finestra di anteprima. Utilizzalo quando desideri visualizzare l'anteprima o modificare in Contrassegnato prima di fare qualsiasi altra cosa.

## Imposta lo stile di anteprima

**Parametri:**

- **Stile** -- stile di anteprima da un selettore (stessi nomi del menu Stile di anteprima e Gestione stili).
- **File** (facoltativo): un file specifico. Se omesso, Marked utilizza il documento anteriore. Se il file non è già aperto, Marked lo apre per primo.

L'impostazione di uno stile ricarica l'anteprima con quel tema (come scegliere uno stile dal menu degli stili di anteprima).

## Azioni di esportazione

Le azioni di esportazione condividono le stesse opzioni principali:

| Parametro | Descrizione |
| --- | --- |
| **Formato** | Markdown, HTML, PDF impaginato, PDF continuo, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack o OPML. |
| **Profilo** (facoltativo) | Un profilo di esportazione salvato da {% prefspane Export %}. |
| **Stile** (opzionale) | Stile di anteprima da applicare prima dell'esportazione (ricaricamento completo dell'anteprima). |
| **Dimensione pagina** (opzionale) | Stampa il nome della dimensione della pagina, ad esempio `A4` o `Letter`. |
| **Margini** (facoltativo) | Abbreviazione del margine (vedi sotto). |
| **Dimensione carattere** (facoltativo) | Dimensione base del carattere in punti per l'esportazione in PDF, ad esempio `14` o `12pt`. |
| **File di output** / **Cartella di output** (opzionale) | Percorso di destinazione. Se omesso, Marked scrive accanto al file sorgente utilizzando l'estensione corretta. |

**Note**

- **PDF impaginato** utilizza la stessa pipeline di layout di stampa di {% appmenu File, Export, Paginated PDF %}. Non è disponibile per i documenti di anteprima HTML non elaborati.
- L'esportazione **HTML** utilizza l'anteprima renderizzata (ciò che vedi in WebView), non il file sorgente Markdown non elaborato.
- **PDF continuo** acquisisce il layout WebView di anteprima corrente.
- **Dimensione carattere** abilita la stessa opzione di dimensione carattere di esportazione/stampa personalizzata da {% prefspane Export %}. Non influisce sui documenti Fountain.

### Apri ed esporta il file

Ideale per i flussi di lavoro del Finder: scegli un file Markdown, aprilo in Marked ed esporta in un solo passaggio.

**Parametri:** **File** (obbligatorio), più le opzioni di esportazione sopra.

Esempio di utilizzo: un'azione rapida che prende i file dal Finder ed esporta **PDF impaginato** con il profilo e lo stile scelti.

### Esporta documento

Esporta un documento che è **già aperto** in Contrassegnato.

**Parametri:**

- **File** (facoltativo): un file aperto specifico. Se omesso, Contrassegnato esporta il documento anteriore.
- Opzioni di esportazione e **File di output** come sopra.

Utilizzalo quando Marked è già in esecuzione e desideri esportare l'anteprima corrente senza riaprire il file.

### Esporta documenti aperti

Esporta **ogni** documento di anteprima attualmente aperto in Contrassegnato.

**Parametri:**

- **Formato** e opzioni di esportazione (profilo, stile, dimensione della pagina, margini, dimensione del carattere).
- **Cartella di output** (opzionale) -- directory per i file esportati. Se omesso, ogni file viene esportato accanto al relativo documento di origine.

Utile per l'esportazione in batch dopo aver rivisto più capitoli o note in Contrassegnato.

## Abbreviazione dei margini

Quando su un'azione di esportazione sono impostati **Margini**, utilizzare una stringa con da una a quattro misurazioni. Unità: `in`, `cm`, `mm`, `pt` o `"` per pollici. Un numero senza unità viene considerato come punti.

| Valore | Significato |
| --- | --- |
| `1in` | Tutti i lati |
| `1in 2in` | Alto e basso `1in`, sinistra e destra `2in` |
| `1in 2in 1in` | In alto `1in`, sinistra e destra `2in`, in basso `1in` |
| `1in 2in 1in 2in` | In alto, a destra, in basso, a sinistra |

Corrisponde alla chiave `margins` nei record di esportazione [AppleScript](AppleScript_Support.html#with-options-properties-record).

## Esempi di flussi di lavoro

### File Finder in PDF

1. **Apri ed esporta file**
2. **File**: input dal foglio di condivisione o dall'azione rapida del Finder.
3. **Formato** -- PDF impaginato.
4. **Stile** -- tema opzionale (ad esempio Amblin).
5. **Profilo** -- profilo di esportazione salvato opzionale.
6. **File di output** -- opzionale; lasciare vuoto per scrivere `filename.pdf` accanto alla fonte.

### Esporta ciò che è aperto in Contrassegnato

1. **Esporta documento**
2. Lascia vuoto **File** per utilizzare la finestra anteriore.
3. Scegli **Formato** e il profilo o lo stile facoltativo.

### Esportazione batch di documenti aperti

1. **Esporta documenti aperti**
2. Scegli **Formato** (ad esempio EPUB).
3. Facoltativamente, imposta **Cartella di output** per raccogliere tutte le esportazioni in un'unica directory.

### Stile quindi esporta (due passaggi)

1. **Imposta stile anteprima**: scegli uno stile (facoltativamente scegli come target un **file** specifico).
2. **Esporta documento**: stesso file o documento iniziale, con il **formato** desiderato.

Puoi anche passare **Stile** direttamente su un'azione di esportazione; Marked applica il tema e attende il ricaricamento dell'anteprima prima di esportare.

## Esporta percorsi e sandbox

- Se **File di output** o **Cartella di output** viene omesso, Marked scrive accanto al documento di origine.
- Contrassegnato può creare cartelle intermedie quando il percorso di esportazione è **all'interno della cartella del documento aperto**.
- Le esportazioni all'esterno della cartella del documento richiedono un percorso scrivibile a cui i contrassegni possono accedere (posizione del documento salvato, segnalibri con ambito di sicurezza o cartelle concesse tramite le finestre di dialogo Apri).

Vedi [Supporto AppleScript](AppleScript_Support.html#export-paths-and-sandboxing) per le stesse regole sandbox.

## Azione Legacy `convert_to`

Il dizionario AppleScript espone ancora **`convert_to`** per la conversione di testo o file Markdown senza un'anteprima aperta. Sono preferibili le azioni dei collegamenti nativi di cui sopra: aprono correttamente i documenti, attendono il caricamento dell'anteprima e supportano l'esportazione di PDF impaginati in modo asincrono.

Vedi [Scorciatoie e `convert_to` nel supporto AppleScript](AppleScript_Support.html#shortcuts-and-convert_to) per i dettagli sul comando legacy.

## Risoluzione dei problemi: le azioni non vengono visualizzate nelle scorciatoie

Indici delle scorciatoie **uno** Identificatore di installazione contrassegnato per bundle (`com.brettterpstra.marked`). Preferisce la copia con il **numero di build più alto** (`CFBundleVersion`), non necessariamente l'app che hai appena creato in Xcode.

Se Contrassegnato non viene visualizzato in **App** nella libreria delle azioni Scorciatoie:

1. Elenca ogni copia sul disco:
   "bash."
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Rimuovere o rinominare le copie obsolete (ad esempio un vecchio `Marked.app` sul desktop o in `/Applications` che è stato copiato da una build **senza** metadati dei collegamenti).
3. Esegui la build che desideri che Shortcuts utilizzi (Xcode **Esegui** o apri direttamente `.app` in DerivedData).
4. Esci e riapri l'app **Scorciatoie**.

Una build che include scorciatoie contiene `Contents/Resources/Metadata.appintents`. Puoi verificare:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

All'avvio, Marked registra `[MKShortcuts] Registering App Intents` in Console.app quando viene eseguita la registrazione (macOS 13+).

## Debug

Abilita la **modalità debug** in {% prefspane Advanced %}. Passaggi di esportazione dei log contrassegnati a livello di informazioni con il prefisso `[AppleScript]` in Console.app e nel visualizzatore log di Marked (la pipeline di esportazione è condivisa con AppleScript).

## Errori

Messaggi comuni quando un'azione fallisce:

- Nessun documento contrassegnato è disponibile (niente di aperto e nessun file specificato).
- Il file non è aperto in Segnato (utilizza **Apri file** o **Apri ed esporta file**).
- Profilo di esportazione o nome dello stile di anteprima sconosciuto.
- Timeout in attesa del caricamento o del ricaricamento dell'anteprima.
- Errori di autorizzazione del percorso di esportazione o errore di generazione del PDF impaginato.