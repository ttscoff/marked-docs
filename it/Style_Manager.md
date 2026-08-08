<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Lo Style Manager fornisce un'interfaccia centralizzata per la gestione di tutti i tuoi
Stili integrati e personalizzati. Ti dà il controllo completo su quale
Gli stili vengono visualizzati nei menu, nel loro ordine, nelle scorciatoie da tastiera e altro ancora.

## Apertura della Gestione stili [opening-the-style-manager]

Per aprire Gestione stili, fai clic sul pulsante **Gestisci stili…** nella {% prefspane Style %}
riquadro o utilizzare {% appmenu Style, Manage Styles (~@$m) %}. Puoi anche trascinare i file CSS direttamente nella finestra delle preferenze --- Contrassegnato
li importerà, aprirà Gestione stili e selezionerà la riga appena aggiunta per
tu.

![Gestione stili][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## Il Tavolo dello Stile [the-style-table]

Il Gestore stili mostra tutti i tuoi stili in una tabella ordinabile che si mescola
stili integrati e personalizzati senza soluzione di continuità. Ogni riga della tabella ne contiene diversi
colonne:

### Casella di controllo abilitata [enabled-checkbox]

La casella di controllo **Abilitato** aggiunge o rimuove immediatamente lo stile dallo Stile
menu, popup Stile predefinito e scorciatoie da tastiera. Quando disabiliti uno stile,
è nascosto dai menu ma rimane nella Gestione stili per una facile riattivazione.

Se disabiliti lo stile attualmente attivo, Marked passa automaticamente allo stile
successivo stile abilitato disponibile.

### Colonna del nome [name-column]

La colonna **Nome** mostra il nome visualizzato dello stile. Puoi modificare questo nome
inline cliccando direttamente su di esso; le modifiche persistono e si propagano a ogni menu
dove appare lo stile. Ciò è particolarmente utile per gli stili personalizzati in cui tu
potrebbe volere un nome più descrittivo rispetto al nome del file.

Gli stili incorporati hanno nomi bloccati che non possono essere modificati. Per personalizzare a
nome dello stile incorporato, duplicalo prima per creare una copia modificabile.

### Colonna sorgente [source-column]

La colonna **Sorgente** indica da dove proviene lo stile:

- **Incorporato**: stili forniti con Marked e memorizzati nell'applicazione
  fascio
- **Personalizzato**: stili che hai aggiunto dai file CSS sul tuo disco
- **Duplicato**: stili creati duplicando un altro stile (integrato
  o personalizzato)

### Colonna Azioni [actions-column]

Ogni riga include una pila di **Azioni** con pulsanti per la gestione di quello stile:

**Modifica**: apre il file CSS nell'editor predefinito. Gli stili incorporati non possono esserlo
modificati direttamente: dovrai prima duplicarli per creare una copia modificabile.

**Duplica**: crea una copia dello stile e un nuovo file CSS su disco. Il
il duplicato viene visualizzato immediatamente sotto lo stile originale nella tabella. Questo è
il modo consigliato per personalizzare gli stili incorporati.

**Rivela**: mostra il file CSS nel Finder, semplificando l'individuazione del file
la tua guida. Questo pulsante è disponibile solo per gli stili personalizzati con un percorso file.

**Elimina**: rimuove lo stile da Contrassegnato. Per gli stili personalizzati, ti verranno forniti
l'opzione per rimuovere solo il riferimento (mantenendo il file CSS) o spostare
il file CSS nel Cestino. Gli stili incorporati non possono essere eliminati, ma sì
disabilitato.

**Ripristina**: per gli stili incorporati, questo pulsante ripristina lo stile originale
stato predefinito se è stato modificato. Questo pulsante è visibile solo per
stili incorporati.

## Riordino degli stili [reordering-styles]

Le righe possono essere riordinate tramite trascinamento. Trascina semplicemente una riga di stile su una nuova
posizione nella tabella. L'ordine impostato qui guida:

- L'ordine del menu Stile nei menu di Marked
- Assegnazioni delle scorciatoie da tastiera (`⌘1`–`⌘9` per i primi nove stili abilitati,
  `⌥⌘1`–`⌥⌘0` per i successivi dieci e così via)

Trascina gli stili negli slot delle scorciatoie da tastiera che desideri
occupare.

## Aggiunta di stili [adding-styles]

Esistono diversi modi per aggiungere nuovi stili personalizzati alla Gestione stili:

### Pulsante Aggiungi [add-button]

Fai clic sul pulsante **Aggiungi nuovo stile** per aprire un selettore di file
dove puoi selezionare uno o più file CSS da importare. I file selezionati saranno
aggiunto alla Gestione stili e abilitato per impostazione predefinita.

### Trascina e rilascia [drag-and-drop]

Puoi trascinare i file CSS direttamente nella finestra Gestione stili. Quando trascini
file sulla finestra, verrà visualizzata una sovrapposizione che mostra "Aggiungi uno stile personalizzato" (o
"Aggiungi N stili personalizzati" per più file). Rilascia i file per importarli.

Puoi anche trascinare i file CSS in posizioni specifiche nella tabella: il drop
L'indicatore mostra dove verrà inserito il nuovo stile, permettendoti di controllarlo
sia l'importazione che il posizionamento in un'unica azione.

Anche il trascinamento dei file CSS nel riquadro delle preferenze {% prefspane Style %} lo farà
importarli e aprire automaticamente la Gestione stili.

## Anteprima dal vivo [live-preview]

Il riquadro destro della Gestione stili visualizza un'anteprima dal vivo del selezionato
stile. L'anteprima restituisce un documento campione completo con intestazioni,
elenchi, tabelle, blocchi di codice, virgolette e altri elementi Markdown comuni,
tutto stilizzato con il CSS effettivo dello stile selezionato.

L'anteprima utilizza il file CSS direttamente dal disco, quindi qualsiasi modifica apportata al tuo
l'editor esterno si aggiornerà immediatamente nell'anteprima. Questo rende facile
guarda le tue modifiche in tempo reale mentre sviluppi stili personalizzati.

### Anteprima della modalità oscura [dark-mode-preview]

Una casella di controllo sopra l'anteprima ti consente di alternare tra la modalità chiara e quella scura
anteprime. Ciò è utile per testare l'aspetto degli stili in entrambe le modalità di aspetto,
soprattutto se stai creando stili che si adattano all'aspetto del sistema.

## Scorciatoie da tastiera [keyboard-shortcuts]

La Gestione stili visualizza una legenda sotto la tabella che mostra come funziona la tastiera
vengono assegnate le scorciatoie. I primi nove stili abilitati ricevono {% kbd cmd 1 %} through
{% kbd cmd 9 %} ({% kbd cmd 0 %} è riservato), i dieci successivi ricevono da {% kbd opt cmd 1 %} a {% kbd opt cmd 0 %} e così via. Puoi vedere le scorciatoie da tastiera assegnate nel menu a comparsa Stile su qualsiasi Anteprima.

## Filtraggio degli stili disabilitati [filtering-disabled-styles]

Una casella di controllo nella parte inferiore della finestra consente di mostrare o nascondere le opzioni disabilitate
stili. Quando non è selezionato, vengono visualizzati solo gli stili abilitati, rendendolo più semplice
concentrati e riordina i tuoi stili attivi. Se selezionato, tutti gli stili (abilitati e disabilitati)
vengono visualizzati, consentendoti di gestire la tua raccolta di stili completa.

## Ripristino degli stili incorporati [restoring-builtin-styles]

Il pulsante **Ripristina tutti gli stili incorporati** nella parte inferiore della finestra
ripristina tutti gli stili incorporati al loro stato predefinito. Questo è utile se lo hai
disabilitato gli stili incorporati e desideri riattivarli o reimpostarli
eventuali modifiche apportate agli stili incorporati.

## Suggerimenti [tips]

- **Organizza per frequenza**: trascina gli stili più utilizzati in alto per regalarli
  assegnargli le scorciatoie da tastiera più semplici ({% kbd cmd 1 %}, {% kbd cmd 2 %}, ecc.)

- **Disabilita invece di eliminare**: invece di eliminare gli stili che non stai utilizzando,
  disabilitarli. Rimarranno lontani ma rimarranno disponibili se ne avrai bisogno
  loro più tardi.

- **Utilizza duplicato per la sperimentazione**: duplica uno stile prima di renderlo maggiore
  modifiche in modo da poter sempre tornare all'originale.

- **Anteprima durante la modifica**: mantieni aperta la Gestione stili durante la modifica dei CSS
  file per vedere le modifiche aggiornate in tempo reale nel riquadro di anteprima.

- **Importazione batch**: puoi selezionare più file CSS contemporaneamente quando utilizzi il file
  Aggiungi il pulsante o trascina più file per importarli tutti in un'unica azione.