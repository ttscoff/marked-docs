# Custom processor permissions in MAS version

Due to sandboxing restrictions, the Mac App Store version of Marked is unable to execute certain types of binary tools as custom processors. If you run into this limitation, there are a few steps you can try.

1. Ensure that you've gone into **Marked** Settings ({% kbd cmd , %}), in the **Advanced** pane and clicked on "Update Permissions." This will attempt to grant Marked access to your entire default drive, clearing up issues with scripts and utilities that need to access temp folders and non-default locations.
2. Try using a script. Reference the utility you want to run (multimarkdown, kramdown, etc.) in a shell script. It can be a bash, Ruby, Perl, or Python script. Then set the processor in Advanced settings to the related shell or executable, and the parameters to the location of the script. For example, I can create a bash script saved to ~/scripts/mmd_wrapper.sh:

        #!/bin/bash
        cat | /usr/local/bin/multimarkdown

    Then make it executable (`chmod a+x ~/scripts/mmd_wrapper.sh`) and set up my Custom Processor settings:

        Processor: /bin/bash
        Arguments: /Users/me/scripts/mmd_wrapper.sh
3. Some executables (especially Pandoc) just won't work within sandboxing. In this case, please contact me via the error window that pops up upon execution to receive a crossgrade license to the direct version.

