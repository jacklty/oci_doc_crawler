Updated 2024-09-16
# Detaching and Deleting a VNIC from Roving Edge Infrastructure
Describes how to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to detach and delete a secondary VNIC. The instance's **Details** page appears.
    4. Click **Attached VNICs** under **Resources**.
The primary VNIC and any secondary VNICs attached to the instance are is displayed.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) to the right of the secondary VNIC you want to delete and select **Delete VNIC**.
    6. Confirm the detachment when prompted.
It takes typically a few seconds before the VNIC is deleted.
  * Use the [oci compute instance detach-vnic](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/detach-vnic.html) command and required parameters to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices:
Copy
```
oci compute instance detach-vnic --compartment-id compartment_ocid --vnic-id vnic-ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DetachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/DetachVnic) operation to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

