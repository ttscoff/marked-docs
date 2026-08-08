# <%= @title %>

[Visual Studio Code][vscode] bevat niet standaard Marked, maar je kunt een community-extensie gebruiken voor **live Markdown preview** in Marked --- preview, export en proefdrukken terwijl je blijft schrijven in VS Code.

## Snel aan de slag [quick-start]

1. Installeer een VS Code **Open in Marked** extensie (zie [Open in Marked extension][ext] hieronder).
2. Open uw Markdown-bestand in VS Code.
3. Stuur het bestand naar Marked --- het voorbeeld wordt bijgewerkt wanneer u het opslaat.

## Openen in Marked extensie [open-in-marked-extension]

De [Open in Marked extension][ext] (Visual Studio Marketplace) voegt een actie **Openen in Marked** toe: titelknop van de editor, **{% kbd shift cmd m %}**, contextmenu's in de editor en bestandsverkenner, optioneel **map openen** voor de bestandsbrowser van Marked, een statusbalkindicator en optioneel automatisch opslaan vóór openen. Met Instellingen kunt u het pad naar de app Marked instellen als deze zich niet op de standaardlocatie bevindt.

I> De extensie is oorspronkelijk gepubliceerd voor Marked 2. Marked 3 gebruikt dezelfde stijl voor bestands- en URL-overdracht, dus deze integratie blijft werken; als er iets verandert, controleer dan de [extension page][ext] of de repository van de auteur op updates.

## Vereisten [requirements]

Marked werkt alleen op macOS. Installeer [Marked 3][marked] en de extensie en wijs vervolgens **app-pad** naar uw Marked app, indien nodig.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/