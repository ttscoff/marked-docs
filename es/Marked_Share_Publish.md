<!-- MT draft for es — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** es el servicio de publicación en línea de Marked en [share.markedapp.com](https://share.markedapp.com). Conecte su Mac una vez y luego publique el documento frontal como **TextPack** con imágenes y aspectos destacados del modo de lectura opcionales. Cualquiera que tenga el enlace puede ver el documento en la web.

Esta función es independiente de la **extensión Compartir** de macOS (menú Compartir del sistema). Consulte [Using the Share Extension](Share_Extension.html) para enviar archivos o selecciones a Marked desde otras aplicaciones.

## Conecta tu cuenta [connect-your-account]

Antes de su primera publicación, conecte Marked a su cuenta Share:

1. Elija {% appmenu Archivo, Publicar, Conectar cuenta… %}.
2. Marked abre su navegador predeterminado para iniciar sesión en share.markedapp.com.
3. Después de aprobar la conexión, el navegador regresa a Marked con un enlace de inicio de sesión seguro. Confirme la etiqueta de cuenta que se muestra en el cuadro de diálogo.

Marked almacena el token de API y la clave del dispositivo en el llavero de macOS de esta Mac. Las credenciales no se escriben en registros ni informes de fallos.

Para desconectarse, elija {% appmenu Archivo, Publicar, Desconectar cuenta… %}. Los documentos publicados permanecen en línea; revocar el acceso en cualquier momento en share.markedapp.com si es necesario.

## Publicar un documento [publish-a-document]

Con un documento abierto en la vista previa, elija {% appmenu Archivo, Publicar, Publicar… %}.

La primera vez que publicas un documento, Marked muestra una pequeña hoja de opciones:

- **Título**: se muestra en Compartir (el valor predeterminado es el nombre del documento sin su extensión).
- **Visibilidad**: privado, no listado o público. Las nuevas publicaciones tienen el valor predeterminado **No listado** (accesible mediante enlace, no listado públicamente).
- **Estilo de lectura**: editorial, manuscrito, suizo, contraste, máquina de escribir o **Ninguno**. Valores predeterminados del estilo de vista previa del documento cuando sea posible. Share usa esto como una sugerencia; los lectores pueden anularlo. Elija **Ninguno** para publicar sin un estilo sugerido.
- **Incluir aspectos destacados y comentarios**: incorpora aspectos destacados del modo de lectura en TextPack. El valor predeterminado es activado cuando el documento tiene resaltados.
- **Permitir que otros hagan remezclas**: cuando está habilitado, los espectadores pueden bifurcar el documento en Compartir.

Marked crea un TextPack en segundo plano (Markdown, activos y `highlights.json` opcional), lo carga y registra la URL compartida en esta Mac.

### Actualizar una publicación existente [update-an-existing-publish]

Después de vincular un documento a Compartir, el elemento del menú dice **Actualizar documento publicado** en lugar de **Publicar…**. Elíjalo para cargar una nueva versión TextPack. Marked envía el hash de contenido del servidor para que se detecten ediciones simultáneas desde otra Mac o la web.

Si alguien más actualizó el documento en Compartir primero, Marked pregunta si desea **Sobrescribir** con la versión de esta Mac, **Abrir en Web** o **Cancelar**.

## Después de publicar [after-publishing]

Cuando finaliza una publicación, Marked confirma el éxito y ofrece:

- **Copiar enlace para compartir** — {% appmenu Archivo, Publicar, Copiar enlace de Share %}
- **Abrir en Web** — {% appmenu Archivo, Publicar, Abrir en la web %}

Estos comandos se aplican al documento frontal cuando tiene un registro de publicación vinculado.

## Ventana Documentos publicados [published-documents-window]

Elija {% appmenu Archivo, Publicar, Documentos publicados… %} para abrir una lista de documentos publicados desde esta Mac y sincronizados desde su cuenta Share.

Para cada entrada puedes:

- **Abra** el archivo local cuando Marked todavía tenga un enlace en el disco.
- **Importar** un TextPack cuando no haya ningún archivo local (guárdelo en cualquier lugar y ábralo en Marked).
- **Abrir en la Web** o **Copiar enlace** para compartir URL.
- **Revelar en Finder** cuando se conoce una ruta local.
- **Olvidar** elimina el registro de esta Mac sin eliminar el documento en línea.

La lista se actualiza desde Compartir cuando estás conectado. Si está desconectado o sin conexión, Marked muestra registros almacenados en caché y puede solicitarle que se vuelva a conectar.

## Lo que puedes publicar [what-you-can-publish]

Puede publicar cualquier documento que Marked pueda representar, incluido:

- Guardado Markdown y archivos de texto
- Vistas previas transitorias (portapapeles, streaming o documentos no guardados)
- TextBundles y otros formatos compatibles

Sólo se ejecuta una operación de publicación a la vez por ventana de documento; el elemento del menú está deshabilitado mientras se realiza una carga.

## Consejos [tips]

- La publicación incluye imágenes a las que hace referencia la vista previa. Es posible que los paquetes muy grandes se rechacen antes de cargarlos; reduzca los activos integrados si alcanza un límite de tamaño.
- Los aspectos destacados exportados en TextPack utilizan el formato JSON de resaltado de Marked. Consulte [Reading Mode](Reading_Mode.html) para crear y exportar aspectos destacados.
- Marked Share está disponible en las versiones Direct, Mac App Store, Setapp y Marked Pro. No se requiere una suscripción separada para publicar.
