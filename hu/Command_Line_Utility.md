<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A `mk` parancssori eszköz egyszerű hozzáférést biztosít a Marked szolgáltatásaihoz a terminálról, lehetővé téve a munkafolyamatok automatizálását, valamint a shell szkriptekkel és más parancssori eszközökkel való integrációt.

## Telepítés [installation]

A `mk` telepítésének javasolt módja a Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Ha nem használja a Homebrew-t, töltse le és telepítse az aláírt csomagot:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

A `mk.pkg` letöltése után kattintson rá duplán, és kövesse a telepítő utasításait.

## Alapvető használat [basic-usage]

### Fájlok megnyitása [opening-files]

Nyisson meg egy markdown fájlt a Marked alkalmazásban a parancssorból:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Tartalom streamelése az STDIN-ről [streaming-content-from-stdin]

Tartalom streamelése közvetlenül a Marked streaming előnézetébe:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

Megnyílik a Streaming Előnézet ablak, és valós időben jeleníti meg a tartalmat, ahogyan azt más parancsokból továbbítják.

## Parancs referencia [command-reference]

### Fájlműveletek [file-operations]

**`mk [file]`** — Nyissa meg a Markdown fájlt a Megjelölt területen

**`mk [file] --raise`** — Nyissa meg a fájlt, és emelje az ablakot a többi fölé

### STDIN és adatfolyam [stdin-and-streaming]

**`mk`** vagy **`mk -`** – Olvasson az STDIN-ből, és nyissa meg a Streaming előnézetét

**`mk --stream`** — Nyissa meg a Streaming előnézeti ablakot az STDIN olvasása nélkül

### Előnézet kezelés [preview-management]

**`mk --refresh`** — A legelső előnézeti ablak frissítése

**`mk --refresh all`** — Az összes megnyitott előnézeti ablak frissítése

**`mk --refresh file.md`** — Egy adott fájl előnézetének frissítése (ha nyitva van)

### Beállítások [preferences]

**`mk --pref`** — Megjelölt beállítások megnyitása (Általános oldal)

**`mk --pref Advanced`** — Nyissa meg a beállításokat egy adott oldalhoz

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Felhasználói beállítások megadása (több pár is megengedett)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Stíluskezelés [style-management]

**`mk --style NAME`** — Előnézeti stílus beállítása a nyitott ablakokhoz

**`mk --add-style FILE`** — Adjon hozzá egy CSS-fájlt egyéni stílusként a Megjelölthez

```bash
mk --add-style ~/Styles/custom.css
```

### JavaScript végrehajtás [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** — JavaScript futtatása a legelső ablakban

**`mk --dojs "SCRIPT" all`** — Futtassa a JavaScriptet az összes ablakban

**`mk --dojs "SCRIPT" file.md`** — JavaScript futtatása adott fájl(ok)ban

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Tartalom kinyerése és importálása [content-extraction-and-import]

**`mk --extract URL`** – Tartalom kinyerése az URL-ből, és megnyitása a Megjelöltben

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** – URL importálása ablak megnyitása (opcionálisan URL-lel)

**`mk --stylestealer [URL]`** — Open Style Stealer HUD (opcionálisan URL-lel)

### Segédprogramok parancsai [utility-commands]

**`mk --paste`** — Új dokumentum létrehozása a vágólapról

**`mk --preview TEXT`** — Szöveg előnézete közvetlenül egy új dokumentumban

**`mk --dingus`** — Nyissa meg a Markdown Dingust a processzorok teszteléséhez

**`mk --help`** vagy **`mk -h`** — Használati információk megjelenítése

**`mk --version`** vagy **`mk -v`** — Verzióinformációk megjelenítése

## Példák [examples]

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Integráció [integration]

### Shell álnevek [shell-aliases]

Adja hozzá a `~/.zshrc` vagy `~/.bash_profile` számhoz:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Szkriptek [scripts]

A `mk` használata shell szkriptekben az automatizáláshoz:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Munkafolyamatok [workflows]

Kombináld más eszközökkel:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## Nyílt forráskód [open-source]

A `mk` parancssori eszköz nyílt forráskódú, és elérhető a GitHubon:

**https://github.com/ttscoff/mk**

A következőket teheti:
- Tekintse meg a forráskódot
- Hozzájáruljon a fejlesztésekhez
- Problémák bejelentése
- Ha szükséges, készítsen forrásból

Az eszköz Swiftben íródott, és Xcode segítségével fordítható. Lásd: [README](https://github.com/ttscoff/mk) az összeállítási utasításokért.

## Verzió [version]

Ellenőrizze a telepített `mk` verziót a következővel:

```bash
mk --version
```

## Kapcsolódó szolgáltatások [related-features]

- A Marked URL-sémájával kapcsolatos további információkért lásd: [URL-kezelő](URL_Handler).
- A streaming előnézeti funkcióval kapcsolatos részletekért lásd: [Streaming Preview](Streaming_Preview)
- Automatizálási példákért lásd: [Workflow Integration](Workflow_Integration).