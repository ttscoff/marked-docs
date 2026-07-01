# <%= @title %>

Extract and steal styles from any website.

## What is the Style Stealer?

The Style Stealer is a tool that allows you to extract CSS styles from any website and apply them to your Markdown documents as [Custom Styles](Custom_Styles.html). It's perfect for:

- **Bloggers** who want to match the styling of their favorite websites
- **Writers** who need to create documents that match a specific brand or publication
- **Developers** who want to quickly prototype with existing design systems
- **Anyone** who wants to capture the look and feel of any well-designed website

> The Style Stealer depends on a site to be relatively well laid out with clear markup divisions. It won't work on every site, but it should do a good job on most.

> For the best results, enter a page that contains as much text content as possible. For example, to extract styles from a blog, open directly to an article or post, not to the main index page.

## How to Use the Style Stealer

### Step 1: Open the Style Stealer

Access the Style Stealer through the **Help** → **Style Stealer**.

### Step 2: Enter a URL

In the URL field, enter the address of the website you want to extract styles from. The Style Stealer works with any publicly accessible website. If the site is behind a paywall you may have to log in to be able to extract the content.

![Style Stealer Preview][preview]

  [preview]: images/style-stealer-preview.jpg @2x width=800

### Step 3: Load and Navigate

Click **Extract** or press {% kbd return  %} to load the website. Once loaded, you can:

- **Navigate** the site using Command+Click on links
- **Hover** over content areas to see them highlighted
- **Click** on the main content area you want to extract styles from

The main content area you select should only contain headlines, paragraphs, lists, etc. Do not select a content area that contains menus, sidebars, or other extraneous content. Often a headline will be in a separate container from the regular paragraph content. In these cases, first try selecting the smallest container that still contains both. If the results are poor, click **Extract** again and re-select just the container that holds the paragraphs.

### Step 4: Extract Styles

When you click the content area, the styles that apply to that area will be extracted. The preview will reload with a generic page that showcases all common HTML elements and how the extracted styles will apply to them.

You can then save this Custom Style to your Custom CSS folder for use in any document. Click the **Save** button or press {% kbd cmd S %} to save. The style will be named based on the domain of the URL you entered.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## What Gets Extracted

The Style Stealer captures a comprehensive set of styles including:

### Typography

- **Font families** and sizes for all heading levels (H1-H6)
- **Paragraph** styling including line height and spacing
- **Text colors** and background colors
- **Font weights** and styles (bold, italic, etc.)

### Layout and Spacing

- **Margins and padding** for all elements
- **Border** styles and colors
- **Background colors** including body backgrounds for dark themes

### Interactive Elements

- **Link styles** including hover and visited states
- **Button** and form element styling
- **List** styling (bullets, numbers, indentation)

### Special Features

- **First paragraph** styling
- **Blockquote** formatting
- **Code** and pre-formatted text styling
- **Table** styling
- **Custom font faces** and web fonts

## Advanced Features

### Media Blocking

The Style Stealer automatically blocks media content (videos, images, audio) to prevent crashes and focus on text styling. This ensures a smooth extraction process even on media-heavy websites.

### Pseudo-Selector Support

The tool captures CSS pseudo-selectors like:

- `:hover` states for links and buttons
- `:visited` link states
- `:first-child` paragraph styling
- `::first-letter` for drop caps

### Smart Filtering

The Style Stealer intelligently filters out:

- Default browser styles
- Unnecessary vendor prefixes
- Conflicting or redundant rules
- Styles that would make text unreadable

### Debug Mode

Enable debug mode in the Style Stealer to see detailed logging of the extraction process. This is helpful for troubleshooting or understanding what styles are being captured.

## Tips for Best Results

### Choose the Right Content Area

- Click on the **main content area** of the page, not headers, sidebars, or footers
- Look for the area that contains the article text, blog post, or main content
- Avoid areas with heavy JavaScript or dynamic content

### Handle Dark Themes

The Style Stealer automatically captures body background colors, making it perfect for extracting dark theme styles. The preview will show how your content looks with the extracted dark styling.

### Font Considerations

- **Web fonts** are captured and included in the extracted styles
  - Fonts that are loaded from a remote URL (e.g. Google Fonts) will maintain that URL. Fonts loaded from data URLs will be duplicated in the generated stylesheet.
- **System fonts** will fall back gracefully on different systems
- **Font loading** may take a moment in the preview

### Testing Your Styles

After saving extracted styles:

1. Apply them to a test document
2. Check how they look with your actual content
3. Make adjustments by:
   1. Open the {% prefspane Style %}
   2. Select the new style in the Custom Styles table
   3. Click Reveal to show the file in Finder
   4. Open the file in any plain text editor (TextEdit will work in plain text mode) and make adjustments as needed

## Troubleshooting

### Website Won't Load

- Check that the URL is correct and publicly accessible
- Some sites may block automated access
- Try a different page on the same site

### Styles Look Different

- The extracted styles are based on the specific content you selected
- Some sites use complex CSS that may not translate perfectly
- Use Additional CSS or edit the stylesheet to make fine adjustments

### Missing Styles

- Ensure you selected the main content area, not a sidebar or header
- Some styles may be applied via JavaScript and won't be captured
- Check the debug console for detailed extraction information

## Keyboard Shortcuts

- {% kbd return  %} - Load URL for extraction
- {% kbd cmd S %} - Save the extracted style to a Custom Style CSS file
- {% kbd cmd  %}-Click - Navigate links while previewing

## Integration with Custom Styles

Extracted styles are saved to your Custom CSS folder and can be:

- **Applied** to any document through the Style menu
- **Modified** using any text editor
- **Shared** with others by copying the CSS file
- **Combined** with other custom styles

The Style Stealer makes it easy to build a library of beautiful styles inspired by the best-designed websites on the internet.
