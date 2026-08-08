<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked include un'**estensione Condividi** di macOS che compare nel menu Condividi di sistema. Usala per inviare un file o testo selezionato a Marked senza cambiare app o copiare URL a mano.

L'estensione Condividi è **inclusa in Marked 3**. Non si scarica né si installa separatamente. È presente nelle build Direct, Mac App Store, Marked Pro e Setapp.

## Come funziona [how-it-works]

Quando scegli **Marked** da un menu Condividi, Marked si apre subito. Non c'è una finestra di composizione intermedia.

### Condividere un file [share-a-file]

Da **Finder** (o un'altra app che condivide file), scegli **Condividi → Marked**.

Marked riceve il percorso del file e lo apre con lo stesso gestore URL `x-marked-3://open` usato altrove. Il file si apre in Marked come un documento trascinato sull'icona del Dock o scelto con {% appmenu File, Open... ({{cmd}}O) %}.

Sono supportati URL di file, file locali e URL web quando l'app di origine li fornisce.

### Condividere testo selezionato [share-selected-text]

Seleziona testo in un'app come **TextEdit**, **Safari** o **Mail**, poi scegli **Condividi → Marked**.

Marked mette il testo negli appunti e apre un'**anteprima transitoria** con il gestore `x-marked-3://paste`. È lo stesso tipo di anteprima non salvata di {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Puoi salvarla dopo con {% appmenu File, Save Transient Preview %}.

Testo semplice, HTML, RTF e Markdown sono supportati quando l'app di origine li fornisce.

Vedi [URL Handler](URL_Handler.html) per i dettagli dei comandi sottostanti.

## Usare il menu Condividi [using-the-share-menu]

### Da Finder [from-finder]

1. Fai clic destro su un file Markdown o di testo (oppure selezionalo e clicca **Condividi** nella barra degli strumenti del Finder).
2. Scegli **Marked** dal menu Condividi.

Se **Marked** non è visibile, vedi [Abilitare l'estensione Condividi](#enable-the-share-extension) sotto.

### Da una selezione di testo [from-a-text-selection]

1. Seleziona il testo da anteprare.
2. Apri il menu **Condividi** dell'app (voce Condividi, pulsante barra strumenti o menu contestuale).
3. Scegli **Marked**.

Marked si avvia (o passa in primo piano) con un'anteprima del contenuto condiviso.

## Abilitare l'estensione Condividi [enable-the-share-extension]

Marked deve essere installato in `/Applications` (o nella cartella Applicazioni abituale) e avviato almeno una volta prima che macOS elenchi la sua estensione Condividi.

### Attivare Marked in Impostazioni di sistema [turn-on-marked-in-system-settings]

1. Apri **Impostazioni di sistema**.
2. Vai a **Generali → Elementi login e estensioni** (su alcune versioni di macOS: **Privacy e sicurezza → Estensioni**).
3. Clicca **Estensioni** (o il pulsante **ⓘ** accanto a Estensioni).
4. Seleziona **Condivisione** (o **Sharing**).
5. Attiva **Marked**.

### Aggiungere Marked al menu Condividi di un'app [add-marked-to-an-apps-share-menu]

Anche con l'estensione attiva a livello di sistema, ogni app sceglie quali destinazioni Condividi mostrare:

1. Apri un'app con Condividi (Finder e TextEdit sono utili per provare).
2. Apri il menu **Condividi**.
3. Scegli **Modifica estensioni…** (su macOS più vecchi: **Altro…** o **Preferenze estensioni…**).
4. In **Condividi**, seleziona **Marked**.
5. Opzionalmente trascina **Marked** più in alto nell'elenco per un accesso più rapido.

Le modifiche si applicano subito nella maggior parte delle app.

## Se Marked non compare in Condividi [if-marked-does-not-appear-in-share]

W> L'estensione Condividi è disponibile da Marked 3.1.9. Assicurati di aver aggiornato almeno a quella versione.

Prova questi passaggi in ordine:

1. **Avvia Marked una volta** dopo installazione o aggiornamento. Chiudi e riapri Marked se hai appena aggiornato.
2. **Conferma che l'estensione è attiva** in Impostazioni di sistema come descritto sopra.
3. **Personalizza il menu Condividi** nell'app da cui condividi. macOS nasconde le destinazioni poco usate finché non le attivi.
4. **Più copie di Marked:** se hai installato le build Direct e Mac App Store, solo la copia in esecuzione registra la sua estensione. Rimuovi o rinomina l'altra copia, poi avvia quella desiderata.
5. **Riavvia il Mac** se l'estensione non compare dopo un aggiornamento. macOS memorizza nella cache la registrazione delle estensioni Condividi.
6. **Reinstalla Marked** in `/Applications` se stai testando una build copiata manualmente da Xcode o da un'immagine disco. L'estensione deve essere in `Marked.app/Contents/PlugIns/`.

## Suggerimenti [tips]

- L'estensione Condividi è ideale per anteprime rapide di frammenti web, paragrafi di email o note senza creare prima un file.
- Per pagine intere o selezioni complesse dal browser, le [estensioni del browser](Using_the_Browser_Extensions.html) offrono spesso più controllo (selezione sezione, Markdownify URL, ecc.).
- I file condivisi si aprono come documenti Marked normali con monitoraggio del file. Il testo condiviso apre un'anteprima transitoria finché non salvi.
