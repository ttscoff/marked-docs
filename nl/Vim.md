# <%= @title %>

[vim-marked][vimrepo] is een Vim-plug-in die de huidige Markdown buffer opent in Marked. Het voegt `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` en `:MarkedPreview` toe, zodat je het bestand (of een bereik) naar Marked kunt sturen zonder de editor te verlaten.

## Installatie

Installeer met uw plug-inbeheerder; zie de [project README][vimrepo] voor `vim-plug` en andere opties. De standaard `g:marked_filetypes` omvat `markdown` en algemene varianten; breid de lijst uit als u een aangepaste `filetype` gebruikt.

## macOS en app-naam

Marked is alleen voor macOS, dus de plug-in wordt niet op andere systemen geladen. De standaard app-naam is **Marked 2**; als uw exemplaar van Marked is geïnstalleerd onder een andere naam of een ander pad, stelt u `g:marked_app` zo in dat dit overeenkomt (bijvoorbeeld een volledig pad naar de appbundel). De README behandelt het gedrag van stoppen, automatisch stoppen en focussen.

I> Dit helponderwerp maakt geen deel uit van het vim-gemarkeerde project; voor de nieuwste opdrachten en opties gebruikt u [GitHub repository][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked
