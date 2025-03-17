Updated 2025-03-14
# Listing Block Volume Attachments within a Roving Edge Infrastructure Device
Describes how to list the block volumes attached to a compute instance on your Roving Edge Infrastructure device.
See [Listing Volume Attachments](https://docs.oracle.com/iaas/Content/Block/Tasks/listingvolumeattachments.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance to which you want to attach a block volume under **Instances**.
    4. Click **Attached Block Volumes** in the lower left corner. All attached block volumes are listed in tabular form.
  * Use the [oci compute volume-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/list.html) command and required parameters to list the block volumes attached to a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute volume-attachment list --compartment-id <compartment_OCID> --instance-id <instance_OCID> [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/ListVolumeAttachments) operation to list the block volumes attached to a compute instance on your Roving Edge Infrastructure devices. 


Was this article helpful?
YesNo

