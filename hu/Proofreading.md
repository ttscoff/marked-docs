<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Lépjen be a lektorálás módba a fogaskerék menüből. Ez egy kísérleti funkció, amelyet elsősorban azoknak a szerkesztőknek terveztek, akik szöveget kapnak másoktól, és megjegyzéseket kell tenniük és visszajelzést kell adniuk.

A korrektúra mód leállítja a dokumentumfrissítéseket, így megakadályozza, hogy a megjegyzések és megjegyzések elveszjenek a dokumentum frissítésekor. Egy piros jelző jelenik meg a felső sávban, emlékeztetve arra, hogy a korrektúra mód aktív.

Billentyűzet navigáció, könyvjelzők és kulcsszavak kiemelése minden funkció a korrektúra során.

## Annotációk

Lektorálási módban a szöveg kijelölése a dokumentumban egy felugró ablakot generál, amely lehetővé teszi, hogy több különböző kiemelési típus közül válasszon. Kattintson a szöveghez hozzáadni kívánt kiemelés típusára, vagy törölje a "Mégse" gombra kattintva, vagy egyszerűen kattintson a felugró ablakon kívülre.

## Megjegyzések

![Annotations][1]

[1]: images/Annotating.jpg class=center

Miután hozzáadott egy kiemelést, rövid jegyzeteket adhat hozzá a kiemelésre kattintva. A felugró ablak most egy szövegmezőt fog tartalmazni, amelybe beírhat minden olyan megjegyzést, amely a kiemelt szövegre vonatkozik. A jegyzetek törölhetők és szerkeszthetők, ha rákattint egy olyan kiemelésre, amelyhez már tartozik jegyzet.

A megjegyzések **csak** exportálásra kerülnek HTML formátumba történő mentéskor. A kiemelések a legtöbb exportformátumban megmaradnak, beleértve az RTF-et és a PDF-t is.

## Helyesírás-ellenőrzés

Lektorálási módban a rendszerszintű helyesírás-ellenőrzőt a fogaskerék menüből érheti el: {% appmenu {{gear}}, Proofing, Show Spelling Errors %}. Ez lassú lesz nagy dokumentumok esetén, és figyelmeztetés jelenik meg, amely értesíti Önt, ha a folyamat körülbelül 30 másodpercig tart. Mivel a helyesírás-ellenőrző nem működik a Marked webes előnézetében, egy „hack” kerül végrehajtásra, hogy ez működjön, és ez nem gyors.

A helyesírás-ellenőrzés lefutása után megnyithatja a Helyesírási tippek panelt a Nyelvtani ellenőrzés bekapcsolásához, valamint a hibák kijavítására vonatkozó javaslatok megtekintéséhez. A *nem* megjelölve ezeket a helyükön szerkesztheti, az eredmények felhasználásához vissza kell térnie az eredeti dokumentumhoz.

*Parancsikonok:* {% kbd ctrl opt cmd S %} futtatja a helyesírás-ellenőrzőt. A {% kbd ctrl opt cmd N %} a dokumentum következő hibájára lép, a {% kbd ctrl opt cmd G %} pedig a találgatások panelt jeleníti meg.