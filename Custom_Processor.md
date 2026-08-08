# <%= @title %>


Marked gives you full control with Custom Rules, text
transforms, and the ability to run your own commands or run
different processors based on matching file properties.


## Using Custom Preprocessors/Processors [using-custom-preprocessorsprocessors]

To add Custom Processors, go to the {% prefspane Processor %}
and click on **Custom Rules**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=100%


In the Rules Editor (AKA "Conductor"), you can add custom
rules that have criteria to match files based on filename,
path, matches in the content, metadata, and even whether
other files exist in the same tree as the document being
opened. When a rule is matched, the actions defined for the
rule are run on that file.

![Rules Editor][2]

[2]: images/CustomRules-800.jpg @2x width=800

To create a new rule, use the `+`
button at the bottom of the left-hand rules list. Give the
rule a name and set it as a preprocessor or a processor.

The three dots next to a rule indicate Prerocessor, Processor, and Enabled. Only one of Preprocessor or Processor can be highlighted, and you can click on dots to change the rule's states.

Preprocessor
: Runs after the file is initially processed, when Marked adds included files, handles style preferences like GitHub newlines, etc., but before the processing phase. The document is still raw Markdown at this point and you can make changes to the content to pass to the processor. If no Custom Processor matches, or no Run Processor action is run in a matched Custom Processor, then the default processor will be run.

Processor
: A Custom Processor replaces the built-in processor defined in the {% prefspane Processor %}. It can handle all of the actions that a Preprocessor can, and adds Run Command and Run Processor actions. This allows you to run a custom command, e.g. Pandoc, or run a different built-in processor on files matching the criteria.

All tables in the Custom Rules editor can be reordered by
dragging and dropping, so you can affect the order in which
rules are run, the order of the criteria in the predicate
editor, and the order of actions to be run in sequence.

### Predicate Editor [predicate-editor]

![Predicate Editor][predicate]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=548

Once a rule is added, use the predicate editor to define
criteria that will determine whether the rule is run for a
given file. Use the left side dropdown to select a
criterion, then use the comparator and value fields to build
the predicate.

- _Filename_ matches just the filename of the file
- _Extension_ matches just the extension of the file
- _Path_ matches the full POSIX (Unix) path of the file
- _Tree_ searches for filename matches anywhere in the
  directory tree of the file
- _Text_ matches text content in the file. Use forward
  slashes around the text value to make it a regular
  expression search.
- _File includes_ tests whether the file contains included
  files (using any of [Marked's include
  syntaxes](Multi-File_Documents.html)).
- _Metadata type_ tests whether the file includes YAML,
  MultiMarkdown, or Pandoc metadata
- _Metadata:_ fields (for example _Metadata: Author_,
  _Metadata: Date_, _Metadata: Title_) test for specific
  metadata keys. Any metadata key appears in the dropdown as
  _Metadata:_ followed by the field name.
- _Manually enabled_ matches when that rule has been turned
  on for the current preview window (see [Manually enabled
  rules](#manuallyenabled) below). Combine it with other
  criteria in an All (AND) group so the rule only runs when
  you opt in and the file matches your other conditions.

To match all files (i.e. a Custom Processor that always
runs), set _Filename_ to `contains` `*`. The asterisk will
act as a wildcard and match all files.

[Add a predicate][addpredicate]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Click the plus sign (+) on the predicate row to add another predicate. Hold down Option while clicking the + to add a boolean group that can be set to All (AND) or Any (OR).

### Manually enabled rules [manuallyenabled]

Some rules should not run on every file that matches their
criteria. Add a **Manually enabled** criterion when you want
a rule to run only after you turn it on for the current
preview.

Use the **Add Manually Enabled** button below the predicate
editor to insert this criterion. Each rule can include it
only once. When present, the rule appears in the {% appmenu
Preview, Enable Custom Rule %} submenu for that preview
window.

**Example use case:** You maintain a rule that injects
print CSS, strips comments, and shifts header levels for
PDF export. You do not want that transformation on every
save while drafting, but you do want it on demand. Give the
rule normal file-matching criteria plus **Manually enabled**,
then toggle it from the Preview menu (or a trigger shortcut)
when you are ready to proof the print layout.

#### Trigger shortcut [trigger-shortcut]

When a selected rule includes **Manually enabled**, a
**Trigger shortcut** field appears beside **Add Manually
Enabled**. Click the recorder, then press the key
combination you want. That shortcut toggles the rule for the
frontmost Marked preview (enable if off, disable if on). The
shortcut is stored with the rule and persists across launches.
Clear the field to remove the shortcut.

![Trigger shortcut recorder in the Conductor][manualshortcut]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Per-preview overrides in the Preview menu [per-preview-overrides-in-the-preview-menu]

Two Preview menu submenus control overrides for the active
preview only. Settings are saved per [view](Opening_Files.html#multiview) when
multiple windows show the same file.

**Enable Custom Rule**
: Lists every enabled rule that includes a **Manually
  enabled** criterion. Check a rule to turn it on for this
  preview; uncheck to turn it off. The preview refreshes
  immediately.

**Custom Rule Override**
: Lists Process-phase rules. Choose one to *pin* it: during
  the Process phase, only that rule is evaluated (other
  Process rules are skipped). Choose **None (automatic)** to
  return to normal rule matching. This is useful when you
  want to force a specific processor pipeline for one
  preview without changing global Custom Rules.

#### Override button in the preview toolbar [override-button-in-the-preview-toolbar]

When a preview has at least one manually enabled rule or a
pinned Process override, a branch icon appears in the bottom
toolbar (to the left of the export and drawer controls).
The filled, accent-colored icon means overrides are active;
the outline icon means overrides are suspended.

![Custom rule override button in the preview toolbar][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Click the button to suspend or re-enable overrides for this
preview without clearing your manual-rule checkmarks or
pinned Process rule. Suspended overrides are restored when
you click again. This is faster than unchecking rules in the
menu when you want to compare the normal preview with your
override pipeline.

### Actions [actions]

Use the *+ Action* button to add actions to the rule.

![Add an action][addaction]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Available actions include:

Set Style
: Set the Style for the preview. Any built-in Style or Custom Style you've added is available.

Run Command
: This takes a command line command, including any arguments, and will pass the content of the file on STDIN. The command should return resulting output on STDOUT.

> **Mac App Store Sandboxing**: The Mac App Store (MAS) version of Marked runs in a sandboxed environment that restricts execution of external binaries. If you need to use external processors like Pandoc in the MAS version, you must copy the binary into the app bundle. To do this:
>
> 1. Right-click Marked.app → Show Package Contents
> 2. Navigate to Contents/Resources/
> 3. Create a `bin` folder if it doesn't exist
> 4. Copy your binary (e.g., `pandoc`) into this
> `bin` folder
> 5. Make it executable: `chmod +x` the binary
> 6. In the Run Command action, reference it as:
>
>     `YOUR_BINARY_NAME [arguments]`
>     Or use the full path:
>     `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Note**: Scripts with external shebangs (like Python scripts pointing to `/opt/homebrew/bin/python`) will automatically be executed through system interpreters when copied to the bundle. The MAS version may still have trouble executing binaries that are actually Python or Ruby scripts instead of binary files.
> You'll need to re-copy binaries after each app update, as updates replace the entire bundle. Alternatively, use **Help->Crossgrade** to get the non-sandboxed version which has no such restrictions.

Run Embedded Script
: Edit a full script in the built-in code editor. Like Run Command, this should take input on STDIN and return output on STDOUT.

Set Metadata
: Adds or sets metadata. Provide a key and a value. If the key exists, its value will be updated, if not, it will be added. The type of metadata used will be automatically determined by the file's contents (or the result of a metadata conversion action).
: If no existing metadata is found, the metadata will be added in MultiMarkdown format inside of an HTML comment. Marked can read this metadata, but it won't appear in your preview no matter what processor is used.

Delete Metadata
: Delete a metadata based on its key.

Strip Metadata
: Delete all metadata. Affects YAML, MultiMarkdown, and Pandoc metadata.

Convert YAML Meta to MMD
: Converts a YAML metadata block at the top of the file to MultiMarkdown style metadata.

Convert MMD Meta to YAML
: Converts a MultiMarkdown metadata block to YAML.

Search and Replace
: Perform a search and replace on the file's content.
: If the search string is surrounded in forward slashes (e.g. `/Project \w+/`), it will be treated as a regular expression. You can use `$1`, `$2`, etc. to include match groups in the replacement string.
: The replacement field supports a few escape sequences (a backslash followed by): `\n` inserts a newline, `\t` inserts a tab character, `\\` inserts a literal backslash, `\$` inserts a literal dollar sign (instead of a match group)
: Any other `\X` sequence is treated as just `X` (the backslash is dropped), so `\e` becomes `e`. A trailing \ with no character after it is preserved as a literal backslash.
: Use `[%key]` in the replacement string to insert a value from document metadata, environment variables, or context (e.g. `[%title]`, `[%MARKED_PATH]`). Keys set by earlier actions in the same rule or by a preceding rule are available. Unmatched keys are replaced with an empty string.

Insert Title H1
: Inserts an H1 in the document. This can either be pulled from metadata or the filename.

Shift Headers
: Adjust header levels, from -5--+5. For example, if you set this to -1, then all H1s become H2s, H2s become H3s, etc. Set it to a positive number to hoist the header levels by that amount.

Normalize Headers
: This action will ensure, if possible, that there's only one H1 in the document, and adjust all header levels so that they're in a semantic order and don't skip levels, e.g. from H2 to H4. If the original document is at all semantically ordered to begin with, this will refine the hierarchy well.

Insert TOC
: Insert a Table of Contents. The TOC can go after the first H1, the first H2, or at the top of the file (will be inserted after any metadata).

Insert File
: Inserts a selected text file at a given point in the document. This can be after the first H1, first H2, top, bottom, or after a text match (use `/pattern/` to search for a regular expression).

Insert Text
: Provides a popup editor with which you can embed text into the action directly. Positioning options are the same as _Insert File_.
: Use `[%key]` anywhere in the inserted text to pull values from document metadata, environment variables, or Marked context (e.g. `[%author]`, `[%MARKED_PATH]`). This works regardless of which processor you use, so you do not need MultiMarkdown for metadata substitution. Values from earlier actions in the same rule (such as **Set Metadata**) or from a preceding rule are included. Unmatched keys are replaced with an empty string.

Insert CSS File
: Injects a selected CSS file into the document. This will be loaded after any Style selection and can be used to override existing styles or add new ones.

Insert CSS
: Offers a pop-up CSS editor where you can add your own CSS directly to the action. This CSS will be injected at the top of the document, after any existing styles. The order of injected styles will match the order of the actions in the rule.

Insert JavaScript File
: Injects a selected JavaScript file at the end of the document. Note that you need to use an *Insert JavaScript* action with an [update hook](#updatehook) if you want the script to reload with every update.

Insert JavaScript from URL
: Use this to insert a `<script>` tag linked to a CDN or other remote URL at the end of the document. Note that you need to use an *Insert JavaScript* action with an [update hook](#updatehook) if you want the script to reload with every update.

Insert JavaScript
: Provides a popup JavaScript editor with which you can embed custom JavaScript directly in the action. This will be injected at the end of the document, and the order of JavaScript run by the rule will be determined by the sequence of the actions, with the last action added last.
: Note that you need to use an [update hook](#updatehook) if you want scripts to run with every update.

Self-Link URLS
: Convert any bare URLs to `<url>`, which will generate a hyperlink in any processor.

Run Shortcut
: Run an Apple Shortcut. Any Shortcut run should take input from STDIN and return output at the end (Stop and Return Output). If you want to perform actions that don't modify the text, set the input to a variable, run your actions, and then output the original text variable at the end.

Run System Service
: Run any System Service in `~/Library/Services`. The Service should accept input and return output.

Run Automator Workflow
: Run any Automator `.workflow` file. Input will be passed on STDIN and output is expected on STDOUT.

Run Rule
: Run another Custom Rule's actions from the current rule.
  Choose the target rule from the popup. The invoked rule
  runs in the same phase (Preprocessor or Process) without
  re-evaluating its predicate, which makes it useful for
  reusable "ingredient" rules.

  **Example use case:** Define a small rule named "Strip
  HTML comments" with a Search and Replace action, and give
  it a **Manually enabled** criterion so it never runs
  automatically. In your main book-processing rule, add
  **Run Rule** actions in sequence: first "Normalize headers,"
  then "Strip HTML comments," then a Run Command that calls
  Pandoc. You keep each step maintainable without duplicating
  actions across rules.

  **Nesting:** A rule invoked by **Run Rule** cannot invoke
  another rule. If the target rule contains a **Run Rule**
  action, that action is skipped; all other actions in the
  target rule still run. You can add multiple **Run Rule**
  actions to a single rule and they execute in order.

  A rule cannot invoke itself, and Marked detects cycles
  (for example, Rule A invoking Rule B which invokes Rule A)
  and skips the nested call. See the [Custom Rules
  Log](#customprocessorlog) for skip messages.

Continue
: By default, once a rule is matched, processing will stop (separately for Preprocessors and Processors, so one Preprocessor and one Processor can match). This action will force rule matching to continue after the rule performs its actions.

### Update Hook [updatehook]

Marked does not do a full refresh with every update, so if
you have scripts that render portions of the DOM, they need
to run their render function using Marked's Hook API.

The example below uses Mermaid, which you never actually
need to do, as Mermaid is now included by default. But
here's how you would do it if you were including it manually.

Add an **Insert JavaScript** action, and in the "Edit JS"
window, initialize the script and add the hook:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

This will cause `mermaid.run()` to be executed every time
Marked performs a partial update.

### Test Rules [test-rules]

The _Test Rules_ button under the Rules list will open a
dialog where you can select any Markdown file and it will be
tested against all of your Rules. Rules that match will get
highlighted with a green tab on the left side. When matching
against a file, an X button will appear which can be used to
clear the test and unhighlight the rows.

## Drag and Drop [drag-and-drop]

The Conductor window supports enhanced drag and drop
capabilities that intelligently detect file types and
provide appropriate actions based on the dragged file. The
implementation includes a split overlay system for text
files that allows users to choose between testing the file
against rules or adding it as an action.

![Drag and Drop in Custom Rules][drag]

[drag]: images/draganddropconductor.jpg @2x width=800

### File Type Detection [file-type-detection]

The system automatically detects different file types and
shows appropriate overlay messages:

- **CSS files** (`.css`): Shows "Insert CSS File" overlay
- **JavaScript files** (`.js`, `.javascript`): Shows "Insert
  JS File" overlay
- **Script files** (any executable file)): Shows "Run
  Command" overlay
- **Text files**: Shows split overlay
- **Executable files**: Shows "Run Command" overlay
- **Unknown extensions**: Defaults to "text" type and shows
  split overlay

## Custom Processor Log [customprocessorlog]

If you're getting odd results and want a look at what's going on, the Custom Rules Log will show you what rules are running in what order. Use **Help->Show Custom Rules Log** to open it. Invoked **Run Rule** actions and skipped nested calls are logged here as well.

![Custom Rules Log][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Executing Multiple Commands [executing-multiple-commands]

A rule can have multiple commands in sequence. The output of
each command will be passed to the next. If you want to have
a command output something at the same time as Marked's
preview updates, be sure to pass the original content back
to STDOUT for processing the next command or built-in
processor.

For example, if you wanted to have a command update a PDF
document using Pandoc, just pass the original file path
(from environment variables) to Pandoc with appropriate
command line options, and then echo the STDIN content back
out to STDOUT.

## Dynamically bypassing custom processors [dynamically-bypassing-custom-processors]

If a custom processor returns "NOCUSTOM" on STDOUT, Marked
will terminate the custom processor and fall back to the
default internal processor. This allows you to create a
custom processor that can decide whether or not it needs to
run using the [environment variables](#environmentvariables)
below, the document filename or extension, content matching
or other logic.

If instead of `NOCUSTOM` a Custom Processor returns
`MULTIMARKDOWN` or `DISCOUNT` (or `GFM`), `KRAMDOWN`, or
`COMMONMARK`, then that internal processor will be used for
just that document. This change will not affect the default
processor set in Settings.

## Environment variables [environmentvariables]

The Run Command action has an environment editor where you
can set your own environment variables that will be
available to the command or script. In addition to these
custom variables, Marked includes some of its own.

Marked runs the custom processor in its own shell, meaning
standard environment variables are not automatically passed.
You can use Marked's environment variables to augment your
own in your scripts. Marked makes the following variables
available for use in your shell scripts:

**MARKED_ORIGIN**
: The location (base directory) of your primary working file (the folder of the working text, Scrivener or index file).

**PATH**
: Marked sets a path which includes default executable folders and appends the directory in the `MARKED_ORIGIN` above. The defaults are: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. You can add your own by setting the PATH variable as needed and appending or overwriting Marked's path (e.g. `PATH=/usr/local/yourfolder:$PATH`).

**HOME**
: The home directory of the logged-in user. Python and other scripts which rely on the HOME variable being set will pick this up automatically, but it's available for other uses in your scripts.

**MARKED_EXT**
: The extension of the primary file being processed. This variable allows you to script different processes based on the type of file being viewed. For example, if `$MARKED_EXT == "md"` run your preferred Markdown processor, but if `$MARKED_EXT == "textile"` run a Textile processor.

**MARKED_PATH**
: This is the full UNIX path to the main file open in Marked when at the time it's loaded.

**MARKED_INCLUDES**
: A quoted, comma-separated list of the files Marked has included in the text being passed using the various [include syntaxes](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: This will be set to either "PROCESS" or "PREPROCESS," allowing you to use a single script to handle both phases based on this variable.

**MARKED_CSS_PATH**
: The full path to the current stylesheet

### Metadata Environment Variables [metadata-environment-variables]

When the Run Command action is executed in Marked's
Conductor system, document metadata is automatically
extracted and made available as environment variables to the
command.

#### How it works [how-it-works]

1. **Metadata Extraction**: The system extracts metadata from the document using the existing `extractMetaDataFromString:` method, which supports:
   - YAML front matter (`---` blocks)
   - MultiMarkdown metadata (key: value lines)
   - Pandoc metadata (`%` title blocks)
   - HTML comment metadata (`<!-- key: value -->`)

2. **Key Normalization**: Metadata keys are normalized for use as environment variables:
   - Converted to lowercase
   - All non-alphanumeric characters are removed
   - Spaces and special characters are stripped

3. **Environment Variable Format**: Each metadata key becomes an environment variable with the `MD_` prefix:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Example [example]

Given a document with this metadata:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

The following environment variables would be available to
commands:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Usage in Commands [usage-in-commands]

You can now use these environment variables in your Run Command actions:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Supported Actions [supported-actions]

This metadata-to-environment variable functionality is
available in:

- **Run Command** actions
- **Run Embedded Script** actions

The metadata is automatically extracted from the document
content and made available to any command or script that
runs through these actions.

## Enabling and Disabling [enabling-and-disabling]

The custom processors can be turned on and off for
individual documents using {% kbd opt cmd C %}. You
can also turn a preprocessor or processor on for a document
automatically [using metadata](#perdocument) at the top of
the document.

The current statuses of the processors for each document are
displayed as indicator lights (only visible when a processor
is enabled) to the left of the toolbar items in the bottom
right toolbar of the Preview.

### Preprocessor [preprocessor]

If you set up preprocessor rules, they are run after Marked
handles any Marked-specific tasks such as including external
documents and code, but before it runs the processor
(internal or custom). This gives you a chance to render
custom template variables, handle substitutions or inject
your own content by any other means.

Marked sets an environment variable for the working
directory (`MARKED_ORIGIN`) to the parent directory of the
file being previewed. You can use this to change the working
directory of a script and include files with paths relative
to the original document. As an example, in Ruby you can
use:

	Dir.chdir(ENV['MARKED_ORIGIN'])

When enabled, the custom preprocessor can be turned on and
off for individual documents using
{% kbd ctrl opt cmd C %}.

#### Per-document Processor/Pre-processor [perdocument]

Custom Processors can also be set on a per-document basis
using the metadata format for [Per-Document
settings](Per-Document_Settings.html).

You can specify whether to use custom processor settings and
override the default for a document using [Per-Document
settings](Per-Document_Settings.html) (`Custom Processor:`
and `Custom Preprocessor:`). Any setting other than "true"
or "yes" will disable the custom pre/processor.

Example usage:

    Custom Processor: true
    Custom Preprocessor: false

As noted in the [Per-Document
Settings](Per-Document_Settings.html#hidingmeta) page, you
can surround this metadata with HTML comment markers to hide
it from GitHub and other processors that don't remove it
from the output:

    <!--
    Custom Processor: true
    Custom Preprocessor: true
    -->

## Using an alternative Markdown processor [using-an-alternative-markdown-processor]

Any Markdown flavor you can render from the command line can
be used with Marked. It needs to be able to take input on
STDIN, which is the same as "piping" your Markdown to it on
command line, i.e. `cat myfile.md | myprocessor`. It needs
to return the resulting HTML on STDOUT, which every
processor I've ever worked with does by default.

Use `which YOUR_PROCESSOR` in Terminal to determine the path
to the executable, then paste that into the Run Command path
field, or just drag the executable to the Custom Rules window
with the rule to which you want to add the action selected.

If your processor requires arguments on the command line,
you'll need to enter those in the field as well. Some
processors need hyphens to function on STDIN and/or STDOUT,
e.g. `-o - -` often signals input from STDIN, output to
STDOUT. See your processor's documentation for details.

I've tested the Custom Processor feature with Pandoc,
Kramdown, marked (discount), MultiMarkdown 6, Maruku, and
various other flavors.

### A note about Pandoc and Sandboxing [a-note-about-pandoc-and-sandboxing]

Pandoc (and some other command line tools) will not run in
the Mac App Store (sandboxed) version of Marked.
If you need to run Pandoc, use **Help->Crossgrade** to get a
free license for the direct (Paddle) version. This is true
of any processor that runs into sandboxing issues: if Marked
can't execute it due to MAS permissions issues, it will
offer the steps to crossgrade. If you're experiencing issues
and this isn't happening, please contact me through the
[support site](https://support.markedapp.com/questions/add).

### Pandoc as Swiss Army Markdown Processor [pandoc-as-swiss-army-markdown-processor]

[Pandoc](https://pandoc.org/) is by far the most flexible
all-purpose tool for handling an array of markup formats. By
adding a `-f` argument with one of the following, Pandoc can
be your Custom Processor for any of:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

And a bunch of others. See the [Pandoc
documentation](https://pandoc.org/MANUAL.html) for more
info. To use one of these as an input format, just add the
following in your Run Command field:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc is perfect for writing a script that uses the
`$MARKED_EXT` environment variable to determine which format
to run through Pandoc, or use a series of Rules with
extension matches. If the extension is `md`, use
`pandoc -f gfm` or `pandoc -f markdown_mmd` (or just return
`NOCUSTOM` on STDOUT to use the default processor). But if it's
`textile`, run `pandoc -f textile` within the script. And if
it's `wiki`, use one of the wiki markup processors. You get
the idea.

As Pandoc aficionados will know, Pandoc can also handle
extensive bibliography and LaTeX scenarios. Most features
you can access through the command line are available just
by using passing arguments in Marked.

## Using Textile [using-textile]

A few people have asked how to get Textile working in
Marked. You need to have a Textile converter available from
the command line. There are a few options, including Pandoc
(see above), but if you don't already have Pandoc installed,
two other options are RedCloth for Ruby and Textile for Perl
(requires that the Developer Tools be installed). Install
one or the other:

1. Install Textile from
   <https://github.com/bradchoate/text-textile> **OR**
   `sudo gem install RedCloth` in Terminal
2. Use `which textile` or `which redcloth` to determine the
   path to use in the Custom Processor path settings

Now Marked is a Textile previewer for you!

## Using AsciiDoc [using-asciidoc]

1. Install [AsciiDoctor](http://asciidoctor.org/).
2. Enable a Custom Rule in {% prefspane Processor %} to match your AsciiDoc files.
3. Set the Rule to be a Processor and add a Run Command action
    1. Determine the path to `asciidoc`, which will be
       something like `/usr/bin/asciidoc` or
       `/opt/local/bin/asciidoc`. If unsure, use
       `which asciidoc` to locate
    2. Enter `[PATH To asciidoc] --backend html5 -o - -` as
       the command (the - at the end sends the output as
       STDOUT)

This sends the current document to STDIN and displays the
generated HTML as STDOUT.

See [this gist](https://gist.github.com/mojavelinux/6324279)
from [Dan Allen](https://gist.github.com/mojavelinux) for
more information.
