<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Felveheti saját JavaScript-kódját CDN-ekből vagy nyers kód beillesztésével.

## Megjegyzés a megjelölt karmesterről

A dokumentumtípusonként és helyenként változó egyéni JavaScript megvalósításának legegyszerűbb módja a [Marked Conductor][conductor]. Lehetővé teszi, hogy YAML konfigurációt használjon szkriptek hozzáfűzéséhez "szűrők" segítségével. Nézze meg a [Conductor page][conductor] oldalt a részletekért, és tekintse meg a [sample config][sample config] példákat.

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## JavaScript hozzáadása a CDN-ekből [cdns]

![][1]

   [1]: images/screenshots/AdditionalJavascript.jpg @2x width=592px height=576px class=center

JavaScript CDN URL-címeket adhat hozzá a „További szkriptek” ablakban, amely innen érhető el: {% prefspane Style %}. Adja meg a CDN URL-címeket, soronként egyet. Ne adjon meg semmilyen `<script>` címkét, csak az URL-t:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> Vegye figyelembe, hogy a jQuery már szerepel az előnézeti ablakban.

Ezek a szkriptek az előnézet végére, a dokumentumcímke elé kerülnek beszúrásra. Ha meg kell hívnia egy init függvényt vagy frissítenie kell minden alkalommal, amikor az előnézet megteszi, olvassa el a [Nyers JavaScriptet beleértve](#rawjs) című részt. A DOM ellenőrzéséhez és ezeknek a szkripteknek egy élő Marked előnézetben történő hibakereséséhez csatolja a Safari Web Inspector alkalmazást a [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) részben leírtak szerint.


### Beleértve a nyers JavaScriptet [rawjs]

A További szkriptek ablak alsó szövegmezőjébe nyers JavaScriptet szúrhat be. Ez egy `<script></script>` páron belül fog szerepelni, ezért ne szerepeltesse a bemenetben. Ez a mező bármilyen JavaScript-parancsot tartalmazhat, amelyre szüksége van egy adott könyvtár inicializálásához, DOM-módosítások végrehajtásához, vagy bármi máshoz, amelyet a WebKit nézetben szeretne végrehajtani. A jQuery már benne van a DOM-kezelés megkönnyítése érdekében.

Ezek a szkriptek csak az ablak első betöltésekor futnak. Amikor az előnézet frissül, az a helyén történik a DOM egyes részeinek cseréjével, tehát a frissített tartalomra reagáló szkripteknek ezt a [Hookok](Embedding_Scripts.html#hooks) használatával kell megtenniük.

A nyers JavaScript mezőbe írjon be egy ilyen hívást:

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
