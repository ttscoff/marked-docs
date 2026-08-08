<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

La tavolozza Azioni rapide è un launcher di comandi ricercabile per Marked. Raccoglie le azioni dalla barra dei menu principale e dal **menu a forma di ingranaggio** di anteprima, oltre ai comandi da tastiera di sola anteprima che non vengono visualizzati nei menu (come **Scorrimento automatico**). Usalo quando sai cosa vuoi fare ma non ricordi in quale menu lo contiene.

## Apertura della tavolozza Azioni rapide [opening-the-quick-actions-palette]

Apri la tavolozza con {% kbd shift cmd P %} o da {% appmenu File, Quick Actions… %}. Il pannello appare come una finestra mobile sopra il documento corrente.

Premi di nuovo la stessa scorciatoia o premi **Esc** per chiudere la tavolozza. Se la tavolozza è già aperta, anche la scelta di **Azioni rapide…** dal menu la chiude.

## Personalizzazione della scorciatoia [customizing-the-shortcut]

La scorciatoia predefinita è {% kbd shift cmd P %}. Per modificarlo, apri {% prefspane General %} e registra una nuova combinazione in **Apri tavolozza azioni** nella sezione **Scorciatoie**.

A differenza di **Attiva contrassegnata** e **Alza prima finestra**, il collegamento Azioni rapide funziona solo quando Contrassegnato è l'applicazione attiva. Aggiorna il collegamento del menu {% appmenu File, Quick Actions… %} in modo che corrisponda alle tue impostazioni.

## Cerca e filtra [search-and-filter]

Digita nel campo di ricerca nella parte superiore del pannello per filtrare i comandi in tempo reale. L'abbinamento è confuso e indulgente:

- L'ordine delle parole non ha importanza (`view source` corrisponde a **Attiva/disattiva visualizzazione sorgente**)
- Le iniziali funzionano bene (`sv` corrisponde a **Source View**)
- La corrispondenza compressa trova i comandi senza spazi (`akdoc` corrisponde a **Chiedi informazioni sul documento**)

Ogni risultato mostra il nome del comando a sinistra e la relativa scorciatoia da tastiera (se disponibile) a destra in grigio. Alcuni comandi mostrano anche un percorso breadcrumb (ad esempio `Preview › Autoscroll`) quando l'azione proviene da un sottomenu o dal motore di anteprima.

## Cosa appare nell'elenco [what-appears-in-the-list]

La tavolozza include:

- **Comandi di menu** dalla barra dei menu principale, inclusi menu dinamici come **Stile**, **Cronologia** e schede aperte **Finestra**
- Comandi del **Menu ingranaggio** dalla finestra di anteprima
- **Scorciatoie in anteprima** dalla mappa della tastiera in anteprima (gli stessi comandi mostrati nell'HUD della guida in anteprima), inclusi navigazione, scorrimento automatico, segnalibri, ricerca e altre azioni solo in anteprima

Quando lo stesso comando appare in più di una posizione, Marked mostra il percorso del menu più breve e unisce le informazioni sui collegamenti dai duplicati.

## Navigazione tramite tastiera [keyboard-navigation]

Naviga nella palette Azioni rapide interamente dalla tastiera:

- **Tasti freccia ↑/↓**: spostati nell'elenco filtrato
- **Invio**: esegue il comando selezionato
- **Escape**: chiude la tavolozza
- **Scorciatoie da tasto ⌘**: chiudi la palette ed esegui il comando del menu corrispondente (ad esempio, premi {% kbd cmd U %} per eseguire **Attiva/disattiva visualizzazione sorgente** invece di selezionarlo nell'elenco)

La digitazione semplice (senza il tasto Comando) filtra il campo di ricerca. Le scorciatoie a tasto singolo di sola anteprima come `s` per lo scorrimento automatico filtrano l'elenco; premi **Invio** per eseguire il comando selezionato.

## Esecuzione dei comandi [running-commands]

La selezione di un comando di menu lo invia nello stesso modo in cui lo si sceglie dal menu, comprese le voci del menu dinamico e a ingranaggio.

Selezionando una **scorciatoia per l'anteprima** viene eseguita l'azione associata nell'anteprima attiva (ad esempio, attivare/disattivare lo scorrimento automatico o passare all'intestazione successiva). Questi comandi richiedono un documento aperto con un'anteprima; se non è disponibile alcuna anteprima, la tavolozza si apre comunque ma le azioni di sola anteprima non avranno alcun effetto.

Per il cambio di file correlato, vedere [Apertura rapida](Quick_Open.html). Per i riferimenti completi alla tastiera dell'anteprima, vedi [Scorciatoie da tastiera](Keyboard_Shortcuts.html) o premi {% kbd h %} nell'anteprima per mostrare l'HUD della guida.