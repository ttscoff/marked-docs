<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Megjelölt opciókat kínál.

## Élő előnézeti munkafolyamat [live-preview-workflow]

1. Húzzon egy Markdown fájlt a Megjelölt elemre (vagy használja a {% appmenu File, Open... ({{cmd}}O) %} gombot).
2. Szerkessze a fájlt a kívánt szerkesztőben.
3. Mentés --- A Megjelölve automatikusan frissíti az előnézetet.

Tekintse meg az [Élő Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) részt a Vault megtekintésével, a streaming előnézetével és a szerkesztő-specifikus útmutatókkal.

## Húzza a dokkoló ikonra [drag-to-dock-icon]

A Már szerkesztett fájlon a Marked funkció használatának legegyszerűbb módja, ha a dokumentum ikont a szerkesztő eszköztáráról vagy a Finderből a Dock Megjelölt ikonjára húzza. A Marked azonnal elkezdi követni a ráesett Markdown fájlokat (vagy szöveges fájlokat). Fájlokat közvetlenül a Finderből is húzhat.

## A menü használata [using-the-menu]

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

Természetesen a Markdown fájlokat közvetlenül is megnyithatja az {% appmenu File, Open... ({{cmd}}O) %} menüopció használatával. A Marked jól működik _szövegszerkesztő nélkül_ is. A Markdown előnézetét és konvertálását egyetlen kattintással megtekintheti.

A Megjelölt közvetlenül is megnyithat **`.rtf` és `.rtfd`** fájlokat (például a Pagesből vagy a TextEditből történő exportálást). A rendszer Markdown formátumba konvertálja az előnézethez és frissítéshez, amikor elmenti az eredeti alkalmazásban. Lásd az [RTF és RTFD támogatás](RTF_Support.html) részt a részletekért, beleértve a képeket és a korlátozásokat.

A megjelölt **`.pdf`** fájlt ugyanúgy meg tud nyitni: a konverzió a háttérben fut, majd az előnézet frissül, ha kész. Ez rövidebb, szöveges PDF-ekhez működik a legjobban; a nagy kézikönyvek és a beolvasott dokumentumok lassabbak és kevésbé pontosak. A részletekért és a korlátozásokért lásd: [PDF támogatás](PDF_Support.html).

## A vágólapról [from-the-clipboard]

Ha a vágólapon kompatibilis (például Markdown) szöveg található, azonnali előnézetet nyithat meg a {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} kiválasztásával. Ha egy kijelölést egy webböngészőből vagy más alkalmazásból másolt ki, amely HTML-t vagy RTF-et helyezett a vágólapra, a Marked átkonvertálja azt Markdown-ba az előnézethez. Amikor RTF-et illeszt be egy olyan alkalmazásból, mint a TextEdit vagy a Pages, a nagyobb betűméretek nagyjából címsorszintekké alakulnak (például a nagyon nagy szövegből 1. szintű címsor lesz, a kisebb, nagy szövegből 2. szintű stb.). Egyszerre több vágólap előnézetet is megnyithat, és a {% appmenu File, Save Transient Preview %} kiválasztásával új fájlba mentheti őket.

## Új dokumentum létrehozása [creating-a-new-document]

A Marked lehetővé teszi egy új, üres szövegfájl létrehozását a {% appmenu File, New ({{cmd}}N) %} paranccsal. Azonnal kérni fogja a fájl mentési helyét, és engedélyezheti az "Új fájlok automatikus szerkesztése" opciót az {% prefspane Apps %}-ben a Szövegszerkesztő gomb mellett, hogy automatikusan megnyissa az újonnan létrehozott fájlt az alapértelmezett szerkesztőben.

## Nyissa meg a Legutóbbiakat [open-recent]

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

A Marked nyomon követi a legutóbbi dokumentumokat is. A {% appmenu File, Open Recent %} menüopció megmutatja a megnyitott fájlokat, és visszaugorhat hozzájuk. Gyorsan újra megnyithatja az utoljára megtekintett fájlt a {% kbd shift cmd R %} gombbal. Használja a {% kbd shift cmd P %} vagy a [Gyorsműveletek](Quick_Actions.html) gombokat a menü- és előnézeti parancsok futtatásához a billentyűzetről. Ha még sok mást is megtudhat, akkor még sok rövidítést találhat. egy diagramot a [Billentyűparancsok](Keyboard_Shortcuts.html) alatt.

## Új nézet az aktuális fájlban [multiview]

A {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, az előnézet helyi menüjében is) segítségével nyissa meg a
második előnézeti ablak ugyanazon a mentett fájlon. Mindkét ablak
nézze meg a fájlt a lemezen, és frissítse, amikor menti a saját mappájába
szerkesztő, de minden nézet megtartja a saját görgetési pozícióját,
könyvjelzőket, előnézeti stílust és [Custom Rule
felülír](Custom_Processor.html#manuallyenabled).

**Példa felhasználási eset:** Ön egy hosszú kéziratot szerkeszt
MultiMarkdown a megszokott stílussal és processzorral. Nyissa meg a
második nézet, állítsa át próbastílusra, rögzítse a folyamatot
szabály, amely egy másik beépített processzort futtat, és engedélyezze a
kézi szabály, amely kiemeli a revíziójelölést. Te összehasonlítod
vázlat és próba elrendezések egymás mellett, kettő fenntartása nélkül
a fájl másolatai.

Ha egy fájl több nézete van nyitva, az ablak címe
tartalmazza a **View 2**, **View 3**, és így tovább, hogy tudja
ablakokat az Ablak menüben és a Mission Controlban.

A nem mentett dokumentumokhoz nem állnak rendelkezésre alternatív nézetek,
vágólap előnézetek, streaming előnézetek vagy mappaalapú
olyan projektek, amelyek nem képezik le egyetlen fájlt a lemezen.

## Gyors nyitás ## [quick-open]

Gyorsan válthat a megnyitott dokumentumok között, megnyithatja a legutóbbi dokumentumokat, vagy megnyithatja a Fájl->Megnyitás párbeszédpanelt a [Gyorsmegnyitás panel](Quick_Open.html) ({% kbd cmd shift o %}) segítségével.