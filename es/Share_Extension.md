<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked incluye una **extensión de Compartir** de macOS que aparece en el menú Compartir del sistema. Úsela para enviar un archivo o texto seleccionado a Marked sin cambiar de aplicación ni copiar URL manualmente.

La extensión de Compartir **viene incluida con Marked 3**. No se descarga ni instala por separado. Se incluye en las compilaciones Direct, Mac App Store, Marked Pro y Setapp.

## Cómo funciona [how-it-works]

Cuando elige **Marked** en un menú Compartir, Marked se abre de inmediato. No hay una ventana intermedia de composición.

### Compartir un archivo [share-a-file]

Desde **Finder** (u otra app que comparta archivos), elija **Compartir → Marked**.

Marked recibe la ruta del archivo y lo abre con el mismo controlador de URL `x-marked-3://open` usado en otros flujos. El archivo se abre en Marked como si lo hubiera arrastrado al icono del Dock o elegido con {% appmenu File, Open... ({{cmd}}O) %}.

Entradas admitidas: URL de archivo, archivos locales y URL web cuando la app de origen las proporciona.

### Compartir texto seleccionado [share-selected-text]

Seleccione texto en una app como **TextEdit**, **Safari** o **Mail**, luego elija **Compartir → Marked**.

Marked coloca el texto en el portapapeles y abre una **vista previa transitoria** con el controlador `x-marked-3://paste`. Es el mismo tipo de vista previa sin guardar que {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Puede guardarla después con {% appmenu File, Save Transient Preview %}.

Se admiten texto plano, HTML, RTF y Markdown cuando la app de origen los proporciona.

Consulte [URL Handler](URL_Handler.html) para detalles de los comandos subyacentes.

## Usar el menú Compartir [using-the-share-menu]

### Desde Finder [from-finder]

1. Haga clic derecho en un archivo Markdown o de texto (o selecciónelo y pulse **Compartir** en la barra de herramientas de Finder).
2. Elija **Marked** en el menú Compartir.

Si **Marked** no aparece, consulte [Activar la extensión de Compartir](#enable-the-share-extension) más abajo.

### Desde una selección de texto [from-a-text-selection]

1. Seleccione el texto que desea previsualizar.
2. Abra el menú **Compartir** de la app (menú Compartir, botón de la barra de herramientas o menú contextual).
3. Elija **Marked**.

Marked se inicia (o pasa al frente) con una vista previa del contenido compartido.

## Activar la extensión de Compartir [enable-the-share-extension]

Marked debe estar instalado en `/Applications` (o su carpeta Aplicaciones habitual) y haberse abierto al menos una vez antes de que macOS liste su extensión de Compartir.

### Activar Marked en Ajustes del Sistema [turn-on-marked-in-system-settings]

1. Abra **Ajustes del Sistema**.
2. Vaya a **General → Objetos de inicio de sesión y extensiones** (en algunas versiones de macOS: **Privacidad y seguridad → Extensiones**).
3. Pulse **Extensiones** (o el botón **ⓘ** junto a Extensiones).
4. Seleccione **Compartir** (o **Sharing**).
5. Active **Marked**.

### Añadir Marked al menú Compartir de una app [add-marked-to-an-apps-share-menu]

Aunque la extensión esté activada en todo el sistema, cada app elige qué destinos de Compartir mostrar:

1. Abra una app con Compartir (Finder y TextEdit son buenas pruebas).
2. Abra el menú **Compartir**.
3. Elija **Editar extensiones…** (en macOS antiguos puede decir **Más…** o **Preferencias de extensiones…**).
4. En **Compartir**, marque **Marked**.
5. Opcionalmente arrastre **Marked** más arriba en la lista para acceder más rápido.

Los cambios se aplican de inmediato en la mayoría de las apps.

## Si Marked no aparece en Compartir [if-marked-does-not-appear-in-share]

W> La extensión de Compartir está disponible desde Marked 3.1.9. Asegúrese de haber actualizado al menos a esa versión.

Pruebe estos pasos en orden:

1. **Abra Marked una vez** tras instalar o actualizar. Cierre y vuelva a abrir Marked si acaba de actualizar.
2. **Confirme que la extensión está activada** en Ajustes del Sistema como se describe arriba.
3. **Personalice el menú Compartir** en la app desde la que comparte. macOS oculta destinos poco usados hasta que los activa.
4. **Varias copias de Marked:** si tiene instaladas las versiones Direct y Mac App Store, solo la copia en ejecución registra su extensión. Elimine o renombre la que no use y abra la deseada.
5. **Reinicie el Mac** si la extensión sigue sin aparecer tras una actualización. macOS cachea el registro de extensiones de Compartir.
6. **Reinstale Marked** en `/Applications` si prueba una compilación copiada manualmente desde Xcode o una imagen de disco. La extensión debe estar en `Marked.app/Contents/PlugIns/`.

## Consejos [tips]

- La extensión de Compartir es ideal para vistas previas rápidas de fragmentos web, párrafos de correo o notas sin crear un archivo primero.
- Para páginas completas o selecciones complejas en un navegador, las [extensiones del navegador](Using_the_Browser_Extensions.html) pueden ofrecer más control (selección de sección, Markdownify URL, etc.).
- Los archivos compartidos se abren como documentos normales de Marked con seguimiento de archivo. El texto compartido abre una vista previa transitoria hasta que guarde.
