<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked se creó con mucha ayuda de la comunidad de código abierto. Esta página enumera el código de terceros que se envía dentro de Marked. El texto completo de la licencia para los procesadores Markdown está disponible en las páginas vinculadas en [Acerca de Markdown](MultiMarkdown_Information.html).

## Procesadores Markdown y conversión

| Componente | Autores | Licencia | Utilizado para |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | Estilo BSD | Procesador Markdown predeterminado |
| [Descuento](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Procesador Markdown alternativo (a través de GGHarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Oliver Letterer](https://github.com/OliverLetterer) | MIT | Envoltorio Objective-C alrededor del descuento |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) y colaboradores | Cláusula BSD-2 | Análisis de Markdown con sabor a GitHub |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Opción de procesador Kramdown (Ruby incluido) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | Importación de PDF a Markdown |

## Código nativo y marcos

| Componente | Autores | Licencia | Utilizado para |
| --- | --- | --- | --- |
| [Fuente](https://fountain.io/) | Nima Yousefi y John Agosto | MIT | Análisis del guión de la fuente |
| [CacaoLeñador](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | Cláusula BSD-3 | Registro de depuración |
| [Brillo](https://sparkle-project.org/) | Proyecto Brillo | MIT | Actualizaciones automáticas (compilaciones de descarga directa) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomery | Cláusula BSD-2 | Análisis de metadatos YAML |
| [libiaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | Biblioteca YAML (utilizada por YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave De Long | MIT | Importación de tablas CSV |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Legibilidad y estadísticas de texto |
| [RegexKitLite](http://regexkit.sourceforge.net/) | Juan Engelhart | BSD | Utilidades de expresiones regulares |
| [Categorías RegEx](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Categorías de expresiones regulares |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | Cláusula BSD-2 | Ayudantes de acceso a archivos Sandbox |
| [VDKCola](https://github.com/bdkjones/VDKQueue) | Bryan DK Jones | Permisivo personalizado | Notificaciones de cambio de archivos |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Información-ZIP | estilo zlib | Manejo de archivos ZIP |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | Kit de mantequilla | MIT | Utilidades de vista de desplazamiento |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC POR 3.0](https://creativecommons.org/licenses/by/3.0/) | Barra de herramientas de la ventana Preferencias |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Ver proyecto | Representación de tablas CSV |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Ver proyecto | Indicadores de progreso |
| [Administrador de IAPM](https://github.com/mruegenberg/IAPManager) | Marcel Rügenberg | Ver proyecto | Asistentes de compra dentro de la aplicación (heredados) |

## Vista previa de JavaScript

Estas bibliotecas están concatenadas en el paquete de vista previa de Marked (`marked.min.js` y recursos relacionados):

| Componente | Autores | Licencia | Utilizado para |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | Fundación jQuery | MIT | DOM y utilidades de eventos |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Manejo táctil y gestual |
| [Resaltar.js](https://highlightjs.org/) | Josh Goebel y colaboradores | Cláusula BSD-3 | Resaltado de sintaxis |
| [MathJax](MathJax.html) | El consorcio MathJax | Apache-2.0 | Representación matemática (paquete local) |
| [KaTeX](https://katex.org/) | Khan Academy y colaboradores | MIT | Representación matemática (opción KaTeX) |
| [Sirena](https://mermaid.js.org/) | Colaboradores de sirena | MIT | Representación del diagrama |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Detección de características |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alejandro Farkas | MIT/GPL2 | Compatibilidad con elementos HTML5 (a través de la compilación Modernizr) |
| [Sí, no](https://github.com/SlexAxton/yepnope) | Alex Sexton y Paul Irish | MIT/WTFPL | Carga de script (a través de la compilación Modernizr) |
| [Bloque de libros](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Modo de presentación de cambio de página |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (acelerador/rebote) | MIT | Atajos de teclado |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Detección de texto bidireccional |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Formato de fecha |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Detección de ventana gráfica |
| [palabra resaltada.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Resaltado de búsqueda en documentos |

## Localización

Marked está disponible en varios idiomas gracias a traductores voluntarios:

-Akira
- Brett Crawley
-Enoc Ko
- Fleming Mahler
- Hans Tammen
- Mathías Maul
-Miguel Martínez de la Torre
-Normand Primeau
- PG Neuromonaco
-Richard Kranendonk
- Sébastien Gaïde
- Yuki Tamari
-亮王

## Agradecimientos

Gracias también a Daniel Jalkut por sus años de orientación y a Felippe van Eekhout por el icono de Marked.