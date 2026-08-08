<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Estrai e ruba stili da qualsiasi sito web.

## Cos'è lo Style Stealer? [what-is-the-style-stealer]

Style Stealer è uno strumento che ti consente di estrarre stili CSS da qualsiasi sito Web e applicarli ai tuoi documenti Markdown come [Stili personalizzati](Custom_Styles.html). È perfetto per:

- **Blogger** che desiderano abbinare lo stile dei loro siti Web preferiti
- **Scrittori** che necessitano di creare documenti che corrispondano a un marchio o una pubblicazione specifica
- **Sviluppatori** che desiderano prototipare rapidamente con i sistemi di progettazione esistenti
- **Chiunque** desideri catturare l'aspetto di qualsiasi sito web ben progettato

> Lo Style Stealer dipende da un sito relativamente ben strutturato con chiare divisioni di markup. Non funzionerà su tutti i siti, ma dovrebbe fare un buon lavoro sulla maggior parte.

> Per ottenere i migliori risultati, inserisci una pagina che contenga quanto più contenuto testuale possibile. Ad esempio, per estrarre stili da un blog, apri direttamente a un articolo o post, non alla pagina dell'indice principale.

## Come utilizzare il ladro di stili [how-to-use-the-style-stealer]

### Passaggio 1: apri Style Stealer [step-1-open-the-style-stealer]

Accedi a Style Stealer tramite **Aiuto** → **Style Stealer**.

### Passaggio 2: inserisci un URL [step-2-enter-a-url]

Nel campo URL, inserisci l'indirizzo del sito web da cui desideri estrarre gli stili. Style Stealer funziona con qualsiasi sito Web accessibile al pubblico. Se il sito è protetto da paywall potrebbe essere necessario effettuare l'accesso per poter estrarre il contenuto.

![Anteprima di Style Stealer][anteprima]

  [anteprima]: images/style-stealer-preview.jpg @2x width=800

### Passaggio 3: carica e naviga [step-3-load-and-navigate]

Fai clic su **Estrai** o premi {% kbd return  %} per caricare il sito web. Una volta caricato, puoi:

- **Naviga** nel sito utilizzando Comando+clic sui collegamenti
- **Passa il mouse** sulle aree dei contenuti per vederle evidenziate
- **Fai clic** sull'area del contenuto principale da cui desideri estrarre gli stili

L'area di contenuto principale selezionata deve contenere solo titoli, paragrafi, elenchi e così via. Non selezionare un'area di contenuto che contenga menu, barre laterali o altri contenuti estranei. Spesso un titolo si troverà in un contenitore separato dal normale contenuto del paragrafo. In questi casi, prova prima a selezionare il contenitore più piccolo che li contenga ancora entrambi. Se i risultati sono scadenti, fai di nuovo clic su **Estrai** e seleziona nuovamente solo il contenitore che contiene i paragrafi.

### Passaggio 4: estrai gli stili [step-4-extract-styles]

Quando si fa clic sull'area del contenuto, verranno estratti gli stili applicabili a quell'area. L'anteprima verrà ricaricata con una pagina generica che mostra tutti gli elementi HTML comuni e il modo in cui verranno applicati ad essi gli stili estratti.

Puoi quindi salvare questo stile personalizzato nella cartella CSS personalizzata per utilizzarlo in qualsiasi documento. Fai clic sul pulsante **Salva** o premi {% kbd cmd S %} per salvare. Lo stile verrà denominato in base al dominio dell'URL inserito.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## Cosa viene estratto [what-gets-extracted]

Style Stealer cattura un set completo di stili tra cui:

### Tipografia [typography]

- **Famiglie di caratteri** e dimensioni per tutti i livelli di intestazione (H1-H6)
- Stile del **Paragrafo** inclusa l'altezza della riga e la spaziatura
- **Colori del testo** e colori dello sfondo
- **Peso dei caratteri** e stili (grassetto, corsivo, ecc.)

### Layout e spaziatura [layout-and-spacing]

- **Margini e imbottitura** per tutti gli elementi
- Stili e colori **Bordi**
- **Colori di sfondo** inclusi gli sfondi del corpo per i temi scuri

### Elementi interattivi [interactive-elements]

- **Stili di collegamento** inclusi gli stati al passaggio del mouse e quelli visitati
- **Pulsante** e stile degli elementi del modulo
- Stile **Elenco** (punti elenco, numeri, rientro)

### Caratteristiche speciali [special-features]

- Stile del **Primo paragrafo**
- Formattazione **Blockquote**
- **Codice** e stile del testo preformattato
- Stile **Tabella**
- **Facce di caratteri personalizzati** e caratteri web

## Funzionalità avanzate [advanced-features]

### Blocco dei media [media-blocking]

Style Stealer blocca automaticamente i contenuti multimediali (video, immagini, audio) per evitare arresti anomali e concentrarsi sullo stile del testo. Ciò garantisce un processo di estrazione regolare anche su siti Web ricchi di contenuti multimediali.

### Supporto per pseudo-selettore [pseudo-selector-support]

Lo strumento cattura pseudo-selettori CSS come:

- `:hover` stati per collegamenti e pulsanti
- `:visited` stati dei collegamenti
- `:first-child` Stile dei paragrafi
- `::first-letter` per i capolettera

### Filtraggio intelligente [smart-filtering]

Lo Style Stealer filtra in modo intelligente:

- Stili del browser predefiniti
- Prefissi del fornitore non necessari
- Regole contrastanti o ridondanti
- Stili che renderebbero illeggibile il testo

### Modalità di debug [debug-mode]

Abilita la modalità debug in Style Stealer per visualizzare la registrazione dettagliata del processo di estrazione. Ciò è utile per la risoluzione dei problemi o per comprendere quali stili vengono acquisiti.

## Suggerimenti per ottenere i migliori risultati [tips-for-best-results]

### Scegli l'area contenuto giusta [choose-the-right-content-area]

- Fai clic sull'**area del contenuto principale** della pagina, non su intestazioni, barre laterali o piè di pagina
- Cerca l'area che contiene il testo dell'articolo, il post del blog o il contenuto principale
- Evita aree con JavaScript pesante o contenuto dinamico

### Gestisci i temi scuri [handle-dark-themes]

Style Stealer cattura automaticamente i colori dello sfondo del corpo, rendendolo perfetto per estrarre stili di temi scuri. L'anteprima mostrerà come appaiono i tuoi contenuti con lo stile scuro estratto.

### Considerazioni sui caratteri [font-considerations]

- I **Caratteri Web** vengono acquisiti e inclusi negli stili estratti
  - I caratteri caricati da un URL remoto (ad esempio Google Fonts) manterranno tale URL. I caratteri caricati dagli URL dei dati verranno duplicati nel foglio di stile generato.
- **I caratteri di sistema** verranno ripristinati con garbo su sistemi diversi
- Il **caricamento dei caratteri** potrebbe richiedere qualche istante nell'anteprima

### Testare i tuoi stili [testing-your-styles]

Dopo aver salvato gli stili estratti:

1. Applicateli a un documento di prova
2. Controlla come appaiono con il tuo contenuto reale
3. Apportare modifiche tramite:
   1. Apri {% prefspane Style %}
   2. Seleziona il nuovo stile nella tabella Stili personalizzati
   3. Fare clic su Rivela per mostrare il file nel Finder
   4. Apri il file in qualsiasi editor di testo semplice (TextEdit funzionerà in modalità testo semplice) e apporta le modifiche necessarie

## Risoluzione dei problemi [troubleshooting]

### Il sito web non viene caricato [website-wont-load]

- Verifica che l'URL sia corretto e accessibile al pubblico
- Alcuni siti potrebbero bloccare l'accesso automatizzato
- Prova una pagina diversa sullo stesso sito

### Gli stili sembrano diversi [styles-look-different]

- Gli stili estratti si basano sul contenuto specifico selezionato
- Alcuni siti utilizzano CSS complessi che potrebbero non tradursi perfettamente
- Utilizza CSS aggiuntivi o modifica il foglio di stile per apportare modifiche precise

### Stili mancanti [missing-styles]

- Assicurati di aver selezionato l'area del contenuto principale, non una barra laterale o un'intestazione
- Alcuni stili possono essere applicati tramite JavaScript e non verranno acquisiti
- Controlla la console di debug per informazioni dettagliate sull'estrazione

## Scorciatoie da tastiera [keyboard-shortcuts]

- {% kbd return  %} - Carica l'URL per l'estrazione
- {% kbd cmd S %} - Salva lo stile estratto in un file CSS di stile personalizzato
- {% kbd cmd  %}-Click - Naviga tra i collegamenti durante l'anteprima

## Integrazione con stili personalizzati [integration-with-custom-styles]

Gli stili estratti vengono salvati nella cartella CSS personalizzata e possono essere:

- **Applicato** a qualsiasi documento tramite il menu Stile
- **Modificato** utilizzando qualsiasi editor di testo
- **Condiviso** con altri copiando il file CSS
- **Combinato** con altri stili personalizzati

Style Stealer semplifica la creazione di una libreria di bellissimi stili ispirati ai migliori siti Web su Internet.