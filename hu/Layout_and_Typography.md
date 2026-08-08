<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked alapértelmezéseket biztosít a tipográfia és az exportelrendezés javításához, valamint a beállítások véges szabályozását, ha további testreszabásra van szüksége.

## Tipográfia [typography]

### Kötőjelölés és özvegyek [hyphenation-and-widows]

Az _Automatikus elválasztás a bekezdésekben_ beállítás lehetővé teszi, hogy a Marked meghatározza, hol lenne a legjobb egy sor elválasztása a bekezdés "rongyának" javítása érdekében. Ez akkor a leghasznosabb, ha igazított igazítású stílust használ, de javíthatja az olvasási folyamatot a hosszabb bekezdésekben is.

Az _Özvegyek elkerülése a címsorokban és bekezdésekben_ beállítás, ha engedélyezve van, töréseket kényszerít a címsorokban és bekezdésekben, hogy megakadályozza, hogy egyetlen, rövid szavak maguktól egy sorba kerüljenek.

A Megjelölt automatikusan összekapcsolja a címsorokat a következő elemmel, hogy elkerülje az árva címsorokat oldalszámozott formátumba (PDF, nyomtatás) történő exportáláskor.

### Írásjelek [punctuation-marks]

Ha a processzor MultiMarkdownra van állítva, akkor a _Tipográfiailag helyes idézőjelek és írásjelek generálása_ opció segítségével engedélyezheti vagy letilthatja az "intelligens írásjeleket". Ha engedélyezve van, a párosított dupla és szimpla idézőjelek "göndör" idézőjelekké alakulnak, az aposztrófokat tipográfiailag helyes szimbólumokra cserélik, és egyéb automatikus módosításokat hajtanak végre.

### Lábjegyzetjelzők [footnote-markers]

A {% prefspane Style %} Elrendezés és tipográfia részében a _Surround lábjegyzetjelzők szögletes zárójelekkel_ alapértelmezés szerint engedélyezve van a MultiMarkdown processzor használatakor, és lábjegyzetjelzőket hoz létre a dokumentumon belül, amelyeket szögletes zárójelek vesznek körül (pl. "[1]"). A szögletes zárójelek létrehozásának letiltásához törölje a jelölőnégyzetet.

## Vázlat mód [outline-mode]

A Vázlat mód minden olyan fájlt megjelenít, amely hierarchikus fejlécsorozatot tartalmaz APA vagy decimális körvonalként. Az alapértelmezett az APA stílus, de ez ki is kapcsolható.

Az „Elrendezés és tipográfia” alatti {% prefspane Style %} részben olyan fájlnév-kiterjesztéseket adhat hozzá, amelyeknél a Vázlat mód automatikusan engedélyezve van. Ez különösen hasznos az OPML és a támogatott gondolattérkép-fájlok (például iThoughtsX és MindNode) esetén. A kiterjesztés csak a fájlnév alfanumerikus része lehet, amely az utolsó pont karakter után jelenik meg.

Váltsa át az alapértelmezett körvonalmódot az _APA-stílus használata_ jelölőnégyzet segítségével. Ez ideiglenesen átkapcsolható egy dokumentumablak Fogaskerék menüjéből.


## Költészet [poetry]

A _Szó szerinti kódblokkok stílusa költészetként_ beállítás a {% prefspane Style %}-ben a 4 vagy több szóközzel behúzott blokkokat a téma „költészet” stílusával jeleníti meg. Ez általában egy szintaxis nélkül kiemelt, dőlt betűs szakasz.

A sortörések ezekben a blokkokban alapértelmezés szerint megmaradnak, így egyszerű módot kínál a verses és dalszövegrészek beillesztésére egy olyan dokumentumba, amelyhez nincs szükség más kódblokkra.

> Ez a beállítás hozzáad egy "költészet" törzsosztályt, amely egyéni témákban használható a kódblokkok és más elemek stílusához, ha a "költészet mód" engedélyezett.

## Kódblokk burkolása [code-block-wrapping]

A _Témák kódblokkba tördelésének engedélyezése_ lehetővé teszi, hogy az előnézeti stílus határozza meg a kódblokkok formázását. Ennek az opciónak a letiltása arra kényszeríti az összes kódblokkot, hogy vízszintes túlcsordulást görgesse, ahelyett, hogy becsomagolná, függetlenül az aktuális előnézeti stílustól.

## Teljes képernyős működés [working-full-screen]

A Megjelölve teljes képernyős módban (Control-Command-F) használatakor érdemes lehet korlátozni a megjelenített szöveg szélességét, hogy egy olvasható tartalom középső oszlopát hozzon létre. A _Szövegszélesség korlátozása az előnézetben_ jelölőnégyzet engedélyez egy csúszkát, amellyel meghatározhatja a megjelenített tartalom maximális szélességét. Ez a nem teljes képernyős megjelenítést is érinti.