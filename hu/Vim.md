<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [vim-marked][vimrepo] egy Vim beépülő modul, amely megnyitja az aktuális Markdown puffert a Marked alkalmazásban. Hozzáadja az `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` és `:MarkedPreview` karaktereket, így elküldheti a fájlt (vagy egy tartományt) a Marked alkalmazásba anélkül, hogy elhagyná a szerkesztőt.

## Beállítás

Telepítse a bővítménykezelővel; lásd a [README][vimrepo projektet] az `vim-plug` és egyéb lehetőségekért. Az alapértelmezett `g:marked_filetypes` tartalmazza a `markdown`-t és a gyakori változatokat; bővítse ki a listát, ha egyéni `filetype`-t használ.

## macOS és az alkalmazás neve

A megjelölt csak macOS-re vonatkozik, így a beépülő modul nem töltődik be más rendszerekre. Az alkalmazás alapértelmezett neve **2-val jelölve**; ha a Marked más néven vagy elérési úton van telepítve, állítsa be a `g:marked_app` értéket, hogy megfeleljen (például az alkalmazáscsomag teljes elérési útja). A README lefedi a kilépést, az automatikus kilépést és a fókuszálási viselkedést.

I> Ez a súgótéma nem része a vim-jelölt projektnek; a legfrissebb parancsokhoz és beállításokhoz használja a [GitHub-tárolót][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked