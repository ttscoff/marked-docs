<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% appmenu File, New, Streaming Preview %} megnyitásával a Marked élő frissítéseket kap egy elnevezett kartonon keresztül, ahelyett, hogy egy fájlt nézne a lemezen. A forrásalkalmazásnak integrálnia kell a Marked alkalmazást.

[Curio](Curio.html), [Piszkozatok](Drafts.html) és [Az archívum](The_Archive.html) és a [Traverse](Traverse.html) dokumentálják saját kapcsolóit és menüparancsaikat. Az nvUltra, nvALT, Bear és mások ugyanazt a csatornát használják: nyissa meg a streaming előnézetét a Marked alkalmazásban, engedélyezze az integrációt a szerkesztőben, és kezdjen el gépelni; a frissítések közel valós időben érkeznek.

## Fejlesztők [developers]

A Streaming Preview és az alkalmazás integrálásához csak el kell helyeznie a megjelölt szöveget az előnézethez egy elnevezett vágólapra. Használja a következő kódot (Objective-C) a frissítéshez, lehetőleg didEndEditing módszerrel vagy korlátozott időközönként:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### A forrásalkalmazás és a formátum megadása [declaring-the-origin-app-and-format]

Tegyen egy `source` vagy `format` kulcsszót egy HTML-megjegyzésbe a küldött szöveg elejére. A Marked beolvassa a megjegyzést, és kiveszi az előnézetből, így a jegyzet kompatibilis marad a GFM és MultiMarkdown processzorokkal. A kettőspont utáni szóköz nem kötelező (`source:Bear.app` és `source: Bear.app` ugyanaz), és a kulcsszó nem különbözteti meg a kis- és nagybetűket.

Mindkét érték szabad szöveg. Néhányhoz a Marked beépített viselkedést ad, és minden érték elérhető a [Custom Processor](Custom_Processor.html) (Conductor) feltételei között **Streaming-előnézet forrása** és **Streaming-előnézet formátuma** néven. Ezek a feltételek az **egyenlő**, **nem egyenlő**, **tartalmazza** és **nem tartalmazza** összehasonlítót fogadják.

A **`source: APP_NAME`** megnevezi a forrásalkalmazást, az app nevével vagy a bundle id-jével. A Marked ezzel ad külön kezelést annak az appnak. A `source: Bear.app` és a `source: Drafts.app` bekapcsolja ezeknek az appoknak az előnézeti viselkedését. Bármely más név is összevethető egy Conductor-szabállyal, így saját műveleteket futtathat ahhoz az apphoz:

```html
<!--source:Bear.app-->
```

A **`format: fountain`** bekapcsolja a [Fountain](Fountain_for_Screenwriters.html) kezelését, így a folyam forgatókönyvként jelenik meg, nem Markdownként. Bármely más formátumérték nem változtatja a processzort. Arra való, hogy egy Conductor-szabály összevesse, például **Streaming-előnézet formátuma** `egyenlő` `fountain`.

```html
<!--format:fountain-->
```

Egy megjegyzés mindkét kulcsszót tartalmazhatja:

```html
<!--
source: Bear.app
format: fountain
-->
```

### A Streaming előnézetének programozott megnyitása [opening-the-streaming-preview-programatically]

Alkalmazása a `x-marked-3://stream/` URL-kezelő módszerrel programozottan is megnyithatja a Streaming előnézetet. Ez a módszer egy `x-success` paramétert is elfogad, amelyben átadhatja egy alkalmazás csomagazonosítóját, amely a befejezés után aktiválódik.