<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked Mac App Store (MAS) verziója sandbox környezetben fut, amely biztonsági okokból korlátoz bizonyos műveleteket. Ez hatással lehet néhány szolgáltatásra, különösen, ha egyéni processzorokat használ külső binárisokkal vagy szkriptekkel.

## Általános Sandbox korlátozások

### A Command Binaries futtatása

A felhasználók által tapasztalt leggyakoribb probléma az, hogy a külső bináris fájlokat nem lehet közvetlenül végrehajtani a MAS verzióban. Ez érinti:

- **Külső processzorok**, például Pandoc, Kramdown vagy más parancssori eszközök
- **Egyéni szkriptek**, amelyek külső binárisokra támaszkodnak
- **Rendszer segédprogramok**, amelyek nem érhetők el a homokozóból

### Megoldások

#### Bináris fájlok másolása az App Bundle csomagba

Ha külső processzorokat, például Pandoc-ot kell használnia a MAS verzióban, átmásolhatja a bináris fájlt az alkalmazáscsomagba:

1. Kattintson jobb gombbal a Marked.app → **Csomag tartalmának megjelenítése** lehetőségre.
2. Keresse meg a **Tartalom/Források/**
3. Ha nem létezik, hozzon létre egy `bin` mappát
4. Másolja a bináris fájlt (pl. `pandoc`) ebbe a `bin` mappába
5. Tegye végrehajthatóvá: `chmod +x` a bináris
6. A Parancs futtatása műveletben hivatkozzon rá:
   - `YOUR_BINARY_NAME [arguments]`
   - Vagy használja a teljes elérési utat: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Megjegyzés**: A külső shebang-okat tartalmazó szkriptek (például a `/opt/homebrew/bin/python`-re mutató Python-szkriptek) automatikusan végrehajtásra kerülnek a rendszer értelmezőin keresztül, amikor a csomagba másolják őket. A MAS-verziónak továbbra is gondjai lehetnek a bináris fájlok helyett valójában Python- vagy Ruby-szkriptek végrehajtásával.

**Fontos**: Minden alkalmazásfrissítés után újra át kell másolnia a bináris fájlokat, mivel a frissítések felváltják a teljes csomagot.

#### Beágyazott szkriptek használata

Külső parancsok futtatása helyett használhatja a **Beágyazott parancsfájl futtatása** műveletet az egyéni szabályokban. Ez lehetővé teszi, hogy közvetlenül a Marked kódszerkesztőjébe írjon szkripteket, amelyek hozzáférhetnek a sandboxon belül elérhető rendszerértelmezésekhez.

## Váltás a nem homokozós verzióra [crossgrade]

Ha gyakran kell külső bináris fájlokat használnia, vagy más sandbox-korlátozásokba ütközik, érdemes átváltani a Marked nem sandboxos verziójára. A nem homokozós verziónak nincsenek ilyen korlátozásai, és bármilyen telepített parancssori eszközt vagy szkriptet futtathat.

### Előfizetéses felhasználóknak

Ha aktív Mac App Store-előfizetéssel rendelkezik:

1. **Szüntesse meg MAS-előfizetését** a Rendszerbeállítások → Apple ID → Média és vásárlások → Előfizetések menüpontban.
2. **Töltse le az ingyenes próbaverziót** innen: [https://markedapp.com](https://markedapp.com)
3. **Indítson el egy Paddle-előfizetést** közvetlenül az alkalmazáson vagy a webhelyen keresztül

A Paddle verzió ugyanazokat a szolgáltatásokat kínálja, homokozó korlátozások nélkül.

### Állandó feloldó tartókhoz

Ha végleges feloldást vagy élettartamra szóló licencet vásárolt a Mac App Store-on keresztül, kérjük, [küldje el e-mailben a fejlesztő](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Please%20include%20 a%20UUID%20%28Súgó-%3ECopy%20UUID%20in%20Megjelölve%29%20in%20e%20e-mail%20a%20receipt%20ellenőrzés.) hogy ingyenes életre szóló Paddle licencet kérjen.

**Fontos**: A vásárlás igazolásához kérjük, adja meg az alábbiak egyikét az e-mailben:

- Az Ön **felhasználói azonosítója** (UUID) - a **Súgó->UUID másolása** segítségével másolja a vágólapra, majd illessze be az e-mailbe
- Az Ön **tranzakciós azonosítója** az App Store nyugtáján (ezt megtalálhatja a vásárlási előzmények között az App Store alkalmazásban)

A Mac App Store nem adja meg az Ön e-mail címét a fejlesztők számára, ezért a vásárlásokat a szerverünkön tárolt tranzakcióazonosítók vagy felhasználói azonosítók segítségével igazoljuk. Ezen információk megadása segít nekünk a vásárlás gyors ellenőrzésében és az ingyenes Paddle licenc létrehozásában.

### Setapp verzió

Alternatív megoldásként, ha rendelkezik Setapp-előfizetéssel, használhatja a Marked Setapp verzióját, amely szintén nem homokozó, és teljes hozzáféréssel rendelkezik a rendszererőforrásokhoz.

## További források

További információ az egyéni processzorokról és képességeikről: [Egyéni processzor](Custom_Processor.html).