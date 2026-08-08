<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Quick Open fornisce un accesso rapido ai documenti aperti e ai file recenti.

## Apertura Apertura rapida [opening-quick-open]

Accedi al pannello Apertura rapida utilizzando {% kbd shift cmd O %} o dal menu {% appmenu File, Quick Open %}. Il pannello appare come una finestra mobile sopra il documento corrente, consentendoti di passare rapidamente da un documento aperto all'altro o di aprire file recenti.

![Pannello di apertura rapida][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Sezioni del documento [document-sections]

Il pannello Apertura rapida organizza i documenti in sezioni chiare:

### Apri documenti [open-documents]

In cima all'elenco vedrai tutti i documenti attualmente aperti. I documenti sono raggruppati visivamente in base alla loro finestra:

- **Finestre a schede**: i documenti nelle finestre a schede mostrano "Finestra con X schede" come sottotitolo, indicando quante schede sono presenti in quel gruppo di finestre
- **Windows autonomo**: i documenti nelle singole finestre mostrano "Finestra" come sottotitolo

Ogni documento aperto visualizza:
- Il nome del file del documento come titolo principale
- Le informazioni sul raggruppamento delle finestre come sottotitolo
- Un'icona del documento

### Documenti recenti [recent-documents]

Sotto i documenti aperti, un separatore "Documenti recenti" divide l'elenco. La sezione dei documenti recenti mostra fino a 10 dei file aperti più di recente che non sono attualmente aperti. Ogni documento recente visualizza:

- Il nome del file del documento come titolo principale
- "Recenti" come sottotitolo
- Un'icona del documento

### Apri Altro [open-other]

In fondo all'elenco, l'opzione "Apri altro..." ti consente di aprire il selettore file standard di macOS per selezionare qualsiasi file. Questa opzione visualizza:

- "Apri altro..." come titolo principale
- "Apri un file o una cartella" come sottotitolo
- L'icona di una cartella

## Cerca e filtra [search-and-filter]

Digita nel campo di ricerca nella parte superiore del pannello per filtrare l'elenco in tempo reale. La ricerca corrisponde a:

- Nomi dei file dei documenti
- Percorsi di file completi

Durante la digitazione, l'elenco si aggiorna immediatamente per mostrare solo i documenti corrispondenti. L'opzione "Apri altro..." rimane sempre visibile nella parte inferiore dei risultati filtrati.

## Navigazione tramite tastiera [keyboard-navigation]

Naviga nel pannello Apertura rapida interamente con la tastiera:

- **Tasti freccia ↑/↓**: spostati su e giù nell'elenco
- **Restituisci**: apre il documento o l'opzione selezionata
- **Escape**: chiude il pannello di apertura rapida
- **Comando (⌘)**: tieni premuto per rivelare i percorsi dei file (vedi sotto)

## Visualizzazione dei percorsi dei file [viewing-file-paths]

Tieni premuto il tasto **Comando (⌘)** mentre il pannello Apertura rapida è aperto per visualizzare il percorso completo del file per ciascun documento nell'area dei sottotitoli. I percorsi nella tua home directory vengono visualizzati utilizzando la scorciatoia `~` (ad esempio, `~/Documents/file.md`). Rilascia il tasto Comando per tornare alla visualizzazione normale che mostra il raggruppamento delle finestre o le informazioni "Recenti".

Ciò è particolarmente utile quando sono aperti più file con lo stesso nome o quando è necessario verificare la posizione esatta di un documento.

## Apertura dei documenti [opening-documents]

- **Documenti aperti**: la selezione di un documento aperto porta la sua finestra in primo piano e passa alla scheda del documento se si trova in una finestra a schede
- **Documenti recenti**: selezionando un documento recente lo si apre in una nuova finestra o lo si aggiunge come scheda (a seconda della preferenza "Apri documenti in schede" in {% prefspane General %})
- **Apri altro...**: selezionando questa opzione si apre la finestra di dialogo di selezione file standard di macOS