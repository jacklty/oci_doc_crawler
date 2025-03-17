Updated 2023-09-30
# Creating a Manual Backup for a Block Volume
Create a manual backup for a volume in the Block Volume service.
Volume backups are point-in-time snapshots of volume data. For more information, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups). You can create a manual backup for a volume by using the steps in this topic. To create backups based on a defined schedule and retention policy, see [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups). 
Manual backups don't expire, they're maintained until you delete them.
For information to help you decide whether to create a backup or a clone of a boot volume, see [Differences Between Block Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backupsvsclones).
**Note** The size of a volume backup size might be larger than the current volume usage. See [Volume Backup Size](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Size).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List scope** , select the compartment that contains the block volume.
    3. In the **Block Volume** list, click the name of the block volume that you want to create a backup for.
    4. Under **Resources** , click **Block Volume Backups**.
    5. Click **Create Block Volume Backup**.
    6. Enter a name for the backup. Avoid entering confidential information.
    7. Select the backup type, either incremental or full. See [Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype). 
    8. (Optional) Click **Show Tagging Options** to add tags to the backup. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    9. Click **Create Block Volume Backup**.
The backup is complete when the state changes to **Available**.
  * Use the [oci bv backup create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/create.html) command and required parameters to create a block volume backup:
Command
CopyTry It
```
oci bv backup create --volume-id volume_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CreateVolumeBackup.html) operation to create a block volume backup.


Was this article helpful?
YesNo

