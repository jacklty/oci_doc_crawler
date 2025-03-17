Updated 2024-09-16
# Getting a Block Volume Attachment's Details within a Roving Edge Infrastructure Device
Describes how to get the details of a block volume attached to a compute instance on your Roving Edge Infrastructure device.
See [Listing Volume Attachments](https://docs.oracle.com/iaas/Content/Block/Tasks/listingvolumeattachments.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance to which you want to attach a block volume.
    4. Click **Attached Block Volumes** in the lower left corner. All attached block volumes are listed in tabular form.
    5. Click the block volume whose details you want to get. The block volume's **Details** page appears.
  * Use the [oci compute volume-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/get.html) command and required parameters to get the details of a block volume attached to a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute volume-attachment get --volume-attachment-id volume_attachment_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment) operation to get the details of a block volume attached to a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

