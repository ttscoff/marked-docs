<!-- MT-DRAFT: machine translation; human review required -->

# Markdownifier

Markdownifier è uno strumento che estrae automaticamente il contenuto dalle pagine Web e lo converte in un formato Markdown pulito. Elabora in modo intelligente i contenuti web per fornirti solo il testo e la struttura significativi, filtrando annunci, elementi di navigazione e altra confusione.

![URL Markdownify][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Come funziona

Markdownifier utilizza algoritmi avanzati di estrazione dei contenuti per:

1. **Recupera e analizza** il contenuto della pagina web
2. **Identificare il testo e la struttura dell'articolo principale**
3. **Pulisci e formatta** il contenuto nel Markdown corretto
4. **Filtra** pubblicità, navigazione e altri elementi non di contenuto
5. **Preserva** formattazioni importanti come intestazioni, elenchi e collegamenti

## Apertura del Markdownifier

Per accedere al Markdownifier, apri {% appmenu File, New, Markdownify URL (@~k) %}. Inserisci l'URL che desideri Markdownify e premi Invio ({% kbd return %}).

## Utilizzo del Markdownifier

### Utilizzo di base

1. **Apri Markdownifier** utilizzando uno dei metodi sopra indicati
2. **Inserisci un URL** nel campo di testo
3. **Fai clic su "Automatico"** o premi `Return` per estrarre il contenuto
4. Il contenuto estratto si aprirà **automaticamente** in un nuovo documento contrassegnato

### Selezione manuale dei contenuti

Se l'estrazione automatica non acquisisce il contenuto desiderato:

1. Fare clic sul pulsante **"Manuale"** per caricare la pagina in una visualizzazione Web
2. **Naviga e scorri** per trovare il contenuto desiderato
3. **Fai clic sul pulsante "Estrai contenuto"** visualizzato sulla pagina web
4. Il contenuto selezionato verrà convertito in Markdown e aperto in Contrassegnato

### Integrazione degli appunti

Markdownifier rileva automaticamente gli URL negli appunti quando vengono aperti:

- Se viene trovato un URL, verrà **precompilato** nel campo URL
- Devi ancora fare clic su **"Automatico"** o premere `Return` per elaborarlo
- Ciò impedisce l'elaborazione accidentale degli URL degli appunti

## Elaborazione dei contenuti

### Convalida automatica dei contenuti

Markdownifier convalida in modo intelligente il contenuto estratto per garantire che contenga testo significativo:

- **Rimuove i metadati** (frontmatter YAML, intestazioni MultiMarkdown)
- **Rimuove le definizioni dei collegamenti** e i collegamenti in stile riferimento
- **Filtra** URL autonomi ed elementi di navigazione
- **Comprime gli spazi bianchi** per una valutazione accurata della lunghezza
- **Richiede un minimo di 200 caratteri** di contenuto effettivo

Se il contenuto estratto è troppo breve o sembra essere costituito principalmente da navigazione/annunci, Markdownifier tornerà automaticamente alla modalità di selezione manuale.

### Formattazione dei contenuti

Il contenuto estratto viene formattato come Markdown pulito con:

- **Link alla fonte** in alto: `[source](original-url)`
- **Inserimento titolo H1** quando necessario
- **Elenchi conservati** (ordinati e non ordinati)
- **Collegamenti mantenuti** e formattazione enfatizzata
- **Paragrafi puliti** con spaziatura adeguata

## Caratteristiche di sicurezza

### Prevenzione degli incidenti

Il Markdownifier include diverse misure di sicurezza per prevenire incidenti:

- **Blocca URL problematici** (reti pubblicitarie, servizi di tracciamento, contenuti correlati alla crittografia)
- **Filtra le immagini danneggiate** che potrebbero causare problemi di rendering
- **Disabilita funzionalità web avanzate** che potrebbero causare instabilità
- **Ripristino automatico da crash** con fallback in modalità provvisoria

### Tutela della privacy

- **La modalità di navigazione privata** impedisce il tracciamento e i cookie
- **Nessun plugin o esecuzione Java** per motivi di sicurezza
- **JavaScript limitato** con blocco dell'API crittografica
- Il **filtro delle risorse** blocca il tracciamento e il contenuto degli annunci

## Risoluzione dei problemi

### Contenuto non estratto

Se l'estrazione automatica fallisce:

1. **Prova la selezione manuale** utilizzando il pulsante "Manuale".
2. **Verifica se il sito richiede JavaScript**: alcuni siti richiedono il caricamento manuale
3. **Verificare che l'URL** sia accessibile e contenga il contenuto dell'articolo
4. **Cerca paywall o requisiti di accesso** che potrebbero bloccare l'accesso

### Problemi con WebView

Se la visualizzazione Web diventa instabile:

1. Markdownifier **entrerà automaticamente in modalità provvisoria**
2. **JavaScript verrà disabilitato** per evitare arresti anomali
3. **Utilizza il pulsante "Converti"** anziché la selezione manuale
4. **Chiudi e riapri** Markdownifier per reimpostarlo

### Contenuto mancante

Se dall'estrazione mancano contenuti importanti:

1. L'**algoritmo automatico** potrebbe averlo filtrato
2. **Utilizza la selezione manuale** per scegliere il contenuto specifico desiderato
3. **Controlla l'HTML di origine** per vedere se il contenuto è caricato dinamicamente
4. **Prova un URL diverso** se il sito ha una struttura complessa

## Suggerimenti per ottenere i migliori risultati

### Selezione dell'URL

- **Utilizza gli URL degli articoli** anziché la home page o le pagine delle categorie
- **Evita gli URL con parametri di monitoraggio** quando possibile

### Qualità dei contenuti

- Gli **articoli più lunghi** generalmente estraggono meglio dei post brevi
- **Contenuti ben strutturati** con titoli adeguati funzionano meglio
- **Evita siti con JavaScript pesante** per l'estrazione automatica

### Selezione manuale

- **Attendere il caricamento completo della pagina** prima dell'estrazione
- **Scorri il contenuto** per assicurarti che sia tutto caricato
- **Passa il mouse sopra le aree** per selezionare la casella blu più piccola che contiene tutto il contenuto che desideri estrarre
- **Fai clic su** quando hai trovato il contenuto desiderato

## Funzionalità avanzate

### Elaborazione batch

Mentre Markdownifier elabora un URL alla volta, puoi:

- **Acconda più URL** aprendo Markdownifier più volte
- **Utilizza l'integrazione dei servizi** per elaborare URL da altre applicazioni
- **Copia il contenuto estratto** e incollalo nei documenti contrassegnati esistenti

### Integrazione con Marked

Il contenuto estratto si apre in Contrassegnato con:

- **Denominazione automatica dei file** in base al titolo dell'articolo
- **Conservazione dell'URL di origine** nei metadati del documento
- **Funzionalità complete** per la lettura e l'esportazione)

## Dettagli tecnici

### Tipi di contenuto supportati

- **Articoli HTML** con markup standard
- **Post di blog** e articoli di notizie
- **Documentazione** e pagine di aiuto
- **Post del forum** e contenuti delle discussioni

### Limitazioni

- **Siti protetti da paywall** potrebbero richiedere l'accesso e l'estrazione manuale
- I **siti con uso intensivo di JavaScript** potrebbero richiedere la selezione manuale
- I **contenuti dinamici** caricati dopo il caricamento della pagina potrebbero non essere rilevati, ma l'estrazione manuale può catturarli
- I **Layout complessi** potrebbero includere elementi di navigazione indesiderati

Markdownifier è progettato per rendere l'estrazione dei contenuti Web il più semplice e affidabile possibile, fornendo allo stesso tempo opzioni di fallback per siti Web complessi o problematici.