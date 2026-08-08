<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked kétféleképpen működik az [Obsidian][obsidian-app] jegyzetekkel: nyisson meg egy **vault mappát** az automatikus követéshez, vagy használja a **közösségi beépülő modult** a szorosabb szinkronizáláshoz.

Az Obsidian beépített előnézete ideális, ha soha nem hagyja el az alkalmazást. Válassza a Megjelölve lehetőséget, ha közzétételi minőségű exportálást, speciális lektorálást, egyéni CSS-témákat vagy ugyanazt az élő előnézeti munkafolyamatot szeretné több szerkesztőn keresztül. A teljes összehasonlításhoz lásd a [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) részt.

## Nyisson meg egy teljes trezort [open-an-entire-vault]

Húzza a **vault mappát** (az Obsidian rejtett konfigurációs mappáját tartalmazó könyvtárat a tároló gyökerében) a Marked in the Dock-ba. A Megjelölt figyeli ezt a fát, megtartja a **legutóbb szerkesztett** megjegyzést az előnézetben, és az Obsidianban történő mentéskor frissül.

A tárolóspecifikus alapértelmezett beállításokhoz (stílus, processzor, képek alap URL-je stb.) adjon hozzá egy [Egyéni szabályt] (http://support.markedapp.com), amely megfelel az adott tároló elérési útjainak.

## Obszidián kiemelés szintaxisa [obsidian-callout-syntax]

Amikor a MultiMarkdown processzor fut, a Marked a gyakori **Obszidián-stílusú kiemeléseket** (az `> [!note]` mintát) stílusos blokkjelölésekké alakítja, így azok illeszkednek az előnézet többi részéhez.

## Marked 3 Obsidian plugin [marked-3-obsidian-plugin]

A [Marked 3 Obsidian plugin][plugin] parancsokkal vagy gyorsbillentyűkkel meg tudja nyitni az aktuális jegyzetet vagy az egész tárolót, így a Marked ablak követi, hogy mit szerkeszt. Használja a Parancspalettát (**⌘P**), és keresse meg a **Megjelölt** kifejezést, vagy rendeljen hozzá gyorsbillentyűket az Obsidian **Hotkeys** beállításaiban.

### Telepítés közösségi beépülő modulokból [installing-from-community-plugins]

Az Obsidianban nyissa meg a **Beállítások → Közösségi beépülő modulok** menüpontot, böngésszen vagy keressen a **megjelölt** elemre, és telepítse a **Megnyitás Markedben** elemet.

### A bővítmény manuális telepítése [manually-installing-the-plugin]

Ha inkább a GitHubról szeretne telepíteni:

1. Töltse le a `main.js` és `manifest.json` fájlokat a [legújabb kiadás][plugin-releases] GitHubon (vagy készítse el őket a [Marked3-obsidian][plugin] tárolóból).
2. A tárolóban hozza létre a beépülő modul mappáját a `plugins/` alatt az Obsidian konfigurációs könyvtárában, a tároló gyökérjében. A mappa nevének meg kell egyeznie a `id` beépülő modullal a `manifest.json`-ben (a teljes elérési útért lásd a [plugin README][plugin] részt).
3. Másolja a `main.js` és a `manifest.json` jelet ebbe a mappába.
4. Az Obsidianban nyissa meg a **Beállítások → Közösségi beépülő modulok** menüpontot, szükség esetén kapcsolja ki a **Korlátozott módot**, és engedélyezze a **Megnyitás megjelöltben** lehetőséget.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest