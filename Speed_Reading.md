# <%= @title %>

Speed Read is an RSVP-style reading mode that displays one word at a time in a focused overlay.

## How Speed Read works

Speed Read uses a method called **Rapid Serial Visual Presentation** (RSVP). Instead of moving your eyes across lines of text, the words appear in one fixed position. This reduces the eye movements, line changes, and backtracking that normally happen during reading, which can make it useful for skimming, reviewing familiar material, or moving quickly through text without losing your place.

The method is not magic, and it does not guarantee better comprehension at very high speeds. Reading comprehension still depends on the complexity of the writing, your familiarity with the subject, and the WPM setting. For dense or unfamiliar material, a moderate speed is usually more effective than pushing the rate as high as possible.

The red letter marks the word's visual anchor point, sometimes called the **optimal recognition point**. In many words, readers identify the word most efficiently when their gaze lands slightly left of center rather than at the first letter. By keeping that anchor point in the same place and highlighting it, Speed Read gives your eye a consistent target. The result is less refocusing between words and a steadier rhythm while the text advances.

## Opening Speed Read

Use **Preview > Speed Read**, the **Speed Read** item in the preview window Gear menu, or press {% kbd ctrl opt S %}. The menu item is available when a Markdown preview document window is active (it is disabled for raw HTML previews and when no document is open).

When Speed Read opens, it starts in a paused state so you can orient before playback begins.

<video controls preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Your browser does not support the Speed Read demo video.
</video>
<p><em>Speed Read overlay showing playback controls, sync option, and help access.</em></p>

## Overlay controls

Once the overlay is visible, these keys are available:

| Shortcut | Function |
| :-- | :-- |
| {% kbd space %} | Play/Pause |
| {% kbd [ %} | Jump to paragraph start (press again for previous paragraph) |
| {% kbd ] %} | Jump to start of next paragraph |
| {% kbd left %} | Decrease reading speed (WPM) |
| {% kbd right %} | Increase reading speed (WPM) |
| {% kbd esc %} | Exit Speed Read |

Brackets are captured for paragraph navigation, and left/right arrows are captured for speed changes, so these keys do not trigger preview navigation while Speed Read is open. You can also click the circular **X** button in the upper-left corner of the overlay to dismiss it.

Other normal preview navigation shortcuts still work while Speed Read is active, including `t`/`gg` (top), `G`/`b` (bottom), and `,`/`.` (header navigation). See [Preview Navigation](Keyboard_Shortcuts#preview-navigation) for the full list.

The Table of Contents can also be used while Speed Reading. Press {% kbd cmd t %} to open it and navigate, or press {% kbd f %} to immediately focus the quick search to navigate document headers.

## Starting from a selection

If text is selected in the preview when you start Speed Read, playback uses the selected text. If no selection is active, Speed Read uses the full document text.

## Syncing with scroll position

Enable **Sync Speed Reading with Scroll Position** in {% prefspane Preview %}, or use the checkbox in the Speed Read overlay, to keep the preview and Speed Read position together.

When this option is enabled, Speed Read starts at the content currently visible at the top of the preview instead of the beginning of the document. As playback advances, the preview scrolls along with the displayed words.

If you close Speed Read, scroll the preview, and reopen the overlay, playback starts from the new visible position. If you turn the overlay checkbox on after Speed Read is already open, playback resets to the current scroll position and continues from there.

## Remembered speed

The WPM value is saved automatically when you change it with {% kbd ← %} and {% kbd → %}. Your chosen speed is restored the next time you use Speed Read.
