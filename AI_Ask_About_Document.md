# <%= @title %>

Ask About Document uses **Apple Intelligence** and the on-device language model built into recent versions of macOS to summarize your Markdown preview and answer questions about its content. All processing happens on your Mac; document text is not sent to Marked's servers or third-party AI services for this feature.

## What Apple Intelligence provides

Apple Intelligence is Apple's system for on-device generative features. Marked uses Apple's **Foundation Models** framework to access the same on-device model that powers system writing tools, exposed directly inside Marked for document-focused tasks.

Marked sends your document's plain text (Markdown syntax stripped for clarity) to this local model. The model generates summaries, outlines, and answers in a floating panel beside your preview window. Because the model runs locally, it works offline once Apple Intelligence is set up and the system model has finished downloading.

Apple Intelligence is best at language tasks such as summarization, outlining, extracting key points, and answering questions about provided text. It is not a general coding assistant or calculator, and very long documents are handled in sections so results stay within the model's context limits.

## System compatibility

Ask About Document appears only when your Mac can run the feature.

**Required:**

- **macOS 26 (Tahoe)** or later
- A **Mac with Apple Intelligence support** (Apple silicon Macs that meet Apple's device requirements)
- **Apple Intelligence turned on** in System Settings

**Not supported:**

- Intel Macs and other Macs marked as ineligible for Apple Intelligence
- macOS versions earlier than Tahoe 26
- Raw **HTML previews** (the feature is for Markdown and text-based document workflows)

If your Mac qualifies but the menu item is missing, confirm that Apple Intelligence is enabled and that you are running a current build of Marked that includes this feature. The menu is hidden entirely on unsupported systems rather than shown in a disabled state.

## Enabling Apple Intelligence

1. Open **System Settings**.
2. Go to **Apple Intelligence & Siri** (or **Apple Intelligence**, depending on your macOS version).
3. Turn on **Apple Intelligence** and complete any setup steps Apple requests.
4. Wait for the on-device model to finish downloading if prompted. Until the model is ready, Marked may show the menu item but display a message that Apple Intelligence is still preparing.

Marked does not include a separate preference for this feature. Availability follows the system model status reported by macOS.

## Opening Ask About Document

Open the panel using any of these methods:

- **Preview > Ask About Document…**
- Keyboard shortcut {% kbd shift ctrl cmd I %} (while a Markdown preview document is the active window)

The panel docks to the left side of the document window. You need an open document with readable text; an empty document or HTML-only preview will not offer the command.

## The Ask About Document panel

The panel is organized like a simple chat view:

- **Preset actions** at the top for common tasks
- A **response area** in the middle where summaries and answers appear (streaming as they are generated)
- A **question field** at the bottom where you type custom questions, with **Ask** and **Cancel** buttons

After a response completes, focus returns to the question field so you can ask a follow-up without clicking.

### Preset actions

| Action | What it does |
| :-- | :-- |
| **Summarize Document** | Produces a short cohesive summary of the full document. Long documents are summarized in sections and combined. |
| **Summarize Selection** | Summarizes only the text currently selected in the preview. Select text first; otherwise Marked prompts you to make a selection or use Summarize Document. |
| **Outline** | Builds a hierarchical outline of the document structure using headings and bullet points. |
| **Key Points** | Lists the most important points from the document as a bullet list. |

Preset actions do not require text in the question field. Click a button and wait for the response in the panel above.

### Asking your own questions

1. Type a question in the field at the bottom of the panel, for example "What problem does this document solve?" or "Who is the intended audience?"
2. Press **Return** or click **Ask**.
3. Read the answer as it streams into the response area.

For questions about a specific passage, **select that text in the preview** before asking. Marked sends the selection as context instead of the whole document when a selection is active.

Click **Cancel** to stop a request in progress.

## Examples

### Quick overview of a long article

Open a lengthy blog post or report in Marked, choose **Preview > Ask About Document…**, and click **Summarize Document**. Use the summary to decide whether to read the full piece or to refresh your memory after time away from the draft.

### Notes on a selected paragraph

Highlight a dense paragraph in the preview, open Ask About Document, and click **Summarize Selection**. Useful when you only need a shorter version of one section.

### Structural review

Click **Outline** on a draft with many headings to see whether the argument flows logically, or use **Key Points** before sending a document to someone else to check that the main ideas are clear.

### Targeted questions

With no selection active, type questions such as:

- "What are the three main recommendations?"
- "Does this document mention licensing?"
- "List any dates or deadlines mentioned."

With a selection active, ask narrower questions such as "What does this paragraph assume about the reader?" or "Rewrite this idea in one sentence" (the model answers about the selection; it does not edit your source file).

## Tips and limitations

- **Privacy:** Processing uses Apple's on-device model. Marked still reads your document text locally to provide content to that model; treat sensitive material accordingly.
- **Accuracy:** Verify important facts against your source. AI summaries can omit details or misread ambiguous passages.
- **Length:** Extremely long documents are processed in chunks. Summaries and answers reflect the full text indirectly; for precision on one section, select that section first.
- **Language:** Results follow the language capabilities of the system Apple Intelligence model on your Mac.
- **Refusals:** The system may decline some requests based on Apple's safety policies.

If Ask About Document is unavailable, check System Settings for Apple Intelligence status and ensure you are previewing a Markdown document on a supported Mac running macOS 26 or later.
