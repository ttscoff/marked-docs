<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## AppleScript

A Marked tartalmaz egy teljes [AppleScript-szótárt](AppleScript_Support.html) a fájlok megnyitásához, az előnézet vezérléséhez (újratöltés, görgetés, kiemelések, automatikus görgetés, gyorsolvasás), statisztikák olvasásához, processzorok beállításához, HTML vagy RTF másolásához, előnézeti stílusok megváltoztatásához, valamint Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RMLTF és TextBundle formátumba exportáláshoz. **Az előnézeti címsorok / tartalomjegyzék** az AppleScript segítségével [folyamatban lévő munkaként dokumentálva](AppleScript_Support.html#table-of-contents-work-in-progress), és még nem megbízható.

Megcélozhatja az alkalmazást, egy adott ablakot vagy dokumentumot. Az alkalmazásparancsok közé tartozik a **adatfolyam előnézetének megnyitása**, **előnézeti vágólap** és **összes bezárása**. A dokumentum parancsok közé tartozik a **statisztika lekérése** és a **profil nyomtatása**. Az exportálási parancsok elfogadnak egy opcionális export **profilt** vagy egy **`with`** rekordot az olyan opciókhoz, mint az előnézeti **stílus**, **oldalméret** és **margók**. Például:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Lásd: [AppleScript támogatás](AppleScript_Support.html) a parancsok listájáért, a margógyorsításért, a sandbox megjegyzésekért és a hibakeresési tippekért.

Az AppleScript integráció azt is lehetővé teszi, hogy az olyan alkalmazások, mint a Tags.app, közvetlenül a Markeden belül működjenek.

{% note %}
## Parancsikonok

A megjelölt natív [Parancsikon-műveletek](Shortcuts_Integration.html) macOS 13 vagy újabb rendszeren. Használja a **Fájl megnyitása és exportálása** a Finder-ből PDF-be munkafolyamatokhoz, a **Dokumentum exportálása** a Megjelöltben már megnyitott elemekhez, vagy az **Előnézeti stílus beállítása** a témák módosításához az exportálás előtt. Az exportálási műveletek elfogadják a **profilokat**, az előnézeti **stílusokat** és az olyan beállításokat, mint az **oldalméret**, **margók** és **betűméret** (ugyanaz a szemantika, mint az AppleScript `with` rekordoknál).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## URL-kezelő

A [Megjelölt URL-kezelő][urlhandler] kiterjedt integrációt tesz lehetővé egyszerűen az URL-ek meghívásával, akár AppleScriptből, akár egy héjszkriptben található alap `open` paranccsal.

## Megjelölt bónuszcsomag

A Marked Bonus Pack szkriptek, parancsok és szolgáltatások gyűjteménye. Néhányan több szerkesztővel dolgoznak, vannak, amelyek bizonyos szerkesztőkre vonatkoznak. A Szolgáltatások általában minden olyan szerkesztővel működnek, amely rendelkezik a szükséges képességekkel. A többiek mappákba vannak rendezve az alkalmazás alapján, amellyel dolgoznak.

Letöltheti a bónuszcsomagot, és utasításokat talál a telepítéséhez és használatához ebben a [tudásbázis-cikkben](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html