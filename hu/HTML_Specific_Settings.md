<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Az automatikus fejlécazonosítók letiltása [disable-automatic-header-ids]

A Megjelölt lehetőséget tartalmaz az automatikus fejlécazonosító-generálás letiltására. Ezt a lehetőséget a {% prefspane Processor %} oldalon találja.

## Véletlenszerű lábjegyzetazonosítók [random-footnote-ids]

A **Feldolgozó** panelen bejelölheti a "Véletlen lábjegyzet-azonosítók használata" lehetőséget, hogy véletlenszerű lábjegyzet-azonosítókat generáljon, ami segít elkerülni az ütközéseket, amikor több dokumentum jelenik meg egy weboldalon. Ez az opció csak MultiMarkdown processzor használata esetén érhető el.

## Folyamat jelölése a HTML-ben [process-markdown-inside-of-html]

Alapértelmezés szerint a Markdown processzorok általában figyelmen kívül hagyják a HTML blokkcímkéken belüli Markdown szintaxist. Ez az opció arra kényszeríti a Marked-et, hogy folytassa a feldolgozást a blokkelemeken belül. Vegye figyelembe, hogy bizonyos jelölések problémákat okozhatnak.