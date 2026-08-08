# <%= @title %>

[Curio][curio] est une application de brainstorming visuel et de prise de notes qui peut diffuser l'élément que vous modifiez dans le canal **aperçu en continu** de Marked.

## Flux sélectionné sur Marked [stream-selected-to-marked]

1. Dans Marked, choisissez {% appmenu File, New, Streaming Preview %} pour qu'une fenêtre d'aperçu en continu soit prête.
2. Dans Curio, activez **Affichage → Flux sélectionné sur Marked**.

Lorsque vous double-cliquez pour modifier une figure, une note, une liste ou un autre élément dans Curio, son Markdown est transmis à l'aperçu en continu et se met à jour au fur et à mesure que vous écrivez.

Les mises à jour se font en temps quasi réel, suivant le même contrat de presse-papiers `mkStreamingPreview` que les autres applications intégrées : voir [Détails techniques](Streaming_Preview.html#developers) sous [Aperçu en continu](Streaming_Preview.html).

Si les aperçus cessent de se mettre à jour, vérifiez qu'une fenêtre d'aperçu en continu est ouverte dans Marked et basculez **Flux sélectionné sur Marked** une fois dans Curio.

[curio]: https://www.zengobi.com/products/curio/
