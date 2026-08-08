<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A {% appmenu File, New, Streaming Preview %} megnyitásával a Marked élő frissítéseket kap egy elnevezett kartonon keresztül, ahelyett, hogy egy fájlt nézne a lemezen. A forrásalkalmazásnak integrálnia kell a Marked alkalmazást.

[Curio](Curio.html), [Piszkozatok](Drafts.html) és [Az archívum](The_Archive.html) dokumentálják saját kapcsolóit és menüparancsaikat. Az nvUltra, nvALT, Bear és mások ugyanazt a csatornát használják: nyissa meg a streaming előnézetét a Marked alkalmazásban, engedélyezze az integrációt a szerkesztőben, és kezdjen el gépelni; a frissítések közel valós időben érkeznek.

## Fejlesztők [developers]

A Streaming Preview és az alkalmazás integrálásához csak el kell helyeznie a megjelölt szöveget az előnézethez egy elnevezett vágólapra. Használja a következő kódot (Objective-C) a frissítéshez, lehetőleg didEndEditing módszerrel vagy korlátozott időközönként:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Alap URL deklarálása a relatív eszközökhöz [declaring-a-base-url-for-relative-assets]

Megadhat egy alap URL-t is a streaming előnézetéhez, lehetővé téve, hogy a képekben és más elemekben lévő relatív URL-ek úgy működjenek, mint a forrásalkalmazásban. Ha az alap URL fájlnevet tartalmaz, akkor annak neve és kiterjesztése elérhető lesz az egyéni processzorok számára, de ez nem kötelező. Az alap URL megadásához egyszerűen helyezzen el egy NSURL objektumot a vágólapra:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Vagy Swiftben:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Ha a Marked Mac App Store-verzióját használja, és a baseURL nem érhető el sandboxon keresztül, akkor engedélyt kér az URL első betöltésekor az előnézetbe.

### A forrásalkalmazás deklarálása [declaring-the-source-application]

Az alkalmazások egy `source` metaadatsor hozzáadásával is megjelölhetik magukat az előnézeti tartalom forrásaként. Ez általában egy HTML megjegyzésben történik, hogy lehetővé tegye a GFM és a MultiMarkdown processzorokkal való kompatibilitást. Egyszerűen adja meg az alkalmazás nevét vagy csomagazonosítóját:

```html
<!--
source: Bear.app
-->
```

### A Streaming előnézetének programozott megnyitása [opening-the-streaming-preview-programatically]

Alkalmazása a `x-marked-3://stream/` URL-kezelő módszerrel programozottan is megnyithatja a Streaming előnézetet. Ez a módszer egy `x-success` paramétert is elfogad, amelyben átadhatja egy alkalmazás csomagazonosítóját, amely a befejezés után aktiválódik.