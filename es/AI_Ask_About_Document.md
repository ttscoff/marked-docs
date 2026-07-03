<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Pregunte sobre el documento utiliza **Apple Intelligence** y el modelo de lenguaje del dispositivo integrado en versiones recientes de macOS para resumir su vista previa de Markdown y responder preguntas sobre su contenido. Todo el procesamiento ocurre en tu Mac; El texto del documento no se envía a los servidores de Marked ni a los servicios de inteligencia artificial de terceros para esta función.

## Qué proporciona Apple Intelligence

Apple Intelligence es el sistema de Apple para funciones generativas en el dispositivo. Marked utiliza el marco **Foundation Models** de Apple para acceder al mismo modelo en el dispositivo que impulsa las herramientas de escritura del sistema, expuesto directamente dentro de Marked para tareas centradas en documentos.

Marked envía el texto sin formato de su documento (la sintaxis de Markdown se elimina para mayor claridad) a este modelo local. El modelo genera resúmenes, esquemas y respuestas en un panel flotante al lado de la ventana de vista previa. Debido a que el modelo se ejecuta localmente, funciona sin conexión una vez que Apple Intelligence está configurado y el modelo del sistema ha terminado de descargarse.

Apple Intelligence es mejor en tareas lingüísticas como resumir, esquematizar, extraer puntos clave y responder preguntas sobre el texto proporcionado. No es un asistente de codificación ni una calculadora general, y los documentos muy extensos se manejan en secciones para que los resultados se mantengan dentro de los límites del contexto del modelo.

## Compatibilidad del sistema

Preguntar sobre el documento aparece solo cuando su Mac puede ejecutar la función.

**Requerido:**

- **macOS 26 (Tahoe)** o posterior
- Una **Mac compatible con Apple Intelligence** (Macs Apple Silicon que cumplen con los requisitos de dispositivos de Apple)
- **Apple Intelligence activada** en Configuración del sistema

**No compatible:**

- Intel Mac y otros Mac marcados como no elegibles para Apple Intelligence
- Versiones de macOS anteriores a Tahoe 26
- **Vistas previas HTML** sin procesar (la característica es para Markdown y flujos de trabajo de documentos basados en texto)

Si su Mac califica pero falta el elemento del menú, confirme que Apple Intelligence esté habilitado y que esté ejecutando una versión actual de Marked que incluya esta función. El menú está completamente oculto en sistemas no compatibles en lugar de mostrarse en un estado deshabilitado.

## Habilitando la inteligencia de Apple

1. Abra **Configuración del sistema**.
2. Vaya a **Apple Intelligence y Siri** (o **Apple Intelligence**, según su versión de macOS).
3. Active **Apple Intelligence** y complete los pasos de configuración que Apple solicite.
4. Espere a que el modelo del dispositivo termine de descargarse si se le solicita. Hasta que el modelo esté listo, Marked puede mostrar el elemento del menú pero mostrar un mensaje de que Apple Intelligence aún se está preparando.

Marcado no incluye una preferencia separada para esta característica. La disponibilidad sigue el estado del modelo del sistema informado por macOS.

## Abrir documento de pregunta sobre

Abra el panel usando cualquiera de estos métodos:

- **Vista previa > Preguntar sobre el documento…**
- Método abreviado de teclado {% kbd shift ctrl cmd I %} (mientras un documento de vista previa de Markdown es la ventana activa)

El panel se acopla al lado izquierdo de la ventana del documento. Necesita un documento abierto con texto legible; un documento vacío o una vista previa de solo HTML no ofrecerán el comando.

## El panel Preguntar sobre el documento

El panel está organizado como una simple vista de chat:

- **Acciones preestablecidas** en la parte superior para tareas comunes
- Un **área de respuesta** en el medio donde aparecen resúmenes y respuestas (transmitiendo a medida que se generan)
- Un **campo de preguntas** en la parte inferior donde puedes escribir preguntas personalizadas, con botones **Preguntar** y **Cancelar**

Una vez completada una respuesta, el foco vuelve al campo de preguntas para que pueda realizar un seguimiento sin hacer clic.

### Acciones preestablecidas

| Acción | Qué hace |
| :-- | :-- |
| **Resumir documento** | Produce un breve resumen coherente del documento completo. Los documentos extensos se resumen en secciones y se combinan. |
| **Resumir selección** | Resume solo el texto actualmente seleccionado en la vista previa. Seleccione el texto primero; de lo contrario, Marcado le solicita que haga una selección o utilice Resumir documento. |
| **Esquema** | Crea un esquema jerárquico de la estructura del documento utilizando títulos y viñetas. |
| **Puntos clave** | Enumera los puntos más importantes del documento como una lista con viñetas. |

Las acciones preestablecidas no requieren texto en el campo de pregunta. Haga clic en un botón y espere la respuesta en el panel de arriba.

### Haciendo tus propias preguntas

1. Escriba una pregunta en el campo en la parte inferior del panel, por ejemplo "¿Qué problema resuelve este documento?" o "¿Quién es el público objetivo?"
2. Presione **Volver** o haga clic en **Preguntar**.
3. Lea la respuesta a medida que llega al área de respuestas.

Si tiene preguntas sobre un pasaje específico, **seleccione ese texto en la vista previa** antes de preguntar. Marcado envía la selección como contexto en lugar de todo el documento cuando una selección está activa.

Haga clic en **Cancelar** para detener una solicitud en curso.

## Ejemplos

### Descripción rápida de un artículo extenso

Abra una publicación de blog extensa o un informe en Marcado, elija **Vista previa > Preguntar sobre el documento...** y haga clic en **Resumir documento**. Utilice el resumen para decidir si leer el artículo completo o refrescar su memoria después de un tiempo sin leer el borrador.

### Notas sobre un párrafo seleccionado

Resalte un párrafo denso en la vista previa, abra Preguntar sobre el documento y haga clic en **Resumir selección**. Útil cuando solo necesitas una versión más corta de una sección.

### Revisión estructural

Haga clic en **Esquema** en un borrador con muchos títulos para ver si el argumento fluye de manera lógica, o use **Puntos clave** antes de enviar un documento a otra persona para verificar que las ideas principales estén claras.

### Preguntas específicas

Sin ninguna selección activa, escriba preguntas como:

- "¿Cuáles son las tres recomendaciones principales?"
- "¿Este documento menciona la concesión de licencias?"
- "Indique las fechas o plazos mencionados".

Con una selección activa, haga preguntas más específicas como "¿Qué supone este párrafo sobre el lector?" o "Reescribe esta idea en una frase" (el modelo responde sobre la selección; no edita tu archivo fuente).

## Consejos y limitaciones

- **Privacidad:** El procesamiento utiliza el modelo en el dispositivo de Apple. Marked todavía lee el texto de su documento localmente para proporcionar contenido a ese modelo; trate el material sensible en consecuencia.
- **Precisión:** Verifique hechos importantes con su fuente. Los resúmenes de IA pueden omitir detalles o malinterpretar pasajes ambiguos.
- **Longitud:** Los documentos extremadamente largos se procesan en trozos. Los resúmenes y las respuestas reflejan indirectamente el texto completo; Para mayor precisión en una sección, seleccione esa sección primero.
- **Idioma:** Los resultados siguen las capacidades de idioma del modelo del sistema Apple Intelligence en su Mac.
- **Rechazos:** El sistema puede rechazar algunas solicitudes según las políticas de seguridad de Apple.

Si Preguntar sobre el documento no está disponible, verifique la Configuración del sistema para conocer el estado de Apple Intelligence y asegúrese de obtener una vista previa de un documento de Markdown en una Mac compatible con macOS 26 o posterior.