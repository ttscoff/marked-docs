<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[vim-marked] [vimrepo] è un plugin Vim che apre l'attuale buffer Markdown in Marked. Aggiunge `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` e `:MarkedPreview` in modo da poter inviare il file (o un intervallo) a Marked senza uscire dall'editor.

## Configurazione [setup]

Installa con il tuo gestore plugin; vedere il [README del progetto] [vimrepo] per `vim-plug` e altre opzioni. Il valore predefinito `g:marked_filetypes` include `markdown` e varianti comuni; estendi l'elenco se usi un `filetype` personalizzato.

## macOS e nome dell'app [macos-and-app-name]

Contrassegnato è solo per macOS, quindi il plug-in non viene caricato su altri sistemi. Il nome predefinito dell'app è **Contrassegnato 2**; se la tua copia di Marked è installata con un nome o percorso diverso, imposta `g:marked_app` in modo che corrisponda (ad esempio un percorso completo all'app bundle). Il README copre il comportamento di uscita, uscita automatica e messa a fuoco.

I> Questo argomento della guida non fa parte del progetto contrassegnato da vim; per i comandi e le opzioni più recenti, utilizzare il [repository GitHub] [vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked