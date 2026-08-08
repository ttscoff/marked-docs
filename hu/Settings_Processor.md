<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% prefspane Processor %} opciói:

![Beállítások: Processzor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane-scroll

### A leértékelés folyamata ezzel [process-markdown-with]

Alapértelmezett Markdown processzor. A CommonMark processzort részesítik előnyben a GitHub-felhasználók, a MultiMarkdown ideális az íróknak, a Discount és a Kramdown pedig speciális célokat szolgál. A Marked kompenzálja a szintaxis közötti különbségeket. További információkért lásd a __Súgó->Megjelölési hivatkozás__ részt.

Egyéni szabályok
: Kattintson az Egyéni szabályok gombra a Szabályszerkesztő megnyitásához, ahol az illeszkedési feltételek alapján különböző feldolgozókat és dokumentum-átalakításokat adhat meg. A részletekért lásd: [Egyéni processzor](Custom_Processor.html).

Az új dokumentumok egyéni használatot használnak
: Ha be van jelölve, az új dokumentumok automatikusan az egyéni szabályokból mentett **előfeldolgozót** és/vagy **feldolgozót** használják anélkül, hogy dokumentumonkénti beállításra lenne szükség.

Teljes lemezhozzáférés
: Kattintson a **Megenged** gombra, hogy engedélyt adjon a Megjelöltnek a homokozón kívüli fájlok olvasására, ha egyéni processzorokat vagy más olyan funkciókat használ, amelyek szélesebb fájlhozzáférést igényelnek.

A processzorok közötti különbségek felfedezéséhez tekintse meg a [Markdown Dingus](Markdown_Dingus.html) részt.

### HTML [html]

Hozzon létre azonosítókat a címsorokon
: Fejlécazonosítókat generál a h1-h6 címke tartalma alapján.

Használjon véletlenszerű lábjegyzet-azonosítókat
: Véletlenszerű lábjegyzetazonosítókat generál az ütközések elkerülése érdekében, amikor több dokumentum jelenik meg egy oldalon.

Folyamat leértékelés a HTML-ben
: Alapértelmezés szerint a HTML-címkéken belüli Markdown általában figyelmen kívül marad. Ez az opció arra kényszeríti a Marked-et, hogy folytassa a feldolgozást a blokkelemeken belül. Vegye figyelembe, hogy bizonyos jelölések problémákat okozhatnak.

### Renderelés [rendering]

Megőrzi a sortöréseket a bekezdésekben
: Tartsa tiszteletben a bekezdésszöveg sortöréseit, és az előző sorral való összefűzés helyett kemény törésekre cserélje.

A GitHub jelölőnégyzeteinek megjelenítése
: Jelenítse meg a `- [ ]` és `- [x]` jelölőnégyzeteket a listákban. A jelölőnégyzetek megjelennek az előnézethez, de nem működnek a Megjelölve.

GitHub megjelenítése :emoji:
: jelenítse meg az `:name:` rövid kódokat GitHub-stílusú hangulatjelként az előnézetben.

\#A szöveg címke
: Lehetővé teszi a hashtagek (`#` közvetlenül utána szóköz nélküli szöveg) címkékként, nem címsorként értelmezését. Ez a funkció alapértelmezett a Bear felhasználók számára.

Stíluscímkék
: Ha a **#Text is tag** engedélyezve van, a felismert címkéket kapszula stílussal jelenítse meg. A címkék megjeleníthetők vagy elrejthetők a következőből: {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Text is tag enabled][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

`==highlight==` és `~~delete~~` megjelenítése
: Ha ez az opció engedélyezve van, akkor a `==highlight==` szöveg HTML `<mark>` címkeként jelenik meg, amely sárga kiemelésként jelenik meg, hacsak a stílus másként nem módosítja. Ezenkívül a `~~delete~~` szintaxis egy `<del>` címkével jelenik meg.

: Ha a __Render as CriticMarkup__ engedélyezve van, akkor a `==highlight==` és `~~delete~~` szintaxis át lesz konvertálva CriticMarkup formátumba, amely ezután megjeleníthető eredeti, jelölő és szerkesztett nézetben.

Jelenítse meg a `~text~`-t aláhúzásként
: Ha ez az opció be van kapcsolva, a `~text~` egyedi hullámokkal körülvéve aláhúzottként jelenik meg. Ez ütközik az alsó index MultiMarkdown szintaxisával, és alapértelmezés szerint le van tiltva.