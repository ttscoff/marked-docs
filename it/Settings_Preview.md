<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane Preview %}:

![Impostazioni: Anteprima][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Anteprima del comportamento

Abilita la navigazione sulla minimappa
: Genera una mappa visiva del documento che appare quando si preme "0". Può causare brevi ritardi durante il rendering di documenti di grandi dimensioni.

I titoli comprimono le sezioni
: facendo clic su un elemento del titolo si comprime la sezione tra esso e il titolo successivo.

Richiede {% kbd cmd %}‑clic
: se questa opzione è selezionata, i titoli verranno compressi/espansi solo quando si fa clic tenendo premuto il tasto Comando.

Sincronizza l'anteprima e lo scorrimento della sorgente
: quando il tuo editor lo supporta, mantieni l'anteprima fatta scorrere in modo che corrisponda alla posizione corrispondente nel documento di origine.

Sincronizza la lettura veloce con la posizione di scorrimento
: Mantieni la sovrapposizione [Lettura veloce](Speed_Reading.html) allineata con la posizione di scorrimento dell'anteprima. Puoi anche attivare questa opzione dalla sovrapposizione Lettura veloce.

### Scorri per modificare

Scorri per modificare
: Quando si aggiorna l'anteprima, Marked può determinare il primo punto in cui il documento è cambiato e scorrere automaticamente fino ad esso. Ciò mantiene l'anteprima sincronizzata con la posizione corrente nel documento che stai modificando. L'indicatore di modifica più recente rappresenta la prima differenza nel documento dall'ultimo aggiornamento. Abilitando "Ordine differenze inverti" si considererà invece l'ultima differenza nel documento (dall'alto al basso) come la modifica più recente.

Mostra l'indicatore di modifica più recente
: Un piccolo contrassegno rosso appare nel punto della prima modifica rilevata. Disattivalo per renderlo invisibile. (Richiede **Scorri per modificare**.)

Mostra tutti gli indicatori di differenza
: Se è abilitato, tutte le differenze tra l'ultimo aggiornamento e il contenuto corrente verranno evidenziate nel margine interno. Puoi navigare tra le modifiche, scorrendole fino al centro della vista, usando <kbd>e</kbd> (avanti) e {% kbd shift E %} (indietro).

Ordine differenziale inverso
: Se è abilitato, le differenze verranno contrassegnate in ordine inverso (dal basso verso l'alto). Ciò influisce sulla navigazione, quindi <kbd>e</kbd> navigherà verso l'alto e {% kbd shift E %} navigherà verso il basso. La "modifica più recente" diventerà l'ultima differenza nel documento.

### Funzionalità aggiuntive

Il sommario tiene traccia della posizione di scorrimento
: Il sommario evidenzia la sezione corrente.

Statistiche popup per la selezione del testo
: mostra un popup di conteggio delle parole per il testo selezionato ogni volta che viene effettuata una selezione.

Abilita i popover dei collegamenti
: mostra un menu a comparsa quando si fa clic e si tengono premuti i collegamenti esterni prima del rilascio.

Convalida automaticamente gli URL durante l'aggiornamento
: convalida gli URL al caricamento e all'aggiornamento del documento. Visualizza i risultati solo se sono presenti errori.
: Viene eseguito [convalida collegamento](Link_Validation.html) ogni volta che il documento viene aggiornato (se si dispone di un numero significativo di collegamenti, questo può essere un processo lento e dovrebbe essere evitato).

### Collegamento al wiki

Converti [[Link Wiki]]
: Abilita la [navigazione wiki](Wiki_Navigation.html) di Marked per la sintassi `[[wiki link]]`.

Estensione predefinita
: l'estensione del nome file che Marked utilizza quando si risolvono collegamenti wiki che non includono un'estensione (ad esempio, `md`).

### Aspetto

Modalità oscura
: Visualizza tutte le finestre in modalità "Contrasto elevato", con cromatura scura e, se disponibile, la versione invertita dello stile corrente (potrebbe non applicarsi agli stili personalizzati).

Corrispondenza impostazione di sistema
: cambia automaticamente la modalità oscura quando la modalità oscura di macOS è attivata o disattivata a livello di sistema.

Mostra il percorso completo nel titolo della finestra
: Se abilitato, Marked mostrerà il percorso completo del documento corrente nel titolo della finestra.