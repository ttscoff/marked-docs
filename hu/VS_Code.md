<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [Visual Studio Code][vscode] nem tartalmazza a Kiválasztott elemet, de használhat közösségi bővítményt az **élő Markdown előnézethez** a Marked --- előnézethez, exportáláshoz és lektoráláshoz, miközben folyamatosan ír a VS Code-ban.

## Gyors kezdés

1. Telepítsen egy VS Code **Open in Marked** bővítményt (lásd lent a [Megnyitás megjelölt bővítményben][ext]).
2. Nyissa meg a Markdown fájlt a VS Code alkalmazásban.
3. Küldje el a fájlt a Marked --- mappába, ahol az előnézet mentéskor frissül.

## Megnyitás a Megjelölt bővítményben

A [Megnyitás megjelölt kiterjesztésben][ext] (Visual Studio Marketplace) hozzáad egy **Megnyitás Markedben** műveletet: szerkesztő címgombja, **{% kbd shift cmd m %}**, helyi menük a szerkesztőben és a fájlkezelőben, opcionális **mappa megnyitása** a Marked fájlböngészőjéhez, állapotsorjelző és opcionális automatikus mentés a megnyitás előtt. A beállításokkal megadhatja a Megjelölt alkalmazás elérési útját, ha az nem az alapértelmezett helyen van.

I> A kiterjesztést eredetileg a Marked 2-hez tették közzé. A Marked 3 ugyanazt a fájl- és URL-átadási stílust használja, így ez az integráció továbbra is működik; Ha bármi megváltozik, ellenőrizze a [bővítményoldalt][ext] vagy a szerző tárházát a frissítésekért.

## Követelmények

A megjelölt csak macOS rendszeren fut. Telepítse a [Marked 3][marked] elemet és a bővítményt, majd szükség esetén mutasson az **alkalmazás elérési útjára** a megjelölt alkalmazásra.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/