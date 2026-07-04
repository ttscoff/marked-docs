<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Feliratok

## Medve/Obszidián ##

A Marked támogatja az Obsidian és Bear által használt szintaxisú feliratokat, amely egy speciálisan formázott blokk idézet:

	> [!MEGJEGYZÉS] Megjegyzés címe
	> További szöveg

A „MEGJEGYZÉS” az `[!NOTE]`-ben nem különbözteti meg a kis- és nagybetűket. Bármelyik lehet:

- MEGJEGYZÉS
- ABSZTRAKT, ÖSSZEFOGLALÓ, TLDR
- INFORMÁCIÓ
- TODO
- TIPP, TIPP, FONTOS
- SIKER, ELLENŐRZÉS, KÉSZ
- KÉRDÉS, SEGÍTSÉG, GYIK
- FIGYELEM, VIGYÁZAT, FIGYELEM
- SIKERTELEN, SIKERTELEN, HIÁNYZAT
- VESZÉLY, HIBA
- BUG
- PÉLDA
- IDÉZET, CITE

Ezek speciálisan formázott blokkokat hoznak létre.

Használhat egy `+` vagy `-` jelet a kiemelés összecsukhatóvá tételéhez. A pluszjel (`+`) azt jelenti, hogy a kiemelés összecsukható, de alapértelmezés szerint megnyílik. A mínuszjel (`-`) azt jelenti, hogy a kiemelés összecsukható, de alapértelmezés szerint zárt.

  ![Callouts in Marked][callouts]

[callouts]: images/callouts-800.jpg @2x width=800

### Xcode Playground ###

Az Xcode Playground fájlok előnézetének megtekintésekor a Marked támogatja a natív Xcode Playground kiemelés szintaxisát:

	- Figyelem: Választható cím
	A kiemelés tartalma ide kerül.

A kiemelés típusa (pl. "Figyelem") nem különbözteti meg a kis- és nagybetűket, és a következő Xcode Playground kiemelési típusok bármelyike lehet:

- **Figyelem** - Információs feliratként formázva
- **Szerző** - Metaadatok kiemelése
- **Szerzők** - Metaadatok kiemelése
- **Hiba** - Hiba/veszély jelzés
- **Bonyolultság** - Jegyzetszerű kiemelés
- **Szerzői jog** - Metaadat kiemelés
- **Egyéni kiemelés** - Példaszerű kiemelés
- **Dátum** - Metaadatok kiemelése
- **Példa** - Példa kiemelésre
- **Kísérlet** - Tipp stílusú kiemelés
- **Fontos** - Információs stílusú kiemelés
- **Változatlan** - Jegyzetszerű kiemelés
- **Megjegyzés** - Megjegyzés kiemelés
- **Előfeltétel** - Jegyzetszerű kiemelés
- **Utólagos állapot** - Jegyzetszerű kiemelés
- **Megjegyzés** - Jegyzetszerű kiemelés
- **Szükséges** - Jegyzetszerű kiemelés
- **Lásd még** - Információs stílusú kiemelés
- **Azóta** - Metaadat kiemelés
- **Verzió** - Metaadat kiemelés
- **Figyelmeztetés** - Figyelmeztető felirat

A kettőspont utáni opcionális cím lesz a kiemelés címe. Ha nincs megadva cím, a kiemelés típusának neve lesz címként használatos.

A kiemelés tartalma azonnal következik a következő sorban (nincs szükség üres sorra). A tartalom egy üres sorig, a következő kiemelésig, egy elkerített kódblokkig vagy a dokumentum végéig folytatódik.

Példa:

````leértékelés
- Fontos: Teljesítményre vonatkozó megjegyzés
Ez az algoritmus O(n log n) bonyolultságú.

- Példa: Gyors rendezés
A megvalósítás módja:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

A címet teljesen elhagyhatod:

	- Figyelmeztetés
	Ez egyéni cím nélküli figyelmeztetés.

Ezeket a feliratokat a rendszer automatikusan konvertálja a Marked kiemelési formátumára, és megfelelő stílust alakít ki. Az eredeti kiemelés típusa megmarad a `data-callout` attribútumban, amely lehetővé teszi az egyéni CSS-stílus használatát, ha szükséges.

> Ez a funkció csak az Xcode Playground fájlok előnézetének megtekintésekor működik (`.playground`). A normál leíró fájlok nem dolgozzák fel ezt a szintaxist.


## Tartalomjegyzék

A `<!--TOC-->` segítségével megadhatja, hogy a dokumentumban hol jelenjen meg a tartalomjegyzék. Ha ez be van állítva, akkor ez felülírja a Beállításokban található beállítást, és mindig megjelenik az előnézeti ablakban, valamint mentéskor és nyomtatáskor. A tartalomjegyzék csak egyszer jelenik meg, még akkor is, ha a tartalomban több `<!--TOC-->` specifikáció található.

Ha hozzáadja a `max#` értéket a fenti címkéhez (ahol a # egy 1 és 5 közötti számjegy), ez szabályozza a megjelenített tartalomjegyzék mélységét. Például a `<!--TOC max2-->` csak az első és a második szintű fejlécet jeleníti meg a listában. A `<!--TOC min2-->` gombbal megadhat egy minimális fejlécszintet is. A maximumok és minimumok a tényleges címsorszinteken alapulnak, nem a beágyazási szinteken. Maximum és minimum együtt használható.

A Marked felismeri a MultiMarkdown-stílusú `{{TOC}}` és a Pandoc-stílusú `{{TOC:2-6}}` karaktereket is, ahol a `2-6` a fejlécek minimális és maximális szintjének tartománya.

Alapértelmezés szerint a tartalomjegyzék a dokumentum első oldalára kerül nyomtatásra, ha a „Tartalomjegyzék nyomtatása” engedélyezve van a {% prefspane Export %} alatt. Ha van jelölő a dokumentumban, akkor az arra a pontra kerül helyette.

I> Megadhatja a beágyazott tartalomjegyzék-hierarchia egyes szintjei számozásának vagy betűinek típusát az {% prefspane Export %}-ben.

## Oldaltörések

A következő szintaxis használatával oldaltörést kényszeríthet a nyomtatási/PDF-kimenethez:

```html
<!--BREAK-->
```

Helyezze a tokent önmagában egy sorra, és ez olyan jelölést generál, amely új oldalt kényszerít ezen a ponton. A Marked a Leanpub formátumot is megérti:

	{::oldaltörés /}

## Az automatikus görgetés szünetel [szünet]

A Marked az [Autoscroll](Autoscroll.html) funkció használatával távközlőként működhet (hozzá kell adnia a [Teleprompter style](https://markedapp.com/styles/preview?style=teleprompter)) funkciót. Ilyenkor hasznos lehet szüneteket beiktatni a dokumentumba. Tegye ezt a következő használatával:

```html
<!--PAUSE:X-->
```

Ahol `X` az a másodpercek száma, ameddig a Megjelöltnek szünetet kell tartania. Tehát a `<!--PAUSE:15-->` beillesztése 15 másodperces szünetet ad, amikor a dokumentum adott pontja eléri a képernyő közepét.

## A fájl tartalmazza

További fájlok tartalma a szintaxis használatával illeszthető be:

	<<[mappa/fájlnév]

A fájl elérési útja lehet az indexfájlhoz képest relatív vagy abszolút. Az Includes beágyazható; ugyanezt a szintaxist használhatja egy mellékelt fájlon belül is. Ha relatív elérési utakat használ, a beágyazott fájlokban lévő szerepeltetésnek relatívnak kell lennie az adott fájlhoz. ***Azonban*** a MultiMarkdown mindent az első megnyitott fájl helye alapján dolgoz fel, így minden képútvonalnak vagy egyéb beágyazásnak relatívnak kell lennie az első szülőfájlhoz képest, még akkor is, ha az alárendelt dokumentumokban szerepel.

A MultiMarkdown metaadatok és a YAML-fejlécek renderelés előtt automatikusan eltávolíthatók a mellékelt fájlokból. Ez megakadályozza, hogy a fejlécek megjelenjenek a dokumentumban, de ügyeljen arra, hogy az olyan metaadatokat, mint az "alapfejléc szintje", figyelmen kívül hagyja a mellékelt dokumentumokban.

T> Vegye figyelembe, hogy a mellékelt fájlokat tartalmazó dokumentumok megtekintésekor az "I" (shift-i) beírásával megtekintheti, hogy melyik fájl van a látható területen.

További információért lásd a ["Többfájlos dokumentumok"][ext] részt.

[ext]: Multi-File_Documents.html

## Kóddal együtt

A megjelölt tartalmazhat külső fájlokat kódként, a fenti fájlokhoz hasonló szintaxissal:

	<<(mappa/fájlnév)

Szögletes zárójelek helyett vegye figyelembe a zárójelet. A Leanpub szintaxissal való kompatibilitás érdekében a Marked a címet tartalmazó előző szögletes zárójeleket is felismeri, de jelenleg semmi sem történik vele a Markedben:

	<<[Kódcím](mappa/fájlnév)

A megadott fájl tartalma egy pre>kód blokkba kerül be a dokumentumba, és elérhető lesz az automatikus szintaxis kiemeléshez, ha engedélyezve van. A kódblokkok nem ágyazhatók be, és a MultiMarkdown nem dolgozza fel őket. Az egyéni processzorok továbbra is a létrehozott pre>kód blokkon futnak.

## Beleértve a feldolgozatlan szöveget vagy html-t

E> **Megjegyzés:** Ez a funkció haladó felhasználók számára készült.

Ha nyers HTML-t vagy más olyan szöveget szeretne belefoglalni, amelyet a MultiMarkdown (vagy az egyéni processzor) nem dolgozhat fel, zárójelek (`{}`) segítségével hozzáadhat egy fájlt, *miután* feldolgozta a dokumentum többi részét:

	<<{folder/raw_file.html}

Ezekben a fájlokban a rendszer nem ismeri fel a belefoglaló szintaxist (nincs egymásba ágyazás), és a fájl **nyers** tartalma bekerül a végső HTML-kimenetbe. Ez nagyszerű a HTML beszúrásához anélkül, hogy a szövegfeldolgozó leakadna, vagy ha nem szeretné, hogy konvertálják/kihagyják a dolgokat, de legyen óvatos, mivel kevés biztosíték van annak biztosítására, hogy a beszúrt szöveg körül a dokumentum formázása megmaradjon.