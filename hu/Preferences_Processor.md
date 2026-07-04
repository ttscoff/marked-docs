<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Processor %} opciói:

![Beállítások: Processzor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### A leértékelés folyamata ezzel

Alapértelmezett Markdown processzor. A Discount processzort a GitHub felhasználók részesítik előnyben, a MultiMarkdown ideális az íróknak. A Marked kompenzálja a szintaxis közötti különbségeket. További információkért lásd a __Súgó->Megjelölési hivatkozás__ részt.

Egyéni szabályok
: Az Egyéni szabályok gombbal nyissa meg az Egyéni szabályok szerkesztőjét, amely lehetővé teszi a feldolgozási lehetőségek és a dokumentum-átalakítások meghatározását kritériumok alapján. A részletekért lásd az [Egyéni processzor dokumentációját](Custom_Processor.html).

Az új dokumentumok egyéni használatot használnak
: Az előfeldolgozó és/vagy processzor kiválasztása az új dokumentumok szabályfeldolgozásának automatikus engedélyezéséhez. Ha egyéni szabályokat használ, valószínűleg mindkettőt engedélyezni szeretné.

### HTML

Hozzon létre azonosítókat a címsorokon
: Fejlécazonosítókat generál a h1-h6 címke tartalma alapján.

Használjon véletlenszerű lábjegyzet-azonosítókat
: Véletlenszerű lábjegyzetazonosítókat generál az ütközések elkerülése érdekében, amikor több dokumentum jelenik meg egy oldalon.

Folyamat leértékelés a HTML-ben
: Alapértelmezés szerint a HTML-címkéken belüli Markdown általában figyelmen kívül marad. Ez az opció arra kényszeríti a Marked-et, hogy folytassa a feldolgozást a blokkelemeken belül. Vegye figyelembe, hogy bizonyos jelölések problémákat okozhatnak.


### Renderelés

Megőrzi a sortöréseket a bekezdésekben
: Tartsa tiszteletben a bekezdésszöveg sortöréseit, és az előző sorral való összefűzés helyett kemény törésekre cserélje.

A GitHub jelölőnégyzeteinek megjelenítése
: Jelenítse meg a `- [ ]` és `- [x]` jelölőnégyzeteket a listákban. A jelölőnégyzetek megjelennek az előnézethez, de nem működnek a Megjelölve.

\#A szöveg címke
: Lehetővé teszi a hashtagek (`#` közvetlenül utána szóköz nélküli szöveg) címkékként, nem címsorként értelmezését. Ez a funkció alapértelmezett a Bear felhasználók számára.
: A __Style tags__ a címkéket "kapszula" formázással jeleníti meg, hogy megkülönböztesse őket a szövegtől. Ha ez engedélyezve van, a címkék az {% appmenu {{gear}}, Proofing, Show Comments %} segítségével jeleníthetők meg/elrejthetők.

![#Text is tag enabled][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

`==highlight==` és `~~delete~~` megjelenítése
: Ha ez az opció engedélyezve van, akkor a `==highlight==` szöveg HTML `<mark>` címkeként jelenik meg, amely sárga kiemelésként jelenik meg, hacsak a stílus másként nem módosítja. Ezenkívül a `~~delete~~` szintaxis egy `<del>` címkével jelenik meg.

: Ha a __Render as CriticMarkup__ engedélyezve van, akkor a `==highlight==` és `~~delete~~` szintaxis CriticMarkup formátumba lesz konvertálva, amely ezután megjeleníthető az eredeti, jelölő és szerkesztett nézetekben.

Jelenítse meg a `~text~`-t aláhúzásként
: Ha ez az opció engedélyezve van, a `~text~` egyedi hullámokkal körülvéve aláhúzottként jelenik meg. Ez ütközik az alsó index MultiMarkdown szintaxisával, és alapértelmezés szerint le van tiltva.