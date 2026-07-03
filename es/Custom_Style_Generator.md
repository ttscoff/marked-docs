<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

El Generador de estilos personalizados es una herramienta basada en web que le permite crear estilos personalizados para Marked sin escribir CSS a mano. Proporciona una interfaz visual con controles de tipografía, colores, espaciado y más, con una vista previa en vivo que se actualiza a medida que realiza cambios.

## Accediendo al generador

El Generador de estilos está disponible en [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). Puede usarlo directamente en su navegador web, no requiere instalación.

![Generador de estilos][img-style-generator]

  [img-style-generator]: imágenes/style-generator-800.jpg @2x ancho=800 clase=centro

## Empezando

Cuando abras el generador por primera vez, verás:

- **Panel de vista previa** (izquierda): una vista previa en vivo de su estilo aplicado al contenido de rebajas de muestra
- **Panel de controles** (derecha): todos los controles de estilo organizados en secciones
- **Barra de herramientas** (arriba): título de estilo, selector de tema base y opción de importación de CSS

### Elegir un tema base

Comience seleccionando un **Tema base** del menú desplegable. Esto proporciona una base para su estilo; luego puede personalizar cada aspecto del mismo. Las opciones populares incluyen En blanco (para empezar desde cero), Predeterminado y varios temas integrados.

### Importación de CSS existente

Si tiene un archivo CSS existente que le gustaría usar como punto de partida, haga clic en **Importar CSS** y seleccione su archivo. El generador cargará esos estilos y luego podrás modificarlos usando los controles.

## Controles de estilo

El generador organiza los controles en secciones lógicas:

### Tipografía básica

Controle la configuración de tipografía fundamental:

- **Usar ritmo**: cuando está habilitado, utiliza una escala tipográfica matemática para tamaños y espacios de encabezado consistentes.
- **Tamaño de fuente base**: el tamaño de fuente raíz (normalmente 16 píxeles)
- **Altura de línea**: el espacio entre líneas de texto
- **Relación de escala**: la relación utilizada para la escala tipográfica (afecta el tamaño de los títulos)

### Diseño

Ajustar el espaciado y la sangría:

- **Relleno envolvente**: espacio alrededor del área de contenido
- **Sangría de párrafo**: sangría de primera línea para párrafos
- **Sangría de lista**: sangría para listas
- **Sangría de cita en bloque**: margen izquierdo para citas en bloque

### Fuentes

Configure familias de fuentes y pesos:

- **Fuentes de encabezado**: lista de fuentes separadas por comas para los encabezados (por ejemplo, "Georgia, serif")
- **Fuentes del cuerpo**: lista de fuentes separadas por comas para el cuerpo del texto
- **Peso del encabezado**: Peso de fuente para los títulos (100–900)
- **Peso del cuerpo**: Peso de fuente para el texto del cuerpo
- **Peso en negrita**: peso de fuente para texto en negrita
- **Espaciado entre letras**: espaciado entre caracteres para encabezados y cuerpo de texto

### Fuentes de Google

Añade Google Fonts a tu estilo:

1. Escriba un nombre de fuente en el campo de búsqueda (aparecen sugerencias de autocompletar)
2. Opcionalmente, especifique estilos (por ejemplo, "400,400i,700" para regular, cursiva y negrita)
3. Haga clic en **Agregar** para incluirlo.
4. Utilice **Buscar fuentes de Google** para explorar el catálogo completo con vistas previas.

Las fuentes agregadas aparecen en una lista debajo de los controles; haga clic en × para eliminarlas.

### Colores

Establecer colores para varios elementos:

- **Fondo**: color de fondo de la página
- **Texto base**: color de texto predeterminado
- **Color del encabezado**: color para todos los títulos (se puede anular según el nivel del encabezado)
- **Color del cuerpo**: color del texto del cuerpo
- **Color del enlace**: Color de los enlaces
- **Color de énfasis**: Color para texto enfatizado (`<em>`)
- **Color fuerte**: Color para texto fuerte (`<strong>`)
- **Fondo de marca**: color de fondo para el texto resaltado (`<mark>`)

Los colores de encabezado individuales (H1–H6) se pueden configurar por separado; use **Restablecer** para borrar una anulación y volver al color del encabezado.

### Modo oscuro

Active el **Modo oscuro** para obtener una vista previa y configurar los colores del modo oscuro. Cuando esté habilitado, verá controles de color separados para las variantes del modo oscuro. Los estilos del modo oscuro se aplican cuando `.inverted` está configurado en el elemento del cuerpo en Marcado.

Utilice **Generar colores** para crear automáticamente una paleta de modo oscuro basada en los colores de su modo claro.

### Imágenes

Controlar la apariencia de la imagen:

- **Ancho máximo**: ancho máximo para imágenes (por ejemplo, "100%", "800px")
- **Radio del borde**: esquinas redondeadas (por ejemplo, "8px", "0")
- **Alineación**: documento predeterminado, izquierda, centro o derecha

### Citas en bloque

Citas en bloque de estilo:

- **Ancho del borde izquierdo**: Grosor del borde izquierdo
- **Color del borde izquierdo**: Color del borde izquierdo
- **Color de fondo**: color de fondo para citas en bloque
- **Estilo de fuente**: Normal o cursiva
- **Margen izquierdo**: espaciado desde el borde izquierdo
- **Margen izquierdo anidado**: espaciado para citas en bloque anidadas (puede ser "heredado")

Hay controles separados disponibles para citas en bloque en modo oscuro.

### Listas

Configurar la apariencia de la lista:

- **Posición del estilo de lista**: Interior o Exterior (donde aparecen viñetas/números)
- **Margen izquierdo**: espaciado desde el borde izquierdo
- **Margen izquierdo anidado**: espaciado para listas anidadas (puede ser "heredado")

### Listas de definiciones

Listas de definiciones de estilo (`<dl>`, `<dt>`, `<dd>`):

- **DL Indent**: sangría general
- Configuración **DT** (término): tamaño, peso y estilo de fuente
- Configuración de **DD** (definición): tamaño de fuente, peso, estilo y sangría

### Tablas

Estilo completo de mesa:

- **Color de fondo**: fondo de la tabla
- **Color del borde**: color del borde de las celdas
- **Color del texto de la tabla**: color de texto predeterminado en las tablas
- **Alternancia de filas/columnas**: habilite rayas de cebra con colores personalizados
- **Borde**: Mostrar/ocultar el esquema de la tabla
- **Cuadrícula**: Mostrar/ocultar líneas de cuadrícula internas
- **Alineación**: izquierda o centro
- **Radio del borde**: Esquinas redondeadas
- **Ancho máximo**: ancho máximo de la mesa
- **Relleno de celda**: espaciado interno
- Configuración de **Encabezado**: peso, tamaño y estilo de fuente
- Configuración de **Subtítulos**: peso, tamaño, estilo y color del texto de la fuente

Hay controles separados disponibles para tablas en modo oscuro.

### Bloques de código

Bloques de código de estilo y código en línea:

- **Familia de fuentes de código**: pila de fuentes monoespaciadas
- **Fondo**: color de fondo
- **Color del borde**: color del borde
- **Radio del borde**: Esquinas redondeadas
- **Modo de envoltura**: Sin envoltura (pre-envoltura), Conservar + envoltura (pre-envoltura) o Normal (envoltura)
- **Relleno de código**: espaciado interno

Hay controles separados disponibles para bloques de código en modo oscuro.

### Notas al pie

Notas a pie de página de estilo:

- **Color del marcador**: color de los marcadores de notas al pie
- **Color del texto**: color del texto de la nota al pie
- **Estilo de fuente del texto**: Normal o cursiva

Hay controles separados disponibles para las notas a pie de página en modo oscuro.

### Sombra paralela

Agregue sombras paralelas a los elementos:

1. Elija sombra **Fuerza**: Suave, Media o Fuerte
2. Seleccione a qué elementos aplicar sombras:
   - Imágenes
   - Bloques de código
   - Citas en bloque
   - Mesas

## CSS personalizado

Para una personalización avanzada más allá de los controles disponibles, use el botón **CSS personalizado** para abrir un editor de código. Cualquier CSS que agregue aquí se agregará al estilo generado y se ajustará automáticamente para que funcione dentro de la estructura del documento de Marked.

El editor incluye resaltado y validación de sintaxis: los CSS no válidos se marcarán con mensajes de error.

## Vista previa en vivo

El panel de vista previa muestra su estilo aplicado al contenido de rebajas de muestra, que incluye:

- Títulos (H1–H6)
- Párrafos con varios formatos en línea
- Mesas
- Bloques de código
- Imágenes
- Listas (ordenadas y desordenadas)
- Citas en bloque
- Listas de definiciones
- Notas a pie de página
- Listas de tareas

Los cambios se actualizan en tiempo real a medida que ajustas los controles.

## Guardar y compartir

Una vez que esté satisfecho con su estilo, tiene varias opciones:

### Ver CSS

Haga clic en **Ver CSS** para ver el CSS generado completo en una ventana emergente. Puedes copiarlo a tu portapapeles o revisarlo antes de guardarlo.

### Guardar CSS

Haga clic en **Guardar CSS** para descargar su estilo como un archivo CSS. Se le pedirá que ingrese metadatos (título, autor, descripción) antes de descargar.

### Agregar a marcado

Haga clic en **Agregar a Marked** para agregar directamente el estilo a su instalación de Marked. Esto requiere que Marked se esté ejecutando y se abrirá un cuadro de diálogo para confirmar el nombre del estilo y la información del autor.

### Compartir estilo

Haga clic en **Compartir estilo** para publicar su estilo en la [Galería de estilos marcados](https://markedapp.com/styles) para que otros lo utilicen. Deberá proporcionar:

- Título de estilo
- Tu nombre
- URL del autor (opcional)
- Descripción
- Nota (opcional)

Aparecerá una vista previa de su estilo en el cuadro de diálogo para compartir antes de publicarlo.

## Metadatos

Utilice la sección de metadatos (ampliable mediante el botón de flecha junto al título del estilo) para configurar:

- **Autor**: su nombre (persiste en todas las sesiones)
- **URL del autor**: la URL de su sitio web o perfil
- **Descripción**: una descripción del estilo.
- **Nota**: Notas adicionales (no incluidas en estilos compartidos)

Estos metadatos se incluyen en el encabezado del archivo CSS y se utilizan al compartir estilos.

## Consejos

- Comience con un tema base cercano a lo que desea y luego personalícelo
- Utilice el tema **En blanco** si desea un control total desde cero
- Habilite **Ritmo** para una tipografía matemáticamente consistente
- Pon a prueba tu estilo con el interruptor **Modo oscuro** si planeas admitirlo
- Utilice **CSS personalizado** con moderación: la mayoría de las necesidades se pueden satisfacer con los controles integrados
- Obtenga una vista previa de su estilo con varios tipos de contenido antes de compartirlo

## Compatibilidad del navegador

El Generador de estilos funciona mejor en navegadores modernos (Chrome, Firefox, Safari, Edge). Requiere que JavaScript esté habilitado.