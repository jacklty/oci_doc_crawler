Updated 2024-09-16
# Getting a Block Volume's Details for a Roving Edge Infrastructure Device
Describes how to get the details of a block volume on your Roving Edge Infrastructure device.
See [Listing Volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/listingvolumes.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/get_block_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/get_block_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/get_block_volume.htm)


  *     1. Open the navigation menu and select **Block Storage > Block Volumes**. The **Block Volumes** page appears. All block volumes are listed in tabular form.
    2. Select a **State** from the list to limit the block volumes displayed to that state. Click the block volume whose details you want to get. The block volume's **Details** page appears.
  * Use the [oci bv volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/get.html) command and required parameters to get the details of a block volume on your Roving Edge Infrastructure devices:
Copy
```
oci bv volume get --volume-id volume_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/GetVolume) operation to get the details of a block volume on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

