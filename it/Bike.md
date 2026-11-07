# <%= @title %>

Trascina una struttura [Bike][bike] (`.bike`) su Marked per vederla come un elenco Markdown annidato, con le righe di titolo in grassetto e le attività come caselle di spunta.

## Aprire una struttura Bike [opening-a-bike-outline]

Marked converte la struttura quando apri il file:

- Le righe segnate come titolo diventano elementi di elenco in **grassetto**.
- Le attività diventano caselle di spunta nello stile di GitHub. Un'attività è spuntata quando Bike registra un orario di completamento o la segna come fatta.
- I link e la formattazione nel testo della riga restano Markdown.

Aprire un file `.bike` usa sempre questo elenco. Non trasforma la struttura in un diagramma Mermaid.

## Includere una struttura Bike [including-a-bike-outline]

Un file `.bike` si può anche includere in un altro documento Markdown. Vedi [Incorporare mappe mentali e strutture](Embedding_Mind_Maps_and_Outlines.html).

In {% prefspane Apps %}, sotto *Mind Maps and Outlines*, **Bike outlines** vale per i file inclusi:

- **Attivo** (predefinito) — un diagramma Mermaid. Il nome del file, senza `.bike`, è il nodo radice.
- **Disattivo** — lo stesso elenco Markdown annidato usato all'apertura del file, senza titolo del documento.

I diagrammi Mermaid richiedono MultiMarkdown, CommonMark (GFM) o Kramdown. Non vengono disegnati con il processore Discount.

[bike]: https://www.hogbaysoftware.com/bike/
