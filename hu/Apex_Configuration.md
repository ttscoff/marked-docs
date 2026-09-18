<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ezek a beállítások a **Configure Apex** lapon vannak. A {% prefspane Processor %} panelen nyithatók meg, ha az alapértelmezett processzor az **Apex (béta)**. Minden itt lévő beállítás csak az Apexre vonatkozik. A matematika, a Critic Markup, a címkék, a fájlbeillesztések és a címsor-azonosítók a Marked többi beállításában maradnak.

Lásd: [Apex (béta)](Apex.html), hogy mi az Apex, és milyen szintaxist fed le.

A lap jelölőnégyzetei felülírják az Apex metaadatfájl azonos beállításait. A fájlútvonalak nem kötelezők. Ha a Marked nem tudja olvasni az útvonalat, kihagyja, és az előnézet ettől még lefut.

## Fájlok [files]

CSL
: Citation Style Language fájl (`.csl`), amelyet az Apex a bibliográfia formázásához használ. Hagyja üresen, ha a dokumentumban vagy a metaadatfájlban megadott stílust szeretné használni.

Bibliográfia
: Egy vagy több bibliográfiai fájl. Elfogadott típusok: BibTeX (`.bib`), CSL JSON (`.json`) és CSL YAML (`.yml`, `.yaml`). További fájlhoz kattintson az **Add** gombra. Az Apex ezekben keresi a hivatkozásokat.

Konkordancia
: Egy vagy több konkordanciafájl (`.tsv`, `.txt` vagy `.csv`) a tárgymutató készítéséhez. További fájlhoz kattintson az **Add** gombra.

Metaadatfájl
: Külső metaadatfájl (`.yml`, `.yaml`, `.txt` vagy `.md`), amelyet az Apex futása előtt egyesít a dokumentummal. Ha a dokumentum és a fájl ugyanazt a kulcsot adja meg, a dokumentum metaadata az erősebb. A lap jelölőnégyzetei felülírják a metaadatfájl értékeit.

## Szintaxis [syntax]

Alapértelmezés szerint be van kapcsolva, hacsak nincs másképp jelezve.

Táblázatok
: Függőleges vonalas táblázatok, fejlécsorral és elválasztósorral.

Lábjegyzetek
: Hivatkozó lábjegyzetek (`[^id]`) és soron belüli lábjegyzetek.

Definíciós listák
: Kifejezés és definíció listák (`: definition`).

Felső index / alsó index
: `^super^` és `~sub~`. Kapcsolja ki, ha az egyszeres hullámvonal ne jelentsen alsó indexet. A Marked **~text~ aláhúzásként** beállítása külön van, és ütközik az alsó indexszel.

Áthúzás
: `~~deleted~~`.

URL-ek és e-mailek automatikus linkelése
: A csupasz `https://` URL-ek és e-mail-címek linkké válnak.

Kerített div-ek
: `::: name` blokkok, amelyek egy szakaszt `<div>` elembe csomagolnak.

Szögletes span-ek
: Soron belüli attribútumspanek, például `[text]{.class}`.

Betűs listák
: `a.` vagy `A.` kezdetű listák, a számozottakon kívül.

Vegyes listajelölők
: Egy lista keverheti a `*`, `+` és `-` jelölőket, és egy listának számít.

Markdown HTML-ben
: A HTML blokkcímkéken belüli Markdown feldolgozásra kerül. Egyes jelölések ettől még elromolhatnak.

Metaadat-átalakítások
: A `[%key]` helyőrzőket a dokumentum metaadataiból tölti ki.

## Táblázatok és képek [tables-and-images]

Rácstáblázatok
: `+` és `|` jelekkel rajzolt rácstáblázatok. Alapértelmezés szerint ki.

Laza táblázatok
: A vonalas táblázatok elhagyhatják a kezdő és záró vonalakat. Alapértelmezés szerint be.

Cellaenkénti igazítás
: A cella igazításjelölői felülírják az oszlop igazítását. Alapértelmezés szerint be.

Képaláírások
: A kép címe, vagy cím hiányában az alt szöveg, látható képaláírás lesz. Alapértelmezés szerint be.

Csak címfelirat
: Csak a kép címe lesz a képaláírás. Az alt szöveget figyelmen kívül hagyja. Alapértelmezés szerint ki. Nincs hatása, ha a **Képaláírások** ki van kapcsolva.

## Hivatkozások és tárgymutatók [links-and-indexes]

Wikihivatkozások
: Az Apex átalakítja a `[[wiki links]]`. Alapértelmezés szerint ki. Ha be van kapcsolva, a Marked kihagyja a saját „wikihivatkozások átalakítása” előnézeti lépését, és az Apex másképp oldhatja fel a célfájlt, mint a Marked. Az alapértelmezett kiterjesztés a Marked wikihivatkozás-beállításaiból jön.

Wikihivatkozás-URL-ek tisztítása
: A generált URL-eket kisbetűsíti, eltávolítja az aposztrófokat, és a nem betű vagy szám karaktereket lecseréli. Alapértelmezés szerint ki. Csak akkor érhető el, ha a **Wikihivatkozások** be van kapcsolva.

Tárgymutató feldolgozása
: Felismeri a tárgymutató-jelölőket (MultiMarkdown, mmark, Leanpub és textindex stílus). Alapértelmezés szerint be.

Tárgymutató kimenet elrejtése
: Beolvassa a jelölőket, de nem nyomtatja ki a kész tárgymutatót. Alapértelmezés szerint ki.

## Figyelmeztetések (extra) [callouts-extra]

Mindkettő alapértelmezés szerint ki van kapcsolva. Az Obsidian- és Bear-figyelmeztetéseket (`> [!NOTE]`) a Marked az Apex előtt kezeli, itt nem állíthatók.

Python-Markdown figyelmeztetések
: `!!! note` stílusú figyelmeztetések.

Quarto figyelmeztetések
: Quarto `::: {.callout-note}` blokkok.

## Akadálymentesség [accessibility]

Mindkettő alapértelmezés szerint ki van kapcsolva.

ARIA-címkék
: ARIA-attribútumokat ad hozzá, amelyek leírják az Apex által kiadott HTML szerkezetét.

Címsorhorgonyok
: Minden címsorra `<a>` horgonyt ad, nem csak `id` attribútumot a címsoron.
