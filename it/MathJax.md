<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

I numeri contano tanto quanto le parole.

## Anteprima delle formule con MathJax [preview-formulas-with-mathjax]

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

Attivando MathJax in {% prefspane Style %}, gli script e i CSS necessari verranno inclusi nell'anteprima. Quindi la sintassi matematica di MultiMarkdown può essere utilizzata nel documento Markdown e i risultati verranno visualizzati.

Esempio di sintassi MMD MathJax:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Se scegli di includere MathJax in un file HTML esportato, verrà utilizzato un collegamento CDN al posto del codice MathJax incorporato. Ciò richiede una connessione Internet per visualizzare il MathML renderizzato.

## Fonte MathJax: locale vs CDN [mathjax-source-local-vs-cdn]

Quando MathJax è abilitato, Marked può caricarlo da:

- **Locale**: una copia di MathJax v3 inclusa nell'app (più veloce da caricare, funziona offline).
- **CDN**: il CDN ufficiale MathJax v3 (sempre aggiornato, nessun impatto sull'app bundle).

Il popup **MathJax Source** in {% prefspane Style %} ti consente di scegliere:

- **Locale**: utilizza il componente ES5 `tex-chtml.js` dall'app bundle.
- **CDN** – carica lo stesso componente dal CDN. Ciò richiede una connessione Internet.

I file HTML esportati fanno sempre riferimento a MathJax da una CDN, indipendentemente dall'origine dell'anteprima, quindi rimangono autonomi e di piccole dimensioni.

## Numerazione delle equazioni [equation-numbering]

Puoi abilitare la numerazione delle equazioni in {% prefspane Style %}. Funziona sia con MathJax che con KaTeX, ma è implementato in modo diverso internamente. Per MathJax v3, Marked mappa le tue impostazioni sulla configurazione MathJax appropriata in modo che:

- "Equazioni numeriche" controlla se vengono visualizzati i numeri.
- L'opzione "laterale" controlla se i numeri appaiono a sinistra o a destra.
- L'opzione "Solo AMS" limita la numerazione alle equazioni in stile AMS.

Queste opzioni corrispondono alle impostazioni `tex.tags` e `tex.tagSide` di MathJax dietro le quinte.

## Pacchetti aggiuntivi [additional-packages]

MathJax v3 è modulare. Marked abilita sempre i pacchetti TeX/AMS principali e, facoltativamente, puoi attivarne di aggiuntivi in {% prefspane Style %}:

- **Fisica** (`physics`) – notazione fisica e comodità.
- **Chimica** (`mhchem`) – equazioni chimiche.
- **Bra–ket** (`braket`) – Notazione bra–ket di Dirac.
- **Simboli in grassetto** (`boldsymbol`) – simboli matematici in grassetto.

Fai clic su **Pacchetti aggiuntivi…** per aprire un piccolo elenco di controllo in cui puoi attivare o disattivare questi pacchetti. Le modifiche avranno effetto la prossima volta che Marked eseguirà il rendering della matematica nell'anteprima.

## Configurazione avanzata di MathJax [mathjax-advanced-configuration]

Puoi applicare ulteriori configurazioni personalizzate oltre alle impostazioni predefinite di Marked aggiungendo un oggetto JSON valido nel campo **Configurazione avanzata**. Questo campo viene unito all'oggetto di configurazione MathJax v3 (`window.MathJax`) prima del caricamento di MathJax. Può contenere [qualsiasi opzione supportata da MathJax v3](https://docs.mathjax.org/en/latest/options/), ad esempio:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macro": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "pacchetti": { "[+]": ["fisica"] }
        }
    }

Questo esempio regola i delimitatori TeX, aggiunge una macro `\tr` e abilita il pacchetto `physics` oltre al set predefinito. Con queste impostazioni, tutti i seguenti elementi vengono visualizzati correttamente:

    Formula in linea che utilizza parentesi, \\\\({x}^{2} {y}^{2}=1\\\\) o con il simbolo del dollaro, ${x}^{2} {y}^{2}=1$.

    Visualizzazione con parentesi escape:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    O con il doppio simbolo del dollaro:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

La configurazione aggiuntiva estende l'oggetto esistente, quindi solo le proprietà specificate verranno sovrascritte. Le opzioni non specificate rimarranno predefinite per la preimpostazione corrente.

Tieni presente che utilizzando il processore MultiMarkdown con delimitatori non standard, i caratteri all'interno dell'espressione vengono analizzati, quindi simboli come `*` e `^` causeranno modifiche tipografiche che danneggeranno il processore MathJax. La soluzione migliore in questi casi è utilizzare il processore Sconto in [Impostazioni processore](x-marked-3://pref/processor).

Marked esegue un po' di magia quando MathJax o KaTeX sono abilitati, convertendo la sintassi matematica per garantire che sia il più compatibile possibile con il processore corrente (MultiMarkdown o Discount). Dovrebbe essere ottimo in tutte le circostanze, ma se ritieni che causi problemi, [contatta l'assistenza](https://support.markedapp.com/questions/add)!


## KaTeX [katex]

[katex]: https://katex.org/

[KaTeX][] è disponibile come alternativa a MathJax. È più leggero e quindi più veloce da caricare, il che può essere ottimo su documenti con un gran numero di formule. Tuttavia, non ha così tante funzionalità e alcune equazioni che funzionano con MathJax (o LaTeX) potrebbero non essere supportate.

## Numerazione automatica delle equazioni [numbering]

Puoi abilitare la numerazione delle equazioni in {% prefspane Style %}. Funziona sia con MathJax che con KaTeX. Puoi selezionare se i numeri devono apparire sul lato sinistro o destro dell'equazione.

### In MathJax [in-mathjax]

In MathJax, questo utilizza l'impostazione:

    {
      TeX: {EquationNumbers: {autoNumber: "all" } }
    }

Se desideri numerare solo le equazioni AMS, seleziona "Solo AMS" a destra del menu a discesa "laterale".

### In KaTeX [in-katex]

KaTeX non offre la numerazione delle equazioni. Per simulare ciò in Marked, viene utilizzato il CSS e tutte le equazioni visualizzate sono numerate.

## Problemi di esportazione [export-issues]

I formati Rich Text non gestiranno le equazioni (né di MathJax né di KaTeX). Saranno nascosti nel documento di output poiché provare a includere i caratteri speciali crea un pasticcio più grande di quanto si possa immaginare... Questo è qualcosa che spero di risolvere prima o poi, ma per ora è un difetto.