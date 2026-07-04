<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Többféleképpen is beágyazhat további JavaScripteket a Markedbe.

## Beleértve a dokumentumonkénti JavaScriptet

A szkripteket egyetlen dokumentumba foglalhatja magában a tartalomban található `<script>` címkék használatával. Ez hasznos lehet olyan könyvtáraknál, mint a [D3](https://d3js.org/) olyan adatvizualizációknál, amelyekre csak bizonyos dokumentumokban van szükség:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Ha a MultiMarkdownt használja processzorként, akkor szkripteket is beilleszthet a metaadatokba, és beilleszthetők a dokumentumba. Mivel a Marked csak a "részletet" adja ki, az `XHTML Header` kulcs nem ideális. Ehelyett használja a `CSS Header`-t, és a szkriptek a dokumentum aljára szúródnak be.

	CSS-fejléc: <script src="file.js"></script>

Ha azt szeretné, hogy a mellékelt szkriptek a tartalom megváltozásakor frissüljenek, olvassa el a [Hookok](#hooks) részt.

## Beleértve a JavaScriptet

Felveheti saját JavaScript-kódját helyi fájlokból, CDN-ekből vagy nyers kód beillesztésével. Ennek eléréséhez nyissa meg a {% prefspane Style %}-t, és kattintson az *Egyéni szabályok* gombra.

Állítson be új egyéni szabályt, vagy adjon hozzá szkripteket egy meglévőhöz. Ha minden fájlhoz hozzá szeretné adni a szkripteket, állítsa be a predikátumot a „fájlnév tartalmazza a *” értékre.

Az egyéni szabályok Műveletek szerkesztője három lehetőséget kínál a szkriptek felvételére:

JavaScript fájl beszúrása
: Kiválaszthat egy helyi fájlt, amelyet a dokumentum végére kíván beilleszteni

JavaScript beillesztése az URL-ből
: Lehetővé teszi egy CDN vagy más távoli URL felvételét, amely egy `<script>` címkét hoz létre a dokumentum végén az URL-címmel.

JavaScript beillesztése
: Megnyit egy kódszerkesztőt, amelybe saját JavaScript-kódot írhat/beilleszthet

Ezek a szkriptek az előnézet végére, a dokumentumcímke elé kerülnek beszúrásra. Ha meg kell hívnia egy init függvényt vagy frissítenie kell minden alkalommal, amikor az előnézet frissül, olvassa el a [Nyers JavaScriptet beleértve](#rawjs) című részt, és ismerkedjen meg a Marked [hookjaival] (#hooks).

## Mermaid és egyéb forgatókönyvek {#mermaid}

A jQuery alapértelmezés szerint benne van, és bármely olyan szkriptben használható, amelyet az alábbi módszerek bármelyikével hozzáad a Markedhez.

A [Mermaid](https://mermaid.js.org/intro/) a Markdown-szerű diagramkészítéshez mostantól alapértelmezés szerint minden dokumentumban megtalálható. A `mermaid` nyelvű elkerített kódblokkok automatikusan diagramként jelennek meg.

Az {% prefspane Style %} alján egy "Pásztázási és nagyítási diagramok" jelölőnégyzet érhető el, ha sellőtartalom van jelen. Ha bejelöli ezt a jelölőnégyzetet, a diagramok {% kbd cmd %}-görgetéssel nagyíthatók, majd kattintással és húzással pásztázhatók. A funkció szkriptje egy CDN-ből származik, és internetkapcsolatot igényel.

Ha van egy adott könyvtár, amelyet alapértelmezés szerint szerepeltetni szeretne, tudassa velem a [BrettTerpstra.com fórumon](https://forum.brettterpstra.com/) vagy [a támogatási webhelyen](https://support.markedapp.com/questions/add).

## Horgok [horgok]

A legújabb verzióktól kezdve a Marked már nem hajt végre teljes oldalfrissítést a tartalom frissítésekor, hanem az új tartalmat oldalbetöltés nélkül szúrja be a DOM-ba. Ez azt jelenti, hogy az oldalbetöltéskor aktiválódó szkriptek nem aktiválódnak újra a tartalom frissítésekor. A Marked egy „horgok” funkciót biztosít ehhez. A hook regisztrálásához tartalmaznia kell egy második szkriptblokkot, amely meghívja a [`Marked.hooks.register()` függvényt](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), amely elfogad egy triggert, ebben az esetben az „update”-t, és egy végrehajtandó függvényt.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

A Marked összes [API-funkciója](https://markedapp.com/jsapi/) használható ebben a mezőben. (Az API-t bármely betöltött szkriptben is használhatja.) Az interaktív hibakereséshez és az API-val való kísérletezéshez élő előnézetben tekintse meg a [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) részt a Safari Fejlesztés menüjének Marked funkcióval történő használatáról.

Mostantól, amikor frissítés történik (amikor a figyelt forrásfájlt elmentik), az átadott funkció végrehajtásra kerül. Mindaddig, amíg a futtatott szkriptnek van valamilyen indító vagy renderelő funkciója, egy hook segítségével meghívhatja, és minden alkalommal renderelheti, amikor a dokumentumot elmenti, és frissítést indít el.



*[CDN]: Tartalomelosztó hálózat