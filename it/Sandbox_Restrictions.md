<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La versione Mac App Store (MAS) di Marked viene eseguita in un ambiente sandbox che limita determinate operazioni per motivi di sicurezza. Ciò può influire su alcune funzionalità, in particolare quando si utilizzano processori personalizzati con file binari o script esterni.

## Restrizioni comuni del Sandbox [common-sandbox-restrictions]

### Esegui i binari dei comandi [run-command-binaries]

Il problema più comune riscontrato dagli utenti è che i file binari esterni non possono essere eseguiti direttamente nella versione MAS. Ciò influisce:

- **Processori esterni** come Pandoc, Kramdown o altri strumenti da riga di comando
- **Script personalizzati** che si basano su file binari esterni
- **Utilità di sistema** non accessibili dalla sandbox

### Soluzioni alternative [workarounds]

#### Copia dei file binari nell'app bundle [copying-binaries-to-the-app-bundle]

Se devi utilizzare processori esterni come Pandoc nella versione MAS, puoi copiare il file binario nell'app bundle:

1. Fare clic con il pulsante destro del mouse su Marked.app → **Mostra contenuto pacchetto**
2. Vai a **Contenuti/Risorse/**
3. Crea una cartella `bin` se non esiste
4. Copia il tuo file binario (ad esempio, `pandoc`) in questa cartella `bin`
5. Rendilo eseguibile: `chmod +x` il binario
6. Nell'azione Esegui comando, fare riferimento ad esso come:
   - `YOUR_BINARY_NAME [arguments]`
   - Oppure utilizza il percorso completo: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Nota**: gli script con shebang esterni (come gli script Python che puntano a `/opt/homebrew/bin/python`) verranno automaticamente eseguiti tramite interpreti di sistema quando copiati nel bundle. La versione MAS potrebbe ancora avere problemi nell'esecuzione di file binari che in realtà sono script Python o Ruby invece di file binari.

**Importante**: dovrai copiare nuovamente i file binari dopo ogni aggiornamento dell'app, poiché gli aggiornamenti sostituiscono l'intero pacchetto.

#### Utilizzo degli script incorporati [using-embedded-scripts]

Invece di eseguire comandi esterni, puoi utilizzare l'azione **Esegui script incorporato** in Regole personalizzate. Ciò ti consente di scrivere script direttamente nell'editor di codice di Marked, che può accedere agli interpreti di sistema disponibili nella sandbox.

## Passaggio alla versione non sandbox [crossgrade]

Se hai spesso bisogno di utilizzare file binari esterni o riscontri altre limitazioni di sandboxing, potresti voler passare alla versione senza sandbox di Marked. La versione senza sandbox non presenta tali restrizioni e può eseguire qualsiasi strumento o script da riga di comando installato.

### Per gli utenti in abbonamento [for-subscription-users]

Se hai un abbonamento attivo al Mac App Store:

1. **Annulla il tuo abbonamento MAS** in Impostazioni di sistema → ID Apple → Media e acquisti → Abbonamenti
2. **Scarica la prova gratuita** da [https://markedapp.com](https://markedapp.com)
3. **Attiva un abbonamento Paddle** direttamente tramite l'app o il sito web

La versione Paddle offre le stesse funzionalità senza restrizioni di sandboxing.

### Per i titolari di sblocco permanente [for-permanent-unlock-holders]

Se hai acquistato uno sblocco permanente o una licenza a vita tramite il Mac App Store, invia un'e-mail a sviluppatore](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Please%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.) a richiedi una licenza gratuita a vita di Paddle.

**Importante**: per verificare il tuo acquisto, includi uno dei seguenti elementi nella tua email:

- Il tuo **identificatore utente** (UUID): usa **Aiuto->Copia UUID** per copiarlo negli appunti, quindi incollalo nella tua email
- Il tuo **ID transazione** dalla ricevuta dell'App Store (puoi trovarlo nella cronologia degli acquisti nell'app App Store)

Il Mac App Store non fornisce il tuo indirizzo email agli sviluppatori, quindi verifichiamo gli acquisti utilizzando gli ID transazione o gli identificatori utente memorizzati sul nostro server. Includere queste informazioni ci aiuterà a verificare rapidamente il tuo acquisto e a generare la tua licenza Paddle gratuita.

### Versione Setapp [setapp-version]

In alternativa, se disponi di un abbonamento Setapp, puoi utilizzare la versione Setapp di Marked, anch'essa senza sandbox e con accesso completo alle risorse di sistema.

## Risorse aggiuntive [additional-resources]

Per ulteriori informazioni sui processori personalizzati e sulle relative funzionalità, vedere [Processore personalizzato](Custom_Processor.html).