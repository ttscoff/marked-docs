<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %> [toc]

## Il codice di licenza è già stato utilizzato [license_code_has_already_been_utilized]

Se esegui una nuova installazione di Marked 2 e ricevi l'errore "Il codice di licenza è già stato utilizzato" quando inserisci la licenza, <a href="mailto:me@brettterpstra.com">contattami</a> richiedendo una nuova licenza. **Includi l'indirizzo email con cui ti sei registrato e/o il codice di licenza attuale.**

Le prime licenze generate per Marked avevano un limite di utilizzo anziché un limite del computer, quindi 3 installazioni, anche sullo stesso computer, avrebbero utilizzato le attivazioni. Questi limiti sono stati corretti nelle licenze generate più recentemente. L'acquisto di una licenza Marked 2 ti consente di installare Marked 2 su qualsiasi macchina che possiedi, quindi non esitare a chiedere una sostituzione se riscontri problemi.

[Sommario](#toc)

## Licenze del sito e sconti didattici [site_licenses_and_educational_discounts]

Sono disponibili licenze scontate per sito/in blocco per Marked 2. Per richiedere un collegamento di acquisto, contatta <a href="mailto:me@brettterpstra.com">Brett</a> e specifica il numero di licenze che desideri acquistare.

**Sconti**

- 5-9: **10% di sconto**
- 10-19: **12% di sconto**
- 20-49: **15% di sconto**
- 50+: **20% di sconto**

È disponibile anche uno sconto educativo sia per la versione diretta che per quella del Mac App Store. Per il Mac App Store, sono abilitati gli sconti didattici standard di Apple. Per acquistare una versione diretta con uno sconto educativo, <a href="mailto:me@brettterpstra.com">contattami</a> e richiedi un coupon.

[Sommario](#toc)

## Un URL non verrà convalidato o restituirà "Sconosciuto" [a_url_wont_validate_or_returns_unknown]

La [convalida del collegamento](http://marked2app.com/help/Link_Validation.html) di Marked utilizza una richiesta HEAD di base per determinare se un collegamento è valido. Qualsiasi risultato diverso da 200 (esito positivo) restituirà un codice sconosciuto o un errore se si tratta di un codice di errore comune come 404 (non trovato) o 500 (errore del server). Gli URL dietro l'autenticazione (come gli URL degli sviluppatori Apple o qualsiasi cosa che richieda l'accesso per accedere) restituiranno un "sconosciuto", così come alcuni siti come Amazon.com in cui il server restituisce codici di risposta bizzarri. Non c'è molto che Marked possa fare al riguardo.

[Sommario](#toc)

## Autorizzazioni personalizzate del processore nella versione MAS [custom_processor_permissions_in_mas_version]

A causa delle restrizioni del sandboxing, la versione di Marked 2 del Mac App Store non è in grado di eseguire determinati tipi di strumenti binari come processori personalizzati. Se riscontri questa limitazione, puoi provare alcuni passaggi.

1. Assicurati di essere entrato nelle Preferenze **Segnato 2** (⌘,), nel riquadro **Avanzate** e di aver fatto clic su "Aggiorna autorizzazioni". Questo tenterà di concedere a Mark l'accesso all'intera unità predefinita, risolvendo i problemi con script e utilità che devono accedere a cartelle temporanee e posizioni non predefinite.
2. Prova a utilizzare uno script. Fai riferimento all'utilità che desideri eseguire (multimarkdown, kramdown, ecc.) in uno script di shell. Può essere uno script bash, Ruby, Perl o Python. Quindi imposta il processore nelle preferenze Avanzate sulla relativa shell o eseguibile e i parametri sulla posizione dello script. Ad esempio, posso creare uno script bash salvato in ~/scripts/mmd_wrapper.sh:
    
        #!/bin/bash
        gatto | /usr/local/bin/multimarkdown
    
    Quindi rendilo eseguibile (`chmod a+x ~/scripts/mmd_wrapper.sh`) e imposta le preferenze del processore personalizzato:

        Processore: /bin/bash
        Argomenti: /Users/me/scripts/mmd_wrapper.sh
3. Alcuni eseguibili (specialmente Pandoc) semplicemente non funzioneranno all'interno del sandboxing. In questo caso contattami tramite la finestra di errore che appare al momento dell'esecuzione per ricevere una licenza crossgrade alla versione diretta.

[Sommario](#toc)

## Collegamenti interni al documento nei PDF esportati [intra-document_links_in_exported_pdfs]

L'esportazione PDF di Marked attualmente utilizza le funzionalità di stampa di WebKit. Una conseguenza di ciò è che i collegamenti intra-documento (interni), compresi quelli in un sommario, non passeranno ad altri punti del documento. Questo non sembra essere qualcosa che Apple abbia intenzione di risolvere nella versione di WebKit utilizzata da Marked 2.

In alcuni casi potresti ottenere buoni risultati esportando HTML con stile incorporato e quindi utilizzando il browser Web per stampare in PDF. Non otterrai tutte le funzionalità di esportazione di Marked, ma di solito otterrai un PDF con collegamenti interni funzionanti. È un compromesso per ora.

[Sommario](#toc)

## Percorsi relativi nei file inclusi [relative_paths_in_included_files]

I file inclusi utilizzando la [sintassi di inclusione] [include] di Marked, così come i [file di Scrivener] [scriv], possono utilizzare percorsi relativi per fare riferimento ad altri file. (_**Nota:** questo non si applica ai file inclusi utilizzando la sintassi `/file` di IA Writer o i file CSV_). A partire dalle versioni recenti (2.5.10+), questi percorsi sono _relativi al file incluso_, non al file di base.

Data una struttura di file/cartelle come questa:

    -file_base.md
    - sottocartella
        - file_incluso.md
    - immagini
        -immagine1.jpg

Se `included_file.md` fa riferimento a image1.jpg tramite un percorso relativo, deve essere scritto come `../images/image1.jpg`, _non_ `images/image1.jpg`. (`..` indica la directory principale) .

[include]: http://marked2app.com/help/Multi-File_Documents.html
[scriv]: http://marked2app.com/help/Scrivener_Support.html

[Sommario](#toc)

## Come posso recuperare una licenza persa (versione diretta) [how_do_i_retrieve_a_lost_license_direct_version]

Se hai perso una licenza acquistata per Marked 2 tramite Paddle, puoi recuperarla su [my.paddle.com](https://my.paddle.com/). Se riscontri problemi con l'accesso da lì, puoi richiedere una ricerca tramite una richiesta privata sul [sito di supporto](http://support.markedapp.com).

[Sommario](#toc)

## Problemi di acquisto in-app (Errore Domain=Paddle Code=0 "(null)") [in-app_purchase_issues_error_domainpaddle_code0_null]

Paddle mi ha recentemente informato che gli IAP non funzionano e che non hanno intenzione di risolverli perché non sono stati implementati da un numero sufficiente di sviluppatori. (Il che è frustrante per me quanto lo è per te.) La parte veramente frustrante è che non hanno smesso di consentire i pagamenti, quindi devo rimborsare manualmente gli acquisti finché non viene fatto qualcosa sul modo in cui vengono gestite le licenze. Si suppone che un nuovo sistema verrà implementato nelle prossime due settimane, quindi se sei disposto ad aspettare, farò tutto il possibile per garantire che tutti gli attuali acquisti di IAP ortografia/grammatica vengano onorati attraverso qualunque sistema verrà fornito successivamente

Se preferisci un rimborso, <a href="mailto:me@brettterpstra.com">inviami direttamente un'e-mail</a> con l'account e-mail utilizzato per la licenza o l'ID della transazione dalla ricevuta.

**Aggiornamento:** Paddle ha annunciato ufficialmente la nuova soluzione IAP e verrà implementata non appena sarà disponibile al pubblico. Le attuali licenze di acquisto in-app (ortografia/grammatica) verranno trasferite automaticamente e verrà fornito un nuovo codice coupon. Questo dovrebbe accadere presto.

[Sommario](#toc)

## Blocchi di codice recintati all'interno di blocchi di codice rientrati [fenced_code_blocks_inside_indented_code_blocks]

In circostanze abbastanza rare potresti voler mostrare le recinzioni di un blocco di codice recintato. Normalmente ciò potrebbe essere ottenuto in Markdown indentando il codice recintato, forzando un blocco "letterale" rientrato contenente il blocco di codice recintato, che verrebbe quindi non elaborato. Marked gestisce il codice protetto in modo diverso (come parte della sua capacità di lavorare con più opzioni di sintassi), quindi per ottenere ciò è necessario utilizzare un doppio recinto. Poiché è possibile utilizzare un numero qualsiasi di backtick o tilde per recintare un blocco di codice (a condizione che il conteggio di apertura e chiusura corrisponda, è possibile utilizzare semplicemente due recinzioni di lunghezza diversa. Ad esempio

    `````
    ```
    Codice protetto effettivo
    ```
    `````

[Sommario](#toc)