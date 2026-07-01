# <%= @title %>

Keep track as you write.

## Word Count and Document Statistics

![][1]

   [1]: images/WordCount.jpg @2x width=840px height=61px class=center

Word count is located in the bottom status bar and can be enabled and disabled from the {% prefspane General %} under Status Bar. You can view further statistics in the preview or source window from the gear menu, clicking the word count or by typing Option-Command-S ({% kbd opt cmd S %}). Hold down the Option ({% kbd opt  %}) key while clicking to show Readability Statistics, and hold down Option-Command ({% kbd opt cmd %}) to open the Advanced Statistics panel.

If text is selected, the word count display and the paragraph/sentences/character popup will update with info just for the selection.

## Word Count for Selection

![Word count popup on text selection][2]

   [2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

When you select text in the preview, the word count at the bottom of the window will show statistics for the selected text only.

If "Show Word Count For Selection" is enabled in the {% prefspane Preview %}, a small popup will pop up by the cursor to show the word/line/character count for the selected text. This is dismissed simply by moving the mouse away from the popup.

The zoom feature is handy for quickly selecting and getting counts for larger chunks of text. Type {% kbd z %} to zoom out and make your selection.

## Readability Statistics

![Readability stats bar][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

Additional statistics from Flesch/Kincaid and the Fog Index are available with {% kbd opt shift cmd S %}.

### Readability information

**Flesch Reading Ease:** higher scores indicate material that is easier to read; lower numbers mark passages that are more difficult to read.

**90.0--100.0**: average 11-year-old student
**60.0--70.0**: 13-to-15-year-old students
**0.0--30.0**: university graduates

**Flesch-Kincaid Grade Level:** the number of years of education generally required to understand this text.

**Gunning fog index:** measures the readability of English writing. The index estimates the years of formal education needed to understand the text on a first reading. A fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old).

## Advanced Statistics

![Advanced Statistics popup][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Selecting Advanced Statistics from the gear menu ---- or pressing {% kbd cmd I %} --- will drop down a panel containing more advanced document statistics including average word and sentence length and average word complexity.

### Floating Advanced Statistics

![Floating Info Window][floating]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Pressing {% kbd shift cmd I %} will open a floating panel containing all of the detailed stats and readability information. This panel can remain in the forefront when you switch to your editor, so you can see your statistics update every time you save, whether the preview is visible or not. Pressing the `<` icon will return the associated Marked Preview to the foreground. If you hold down option and click the same button, it will open the Markdown file in your default text editor (set in the {% prefspane Apps %}).

### Word Targets

If you have a specific target for word count as you're writing, you can add a "target:" metadata key at the top of your document and Marked will track your progress, displaying a completion indicator in the Detailed Statistics panel ({% kbd cmd I %}) and in the Floating Stats ({% kbd shift cmd I %}).

![][targetwordcount]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualize Word Repetition

Selecting Visualize Word Repetition from the gear menu (or pressing {% kbd ctrl cmd W %}) will switch to a special view which removes non-text elements and highlights words that are repeated in your document. Repeated words are highlighted in light pink, and hovering over a highlighted word will brighten the matching words throughout the document. Clicking a highlighted word will darken the background and "stick" the highlighting for further review.

![Word Repetition][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

You can use the "zoom" feature (type "z") in this mode as well, allowing you to highlight a repeated word, then quickly scan the entire document to see where repeats are concentrated.

Words are compared by their "stem," meaning that "part," "partly," and "parts" will be considered repeated words. This accounts for syllables and conjugation when checking for repeat density.

**Scope**

The scope of the repetition check can be changed in the bottom toolbar for the document, and can be set to Document or Paragraph. Document mode is default; selecting Paragraph only counts repetition within each block of text. Repeats will still be highlighted through the entire document, but only counted if a word appears more than once within a single paragraph.

**Ignoring words**

You can temporarily exclude a word and all of its various conjugations and pluralizations by Option-Clicking on the highlighted word. Temporarily ignored words will appear in the lower right corner of the preview. Clicking a word in the ignored word list will restore it to the visualization.

To permanently ignore words, you can edit a list in the {% prefspane Proofing %} under the Ignore Repeats tab. Words (or word stems) added one-per-line in this list will always be ignored. To automatically add a word to this list, Option-Shift-Click it in the word repetition visualization.

**Exiting Word Repetition mode**

You can close the word repetition view using the Close icon next to the scope selector in the bottom toolbar or by pressing escape.
