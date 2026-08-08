<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

La convalida del collegamento esegue il ping della destinazione di un URL e verifica la presenza di errori. Ciò aiuta a evitare collegamenti interrotti e non validi nel documento pubblicato ed è particolarmente utile per i blogger.

## Convalida dei collegamenti singoli [validating-single-links]

![][1]

   [1]: images/validate_single.png @2x width=832px height=267px class=center

Fare clic e tenere premuto su un collegamento nell'anteprima finché non lampeggia, quindi rilasciare per aprire il menu delle azioni del collegamento. Scegli "Convalida collegamento" per eseguire il test. I risultati vengono visualizzati nel popup.

## Convalida di tutti i collegamenti [validating-all-links]

![][2]

   [2]: images/screenshots/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Scegli "Convalida tutti i collegamenti" (scorciatoia {% kbd ctrl cmd L %}) dal menu ingranaggio o dal menu contestuale. Tutti i collegamenti remoti nel documento verranno controllati e i risultati verranno visualizzati in un popup. Facendo clic su un collegamento nel popup si scorrerà ed evidenzierà il rispettivo collegamento nel documento.

Gli URL validi possono essere nascosti dal popup con il pulsante "Nascondi validi" nella parte superiore. Verranno visualizzati solo gli URL che hanno restituito uno stato di errore.

Premendo Escape si nasconderanno i risultati della convalida. Possono essere rivelati nuovamente utilizzando {% kbd ctrl cmd L %} o il menu Gear.

## Convalida automatica [validating-automatically]

Attiva "Convalida automaticamente gli URL all'aggiornamento" nelle impostazioni di anteprima (o nella parte inferiore del popup di convalida del collegamento). Quando il documento viene caricato, i collegamenti contenuti verranno testati in background. Verrà visualizzata una finestra di dialogo solo se sono presenti errori.

Per disabilitare il popup, disattivalo nelle impostazioni o deseleziona la casella nella parte inferiore della finestra popup.