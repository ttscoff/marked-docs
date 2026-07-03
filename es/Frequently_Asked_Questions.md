<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %> [toc]

## El código de licencia ya se ha utilizado [license_code_has_already_been_utilized]

Si realiza una instalación nueva de Marked 2 y recibe el error "El código de licencia ya se ha utilizado" al ingresar su licencia, <a href="mailto:me@brettterpstra.com">comuníquese conmigo</a> para solicitar una nueva licencia. **Incluya la dirección de correo electrónico con la que se registró y/o su código de licencia actual.**

Las primeras licencias generadas para Marked tenían un límite de uso en lugar de un límite de máquina, por lo que 3 instalaciones, incluso en la misma máquina, consumirían activaciones. Estos límites se han corregido en las licencias generadas más recientemente. La compra de una licencia de Marked 2 le permite instalar Marked 2 en cualquier máquina de su propiedad, así que no dude en solicitar un reemplazo si tiene problemas.

[Tabla de contenidos](#toc)

## Licencias de sitio y descuentos educativos [site_licenses_and_educational_discounts]

Hay licencias de sitio/a granel con descuento disponibles para Marked 2. Para solicitar un enlace de compra, comuníquese con <a href="mailto:me@brettterpstra.com">Brett</a> y especifique la cantidad de licencias que desea comprar.

**Descuentos**

- 5-9: **10% de descuento**
- 10-19: **12% de descuento**
- 20-49: **15% de descuento**
- 50+: **20% de descuento**

También hay disponible un descuento educativo tanto para la versión directa como para la Mac App Store. Para Mac App Store, están habilitados los descuentos educativos estándar de Apple. Para comprar una versión directa con un descuento educativo, <a href="mailto:me@brettterpstra.com">contácteme</a> y solicite un cupón.

[Tabla de contenidos](#toc)

## Una URL no se valida o devuelve "Desconocido" [a_url_wont_validate_or_returns_unknown]

La [validación de enlace](http://marked2app.com/help/Link_Validation.html) de Marked utiliza una solicitud HEAD básica para determinar si un enlace es válido. Cualquier resultado que no sea 200 (éxito) generará una incógnita o un error si se trata de un código de error común como 404 (no encontrado) o 500 (error del servidor). Las URL detrás de la autenticación (como las URL de desarrolladores de Apple o cualquier cosa que requiera iniciar sesión para acceder) devolverán un valor "desconocido", al igual que ciertos sitios como Amazon.com, donde el servidor devuelve códigos de respuesta extraños. No hay mucho que Marked pueda hacer al respecto.

[Tabla de contenidos](#toc)

## Permisos de procesador personalizados en la versión MAS [custom_processor_permissions_in_mas_version]

Debido a restricciones de espacio aislado, la versión Mac App Store de Marked 2 no puede ejecutar ciertos tipos de herramientas binarias como procesadores personalizados. Si se encuentra con esta limitación, hay algunos pasos que puede probar.

1. Asegúrese de haber entrado en **Preferencias marcadas 2** (⌘,), en el panel **Avanzado** y haber hecho clic en "Actualizar permisos". Esto intentará otorgar acceso a Marked a toda su unidad predeterminada, solucionando problemas con scripts y utilidades que necesitan acceder a carpetas temporales y ubicaciones no predeterminadas.
2. Intente utilizar un script. Haga referencia a la utilidad que desea ejecutar (multimarkdown, kramdown, etc.) en un script de shell. Puede ser un script bash, Ruby, Perl o Python. Luego configure el procesador en Preferencias avanzadas al shell o ejecutable relacionado, y los parámetros a la ubicación del script. Por ejemplo, puedo crear un script bash guardado en ~/scripts/mmd_wrapper.sh:
    
        #!/bin/bash
        gato | /usr/local/bin/multimarkdown
    
    Luego, hazlo ejecutable (`chmod a+x ~/scripts/mmd_wrapper.sh`) y configura mis preferencias de Procesador personalizado:

        Procesador: /bin/bash
        Argumentos: /Users/me/scripts/mmd_wrapper.sh
3. Algunos ejecutables (especialmente Pandoc) simplemente no funcionan en el sandboxing. En este caso, comuníquese conmigo a través de la ventana de error que aparece durante la ejecución para recibir una licencia cruzada para la versión directa.

[Tabla de contenidos](#toc)

## Enlaces dentro del documento en archivos PDF exportados [intra-document_links_in_exported_pdfs]

La exportación de PDF de Marked actualmente utiliza las funciones de impresión de WebKit. Una consecuencia de esto es que los enlaces dentro del documento (internos), incluidos los de una tabla de contenido, no saltarán a otros puntos del documento. Esto no parece ser algo que Apple tenga intención de solucionar en la versión de WebKit que utiliza Marked 2.

En algunos casos, puede obtener buenos resultados exportando HTML con estilo incrustado y luego utilizando su navegador web para imprimir en PDF. No obtendrá todas las funciones de exportación de Marked, pero normalmente obtendrá un PDF con enlaces internos que funcionen. Es una compensación por ahora.

[Tabla de contenidos](#toc)

## Rutas relativas en archivos incluidos [relative_paths_in_included_files]

Los archivos incluidos con la [sintaxis de inclusión][incluir] de Marked, así como los [archivos de Scrivener][scriv], pueden usar rutas relativas para hacer referencia a otros archivos. (_**Nota:** esto no se aplica a los archivos incluidos con la sintaxis `/file` de IA Writer o archivos CSV_). A partir de versiones recientes (2.5.10+), estas rutas son _relativas al archivo incluido_, no al archivo base.

Dada una estructura de archivo/carpeta como esta:

    - archivo_base.md
    - subcarpeta
        - archivo_incluido.md
    - imágenes
        - imagen1.jpg

Si `included_file.md` hace referencia a image1.jpg a través de una ruta relativa, debe escribirse como `../images/image1.jpg`, _no_ `images/image1.jpg`. (`..` indica el directorio principal).

[include]: http://marked2app.com/help/Multi-File_Documents.html
[scriv]: http://marked2app.com/help/Scrivener_Support.html

[Tabla de contenidos](#toc)

## ¿Cómo recupero una licencia perdida (versión directa) [how_do_i_retrieve_a_lost_license_direct_version]

Si perdió una licencia que compró para Marked 2 a través de Paddle, puede recuperarla en [my.paddle.com](https://my.paddle.com/). Si tiene algún problema para iniciar sesión allí, puede solicitar una búsqueda mediante una solicitud privada en el [sitio de soporte](http://support.markedapp.com).

[Tabla de contenidos](#toc)

## Problemas de compras dentro de la aplicación (Dominio de error=Código Paddle=0 "(nulo)") [in-app_purchase_issues_error_domainpaddle_code0_null]

Paddle me informó recientemente que los IAP no funcionan y que no planean solucionarlos porque no los han implementado suficientes desarrolladores. (Lo cual es tan frustrante para mí como para usted). La parte verdaderamente frustrante es que no han dejado de permitir pagos, por lo que necesito reembolsar las compras manualmente hasta que se haga algo con respecto a la forma en que se manejan las licencias. Se supone que se implementará un nuevo sistema en las próximas semanas, por lo que si está dispuesto a esperar, haré todo lo posible para garantizar que todas las compras actuales del IAP de Ortografía/Gramática se respeten a través del sistema que se proporcione a continuación.

Si prefiere un reembolso, simplemente <a href="mailto:me@brettterpstra.com">envíeme un correo electrónico directamente</a> con la cuenta de correo electrónico utilizada para obtener la licencia o el ID de la transacción que figura en el recibo.

**Actualización:** Paddle ha anunciado oficialmente la nueva solución IAP y se implementará tan pronto como esté disponible públicamente. Las licencias actuales de compra en la aplicación (ortografía/gramática) se migrarán automáticamente y se proporcionará un nuevo código de cupón. Esto debería suceder pronto.

[Tabla de contenidos](#toc)

## Bloques de código vallados dentro de bloques de código con sangría [fenced_code_blocks_inside_indented_code_blocks]

En circunstancias bastante raras, es posible que desees mostrar las barreras de un bloque de código delimitado. Normalmente, esto podría lograrse en Markdown sangrando el código delimitado, forzando un bloque "textualmente" sangrado que contenga el bloque de código delimitado, que luego no se procesaría. Marked maneja el código delimitado de forma diferente (como parte de su capacidad para trabajar con múltiples opciones de sintaxis), por lo que para lograr esto es necesario utilizar un delimitador doble. Porque puede usar cualquier cantidad de comillas invertidas o tildes para cercar un bloque de código (siempre que el recuento de apertura y cierre coincida, puede usar dos cercas de diferentes longitudes. Por ejemplo

    `````
    ```
    Código vallado real
    ```
    `````

[Tabla de contenidos](#toc)