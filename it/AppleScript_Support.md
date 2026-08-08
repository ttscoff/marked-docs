<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked include un dizionario AppleScript per automatizzare l'anteprima, l'esportazione e l'integrazione del flusso di lavoro. Puoi aprire documenti, controllare l'anteprima (ricarica, scorrimento, evidenziazioni, scorrimento automatico, lettura veloce), leggere statistiche, modificare processori e stili, copiare HTML o RTF negli appunti ed esportare nella maggior parte degli stessi formati disponibili nel menu {% appmenu File, Export %}. **L'anteprima dei titoli/del sommario tramite AppleScript è in fase di elaborazione** (vedi sotto).

Per l'automazione basata su URL (script di shell, `open` comandi e callback), vedere [Gestore URL](URL_Handler.html). AppleScript e il gestore URL si completano a vicenda: usa AppleScript quando devi indirizzare un documento o una finestra specifica e gli URL quando è sufficiente una semplice chiamata `open 'x-marked://...'`.

## Visualizzazione del dizionario [viewing-the-dictionary]

In **Script Editor**, scegli {% appmenu File, Open Dictionary... %} e seleziona Contrassegnato. Il dizionario elenca i comandi sugli oggetti **applicazione**, **document** e **finestra**, oltre ai comandi di esportazione nella suite Marked.

Su macOS puoi sfogliare le definizioni di script con **Script Editor**.

## Targeting contrassegnato [targeting-marked]

Per l'installazione standard:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Documenti e finestre [documents-and-windows]

**Applicazione**

- `documents` -- documenti di anteprima aperti (elenco ordinato).
- `windows` -- finestre di anteprima.

**Documento**

- `name` -- nome visualizzato.
- `path` -- percorso del file quando il documento viene salvato su disco.
- `modified` -- se il documento presenta modifiche dell'editor non salvate.
- `processor` -- Processore Markdown per questa anteprima (lettura/scrittura). Nomi validi: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. L'impostazione `processor` applica una sostituzione per documento e ricarica l'anteprima; non modifica l'impostazione predefinita globale in {% prefspane Processor %}.
- `preprocessor` -- preprocessore per questa anteprima (lettura/scrittura). Utilizzare `true` o `false` per abilitare o disabilitare il preprocessore personalizzato o il nome del preprocessore, se applicabile.
- `source text` -- sorgente Markdown grezza (sola lettura).
- `critic markup mode` -- se l'elaborazione CriticMarkup è abilitata (lettura/scrittura). Modificandolo si ricarica l'anteprima.
- `is autoscrolling` -- se lo scorrimento automatico è attivo (sola lettura).
- `is speed reading` -- se la modalità di lettura veloce è attiva (sola lettura).
- Comandi di anteprima, lettore, statistiche ed esportazione (vedi sotto).

**Finestra**

- `document` -- il `MarkdownDocument` mostrato in quella finestra.
- `style` -- nome dello stile di anteprima corrente (lettura/scrittura). L'impostazione `style` ricarica l'anteprima con il tema scelto (come scegliere uno stile dal menu degli stili di anteprima).
- `close`, `save`, `print` -- comandi finestra standard.
- Gli stessi comandi di anteprima, lettore, statistiche ed esportazione dei documenti (inoltrati al documento della finestra).

Preferisci `tell document 1` o `tell window 1's document` quando esporti un'anteprima specifica. I comandi di esportazione sull'applicazione utilizzano la finestra chiave o il documento corrente quando non è specificato alcun destinatario.

### Esempio: aprire e leggere il percorso [example-open-and-read-path]

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Esempio: modifica dello stile di anteprima [example-change-preview-style]

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

I nomi degli stili corrispondono al menu dello stile di anteprima (nome visualizzato, nome della risorsa CSS come `swiss` o identificatore interno). Sono supportati gli stili personalizzati aggiunti in Gestione stili.

Utilizzare **`get preview style names`** sull'oggetto applicazione per elencare i nomi visualizzati degli stili abilitati.

### Esempio: processore e testo sorgente [example-processor-and-source-text]

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Comandi dell'applicazione [application-commands]

Questi comandi si applicano all'oggetto **applicazione** (non a un documento specifico).

| Comando | Descrizione |
| --- | --- |
| `open streaming preview` | Apri una finestra [anteprima degli appunti in streaming](Streaming_Preview.html). |
| `preview clipboard` | Apri un'[anteprima degli appunti](Opening_Files.html) del contenuto corrente degli appunti (come {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Chiudi tutti i documenti di anteprima aperti (nessuna richiesta di salvataggio; Contrassegnato non modifica i file di origine). |
| `get available processors` | Elenca i nomi dei processori: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Elenca i nomi visualizzati per gli stili di anteprima abilitati. |
| `get_available_formats` | Elenca i nomi dei formati `convert_to` supportati. |
| `get_available_profiles` | Elenca i nomi dei profili di esportazione (uguali alla proprietà `profiles`). |

Porta Marked in primo piano con il comando AppleScript **`activate`** standard:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Controllo anteprima [preview-control]

Disponibile su **documento** e **finestra**. La maggior parte di questi richiede un'anteprima WebView caricata.

| Comando | Parametri | Descrizione |
| --- | --- | --- |
| `refresh preview` | — | Ricarica l'anteprima dal file sorgente (come {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Rivela il file del documento nel Finder. |
| `show highlights` | — | Abilita l'evidenziazione delle parole chiave (evita parole, alternative, voce passiva, elenchi personalizzati). |
| `full screen` | opzionale `enabled` booleano | Accedi, esci o attiva la modalità di anteprima a schermo intero. |
| `scroll to heading` | `title` o `id` | Scorri fino a un'intestazione tramite il testo del titolo visibile o DOM `id`. |
| `scroll to position` | `percent` o `line` | Scorri in base alla percentuale dell'altezza del documento o al numero di riga approssimativo. |
| `copy html` | — | Copia l'HTML di anteprima negli appunti (menu a forma di ingranaggio o {% kbd shift cmd C %}; vedi [Copia HTML](Exporting.html#copyhtml)). |
| `copy rtf` | — | Copia il testo RTF negli appunti. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Scorrimento automatico e lettura veloce [autoscroll-and-speed-read]

| Comando | Descrizione |
| --- | --- |
| `autoscroll` | Avvia lo scorrimento automatico. Il numero intero opzionale `wpm` imposta le parole al minuto prima di iniziare. |
| `stop autoscroll` | Interrompi lo scorrimento automatico. |
| `pause autoscroll` | Metti in pausa o riprendi lo scorrimento automatico. |
| `speed read` | Avvia o attiva [lettura veloce](Speed_Reading.html). |
| `stop speed read` | Interrompe la lettura veloce. |
| `pause speed read` | Metti in pausa o riprendi la lettura veloce. |

Controlla lo stato con le proprietà del documento `is autoscrolling` e `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Statistiche [statistics]

**`get statistics`** restituisce un `statistics_record` con valori numerici calcolati dall'attuale sorgente Markdown (non le stringhe formattate mostrate nel cassetto delle statistiche).

| Immobile | Descrizione |
| --- | --- |
| `word_count` | Conteggio parole |
| `sentence_count` | Conteggio frasi |
| `character_count` | Conteggio caratteri |
| `paragraph_count` | Conteggio paragrafi |
| `average_words_per_sentence` | Parole medie per frase |
| `average_syllables_per_word` | Sillabe medie per parola |
| `complex_word_percentage` | Percentuale di parole complesse |
| `reading_ease` | Flesch facilità di lettura |
| `fog_index` | Indice della nebbia sparante |
| `grade_level` | Grado di grado Flesch – Kincaid |
| `gulpease` | Indice Gulpease (leggibilità italiana; `0` quando non applicabile) |
| `gulpease_band` | Banda Gulpease `1`–`4` (se applicabile) |
| `reading_time_minutes` | Tempo di lettura a **250 WPM** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Indice (lavori in corso) [table-of-contents-work-in-progress]

{% note %}
**WIP: non ancora affidabile.** Il dizionario include una proprietà **`headings`** e un comando **`headings`** per leggere le intestazioni di anteprima annidate (record `heading_item`). Questa automazione **non funziona correttamente** nelle build attuali (risultati vuoti, errori di coercizione o "nessun risultato restituito"). Verrà risolto in una versione successiva. Preferisco **`scroll to heading`** con un titolo o ID noto fino ad allora.
{% endnote %}

**Comportamento pianificato** (una volta completato): `heading_item` record nidificati dalle intestazioni nell'**anteprima** (`h1`–`h6`), non da Markdown grezzo.

| Immobile | Descrizione |
| --- | --- |
| `title` | Testo dell'intestazione |
| `id` | Attributo DOM `id` (stringa vuota quando assente) |
| `level` | Livello di rotta `1`–`6` |
| `children` | Elenco nidificato di `heading_item` record |

**`headings`** (proprietà del documento): tutti i livelli. **`headings levels {2, 3}`** (comando) — filtro opzionale: solo le profondità di rotta (non un intervallo).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Utilizza i valori `id` con **`scroll to heading id "..."`** una volta che l'automazione delle intestazioni è stabile.

## Stampa con profilo [print-with-profile]

**`print with profile`** applica temporaneamente le impostazioni di stampa di un profilo di esportazione, quindi stampa il documento (stesso pacchetto di preferenze dei profili di esportazione da {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

I nomi dei profili fanno distinzione tra maiuscole e minuscole. Dopo la stampa, Marked ripristina il profilo di esportazione precedentemente attivo.

## Esporta profili [export-profiles]

I profili di esportazione memorizzano gruppi di preferenze di esportazione/stampa (margini, intestazioni, opzioni sommario e impostazioni simili da {% prefspane Export %}).

**Leggi i nomi dei profili**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Esporta con un profilo**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

I nomi dei profili fanno distinzione tra maiuscole e minuscole e devono corrispondere esattamente a un profilo salvato.

## Esporta comandi [export-commands]

I comandi di esportazione sono disponibili sugli oggetti **applicazione**, **documento** e **finestra**. Ogni comando richiede un parametro **`to`** con il percorso di output (stringa del percorso POSIX o oggetto `file`).

| Comando | Uscita |
| --- | --- |
| `export markdown` | Ribasso (.md) |
| `export html` | HTML |
| `export paginated pdf` | PDF impaginato (layout di stampa) |
| `export continuous pdf` | PDF a scorrimento continuo |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | Testo OpenDocument |
| `export textbundle` | Pacchetto di testo |
| `export rtf` | RTF |
| `export opml` | OPML |

**Note**

- Il PDF impaginato utilizza la stessa pipeline da HTML a PDF di {% appmenu File, Export, Paginated PDF %}. Non è disponibile per i documenti di anteprima HTML non elaborati.
- L'esportazione HTML utilizza l'**anteprima renderizzata** (ciò che vedi in WebView), non il file sorgente Markdown non elaborato.
- Il PDF continuo acquisisce il layout WebView di anteprima corrente.

### Esportazione di base [basic-export]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Esporta percorsi e sandbox [export-paths-and-sandboxing]

- Utilizzare un percorso POSIX completo per il file di destinazione.
- Contrassegnato può creare cartelle intermedie quando il percorso di esportazione è **all'interno della cartella del documento aperto** (ad esempio esportando a `.../MyProject/build/output.pdf` durante l'anteprima `.../MyProject/chapter.md`).
- Le esportazioni all'esterno della cartella del documento richiedono un percorso scrivibile a cui i contrassegni possono accedere (posizione del documento salvato, segnalibri con ambito di sicurezza o cartelle concesse tramite le finestre di dialogo Apri). Se il percorso non è scrivibile, il comando restituisce un errore prima dell'avvio dell'esportazione.

## `with` opzioni (registro delle proprietà) [with-options-properties-record]

Invece di `with profile`, puoi passare un record di opzioni utilizzando **`with`** o **`with properties`**:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript riconosce direttamente queste chiavi (vengono mappate prima dell'esportazione):

| Chiave | Descrizione | Esempio |
| --- | --- | --- |
| `style` | Stile di anteprima da applicare prima dell'esportazione (ricaricamento completo dell'anteprima) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Stampa il nome della dimensione della pagina | `"A4"`, `"Letter"` |
| `margins` | Margini di stampa (vedi sotto) | `"1in"`, `"1in 2in"` |
| `fontSize` | Sostituisci la dimensione del carattere base di esportazione/stampa in punti (PDF impaginato e continuo) | `"14"`, `"12pt"` |

`fontSize` abilita la stessa opzione **Dimensione carattere personalizzata per esportazione/stampa** di {% prefspane Export %}. Non influisce sui documenti Fountain, che utilizzano dimensioni fisse della sceneggiatura.

Quando è incluso `style`, Marked applica quel tema, attende il completamento del ricaricamento dell'anteprima, quindi esporta. Non è necessario un passaggio `set style` separato.

Altre chiavi nel record possono corrispondere ai nomi di **preferenza di esportazione** dai profili (le stesse chiavi memorizzate in {% prefspane Export %}, come `printBackgrounds`, `printTOC`, `topPrintMargin`). Tali valori vengono applicati temporaneamente per l'esportazione.

Non puoi combinare fonti contrastanti con noncuranza: se usi `with profile`, carica prima quel profilo; se utilizzi un record `with`, le chiavi del profilo nel record sovrascrivono le impostazioni correnti per quell'esportazione.

### Abbreviazione dei margini [margin-shorthand]

Il valore `margins` è una stringa con da una a quattro misurazioni. Unità: `in`, `cm`, `mm`, `pt` o `"` per pollici. Un numero senza unità viene considerato come punti.

| Valori | Significato |
| --- | --- |
| `1in` | Tutti i lati |
| `1in 2in` | Sopra e sotto `1in`, sinistra e destra `2in` |
| `1in 2in 1in` | In alto `1in`, sinistra e destra `2in`, in basso `1in` |
| `1in 2in 1in 2in` | In alto, a destra, in basso, a sinistra |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Esempio combinato [combined-example]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to` [convert_to]

L'oggetto dell'applicazione espone anche comandi di scripting legacy:

- **`convert_to`** -- converte il testo Markdown o il percorso di un file in un formato (`html`, `pdf`, `epub`, `docx`, `rtf` e altri), opzionalmente con `profile` e `output_path`.
- **`get_available_formats`** -- elenca i nomi dei formati di conversione supportati.
- **`get_available_profiles`** -- elenca i nomi dei profili di esportazione (come la proprietà `profiles`).

`convert_to` rimane disponibile per i flussi di lavoro meno recenti e per l'automazione solo AppleScript.

## Debug [debugging]

Abilita la **Modalità debug** in {% prefspane Advanced %} (o la preferenza di debug in Impostazioni). Marked registra quindi i passaggi di esportazione di AppleScript a livello di informazioni con il prefisso `[AppleScript]` in Console.app e nel visualizzatore di log di Marked.

Righe di registro utili quando si traccia un'esportazione PDF impaginato:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Le esportazioni lunghe (in particolare i PDF impaginati) sospendono l'evento AppleScript fino al completamento in modo che i client non vadano in timeout durante l'esportazione.

## Errori [errors]

Le esportazioni non riuscite impostano la stringa di errore dello script sul comando (visibile in Script Editor e nei gestori `on error`). Messaggi comuni:

- Il percorso di esportazione è obbligatorio.
- La directory di esportazione non esiste (all'esterno della cartella documenti).
- Impossibile creare la directory di esportazione o errore di autorizzazione durante la scrittura del file.
- Nome dello stile di anteprima sconosciuto.
- Timeout in attesa del ricaricamento dell'anteprima dopo la modifica dello stile.
- L'esportazione del PDF impaginato è scaduta o non è riuscita durante la generazione delle pagine.

## Integrazione con altri strumenti [integration-with-other-tools]

Le applicazioni possono utilizzare la superficie AppleScript di Marked per leggere i metadati del documento. Per flussi di lavoro basati su shell, osservatori di cartelle e callback di editor, [Gestore URL](URL_Handler.html) è spesso più semplice. Il [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) include script e servizi aggiuntivi.