<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Consulte [Markdown Dingus](x-marked-3://dingus?processor=commonmark) para experimentar con el procesador CommonMark (GFM).


## ¿Qué es CommonMark? [what-is-commonmark]

CommonMark es una implementación altamente compatible y fuertemente especificada de Markdown. Fue creado para abordar las ambigüedades e inconsistencias en la especificación Markdown original de John Gruber, lo que llevó a implementaciones divergentes en diferentes plataformas y herramientas.

## Por qué existe CommonMark [why-commonmark-exists]

La especificación Markdown original de John Gruber era intencionalmente ambigua en muchas áreas, lo que llevó a diferentes interpretaciones por parte de varias implementaciones. Esto creó problemas en los que el mismo documento Markdown se representaba de manera diferente en diferentes plataformas (GitHub, StackOverflow, Reddit, etc.).

CommonMark proporciona:

- **Especificaciones inequívocas** para toda la sintaxis de Markdown
- **Suite de pruebas integral** para garantizar un comportamiento consistente
- **Reglas de precedencia claras** para sintaxis conflictiva
- **Algoritmo de análisis detallado** que se puede implementar de forma coherente

## Diferencias clave con respecto al descuento estándar [key-differences-from-standard-markdown]

### 1. **Reglas de análisis más estrictas** [1-stricter-parsing-rules]

CommonMark impone un comportamiento de análisis más consistente:

**Líneas en blanco antes de los elementos del bloque**

- CommonMark requiere líneas en blanco antes de títulos, citas en bloque y listas
- Markdown estándar a menudo permite esto sin líneas en blanco.

```markdown
Text
# Heading
```

*CommonMark: Requiere una línea en blanco antes del título*

*Rebaja estándar: a menudo se permite sin línea en blanco*

### 2. **Análisis de elementos de lista** [2-list-item-parsing]

**Requisitos de sangría**

- CommonMark tiene reglas específicas para la sangría de elementos de lista
- Las sublistas deben tener una sangría consistente (normalmente 4 espacios)
- Las implementaciones estándar de Markdown varían en este sentido.

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Continuación de la lista**

- CommonMark tiene reglas claras para determinar cuándo los elementos de la lista son "flexibles" o "estrictos".
- Las listas sueltas envuelven elementos en etiquetas `<p>`, las listas ajustadas no

### 3. **Manejo de bloques de código** [3-code-block-handling]

**Bloques de código cercados**

- CommonMark estandariza la sintaxis de bloques de código delimitados con comillas invertidas o tildes
- Requiere marcadores de sangría y cierre consistentes


    ```lenguaje
    código aquí
    ```


**Bloques de código con sangría**

- CommonMark requiere líneas en blanco antes de los bloques de código con sangría
- Markdown estándar a menudo los permite sin líneas en blanco.

### 4. **Procesamiento de enlaces e imágenes** [4-link-and-image-processing]

**Precedencia del enlace de referencia**

- CommonMark tiene reglas claras para las cuales la definición de referencia tiene prioridad
- Múltiples definiciones para la misma referencia se manejan de manera consistente

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Orden de análisis de enlaces**

- CommonMark procesa los enlaces antes del énfasis.
- Esto afecta cómo se interpreta la sintaxis anidada.

### 5. **Énfasis y fuerte énfasis** [5-emphasis-and-strong-emphasis]

**Reglas de énfasis anidadas**

- CommonMark tiene algoritmos específicos para manejar marcadores anidados `*` y `_`
- Evita el análisis ambiguo de patrones de énfasis complejos

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Procesamiento delimitador**

- CommonMark utiliza un algoritmo de "pila delimitadora" para un análisis de énfasis consistente
- Las implementaciones estándar de Markdown varían en su enfoque.

### 6. **Procesamiento de bloques HTML** [6-html-block-processing]

**Detección de bloques HTML**

- CommonMark tiene 7 tipos diferentes de bloques HTML con reglas específicas
- Cada tipo tiene diferentes requisitos para las condiciones de inicio/finalización.

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Manejo de saltos de línea** [7-line-break-handling]

**Saltos de línea duros**

- CommonMark requiere dos espacios al final de la línea para pausas difíciles
- Los saltos de línea simples se convierten en saltos suaves (ignorados en HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Referencias de entidades y personajes** [8-entity-and-character-references]

**Referencias de caracteres numéricos**

- CommonMark admite referencias numéricas decimales y hexadecimales
- El soporte estándar de Markdown varía

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## Algoritmo de análisis de CommonMark [commonmark-parsing-algorithm]

CommonMark utiliza un enfoque de análisis de dos fases:

### Fase 1: Estructura de bloques [phase-1-block-structure]

1. **Procesamiento de línea**: cada línea se analiza en busca de marcadores a nivel de bloque.
2. **Bloques de contenedores**: se identifican citas en bloque, listas y otros contenedores.
3. **Bloques de hojas**: se procesan títulos, bloques de código y párrafos.
4. **Enlaces de referencia**: las definiciones de enlaces se recopilan para su uso posterior

### Fase 2: Estructura en línea [phase-2-inline-structure]

1. **Procesamiento en línea**: el texto dentro de los bloques se analiza en busca de elementos en línea
2. **Análisis de énfasis**: utiliza un algoritmo de pila de delimitadores para un énfasis consistente
3. **Resolución de enlaces**: los enlaces de referencia se resuelven utilizando definiciones recopiladas.
4. **Procesamiento de entidades**: las referencias de caracteres se convierten en caracteres reales

## Beneficios de CommonMark [benefits-of-commonmark]

1. **Comportamiento predecible**: la misma entrada siempre produce la misma salida
2. **Compatibilidad multiplataforma**: funciona de manera consistente en diferentes herramientas
3. **Pruebas integrales**: un amplio conjunto de pruebas garantiza la confiabilidad
4. **Documentación clara**: las especificaciones detalladas eliminan las conjeturas
5. **A prueba de futuro**: puntos de extensión bien definidos para nuevas funciones

## Notas de implementación [implementation-notes]

CommonMark está diseñado para ser:

- **Cumple con las especificaciones**: sigue exactamente la especificación oficial de CommonMark
- **Basado en pruebas**: pasa el conjunto de pruebas oficial CommonMark
- **Extensible**: se puede ampliar con funciones adicionales manteniendo la compatibilidad
- **Rápido**: algoritmos de análisis optimizados para el rendimiento

## Recursos [resources]

- [Especificación de marca común](https://spec.commonmark.org/0.31.2/)
- [Suite de pruebas CommonMark](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Herramienta de prueba en línea
- [Foro de discusión de CommonMark](https://talk.commonmark.org/)

---

*Esta documentación cubre CommonMark 0.31.2 (2024-01-28). Para obtener la información más actualizada, consulte siempre la especificación oficial.*