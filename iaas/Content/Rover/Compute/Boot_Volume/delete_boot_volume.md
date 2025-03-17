Updated 2024-09-16
# Deleting a Boot Volume from a Compute Instance on a Roving Edge Infrastructure Device
Describes how to delete a boot volume from a compute instance on your Roving Edge Infrastructure device.
See [Deleting a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/deletingbootvolume.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
**Important**
You cannot undo this operation. Any data on a volume is permanently deleted after the volume is deleted. You are not able to restart the associated instance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose attached boot volume you want to delete. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
    5. Click the boot volume that you want to delete. The boot volume's **Details** page appears.
    6. Click **Terminate**.
    7. Confirm the deletion when prompted.
  * Use the [oci bv boot-volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/delete.html) command and required parameters to delete a boot volume from a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci bv boot-volume delete --boot-volume-id boot_volume_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DeleteBootVolume) operation to delete a boot volume from a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

