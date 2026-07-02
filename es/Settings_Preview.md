<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Preview %}:

![Configuración: Vista previa][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Comportamiento de vista previa

Habilitar la navegación del minimapa
: Genera un mapa visual del documento que aparece cuando se presiona "0". Puede causar breves retrasos al procesar documentos grandes.

Los titulares colapsan secciones
: Al hacer clic en un elemento de título, se contrae la sección entre este y el siguiente título.

Requerir {% kbd cmd %}‑clic
: Si esto está marcado, los titulares solo se contraerán/expandirán cuando se haga clic con la tecla Comando presionada.

Sincronización de vista previa y desplazamiento de fuente
: Cuando su editor lo admita, mantenga la vista previa desplazada para que coincida con la ubicación correspondiente en el documento fuente.

Sincronización de lectura rápida con posición de desplazamiento
: Mantenga la superposición [Lectura rápida](Speed_Reading.html) alineada con la posición de desplazamiento de vista previa. También puede alternar esto desde la superposición de Lectura rápida.

### Desplázate para editar

Desplázate para editar
: Al actualizar la vista previa, Marked puede determinar el primer punto donde cambió el documento y desplazarse automáticamente hasta él. Esto mantiene la vista previa sincronizada con su ubicación actual en el documento que está editando. El marcador de edición más reciente es la primera diferencia en el documento desde la última actualización. Al habilitar el "Orden de diferencias inverso", se considerará la última diferencia en el documento (de arriba a abajo) como la edición más reciente.

Mostrar marcador de edición más reciente
: Aparece un pequeño marcador rojo en el punto de la primera edición detectada. Desactiva esto para hacerlo invisible. (Requiere **Desplácese para editar**).

Mostrar todos los marcadores de diferencias
: Si esto está habilitado, todas las diferencias entre la última actualización y el contenido actual se resaltarán en el margen. Puede navegar a través de las ediciones, desplazándolas hasta el centro de la vista, usando <kbd>e</kbd> (hacia adelante) y {% kbd shift E %} (hacia atrás).

Orden de diferenciación inverso
: Si esto está habilitado, las diferencias se marcarán en orden inverso (de abajo hacia arriba). Esto afecta la navegación, por lo que <kbd>e</kbd> navegará hacia arriba y {% kbd shift E %} navegará hacia abajo. La "edición más reciente" se convertirá en la última diferencia en el documento.

### Funciones adicionales

La tabla de contenido rastrea la posición de desplazamiento
: La tabla de contenido destaca la sección actual.

Estadísticas emergentes para selección de texto
: muestra una ventana emergente de recuento de palabras para el texto seleccionado cada vez que se realiza una selección.

Habilitar enlaces emergentes
: Muestra un menú emergente cuando se hace clic y se mantiene presionado en enlaces externos antes de liberarlos.

Validar automáticamente las URL al actualizar
: Valide las URL al cargar y actualizar el documento. Sólo muestra resultados si hay errores.
: Esto ejecuta [validación de enlaces](Link_Validation.html) cada vez que se actualiza el documento (si tiene una cantidad significativa de enlaces, esto puede ser un proceso lento y debe evitarse).

### Enlace wiki

Convertir [[Enlaces Wiki]]
: Habilite la [navegación wiki](Wiki_Navigation.html) de Marked para la sintaxis `[[wiki link]]`.

Extensión predeterminada
: La extensión de nombre de archivo que Marked utiliza al resolver enlaces wiki que no incluyen una extensión (por ejemplo, `md`).

### Apariencia

Modo oscuro
: muestra todas las ventanas en modo "Alto contraste", con cromo oscuro y, si está disponible, la versión invertida del estilo actual (es posible que no se aplique a los estilos personalizados).

Configuración del sistema de partidos
: cambia el modo oscuro automáticamente cuando el modo oscuro de macOS está activado o desactivado en todo el sistema.

Mostrar ruta completa en el título de la ventana
: Cuando está habilitado, Marcado mostrará la ruta completa al documento actual en el título de la ventana.