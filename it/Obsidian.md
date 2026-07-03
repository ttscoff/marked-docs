<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked funziona con le note [Obsidian] [obsidian-app] in due modi: apri una **cartella Vault** per seguire automaticamente o utilizza il **plug-in della community** per una sincronizzazione più stretta.

L'anteprima integrata di Obsidian è l'ideale quando non lasci mai l'app. Scegli Contrassegnato se desideri un'esportazione di qualità pubblicata, una correzione di bozze avanzata, temi CSS personalizzati o lo stesso flusso di lavoro di anteprima dal vivo su più editor. Vedi [Anteprima Marked vs Obsidian](Marked_vs_Obsidian_Preview.html) per un confronto completo.

## Apri un intero caveau

Trascina la **cartella del vault** (la directory che contiene la cartella di configurazione nascosta di Obsidian nella radice del vault) su Contrassegnato nel Dock. Marked osserva quell'albero, conserva la nota **modificata più recentemente** nell'anteprima e si aggiorna man mano che salvi in ​​Obsidian.

Per le impostazioni predefinite specifiche del deposito (stile, processore, URL di base per le immagini e così via), aggiungi una [Regola personalizzata](http://support.markedapp.com) che corrisponda ai percorsi sotto quel deposito.

## Sintassi del callout dell'ossidiana

Quando il processore MultiMarkdown viene eseguito, Marked converte i comuni **richiami in stile Obsidian** (il modello `> [!note]`) in markup di blocco con stile in modo che corrispondano al resto dell'anteprima.

## Plugin di ossidiana contrassegnato con 3

Il [plug-in Marked 3 Obsidian] [plug-in] può aprire la nota corrente o l'intero vault con comandi o tasti di scelta rapida in modo che la finestra Marked tenga traccia di ciò che stai modificando. Utilizza la tavolozza dei comandi (**⌘P**) e cerca **Contrassegnato**, oppure assegna i tasti di scelta rapida nelle impostazioni **Tasti di scelta rapida** di Obsidian.

### Installazione dai plugin della comunità

In Obsidian, apri **Impostazioni → Plug-in della community**, sfoglia o cerca **contrassegnato** e installa **Apri in Contrassegnato**.

### Installazione manuale del plugin

Se preferisci installare da GitHub:

1. Scarica `main.js` e `manifest.json` dall'[ultima versione] [rilasci di plug-in] su GitHub (o creali dal repository [Marked3-obsidian] [plug-in]).
2. Nel tuo vault, crea la cartella del plugin sotto `plugins/` all'interno della directory di configurazione di Obsidian nella radice del vault. Il nome della cartella deve corrispondere al plugin `id` in `manifest.json` (vedi [plugin README] [plugin] per il percorso completo).
3. Copia `main.js` e `manifest.json` in quella cartella.
4. In Obsidian, apri **Impostazioni → Plug-in della community**, disattiva la **Modalità limitata** se necessario e attiva **Apri in contrassegnati**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest