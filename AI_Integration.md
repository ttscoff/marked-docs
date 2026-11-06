# <%= @title %>

Give an LLM agent a skill file so it can open files and folders in Marked, jump to a Settings section, and change preferences. The agent uses Marked's [URL handler](URL_Handler.md). You do not need a separate plugin or server.

## Download the skill [download-the-skill]

{% download "SKILL.md" "Agent skill for opening files in Marked and changing preferences. Save it as SKILL.md." %}

The file is plain Markdown with a short header your agent reads before it acts. Hand the same file to any agent that accepts a skill or a standing instruction.

## Install it [install-it]

Put the file in a folder named for the skill, and keep the filename `SKILL.md`.

For Cursor, either location works:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

The first is available in every project. The second applies only to that project. Other agents can use the same text as a project instruction if they do not have a skills folder.

After it is installed, ask the agent to open a file or folder in Marked. It should run a command like:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

A folder uses the same command. The path has to exist, and spaces and other reserved characters must be percent-encoded. See [URL Handler](URL_Handler.md) for the full scheme, including refresh, Streaming Preview, and callbacks.

## Preferences [preferences]

The skill also covers two preference commands:

`pref`
: Opens Settings to a named section, such as Preview or Style. It does not change a value.

`defaults`
: Sets a preference Marked already stores, then reloads open previews. Pass `refresh=0` to leave the previews alone. The agent should read the current preferences before it writes one, because an unknown key is ignored.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Related [related]

[Using Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.md) covers watching a folder of plans and notes while an agent writes them. The [command line utility](Command_Line_Utility.md) is the same kind of access from a shell, without an agent.
