Updated 2024-09-16
# Renaming a Boot Volume for a Compute Instance on a Roving Edge Infrastructure Device
Describes how to rename a boot volume for a compute instance on your Roving Edge Infrastructure device.
See [Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/update_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/update_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/update_boot_volume.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose attached boot volumes you want to rename. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
    5. Click the boot volume you want to rename. The **Edit Boot Volume** dialog box appears.
    6. Rename the boot volume.
    7. Click **Save Changes**.
  * Use the [oci bv boot-volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html) command and required parameters to rename a boot volume for a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci bv boot-volume update --boot-volume-id boot_volume_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume) operation to rename a boot volume for a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

