<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked può creare automaticamente elementi reattivi `<picture>` per le immagini locali quando i file complementari **modalità oscura** e **Retina** si trovano accanto all'immagine a cui fai riferimento. Utilizza le stesse convenzioni di denominazione dei cataloghi di documentazione DocC di Apple, ma funziona per **qualsiasi documento Markdown o HTML** con normali percorsi di immagine che includono un'estensione di file.

Vedi anche [Supporto DocC](DocC_Support.html) per i riferimenti ai cataloghi senza estensione all'interno dei bundle `.docc`.

## Abilitazione delle varianti dell'immagine

In {% prefspane Apps %}, attiva **Risolvi varianti immagine scure e @2x** (attivata per impostazione predefinita) nelle impostazioni DocC.

Questa preferenza è separata da **Risolvi riferimenti immagine DocC**, che si applica solo all'interno dei cataloghi `.docc`. Puoi usarne uno, entrambi o nessuno dei due a seconda del tuo progetto.

## Convenzione di denominazione

Inserisci i file delle varianti nella **stessa cartella** dell'immagine principale. Contrassegnato cerca quattro combinazioni in base al nome della base:

| Ruolo | Nome file di esempio |
|------|------------|
| Luce (1x) | `icon.png` |
| Scuro (1x) | `icon~dark.png` |
| Luce (2x) | `icon@2x.png` |
| Scuro (2x) | `icon~dark@2x.png` |

L'ordine dei suffissi è flessibile: `icon@2x~dark.png` e `icon~dark@2x.png` vengono trattati allo stesso modo.

Estensioni supportate: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` e `pdf`.

## Cosa viene riscritto

Marked esegue la scansione del documento **prima** del rendering dell'anteprima finale:

- **Ribasso:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Se sul disco esistono almeno **due** file di varianti corrispondenti, il riferimento viene sostituito con un blocco `<picture>`. È sufficiente un solo file in più: non sono necessarie tutte e quattro le varianti.

Esempio di output quando sono presenti file chiari, scuri e @2x:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

L'anteprima (e l'esportazione HTML) segue quindi l'aspetto del sistema dell'utente per le varianti scure e la densità di pixel del dispositivo per le risorse @2x.

## Cosa viene saltato

Marked **non** riscrive:

- URL remoti (`http://`, `https://`, `data:`)
- Riferimenti che puntano già a un file `~dark`
- `<img>` tag già all'interno di un elemento `<picture>` esistente
- Nomi senza estensione come `![Diagram](diagram)`: utilizza [Supporto DocC](DocC_Support.html) per riferimenti in stile catalogo

## Anteprima dal vivo e visione dei file

Quando vengono rilevate varianti, Marked aggiunge **ogni file di variante esistente** alla sua lista di controllo insieme al documento principale. Il salvataggio di `icon~dark.png` in un editor esterno attiva lo stesso ricaricamento dell'immagine live della modifica `icon.png`.

## Suggerimenti

- Fai riferimento all'immagine **luce 1x** nella tua sorgente quando possibile (`icon.png`, non `icon~dark.png`). Marked scopre dei fratelli da quel percorso.
- Se hai solo risorse `@2x`, includi almeno un'altra variante (in genere `~dark`) altrimenti Marked lascerà invariato il riferimento.
- La risoluzione delle varianti utilizza i percorsi **relativi al documento** (o la cartella del file incluso per le inclusioni nidificate), le stesse regole di percorso di base di [Documenti multi-file](Multi-File_Documents.html).

## Argomenti correlati

- [Supporto DocC](DocC_Support.html): nomi di immagini senza estensione all'interno dei cataloghi `.docc`
- [Impostazioni: App](Settings_Apps.html): attiva/disattiva le preferenze per DocC e varianti di immagini
- [Anteprima](Previewing.html): anteprima dal vivo e aggiornamenti dei file