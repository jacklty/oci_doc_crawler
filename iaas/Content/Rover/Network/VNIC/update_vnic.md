Updated 2024-11-18
# Editing a VNIC for Roving Edge Infrastructure
Describes how to edit a VNIC on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the VCNs displayed to that state.
    3. Click the instance associated with the VNIC you want to edit. The instance's **Details** page appears.
    4. Click **Attached VNICs** under **Resources**.
    5. Click the VNIC you want to edit. The VNIC **Details** page appears.
    6. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) to the right of the VNIC entry and select **Edit**. The **Edit VNIC** dialog box appears.
    7. Make your edits. See [Creating and Attaching VNICs](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm#top "Describes how to create and attach a secondary VNIC to your Roving Edge Infrastructure devices.") for descriptions of the settings
    8. Click **Save Changes**.
  * Use the [oci network vnic update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/update.html) command and required parameters to edit a VNIC on your Roving Edge Infrastructure devices:
Copy
```
oci network vnic update --vnic-id vnic-ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic) operation to edit a VNIC on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

