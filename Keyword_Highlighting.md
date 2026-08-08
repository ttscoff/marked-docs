# <%= @title %>

Catching troublesome verbiage and spotlighting important phrases.

## Highlighting Keywords [highlighting-keywords]

Keyword highlighting in Marked allows you to catch common phrases that you might want to avoid, find alternate terms for or just highlight for general purposes. The list of keywords used to match each category can be edited in the {% prefspane Proofing %}.

Enable highlighting with {% kbd shift cmd H %}, from the gear menu ({% appmenu {{gear}}, Highlight Keywords %}), or open the keyword drawer using the highlighter icon in the lower left (near the gear menu). The drawer can be opened with the keyboard shortcut {% kbd shift cmd K %} as well. Highlighting is automatically enabled when the drawer is opened, and can be toggled on and off with the switch on the left side of the drawer.

## The Keyword Drawer [the-keyword-drawer]

![Keyword Drawer][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

The Keyword Drawer that's revealed when enabling highlighting provides quick access to highlighting options, including the ability to enable and disable individual highlight types. The vertical row of colored labels on the left side correlates to the highlights in the text. Clicking a label toggles highlights for that keyword type.

To the left of each label is a target icon. Clicking this will begin scrolling the document to the next instance of the highlight in document order. To the right of the label is a count showing the total number of highlights for that type.

You can navigate quickly through the highlights using the keyboard. Typing `[` and `]` will initially move forward and backward through all the highlights. If you click a target icon, `[` and `]` will switch to navigating just that type of highlight. `{` (Shift-[) and `}` (Shift-]) will always navigate all highlights, regardless of the last target clicked.

If a highlighted word or phrase is clicked, that type will become the target for navigation and using `[` or `]` will navigate from that point in the document.

## Editing Keywords [editing-keywords]

![Proofreading Settings][proofprefs]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

By default Marked uses the [Plain English Campaign's](http://www.plainenglish.co.uk) list of overused words and phrases. You can add to or replace these easily by editing them in the {% prefspane Proofing %}. Each field is free-form text, and each line is interpreted as a search phrase. Use `*` at the beginning of a phrase or word to match any preceding text, and `?` to match a single character as a wildcard.

Regular expressions can be used by surrounding the expression with forward slashes:

    /\\S*?ly/

The above will match any words ending in "ly" for highlighting. The syntax for regular expressions in Marked's keyword highlighting is the [same as JavaScript](http://www.regular-expressions.info/javascript.html).

## Temporary Keywords [temporary-keywords]

You can also add temporary keywords in the Keyword Drawer by editing the notepad. Just like in the {% prefspane Proofing %} fields, you add one keyword or phrase per line, regular expressions allowed (surrounded by forward slashes). After editing temporary keywords, be sure to click the "Update" button (or press {% kbd cmd return  %}) to save the changes and see them highlighted in your document.

Regular expressions work in the temporary keyword field as well, just surround the text with forward slashes (`/my expression\b/`).

Temporary keywords are intended for situations where keyword density is important, and allow you to quickly see how many times you've used the target words, highlighting their locations in the document. A count of matches for the temporary keywords is prominently displayed in the drawer.

Also see the ["Visualize Word Repetition"][wordrep] command to find overused words in your text.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Passive Voice [passive-voice]

Marked will point out usage of "passive voice" in English text. As [defined by Wikipedia][passive]:

> the grammatical subject expresses the theme or patient of the main verb – that is, the person or thing that undergoes the action or has its state changed.

Passive voice isn't evil, as you can read about [in posts by linguist Geoffrey K. Pullum][gkp]. Marked points out passages using passive voice, but the decision as to their validity is yours.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Doubled Words [doubled-words]

Double words (e.g. "the the") are automatically highlighted in orange when Keyword Highlighting is enabled. This is currently not configurable, but should prove handy for proofreading.
