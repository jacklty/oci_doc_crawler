Updated 2024-11-18
# Getting a VNIC Attachment's Details for Roving Edge Infrastructure
Describes how to get the details of a VNIC attachment on your Roving Edge Infrastructure devices.
Use this command to get the VNIC VLAN tag and other properties.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the VCNs displayed to that state.
    3. Click the instance associated with the VNIC to which you want to assign a secondary private ID. The instance's **Details** page appears.
    4. Click **Attached VNICs** under **Resources**. The primary VNIC is listed.
    5. Click the VNIC whose details you want to get. The VNIC **Details** page appears.
  * Use the [oci compute vnic-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/vnic-attachment/get.html) command and required parameters to get the details of a VNIC attachment on your Roving Edge Infrastructure devices:
Copy
```
oci compute vnic-attachment get --vnic-attachment-id vnic-attachment-ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetVnicAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/GetVnicAttachment) operation to get the details of a VNIC attachment on your Roving Edge Infrastructure devices. 


Was this article helpful?
YesNo

