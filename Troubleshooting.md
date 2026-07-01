# <%= @title %>

### Debug Mode

You can enable debug logging by opening {% prefspane Advanced %} and checking the **Debug Mode** checkbox at the bottom of the pane. This will display a dropdown menu where you can set the level of logging you'd like to see:

- **Errors only**: Only severe errors will be logged
- **Errors and Warnings**: Additionally display less urgent warnings
- **All**: Display errors, warnings, and info-level debug messages. This is the recommended setting for troubleshooting.

{% note %}
TODO: Does this still work?
You can also access these options by holding the {% kbd opt  %} key when opening {% appmenu Help %} in the menu bar.
{% endnote %}

### Viewing the log

With **Debug Mode** enabled, you can open the {% appmenu Help %} menu and select Open Debug Log. This will open Marked's log in Console.app, which will be updated live as log messages are added while using Marked.

### Troubleshooting Custom Rules

[Custom preprocessors and processors](Custom_Processor.html) get their own log interface. Select {% appmenu Help, Show Custom Rules Log %} to open the window. This window will display a colorized log showing which rules matched and what commands they run.

### Reporting an Issue

Use {% appmenu Help, Report an Issue %} to open a window that shows your settings for the most common keys, and a template for creating a bug report. Use the "Copy to Clipboard" button to copy the contents of the window, and click "Open Support Site" to open [the new-question form](https://support.markedapp.com/questions/add) where you can paste your report. I try to respond to reports within 48 hours.
