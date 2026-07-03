<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

{% apponly div %}
*Per la versione più recente di questa documentazione, visitare la [versione online][aiuto].*
{% endapponly %}

**Assicurati di dare un'occhiata alla crescente raccolta di [Video tutorial contrassegnati](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## Cos'è il Markdown?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown è un linguaggio di markup di base che utilizza simboli semplici, consentendoti di scrivere HTML (ed esportare in altri formati) con una sintassi semplice come `*italics*` e `**bold**`. Markdown è stato creato da John Gruber e sta rapidamente diventando lo standard de facto per la pubblicazione sul web, per prendere appunti e persino per la pubblicazione di libri. Ti consente di scrivere senza un mucchio di barre degli strumenti e problemi di formattazione, semplicemente inserendo le parole sulla pagina e lasciando che i tuoi processori (come Marked) gestiscano lo stile e la formattazione.

Marked funziona con GitHub Flavored Markdown, CommonMark (GFM), Kramdown e MultiMarkdown e può convertire la sintassi da diverse varianti per l'anteprima (può anche essere esteso per funzionare con praticamente qualsiasi processore di cui hai bisogno, inclusi Textile, reStructuredText, Wikitext e altro). Presumo che --- visto che sei qui --- tu sappia cosa sia almeno uno di questi linguaggi di markup. In caso contrario, dovresti iniziare da [Markdown Basics] [daringfireball] di John Gruber, controlla [MarkdownGuide.org] [mdguide]. Marked include una guida completa alla sintassi Markdown nel menu Guida.

Puoi utilizzare [Markdown Dingus](x-marked-3://dingus) per sperimentare le diverse versioni di Markdown supportate da Marked.

## Cosa è contrassegnato?

Marked è un'app di anteprima Markdown live per macOS --- un'applicazione di anteprima Markdown (Multi) indipendente dall'editor che controlla le modifiche di un file, aggiornando l'anteprima ogni volta che salvi. Separando e automatizzando i dettagli della formattazione ti consente di concentrarti maggiormente sulla scrittura e meno sulla presentazione, il tutto mantenendo sotto controllo il tuo prodotto finale.

Per i flussi di lavoro di configurazione e gli avviamenti rapidi specifici dell'editor, consulta [Anteprima Live Markdown su Mac](Live_Markdown_Preview_on_Mac.html). Per una panoramica più breve del prodotto, visita [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked funziona con qualsiasi file accessibile localmente, inclusi i documenti iCloud. Basta trascinare un documento di testo dalla barra degli strumenti di qualsiasi editor su Contrassegnato e lo renderà come anteprima HTML e inizierà a tenere traccia delle modifiche, aggiornando l'anteprima mentre scrivi. Può anche compilare [documenti multi-file](Multi-File_Documents.html) utilizzando una sintassi di base "include" o dai formati di indice Scrivener, Leanpub e mmd_merge.

Marked ha funzionalità aggiuntive, tra cui il conteggio delle parole e altre statistiche sui documenti, la possibilità di fluttuare sopra altre applicazioni o oscurarsi sullo sfondo e può visualizzare il tuo lavoro in una varietà di stili ben realizzati. Può stampare o PDF, documenti Word, documenti HTML completi (inclusi stili e immagini) o copiare dati sorgente HTML o RTF negli appunti con la semplice pressione di un tasto. Marked ha anche un dizionario AppleScript di base e un [gestore URL](URL_Handler.html) che ne facilitano l'integrazione nel tuo flusso di lavoro.

Oh sì, e funziona con tantissime delle tue app preferite: editor di testo che vanno da Vim ed Emacs a Sublime Text e TextMate, editor Markdown come MultiMarkdown Composer, Byword e iA Writer, persino app che potresti non aspettarti come Ulysses, Scrivener, VoodooPad, MarsEdit e altre.

## Esempi di utilizzo

Marked trasforma qualsiasi editor di testo in un editor abilitato per Markdown. L'anteprima è sempre disponibile e si aggiorna mentre lavori.

* Se il tuo editor preferito non offre un'anteprima Markdown dal vivo, apri il documento su cui stai lavorando in Marked e sposta la finestra lateralmente per un'esperienza di scrittura Markdown completa.
* Ti piace scrivere o bloggare in MacVim o in un altro editor basato su terminale? Ora hai un'anteprima Markdown sincronizzata mentre lavori.
* Marked offre inoltre funzionalità di visualizzazione che vanno oltre qualsiasi anteprima Markdown esistente e può essere utilizzato invece per fornire statistiche complete sul conteggio delle parole e sui documenti, suggerimenti di scrittura e persino evidenziare errori nella formattazione Markdown.
* Puoi anche utilizzare Marked senza un editor. Basta trascinare i file Markdown sull'icona per visualizzarli in anteprima, stamparli ed esportarli in codice sorgente PDF, DOC, RTF o HTML. Marked può anche **aprire `.rtf` e `.rtfd` file** come documenti di origine ([Supporto RTF e RTFD](RTF_Support.html)).
* Nelle app che effettuano il salvataggio automatico, scoprirai che l'anteprima segue la tua scrittura senza alcun aiuto. Usalo con qualsiasi editor... o *tutti* i tuoi editor.
* Scrivere un libro? Marked può compilare più file per un'anteprima completa del tuo lavoro e persino controllare le modifiche nei file inclusi, aggiornando il documento principale ad ogni salvataggio. Può anche controllare le modifiche di un'intera cartella, passando automaticamente l'anteprima al file che stai aggiornando. Quando sei pronto, puoi pubblicare nei formati EPUB, DOCX o TextBundle.
* Lavori con una piattaforma di codifica AI? Apri una cartella del piano o della documentazione in Marked e ogni volta che un file Markdown in quella cartella cambia, Marked lo visualizzerà, scorrendo automaticamente fino al punto della modifica più recente. Marked visualizza i diagrammi della sirena e può gestire tutti i tipi di sintassi estesa. Tieni traccia dei piani e della documentazione mentre lavori, senza passare da un file all'altro.