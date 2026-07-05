# Glossary: French (fr)

Agreed translations for recurring terms. The lead translator maintains this file; contributors should follow it consistently.

**Status:** Filled in from the official app localization (`fr-ui-review.marked-l10n`) where a match exists. Updated with terms confirmed while reviewing AI_Ask_About_Document.md.

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

## Do not translate (keep English)

- File names and code identifiers
- `{% prefspane General %}`, `{% kbd cmd S %}`, `{{cmd}}`, etc.
- URL schemes: `x-marked-3://`
- Version numbers and build metadata

## Ambiguous terms

Document choices that affect multiple pages:

| English | Chosen translation | Avoid (reason) |
|---------|-------------------|----------------|
| Settings | Paramètres | Avoid "Réglages" in new content: the app's newer strings use "Paramètres" (window.title), but many legacy menu strings still say "Réglages…" (e.g. "129.title"). The app itself is inconsistent; docs should standardize on "Paramètres" and not carry the older term forward. |
| tag | balise | Avoid "tag": confirmed app terminology is "balise" (see main table). Caught during Bear.md review where both a heading and body text used "tags" inconsistently with the app. |
| export (verb vs noun) | exporter (verb) / export (noun, when natural) | Avoid forcing "exportation" everywhere; the app itself mixes "Exporter sous" (verb form) with more technical noun uses like "Profil d'exportation." Match the app's pattern per context rather than picking one form globally. |
