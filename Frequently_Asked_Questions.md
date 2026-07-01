# <%= @title %> [toc]

## License code has already been utilized [license_code_has_already_been_utilized]

If you do a fresh install of Marked 2 and receive the error "License code has already been utilized" when entering your license, please <a href="&#109;&#97;&#105;&#108;&#x74;&#111;&#x3a;&#x6d;&#x65;&#64;&#x62;&#x72;&#x65;&#x74;&#116;&#116;&#101;&#114;&#112;&#115;&#116;&#114;&#x61;&#46;&#99;&#x6f;&#x6d;">contact me</a> requesting a new license. **Please include the email address you registered under and/or your current license code.**

Early licenses generated for Marked had a usage limit instead of a machine limit, so 3 installs---even on the same machine---would use up activations. These limits have been corrected in more recently-generated licenses. Purchase of a Marked 2 license permits you to install Marked 2 on any machine you own, so don't hesitate to ask for a replacement if you run into issues.

[Table of contents](#toc)

## Site licenses and educational discounts [site_licenses_and_educational_discounts]

Discounted site/bulk licenses are available for Marked 2. To request a purchase link, please contact <a href="&#109;&#97;&#105;&#108;&#x74;&#111;&#x3a;&#x6d;&#x65;&#64;&#x62;&#x72;&#x65;&#x74;&#116;&#116;&#101;&#114;&#112;&#115;&#116;&#114;&#x61;&#46;&#99;&#x6f;&#x6d;">&#x42;&#x72;&#101;&#x74;&#x74;</a> and specify the number of licenses you'd like to purchase.

**Discounts**

- 5-9: **10% off**
- 10-19: **12% off**
- 20-49: **15% off**
- 50+: **20% off**

An educational discount is also available for both the direct and Mac App Store versions. For the Mac App Store, standard Apple educational discounts are enabled. To purchase a direct version with an educational discount, <a href="&#109;&#97;&#105;&#108;&#x74;&#111;&#x3a;&#x6d;&#x65;&#64;&#x62;&#x72;&#x65;&#x74;&#116;&#116;&#101;&#114;&#112;&#115;&#116;&#114;&#x61;&#46;&#99;&#x6f;&#x6d;">contact me</a> and request a coupon.

[Table of contents](#toc)

## A URL won't validate or returns "Unknown" [a_url_wont_validate_or_returns_unknown]

Marked's [link validation](http://marked2app.com/help/Link_Validation.html) uses a basic HEAD request to determine whether a link is valid. Anything other than a 200 (success) result will give either an unknown, or an error if it's a common error code such as 404 (not found) or 500 (server error). URLs behind authentication (such as Apple Developer urls or anything that requires login to access) will return an "unknown", as will certain sites such as Amazon.com where the server returns bizarre response codes. There's not much Marked can do about this.

[Table of contents](#toc)

## Custom processor permissions in MAS version [custom_processor_permissions_in_mas_version]

Due to sandboxing restrictions, the Mac App Store version of Marked 2 is unable to execute certain types of binary tools as custom processors. If you run into this limitation, there are a few steps you can try.

1. Ensure that you've gone into **Marked 2** Preferences (⌘,), in the **Advanced** pane and clicked on "Update Permissions." This will attempt to grant Marked access to your entire default drive, clearing up issues with scripts and utilities that need to access temp folders and non-default locations.
2. Try using a script. Reference the utility you want to run (multimarkdown, kramdown, etc.) in a shell script. It can be a bash, Ruby, Perl, or Python script. Then set the processor in Advanced preferences to the related shell or executable, and the parameters to the location of the script. For example, I can create a bash script saved to ~/scripts/mmd_wrapper.sh:
    
        #!/bin/bash
        cat | /usr/local/bin/multimarkdown
    
    Then make it executable (`chmod a+x ~/scripts/mmd_wrapper.sh`) and set up my Custom Processor preferences:

        Processor: /bin/bash
        Arguments: /Users/me/scripts/mmd_wrapper.sh
3. Some executables (especially Pandoc) just won't work within sandboxing. In this case, please contact me via the error window that pops up upon execution to receive a crossgrade license to the direct version.

[Table of contents](#toc)

## Intra-document links in exported PDFs [intra-document_links_in_exported_pdfs]

Marked's PDF export currently uses WebKit's print features. One consequence of this is that intra-document (internal) links, including those in a Table of Contents, will not jump to other points in the document. This doesn't appear to be something Apple has any intention of fixing in the version of WebKit that Marked 2 uses.

In some cases you may get good results by exporting HTML with embedded Style and then using your web browser to print to PDF. You won't get all of Marked's export features, but you'll usually get a PDF with working internal links. It's a tradeoff for now.

[Table of contents](#toc)

## Relative paths in included files [relative_paths_in_included_files]

Files included using Marked's [include syntax][include], as well as [Scrivener files][scriv], can use relative paths to reference other files. (_**Note:** this doesn't apply to files included using IA Writer's `/file` syntax or CSV files_). As of recent versions (2.5.10+), these paths are _relative to the included file_, not the base file.

Given a file/folder structure like this:

    - base_file.md
    - subfolder
        - included_file.md
    - images
        - image1.jpg

If `included_file.md` references image1.jpg via a relative path, it needs to be written as `../images/image1.jpg`, _not_ `images/image1.jpg`. (`..` indicates the parent directory) .

[include]: http://marked2app.com/help/Multi-File_Documents.html
[scriv]: http://marked2app.com/help/Scrivener_Support.html

[Table of contents](#toc)

## How do I retrieve a lost license (direct version) [how_do_i_retrieve_a_lost_license_direct_version]

If you've lost a license you've purchased for Marked 2 through Paddle, you can retrieve it at [my.paddle.com](https://my.paddle.com/). If you have any trouble with logging in there, you can request a lookup via a private request on the [support site](http://support.markedapp.com).

[Table of contents](#toc)

## In-app purchase issues (Error Domain=Paddle Code=0 "(null)")  [in-app_purchase_issues_error_domainpaddle_code0_null]

Paddle recently informed me that IAPs are broken, and that they don't plan to fix it because not enough developers have implemented them. (Which is as frustrating to me as it is to you.) The truly frustrating part is that they haven't stopped allowing payments, so I need to manually refund purchases until something is done about the way the licenses are handled. A new system is supposedly going to roll out in the next couple of weeks, so if you're willing to wait, I'll do everything I can to ensure that all current purchases of the Spelling/Grammar IAP are honored through whatever system is provided next

If you do prefer a refund, just <a href="&#109;&#97;&#105;&#108;&#x74;&#111;&#x3a;&#x6d;&#x65;&#64;&#x62;&#x72;&#x65;&#x74;&#116;&#116;&#101;&#114;&#112;&#115;&#116;&#114;&#x61;&#46;&#99;&#x6f;&#x6d;">email me directly</a> with the email account used to license or the transaction ID from the receipt.

**Update:** Paddle has officially announced the new IAP solution, and it will be implemented as soon as it's publicly available. Current in-app purchase licenses (Spelling/Grammar) will be automatically migrated, and a new coupon code will be provided. This should happen soon.

[Table of contents](#toc)

## Fenced code blocks inside indented code blocks [fenced_code_blocks_inside_indented_code_blocks]

In fairly rare circumstances you may want to show the fences of a fenced code block. Normally this could be accomplished in Markdown by indenting the fenced code, forcing an indented "verbatim" block containing the fenced code block, which would then be unprocessed. Marked handles fenced code differently (as part of its ability to work with multiple syntax options), so to accomplish this you need to use a double fence. Because you can use any number of backticks or tildes to fence a code block (as long as the opening and closing count match, you can just use two different length fences. For example

    `````
    ```
    Actual fenced code
    ```
    `````

[Table of contents](#toc)

