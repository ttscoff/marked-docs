# <%= @title %>

[Bear][bear] can send a live preview straight to Marked.

## Sending from Bear [sending-from-bear]

In Bear choose **Preview in Marked** from the **View** menu (wording may vary slightly by Bear version). Marked receives a TextBundle, so embedded images and assets generally travel with the text.

Images referenced with absolute paths or `https` URLs also resolve as long as Marked can reach them.

## Mac App Store note [mac-app-store-note]

If you use the **Mac App Store** build of Marked and macOS keeps asking for permission to open directories when previewing from Bear, [contact Marked support](http://support.markedapp.com) for a free cross-grade to the direct-download edition, which avoids that particular sandbox friction.

## Tags [tags]

Bear-style tags can be rendered as such by turning on **#Text is tag** and **Style tags** under {% prefspane Processor %}.

W> This setting can confuse Marked if you write regular headlines without spaces after the `#`.

## Filenames and export [filenames-and-export]

If you turn on **Use first H1 as fallback title** in {% prefspane Export %}, that title can drive the filename and the `%title` placeholder when you print or export PDFs from Marked.

I> A preview style that approximates Bear's own look [is available on markedapp.com/styles](https://markedapp.com/styles/preview?style=bear).

Streaming preview from Bear is summarized on the [Streaming Preview](Streaming_Preview.html) page and in [Additional app integrations](Additional_Application_Support.html).

[bear]: https://bear.app/
