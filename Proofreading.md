# <%= @title %>

Enter proofreading mode from the gear menu. This is an experimental feature designed primarily for editors who receive text from others and need to make comments and provide feedback.

Proofreading mode freezes document updates, preventing annotations and notes from being lost when the document refreshes. A red indicator shows up in the top bar to remind you that proofreading mode is active.

Keyboard navigation, bookmarking and keyword highlighting all function when proofing.

## Annotations

While in proofreading mode, selecting text in the document will generate a popup that allows you to select from several different highlight types. Click the type of highlight you want to add to the text, or cancel by clicking the "Cancel" button or just clicking outside of the popup.

## Notes

![Annotations][1]

[1]: images/Annotating.jpg class=center

Once a highlight is added, you can add short notes to it by clicking the highlight. The popup will now contain a text field where you can enter whatever notes may be pertinent to the highlighted text. Notes can be deleted and edited by clicking a highlight which already has a note.

Notes are **only** exported when saving to HTML. Highlights remain in most export formats, including RTF and PDF.

## Spellcheck

While in proofreading mode, you can access the system-wide spell checker from the gear menu: {% appmenu {{gear}}, Proofing, Highlight All Spelling Errors %}. This will be slow on large documents, and a warning will be displayed notifying you if the process will take over 30 seconds or so. Because the spell checker doesn't function in Marked's web preview, a "hack" is implemented to make this work, and it's not a speedy one.

Once spell check has run, you can open the Spelling Guesses panel to turn on Grammar Checking as well as see the suggestions for fixing errors. Marked *cannot* edit these in place, you have to go back to your original document to make use of the results.

*Shortcuts:* {% kbd ctrl opt cmd S %} will run the spell checker. {% kbd ctrl opt cmd N %} will traverse to the next error in the document, and {% kbd ctrl opt cmd G %} will show the guesses panel.
