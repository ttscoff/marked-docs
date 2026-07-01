# Markdownifier

The Markdownifier is a tool that automatically extracts content from web pages and converts it to clean Markdown format. It intelligently processes web content to give you just the meaningful text and structure, filtering out ads, navigation elements, and other clutter.

![Markdownify URL][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## How It Works

The Markdownifier uses advanced content extraction algorithms to:

1. **Fetch and analyze** web page content
2. **Identify the main article** text and structure
3. **Clean and format** the content into proper Markdown
4. **Filter out** advertisements, navigation, and other non-content elements
5. **Preserve** important formatting like headers, lists, and links

## Opening the Markdownifier

To access the Markdownifier, open {% appmenu File, New, Markdownify URL (@~k) %}. Enter the URL you want to Markdownify and press Return ({% kbd return %}).

## Using the Markdownifier

### Basic Usage

1. **Open the Markdownifier** using any of the methods above
2. **Enter a URL** in the text field
3. **Click "Automatic"** or press `Return` to extract content
4. The extracted content will **automatically open** in a new Marked document

### Manual Content Selection

If automatic extraction doesn't capture the content you want:

1. Click the **"Manual"** button to load the page in a web view
2. **Navigate and scroll** to find the content you want
3. **Click the "Extract Content"** button that appears over the web page
4. The selected content will be converted to Markdown and opened in Marked

### Clipboard Integration

The Markdownifier automatically detects URLs in your clipboard when opened:

- If a URL is found, it will be **pre-filled** in the URL field
- You still need to click **"Automatic"** or press `Return` to process it
- This prevents accidental processing of clipboard URLs

## Content Processing

### Automatic Content Validation

The Markdownifier intelligently validates extracted content to ensure it contains meaningful text:

- **Strips metadata** (YAML frontmatter, MultiMarkdown headers)
- **Removes link definitions** and reference-style links
- **Filters out** standalone URLs and navigation elements
- **Compresses whitespace** for accurate length assessment
- **Requires minimum 200 characters** of actual content

If the extracted content is too short or appears to be mostly navigation/ads, the Markdownifier will automatically fall back to manual selection mode.

### Content Formatting

The extracted content is formatted as clean Markdown with:

- **Source link** at the top: `[source](original-url)`
- **H1 title insertion** when needed
- **Preserved lists** (ordered and unordered)
- **Maintained links** and emphasis formatting
- **Clean paragraphs** with proper spacing

## Safety Features

### Crash Prevention

The Markdownifier includes several safety measures to prevent crashes:

- **Blocks problematic URLs** (ad networks, tracking services, crypto-related content)
- **Filters corrupted images** that could cause rendering issues
- **Disables advanced web features** that might cause instability
- **Automatic crash recovery** with safe mode fallback

### Privacy Protection

- **Private browsing mode** prevents tracking and cookies
- **No plugins or Java** execution for security
- **Limited JavaScript** with crypto API blocking
- **Resource filtering** blocks tracking and ad content

## Troubleshooting

### Content Not Extracted

If automatic extraction fails:

1. **Try manual selection** using the "Manual" button
2. **Check if the site requires JavaScript** - some sites need manual loading
3. **Verify the URL** is accessible and contains article content
4. **Look for paywalls or login requirements** that might block access

### WebView Issues

If the web view becomes unstable:

1. The Markdownifier will **automatically enter safe mode**
2. **JavaScript will be disabled** to prevent crashes
3. **Use the "Convert" button** instead of manual selection
4. **Close and reopen** the Markdownifier to reset

### Missing Content

If important content is missing from the extraction:

1. The **automatic algorithm** might have filtered it out
2. **Use manual selection** to choose the specific content you want
3. **Check the source HTML** to see if content is dynamically loaded
4. **Try a different URL** if the site has complex structure

## Tips for Best Results

### URL Selection

- **Use article URLs** rather than homepage or category pages
- **Avoid URLs with tracking parameters** when possible

### Content Quality

- **Longer articles** generally extract better than short posts
- **Well-structured content** with proper headings works best
- **Avoid sites with heavy JavaScript** for automatic extraction

### Manual Selection

- **Wait for the page to fully load** before extracting
- **Scroll through the content** to ensure everything is loaded
- **Hover over areas** to select the smallest blue box that contains all of the content you want to extract
- **Click** when you've found the content you want

## Advanced Features

### Batch Processing

While the Markdownifier processes one URL at a time, you can:

- **Queue multiple URLs** by opening the Markdownifier multiple times
- **Use Services integration** to process URLs from other applications
- **Copy extracted content** and paste into existing Marked documents

### Integration with Marked

Extracted content opens in Marked with:

- **Automatic file naming** based on the article title
- **Source URL preservation** in the document metadata
- **Full Marked capabilities** for reading and exporting)

## Technical Details

### Supported Content Types

- **HTML articles** with standard markup
- **Blog posts** and news articles
- **Documentation** and help pages
- **Forum posts** and discussion content

### Limitations

- **Paywalled sites** may require login and manual extraction
- **JavaScript-heavy sites** may require manual selection
- **Dynamic content** loaded after page load may be missed, but manual extraction can capture it
- **Complex layouts** might include unwanted navigation elements

The Markdownifier is designed to make web content extraction as simple and reliable as possible, while providing fallback options for complex or problematic websites.
