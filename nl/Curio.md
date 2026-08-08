# <%= @title %>

[Curio][curio] is een visuele brainstorm- en notitie-app waarmee je het item dat je aan het bewerken bent, kunt streamen naar het **streaming preview**-kanaal van Marked.

## Stream geselecteerd tot Marked [stream-selected-to-marked]

1. Kies in Marked {% appmenu File, New, Streaming Preview %} zodat er een streamingvoorbeeldvenster gereed is.
2. Schakel in Curio **Weergave → Stream geselecteerd in op Marked**.

Wanneer u dubbelklikt om een ​​figuur, notitie, lijst of ander item in Curio te bewerken, stroomt de Markdown ervan naar het streamingvoorbeeld en wordt bijgewerkt terwijl u schrijft.

Marked wordt bijna in realtime bijgewerkt, volgens hetzelfde `mkStreamingPreview` klembordcontract als andere geïntegreerde apps. Zie [Technical details](Streaming_Preview.html#developers) onder [Streaming Preview](Streaming_Preview.html).

Als de voorvertoningen niet meer worden bijgewerkt, controleer dan of er een streamingvoorbeeldvenster is geopend in Marked en schakel **Stream geselecteerd naar Marked** in Curio.

[curio]: https://www.zengobi.com/products/curio/
