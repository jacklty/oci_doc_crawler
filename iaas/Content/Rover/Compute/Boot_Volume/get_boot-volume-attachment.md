Updated 2024-09-16
# Getting a Boot Volume Attachment's Details for a Computer Instance on a Roving Edge Infrastructure Device
Describes how to get the details of a boot volume attachment for a compute instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the boot volumes displayed to that state.
    3. Click the instance whose attached boot volumes you want to list. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
    5. Click the boot volume whose attachments you want to list. The boot volume's **Details** page appears.
    6. Click **Attached Instances** under **Resources**. The **Attached Instances** page appears. All attached instances are displayed in tabular form.
  * Use the [oci compute boot-volume-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/get.html) command and required parameters to get the details of a boot volume attachment for a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute boot-volume-attachment get --boot-volume-attachment-id boot_volume_attachment_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetBootVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/GetBootVolumeAttachment) operation to get the details of a boot volume attachment for a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

