<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

### Hibakeresési mód

A hibakeresési naplózás engedélyezéséhez nyissa meg a {% prefspane Advanced %}-t, és jelölje be a **Hibakeresési mód** jelölőnégyzetet a panel alján. Ez megjelenít egy legördülő menüt, ahol beállíthatja, hogy milyen naplózási szintet szeretne látni:

- **Csak hibák**: Csak a súlyos hibák kerülnek naplózásra
- **Hibák és figyelmeztetések**: Ezen kívül kevésbé sürgős figyelmeztetéseket jelenít meg
- **Mind**: hibák, figyelmeztetések és információs szintű hibakeresési üzenetek megjelenítése. Ez az ajánlott beállítás a hibaelhárításhoz.

{% note %}
TODO: Ez még mindig működik?
Ezeket a lehetőségeket úgy is elérheti, hogy lenyomva tartja a {% kbd opt  %} billentyűt, amikor megnyitja a {% appmenu Help %} gombot a menüsorban.
{% endnote %}

### A napló megtekintése

Ha a **Hibakeresési mód** engedélyezve van, megnyithatja az {% appmenu Help %} menüt, és kiválaszthatja a Hibakeresési napló megnyitása lehetőséget. Ezzel megnyílik Marked naplója a Console.app alkalmazásban, amely élőben frissül, amint a Marked használata közben naplóüzeneteket adnak hozzá.

### Egyéni szabályok hibaelhárítása

[Egyéni előfeldolgozók és processzorok](Custom_Processor.html) saját naplófelületet kapnak. Az ablak megnyitásához válassza a {% appmenu Help, Show Custom Rules Log %} lehetőséget. Ez az ablak egy színes naplót jelenít meg, amely megmutatja, hogy mely szabályok feleltek meg, és milyen parancsokat futtatnak.

### Probléma bejelentése

Használja a {% appmenu Help, Report an Issue %} gombot egy ablak megnyitásához, amely a leggyakoribb billentyűk beállításait, valamint egy sablont a hibajelentés létrehozásához. Használja a "Másolás vágólapra" gombot az ablak tartalmának másolásához, majd kattintson a "Támogatási webhely megnyitása" gombra az [új kérdés űrlap] (https://support.markedapp.com/questions/add) megnyitásához, ahová beillesztheti jelentését. Igyekszem 48 órán belül válaszolni a bejelentésekre.