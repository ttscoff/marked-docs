<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked meg tudja tekinteni ugyanazt a fájlt több beépített Markdown processzorral. Mindegyik más-más kompromisszumot köt az **írási munkafolyamat** (könyvek, blogok, GitHub README-k) és a **kimenet-vezérlés** (azonosítók, osztályok, metaadatok) között. Az alapértelmezettet a {% prefspane Processor %}-ben választhatja ki; a processzort dokumentumonként is felülírhatja.

Ez az oldal összefoglalja, hogy miben különbözik a négy fő processzor. A teljes szintaktikai részletekért tekintse meg a **Súgó → Markdown-referencia** hivatkozási oldalait (pl. [MultiMarkdown v5 specifikáció](MultiMarkdown_v5_Spec.html), [Kramdown specifikáció](Kramdown_Spec.html), [CommonMark specifikáció](CommonMark_Spec.html), [Kedvezményes GFM-specifikáció]⧟22).

---

## MultiMarkdown (v5)

**A legalkalmasabb a következőkhöz:** Hosszú próza, tudományos vagy műszaki írások, valamint bármi, ami **metaadatokra**, **idézetekre** és **MultiMarkdown-specifikus** funkciókra támaszkodik.

A **MultiMarkdown 5** jelöléssel ellátva (lásd a [MultiMarkdown felhasználói kézikönyv](https://fletcher.github.io/MultiMarkdown-5/) az upstream dokumentációt).

### Erősségek

- **Narratív és hivatkozásokat tartalmazó dokumentumok:** A lábjegyzetek, az irodalomjegyzék/idézetek és a táblázatok első osztályúak.
- **Metaadatok:** Szabványos MultiMarkdown metaadatblokkok (`Key: Value` fejléc), valamint **átvétel** és egyéb MMD-kényelmek, amelyeket a v5-ös útmutató ismertet.
- **Metaadatok helyettesítése:** A metaadatokból származó kulcsok `[%key]`-stílusú helyettesítéssel illeszthetők be a törzsbe, így a címek, szerzői karakterláncok és hasonló értékek szinkronban maradnak a fejléccel.
- **Táblázatok, képek és kereszthivatkozások:** A MultiMarkdown 5-höz dokumentált jellemzőkkel összhangban.

### Azonosítók és kézi fejlécek

- A címsorazonosítók **normalizáltak** oly módon, hogy hajlamosak **kisbetűs, összefűzött** csigák létrehozására (nincs szóköz – a szavak összefutnak).
- A **kézi fejlécazonosítókhoz** a MultiMarkdown a következő űrlapot használja: `## Headline Text [my-id]` (a zárójelben lévő azonosító a címsor szövege után).

### Mikor válassz valami mást

Ha **GitHub-ízű** feladatlistákra és a GitHub jelenlegi elemzőjének pontos viselkedésére van szüksége, válassza a **CommonMark (GFM)** lehetőséget. Ha **finomszemcsés HTML-osztályokra/azonosítókra** van szüksége tetszőleges elemekhez, fontolja meg a **Kramdown** lehetőséget.

---

## Kramdown

**A legjobb a következőhöz:** Olyan dokumentumokhoz, ahol **pontos vezérlést kíván a HTML-kimenet felett** — egyéni **osztályok**, **azonosítók** és attribútumok, így a CSS meghatározott blokkokat és szakaszokat célozhat meg.

A [kramdown szintaxis hivatkozás] (https://kramdown.gettalong.org/syntax.html) a mérvadó útmutató.

### Erősségek

- **Többnyire kompatibilis** a MultiMarkdown-stílusú szokásokkal a mindennapi Markdown-hoz, miközben saját bővítményekkel is rendelkezik.
- **Inline és blokk attribútumlisták (IAL):** `{: #id .class key="value"}` csatolása bekezdésekhez, fejlécekhez, kódblokkokhoz, hivatkozásokhoz, képekhez és egyebekhez --- ideális Jekyll-stílusú webhelyekhez és egyéni stíluslapokhoz.
- **Fejlécazonosítók:** A kramdown normalizálja az automatikusan generált fejlécazonosítókat **kisbetűs, kötőjellel elválasztott** szavakra (pl. `my-section-title`). A **kézi azonosítók** esetén használja a `{#id}` űrlapot a címsor szövege után – pl. Szöveg: `My Section {#my-section}`, majd az aláhúzás, vagy ATX: `# My Section {#my-section}` (a pontos elhelyezést és az IAL-szabályokat lásd a kramdown [fejléceiben](https://kramdown.gettalong.org/syntax.html#headers)).
- **Definíciós listák, lábjegyzetek, intelligens tipográfia, matematikai blokkok:** Gazdag funkciókészlet olyan folyamatok közzétételéhez, amelyeknek többre van szükségük, mint az „egyszerű” jelölésen.

### Mikor válassz valami mást

Ha a **MultiMarkdown-only** metaadat-helyettesítésre (`[%key]`) vagy MMD-specifikus hivatkozási munkafolyamatokra támaszkodik, a **MultiMarkdown** jobban megfelelhet. Azon **README- és repodokumentumok** esetében, amelyeknek meg kell egyeznie az online GitHub-val, a **CommonMark (GFM)** általában közelebb áll.

---

## CommonMark (GitHub ízesítésű Markdown / cmark-gfm)

**A legjobb:** **README-fájlok**, **probléma/PR-leírások** és **projektdokumentáció**, amelyeknek a lehető legjobban meg kell felelniük a **GitHub jelenlegi Markdown viselkedésének**.

A Marked **GFM**-orientált motort használ (cmark-gfm). A formális specifikáció a [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), amely a [CommonMark]-ra (https://commonmark.org/) épül.

### Erősségek

- **A GitHubhoz legközelebbi egyezés:** A táblázatok, az áthúzások, a feladatlista-elemek, a nyelvi címkékkel ellátott kódblokkok és az automatikus linkek úgy viselkednek, mint a modern GitHub-megjelenítés.
- **Egyértelmű elemzés:** A CommonMark pontosan meghatározza a blokk/soron belüli elsőbbséget és a listaszabályokat – bizonyos éles esetekben szigorúbb, mint a „klasszikus” Markdown.pl viselkedés, de **megjósolhatóbb**, ha megtanulja a szabályokat.
- **Gyakorlati a burkolt szöveghez:** A bekezdés- és listaszabályokat úgy alakították ki, hogy jól viselkedjenek a tömörített prózában (lásd a specifikáció lusta folytatásokról és listákról szóló szakaszait).

### Fejlécazonosítók

Az automatikusan generált fejléchorgonyok jellemzően **kisbetűkkel és kötőjellel elválasztottak**, összhangban a szokásos GitHub-stílusú csúszásokkal.

### Mikor válassz valami mást

A GFM nem replikálja a **MultiMarkdown metaadatok**, **kramdown IAL-ek** vagy **MMD hivatkozás** munkafolyamatokat. Könyvek, szakdolgozatok vagy súlyos metaadatok esetén használja a **MultiMarkdown** vagy **Kramdown** beállítást.

---

## Kedvezmény

**A legjobb:** Egy **gyors, C-alapú** processzor, amely követi a **klasszikus Markdownt** és egy **régebbi GitHub-ízű** funkciókészletet – akkor hasznos, ha az **eredeti Markdown**-hoz, valamint táblázatokhoz, lábjegyzetekhez és kapcsolódó kiterjesztésekhez közelebbi viselkedést szeretne a CommonMark teljes szabálykönyve nélkül.

Projekt otthona: [Kedvezmény](https://www.pell.portland.or.us/~orc/Code/discount/).

### Erősségek

- **PHP Markdown Extra stílusú táblázatok** és sok bővítmény (lábjegyzetek, elkerített kód, ha engedélyezve van, stb. --- lásd Marked [Kedvezményes GFM specifikáció](Discount_GFM_Spec.html), hogy mit engedélyez a Marked).
- **Opcionális „GitHub” extrák** az upstream Discount szolgáltatásban (pl. jelölőnégyzetek listája, ha a megfelelő jelzőkkel készült); A megjelölt az általa szállított kombinációt dokumentálja a Kedvezmény specifikáció oldalán.
- **SmartyPants-stílusú tipográfia** és a Kedvezmény oldalon leírt egyéb kényelmi szolgáltatások (bár az összes mellékelt processzor rendelkezik tipográfiai funkciókkal).
- Filozófiailag közel áll a **John Gruber's Markdown**-hoz, valamint a praktikus bővítményekhez, nem pedig a teljes CommonMark tesztcsomaghoz.

### Mikor válassz valami mást

Ha **pixel-tökéletes paritást szeretne elérni a mai github.com-mal**, válassza a **CommonMark (GFM)** lehetőséget. A **MultiMarkdown metaadatokhoz és hivatkozásokhoz** használja a **MultiMarkdown** lehetőséget.

---

## Gyors összehasonlítás

| Aggodalom | MultiMarkdown | Kramdown | CommonMark (GFM) | Kedvezmény |
|--------|----------------|--------|-------------------|----------|
| **Elsődleges felhasználás** | Próza, dolgozatok, könyvek | Stílusos HTML, Jekyll-szerű webhelyek | README-k, GitHub-szerű dokumentumok | Classic MD + bővítmények |
| **Idézetek / MMD-metaadatok** | Erős | Különböző szintaxison keresztül | Nem | Nem |
| **Kézi címsorazonosító stílus** | `## Title [id]` | `## Title {: #id }` (IAL) | Spec / GitHub slug szabályok | Nincs |
| **Automatikus címsorazonosítók** | Kisbetűk összefűzve | Kisbetűk kötőjellel | Kisbetűk kötőjellel | Kisbetűs kötőjeles |
| **Extra attribútumok (osztályok/azonosítók)** | Korlátozott MMD-mechanizmusok | **IAL-ok** – nagyon erős | Korlátozott | Korlátozott |

---

## Lásd még

- [Beállítások: Processzor](Settings_Processor.html) – alapértelmezett processzor és kapcsolódó opciók
- [Markdown Dingus](Markdown_Dingus.html) — próbálja ki a processzorokat egymás mellett a Markedben
- [Egyedi processzor](Custom_Processor.html) – szükség esetén csatlakoztassa saját eszközláncát