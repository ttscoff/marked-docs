<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked comprende i cataloghi di documentazione [Apple DocC](https://www.swift.org/documentation/docc/) (`.docc` bundle). Quando visualizzi l'anteprima di Markdown che si trova all'interno o accanto a un catalogo, Marked può risolvere i riferimenti alle immagini **senza estensione** ai file nella cartella `Resources` del catalogo, incluse le varianti `~dark` e `@2x`.

Per i normali documenti Markdown che utilizzano **percorsi con estensioni di file** (`images/icon.png`), vedere [Varianti immagine](Image_Variants.html). Questa funzionalità funziona ovunque; La risoluzione DocC è specifica del catalogo.

## Abilitazione della risoluzione DocC [enabling-docc-resolution]

In {% prefspane Apps %}, abilita **Risolvi riferimenti immagine DocC** (attivato per impostazione predefinita).

Il rilevamento DocC viene eseguito quando Marked trova un catalogo `.docc` antenato del documento aperto. Non è richiesto alcuno schema URL speciale o integrazione Xcode: apri Markdown del catalogo come faresti con qualsiasi altro file.

## Riferimenti senza estensione [extensionless-references]

All'interno di un catalogo DocC, gli autori in genere fanno riferimento a immagini **senza** un percorso o un'estensione:

```markdown
![Order flow](OrderStateTransitions)
```

Marked risolve da `OrderStateTransitions` a `Resources/OrderStateTransitions.png` (o un altro tipo supportato) quando quel file esiste nel catalogo.

I riferimenti che già includono un percorso e un'estensione - `images/chart.png` - vengono invece lasciati a [Varianti immagine](Image_Variants.html) e non vengono riscritti dalla risoluzione DocC.

## Modalità oscura e varianti Retina [dark-mode-and-retina-variants]

I cataloghi DocC spesso forniscono più file per immagine:

| Ruolo | Esempio in `Resources/` |
|------|------------------------|
| Luce (1x) | `diagram.png` |
| Scuro (1x) | `diagram~dark.png` |
| Luce (2x) | `diagram@2x.png` |
| Scuro (2x) | `diagram~dark@2x.png` |

Quando esiste più di una variante, Marked emette lo stesso markup reattivo `<picture>` descritto in [Varianti immagine](Image_Variants.html). Un riferimento a file singolo si risolve comunque in un normale percorso `<img>` o `![](Resources/...)`.

## HTML e Markdown [html-and-markdown]

La risoluzione DocC si applica durante il passaggio di inclusione di Marked:

- **Fonti di markdown** — `![alt](ImageName)` riferimenti
- **Sorgenti HTML** — `<img src="ImageName">` senza estensione

Entrambi vengono aggiornati prima del rendering dell'anteprima.

## Visualizzazione di file [file-watching]

Le immagini risolte nella cartella catalogo `Resources` vengono aggiunte alla lista di controllo di Marked. La modifica di un file variante aggiorna esternamente l'anteprima senza aggiornamento manuale.

## Argomenti correlati [related-topics]

- [Varianti immagine](Image_Variants.html) - rilevamento `~dark` e `@2x` per percorsi basati sull'estensione in qualsiasi progetto
- [Xcode Playgrounds](Xcode_Playgrounds.html): anteprima del commento del parco giochi Swift
- [Impostazioni: App](Settings_Apps.html): preferenze per DocC e varianti immagine