Updated 2023-08-29
# Deleting a Block Volume
Delete a block volume from the Block Volume service when it's no longer needed.
**Caution**
  * You can't undo this operation. When you delete a volume, any data on the volume is permanently deleted. 
  * All policy-based backups eventually expire, so if you want to keep a backup of the volume indefinitely, create a manual backup of the volume before you delete it. See [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm#Backing_Up_a_Volume "Create a manual backup for a volume in the Block Volume service.") and [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List scope** , select the compartment that contains the block volume. 
    3. In the **Block Volumes** list, click the name of the volume that you want to delete. 
    4. Click **Terminate**.
    5. In the confirmation dialog box, click **Terminate**. 
  * Use the [oci bv volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/delete.html) command and required parameters to delete a block volume:
Command
CopyTry It
```
oci bv volume delete --volume-id volume_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DeleteVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DeleteVolume) operation to delete a block volume.


Was this article helpful?
YesNo

