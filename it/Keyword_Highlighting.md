<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Catturare la verbosità problematica e mettere in luce le frasi importanti.

## Evidenziazione delle parole chiave

L'evidenziazione delle parole chiave in Marked ti consente di individuare frasi comuni che potresti voler evitare, trovare termini alternativi o semplicemente evidenziare per scopi generali. L'elenco delle parole chiave utilizzate per corrispondere a ciascuna categoria può essere modificato in {% prefspane Proofing %}.

Abilita l'evidenziazione con {% kbd shift cmd H %}, dal menu a forma di ingranaggio ({% appmenu {{gear}}, Highlight Keywords %}), oppure apri il cassetto delle parole chiave utilizzando l'icona dell'evidenziatore in basso a sinistra (vicino al menu a forma di ingranaggio). Il cassetto può essere aperto anche con la scorciatoia da tastiera {% kbd shift cmd K %}. L'evidenziazione viene abilitata automaticamente quando il cassetto viene aperto e può essere attivata e disattivata con l'interruttore sul lato sinistro del cassetto.

## Il cassetto delle parole chiave

![Cassetto delle parole chiave][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

Il cassetto delle parole chiave che viene visualizzato quando si abilita l'evidenziazione fornisce un rapido accesso alle opzioni di evidenziazione, inclusa la possibilità di abilitare e disabilitare i singoli tipi di evidenziazione. La fila verticale di etichette colorate sul lato sinistro è correlata ai punti salienti del testo. Facendo clic su un'etichetta si attiva/disattiva l'evidenziazione per quel tipo di parola chiave.

A sinistra di ciascuna etichetta c'è un'icona di destinazione. Facendo clic su questo si inizierà a scorrere il documento fino all'istanza successiva dell'evidenziazione nell'ordine dei documenti. A destra dell'etichetta c'è un conteggio che mostra il numero totale di evidenziazioni per quel tipo.

Puoi navigare rapidamente tra i punti salienti utilizzando la tastiera. Digitando `[` e `]` inizialmente ti sposterai avanti e indietro attraverso tutti i punti salienti. Se fai clic sull'icona di un bersaglio, `[` e `]` passeranno alla navigazione solo di quel tipo di evidenziazione. `{` (Shift-[) e `}` (Shift-]) navigheranno sempre tra tutte le evidenziazioni, indipendentemente dall'ultimo bersaglio cliccato.

Se si fa clic su una parola o frase evidenziata, quel tipo diventerà la destinazione della navigazione e utilizzando `[` o `]` si navigherà da quel punto nel documento.

## Modifica delle parole chiave

![Impostazioni correzione bozze][proofprefs]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

Per impostazione predefinita, Marked utilizza l'elenco di parole e frasi di uso eccessivo della [Plain English Campaign](http://www.plainenglish.co.uk). Puoi aggiungerli o sostituirli facilmente modificandoli in {% prefspane Proofing %}. Ogni campo è costituito da testo in formato libero e ogni riga viene interpretata come una frase di ricerca. Utilizza `*` all'inizio di una frase o parola per corrispondere a qualsiasi testo precedente e `?` per corrispondere a un singolo carattere come carattere jolly.

Le espressioni regolari possono essere utilizzate circondando l'espressione con barre:

    /\\S*?ly/

Quanto sopra corrisponderà a qualsiasi parola che termina con "ly" per l'evidenziazione. La sintassi per le espressioni regolari nell'evidenziazione delle parole chiave di Marked è la [stessa di JavaScript](http://www.regular-expressions.info/javascript.html).

## Parole chiave temporanee

Puoi anche aggiungere parole chiave temporanee nel cassetto delle parole chiave modificando il blocco note. Proprio come nei campi {% prefspane Proofing %}, aggiungi una parola chiave o una frase per riga, sono consentite le espressioni regolari (circondate da barre). Dopo aver modificato le parole chiave temporanee, assicurati di fare clic sul pulsante "Aggiorna" (o premere {% kbd cmd return  %}) per salvare le modifiche e vederle evidenziate nel documento.

Le espressioni regolari funzionano anche nel campo delle parole chiave temporanee, basta racchiudere il testo tra barre (`/my expression\b/`).

Le parole chiave temporanee sono destinate a situazioni in cui la densità delle parole chiave è importante e ti consentono di vedere rapidamente quante volte hai utilizzato le parole target, evidenziandone la posizione nel documento. Il conteggio delle corrispondenze per le parole chiave temporanee viene visualizzato in modo visibile nel cassetto.

Consulta anche il comando ["Visualizza ripetizione parole"][wordrep] per trovare le parole abusate nel tuo testo.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Voce passiva

Marked indicherà l'uso della "voce passiva" nel testo inglese. Come [definito da Wikipedia] [passivo]:

> il soggetto grammaticale esprime il tema o il paziente del verbo principale, cioè la persona o la cosa che subisce l'azione o cambia il suo stato.

La voce passiva non è malvagia, come puoi leggere [nei post del linguista Geoffrey K. Pullum] [gkp]. Marked segnala i passaggi usando la forma passiva, ma la decisione sulla loro validità spetta a te.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Parole raddoppiate

Le parole doppie (ad esempio "il il") vengono automaticamente evidenziate in arancione quando l'evidenziazione delle parole chiave è abilitata. Questo non è attualmente configurabile, ma dovrebbe rivelarsi utile per la correzione di bozze.