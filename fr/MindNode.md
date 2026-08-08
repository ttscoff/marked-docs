# <%= @title %>

Faites glisser un document [MindNode][mn] sur Marked (ou utilisez la commande **Ouvrir dans Marked**/aperçu de MindNode, selon la version de MindNode). Marked traite le fichier comme l'exportation Markdown de MindNode, de sorte que la hiérarchie de votre carte devient des en-têtes et des listes dans l'aperçu.

## Aperçu en continu (MindNode 2026.3+) [streaming-preview-mindnode-20263]

I> **MindNode 2026.3** et les versions ultérieures ajoutent la prise en charge de l'[aperçu en continu](Streaming_Preview.html) de Marked. Dans MindNode, choisissez **Affichage → Aperçu dans Marked** pour l'ouvrir ; l'aperçu est mis à jour en direct à mesure que vous modifiez la carte.

## MindNode Classic contre MindNode 7+ [mindnode-classic-versus-mindnode-7]

W> L'intégration actuelle cible les bundles **MindNode Classic**. Les versions plus récentes de MindNode utilisent un format de package différent ; si l'ouverture d'une carte échoue ou si Marked affiche une feuille **"Veuillez ouvrir depuis MindNode"**, préparez la carte à partir du menu **Avancé** de MindNode (souvent **Ouvrir dans une autre application** / Marked), ou exportez un bundle compatible, plutôt que de faire glisser un package `.mindnode` brut qui n'a pas été préparé pour l'aperçu.

Étant donné que le fichier est préparé par MindNode avant que Marked ne le lise, enregistrez-le toujours dans MindNode avant d'attendre une mise à jour dans Marked.

[mn]: https://mindnode.com/
[mn-beta]: https://testflight.apple.com/join/jSvVBpnt
