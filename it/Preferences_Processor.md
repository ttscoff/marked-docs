<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane Processor %}:

![Impostazioni: Processore][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Processa il markdown con

Processore Markdown predefinito. Il processore Discount è preferito per gli utenti GitHub, MultiMarkdown è l'ideale per gli scrittori. Marked compensa alcune differenze tra la sintassi. Vedi __Aiuto->Riferimento Markdown__ per ulteriori informazioni.

Regole personalizzate
: utilizzare il pulsante Regole personalizzate per aprire l'editor Regole personalizzate, che consente di determinare le opzioni di elaborazione e le trasformazioni dei documenti in base ai criteri. Consulta la [documentazione del processore personalizzato](Custom_Processor.html) per i dettagli.

I nuovi documenti utilizzano Custom
: selezionare il preprocessore e/o il processore per abilitare automaticamente l'elaborazione delle regole sui nuovi documenti. Se utilizzi le regole personalizzate, probabilmente vorrai che entrambe siano abilitate.

###HTML

Genera ID sui titoli
: genera ID di intestazione in base al contenuto del tag h1-h6.

Utilizza ID note a piè di pagina casuali
: genera ID di note a piè di pagina casuali per evitare conflitti quando più documenti vengono visualizzati su una pagina.

Processo Markdown all'interno dell'HTML
: per impostazione predefinita, il Markdown all'interno dei tag HTML viene solitamente ignorato. Questa opzione forza Marked a continuare l'elaborazione all'interno degli elementi del blocco. Tieni presente che alcuni markup potrebbero causare problemi.


### Rappresentazione

Conservare le interruzioni di riga nei paragrafi
: Rispetta le interruzioni di riga nel testo del paragrafo, sostituendole con interruzioni rigide invece di concatenarle con la riga precedente.

Renderizza le caselle di controllo di GitHub
: Render `- [ ]` e `- [x]` per creare caselle di controllo negli elenchi. Le caselle di controllo vengono visualizzate per l'anteprima ma non funzionano all'interno di Marked.

\#Il testo è un tag
: consente agli hashtag (`#` immediatamente seguiti da testo senza spazi) di essere interpretati come tag, non come titoli. Questa funzionalità è predefinita per gli utenti Bear.
: __Style tags__ fa sì che i tag vengano visualizzati con la formattazione "capsula" per distinguerli dal testo. Quando è abilitato, i tag possono essere mostrati/nascosti usando {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Il testo è tag abilitato][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Rendering `==highlight==` e `~~delete~~`
: Se questa opzione è abilitata, il testo `==highlight==` verrà visualizzato come tag HTML `<mark>`, che apparirà come evidenziato in giallo a meno che non venga modificato diversamente da uno Stile. Inoltre, la sintassi `~~delete~~` verrà visualizzata con un tag `<del>`.

: Se __Render as CriticMarkup__ è abilitato, la sintassi `==highlight==` e `~~delete~~` verrà convertita in CriticMarkup, che potrà quindi essere visualizzato nelle visualizzazioni originale, markup e modificata.

Visualizza `~text~` come carattere di sottolineatura
: Se questa opzione è abilitata, `~text~` circondato da singole tilde verrà visualizzato come sottolineato. Ciò è in conflitto con la sintassi MultiMarkdown per il pedice ed è disabilitato per impostazione predefinita.