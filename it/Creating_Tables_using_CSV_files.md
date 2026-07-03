<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Se un file incluso tramite [sintassi di inclusione di Marked o sintassi del blocco IA Writer] [include] ha un'estensione CSV o TSV, Marked tenterà di analizzarlo e convertirlo in una tabella MultiMarkdown. Funziona con la maggior parte dei formati standard, inclusi quelli separati da virgole e tabulazioni, nonché separatori aggiuntivi e formati di virgolette che vengono rilevati automaticamente.

Un vantaggio dell'utilizzo di file CSV invece di scrivere tabelle Markdown è che le interruzioni di riga all'interno delle celle vengono automaticamente convertite in tag `<br>`. Questo deve essere fatto manualmente per includere interruzioni di riga durante la scrittura di tabelle MultiMarkdown, quindi è un ulteriore risparmio di tempo.

Come nota a margine, esiste un'eccellente app chiamata [TableFlip][] che semplifica molto la modifica delle tabelle all'interno del documento. Vale la pena verificarlo se lavori spesso con dati tabulari.

I file CSV inclusi verranno controllati per eventuali modifiche, quindi è possibile apportare ulteriori modifiche al file CSV originale e Marked aggiornerà automaticamente l'anteprima al salvataggio.

Le tabelle convertite verranno incluse nell'esportazione Markdown, quindi Marked può essere utilizzato per compilare documenti contenenti dati strutturati ed esportare un singolo file.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/