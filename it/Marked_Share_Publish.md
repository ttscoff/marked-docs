<!-- MT draft for it — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** è il servizio di pubblicazione online di Marked su [share.markedapp.com](https://share.markedapp.com). Collega il tuo Mac una volta, quindi pubblica il documento iniziale come **TextPack** con immagini ed evidenziazioni opzionali della modalità di lettura. Chiunque abbia il collegamento può visualizzare il documento sul Web.

Questa funzionalità è separata dall'**estensione Condividi** di macOS (menu Condividi di sistema). Vedi [Using the Share Extension](Share_Extension.html) per inviare file o selezioni a Marked da altre app.

## Collega il tuo account [connect-your-account]

Prima della prima pubblicazione, collega Marked al tuo account Share:

1. Scegli {% appmenu File, Pubblica, Collega account… %}.
2. Marked apre il browser predefinito per accedere a share.markedapp.com.
3. Dopo aver approvato la connessione, il browser ritorna a Marked con un collegamento di accesso sicuro. Conferma l'etichetta dell'account mostrata nella finestra di dialogo.

Marked memorizza il token API e la chiave del dispositivo nel portachiavi macOS su questo Mac. Le credenziali non vengono scritte nei registri o nei rapporti sugli arresti anomali.

Per disconnettersi, scegliere {% appmenu File, Pubblica, Scollega account… %}. I documenti pubblicati rimangono online; revocare l'accesso in qualsiasi momento su share.markedapp.com, se necessario.

## Pubblica un documento [publish-a-document]

Con un documento aperto nell'anteprima, scegli {% appmenu File, Pubblica, Pubblica… %}.

La prima volta che pubblichi un documento, Marked mostra un piccolo foglio di opzioni:

- **Titolo**: mostrato su Condividi (per impostazione predefinita è il nome del documento senza la sua estensione).
- **Visibilità**: privato, non elencato o pubblico. Per impostazione predefinita le nuove pubblicazioni sono **Non in elenco** (raggiungibile tramite collegamento, non elencato pubblicamente).
- **Stile di lettura**: Editoriale, Manoscritto, Svizzero, Contrasto, Macchina da scrivere o **Nessuno**. Predefiniti dallo stile di anteprima del documento quando possibile. Condividi lo usa come suggerimento; i lettori possono sovrascriverlo. Scegli **Nessuno** per pubblicare senza uno stile suggerito.
- **Includi evidenziazioni e commenti**: incorpora le evidenziazioni della modalità di lettura nel TextPack. Per impostazione predefinita è attivo quando il documento presenta evidenziazioni.
- **Consenti ad altri di remixare**: se abilitato, gli spettatori possono eseguire il fork del documento su Condividi.

Marked crea un TextPack in background (Markdown, risorse e `highlights.json` facoltativo), lo carica e registra l'URL di condivisione su questo Mac.

### Aggiorna una pubblicazione esistente [update-an-existing-publish]

Dopo aver collegato un documento a Condividi, la voce di menu riporta **Aggiorna documento pubblicato** anziché **Pubblica…**. Sceglilo per caricare una nuova versione TextPack. Marked invia l'hash del contenuto del server in modo che vengano rilevate le modifiche simultanee da un altro Mac o dal Web.

Se qualcun altro ha aggiornato prima il documento su Condividi, Marked chiede se **Sovrascrivere** con la versione di questo Mac, **Apri sul Web** o **Annulla**.

## Dopo la pubblicazione [after-publishing]

Al termine della pubblicazione, Marked conferma il successo e offre:

- **Copia link di condivisione** — {% appmenu File, Pubblica, Copia link Share %}
- **Apri sul Web** — {% appmenu File, Pubblica, Apri sul web %}

Questi comandi si applicano al documento iniziale quando ha un record di pubblicazione collegato.

## Finestra Documenti pubblicati [published-documents-window]

Scegli {% appmenu File, Pubblica, Documenti pubblicati… %} per aprire un elenco di documenti pubblicati da questo Mac e sincronizzati dal tuo account Share.

Per ogni voce puoi:

- **Apri** il file locale quando Marked ha ancora un collegamento ad esso sul disco.
- **Importa** un TextPack quando non è presente alcun file locale (salvalo ovunque e aprilo in Marked).
- **Apri sul Web** o **Copia collegamento** per l'URL di condivisione.
- **Rivela nel Finder** quando è noto un percorso locale.
- **Dimentica** rimuove il record da questo Mac senza eliminare il documento online.

L'elenco si aggiorna da Condividi quando sei connesso. Se sei offline o disconnesso, Marked mostra i record memorizzati nella cache e potrebbe chiederti di riconnetterti.

## Cosa puoi pubblicare [what-you-can-publish]

Puoi pubblicare qualsiasi documento che Marked possa visualizzare, tra cui:

- Salvati Markdown e file di testo
- Anteprime temporanee (appunti, streaming o documenti non salvati)
- TextBundles e altri formati supportati

Viene eseguita una sola operazione di pubblicazione alla volta per finestra del documento; la voce di menu è disabilitata mentre è in corso un caricamento.

## Suggerimenti [tips]

- La pubblicazione include le immagini a cui fa riferimento l'anteprima. I pacchetti molto grandi potrebbero essere rifiutati prima del caricamento; riduci le risorse incorporate se raggiungi un limite di dimensione.
- I momenti salienti esportati in TextPack utilizzano il formato JSON dei momenti salienti di Marked. Vedi [Reading Mode](Reading_Mode.html) per creare ed esportare i momenti salienti.
- Marked Share è disponibile nelle versioni Direct, Mac App Store, Setapp e Marked Pro. Per la pubblicazione non è richiesto alcun abbonamento separato.
