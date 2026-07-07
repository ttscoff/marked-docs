# Glossary: French (fr)

Agreed translations for recurring terms. The lead translator maintains this file; contributors should follow it consistently.

**Status:** Filled in from the official app localization (`fr-ui-review.marked-l10n`) where a match exists. Updated with terms confirmed while reviewing AI_Ask_About_Document.md, Scroll_to_Edit.md, Settings_Advanced.md, and Settings_Apps.md.

| English | Translation | Notes |
|---------|-------------|-------|
| Marked | Marked | Product name, unchanged |
| Markdown | Markdown | Kept as loanword, per app convention |
| preview | aperçu | Confirmed in app (menu items 295/296) |
| export | exporter / export | "Exporter sous" for the export command; "export" as a noun stays close to English in prose |
| Settings | Paramètres | Confirmed: window.title = "Paramètres" (note: older strings still say "Réglages…", app is transitioning terminology; use "Paramètres" going forward) |
| gear menu | menu Action | Confirmed: kbs.action.gearMenu = "Menu Action" (not a literal "gear" translation) |
| processor | processeur | Confirmed: "Processor" = "Processeur" |
| style / theme | style / thème | Both used in the app depending on context; "style" for named preview styles, "thème" for syntax/theme settings (e.g. "Thème pour la coloration syntaxique") |
| proofing | relecture | Confirmed: Pix-Cz-p0c.title = "Relecture" |
| Table of Contents | table des matières | Confirmed, multiple entries |
| bookmark | signet | Confirmed: "Bookmarking" = "Mise en signet" |
| Mini Map | mini-carte | Confirmed, lowercase with hyphen as used in-app |
| Quick Actions | Actions rapides | Confirmed |
| Quick Open | Ouverture rapide | Confirmed |
| Custom Processor | processeur personnalisé | Confirmed: "Chemin du processeur personnalisé" |
| Custom Rules | Règles personnalisées | Confirmed |
| clipboard preview | aperçu du presse-papiers | Confirmed |
| streaming preview | aperçu en continu | Confirmed |
| keyboard shortcut | raccourci clavier | Confirmed |
| syntax highlighting | coloration syntaxique | Confirmed |
| CriticMarkup | CriticMarkup | Usually unchanged |
| MultiMarkdown | MultiMarkdown | Usually unchanged |
| CommonMark | CommonMark | Usually unchanged |
| Scrivener | Scrivener | App name, unchanged |
| Obsidian | Obsidian | App name, unchanged |
| tag | balise | Confirmed: "#Text is tag" = "#Le texte est une balise", "Style tags" = "Balises de style". Do not use "tag" in prose, including section headings. |
| Ask About Document | Poser des questions sur le document | Confirmed: app string "Ask About Document" = "Poser des questions sur le document"; menu form "Ask About Document…" = "Poser des questions sur le document…" |
| Summarize Document | Résumer le document | Confirmed |
| Summarize Selection | Résumer la sélection | Confirmed |
| Outline (AI panel action) | Plan | Confirmed; not "Plan hiérarchique" despite the descriptive prose using that phrase |
| Key Points | Points clés | Confirmed |
| Ask (button) | Demander | Confirmed |
| Cancel (button) | Annuler | Confirmed |
| System Settings (macOS app, not Marked's own Settings) | Réglages Système | Apple's current French name for the macOS System Settings app, distinct from the "Settings"/"Paramètres" entry above, which refers to Marked's own preferences window |
| Mermaid | Mermaid | Diagramming library (mermaid.js.org). Never translate; confirmed mistranslation seen twice as "Sirène" (the mythical creature). Also used as a Marked setting name: "Intégrer les cartes en tant que diagrammes Mermaid". |
| Hooks | Hooks | Marked's JavaScript API for re-running scripts on preview update (`Marked.hooks.register()`). Keep in English, singular "hook" or plural "hooks" as in source; do not translate to "crochets". |
| Scroll to Edit | défilement vers la modification | Confirmed while translating Scroll_to_Edit.md; used descriptively in prose, not as a fixed UI label |
| preferences pane / prefspane | panneau de préférences | Descriptive phrase used in prose around the `{% prefspane %}` tag (tag itself stays unchanged, see "Do not translate") |
| Find (system-wide search) | recherche | Used for the macOS-wide Find pasteboard feature, not the app's own search UI |
| Find pasteboard | presse-papiers de recherche du système | Confirmed while translating Settings_Advanced.md |
| Debug mode | Mode débogage | Confirmed while translating Settings_Advanced.md |
| Settings Backup | Sauvegarde des paramètres | Aligned with "Settings" = "Paramètres" entry above |
| Text Editor (preference label) | Éditeur de texte | Confirmed while translating Settings_Apps.md |
| Image Editor (preference label) | Éditeur d'images | Confirmed while translating Settings_Apps.md |
| Image annotation/markup editor | Éditeur d'annotation/de balisage d'images | Confirmed while translating Settings_Apps.md |
| Change tracking | suivi des modifications | Word-related feature; standard French term |
| Mind Maps/Outlines | Cartes mentales/Plans | Section heading in Settings_Apps.md |
| tidy-tree layout | disposition en arbre ordonné | Describes Mermaid mind map layout |
| Folders (preference section) | Dossiers | Settings_Apps.md section heading |
| Border (header/footer rule) | Bordure | Confirmed while reviewing Settings_Export.md MT draft; corrects a "Frontière" mistranslation (false friend), consistent with "les bordures" already used in the section's intro paragraph |
| Full Disk Access | Accès complet au disque | Confirmed: official Apple French term for the macOS permission |
| Reading Speed (wpm) | Vitesse de lecture (mpm) | Settings_Proofing.md; "mpm" = mots par minute, French equivalent of "wpm" |
| Avoid (keyword list) | Éviter | Settings_Proofing.md keyword tab label |
| Use Alternate (keyword list) | Utiliser une alternative | Settings_Proofing.md keyword tab label |
| Highlight (keyword list) | Mettre en évidence | Settings_Proofing.md keyword tab label |
| Ignore Repeats (keyword list) | Ignorer les répétitions | Settings_Proofing.md keyword tab label |
| widow (typography) | veuve | Settings_Style.md; standard French typographic term ("veuves et orphelins") |
| Style Manager | Gestionnaire de styles | Settings_Style.md |
| Outline mode | mode Plan | Settings_Style.md; "Outline" here refers to the outline/heading numbering mode, capitalized as a feature name |
| transient preview | aperçu temporaire | Share_Extension.md; unsaved preview from pasted/shared text, distinct from "clipboard preview" (aperçu du presse-papiers) and "streaming preview" (aperçu en continu) |
| Share extension (macOS) | extension de partage | Share_Extension.md |
| Share menu (macOS) | menu Partager | Share_Extension.md |
| Login Items & Extensions (macOS System Settings pane) | Éléments de connexion et extensions | Share_Extension.md; macOS system pane name |
| Shortcuts (Apple app) | Raccourcis | Shortcuts_Integration.md; official Apple French app name |
| App Intents | App Intents | Apple developer framework name; kept in English like "Hooks" |
| Quick Action (Finder feature) | Action rapide | Shortcuts_Integration.md; distinct from Marked's own "Quick Actions" feature (Actions rapides), but same French term applies and is disambiguated by context |
| callout | callout | Special_Syntax.md; kept as English loanword per Obsidian/Bear French community convention, unlike "tag" which has an established French term (balise) |
| Autoscroll | Défilement automatique | Confirmed |
| Teleprompter (style name) | Teleprompter | Special_Syntax.md; proper noun of a named preview style, kept unchanged like other named styles (e.g. Amblin, Grump) |
| Text (Ulysses export format dropdown) | Texte | Confirmed by user, Ulysses.md |
| Open In (Ulysses/macOS share sheet action) | Ouvrir dans | Confirmed by user as a generic macOS share-sheet term; note that this specific button no longer appears in current Ulysses UI (superseded by "Open With Marked", see below) |
| Open With Marked (Ulysses export menu) | Ouvrir avec Marked | Confirmed by user, Ulysses.md; current Ulysses UI action (accessed via the ··· button next to Export), replaces the older "Open In" flow described in the original English doc |
| Markdownify URL (browser extension button) | Markdownifier l'URL | Confirmed by user, Using_the_Browser_Extensions.md |
| Markdownify Selection (browser extension button) | Markdownifier la sélection | Confirmed by user, Using_the_Browser_Extensions.md |

## Do not translate (keep English)

- File names and code identifiers
- `{% prefspane General %}`, `{% kbd cmd S %}`, `{{cmd}}`, etc.
- URL schemes: `x-marked-3://`
- Version numbers and build metadata

## Ambiguous terms

Document choices that affect multiple pages:

| English | Chosen translation | Avoid (reason) |
|---------|-------------------|----------------|
| Settings | Paramètres | Avoid "Réglages" in new content: the app's newer strings use "Paramètres" (window.title), but many legacy menu strings still say "Réglages…" (e.g. "129.title"). The app itself is inconsistent; docs should standardize on "Paramètres" and not carry the older term forward. Caught and corrected in Settings_Advanced.md and Settings_Apps.md, which had initially used "Réglages". |
| tag | balise | Avoid "tag": confirmed app terminology is "balise" (see main table). Caught during Bear.md review where both a heading and body text used "tags" inconsistently with the app. |
| export (verb vs noun) | exporter (verb) / export (noun, when natural) | Avoid forcing "exportation" everywhere; the app itself mixes "Exporter sous" (verb form) with more technical noun uses like "Profil d'exportation." Match the app's pattern per context rather than picking one form globally. |
