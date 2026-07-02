<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[vim-marked][vimrepo] es un complemento de Vim que abre el búfer de Markdown actual en Marked. Agrega `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` y `:MarkedPreview` para que puedas enviar el archivo (o un rango) a Marcado sin salir del editor.

## Configuración

Instálelo con su administrador de complementos; consulte el [proyecto README][vimrepo] para `vim-plug` y otras opciones. El `g:marked_filetypes` predeterminado incluye `markdown` y variantes comunes; amplíe la lista si usa un `filetype` personalizado.

## macOS y nombre de la aplicación

Marked es solo para macOS, por lo que el complemento no se carga en otros sistemas. El nombre predeterminado de la aplicación es **Marcado 2**; Si su copia de Marked está instalada con un nombre o ruta diferente, configure `g:marked_app` para que coincida (por ejemplo, una ruta completa al paquete de aplicaciones). El archivo README cubre el comportamiento de cierre, cierre automático y concentración.

I> Este tema de ayuda no forma parte del proyecto marcado con vim; para obtener los comandos y opciones más recientes, utilice el [repositorio de GitHub][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked