<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

## Callout

## Orso/Ossidiana ##

Marked supporta i callout con la sintassi utilizzata da Obsidian e Bear, ovvero una citazione di blocco appositamente formattata:

	> [!NOTE] Titolo della nota
	> Testo aggiuntivo

La "NOTA" in `[!NOTE]` non fa distinzione tra maiuscole e minuscole. Può essere uno qualsiasi di:

- NOTA
- ASTRATTO, SOMMARIO, TLDR
-INFORMAZIONI
- DA FARE
- SUGGERIMENTO, SUGGERIMENTO, IMPORTANTE
- SUCCESSO, VERIFICA, FATTO
- DOMANDE, AIUTO, FAQ
- ATTENZIONE, ATTENZIONE, ATTENZIONE
- FALLIMENTO, FALLIMENTO, MANCANTE
- PERICOLO, ERRORE
- BUG
- ESEMPIO
- CITARE, CITARE

Questi creeranno blocchi appositamente formattati.

Puoi utilizzare `+` o `-` per rendere il callout comprimibile. Un segno più (`+`) indica che il callout è comprimibile ma per impostazione predefinita si apre. Un segno meno (`-`) indica che il callout è comprimibile ma per impostazione predefinita è chiuso.

  ![Callout in Contrassegnato][callout]

[callouts]: images/callouts-800.jpg @2x width=800

### Parco giochi Xcode ###

Durante l'anteprima dei file Xcode Playground, Marked supporta la sintassi nativa del callout Xcode Playground:

	- Attenzione: titolo facoltativo
	Il contenuto del callout va qui.

Il tipo di callout (ad esempio "Attenzione") non fa distinzione tra maiuscole e minuscole e può essere uno dei seguenti tipi di callout Xcode Playground:

- **Attenzione** - Stile callout informativo
- **Autore** - Callout metadati
- **Autori** - Callout metadati
- **Bug** - Richiamo di errore/pericolo
- **Complessità** - Callout in stile nota
- **Copyright** - Callout metadati
- **Callout personalizzato** - Callout in stile esempio
- **Data** - Callout metadati
- **Esempio** - Callout di esempio
- **Esperimento** - Callout in stile suggerimento
- **Importante** - Callout in stile informazioni
- **Invariante** - Callout in stile nota
- **Nota** - Didascalia della nota
- **Precondizione** - Callout in stile nota
- **Postcondizione** - Callout in stile nota
- **Nota** - Callout in stile nota
- **Richiede** - Callout in stile nota
- **Vedi anche** - Callout in stile informazioni
- **Dal** - Callout metadati
- **Versione** - Callout metadati
- **Avviso** - Richiamo di avviso

Il titolo facoltativo dopo i due punti verrà utilizzato come titolo del callout. Se non viene fornito alcun titolo, come titolo verrà utilizzato il nome del tipo di callout.

Il contenuto del callout segue immediatamente la riga successiva (non è richiesta alcuna riga vuota). Il contenuto continua fino a una riga vuota, al callout successivo, a un blocco di codice recintato o alla fine del documento.

Esempio:

````ribasso
- Importante: nota sulle prestazioni
Questo algoritmo ha complessità O(n log n).

- Esempio: ordinamento rapido
Ecco come implementarlo:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

Puoi anche omettere completamente il titolo:

	- Avvertimento
	Questo è un avviso senza titolo personalizzato.

Questi callout vengono automaticamente convertiti nel formato callout di Marked e stilizzati in modo appropriato. Il tipo di callout originale viene conservato nell'attributo `data-callout`, consentendo uno stile CSS personalizzato, se lo si desidera.

> Questa funzione funziona solo durante l'anteprima dei file Xcode Playground (`.playground`). I normali file di markdown non elaboreranno questa sintassi.


## Sommario

Puoi specificare dove nel documento deve apparire il sommario utilizzando `<!--TOC-->`. Se impostata, sovrascrive l'opzione nelle Preferenze e verrà sempre visualizzata nella finestra di anteprima, nonché durante il salvataggio e la stampa. Il sommario verrà visualizzato solo una volta, anche se nel contenuto sono presenti più specificatori `<!--TOC-->`.

Se aggiungi `max#` al tag sopra (dove # è una cifra da 1 a 5) controllerà la profondità del sommario visualizzato. Ad esempio `<!--TOC max2-->` mostrerà solo le intestazioni di primo e secondo livello nell'elenco. Puoi anche specificare un livello minimo di intestazione con `<!--TOC min2-->`. I valori massimi e minimi si basano sui livelli effettivi dei titoli, non sui livelli di nidificazione. Massimo e minimo possono essere utilizzati insieme.

Marked riconosce anche lo stile MultiMarkdown `{{TOC}}` e lo stile Pandoc `{{TOC:2-6}}`, dove `2-6` è l'intervallo dei livelli minimo e massimo delle intestazioni da includere.

Per impostazione predefinita, il sommario verrà stampato sulla prima pagina del documento se "Stampa sommario" è abilitato sotto {% prefspane Export %}. Se nel documento esiste un contrassegno, verrà invece posizionato in quel punto.

I> È possibile specificare il tipo di numerazione o caratteri di ciascun livello di una gerarchia di sommario nidificata in {% prefspane Export %}.

## La pagina si interrompe

Puoi forzare un'interruzione di pagina per l'output di stampa/PDF utilizzando la sintassi:

```html
<!--BREAK-->
```

Metti il token su una riga da sola e genererà markup che forzerà una nuova pagina in quel punto. Marked comprende anche il formato Leanpub:

	{::interruzione di pagina /}

## Lo scorrimento automatico fa una pausa [pausa]

Marked può funzionare come teleprompter utilizzando la funzione [Autoscroll](Autoscroll.html) (dovresti aggiungere lo [stile teleprompter](https://markedapp.com/styles/preview?style=teleprompter)). In questo caso può essere utile includere delle pause nel documento. Fallo usando:

```html
<!--PAUSE:X-->
```

Dove `X` è il numero di secondi per i quali Marked dovrebbe fare una pausa. Quindi inserendo `<!--PAUSE:15-->` ti darebbe una pausa di 15 secondi quando quel punto del documento raggiunge il centro dello schermo.

## Il file include

Il contenuto di file aggiuntivi può essere inserito utilizzando la sintassi:

	<<[nome cartella/file]

Il percorso del file può essere relativo al file indice o assoluto. Le inclusioni possono essere nidificate; puoi usare questa stessa sintassi all'interno di un file incluso. Se utilizzi percorsi relativi, le inclusioni nei file nidificati dovrebbero essere relative a quel file. ***Tuttavia,*** MultiMarkdown elaborerà tutto in base alla posizione del primo file aperto, quindi tutti i percorsi delle immagini o altri incorporamenti dovrebbero essere relativi al primo file principale, anche quando esistono nei documenti secondari.

I metadati MultiMarkdown e le intestazioni YAML vengono automaticamente rimossi dai file inclusi prima del rendering. Ciò impedirà la visualizzazione delle intestazioni nel documento, ma tieni presente che i metadati come il "livello dell'intestazione di base" verranno ignorati nei documenti inclusi.

T> Tieni presente che quando visualizzi documenti con file inclusi, puoi digitare "I" (shift-i) per vedere quale file incluso si trova nell'area visibile.

Per ulteriori informazioni, vedere ["Documenti con più file"][ext].

[ext]: Multi-File_Documents.html

## Incluso il codice

Contrassegnato può includere file esterni come codice utilizzando una sintassi simile a file include sopra:

	<<(nome cartella/file)

Notare le parentesi invece delle parentesi quadre. Per compatibilità con la sintassi Leanpub, Marked riconoscerà anche una serie precedente di parentesi quadre contenenti un titolo, ma al momento non viene fatto nulla in Marked:

	<<[Titolo codice](nome cartella/file)

Il contenuto del file specificato verrà inserito all'interno di un blocco pre>codice nel documento e sarà disponibile per l'evidenziazione automatica della sintassi, se abilitata. I blocchi di codice non possono essere annidati e non verranno elaborati con MultiMarkdown. I processori personalizzati verranno comunque eseguiti sul blocco pre>codice creato.

## Incluso testo o HTML non elaborato

E> **Nota:** questa funzionalità è riservata agli utenti avanzati.

Se desideri includere HTML non elaborato o altro testo che non deve essere elaborato da MultiMarkdown (o dal tuo processore personalizzato), puoi utilizzare parentesi graffe (`{}`) per includere un file *dopo* aver elaborato il resto del documento:

	<<{cartella/file_raw.html}

All'interno di questi file non verrà riconosciuta alcuna sintassi di inclusione (nessun annidamento) e il contenuto **grezzo** del file verrà inserito nell'output HTML finale. Questo è ottimo per inserire HTML senza impantanare l'elaboratore di testo o convertire o eseguire l'escape di elementi quando non vuoi che lo siano, ma fai attenzione poiché esistono poche garanzie per garantire che la formattazione del documento venga preservata attorno a ciò che inserisci.