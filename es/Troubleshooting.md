<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

### Modo de depuración [debug-mode]

Puede habilitar el registro de depuración abriendo {% prefspane Advanced %} y marcando la casilla **Modo de depuración** en la parte inferior del panel. Esto mostrará un menú desplegable donde puede configurar el nivel de registro que desea ver:

- **Solo errores**: solo se registrarán errores graves
- **Errores y advertencias**: muestra además advertencias menos urgentes
- **Todos**: muestra errores, advertencias y mensajes de depuración a nivel de información. Esta es la configuración recomendada para solucionar problemas.

{% note %}
TODO: ¿Esto todavía funciona?
También puede acceder a estas opciones manteniendo presionada la tecla {% kbd opt  %} al abrir {% appmenu Help %} en la barra de menú.
{% endnote %}

### Ver el registro [viewing-the-log]

Con el **Modo de depuración** habilitado, puede abrir el menú {% appmenu Help %} y seleccionar Abrir registro de depuración. Esto abrirá el registro de Marked en Console.app, que se actualizará en vivo a medida que se agreguen mensajes de registro mientras se usa Marked.

### Solución de problemas de reglas personalizadas [troubleshooting-custom-rules]

[Preprocesadores y procesadores personalizados](Custom_Processor.html) obtienen su propia interfaz de registro. Seleccione {% appmenu Help, Show Custom Rules Log %} para abrir la ventana. Esta ventana mostrará un registro coloreado que muestra qué reglas coincidieron y qué comandos ejecutan.

### Informar de un problema [reporting-an-issue]

Utilice {% appmenu Help, Report an Issue %} para abrir una ventana que muestre la configuración de las claves más comunes y una plantilla para crear un informe de error. Utilice el botón "Copiar al portapapeles" para copiar el contenido de la ventana y haga clic en "Abrir sitio de soporte" para abrir [el formulario de nueva pregunta](https://support.markedapp.com/questions/add) donde puede pegar su informe. Intento responder a los informes dentro de las 48 horas.