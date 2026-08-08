<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A számok éppúgy számítanak, mint a szavak.

## Képletek előnézete a MathJax segítségével [preview-formulas-with-mathjax]

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

Ha bekapcsolja a MathJaxot a {% prefspane Style %}-ben, a szükséges szkriptek és CSS bekerülnek az előnézetbe. Ezután a MultiMarkdown matematikai szintaxis használható a Markdown dokumentumban, és megjelennek az eredmények.

Példa MMD MathJax szintaxisra:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Ha úgy dönt, hogy a MathJaxot belefoglalja egy exportált HTML-fájlba, akkor a beágyazott MathJax-kód helyett egy CDN-hivatkozás kerül felhasználásra. Ehhez internetkapcsolat szükséges a renderelt MathML megtekintéséhez.

## MathJax forrás: Helyi vs CDN [mathjax-source-local-vs-cdn]

Ha a MathJax engedélyezve van, a Marked betöltheti a következők valamelyikéről:

- **Helyi**: a MathJax v3 másolata az alkalmazáson belül (gyorsabban betöltődik, offline módban működik).
- **CDN**: a hivatalos MathJax v3 CDN (mindig naprakész, nincs hatással az alkalmazáscsomagra).

Az {% prefspane Style %} **MathJax Source** előugró ablakában a következők közül választhat:

- **Helyi** – az ES5 `tex-chtml.js` összetevőt használja az alkalmazáscsomagból.
- **CDN** – ugyanazt a komponenst tölti be a CDN-ről. Ehhez internetkapcsolat szükséges.

Az exportált HTML-fájlok mindig a CDN-ről hivatkoznak a MathJax-re, függetlenül az előnézeti forrástól, így önállóak és kicsik maradnak.

## Egyenletszámozás [equation-numbering]

Az egyenletszámozást a {% prefspane Style %}-ben engedélyezheti. Ez működik a MathJax-szel és a KaTeX-szel is, de belsőleg eltérő módon valósítják meg. A MathJax v3 esetén a Marked leképezi a beállításokat a megfelelő MathJax konfigurációra, így:

- A „Számegyenletek” szabályozza, hogy megjelenjenek-e számok.
- Az „oldal” opció szabályozza, hogy a számok a bal vagy a jobb oldalon jelenjenek-e meg.
- A „Csak AMS” opció az AMS-stílusú egyenletekre korlátozza a számozást.

Ezek az opciók megfelelnek a MathJax `tex.tags` és `tex.tagSide` beállításainak a motorháztető alatt.

## További csomagok [additional-packages]

A MathJax v3 moduláris. A Jelölve mindig engedélyezi az alapvető TeX/AMS-csomagokat, és opcionálisan bekapcsolhat továbbiakat is a {% prefspane Style %} alatt:

- **Fizika** (`physics`) – a fizika jelölései és kényelmei.
- **Kémia** (`mhchem`) – kémiai egyenletek.
- **Bra–ket** (`braket`) – Dirac bra–ket jelölés.
- **félkövér szimbólumok** (`boldsymbol`) – félkövér matematikai szimbólumok.

Kattintson a **További csomagok…** elemre egy kis ellenőrzőlista megnyitásához, ahol be- vagy kikapcsolhatja ezeket a csomagokat. A változtatások a következő alkalommal lépnek életbe, amikor a Marked matematikai adatokat jelenít meg az előnézetben.

## MathJax speciális konfiguráció [mathjax-advanced-configuration]

A Marked alapértelmezett beállításain felül további egyéni konfigurációkat is alkalmazhat, ha hozzáad egy érvényes JSON-objektumot a **Speciális konfiguráció** mezőben. Ez a mező a MathJax v3 konfigurációs objektumba (`window.MathJax`) egyesül a MathJax betöltése előtt. Tartalmazhat [a MathJax v3 által támogatott bármely beállítást](https://docs.mathjax.org/en/latest/options/), például:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "makrók": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "csomagok": { "[+]": ["fizika"] }
        }
    }

Ez a példa beállítja a TeX elválasztókat, hozzáad egy `\tr` makrót, és engedélyezi a `physics` csomagot az alapértelmezett beállítás mellett. Ezekkel a beállításokkal az alábbiak mindegyike megfelelően jelenik meg:

    Soron belüli képlet zárójelekkel, \\\\({x}^{2} {y}^{2}=1\\\\), vagy dollárjelekkel, ${x}^{2} {y}^{2}=1$.

    Megjelenítés megtisztított zárójelekkel:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    Vagy dupla dollárjelekkel:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

A további konfiguráció kiterjeszti a meglévő objektumot, így csak a megadott tulajdonságok kerülnek felülírásra. A meghatározatlan opciók az aktuális beállítás alapértelmezett értékei maradnak.

Vegye figyelembe, hogy a MultiMarkdown processzort nem szabványos határolókkal használva a kifejezésben lévő karakterek elemzésre kerülnek, így az olyan szimbólumok, mint a `*` és a `^` tipográfiai változásokat okoznak, amelyek megszakítják a MathJax processzort. Ilyen esetekben a legjobb megoldás a Kedvezmény processzor használata a [Processzorbeállítások] (x-marked-3://pref/processor) részben.

A Marked egy kis varázslatot hajt végre, ha a MathJax vagy a KaTeX engedélyezve van, és átalakítja a matematikai szintaxist, hogy a lehető legjobban kompatibilis legyen az aktuális processzorral (MultiMarkdown vagy Discount). Ennek minden körülmények között nagyszerűnek kell lennie, de ha úgy találja, hogy problémákat okoz, [lépjen kapcsolatba az ügyfélszolgálattal](https://support.markedapp.com/questions/add)!


## KaTeX [katex]

[katex]: https://katex.org/

A [KaTeX][] elérhető a MathJax alternatívájaként. Könnyebb súlyú, ezért gyorsabban tölthető be, ami nagyszerű lehet a sok képletet tartalmazó dokumentumoknál. Ennek ellenére nem rendelkezik annyi funkcióval, és előfordulhat, hogy egyes MathJax-szel (vagy LaTeX-szel) működő egyenletek nem támogatottak.

## Automatikus egyenletszámozás [számozás] [numbering]

Az egyenletszámozást a {% prefspane Style %}-ben engedélyezheti. Ez MathJax és KaTeX esetén is működik. Kiválaszthatja, hogy a számok az egyenlet bal vagy jobb oldalán jelenjenek-e meg.

### MathJax-ban [in-mathjax]

A MathJax-ban ez a következő beállítást használja:

    {
      TeX: { equationNumbers: { autoNumber: "all" } }
    }

Ha csak az AMS-egyenleteket szeretné számozni, válassza a "Csak AMS" lehetőséget az "oldalsó" legördülő menü jobb oldalán.

### A KaTeX-ben [in-katex]

A KaTeX nem kínál egyenletszámozást. Ennek szimulálásához a Markedben CSS-t használnak, és minden megjelenítési egyenlet számozott.

## Exportálási problémák [export-issues]

A Rich Text formátumok nem kezelik az egyenleteket (sem a MathJax, sem a KaTeX által). Elrejtve lesznek a kimeneti dokumentumban, mivel a speciális betűtípusok belefoglalása nagyobb zűrzavart eredményez, mint gondolná... Ezt remélem valamikor kijavítom, de jelenleg ez a hiányosság.