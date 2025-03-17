Updated 2024-09-16
# Listing the Boot Volumes for a Compute Instance on a Roving Edge Infrastructure Device
Describes how to list the boot volumes for a compute instance on your Roving Edge Infrastructure device.
See [Listing Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/listingbootvolumes.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/list_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/list_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/list_boot_volume.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose attached boot volumes you want to list. The instance's **Details** page appears.
    4. Click **Boot Volume** under **Resources**. The **Boot Volumes** page appears, displaying the boot volumes in tabular form.
  * Use the [oci bv boot-volume list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/list.html) command and required parameters to list the boot volumes for a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci bv boot-volume list --compartment-id compartment_ocid --availability-domain orei-1-ad-1 [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ListBootVolumes) operation to list the boot volumes for a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

