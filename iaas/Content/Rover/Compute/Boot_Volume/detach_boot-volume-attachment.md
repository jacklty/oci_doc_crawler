Updated 2024-09-16
# Detaching a Boot Volume Attachment from a Compute Instance on a Roving Edge Infrastructure Device
Describes how to detach a boot volume from a compute instance on your Roving Edge Infrastructure device.
**Note**
You can detach a boot volume only from a stopped compute instance. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance from which you want to detach the boot volume. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the boot volume, and then click **Detach Boot Volume**. Confirm when prompted.
  * Use the [oci compute boot-volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/detach.html) command and required parameters to detach a boot volume from a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute boot-volume-attachment detach --boot-volume-attachment-id boot_volume_attachment_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DetachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DetachBootVolume) operation to detach a boot volume from a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

