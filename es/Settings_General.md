<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane General %}:

![Configuración: General][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Ventana [window]

Mantenga nuevas ventanas en la parte superior
: configura automáticamente nuevas ventanas para que "floten" sobre otras aplicaciones.

Abrir ventana al actualizar
: Cuando se detecta un cambio en un archivo observado, la ventana de vista previa de ese documento se elevará sobre otras ventanas en su escritorio sin activar Marcado.

Translúcido en el fondo
: desvanece la ventana cuando no está enfocada. Utilice el control deslizante para establecer la opacidad.

Deshabilite las funciones que consumen mucha memoria en documentos grandes
: deshabilite algunas funciones que requieren un uso intensivo del procesador, como titulares plegables, cuando los documentos superen los 100 000.

Nuevos documentos abiertos en
: Elija **ventanas**, **pestañas** o **automático** (siga la configuración del sistema macOS para tabulación). Cuando use pestañas, navegue con {% kbd cmd shift [/] %} y el [Panel de apertura rápida](Quick_Open.html).

Traer el documento actualizado al frente
: Cuando se actualiza una vista previa, seleccione su pestaña u ordene su ventana al frente **dentro de Solo marcado**. Si otra aplicación está en primer plano (por ejemplo, su editor de texto), Marked permanece en segundo plano: se selecciona la pestaña correcta para que esté lista cuando vuelva a Marked. Para mostrar la vista previa sobre todas las aplicaciones sin activar Marcado, use **Abrir ventana al actualizar** en su lugar.

Volver a centrarse en la aplicación anterior
: Cuando está habilitado, si una acción de aumento/activación de actualización hace que Marcado tome el foco en primer plano, el foco del teclado vuelve a la aplicación que estaba en primer plano antes de la actualización (como su editor de texto). Cuando está deshabilitado, Marked nunca realiza esta transferencia de enfoque. Si Marcado no pasa a estar al frente, esta opción no tiene ningún efecto.

### Barra de estado [status-bar]

Mostrar selector de estilo
: muestra el selector de estilo en la barra inferior de la ventana de vista previa.

Mostrar recuento de palabras
: muestra el recuento de palabras (y el botón de estadísticas) en la barra inferior de la ventana de vista previa.

El recuento de palabras excluye
: Los cálculos de recuento de palabras pueden ignorar cualquier combinación de:

- **Notas a pie de página/Citas**
- ** Citas en bloque **
- **Bloques de código con sangría** (los bloques de código delimitados siempre se excluyen)
- **Subtítulos de imagen**

### Atajos [shortcuts]

Haga clic en el campo de acceso directo para registrar una combinación de teclas de acceso rápido que desencadena un evento:

Activar marcado
: Cambie a Marcado cuando se presione esta tecla de acceso rápido en cualquier aplicación.

Levante la primera ventana
: eleva la ventana de vista previa marcada más frontal (la última activa) al primer plano sin salir de la aplicación actual.

Abrir paleta de acciones
: Abra la paleta de comandos [Acciones rápidas](Quick_Actions.html) mientras Marcado está activo. Este atajo se aplica a {% appmenu File, Quick Actions… %} y funciona solo dentro de Marked (no desde otras aplicaciones).

Restablecer alertas
: restaure cualquier cuadro de diálogo de alerta que haya descartado anteriormente para que pueda aparecer nuevamente.