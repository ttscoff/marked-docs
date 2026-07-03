<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Contrassegnato ti offre opzioni.

## Flusso di lavoro dell'anteprima dal vivo

1. Trascina un file Markdown su Marked (o usa {% appmenu File, Open... ({{cmd}}O) %}).
2. Modifica il file nel tuo editor preferito.
3. Salva --- Contrassegnato aggiorna automaticamente l'anteprima.

Consulta [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html) per la visione del vault, l'anteprima in streaming e le guide specifiche dell'editor.

## Trascina sull'icona del Dock

Il modo più semplice per utilizzare Marked su un file che stai già modificando è trascinare l'icona del documento dalla barra degli strumenti dell'editor o dal Finder all'icona Marked nel Dock. Marked inizierà immediatamente a tracciare qualsiasi file Markdown (o file di testo) rilasciato su di esso. Puoi anche trascinare i file direttamente dal Finder.

## Utilizzo del menu

![][2]

   [2]: images/file_open.jpg @2x larghezza=300px altezza=118px classe=centro

Ovviamente puoi aprire i file Markdown direttamente utilizzando l'opzione di menu {% appmenu File, Open... ({{cmd}}O) %}. Marked funziona bene anche _senza_ un editor di testo. Puoi visualizzare in anteprima e convertire il tuo Markdown con un solo clic.

Marked può anche aprire direttamente i file **`.rtf` e `.rtfd`**** (ad esempio esportazioni da Pages o TextEdit). Vengono convertiti in Markdown per l'anteprima e l'aggiornamento quando salvi nell'app originale. Vedi [Supporto RTF e RTFD](RTF_Support.html) per i dettagli, comprese immagini e limitazioni.

Marked può aprire i file **`.pdf`** nello stesso modo: la conversione viene eseguita in background, quindi l'anteprima si aggiorna al termine. Funziona meglio con PDF più brevi e basati su testo; manuali di grandi dimensioni e documenti scansionati sono più lenti e meno accurati. Vedi [Supporto PDF](PDF_Support.html) per dettagli e limitazioni.

## Dagli Appunti

Se negli appunti è presente testo compatibile (ad esempio Markdown), puoi aprire un'anteprima istantanea selezionando {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Se hai copiato una selezione da un browser Web o da un'altra app che inserisce HTML o RTF negli appunti, Marked la converte in Markdown per l'anteprima. Quando incolli RTF da un'app come TextEdit o Pages, le dimensioni dei caratteri più grandi vengono convertite approssimativamente in livelli di intestazione (ad esempio, un testo molto grande diventa un'intestazione di livello 1, un testo più piccolo e grande diventa un livello 2 e così via). Puoi avere più anteprime degli appunti aperte contemporaneamente e salvarle in un nuovo file scegliendo {% appmenu File, Save Clipboard Preview %}.

## Creazione di un nuovo documento

Marked ti consente di creare un nuovo file di testo vuoto con il comando {% appmenu File, New ({{cmd}}N) %}. Ti verrà immediatamente chiesto un percorso in cui salvare il file e potrai abilitare l'opzione "Modifica nuovi file automaticamente" in {% prefspane Apps %}, accanto al pulsante Editor di testo per aprire automaticamente il file appena creato nel tuo editor predefinito.

## Apri Recenti

![][3]

   [3]: images/open_recent.jpg @2x larghezza=300px altezza=174px classe=centro

Marked tiene traccia anche dei documenti recenti. L'opzione di menu {% appmenu File, Open Recent %} ti mostrerà i file che hai aperto e ti permetterà di tornare ad essi. Puoi riaprire rapidamente l'ultimo file che stavi visualizzando con {% kbd shift cmd R %}. Usa {% kbd shift cmd P %} o [Azioni rapide](Quick_Actions.html) per eseguire il menu e visualizzare in anteprima i comandi dalla tastiera. Ci sono anche molte altre scorciatoie da tastiera. Se ti interessa impararle, puoi trovare un grafico sotto [Tastiera Scorciatoie](Keyboard_Shortcuts.html).

## Apertura rapida ##

Puoi passare rapidamente da un documento aperto all'altro, aprire documenti recenti o aprire la finestra di dialogo File->Apri con il [pannello Apertura rapida](Quick_Open.html) ({% kbd cmd shift o %}).