Updated 2024-09-16
# Getting a Boot Volume's Details for a Compute Instance on a Roving Edge Infrastructure Device
Describes how to get the details of a boot volume for a compute instance on your Roving Edge Infrastructure device.
See [Listing Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/listingbootvolumes.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance on whose attached boot volume you want to get details. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
    5. Click the boot volume on whose details you want to get. The boot volume's **Details** page appears. The instance associated with the boot volume is listed in the **Attached Instance** field. If the value for this field displays the following message, the boot volume has been detached from the associated instance, or the instance has been terminated while the boot volume was preserved.
```
None in this Compartment.
```

  * Use the [oci bv boot-volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/get.html) command and required parameters to get the details of a boot volume for a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci bv boot-volume get --boot-volume-id boot_volume_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume) operation to get the details of a boot volume for a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

