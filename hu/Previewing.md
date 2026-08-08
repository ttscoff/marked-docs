<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

I> Ez az oldal az előnézeti *megjelenés* --- stílusokat, a nagyítást, a sötét módot és az állapotsort tartalmazza. Az élő előnézet szerkesztőből történő beállításához lásd: [Élő Markdown előnézet Macen](Live_Markdown_Preview_on_Mac.html).

A dolgok látásmódjának megváltoztatása.

## Stílus kiválasztása [choosing-a-style]

![][1]

   [1]: images/StylePicker.jpg @2x width=896px height=195px class=center

Az új dokumentumok alapértelmezett stílusát a {% prefspane Style %}-ban állíthatja be. Ha az Ablakbeállításokban engedélyezve van a stílusmenü az eszköztáron, akkor közvetlenül az Előnézet ablakból módosíthatja a stílust dokumentumonként. A kiválasztott stílust a rendszer megjegyzi, és ez lesz az első választás az exportálási és nyomtatási beállításokhoz.

A Stílusbeállításokban hozzáadott egyéni stílusok mindkét menüben elérhetők lesznek.

A stílusok billentyűparancsokkal választhatók ki. Nyissa meg a stílusmenüt az egyes stílusokhoz tartozó billentyűparancsok megtekintéséhez. A billentyűparancsok stílusrendben vannak hozzárendelve: a lista első 9 stílusa a {% kbd cmd 1 %} -- {% kbd cmd 9 %}, a következő 10 stílus a {% kbd cmd opt 1 %} -- {% kbd cmd opt 0 %} gombokkal érhető el, stb.

## Vázlat mód [outline-mode]

Ha a dokumentum egy hierarchikus lista, például egy gondolattérképből vagy körvonalazó alkalmazásból generált, akkor engedélyezheti a Vázlat módot a Fogaskerék menüben, hogy speciális formázást alkalmazhasson APA vagy Decimális körvonalazási stílusban.

Az automatikus körvonal mód bizonyos fájlkiterjesztésekhez engedélyezhető az {% prefspane Style %}-ben.

## Szöveg nagyítása [text-zoom]

![][2]

   [2]: images/textzoom.jpg @2x width=800px height=414px class=center

Módosíthatja a szöveg méretét a {% kbd cmd shift + %} és a {% kbd cmd shift - %} gombokkal, vagy használja a Nagyítás menüt az Előnézet alatt a menüsorban vagy a fogaskerék menüben a dokumentumablakban. A Megjelölt emlékezni fog minden változtatásra a következő alkalommal (és minden alkalommal). Állítsa vissza a nagyítást 100%-ra a {% kbd cmd 0 %} gombbal (vagy nyissa meg a **Zoom Reset** elemet a Zoom menüből).

## Sötét mód/nagy kontraszt [dark-modehigh-contrast]

Ha inkább a világos szöveget részesíti előnyben a sötét háttér előtt, a Megjelölt lehetőséget nyújt Önnek. Az __Előnézet__ menüben a {% appmenu Preview, Dark Mode ({{opt}}{{cmd}}I) %} segítségével megfordíthatja a színek bármelyikét az alapértelmezett sémák közül a világos-sötét eredmény eléréséhez, és ha egy egyéni téma [megfelelően van megépítve](Writing_Custom_CSS.html), az ott is működik.

## Állapotsor megjelenítése/elrejtése [showhide-status-bar]

Az előnézeti ablak alján lévő állapotsor a {% appmenu Preview, Show Status Bar ({{ctrl}}/) %} menüponttal váltható. Ha el van rejtve, akkor megtekinthető és interakcióba léphet vele, ha az egérmutatót az előnézet alján lévő terület fölé viszi.