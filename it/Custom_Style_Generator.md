<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Il generatore di stili personalizzati è uno strumento basato sul Web che ti consente di creare stili personalizzati per Marked senza scrivere CSS a mano. Fornisce un'interfaccia visiva con controlli per tipografia, colori, spaziatura e altro, con un'anteprima dal vivo che si aggiorna man mano che apporti modifiche.

## Accesso al generatore

Il generatore di stili è disponibile su [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). Puoi usarlo direttamente nel tuo browser web: non è richiesta alcuna installazione.

![Generatore di stili][img-style-generator]

  [img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Per iniziare

Quando apri il generatore per la prima volta, vedrai:

- **Riquadro di anteprima** (a sinistra): un'anteprima dal vivo del tuo stile applicato al contenuto di markdown di esempio
- **Riquadro controlli** (a destra): tutti i controlli di stile organizzati in sezioni
- **Barra degli strumenti** (in alto): titolo dello stile, selettore del tema di base e opzione di importazione CSS

### Scelta di un tema base

Inizia selezionando un **Tema base** dal menu a discesa. Ciò fornisce una base per il tuo stile: puoi quindi personalizzarne ogni aspetto. Le opzioni più popolari includono Vuoto (per iniziare da zero), Predefinito e vari temi integrati.

### Importazione di CSS esistenti

Se disponi di un file CSS esistente che desideri utilizzare come punto di partenza, fai clic su **Importa CSS** e seleziona il file. Il generatore caricherà quegli stili e potrai quindi modificarli utilizzando i controlli.

## Controlli di stile

Il generatore organizza i controlli in sezioni logiche:

### Tipografia di base

Controlla le impostazioni tipografiche fondamentali:

- **Utilizza ritmo**: se abilitato, utilizza una scala tipografica matematica per dimensioni e spaziatura coerenti delle intestazioni
- **Dimensione carattere base**: la dimensione del carattere principale (in genere 16px)
- **Altezza riga**: la spaziatura tra le righe di testo
- **Rapporto di scala**: il rapporto utilizzato per la scala tipografica (influisce sulle dimensioni dell'intestazione)

### Disposizione

Regola spaziatura e rientro:

- **Imbottitura wrapper**: spazio attorno all'area del contenuto
- **Rientro paragrafo**: rientro della prima riga per i paragrafi
- **Rientro elenco**: rientro per gli elenchi
- **Rientro virgolette**: margine sinistro per le virgolette

### Caratteri

Configura famiglie e pesi di caratteri:

- **Caratteri dell'intestazione**: elenco separato da virgole di caratteri per le intestazioni (ad esempio, "Georgia, serif")
- **Caratteri del corpo**: elenco di caratteri separati da virgole per il corpo del testo
- **Peso intestazione**: peso del carattere per le intestazioni (100–900)
- **Peso corpo**: peso del carattere per il corpo del testo
- **Peso grassetto**: spessore del carattere per il testo in grassetto
- **Spaziatura lettere**: spaziatura dei caratteri per intestazioni e corpo del testo

###Caratteri Google

Aggiungi Google Fonts al tuo stile:

1. Digita un nome di carattere nel campo di ricerca (vengono visualizzati i suggerimenti di completamento automatico)
2. Specifica facoltativamente gli stili (ad esempio, "400,400i,700" per normale, corsivo, grassetto)
3. Fare clic su **Aggiungi** per includerlo
4. Utilizza **Sfoglia Google Fonts** per esplorare il catalogo completo con le anteprime

I caratteri aggiunti vengono visualizzati in un elenco sotto i controlli: fai clic su × per rimuoverli.

### Colori

Imposta i colori per vari elementi:

- **Sfondo**: colore dello sfondo della pagina
- **Testo base**: colore del testo predefinito
- **Colore intestazione**: colore per tutte le intestazioni (può essere sovrascritto per livello di intestazione)
- **Colore corpo**: colore del corpo del testo
- **Colore collegamento**: colore per i collegamenti
- **Colore enfasi**: colore per il testo enfatizzato (`<em>`)
- **Colore forte**: colore per testo forte (`<strong>`)
- **Segna sfondo**: colore di sfondo per il testo evidenziato (`<mark>`)

I colori delle singole intestazioni (H1–H6) possono essere impostati separatamente: utilizza **Ripristina** per eliminare una sostituzione e tornare al colore dell'intestazione.

### Modalità oscura

Attiva la **Modalità oscura** per visualizzare in anteprima e configurare i colori della modalità oscura. Se abilitato, vedrai controlli colore separati per le varianti della modalità oscura. Gli stili della modalità oscura si applicano quando `.inverted` è impostato sull'elemento del corpo in Contrassegnato.

Utilizza **Genera colori** per creare automaticamente una tavolozza in modalità scura basata sui colori della modalità luce.

### Immagini

Controllare l'aspetto dell'immagine:

- **Larghezza massima**: larghezza massima per le immagini (ad esempio, "100%", "800px")
- **Raggio bordo**: angoli arrotondati (ad es. "8px", "0")
- **Allineamento**: impostazione predefinita del documento, a sinistra, al centro o a destra

### Citazioni

Citazioni di stile:

- **Larghezza bordo sinistro**: spessore del bordo sinistro
- **Colore bordo sinistro**: colore del bordo sinistro
- **Colore sfondo**: colore di sfondo per le virgolette
- **Stile carattere**: normale o corsivo
- **Margine sinistro**: spaziatura dal bordo sinistro
- **Margine sinistro annidato**: spaziatura per virgolette annidate (può essere "ereditata")

Sono disponibili controlli separati per i blockquote in modalità oscura.

### Elenchi

Configura l'aspetto dell'elenco:

- **Posizione stile elenco**: Interno o Esterno (dove compaiono punti elenco/numeri)
- **Margine sinistro**: spaziatura dal bordo sinistro
- **Margine sinistro nidificato**: spaziatura per elenchi nidificati (può essere "ereditato")

### Elenchi di definizioni

Elenchi di definizioni di stile (`<dl>`, `<dt>`, `<dd>`):

- **Rientro DL**: rientro generale
- Impostazioni **DT** (termine): dimensione, peso e stile del carattere
- Impostazioni **DD** (definizione): dimensione, spessore, stile e rientro del carattere

### Tabelle

Stile completo della tabella:

- **Colore sfondo**: sfondo della tabella
- **Colore bordo**: colore del bordo per le celle
- **Colore testo tabella**: colore predefinito del testo nelle tabelle
- **Righe/colonne alternate**: attiva lo zebra striping con colori personalizzati
- **Bordo**: mostra/nascondi il contorno della tabella
- **Griglia**: mostra/nascondi le linee della griglia interna
- **Allineamento**: a sinistra o al centro
- **Raggio del bordo**: angoli arrotondati
- **Larghezza massima**: larghezza massima del tavolo
- **Imbottitura cella**: spaziatura interna
- Impostazioni **Intestazione**: peso, dimensione e stile del carattere
- Impostazioni **Didascalia**: peso, dimensione, stile e colore del testo del carattere

Sono disponibili controlli separati per le tabelle in modalità oscura.

### Blocchi di codice

Blocchi di codice di stile e codice in linea:

- **Famiglia di caratteri codice**: stack di caratteri a spaziatura fissa
- **Sfondo**: colore dello sfondo
- **Colore bordo**: colore del bordo
- **Raggio del bordo**: angoli arrotondati
- **Modalità Wrap**: Nessun wrap (pre), Conserva + wrap (pre-wrap) o Normale (wrap)
- **Padding codice**: spaziatura interna

Sono disponibili controlli separati per i blocchi di codice in modalità oscura.

### Note a piè di pagina

Note di stile:

- **Colore contrassegno**: colore dei contrassegni delle note a piè di pagina
- **Colore testo**: colore del testo della nota a piè di pagina
- **Stile carattere testo**: normale o corsivo

Sono disponibili controlli separati per le note a piè di pagina della modalità oscura.

### Ombra esterna

Aggiungi ombre esterne agli elementi:

1. Scegli l'ombra **Intensità**: Leggera, Media o Forte
2. Seleziona a quali elementi applicare le ombre:
   - Immagini
   - Blocchi di codice
   - Blockquote
   - Tabelle

## CSS personalizzato

Per una personalizzazione avanzata oltre ai controlli disponibili, utilizza il pulsante **CSS personalizzato** per aprire un editor di codice. Qualsiasi CSS aggiunto qui verrà aggiunto allo stile generato e verrà automaticamente adattato per funzionare all'interno della struttura del documento di Marked.

L'editor include l'evidenziazione e la convalida della sintassi: i CSS non validi verranno contrassegnati con messaggi di errore.

## Anteprima dal vivo

Il riquadro di anteprima mostra lo stile applicato al contenuto di markdown di esempio, tra cui:

- Titoli (H1–H6)
- Paragrafi con varie formattazioni in linea
- Tabelle
- Blocchi di codice
- Immagini
- Elenchi (ordinati e non ordinati)
- Blockquote
- Elenchi di definizioni
- Note a piè di pagina
- Elenchi di attività

Le modifiche si aggiornano in tempo reale mentre regoli i controlli.

## Salvataggio e condivisione

Una volta che sei soddisfatto del tuo stile, hai diverse opzioni:

### Visualizza CSS

Fai clic su **Visualizza CSS** per vedere il CSS completo generato in un popover. Puoi copiarlo negli appunti o rivederlo prima di salvarlo.

### Salva CSS

Fai clic su **Salva CSS** per scaricare il tuo stile come file CSS. Ti verrà richiesto di inserire i metadati (titolo, autore, descrizione) prima del download.

### Aggiungi a contrassegnato

Fai clic su **Aggiungi a Marked** per aggiungere direttamente lo stile all'installazione Marked. Ciò richiede che Marked sia in esecuzione e si aprirà una finestra di dialogo per confermare il nome dello stile e le informazioni sull'autore.

### Condividi stile

Fai clic su **Condividi stile** per pubblicare il tuo stile nella [Galleria stili contrassegnati](https://markedapp.com/styles) affinché altri possano utilizzarlo. Dovrai fornire:

- Titolo di stile
- Il tuo nome
- URL dell'autore (facoltativo)
- Descrizione
- Nota (opzionale)

Un'anteprima del tuo stile apparirà nella finestra di dialogo di condivisione prima della pubblicazione.

## Metadati

Utilizza la sezione metadati (espandibile tramite il pulsante freccia accanto al titolo dello stile) per impostare:

- **Autore**: il tuo nome (persiste tra le sessioni)
- **URL autore**: il tuo sito web o l'URL del tuo profilo
- **Descrizione**: una descrizione dello stile
- **Nota**: note aggiuntive (non incluse negli stili condivisi)

Questi metadati sono inclusi nell'intestazione del file CSS e utilizzati durante la condivisione degli stili.

## Suggerimenti

- Inizia con un tema base vicino a quello che desideri, quindi personalizza
- Utilizza il tema **Vuoto** se desideri il controllo completo da zero
- Abilita **Ritmo** per una tipografia matematicamente coerente
- Metti alla prova il tuo stile con l'interruttore **Modalità oscura** se prevedi di supportarlo
- Utilizza i **CSS personalizzati** con parsimonia: la maggior parte delle esigenze può essere soddisfatta con i controlli integrati
- Visualizza in anteprima il tuo stile con vari tipi di contenuto prima di condividerlo

## Compatibilità del browser

Il generatore di stili funziona meglio con i browser moderni (Chrome, Firefox, Safari, Edge). Richiede che JavaScript sia abilitato.