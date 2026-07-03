# Marked Help — review handoff (es)

**Locale:** Spanish (`es`)  
**Generated:** 2026-07-02  
**Status:** Machine-translated drafts — human review required

This package is ready for post-editing. Work in the `es/` folder on a
`translate/es` (or `locale/es`) branch; open one pull request per locale.

---

## What you received

| Item | Location |
|------|----------|
| Topic pages (MT drafts) | `es/*.md` (118 files) |
| Help index metadata | `es/config.yaml` |
| Style guide | `es/SYNTAX.md` |
| Term glossary | `es/GLOSSARY.md` |
| Menu path reference | `es/APPMENU.md` |
| App UI strings (read-only reference) | `ui-strings/es-ui-review.marked-l10n` |
| Screenshot folder (optional) | `es/images/` (mirror English paths) |

- **English master:** `content/` at repo root (do not edit for locale work)
- **MT banner:** 115 pages still contain `<!-- MT-DRAFT: machine translation; human review required -->` — remove it when a page is reviewed

---

## Read first (30 minutes)

1. Root [`README.md`](../README.md) — tags, links, workflow
2. [`SYNTAX.md`](SYNTAX.md) — Spanish tone, pitfalls, checklist
3. [`GLOSSARY.md`](GLOSSARY.md) — agreed EN → Spanish terms
4. [`APPMENU.md`](APPMENU.md) — `{% appmenu %}` paths vs the localized app
5. [`ui-strings/es-ui-review.marked-l10n`](../ui-strings/es-ui-review.marked-l10n) — Settings/menus wording to match

---

## Review priorities

### Priority 1 — high-traffic pages

Fix menus and Settings terminology first, then polish prose:

- `Overview.md`, `Live_Markdown_Preview_on_Mac.md`, `Opening_Files.md`
- `Settings_General.md`, `Settings_Preview.md`, `Settings_Export.md`, `Settings_Proofing.md`
- `Keyboard_Shortcuts.md`, `Exporting.md`, `Document_Navigation.md`

### Priority 2 — `config.yaml`

Edit in place under `es/config.yaml`:

- `Title`, `MetaDescriptions`, section `title`, `folder` slugs
- Page `title`, `sidebar_title`, `description`
- `keywords` and `wiki_keywords` — rewrite for Spanish search; do not copy English phrases blindly
- **Never change** `file:` keys (English basenames) or build paths (`TargetProject`, `WebHelpBaseURL`, …)

### Priority 3 — integration pages

Editor/app pages (`VS_Code.md`, `Obsidian.md`, `Scrivener_Support.md`, …) — verify product names stay English.

### Priority 4 — spec / reference pages

Syntax spec pages (`CommonMark_Spec.md`, `Kramdown_Spec.md`, …) — keep code blocks intact; translate descriptions only.

---

## Leave unchanged

| Keep as-is | Examples |
|------------|----------|
| Topic filenames | `Exporting.md`, not translated names |
| Link targets | `Page.html`, `#anchors`, `https://…`, `x-marked-3://…` |
| Liquid tags | `{% prefspane General %}`, `{% kbd shift cmd P %}` |
| Shortcut tokens | `{{cmd}}`, `{{opt}}`, `{{shift}}` |
| `config.yaml` `file:` keys | `Overview`, `Settings_General`, … |
| Image paths in Markdown | `images/screenshots/…` |

---

## Fix carefully after MT

1. **`{% appmenu File, Export %}`** — each segment must match `MainMenu.strings` (see `APPMENU.md`)
2. **Settings panes in prose** — align with localized `Settings.strings` / `Preferences.strings`
3. **Reference links** — one `[label]: url` definition per line
4. **Syntax examples** — use Spanish demo words (`*cursiva*`, `**negrita**`) where the English source uses *italics* / **bold**
5. **`wiki_keywords`** — short phrases users might type; must not collide across pages (see root README)

---

## Suggested section order

### Empezando (`Empezando/`)

- [✓] **Descripción general** — `Overview.md`
- [✓] **Vista previa de Markdown en vivo en Mac** — `Live_Markdown_Preview_on_Mac.md`
- [✓] **Qué hay de nuevo** — `Whats_New.md`
- [✓] **Abrir archivos** — `Opening_Files.md`
- [✓] **Usando las extensiones del navegador** — `Using_the_Browser_Extensions.md`
- [✓] **Apertura rápida** — `Quick_Open.md`
- [✓] **Acciones rápidas** — `Quick_Actions.md`
- [✓] **Elegir un procesador** — `Choosing_a_Processor.md`
- [✓] **Vista previa** — `Previewing.md`
- [✓] **Características de la interfaz** — `Interface_Features.md`
- [✓] **Exportador** — `Exporting.md`

### Comparaciones y preguntas frecuentes (`Comparaciones_Preguntas frecuentes/`)

- [✓] **Vista previa marcada vs obsidiana** — `Marked_vs_Obsidian_Preview.md`
- [✓] **Preguntas frecuentes sobre la vista previa de Markdown** — `Markdown_Preview_FAQ.md`

### Funciones de lectura (`Funciones_de_lectura/`)

- [✓] **Navegación de documentos** — `Document_Navigation.md`
- [✓] **Navegación Wiki** — `Wiki_Navigation.md`
- [✓] **Descripción general de Zoom** — `Zoom_Overview.md`
- [✓] **Desplazamiento automático** — `Autoscroll.md`
- [✓] **Lectura rápida** — `Speed_Reading.md`
- [✓] **Preguntar sobre el documento** — `AI_Ask_About_Document.md`

### Funciones de escritura (`Sólo_para_escritores/`)

- [✓] **Diseño y tipografía** — `Layout_and_Typography.md`
- [✓] **Estadísticas de documentos** — `Document_Statistics.md`
- [✓] **Documentos de varios archivos** — `Multi-File_Documents.md`
- [✓] **Fuente para guionistas** — `Fountain_for_Screenwriters.md`
- [✓] **Resaltado de palabras clave** — `Keyword_Highlighting.md`
- [✓] **Ortografía y Gramática** — `Spelling_Grammar.md`
- [✓] **Marcado crítico** — `CriticMarkup.md`
- [✓] **MatemáticasJax** — `MathJax.md`
- [—] **Trabajar con DOCX** — `Working_with_DOCX.md`
- [✓] **Exportación HTML** — `HTML_Export.md`
- [✓] **Exportación EPUB** — `EPUB_Export.md`
- [✓] **Soporte RTF y RTFD** — `RTF_Support.md`
- [✓] **Importación y exportación de PDF** — `PDF_Support.md`
- [✓] **Variantes de imagen** — `Image_Variants.md`
- [✓] **Validación de enlace** — `Link_Validation.md`
- [✓] **Comentarios y anotaciones** — `Comments_and_Annotations.md`
- [✓] **Funciones para codificadores** — `Features_For_Coders.md`
- [✓] **Uso de marcado con codificación agente** — `Using_Marked_with_Agentic_Coding.md`

### Aplicaciones compatibles (`Aplicaciones_compatibles/`)

- [✓] **Oso** — `Bear.md`
- [✓] **Curiosidad** — `Curio.md`
- [✓] **DEVONpensar** — `DEVONthink.md`
- [✓] **Damas** — `Drafts.md`
- [✓] **Vigilancia de carpetas** — `Folder_Watching.md`
- [✓] **Tierras altas** — `Highland.md`
- [✓] **marca de gancho** — `Hookmark.md`
- [✓] **yo un escritor** — `iA_Writer.md`
- [✓] **iPensamientosX** — `iThoughtsX.md`
- [✓] **Marte** — `MarsEdit.md`
- [✓] **Nodo mental** — `MindNode.md`
- [✓] **Compositor MultiMarkdown** — `MultiMarkdown_Composer.md`
- [✓] **nvUltra** — `nvUltra.md`
- [✓] **Obsidiana** — `Obsidian.md`
- [✓] **OmniOutliner y OPML** — `OmniOutliner_and_OPML.md`
- [✓] **Soporte de Escribano 3** — `Scrivener_Support.md`
- [✓] **El Archivo** — `The_Archive.md`
- [✓] **Ulises** — `Ulysses.md`
- [✓] **Empuje** — `Vim.md`
- [✓] **Código VS** — `VS_Code.md`
- [✓] **VudúPad** — `VoodooPad.md`
- [✓] **Parques infantiles Xcode** — `Xcode_Playgrounds.md`
- [✓] **Soporte DocC** — `DocC_Support.md`
- [✓] **Integraciones de aplicaciones adicionales** — `Additional_Application_Support.md`

### Funciones avanzadas (`Características_especiales/`)

- [✓] **Estilos personalizados** — `Custom_Styles.md`
- [✓] **Crear estilos personalizados** — `Writing_Custom_CSS.md`
- [✓] **Generador de estilos personalizados** — `Custom_Style_Generator.md`
- [✓] **Administrador de estilo** — `Style_Manager.md`
- [✓] **Ladrón de estilo** — `Style_Stealer.md`
- [✓] **Rebajador** — `Markdownifier.md`
- [✓] **Procesador personalizado** — `Custom_Processor.md`
- [✓] **Restricciones de la zona de pruebas** — `Sandbox_Restrictions.md`
- [✓] **Configuración por documento** — `Per-Document_Settings.md`
- [✓] **Sintaxis especial marcada** — `Special_Syntax.md`
- [✓] **Crear tablas usando archivos CSV** — `Creating_Tables_using_CSV_files.md`
- [✓] **Incrustar mapas mentales y esquemas** — `Embedding_Mind_Maps_and_Outlines.md`
- [✓] **Atajos de teclado** — `Keyboard_Shortcuts.md`
- [✓] **Integración del flujo de trabajo** — `Workflow_Integration.md`
- [✓] **Controlador de URL** — `URL_Handler.md`
- [✓] **Soporte AppleScript** — `AppleScript_Support.md`
- [✓] **Utilidad de línea de comando** — `Command_Line_Utility.md`
- [✓] **Vista previa de transmisión** — `Streaming_Preview.md`
- [✓] **Configuraciones específicas de HTML** — `HTML_Specific_Settings.md`
- [✓] **Incrustar JavaScript** — `Embedding_Scripts.md`
- [—] **Documentos de la API de JavaScript** — `.md`

### Ajustes (`Ajustes/`)

- [✓] **Configuración: General** — `Settings_General.md`
- [✓] **Configuración: Vista previa** — `Settings_Preview.md`
- [✓] **Configuración: Estilo** — `Settings_Style.md`
- [✓] **Configuración: Procesador** — `Settings_Processor.md`
- [✓] **Configuración: Aplicaciones** — `Settings_Apps.md`
- [✓] **Configuración: revisión** — `Settings_Proofing.md`
- [✓] **Configuración: Exportar** — `Settings_Export.md`
- [✓] **Configuración: Avanzada** — `Settings_Advanced.md`

### Solución de problemas (`Solución de problemas/`)

- [✓] **Vista previa no actualizada** — `Preview_doesn_t_update_when_file_is_saved.md`
- [✓] **Rendimiento general** — `Overall_Performance.md`
- [✓] **Depuración** — `Troubleshooting.md`
- [✓] **Ayuda adicional** — `Additional_Help.md`

### Acerca de las rebajas (`Acerca de_Markdown/`)

- [✓] **Selección del procesador** — `Processor_Selection.md`
- [✓] **Descripción general de rebajas** — `Markdown_Tutorial.md`
- [✓] **Dingus de rebajas** — `Markdown_Dingus.md`
- [✓] **Especificación de MultiMarkdown v5** — `MultiMarkdown_v5_Spec.md`
- [✓] **Especificación de marca común** — `CommonMark_Spec.md`
- [✓] **Especificación de Kramdown** — `Kramdown_Spec.md`
- [✓] **Especificación GFM de descuento** — `Discount_GFM_Spec.md`

### Créditos (`Créditos/`)

- [✓] **Créditos** — `Credits.md`
- [✓] **Licencia MultiMarkdown** — `MultiMarkdown_License.md`
- [✓] **Licencia de descuento** — `Discount_License.md`
- [✓] **Licencia Kramdown** — `Kramdown_License.md`
- [✓] **Licencia de marca común** — `CommonMark_License.md`
- [✓] **Licencia pdf22md** — `PDF22MD_License.md`

---

## Before you open a PR

- [ ] `{% appmenu %}` paths checked against the localized Marked app
- [ ] Terms match `GLOSSARY.md`; new recurring terms added there
- [ ] `config.yaml` keywords/wiki_keywords reviewed for this locale
- [ ] Link targets and `{% … %}` tags unchanged
- [ ] MT banner removed from pages you finished reviewing
- [ ] Branch contains **only** `es/` (and `ui-strings/` if UI wording changed)

Mention **@ttscoff** in the PR if you also edited `ui-strings/` (app string merge is separate from help).

---

## Maintainer commands (reference)

```bash
python3 HelpDocs/content/scripts/bootstrap_locales.py es
python3 HelpDocs/content/scripts/machine_translate_help.py --locale es
python3 HelpDocs/content/scripts/generate_help_review_handoff.py es
```
