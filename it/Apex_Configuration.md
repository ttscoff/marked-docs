<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Queste opzioni sono nel foglio **Configura Apex**. Si apre da {% prefspane Processor %} quando il processore predefinito è **Apex (beta)**. Ogni opzione vale solo per Apex. Matematica, Critic Markup, hashtag, inclusioni di file e ID dei titoli restano nelle altre impostazioni di Marked.

Vedi [Apex (beta)](Apex.html) per capire che cos'è Apex e la sintassi che copre.

Le caselle del foglio hanno la precedenza sulle stesse impostazioni di un file di metadati Apex. I percorsi dei file sono facoltativi. Un percorso che Marked non riesce a leggere viene saltato e l'anteprima continua.

## File [files]

CSL
: Un file Citation Style Language (`.csl`) usato quando Apex formatta una bibliografia. Lascialo vuoto per usare lo stile indicato nel documento o nel file di metadati.

Bibliografia
: Uno o più file di bibliografia. Tipi accettati: BibTeX (`.bib`), CSL JSON (`.json`) e CSL YAML (`.yml`, `.yaml`). Fai clic su **Aggiungi** per un altro file. Apex li consulta per risolvere le citazioni.

Concordanza
: Uno o più file di concordanza (`.tsv`, `.txt` o `.csv`) usati per costruire un indice. Fai clic su **Aggiungi** per un altro file.

File di metadati
: Un file di metadati esterno (`.yml`, `.yaml`, `.txt` o `.md`) unito prima che Apex venga eseguito. Se il documento e il file impostano la stessa chiave, prevalgono i metadati del documento. Le caselle di questo foglio prevalgono sui valori del file di metadati.

## Sintassi [syntax]

Attive per impostazione predefinita, salvo diversa indicazione.

Tabelle
: Tabelle a barre verticali, con una riga di intestazione e una riga separatrice.

Note a piè di pagina
: Note di riferimento (`[^id]`) e note in linea.

Elenchi di definizioni
: Elenchi termine e definizione (`: definizione`).

Apice / pedice
: `^super^` e `~sub~`. Disattivalo se una tilde singola non deve significare pedice. L'impostazione di Marked **Rendi ~text~ come sottolineatura** è separata e va in conflitto con il pedice.

Barrato
: `~~eliminato~~`.

Collegamenti automatici a URL e email
: Gli URL `https://` e gli indirizzi email nudi diventano collegamenti.

Div delimitati
: Blocchi `::: nome` che racchiudono una sezione in un `<div>`.

Span tra parentesi
: Span di attributi in linea, come `[testo]{.class}`.

Elenchi alfabetici
: Elenchi che iniziano con `a.` o `A.`, oltre ai numeri.

Indicatori di elenco misti
: Un elenco può mescolare `*`, `+` e `-` e restare un solo elenco.

Markdown nell'HTML
: Il Markdown dentro i tag di blocco HTML viene elaborato. Qualche marcatura può comunque rompersi.

Trasformazioni dei metadati
: I segnaposto `[%key]` vengono sostituiti con i metadati del documento.

## Tabelle e immagini [tables-and-images]

Tabelle a griglia
: Tabelle disegnate con `+` e `|`. Disattivate per impostazione predefinita.

Tabelle rilassate
: Le tabelle a barre possono omettere le barre iniziale e finale. Attive per impostazione predefinita.

Allineamento per cella
: Gli indicatori di allineamento di una cella sostituiscono l'allineamento della colonna. Attivo per impostazione predefinita.

Didascalie delle immagini
: Il titolo dell'immagine, o il testo alternativo se non c'è un titolo, diventa una didascalia visibile. Attivo per impostazione predefinita.

Solo didascalie dal titolo
: Come didascalia si usa solo il titolo dell'immagine. Il testo alternativo viene ignorato. Disattivo per impostazione predefinita. Non ha effetto se **Didascalie delle immagini** è disattivato.

## Collegamenti e indici [links-and-indexes]

Collegamenti wiki
: Apex converte `[[collegamenti wiki]]`. Disattivo per impostazione predefinita. Se è attivo, Marked salta il proprio passaggio di anteprima «Converti collegamenti wiki» per quel documento, e Apex può risolvere il file di destinazione in modo diverso da Marked. L'estensione predefinita arriva dalle impostazioni dei collegamenti wiki di Marked.

Ripulisci gli URL dei collegamenti wiki
: Gli URL generati vengono messi in minuscolo, gli apostrofi vengono rimossi e gli altri caratteri che non sono lettere o numeri vengono sostituiti. Disattivo per impostazione predefinita. Disponibile solo se **Collegamenti wiki** è attivo.

Elaborazione dell'indice
: Riconosce gli indicatori di indice (stili MultiMarkdown, mmark, Leanpub e textindex). Attivo per impostazione predefinita.

Sopprimi l'output dell'indice
: Legge comunque gli indicatori, ma non stampa l'indice generato. Disattivo per impostazione predefinita.

## Riquadri (extra) [callouts-extra]

Entrambi sono disattivati per impostazione predefinita. I riquadri di Obsidian e Bear (`> [!NOTE]`) sono gestiti da Marked prima di Apex e non si controllano qui.

Riquadri Python-Markdown (!!!)
: Riquadri in stile `!!! note`.

Riquadri Quarto
: Blocchi Quarto `::: {.callout-note}`.

## Accessibilità [accessibility]

Entrambi sono disattivati per impostazione predefinita.

Etichette ARIA
: Aggiunge attributi ARIA che descrivono la struttura dell'HTML emesso da Apex.

Ancore dei titoli
: Emette un'ancora `<a>` su ogni titolo invece del solo `id` sul titolo.
