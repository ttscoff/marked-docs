<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Speed Read egy RSVP-stílusú olvasási mód, amely egy-egy szót jelenít meg fókuszált fedvényben.

## Hogyan működik a Speed Read

A Speed Read a **Rapid Serial Visual Presentation** (RSVP) nevű módszert használja. Ahelyett, hogy a szemét a szövegsorokon mozgatná, a szavak egy rögzített helyen jelennek meg. Ez csökkenti az olvasás során szokásosan előforduló szemmozgásokat, vonalváltásokat és visszalépéseket, ami hasznos lehet a lapozáshoz, az ismerős anyagok áttekintéséhez vagy a szövegben való gyors mozgáshoz anélkül, hogy elveszítené a helyét.

A módszer nem varázslat, és nem garantálja a jobb megértést nagyon nagy sebességnél. A szöveg értése továbbra is az írás összetettségétől, a témában való jártasságától és a WPM beállításától függ. Sűrű vagy ismeretlen anyagok esetén a mérsékelt sebesség általában hatékonyabb, mint a sebesség minél magasabbra tolása.

A piros betű a szó vizuális rögzítési pontját jelöli, amelyet néha **optimális felismerési pontnak** is neveznek. Sok szóval az olvasók akkor azonosítják a szót a leghatékonyabban, ha tekintetük a középponttól kissé balra esik, nem pedig az első betűre. Azáltal, hogy a rögzítési pontot ugyanazon a helyen tartja, és kiemeli, a Speed ​​Read konzisztens célpontot biztosít a szemnek. Az eredmény kevésbé fókuszál a szavak között, és egyenletesebb a ritmus, miközben a szöveg halad előre.

## Nyitási sebesség olvasás

Használja az **Előnézet > Gyorsolvasás** elemet, a **Gyorsolvasás** elemet az előnézeti ablak Fogaskerék menüjében, vagy nyomja meg a {% kbd ctrl opt S %} gombot. A menüelem akkor érhető el, ha a Markdown előnézeti dokumentumablak aktív (a nyers HTML-előnézeteknél le van tiltva, és ha nincs megnyitott dokumentum).

Amikor a Gyorsolvasás megnyílik, szüneteltetve indul el, így a lejátszás megkezdése előtt tájékozódhat.

<video controls preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Az Ön böngészője nem támogatja a Speed Read bemutató videót.
</video>
<p><em>Speed Read fedvény, amely a lejátszásvezérlőket, a szinkronizálási lehetőséget és a súgó elérését mutatja.</em></p>

## Overlay vezérlők

Ha a fedvény látható, a következő billentyűk állnak rendelkezésre:

| Parancsikon | Funkció |
| :-- | :-- |
| {% kbd space %} | Lejátszás/Szünet |
| {% kbd [ %} | Ugrás a bekezdés elejére (az előző bekezdéshez nyomja meg újra) |
| {% kbd ] %} | Ugrás a következő bekezdés elejére |
| {% kbd left %} | Az olvasási sebesség (WPM) csökkentése |
| {% kbd right %} | Olvasási sebesség növelése (WPM) |
| {% kbd esc %} | Kilépés a Speed ​​Read |

A zárójelek rögzítése a bekezdésben történő navigáláshoz, a bal/jobb nyilak pedig a sebességváltoztatáshoz, így ezek a billentyűk nem váltják ki az előnézeti navigációt, amíg a Gyorsolvasás nyitva van. A fedvény bal felső sarkában található kör alakú **X** gombra kattintva is elvetheti.

Más normál előnézeti navigációs billentyűparancsok továbbra is működnek, amíg a Gyorsolvasás aktív, beleértve a `t`/`gg` (fent), `G`/`b` (lent) és `,`/`.` (fejléc-navigáció). A teljes listát lásd az [Előnézeti navigáció] (Keyboard_Shortcuts#preview-navigation) részben.

A tartalomjegyzék gyorsolvasás közben is használható. Nyomja meg a {% kbd cmd t %} gombot a megnyitáshoz és a navigáláshoz, vagy nyomja meg a {% kbd f %} gombot a gyorskeresés azonnali fókuszálásához a dokumentumfejlécek navigálásához.

## Kiválasztásból kiindulva

Ha a Speed Read indításakor szöveg van kiválasztva az előnézetben, a lejátszás a kiválasztott szöveget használja. Ha nincs aktív kijelölés, a Gyorsolvasás a dokumentum teljes szövegét használja.

## Szinkronizálás görgetési pozícióval

Engedélyezze a **Szinkronizálja a gyorsolvasást a görgetési pozícióval** a {% prefspane Preview %} helyen, vagy használja a Gyorsolvasási fedvény jelölőnégyzetét, hogy az előnézet és a gyorsolvasási pozíció együtt maradjon.

Ha ez az opció be van kapcsolva, a gyorsolvasás a dokumentum eleje helyett az előnézet tetején jelenleg látható tartalommal kezdődik. A lejátszás előrehaladtával az előnézet a megjelenített szavakkal együtt gördül.

Ha bezárja a Gyorsolvasást, görgeti az előnézetet, és újra megnyitja az átfedést, a lejátszás az új látható helyről indul. Ha bekapcsolja az átfedés jelölőnégyzetet, miután a Gyorsolvasás már nyitva van, a lejátszás visszaáll az aktuális görgetési pozícióba, és onnan folytatódik.

## Emlékezett sebesség

A WPM értéke automatikusan mentésre kerül, ha a {% kbd ← %} és {% kbd → %} gombokkal módosítja. A kiválasztott sebesség visszaáll a következő alkalommal, amikor a Speed ​​Read funkciót használja.