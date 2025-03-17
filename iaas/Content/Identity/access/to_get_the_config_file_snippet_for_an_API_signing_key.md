Updated 2025-02-18
# Getting the Configuration File Snippet for an API Signing Key
Find the configuration file snipped for an API signing key from the Console.
The following procedure works for a regular user or an administrator. 
  1. View the user's details:
     * If you're getting an API key configuration file snippet for _yourself_ : 
In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator getting an API key configuration file snippet for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Under **Resources** , click **API keys**. The list of API key fingerprints is displayed.
  3. Click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the fingerprint, and select **View configuration file**.
The **Configuration file preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config file`. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file.
If your configuration file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the configuration file.


Was this article helpful?
YesNo

