Updated 2024-02-13
# Using Fiddler to Capture HTTP Traffic
You can use Fiddler to view and debug HTTP traffic between a client and a host computer.
  1. Download the Fiddler installer.
  2. Run the Fiddler installer and follow the wizard to install Fiddler on your client machine.
  3. Stop all other programs and services that might access the internet or use HTTP. This helps to obtain a clean and uncluttered trace.
  4. Select the Fiddler icon in the workstation's Start menu to run Fiddler.
Fiddler starts capturing events as soon as it runs. Fiddler logs all network requests instantly and these requests are summarized in the left-hand pane of the tool.

The individual sections of the Fiddler trace are color coded. Each color is meaningful, but failures are shown in red. The result column contains the HTTP code that the section returned. For example, if a section returned an HTTP 404 or Not Found error message, the section would be red. Since we are typically looking for errors or failures, the sections we want to concentrate on are the red sections in the trace. Fiddler creates a file containing the trace with a file extension of `.saz`.
Was this article helpful?
YesNo

