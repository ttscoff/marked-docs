<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Quick Open proporciona acceso rápido a sus documentos abiertos y archivos recientes.

## Apertura Apertura rápida [opening-quick-open]

Acceda al panel de apertura rápida usando {% kbd shift cmd O %} o desde el menú {% appmenu File, Quick Open %}. El panel aparece como una ventana flotante sobre su documento actual, lo que le permite cambiar rápidamente entre documentos abiertos o abrir archivos recientes.

![Panel de apertura rápida][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Secciones del documento [document-sections]

El panel de apertura rápida organiza los documentos en secciones claras:

### Abrir documentos [open-documents]

En la parte superior de la lista, verá todos los documentos abiertos actualmente. Los documentos se agrupan visualmente por su ventana:

- **Ventanas con pestañas**: los documentos en ventanas con pestañas muestran "Ventana con pestañas X" como subtítulo, lo que indica cuántas pestañas hay en ese grupo de ventanas.
- **Windows independiente**: los documentos en ventanas individuales muestran "Ventana" como subtítulo

Cada documento abierto muestra:
- El nombre del archivo del documento como título principal.
- La ventana que agrupa la información como subtítulo.
- Un icono de documento

### Documentos recientes [recent-documents]

Debajo de los documentos abiertos, un separador de "Documentos recientes" divide la lista. La sección de documentos recientes muestra hasta 10 de los archivos abiertos más recientemente que no están abiertos actualmente. Cada documento reciente muestra:

- El nombre del archivo del documento como título principal.
- "Reciente" como subtítulo
- Un icono de documento

### Abrir otro [open-other]

En la parte inferior de la lista, la opción "Abrir otro..." le permite abrir el selector de archivos estándar de macOS para seleccionar cualquier archivo. Esta opción muestra:

- "Abrir Otro..." como título principal
- "Abrir un archivo o carpeta" como subtítulo
- Un icono de carpeta

## Buscar y filtrar [search-and-filter]

Escriba en el campo de búsqueda en la parte superior del panel para filtrar la lista en tiempo real. La búsqueda coincide con:

- Nombres de archivos de documentos
- Rutas completas de archivos

A medida que escribe, la lista se actualiza inmediatamente para mostrar solo los documentos coincidentes. La opción "Abrir otro..." siempre permanece visible en la parte inferior de los resultados filtrados.

## Navegación por teclado [keyboard-navigation]

Navegue por el panel de apertura rápida completamente con su teclado:

- ** ↑/↓ Teclas de flecha **: moverse hacia arriba y hacia abajo por la lista
- **Volver**: Abre el documento u opción seleccionada
- **Escape**: cierra el panel de apertura rápida
- **Comando (⌘)**: manténgalo presionado para revelar las rutas de los archivos (ver más abajo)

## Ver rutas de archivos [viewing-file-paths]

Mantenga presionada la tecla **Comando (⌘)** mientras el panel de apertura rápida está abierto para ver la ruta completa del archivo de cada documento en el área de subtítulos. Las rutas en su directorio de inicio se muestran usando la abreviatura `~` (por ejemplo, `~/Documents/file.md`). Suelta la tecla Comando para volver a la vista normal que muestra la agrupación de ventanas o la información "Reciente".

Esto es particularmente útil cuando tiene varios archivos abiertos con el mismo nombre o cuando necesita verificar la ubicación exacta de un documento.

## Documentos de apertura [opening-documents]

- **Documentos abiertos**: al seleccionar un documento abierto, su ventana pasa al primer plano y cambia a la pestaña de ese documento si está en una ventana con pestañas.
- **Documentos recientes**: al seleccionar un documento reciente, se abre en una nueva ventana o se agrega como una pestaña (dependiendo de su preferencia "Abrir documentos en pestañas" en {% prefspane General %})
- **Abrir Otro...**: Al seleccionar esta opción se abre el cuadro de diálogo estándar del selector de archivos de macOS.