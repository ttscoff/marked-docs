<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked fornisce impostazioni predefinite per migliorare la tipografia e il layout di esportazione, oltre a offrire un controllo limitato sulle opzioni se è necessaria una maggiore personalizzazione.

## Tipografia

### Sillabazione e vedove

L'opzione _Sillabazione automatica nei paragrafi_ consente a Marked di determinare dove è meglio sillabare una riga per migliorare lo "straccio" di un paragrafo. Ciò è particolarmente utile quando si utilizza uno stile con allineamento giustificato, ma può migliorare il flusso di lettura anche nei paragrafi più lunghi.

L'opzione _Previeni vedove nei titoli e nei paragrafi_, se abilitata, forzerà le interruzioni nei titoli e nei paragrafi per evitare che singole parole brevi finiscano da sole su una riga.

Contrassegnato collega automaticamente i titoli con l'elemento seguente, per evitare titoli orfani durante l'esportazione in un formato impaginato (PDF, stampa).

### Segni di punteggiatura

Se il tuo processore è impostato su MultiMarkdown, avrai la possibilità di abilitare o disabilitare la "punteggiatura intelligente" utilizzando l'opzione _Genera virgolette e punteggiatura tipograficamente corrette_. Se abilitato, le virgolette doppie e singole accoppiate verranno trasformate in virgolette "curve", gli apostrofi verranno sostituiti con simboli tipograficamente corretti e verranno eseguite altre regolazioni automatiche.

### Indicatori di nota a piè di pagina

Nella sezione Layout e tipografia di {% prefspane Style %}, _Circonda gli indicatori di nota a piè di pagina con parentesi quadre_ è abilitato per impostazione predefinita quando si utilizza il processore MultiMarkdown e crea indicatori di nota a piè di pagina all'interno del documento che sono circondati da parentesi quadre (ad esempio "[1]"). Per disabilitare la creazione delle parentesi quadre, deseleziona questa opzione.

## Modalità contorno

La modalità Struttura visualizzerà qualsiasi file contenente una serie gerarchica di intestazioni come struttura APA o decimale. L'impostazione predefinita è lo stile APA, ma è possibile disattivarlo.

In {% prefspane Style %} sotto "Layout e tipografia", puoi aggiungere estensioni di nomi file per le quali la modalità Struttura è automaticamente abilitata. Ciò è particolarmente utile per OPML e i file di mappe mentali supportati (come iThoughtsX e MindNode). L'estensione dovrebbe essere solo la parte alfanumerica del nome file che appare dopo l'ultimo punto.

Attiva o disattiva la modalità struttura predefinita con la casella di controllo _Utilizza stile APA_. Questo può essere attivato temporaneamente dal menu Ingranaggio della finestra del documento.


##Poesia

L'opzione _Stile codice letterale blocchi come poesia_ in {% prefspane Style %} farà sì che i blocchi rientrati di 4 o più spazi vengano visualizzati utilizzando lo stile "poesia" del tema. Di solito si tratta di una sezione in corsivo senza evidenziazione della sintassi.

Le interruzioni di riga vengono conservate in questi blocchi per impostazione predefinita, quindi fornisce un modo semplice per incorporare sezioni di poesie e testi in un documento che non necessita di altri blocchi di codice.

> Questa impostazione aggiunge una classe corpo "poesia" che può essere utilizzata in temi personalizzati per definire lo stile di blocchi di codice e altri elementi quando la "modalità poesia" è abilitata.

## Avvolgimento del blocco di codice

L'opzione _Consenti ai temi di racchiudere il testo all'interno dei blocchi di codice_ consente allo Stile di anteprima di determinare come formattare i blocchi di codice. La disabilitazione di questa opzione forza tutti i blocchi di codice a scorrere l'overflow orizzontale anziché a capo, indipendentemente dallo stile di anteprima corrente.

## Funziona a schermo intero

Quando utilizzi Contrassegnato in modalità a schermo intero (Control-Comando-F), potresti voler limitare la larghezza del testo visualizzato per creare una colonna centrata di contenuto leggibile. La casella di controllo _Limita larghezza del testo nell'anteprima_ abiliterà un dispositivo di scorrimento con il quale è possibile definire la larghezza massima del contenuto visualizzato. Ciò influisce anche sulla visualizzazione non a schermo intero.