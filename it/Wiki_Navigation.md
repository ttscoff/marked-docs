<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked include un sistema di navigazione wiki che ti consente di passare rapidamente tra file di testo correlati utilizzando semplici collegamenti `[[wiki]]`. Questo sistema è progettato per una navigazione senza interruzioni e funziona al meglio se configurato per aprire i collegamenti nella finestra corrente.

## Impostazioni ottimali

Per utilizzare il collegamento wiki, abilita **Converti `[[wiki links]]`** in {% prefspane Preview %} e imposta l'estensione predefinita che Marked utilizzerà durante la ricerca di file corrispondenti.

Per una migliore esperienza, imposta **"I collegamenti ai file di testo dovrebbero aprirsi in:"** su *"la finestra corrente"* in {% prefspane Apps %}. Ciò garantisce che la navigazione sembri naturale e che la storia venga preservata.

Se **Evidenzia errori di sintassi Markdown** è abilitato in {% prefspane Proofing %}, la sintassi `[[wiki link]]` che non corrisponde a un nome file nella directory corrente verrà evidenziata in rosso per indicare che un file di riferimento non esiste. Queste evidenziazioni verranno aggiornate man mano che i file vengono aggiunti, ma solo dopo che il file corrente viene salvato o ricaricato. Facendo clic sul collegamento di un file mancante evidenziato verrà proposta la creazione di un nuovo file, aggiungendo l'estensione predefinita, se necessario. Il nuovo file vuoto verrà aperto in Contrassegnato e, se Modifica nuovi documenti è abilitato, il tuo editor verrà aperto con il nuovo file.

## Come funzionano i collegamenti Wiki

- I **Link Wiki** utilizzano il formato: `[[wiki link]]`.
- Quando fai clic su un collegamento wiki, Marked cercherà un file corrispondente nella **stessa directory** del documento corrente.
- Il file deve avere l'estensione specificata nelle impostazioni di Marked (ad esempio, `.md`), a meno che tu non fornisca un nome file completo con estensione nel collegamento (ad esempio, `[[notes.txt]]`).
- Se desideri utilizzare un testo per il collegamento diverso dal nome del file, aggiungilo dopo una barra verticale (`|`) nel collegamento, ad es. `[[wiki linking|A note about linking]]`, che verrà visualizzato come `[A note about linking](wiki-link.md)`.
- Se un collegamento wiki inizia con `#`, verrà visto come un collegamento di ancoraggio sulla stessa pagina. I nomi delle ancore vengono normalizzati utilizzando lettere minuscole e sostituendo tutti gli spazi con trattini. Per i processori che creano ID di intestazione senza trattini (come MultiMarkdown), ad es. `## wiki links` ottiene un ID `wikilinks`, questa navigazione potrebbe interrompersi. In questi casi, specifica l'ID collegamento corretto, con una pipe e un titolo se necessario, ad es. `[[#wikilinks|#wiki links]]`.

### Nomi file corrispondenti

Quando utilizzi un collegamento come `[[wiki link]]`, Marked cercherà un file con uno dei seguenti nomi (assumendo che l'estensione predefinita sia `.md`):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (e altre combinazioni di spazi, trattini, trattini bassi e InterCaps)

**Tutte le corrispondenze non fanno distinzione tra maiuscole e minuscole e sono flessibili con separatori.**
Se specifichi un'estensione nel collegamento (ad esempio, `[[notes.txt]]`), Marked cercherà quel file esatto.

## Backlink

Quando un file di testo viene aperto e la navigazione wiki è abilitata, il resto dei file nella directory verrà scansionato per `[[links]]` nel file corrente. Ciò avverrà in background e il documento aperto verrà aggiornato con un elenco di backlink, se presenti. Per visualizzare i backlink è necessario che la barra laterale dei commenti sia aperta. Se è chiuso, usa il menu Gear (**Proofing->Mostra commenti**) o premi {% kbd ^@c %} per aprirlo.


## Cronologia della navigazione

Marked tiene traccia della tua navigazione attraverso i collegamenti wiki, consentendoti di spostarti **avanti e indietro** nella cronologia dei file, proprio come un browser web.

- **Indietro:** {% kbd @[ %}
- **Avanti:** {% kbd @] %}

Puoi anche utilizzare il menu **Cronologia** per passare a qualsiasi file visitato in precedenza.