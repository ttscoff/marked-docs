<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Consegna a un agente LLM un file skill, così può aprire file e cartelle in Marked, passare a una sezione delle Impostazioni e cambiare le preferenze. L'agente usa il [gestore dell'URL](URL_Handler.md) di Marked. Non serve un plugin né un server separato.

## Scaricare lo skill [download-the-skill]

{% download "SKILL.md" "Skill per un agente che apre file in Marked e cambia le preferenze. Salvalo come SKILL.md." %}

Il file è Markdown semplice, con una breve intestazione che l'agente legge prima di agire. Puoi consegnare lo stesso file a qualsiasi agente che accetti uno skill o un'istruzione fissa.

## Installarlo [install-it]

Metti il file in una cartella che porta il nome dello skill e lascia il nome `SKILL.md`.

Con Cursor vanno bene entrambe le posizioni:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

La prima è disponibile in ogni progetto. La seconda vale solo per quel progetto. Gli altri agenti possono usare lo stesso testo come istruzione di progetto, se non hanno una cartella di skill.

Dopo l'installazione, chiedi all'agente di aprire un file o una cartella in Marked. Dovrebbe eseguire un comando come questo:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Una cartella usa lo stesso comando. Il percorso deve esistere, e gli spazi e gli altri caratteri riservati vanno codificati in percentuale. Vedi il [gestore dell'URL](URL_Handler.md) per lo schema completo, inclusi refresh, Streaming Preview e i callback.

## Preferenze [preferences]

Lo skill copre anche due comandi per le preferenze:

`pref`
: Apre le Impostazioni su una sezione indicata per nome. Il nome nell'URL resta in inglese, per esempio `Preview` o `Style`. Non cambia alcun valore.

`defaults`
: Imposta una preferenza che Marked ha già memorizzato, poi ricarica le anteprime aperte. Passa `refresh=0` per lasciare le anteprime invariate. L'agente deve leggere le preferenze attuali prima di scriverne una, perché una chiave sconosciuta viene ignorata.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Vedi anche [related]

[Utilizzo di Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.md) spiega come tenere d'occhio una cartella di piani e note mentre un agente li scrive. L'[utilità della riga di comando](Command_Line_Utility.md) offre lo stesso tipo di accesso dalla shell, senza un agente.
