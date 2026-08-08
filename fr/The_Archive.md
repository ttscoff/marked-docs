# <%= @title %>

[The Archive][archive] conserve vos notes sous forme de fichiers sur le disque et peut refléter la note en cours d'édition directement dans le canal d'**aperçu en continu** de Marked.

## Diffuser l'aperçu vers Marked [stream-preview-to-marked]

1. Dans Marked, ouvrez {% appmenu File, New, Streaming Preview %} (ou réutilisez une fenêtre d'aperçu en continu existante).
2. Passez à The Archive et choisissez **Note &#8594; Stream Preview to Marked**, afin que The Archive active Marked et commence à envoyer le texte de la note au premier plan.

Marked se met à jour au fur et à mesure que vous tapez dans The Archive, en suivant le même contrat de presse-papiers `mkStreamingPreview` que les autres applications intégrées&#8212;voir [Détails techniques](Streaming_Preview.html#developers) dans [Aperçu en continu](Streaming_Preview.html).

Si les aperçus semblent obsolètes, vérifiez que la fenêtre d'aperçu en continu est toujours au premier plan dans Marked, puis actionnez une fois la commande de menu dans The Archive.

[archive]: https://www.zettelkasten.de/the-archive/
