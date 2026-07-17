# <%= @title %>

The `mk` command-line tool provides easy access to Marked's features from the terminal, enabling workflow automation and integration with shell scripts and other command-line tools.

## Installation [installation]

The recommended way to install `mk` is with Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

If you do not use Homebrew, download and install the signed package:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

After downloading `mk.pkg`, double-click it and follow the installer prompts.

## Basic Usage [basic-usage]

### Opening Files [opening-files]

Open a markdown file in Marked from the command line:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Streaming Content from STDIN [streaming-content-from-stdin]

Stream content directly to Marked's Streaming Preview:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

The Streaming Preview window will open and display the content in real-time as it's piped from other commands.

## Command Reference [command-reference]

### File Operations [file-operations]

**`mk [file]`** — Open a markdown file in Marked

**`mk [file] --raise`** — Open file and raise the window above all others

### STDIN and Streaming [stdin-and-streaming]

**`mk`** or **`mk -`** — Read from STDIN and open Streaming Preview

**`mk --stream`** — Open Streaming Preview window without reading STDIN

### Preview Management [preview-management]

**`mk --refresh`** — Refresh the frontmost preview window

**`mk --refresh all`** — Refresh all open preview windows

**`mk --refresh file.md`** — Refresh the preview for a specific file (if open)

### Preferences [preferences]

**`mk --pref`** — Open Marked preferences (General page)

**`mk --pref Advanced`** — Open preferences to a specific page

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Set user preferences (multiple pairs allowed)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Style Management [style-management]

**`mk --style NAME`** — Set preview style for open windows

**`mk --add-style FILE`** — Add a CSS file as a custom style to Marked

```bash
mk --add-style ~/Styles/custom.css
```

### JavaScript Execution [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** — Run JavaScript in frontmost window

**`mk --dojs "SCRIPT" all`** — Run JavaScript in all windows

**`mk --dojs "SCRIPT" file.md`** — Run JavaScript in specific file(s)

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Content Extraction and Import [content-extraction-and-import]

**`mk --extract URL`** — Extract content from URL and open in Marked

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** — Open Import URL window (optionally with URL)

**`mk --stylestealer [URL]`** — Open Style Stealer HUD (optionally with URL)

### Utility Commands [utility-commands]

**`mk --paste`** — Create new document from clipboard

**`mk --preview TEXT`** — Preview text directly in a new document

**`mk --dingus`** — Open Markdown Dingus for testing processors

**`mk --help`** or **`mk -h`** — Show usage information

**`mk --version`** or **`mk -v`** — Show version information

## Examples [examples]

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Integration [integration]

### Shell Aliases [shell-aliases]

Add to your `~/.zshrc` or `~/.bash_profile`:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Scripts [scripts]

Use `mk` in shell scripts for automation:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Workflows [workflows]

Combine with other tools:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## Open Source [open-source]

The `mk` command-line tool is open source and available on GitHub:

**https://github.com/ttscoff/mk**

You can:
- View the source code
- Contribute improvements
- Report issues
- Build from source if needed

The tool is written in Swift and can be compiled using Xcode. See the [README](https://github.com/ttscoff/mk) for build instructions.

## Version [version]

Check your installed `mk` version with:

```bash
mk --version
```

## Related Features [related-features]

- See [URL Handler](URL_Handler) for more information about Marked's URL scheme
- See [Streaming Preview](Streaming_Preview) for details on the streaming preview feature
- See [Workflow Integration](Workflow_Integration) for automation examples
