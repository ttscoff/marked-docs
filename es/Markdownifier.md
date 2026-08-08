<!-- MT-DRAFT: machine translation; human review required -->

# Rebajador [markdownifier]

Markdownifier es una herramienta que extrae automáticamente contenido de páginas web y lo convierte a un formato Markdown limpio. Procesa de forma inteligente el contenido web para brindarle solo el texto y la estructura significativos, filtrando anuncios, elementos de navegación y otros elementos innecesarios.

![URL de Markdownify][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Cómo funciona [how-it-works]

Markdownifier utiliza algoritmos avanzados de extracción de contenido para:

1. **Buscar y analizar** el contenido de la página web
2. **Identifique el texto y la estructura del artículo principal**
3. **Limpiar y formatear** el contenido en Markdown adecuado
4. **Filtrar** anuncios, navegación y otros elementos que no sean contenido
5. **Conserve** formatos importantes como encabezados, listas y enlaces

## Abrir el Markdownifier [opening-the-markdownifier]

Para acceder al Markdownifier, abra {% appmenu File, New, Markdownify URL (@~k) %}. Ingrese la URL que desea Markdownify y presione Retorno ({% kbd return %}).

## Usando el Markdownifier [using-the-markdownifier]

### Uso básico [basic-usage]

1. **Abra Markdownifier** usando cualquiera de los métodos anteriores
2. **Ingrese una URL** en el campo de texto
3. **Haga clic en "Automático"** o presione `Return` para extraer el contenido
4. El contenido extraído se **abrirá automáticamente** en un nuevo documento marcado.

### Selección manual de contenido [manual-content-selection]

Si la extracción automática no captura el contenido que desea:

1. Haga clic en el botón **"Manual"** para cargar la página en una vista web.
2. **Navega y desplázate** para encontrar el contenido que deseas
3. **Haga clic en el botón "Extraer contenido"** que aparece sobre la página web.
4. El contenido seleccionado se convertirá a Markdown y se abrirá en Marked.

### Integración del portapapeles [clipboard-integration]

Markdownifier detecta automáticamente las URL en su portapapeles cuando se abre:

- Si se encuentra una URL, estará **precompletada** en el campo URL
- Aún debes hacer clic en **"Automático"** o presionar `Return` para procesarlo
- Esto evita el procesamiento accidental de las URL del portapapeles.

## Procesamiento de contenido [content-processing]

### Validación automática de contenido [automatic-content-validation]

Markdownifier valida de forma inteligente el contenido extraído para garantizar que contenga texto significativo:

- **Metadatos de tiras** (frontmatter YAML, encabezados MultiMarkdown)
- **Elimina definiciones de enlaces** y enlaces de estilo de referencia
- **Filtra** URL independientes y elementos de navegación
- **Comprime espacios en blanco** para una evaluación precisa de la longitud
- **Requiere un mínimo de 200 caracteres** de contenido real

Si el contenido extraído es demasiado corto o parece ser principalmente navegación/anuncios, Markdownifier volverá automáticamente al modo de selección manual.

### Formato de contenido [content-formatting]

El contenido extraído tiene el formato Markdown limpio con:

- **Enlace fuente** en la parte superior: `[source](original-url)`
- **Inserción de título H1** cuando sea necesario
- **Listas conservadas** (ordenadas y desordenadas)
- **Enlaces mantenidos** y formato de énfasis
- **Párrafos limpios** con el espacio adecuado

## Funciones de seguridad [safety-features]

### Prevención de accidentes [crash-prevention]

Markdownifier incluye varias medidas de seguridad para evitar accidentes:

- **Bloquea URL problemáticas** (redes publicitarias, servicios de seguimiento, contenido relacionado con criptografía)
- **Filtra imágenes corruptas** que podrían causar problemas de renderizado
- **Desactiva funciones web avanzadas** que podrían causar inestabilidad
- **Recuperación automática de fallas** con respaldo en modo seguro

### Protección de la privacidad [privacy-protection]

- **Modo de navegación privada** evita el seguimiento y las cookies
- **Sin complementos ni ejecución de Java** por seguridad
- **JavaScript limitado** con bloqueo de API criptográfica
- **Filtrado de recursos** bloquea el seguimiento y el contenido publicitario

## Solución de problemas [troubleshooting]

### Contenido no extraído [content-not-extracted]

Si falla la extracción automática:

1. **Pruebe la selección manual** usando el botón "Manual"
2. **Compruebe si el sitio requiere JavaScript**: algunos sitios necesitan carga manual
3. **Verifique que la URL** sea accesible y contenga el contenido del artículo.
4. **Busque muros de pago o requisitos de inicio de sesión** que puedan bloquear el acceso

### Problemas con WebView [webview-issues]

Si la vista web se vuelve inestable:

1. Markdownifier **entrará automáticamente en modo seguro**
2. **JavaScript estará deshabilitado** para evitar fallas
3. **Utilice el botón "Convertir"** en lugar de la selección manual
4. **Cierre y vuelva a abrir** Markdownifier para restablecerlo

### Contenido faltante [missing-content]

Si falta contenido importante en la extracción:

1. Es posible que el **algoritmo automático** lo haya filtrado
2. **Usa la selección manual** para elegir el contenido específico que deseas
3. **Verifique el HTML fuente** para ver si el contenido se carga dinámicamente
4. **Pruebe con una URL diferente** si el sitio tiene una estructura compleja

## Consejos para obtener mejores resultados [tips-for-best-results]

### Selección de URL [url-selection]

- **Utilice las URL de los artículos** en lugar de las páginas de inicio o de categorías.
- **Evite las URL con parámetros de seguimiento** cuando sea posible

### Calidad del contenido [content-quality]

- **Los artículos más largos** generalmente se extraen mejor que las publicaciones cortas.
- **Contenido bien estructurado** con títulos adecuados funciona mejor
- **Evite sitios con JavaScript pesado** para la extracción automática

### Selección manual [manual-selection]

- **Espere a que la página se cargue por completo** antes de extraer
- **Desplácese por el contenido** para asegurarse de que todo esté cargado
- **Pase el cursor sobre las áreas** para seleccionar el cuadro azul más pequeño que contiene todo el contenido que desea extraer
- **Haz clic** cuando hayas encontrado el contenido que deseas

## Funciones avanzadas [advanced-features]

### Procesamiento por lotes [batch-processing]

Mientras Markdownifier procesa una URL a la vez, usted puede:

- **Pone en cola varias URL** abriendo Markdownifier varias veces
- **Utilice la integración de servicios** para procesar URL de otras aplicaciones
- **Copiar contenido extraído** y pegarlo en documentos marcados existentes

### Integración con marcado [integration-with-marked]

El contenido extraído se abre en Marcado con:

- **Nombramiento automático de archivos** según el título del artículo
- **Preservación de la URL de origen** en los metadatos del documento
- **Capacidades completas marcadas** para leer y exportar)

## Detalles técnicos [technical-details]

### Tipos de contenido admitidos [supported-content-types]

- **Artículos HTML** con marcado estándar
- **Publicaciones de blog** y artículos de noticias
- **Documentación** y páginas de ayuda
- **Publicaciones en foros** y contenido de debates

### Limitaciones [limitations]

- **Los sitios de pago** pueden requerir inicio de sesión y extracción manual
- **Los sitios con mucho JavaScript** pueden requerir una selección manual
- Es posible que se pierda el **contenido dinámico** cargado después de cargar la página, pero la extracción manual puede capturarlo
- **Diseños complejos** pueden incluir elementos de navegación no deseados

Markdownifier está diseñado para hacer que la extracción de contenido web sea lo más simple y confiable posible, al tiempo que brinda opciones alternativas para sitios web complejos o problemáticos.