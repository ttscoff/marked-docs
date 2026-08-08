<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Consulte [Markdown Dingus](x-marked-3://dingus?processor=kramdown) para experimentar con el procesador Kramdown.

## ¿Qué es Kramdown? [what-is-kramdown]

Kramdown es un conversor rápido de superconjunto de Markdown puro de Ruby que amplía la sintaxis original de Markdown con características que se encuentran en otras implementaciones como Maruku, PHP Markdown Extra y Pandoc. Proporciona una sintaxis estricta con reglas definidas y al mismo tiempo mantiene la compatibilidad con la mayoría de los documentos de Markdown.

## Características clave [key-characteristics]

- **Ruby rápido y puro**: escrito íntegramente en Ruby para mayor rendimiento y portabilidad.
- **Sintaxis estricta**: proporciona reglas definidas y especificaciones claras
- **Funciones mejoradas**: incluye muchas extensiones que no se encuentran en Markdown estándar
- **Integración Jekyll**: Procesador Markdown predeterminado para el generador de sitios estáticos Jekyll
- **Completo**: admite elementos a nivel de bloque y de tramo con una amplia personalización

## Principales diferencias con el descuento estándar [major-differences-from-standard-markdown]

### 1. **Elementos mejorados a nivel de bloque** [1-enhanced-block-level-elements]

**Listas de definiciones**

- Kramdown admite listas de definiciones (no en Markdown estándar)
- Utiliza `:` para separar términos de definiciones

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tablas**

- Soporte completo de tablas con encabezados, alineación y formato.
- Más completa que la sintaxis básica de la tabla Markdown

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Bloques matemáticos**

- Soporte para expresiones matemáticas usando sintaxis LaTeX
- Soporte matemático tanto en línea como en bloque

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Marcado de texto avanzado** [2-advanced-text-markup]

**Notas a pie de página**

- Soporte completo de notas a pie de página con numeración automática.
- Notas al pie de estilo de referencia con sintaxis `[^1]`

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abreviaturas**

- Soporte para abreviaturas de estilo HTML
- Ampliación automática de abreviaturas definidas.

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Símbolos tipográficos**

- Conversión automática de caracteres tipográficos comunes.
- Comillas tipográficas, guiones, elipses, etc.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Listas de atributos y extensiones** [3-attribute-lists-and-extensions]

**Definiciones de lista de atributos (ALD)**

- Definir conjuntos de atributos reutilizables.
- Soporte para ID, clases y atributos personalizados

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Listas de atributos en línea (IAL)**

- Adjuntar atributos a elementos específicos
- Soporte tanto a nivel de bloque como a nivel de tramo

```markdown
This *is*{:.underline} some ⟦3⟧{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Extensiones**

- Sistema de extensión personalizado para funcionalidad adicional
- Extensiones integradas para comentarios y opciones.

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Compatibilidad mejorada con bloques de código** [4-enhanced-code-block-support]

**Especificación de idioma**

- Resaltado de sintaxis automático para bloques de código delimitados
- Soporte para muchos lenguajes de programación.

    ```rubí
    definitivamente hola
      pone "¡Hola mundo!"
    fin
    ```

**Bloques de código estándar**

- Manejo mejorado de bloques de código sangrados
- Mejor integración con otros elementos del bloque.

### 5. **Reglas de análisis más estrictas** [5-stricter-parsing-rules]

**Ajuste de línea**

- Soporte para contenido empaquetado (sintaxis diferida)
- Reglas claras sobre cuándo se permite el ajuste de línea
- No recomendado por motivos de legibilidad, pero admitido por motivos de compatibilidad.

**Manejo de pestañas**

- Asume tabulaciones en múltiplos de cuatro
- Las pestañas solo se permiten al comienzo de las líneas para sangría
- No debe ir precedido de espacios.

**Bloquear límites**

- Reglas claras sobre cuándo los elementos deben comenzar/terminar en los límites de los bloques.
- Comportamiento consistente entre diferentes tipos de elementos

### 6. **Soporte avanzado de enlaces e imágenes** [6-advanced-link-and-image-support]

**Enlaces automáticos**

- Detección automática de enlaces mejorada
- Mejor manejo de URL y direcciones de correo electrónico

**Enlaces de referencia**

- Procesamiento de enlaces de referencia mejorado
- Mejor resolución de conflictos para múltiples definiciones

**Atributos de imagen**

- Soporte para atributos de imagen a través de IAL
- Ancho, alto, texto alternativo y otros atributos HTML

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **Integración HTML** [7-html-integration]

**Bloques HTML**

- Mejor manejo de HTML dentro de Markdown
- Soporte para atributos y procesamiento HTML.
- Más flexible que el manejo estándar de Markdown HTML

**Extensiones HTML**

- HTML en línea con soporte de atributos
- Mejor integración con la sintaxis de Markdown

### 8. **Expresiones Matemáticas** [8-mathematical-expressions]

**Matemáticas en línea**

- `$...$` sintaxis para expresiones matemáticas en línea
- Sintaxis compatible con LaTeX

**Bloque de Matemáticas**

- `$$...$$` sintaxis para expresiones matemáticas en bloque
- Soporte para ecuaciones y fórmulas complejas.

## Kramdown frente a otros sabores de Markdown [kramdown-vs-other-markdown-flavors]

| Característica | Kramdown | Marca común (GFM) | Con sabor a GitHub | Rebajas múltiples | Estándar |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Tachado | No | Sí | No | No | No |
| Listas de tareas | No | No | Sí | Sí | No |
| Código vallado | Sí | Sí | Sí | Sí | No |
| Matemáticas | Sí | No | Sí | Sí | No |
| Notas a pie de página | Sí | Sí | Sí | Sí | No |
| Listas de definiciones | Sí | No | No | Sí | No |
| Abreviaturas | Sí | No | No | No | No |
| Listas de atributos | Sí | No | No | No | No |
| Tipografía | Sí | No | No | Sí | No |

## Ventajas clave de Kramdown [key-advantages-of-kramdown]

1. **Conjunto completo de funciones**: incluye muchas extensiones que no se encuentran en otras implementaciones
2. **Integración Jekyll**: integración perfecta con el generador de sitios estáticos Jekyll
3. **Ruby Ecosystem**: implementación de Pure Ruby con buen soporte de herramientas de Ruby
4. **Extensibilidad**: sistema de extensión personalizado para funcionalidad adicional
5. **Soporte de atributos**: sistema de atributos enriquecido para personalización de salida HTML
6. **Soporte matemático**: soporte integrado para expresiones matemáticas LaTeX
7. **Análisis estricto**: reglas de análisis claras e inequívocas

## Casos de uso comunes [common-use-cases]

**Sitios Jekyll**

- Procesador predeterminado para la generación de sitios estáticos Jekyll
- Excelente para documentación y sitios de blogs.

**Documentación técnica**

- Soporte matemático para escritura científica y técnica.
- Listas de atributos para personalización HTML avanzada

**Escritura Académica**

- Soporte de notas al pie para citas y referencias.
- Expresiones matemáticas para fórmulas y ecuaciones.

**Gestión de contenidos**

- Extensiones para funcionalidad personalizada
- Listas de atributos para metadatos y estilos.

## Recursos [resources]

- [Documentación de sintaxis de Kramdown](https://kramdown.gettalong.org/syntax.html)
- [Documentación del convertidor Kramdown](https://kramdown.gettalong.org/converter.html)
- [Guía de integración de Jekyll](https://jekyllrb.com/docs/configuration/markdown/)
- [Repositorio Kramdown GitHub](https://github.com/gettalong/kramdown)

## Migración desde Standard Markdown [migration-from-standard-markdown]

La mayoría de los documentos estándar de Markdown funcionan con Kramdown sin modificaciones. Para aprovechar las funciones de Kramdown:

1. **Agregar listas de definiciones**: convertir glosarios y listas de términos
2. **Usar listas de atributos**: agregue ID, clases y atributos personalizados
3. **Implementar notas al pie**: convertir referencias entre paréntesis

## Mejores prácticas [best-practices]

1. **Evite la sintaxis diferida**: no confíe en el formato rígido para facilitar la lectura
2. **Utilice listas de atributos**: aproveche los IAL para estilos y metadatos
3. **Sangría consistente**: use espacios en lugar de tabulaciones cuando sea posible

---

*Esta documentación cubre Kramdown 2.5.1. Para obtener la información más actualizada, consulte siempre la documentación oficial en [kramdown.gettalong.org](https://kramdown.gettalong.org/).*