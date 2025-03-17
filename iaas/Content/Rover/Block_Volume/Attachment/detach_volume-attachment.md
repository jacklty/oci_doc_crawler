Updated 2024-09-16
# Detaching a Block Volume from a Roving Edge Infrastructure Device
Describes how to detach a block volume from a compute instance on your Roving Edge Infrastructure device.
See [Detaching a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/detachingavolume.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance from which you want to detach the volume under **Instances**. The instance's **Details** page appears.
    4. Click **Attached Block Volumes** in the lower left corner. All attached block volumes are listed in tabular form.
    5. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the block volume you want to detach and click **Detach**.
    6. Confirm the detachment when prompted.
  * Use the [oci compute volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/detach.html) command and required parameters to detach a block volume from a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute volume-attachment detach --volume-attachment-id volume_attachment_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DetachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DetachVolume) operation to detach a block volume from a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

