Updated 2024-09-16
# Deleting a Block Volume from a Roving Edge Infrastructure Device
Describes how to delete a block volume from your Roving Edge Infrastructure device.
The volume cannot have an active connection to an instance. See [Deleting a Volume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DeleteVolume) in the Oracle Cloud Infrastructure documentation for more information on this feature.
**Caution**
All data on the volume is permanently lost when the volume is deleted.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm)


  *     1. Open the navigation menu and select **Block Storage > Block Volumes**. The **Block Volumes** page appears. All block volumes are listed in tabular form.
    2. Select a **State** from the list to limit the block volumes displayed to that state.
    3. Click the block volume that you want to delete. The block volume's **Details** page appears.
    4. Click **Terminate**.
    5. Confirm the deletion when prompted.
  * Use the [oci bv volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/delete.html) command and required parameters to delete a block volume from your Roving Edge Infrastructure devices:
Copy
```
oci bv volume delete --volume-id volume_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DeleteVolume) operation to delete a block volume from your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

