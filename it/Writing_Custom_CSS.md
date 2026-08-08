<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked ha un editor di stile integrato e può applicare file CSS personalizzati.

Puoi utilizzare l'editor per creare bellissimi stili o, se conosci abbastanza CSS per essere pericoloso, puoi far sembrare Marked come preferisci.

## Per iniziare [getting-started]

C'è una galleria di stili personalizzati creati dallo sviluppatore e dagli utenti su [markedapp.com/styles](https://markedapp.com/styles/). La galleria ti consente di visualizzare in anteprima e installare gli stili direttamente in Marked. Qualsiasi stile installato può essere visualizzato nel Finder per esame e modifica. La galleria può essere aperta utilizzando un visualizzatore interno con {% appmenu Style, Generate a Custom Style %} o facendo clic sull'icona della matita (modifica) accanto a qualsiasi stile modificabile in Gestione stili. Se desideri modificare uno stile integrato, dovrai prima duplicarlo nel gestore.

C'è anche un [repository per stili personalizzati](https://github.com/ttscoff/MarkedCustomStyles) su GitHub con esempi. Sentiti libero di navigare, utilizzare e contribuire lì. Se distribuisci il tuo tema in base a uno dei temi di base, sentiti libero di aggiungerti ai crediti come collaboratore.

Con la capacità di Marked di utilizzare file CSS personalizzati, il cielo è il limite quando si personalizza l'anteprima. Tutte le opzioni CSS3 che funzionano in Safari funzioneranno in Marked. Con i file Markdown predefiniti in Marked ci sono solo pochi elementi HTML che devi gestire; tutto il contenuto è in un div con l'id "wrapper", tutto il resto è determinato dal markup del documento.

Se stai progettando per uso personale, non ci sono regole. Attiva il monitoraggio CSS con la casella di controllo sotto il selettore CSS personalizzato e quando modifichi e salvi il tuo CSS personalizzato, l'anteprima verrà aggiornata.

**Un [tema scheletro è disponibile](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) per iniziare.**

Se hai intenzione di condividere la tua creazione CSS, ci sono alcuni punti che devi trattare. Innanzitutto, ci sono alcune classi del corpo a cui è necessario applicare degli stili:

## Classi corporee [body-classes]

I seguenti stili devono essere inclusi in qualsiasi CSS contrassegnato per essere condiviso. Le classi del corpo consentono di individuare e modificare qualsiasi selettore in diverse opzioni di preferenza.

### Invertito [inverted]

 Quando l'utente seleziona {% appmenu Preview, Dark Mode %}, al tag body viene aggiunta la classe "invertito". Puoi usarlo per indirizzare gli stili ad alto contrasto, chiaro su scuro.

Desideri che gli stili invertiti vengano applicati solo all'anteprima, non alla stampa, quindi utilizza una query multimediale (@schermata multimediale) per limitarla. Il codice seguente è abbastanza universale e nella maggior parte dei casi puoi semplicemente inserirlo nel tuo foglio di stile per compatibilità, ma sentiti libero di modificarlo.

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

### Poesia [poetry]

L'utente può scegliere se il testo con rientro di tabulazione è poesia o codice. L'unica differenza è che i blocchi pre/codice hanno uno stile più, ehm, poetico se viene scelta la modalità poesia. La classe "poesia" viene applicata al tag body.

Diventa creativo quanto vuoi con la formattazione, ma ecco uno snippet di base:

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

## Casi particolari [special-cases]

È necessario considerare anche le tabelle, le figure/didascalie e il caso speciale di `a.footnote` e `div.footnotes>a`. Non ci sono regole fisse su come gestirli, ma dai un'occhiata agli stili predefiniti per avere un'idea di quali regole CSS ha bisogno Marked.

Lo stile standard della tabella in tutti gli stili predefiniti utilizza la trasparenza sulle righe alternate per fonderla delicatamente con qualsiasi sfondo. Puoi copiare quegli stili o seguire il tuo percorso, assicurati solo di averli stilizzati! Lo stesso per figura e didascalia; aggiungi un'immagine a un documento con testo alternativo per vedere come apparirà il markup e avere uno stile appropriato.

Le note a piè di pagina incluse in un documento restituiranno un collegamento all'interno del contenuto (a.footnote) e un div alla fine con il testo di riferimento (div.footnotes). Ancora una volta, vedere gli stili predefiniti come riferimento. Per evitare di modificare l'altezza della riga sulle righe contenenti un numero di riferimento della nota a piè di pagina, assicurati di includere qualcosa come:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Per mantenere la freccia di ritorno sulla stessa riga, includere:

```css
.footnotes p {display:inline}
```

È anche una buona idea includere una regola generale per tutte le immagini per mantenerle entro la larghezza della pagina. Qualcosa come:

```css
#wrapper img { max-width: 100% }
```

Se il tuo tema ha un'imbottitura aggiuntiva o una larghezza fissa, modifica la larghezza massima per adattarla.

## Stili di stampa [printstyles]

Assicurati di includere stili di stampa che rimuovano colori di sfondo, scorrimento fisso e l'interfaccia solo per l'anteprima. Marked offre due modi per indirizzare l'output di stampa e PDF.

### `@media print` [media-print]

Le regole CSS di stampa standard si applicano quando si stampa da Marked o quando l'esportazione PDF usa i media di stampa:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### La classe `.mkprinting` [the-mkprinting-class]

Quando Marked prepara un documento per l'**esportazione PDF** o l'**anteprima Stampa/PDF** ({% kbd cmd P %}), aggiunge la classe `mkprinting` al tag `<body>` (insieme a classi di esportazione come `bandw`, `breakAfterTOC` e la classe `mkstyle--*` del tuo stile). I temi integrati di Marked usano questa classe per la maggior parte delle regole specifiche di stampa, invece di affidarsi solo a `@media print`.

L'esportazione PDF spesso carica il WebView di rendering nascosto con media **screen** (soprattutto per stili personalizzati e documenti [Fountain](Fountain_for_Screenwriters.html)), quindi i blocchi `@media print` nel tuo foglio di stile **potrebbero non** applicarsi all'output PDF. Le regole con prefisso `.mkprinting` si applicano sempre durante l'esportazione perché sono selettori di classe normali, non media query.

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

Per stili che devono funzionare **sia** nella stampa dal browser sia nell'esportazione PDF di Marked, duplica le regole critiche o combina i selettori:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

Quando esegui il debug del CSS di stampa personalizzato, apri l'anteprima Stampa/PDF o esporta in PDF, poi usa il [Web Inspector di Safari](#webkitinspector) per ispezionare il documento: il `<body>` avrà la classe `mkprinting` mentre il layout di stampa è attivo.

Nascondere i link in stampa è gestito fuori dal tema principale, così gli utenti possono scegliere di nascondere evidenziazioni e sottolineature dei link nella stampa. Finché hai uno stile base per il testo, non devi preoccupartene.

Quindi diamoci da fare. Converti il tema del tuo blog, crea uno stile di stampa eccellente per i PDF o l'anteprima perfetta per il tuo modo di scrivere. Se crei qualcosa di fantastico, [condividilo con la community](https://markedapp.com/styleshare/).

## Impostazioni CSS aggiuntive [additional-css-settings]

In {% prefspane Style %} puoi modificare CSS aggiuntivi. Questi stili vengono aggiunti a qualsiasi tema caricato e possono servire per modifiche universali a tutti i temi.

Usando [alta specificità](#overridingspecificity), query `@media` per stampa e schermo e selettori `.mkprinting` per l'esportazione PDF, puoi controllare quasi ogni aspetto dello stile con un po' di conoscenza CSS.

## Ispettore WebKit [webkitinspector]

L'Ispettore Web di Safari è il modo più semplice per vedere esattamente cosa sta generando HTML e CSS Marked e per sperimentare dal vivo gli stili personalizzati.

### Abilitazione del menu Sviluppo in Safari [enabling-the-develop-menu-in-safari]

1. Apri Safari e scegli {% appmenu Safari, Settings… %}.
2. Seleziona la scheda **Avanzate**.
3. Abilita **Mostra funzionalità per sviluppatori web** (o **Mostra menu Sviluppo nella barra dei menu** nelle versioni precedenti di macOS).

Una volta abilitato, nella barra dei menu di Safari verrà visualizzato il menu **Sviluppo**.

![Menu Sviluppo Safari che mostra i documenti contrassegnati][develop-menu]

### Ispezione di un documento contrassegnato [inspecting-a-marked-document]

1. Con una finestra di anteprima aperta in Contrassegnato, passa a Safari.
2. Dalla barra dei menu, scegli **Sviluppo → _\<nome del tuo Mac\>_ → Contrassegnato → _\<titolo documento\>_**.
3. Safari aprirà una finestra di ispezione Web allegata all'anteprima contrassegnata selezionata.

Da qui puoi:

- Utilizza la scheda **Elementi** per ispezionare il DOM all'interno del div `#wrapper` e vedere quali regole CSS vengono applicate.
- Passa il mouse sugli elementi nell'albero del DOM per evidenziarli nella finestra Contrassegnata.
- Utilizza la barra laterale **Stili** per modificare le regole in tempo reale, quindi copia nuovamente gli snippet funzionanti in uno stile personalizzato o in un **CSS aggiuntivo**.
    - Dopo aver modificato i CSS nella scheda Elementi, puoi ottenere un riepilogo delle tue modifiche selezionando la scheda Modifiche

	![Modifiche][css-changes]
- Utilizza la scheda **Console** per eseguire JavaScript rispetto all'anteprima dal vivo. L'intera [API JavaScript contrassegnata](https://markedapp.com/help/jsapi/) è disponibile in questa console.
- Esplora altre schede come **Rete** durante il debug delle risorse caricate dal tuo documento.

![Ispezione di un'anteprima contrassegnata con Safari Web Inspector][inspecting]

## Condivisione di CSS personalizzati [sharing-custom-css]

Utilizza {% appmenu Style, Share a Custom Style %} per aprire l'app di condivisione nel tuo browser web. Trascina il tuo CSS nella zona di rilascio (o fai clic per selezionarlo dal disco) e carica il CSS per il tuo stile personalizzato.

Gli stili condivisi devono essere approvati dallo sviluppatore prima di essere visualizzati nella galleria, quindi non vedrai risultati immediati.

## Altri suggerimenti [other-tips]

### Specificità prioritaria [overridingspecificity]

All'interno dell'anteprima Contrassegnato, viene aggiunta una classe del corpo basata sul nome file dello stile corrente. Se l'anteprima è impostata su "Svizzero", ci sarà una classe sul tag `<body>` chiamata `mkstyle--swiss`. Se il tuo CSS personalizzato si chiama MyCustom.css, la classe del corpo sarà `mkstyle--mycustom`. Puoi usarlo prima delle regole definite negli stili di base per sovrascriverle. Per ottenere la specificità assoluta in una regola, utilizza anche l'ID #wrapper dal div del contenitore:

	.mkstyle--mycustom #wrapper p+p { ... }

### Stile del sommario [table-of-contents-styling]

Se utilizzi il token `<!--toc-->` per [inserire un sommario](Special_Syntax.html#tableofcontents), puoi sovrascrivere le impostazioni per gli indicatori di livello del sommario in uno stile personalizzato utilizzando il "#wrapper" per aumentare la specificità:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Ciò farebbe sì che tutti gli elementi dell'elenco nel sommario utilizzino un punto elenco quadrato anziché quello definito in Impostazioni quando lo stile personalizzato è attivo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
