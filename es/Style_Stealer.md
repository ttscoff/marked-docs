<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Extrae y roba estilos de cualquier sitio web.

## ¿Qué es el ladrón de estilos?

Style Stealer es una herramienta que le permite extraer estilos CSS de cualquier sitio web y aplicarlos a sus documentos Markdown como [Estilos personalizados](Custom_Styles.html). Es perfecto para:

- **Blogueros** que quieran combinar el estilo de sus sitios web favoritos
- **Escritores** que necesitan crear documentos que coincidan con una marca o publicación específica
- **Desarrolladores** que quieran crear prototipos rápidamente con sistemas de diseño existentes.
- **Cualquier persona** que quiera capturar la apariencia de cualquier sitio web bien diseñado.

> Style Stealer depende de que un sitio esté relativamente bien diseñado con divisiones de marcado claras. No funcionará en todos los sitios, pero debería funcionar bien en la mayoría.

> Para obtener mejores resultados, ingrese a una página que contenga la mayor cantidad de texto posible. Por ejemplo, para extraer estilos de un blog, ábralo directamente en un artículo o publicación, no en la página de índice principal.

## Cómo utilizar el ladrón de estilos

### Paso 1: abre el ladrón de estilos

Acceda a Style Stealer a través de **Ayuda** → **Style Stealer**.

### Paso 2: Ingrese una URL

En el campo URL, ingrese la dirección del sitio web del que desea extraer estilos. Style Stealer funciona con cualquier sitio web de acceso público. Si el sitio está detrás de un muro de pago, es posible que tengas que iniciar sesión para poder extraer el contenido.

![Vista previa de Style Stealer][vista previa]

  [vista previa]: imágenes/estilo-roba-vista previa.jpg @2x width=800

### Paso 3: cargar y navegar

Haga clic en **Extraer** o presione {% kbd return  %} para cargar el sitio web. Una vez cargado, puedes:

- **Navega** por el sitio usando Comando+Haga clic en los enlaces
- **Pase el cursor** sobre las áreas de contenido para verlas resaltadas.
- **Haga clic** en el área de contenido principal de la que desea extraer estilos.

El área de contenido principal que seleccione solo debe contener titulares, párrafos, listas, etc. No seleccione un área de contenido que contenga menús, barras laterales u otro contenido superfluo. A menudo, un título estará en un contenedor separado del contenido del párrafo normal. En estos casos, primero intente seleccionar el contenedor más pequeño que aún contenga ambos. Si los resultados son deficientes, haga clic en **Extraer** nuevamente y vuelva a seleccionar solo el contenedor que contiene los párrafos.

### Paso 4: Extraer estilos

Al hacer clic en el área de contenido, se extraerán los estilos que se aplican a esa área. La vista previa se recargará con una página genérica que muestra todos los elementos HTML comunes y cómo se aplicarán a ellos los estilos extraídos.

Luego puede guardar este estilo personalizado en su carpeta CSS personalizado para usarlo en cualquier documento. Haga clic en el botón **Guardar** o presione {% kbd cmd S %} para guardar. El estilo recibirá un nombre según el dominio de la URL que ingresó.

![][img3]

  [img3]: imágenes/ladrón de estilos-robados-800.jpg @2x width=800px height=637px class=center

## Qué se extrae

Style Stealer captura un conjunto completo de estilos que incluyen:

### Tipografía

- **Familias de fuentes** y tamaños para todos los niveles de encabezado (H1-H6)
- Estilo de **párrafo** que incluye altura y espaciado de línea
- **Colores de texto** y colores de fondo
- **Pesos de fuente** y estilos (negrita, cursiva, etc.)

### Diseño y espaciado

- **Márgenes y relleno** para todos los elementos
- **Borde** estilos y colores
- **Colores de fondo** incluidos fondos del cuerpo para temas oscuros

### Elementos interactivos

- **Estilos de enlace** incluidos los estados de desplazamiento y visitado
- **Botón** y estilo de elemento de formulario
- Estilo **Lista** (viñetas, números, sangría)

### Características especiales

- Estilo del **primer párrafo**
- Formato **Cita en bloque**
- **Código** y estilo de texto preformateado
- Estilo **Tabla**
- **Fuentes personalizadas** y fuentes web

## Funciones avanzadas

### Bloqueo de medios

Style Stealer bloquea automáticamente el contenido multimedia (vídeos, imágenes, audio) para evitar fallos y centrarse en el estilo del texto. Esto garantiza un proceso de extracción fluido incluso en sitios web con muchos medios.

### Soporte de pseudoselector

La herramienta captura pseudoselectores CSS como:

- `:hover` estados para enlaces y botones
- `:visited` estados de enlace
- `:first-child` estilo de párrafo
- `::first-letter` para mayúsculas

### Filtrado inteligente

Style Stealer filtra inteligentemente:

- Estilos de navegador predeterminados
- Prefijos de proveedores innecesarios
- Normas contradictorias o redundantes
- Estilos que harían que el texto fuera ilegible.

### Modo de depuración

Habilite el modo de depuración en Style Stealer para ver el registro detallado del proceso de extracción. Esto es útil para solucionar problemas o comprender qué estilos se están capturando.

## Consejos para obtener mejores resultados

### Elija el área de contenido adecuada

- Haga clic en el **área de contenido principal** de la página, no en los encabezados, barras laterales ni pies de página.
- Busque el área que contiene el texto del artículo, la publicación del blog o el contenido principal.
- Evite áreas con JavaScript pesado o contenido dinámico

### Manejar temas oscuros

Style Stealer captura automáticamente los colores de fondo del cuerpo, lo que lo hace perfecto para extraer estilos de temas oscuros. La vista previa mostrará cómo se ve su contenido con el estilo oscuro extraído.

### Consideraciones de fuentes

- Las **fuentes web** se capturan y se incluyen en los estilos extraídos.
  - Las fuentes que se cargan desde una URL remota (por ejemplo, Google Fonts) mantendrán esa URL. Las fuentes cargadas desde las URL de datos se duplicarán en la hoja de estilo generada.
- **Fuentes del sistema** recurrirán elegantemente a diferentes sistemas
- **La carga de fuentes** puede tardar un momento en la vista previa

### Probando tus estilos

Después de guardar los estilos extraídos:

1. Aplicarlos a un documento de prueba.
2. Comprueba cómo se ven con tu contenido real.
3. Realice ajustes mediante:
   1. Abra el {% prefspane Style %}
   2. Seleccione el nuevo estilo en la tabla Estilos personalizados.
   3. Haga clic en Revelar para mostrar el archivo en Finder.
   4. Abra el archivo en cualquier editor de texto sin formato (TextEdit funcionará en modo de texto sin formato) y realice los ajustes necesarios

## Solución de problemas

### El sitio web no se carga

- Verifique que la URL sea correcta y de acceso público
- Algunos sitios pueden bloquear el acceso automatizado
- Pruebe con una página diferente en el mismo sitio

### Los estilos se ven diferentes

- Los estilos extraídos se basan en el contenido específico que seleccionó
- Algunos sitios utilizan CSS complejo que puede no traducirse perfectamente
- Utilice CSS adicional o edite la hoja de estilo para realizar ajustes finos

### Estilos faltantes

- Asegúrate de haber seleccionado el área de contenido principal, no una barra lateral o un encabezado.
- Algunos estilos pueden aplicarse a través de JavaScript y no serán capturados
- Consulte la consola de depuración para obtener información detallada sobre la extracción.

## Atajos de teclado

- {% kbd return  %} - Cargar URL para extracción
- {% kbd cmd S %} - Guarde el estilo extraído en un archivo CSS de estilo personalizado
- {% kbd cmd  %}-Clic: navega por los enlaces mientras obtienes una vista previa

## Integración con estilos personalizados

Los estilos extraídos se guardan en su carpeta CSS personalizado y pueden ser:

- **Aplicado** a cualquier documento a través del menú Estilo
- **Modificado** usando cualquier editor de texto
- **Compartido** con otros copiando el archivo CSS
- **Combinado** con otros estilos personalizados

Style Stealer facilita la creación de una biblioteca de hermosos estilos inspirados en los sitios web mejor diseñados de Internet.