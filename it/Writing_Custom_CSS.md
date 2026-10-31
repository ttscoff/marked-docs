# <%= @title %>

Marked include un editor di stili integrato e può applicare fogli di stile CSS personalizzati.

Puoi usare l'editor per creare stili bellissimi, oppure, se conosci il CSS quel tanto che basta per essere pericoloso, puoi far apparire Marked esattamente come vuoi.

## Getting started [getting-started]

Esiste una galleria di Stili personalizzati creati dallo sviluppatore e dagli utenti su [markedapp.com/styles](https://markedapp.com/styles/). La galleria ti permette di visualizzare in anteprima e installare gli Stili direttamente in Marked. Ogni Stile installato può essere rivelato nel Finder per essere esaminato e modificato. La galleria può essere aperta usando un visualizzatore interno con {% appmenu Style, Generate a Custom Style %}, oppure facendo clic sull'icona a matita (modifica) accanto a qualsiasi stile modificabile nel Gestore Stili. Se vuoi modificare uno stile integrato, dovrai prima duplicarlo nel gestore.

Esiste anche un [repository per gli Stili personalizzati](https://github.com/ttscoff/MarkedCustomStyles) su GitHub con alcuni esempi. Sentiti libero di sfogliarlo, usarlo e contribuire. Se distribuisci un tuo tema basato su uno dei temi base, sentiti libero di aggiungerti ai crediti come contributore.

Grazie alla capacità di Marked di usare fogli di stile CSS personalizzati, non ci sono limiti alla personalizzazione dell'Anteprima. Tutte le opzioni CSS3 che funzionano in Safari funzionano anche in Marked. Con i file Markdown predefiniti in Marked ci sono solo pochi elementi HTML da gestire; tutto il contenuto si trova in un div con id "wrapper", mentre tutto il resto è determinato dal markup del tuo documento.

Se stai progettando uno stile per uso personale, non ci sono regole. Attiva il monitoraggio del CSS con la casella di controllo sotto il selettore del CSS personalizzato e, quando modifichi e salvi il tuo CSS personalizzato, l'anteprima si aggiornerà automaticamente.

**È disponibile un [tema scheletro](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) per iniziare.**

Se hai intenzione di condividere la tua creazione CSS, ci sono alcuni punti che devi coprire. Innanzitutto, ci sono alcune classi del body a cui devono essere applicati degli stili:

## Body classes [body-classes]

I seguenti stili devono essere inclusi in qualsiasi CSS di Marked destinato alla condivisione. Le classi del body ti permettono di individuare e modificare qualsiasi selettore in base alle diverse opzioni di preferenza.

### Inverted [inverted]

 Quando l'utente seleziona {% appmenu Preview, Dark Mode %}, al tag body viene aggiunta una classe "inverted". Puoi usarla per definire gli stili ad alto contrasto, chiari su sfondo scuro.

Vuoi che gli stili invertiti si applichino solo all'anteprima e non alla stampa, quindi usa una media query (@media screen) per limitarne l'ambito. Il codice qui sotto è abbastanza generico e, nella maggior parte dei casi, puoi semplicemente inserirlo nel tuo foglio di stile per garantire la compatibilità, ma sentiti libero di modificarlo.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poetry [poetry]

L'utente può scegliere se il testo indentato con tabulazioni è poesia o codice. L'unica differenza è che i blocchi pre/code vengono stilizzati in modo più... poetico, se viene scelta la modalità poesia. La classe "poetry" viene applicata al tag body.

Sbizzarrisciti pure con la formattazione, ma ecco uno snippet di base:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Special cases [special-cases]

Vanno considerati anche le tabelle, Figure/Figcaption, e il caso speciale di `a.footnote` e `div.footnotes>a`. Non ci sono regole fisse su come gestirli, ma dai un'occhiata agli stili predefiniti per farti un'idea di quali regole CSS servono a Marked.

Lo stile standard delle tabelle in tutti gli stili predefiniti usa la trasparenza sulle righe alternate per farle fondere delicatamente con qualsiasi sfondo. Puoi copiare questi stili oppure seguire la tua strada, l'importante è che tu li abbia stilizzati! Lo stesso vale per figure e figcaption; aggiungi a un documento un'immagine con testo alternativo per vedere come verrà generato il markup e stilizzalo di conseguenza.

Le note a piè di pagina incluse in un documento generano un link all'interno del contenuto (a.footnote) e un div alla fine con il testo di riferimento (div.footnotes). Anche in questo caso, fai riferimento agli stili predefiniti. Per evitare di modificare l'altezza della riga nelle righe che contengono un numero di riferimento della nota, assicurati di includere qualcosa come:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Per mantenere la freccia di ritorno sulla stessa riga, includi:

```css
.footnotes p {display:inline}
```

È anche una buona idea includere una regola generale per tutte le immagini, in modo che restino entro la larghezza della pagina. Qualcosa come:

```css
#wrapper img { max-width: 100% }
```

Se il tuo tema ha un padding aggiuntivo o una larghezza fissa, modifica il max-width di conseguenza.

## Print styles [printstyles]

Assicurati di includere stili di stampa che rimuovano i colori di sfondo, lo scrolling fisso e gli elementi dell'interfaccia validi solo per l'anteprima. Marked ti offre due modi per definire l'output di stampa e PDF.

### `@media print` [media-print]

Le regole CSS di stampa standard si applicano quando si stampa da Marked o quando l'esportazione in PDF usa i media di stampa:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### The `.mkprinting` class [the-mkprinting-class]

Quando Marked prepara un documento per l'**esportazione in PDF** o per l'**Anteprima di Stampa/PDF** ({% kbd cmd P %}), aggiunge la classe `mkprinting` al tag `<body>` (insieme alle classi di esportazione come `bandw`, `breakAfterTOC` e alla classe `mkstyle--*` del tuo stile). I temi integrati di Marked usano questa classe per la maggior parte delle regole specifiche di stampa, invece di affidarsi solo a `@media print`.

L'esportazione in PDF spesso carica la WebView di rendering nascosta con i media **screen** (specialmente per gli stili personalizzati e i documenti [Fountain](Fountain_for_Screenwriters.html)), quindi i blocchi `@media print` nel tuo foglio di stile potrebbero **non** applicarsi all'output PDF. Le regole con il prefisso `.mkprinting` si applicano sempre durante l'esportazione perché sono normali selettori di classe, non media query.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Per gli stili che devono funzionare **sia** nella stampa da browser sia nell'esportazione PDF di Marked, duplica le regole fondamentali o combina i selettori:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Stile personalizzato vs CSS aggiuntivo.** In un foglio di stile di Stile personalizzato, scrivi `.mkprinting #wrapper …` come mostrato sopra. Nel campo **CSS aggiuntivo**, Marked riscrive i selettori prima dell'iniezione --- usa invece la forma qualificata con il body:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Consulta [Impostazioni CSS aggiuntivo](#additional-css-settings) per capire come funziona la riscrittura e perché `.mkprinting #wrapper …` da solo non trova corrispondenza in quel contesto.

Per eseguire il debug del CSS di stampa personalizzato, apri l'Anteprima di Stampa/PDF oppure esporta in PDF, quindi usa [Web Inspector di Safari](#webkitinspector) per ispezionare il documento --- il `<body>` avrà la classe `mkprinting` mentre il layout di stampa è attivo.

Il nascondimento dei link in stampa viene gestito al di fuori del tema principale, permettendo agli utenti di scegliere se nascondere l'evidenziazione e la sottolineatura dei link nella stampa. Finché hai impostato uno stile di base per il testo, non devi preoccupartene.

Quindi, mettiti all'opera. Converti il tema del tuo blog, crea uno stile di stampa formidabile per i documenti PDF, oppure realizza l'anteprima perfetta per il tipo di scrittura che fai. Se crei qualcosa di fantastico, [condividilo con la community](https://markedapp.com/styleshare/).

## Additional CSS Settings [additional-css-settings]

In {% prefspane Style %} puoi modificare il **CSS aggiuntivo**. Queste regole vengono **aggiunte in coda a qualsiasi tema sia caricato**. Si tratta di una sovrapposizione parziale e deliberata, non di un tema completo. Se incolli un foglio di stile completo in questo campo --- oppure importi quello stesso foglio parziale tramite il [Gestore Stili](Custom_Styles.html) come se fosse un tema --- tutto ciò che il foglio non copre resterà privo di stile.

### Selector rewriting [additional-css-selector-rewriting]

Marked riscrive i selettori del CSS aggiuntivo prima di iniettarli (come `body.mk-has-additional-css …`) in modo che le regole restino circoscritte all'anteprima:

- Una parte di selettore che inizia già con `body` o `#wrapper` riceve il prefisso `body.mk-has-additional-css`, con le classi del body unite anziché annidate.
- Qualsiasi altra parte di selettore viene circoscritta sotto `body.mk-has-additional-css #wrapper …`.
- Le classi del body iniziali che Marked imposta su `<body>` --- incluse `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` e `.mkstyle--*` --- vengono trattate come `body` e unite al selettore del body invece di essere annidate sotto `#wrapper`.

| Inserito nel CSS aggiuntivo | Risultato |
| :-- | :-- |
| `#wrapper h2` | Corrisponde (circoscritto correttamente) |
| `body.mkprinting #wrapper p` | Corrisponde durante la stampa/PDF |
| `.mkprinting #wrapper p` | **Non** corrisponde (richiederebbe un `#wrapper` annidato) |
| `:root { --x: 1; }` | **Non** corrisponde (preferisci `body` o `#wrapper` per le proprietà personalizzate) |

Per le regole di stampa in questo campo, preferisci `body.mkprinting #wrapper …`. La stessa intenzione visiva in un file di Stile personalizzato può mantenere la forma più breve `.mkprinting #wrapper …`.

Non c'è **alcun limite di dimensione né alcun controllo di validità CSS** sul CSS aggiuntivo. Marked memorizza e inietta ciò che inserisci; un CSS non valido semplicemente non ha alcun effetto nell'anteprima.

### HTML and other exports [additional-css-exports]

Il CSS aggiuntivo si applica nell'anteprima in tempo reale, nell'Anteprima di Stampa/PDF, nell'esportazione PDF e nell'**esportazione HTML** quando gli stili sono inclusi --- il `<body>` esportato riceve la classe `mk-has-additional-css` in modo che i selettori riscritti trovino corrispondenza. DOCX, ODT ed EPUB usano percorsi di stile propri e non applicano il CSS aggiuntivo allo stesso modo.

Usando un'[alta specificità](#overridingspecificity), le query `@media` per stampa e schermo, e i selettori `body.mkprinting` (in questo campo) o `.mkprinting` (negli Stili personalizzati), puoi controllare praticamente ogni aspetto dello stile con un po' di conoscenza del CSS.

## WebKit Inspector [webkitinspector]

Web Inspector di Safari è il modo più semplice per vedere esattamente quale HTML e CSS sta generando Marked, e per sperimentare con gli Stili personalizzati in tempo reale.

### Enabling the Develop menu in Safari [enabling-the-develop-menu-in-safari]

1. Apri Safari e scegli {% appmenu Safari, Settings… %}.
2. Seleziona la scheda **Avanzate**.
3. Attiva **Mostra funzioni per sviluppatori web** (oppure **Mostra menu Sviluppo nella barra dei menu** nelle versioni meno recenti di macOS).

Una volta attivata, nella barra dei menu di Safari comparirà un menu **Sviluppo**.

![Menu Sviluppo di Safari che mostra i documenti Marked][develop-menu]

### Inspecting a Marked document [inspecting-a-marked-document]

1. Con una finestra di anteprima aperta in Marked, passa a Safari.
2. Dalla barra dei menu, scegli **Sviluppo → _\<nome del tuo Mac\>_ → Marked → _\<titolo del documento\>_**.
3. Safari aprirà una finestra di Web Inspector collegata all'anteprima di Marked selezionata.

Da qui puoi:

- Usare la scheda **Elements** per ispezionare il DOM all'interno del div `#wrapper` e vedere quali regole CSS vengono applicate.
- Passare il mouse sugli elementi nell'albero del DOM per evidenziarli nella finestra di Marked.
- Usare la barra laterale **Styles** per modificare le regole in tempo reale, quindi copiare gli snippet funzionanti in uno Stile personalizzato o nel **CSS aggiuntivo**.
    - Dopo aver modificato il CSS nella scheda Elements, puoi ottenere un riepilogo delle modifiche selezionando la scheda Changes

	![Changes][css-changes]
- Usare la scheda **Console** per eseguire JavaScript sull'anteprima in tempo reale. In questa console è disponibile l'intera [API JavaScript di Marked](https://markedapp.com/help/jsapi/).
- Esplorare altre schede come **Network** quando esegui il debug delle risorse caricate dal tuo documento.

![Ispezione di un'anteprima di Marked con Web Inspector di Safari][inspecting]

## Sharing Custom CSS [sharing-custom-css]

Usa {% appmenu Style, Share a Custom Style %} per aprire l'app di condivisione nel tuo browser web. Trascina il tuo CSS nell'area di rilascio (oppure fai clic per selezionarlo dal disco) e carica il CSS per il tuo Stile personalizzato.

Gli stili condivisi devono essere approvati dallo sviluppatore prima di comparire nella galleria, quindi non vedrai risultati immediati.

## Other tips [other-tips]

### Overriding specificity [overridingspecificity]

All'interno dell'anteprima di Marked viene aggiunta una classe del body basata sul nome del file dello stile corrente. Se l'anteprima è impostata su "Swiss", allora ci sarà una classe sul tag `<body>` chiamata `mkstyle--swiss`. Se il tuo CSS personalizzato si chiama MyCustom.css, la classe del body sarà `mkstyle--mycustom`. Puoi usarla prima delle regole definite negli stili di base per sovrascriverle. Per ottenere una specificità assoluta in una regola, usa anche l'ID #wrapper del div contenitore:

	.mkstyle--mycustom #wrapper p+p { ... }

### Table of contents styling [table-of-contents-styling]

Se usi il token `<!--toc-->` per [inserire un sommario](Special_Syntax.html#tableofcontents), puoi sovrascrivere le impostazioni degli indicatori di livello del Sommario in uno Stile personalizzato usando "#wrapper" per aumentare la specificità:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Questo farebbe sì che tutti gli elementi dell'elenco nel Sommario usino un punto elenco quadrato invece di quello definito nelle Impostazioni, quando il tuo Stile personalizzato è attivo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
