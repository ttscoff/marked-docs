# <%= @title %>

The Mac App Store (MAS) version of Marked runs in a sandboxed environment that restricts certain operations for security reasons. This can affect some features, particularly when using Custom Processors with external binaries or scripts.

## Common Sandbox Restrictions [common-sandbox-restrictions]

### Run Command Binaries [run-command-binaries]

The most common issue users encounter is that external binaries cannot be executed directly in the MAS version. This affects:

- **External processors** like Pandoc, Kramdown, or other command-line tools
- **Custom scripts** that rely on external binaries
- **System utilities** that aren't accessible from the sandbox

### Workarounds [workarounds]

#### Copying Binaries to the App Bundle [copying-binaries-to-the-app-bundle]

If you need to use external processors like Pandoc in the MAS version, you can copy the binary into the app bundle:

1. Right-click Marked.app → **Show Package Contents**
2. Navigate to **Contents/Resources/**
3. Create a `bin` folder if it doesn't exist
4. Copy your binary (e.g., `pandoc`) into this `bin` folder
5. Make it executable: `chmod +x` the binary
6. In the Run Command action, reference it as:
   - `YOUR_BINARY_NAME [arguments]`
   - Or use the full path: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Note**: Scripts with external shebangs (like Python scripts pointing to `/opt/homebrew/bin/python`) will automatically be executed through system interpreters when copied to the bundle. The MAS version may still have trouble executing binaries that are actually Python or Ruby scripts instead of binary files.

**Important**: You'll need to re-copy binaries after each app update, as updates replace the entire bundle.

#### Using Embedded Scripts [using-embedded-scripts]

Instead of running external commands, you can use the **Run Embedded Script** action in Custom Rules. This allows you to write scripts directly in Marked's code editor, which can access system interpreters that are available within the sandbox.

## Switching to the Non-Sandboxed Version [crossgrade]

If you frequently need to use external binaries or encounter other sandboxing limitations, you may want to switch to the non-sandboxed version of Marked. The non-sandboxed version has no such restrictions and can execute any command-line tool or script you have installed.

### For Subscription Users [for-subscription-users]

If you have an active Mac App Store subscription:

1. **Cancel your MAS subscription** in System Settings → Apple ID → Media & Purchases → Subscriptions
2. **Download the Free Trial** from [https://markedapp.com](https://markedapp.com)
3. **Start a Paddle subscription** directly through the app or website

The Paddle version offers the same features without sandboxing restrictions.

### For Permanent Unlock Holders [for-permanent-unlock-holders]

If you have purchased a permanent unlock or lifetime license through the Mac App Store, please [email the developer](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Please%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.) to request a free lifetime Paddle license.

**Important**: To verify your purchase, please include one of the following in your email:

- Your **user identifier** (UUID) - use **Help->Copy UUID** to copy it to your clipboard, then paste it into your email
- Your **transaction ID** from your App Store receipt (you can find this in your purchase history in the App Store app)

The Mac App Store doesn't provide your email address to developers, so we verify purchases using transaction IDs or user identifiers stored on our server. Including this information will help us quickly verify your purchase and generate your free Paddle license.

### Setapp Version [setapp-version]

Alternatively, if you have a Setapp subscription, you can use the Setapp version of Marked, which is also non-sandboxed and has full access to system resources.

## Additional Resources [additional-resources]

For more information about Custom Processors and their capabilities, see [Custom Processor](Custom_Processor.html).

