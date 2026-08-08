<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane General %}:

![Impostazioni: Generale][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Finestra [window]

Mantieni le nuove finestre in primo piano
: imposta automaticamente le nuove finestre in modo che "fluttuino" sopra altre applicazioni.

Alza la finestra durante l'aggiornamento
: quando viene rilevata una modifica in un file controllato, la finestra di anteprima per quel documento si alzerà sopra le altre finestre sul desktop senza attivare Contrassegnato.

Traslucido sullo sfondo
: dissolve la finestra quando non è a fuoco. Utilizza il cursore per impostare l'opacità.

Disattiva le funzionalità ad uso intensivo di memoria sui documenti di grandi dimensioni
: disabilita alcune funzionalità che richiedono un utilizzo intensivo del processore, come i titoli comprimibili quando i documenti superano i 100.000.

Si aprono nuovi documenti
: scegli **finestre**, **schede** o **automatico** (segui le impostazioni del sistema macOS per la scheda). Quando utilizzi le schede, naviga con {% kbd cmd shift [/] %} e il [pannello di apertura rapida](Quick_Open.html).

Porta in primo piano il documento aggiornato
: quando un'anteprima viene aggiornata, seleziona la sua scheda o ordina la sua finestra in primo piano **all'interno di Solo contrassegnati**. Se un'altra applicazione è in primo piano (ad esempio il tuo editor di testo), Marked rimane in background: viene selezionata la scheda corretta in modo che sia pronta quando torni a Marked. Per visualizzare l'anteprima sopra tutte le applicazioni senza attivare Contrassegnate, utilizza invece **Alza finestra all'aggiornamento**.

Riporta lo stato attivo sull'app precedente
: se abilitato, se un'azione di aumento/avvio dell'aggiornamento fa sì che Marked venga messo a fuoco in primo piano, lo stato attivo della tastiera viene restituito all'app che era in primo piano prima dell'aggiornamento (ad esempio l'editor di testo). Quando disabilitato, Marked non esegue mai questo trasferimento del focus. Se Marked non diventa in primo piano, questa opzione non ha effetto.

### Barra di stato [status-bar]

Mostra selettore di stile
: mostra il selettore di stile nella barra inferiore della finestra di anteprima.

Mostra il conteggio delle parole
: mostra il conteggio delle parole (e il pulsante delle statistiche) nella barra inferiore della finestra di anteprima.

Il conteggio delle parole esclude
: i calcoli del conteggio delle parole possono ignorare qualsiasi combinazione di:

- **Note a piè di pagina/Citazioni**
- **Blocco di virgolette**
- **Blocchi di codice rientrati** (i blocchi di codice protetti sono sempre esclusi)
- **Didascalie immagini**

### Scorciatoie [shortcuts]

Fare clic sul campo del collegamento per registrare una combinazione di tasti di scelta rapida che attiva un evento:

Attiva Segnato
: Passa a Selezionato quando si preme questo tasto di scelta rapida in qualsiasi applicazione.

Alza la prima finestra
: porta in primo piano la finestra di anteprima contrassegnata in primo piano (ultima attiva) senza uscire dall'applicazione corrente.

Apri la tavolozza delle azioni
: apre la palette dei comandi [Azioni rapide](Quick_Actions.html) mentre è attivo Segnato. Questa scorciatoia si applica a {% appmenu File, Quick Actions… %} e funziona solo all'interno di Marked (non da altre applicazioni).

Reimposta avvisi
: ripristina tutte le finestre di dialogo di avviso precedentemente ignorate in modo che possano essere visualizzate nuovamente.