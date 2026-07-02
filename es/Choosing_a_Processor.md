<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked puede obtener una vista previa del mismo archivo con varios procesadores Markdown integrados. Cada uno hace diferentes concesiones entre **flujo de trabajo de escritura** (libros, blogs, archivos README de GitHub) y **control de salida** (ID, clases, metadatos). Eliges el valor predeterminado en {% prefspane Processor %}; También puede anular el procesador por documento.

Esta página resume en qué se diferencian los cuatro procesadores principales. Para obtener detalles completos de sintaxis, consulte las páginas de referencia en **Ayuda → Referencia de Markdown** (por ejemplo, [Especificación MultiMarkdown v5](MultiMarkdown_v5_Spec.html), [Especificación Kramdown](Kramdown_Spec.html), [Especificación CommonMark](CommonMark_Spec.html), [Especificación GFM de descuento](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5)

**Ideal para:** prosa larga, escritura académica o técnica y cualquier cosa que dependa de **metadatos**, **citas** y características **específicas de MultiMarkdown**.

Marked se envía con **MultiMarkdown 5** (consulte la [Guía del usuario de MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/) para obtener la documentación original).

### Fortalezas

- **Documentos narrativos y con muchas referencias:** Las notas a pie de página, la bibliografía/citas y las tablas son de primera clase.
- **Metadatos:** bloques de metadatos estándar de MultiMarkdown (`Key: Value` encabezados) más **transclusión** y otras comodidades de MMD descritas en la guía v5.
- **Sustitución de metadatos:** Las claves de los metadatos se pueden insertar en el cuerpo con un reemplazo de estilo `[%key]` para que los títulos, las cadenas de autor y los valores similares permanezcan sincronizados con el encabezado.
- **Tablas, imágenes y referencias cruzadas:** Alineadas con las características documentadas para MultiMarkdown 5.

### ID y encabezados manuales

- Los ID de encabezado están **normalizados** de una manera que tiende a producir barras **minúsculas y concatenadas** (sin espacios, las palabras van juntas).
- Para **ID de encabezado manuales**, MultiMarkdown usa el formulario: `## Headline Text [my-id]` (el identificador entre corchetes después del texto del encabezado).

### Cuándo elegir otra cosa

Si necesita listas de tareas **con sabor a GitHub** y el comportamiento exacto del analizador actual de GitHub, prefiera **CommonMark (GFM)**. Si necesita **clases/ID HTML detallados** en elementos arbitrarios, considere **Kramdown**.

---

## Kramdown

**Mejor para:** Documentos en los que desea **control preciso sobre la salida HTML**: **clases**, **ID** y atributos personalizados, para que su CSS pueda apuntar a bloques y tramos específicos.

La [referencia de sintaxis de kramdown](https://kramdown.gettalong.org/syntax.html) es la guía autorizada.

### Fortalezas

- **Mayormente compatible** con hábitos de estilo MultiMarkdown para Markdown cotidiano, al tiempo que agrega sus propias extensiones.
- **Listas de atributos en línea y en bloque (IAL):** Adjunte `{: #id .class key="value"}` a párrafos, encabezados, bloques de código, enlaces, imágenes y más: ideal para sitios estilo Jekyll y hojas de estilo personalizadas.
- **ID de encabezado:** kramdown normaliza los ID de encabezado generados automáticamente a palabras **en minúsculas y separadas por guiones** (por ejemplo, `my-section-title`). Para **identificaciones manuales**, utilice el formulario `{#id}` después del texto del título, p. Setext: `My Section {#my-section}` luego el subrayado, o ATX: `# My Section {#my-section}` (consulte los [encabezados] de kramdown (https://kramdown.gettalong.org/syntax.html#headers) para conocer la ubicación exacta y las reglas IAL).
- **Listas de definiciones, notas a pie de página, tipografía inteligente, bloques matemáticos:** Conjunto de funciones enriquecido para publicaciones en proceso que necesitan más que Markdown "simple".

### Cuándo elegir otra cosa

Si depende de la sustitución de metadatos **solo de MultiMarkdown** (`[%key]`) o de flujos de trabajo de citas específicos de MMD, **MultiMarkdown** puede ser una mejor opción. Para **README y documentos de repositorio** que deben coincidir con GitHub en línea, **CommonMark (GFM)** suele estar más cerca.

---

## CommonMark (Marca con sabor a GitHub / cmak-gfm)

**Mejor para:** **archivos LÉAME**, **descripciones de problemas/PR** y **documentación del proyecto** que deben coincidir lo más posible con el **comportamiento actual de Markdown** de GitHub.

Marked utiliza un motor orientado a **GFM** (cmark-gfm). La especificación formal es la [Especificación de Markdown con sabor a GitHub](https://github.github.com/gfm/), construida sobre [CommonMark](https://commonmark.org/).

### Fortalezas

- **Coincidencia más cercana a GitHub:** Las tablas, los tachados, los elementos de la lista de tareas, los bloques de código delimitados con etiquetas de idioma y los enlaces automáticos se comportan como la representación moderna de GitHub.
- **Análisis inequívoco:** CommonMark define la precedencia de bloque/en línea y las reglas de lista con precisión; es más estricto en algunos casos extremos que el comportamiento "clásico" de Markdown.pl, pero **más predecible** una vez que aprende las reglas.
- **Práctico para texto ajustado:** Las reglas de párrafos y listas están diseñadas para funcionar bien con prosa ajustada (consulte las secciones de especificaciones sobre listas y continuaciones diferidas).

### ID de encabezado

Los anclajes de encabezado generados automáticamente suelen estar **en minúsculas y separados por guiones**, lo que es consistente con el slugging común al estilo de GitHub.

### Cuándo elegir otra cosa

GFM no replica los flujos de trabajo de **metadatos MultiMarkdown**, **Kramdown IAL** o **MMD citation**. Para libros, tesis o metadatos pesados, utilice **MultiMarkdown** o **Kramdown** según corresponda.

---

## Descuento

**Mejor para:** Un procesador **rápido, basado en C** que rastrea el **Mardown clásico** y un conjunto de funciones **más antiguo con sabor a GitHub**: útil cuando desea un comportamiento más cercano al **Mardown original** además de tablas, notas al pie y extensiones relacionadas sin el libro de reglas completo de CommonMark.

Inicio del proyecto: [Descuento](https://www.pell.portland.or.us/~orc/Code/discount/).

### Fortalezas

- **Tablas de estilo PHP Markdown Extra** y muchas extensiones (notas a pie de página, código delimitado cuando está habilitado, etc. --- consulte la [Especificación GFM de descuento](Discount_GFM_Spec.html) de Marked para conocer lo que Marked habilita).
- **Extras opcionales de "GitHub"** en el descuento ascendente (por ejemplo, listas de casillas de verificación cuando se crean con las banderas correctas); Marcado documenta la combinación que envía en la página de especificaciones de descuento.
- **Tipografía estilo SmartyPants** y otras comodidades descritas en el sitio de descuentos (aunque todos los procesadores incluidos en realidad ofrecen funciones de tipografía).
- Filosóficamente cercano a **John Gruber's Markdown** más extensiones prácticas, en lugar del conjunto de pruebas completo de CommonMark.

### Cuándo elegir otra cosa

Para **paridad perfecta de píxeles con el github.com actual**, prefiera **CommonMark (GFM)**. Para **metadatos y citas de MultiMarkdown**, utilice **MultiMarkdown**.

---

## Comparación rápida

| Preocupación | Rebajas múltiples | Kramdown | Marca común (GFM) | Descuento |
|--------|---------------|--------|------------|----------|
| **Uso principal** | Prosa, artículos, libros | HTML con estilo, sitios tipo Jekyll | LÉAME, documentos similares a GitHub | Extensiones MD + clásicas |
| **Citas/metadatos MMD** | Fuerte | A través de una sintaxis diferente | No | No |
| **Estilo de identificación de encabezado manual** | `## Title [id]` | `## Title {: #id }` (IAL) | Reglas de slug de especificaciones/GitHub | Ninguno |
| **ID de rumbo automático** | Minúsculas concatenadas | Minúsculas con guión | Minúsculas con guión | Con guión en minúsculas |
| **Atributos adicionales (clases/ids)** | Mecanismos MMD limitados | **IAL** — muy fuertes | Limitado | Limitado |

---

## Ver también

- [Configuración: Procesador](Settings_Processor.html) — procesador predeterminado y opciones relacionadas
- [Markdown Dingus](Markdown_Dingus.html): prueba los procesadores uno al lado del otro en Marked
- [Procesador personalizado](Custom_Processor.html): conecta tu propia cadena de herramientas cuando sea necesario