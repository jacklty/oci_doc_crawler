Updated 2024-02-13
# Editing a Block Volume's Settings
Edit the settings for a block volume in the Block Volume service.
You can edit the following settings for block volumes: 
  * Volume name
  * Volume size
  * Volume performance
  * Autotune settings for dynamic performance scaling
  * Assigned backup policy for scheduled volume backups
  * Cross region replication


You can update these settings when volumes are online and attached to instances or when they're detached from instances.
This topic provides the basic steps for editing a volume. For instructions applicable to the specific volume setting that you're editing, and more information about that setting, click the links provided in the steps. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List scope** , select the compartment that contains the block volume.
    3. In the **Block Volumes** list, click the name of the block volume that you want to edit.
    4. Click **Edit**.
    5. In the **Edit volume** panel, update the following settings for the volume as needed:
       * In the **Name** field, specify a different name for the volume.
       * In the **Volume size (in GB)** field of the **Volume size and performance** section, specify a larger size for the volume. See [Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#Resizing_a_Volume).
After you increase a volume's size, you need to rescan the disk and extend the partition. See [Rescanning the Disk for a Block Volume or Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanning_the_Disk_for_a_Block_Volume_or_Boot_Volume) and [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume). 
       * In the **Default VPUs/GB** field or using the **VPUs/GB** slider in the **Target volume performance** section, adjust the performance for the block volume while it's online, without any downtime. See [Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#Changing_the_Performance_of_a_Volume).
       * In the **Target volume performance** section, enable or disable **Performance based auto-tune** or **Detached volume auto-tune** for dynamic performance scaling. See [Dynamic Performance Scaling](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm#autotunevolumeperformance "Block Volume provides dynamic performance scaling with autotuning. This feature enables you to configure your volumes so that the service adjusts the performance level automatically to optimize performance.").
       * In the **Backup policies** section, select a user-defined or Oracle-defined backup policy for the volume. This policy configures volume backups to run automatically on a schedule and retain them based on the selected policy. See [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups). You can also enable scheduled cross-region backups, so that scheduled volume backups are automatically copied to a second region. See [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).
       * In the **Cross region replication** section, configure ongoing automatic asynchronous replication of block volumes to other regions for disaster recovery scenarios. See [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.").
    6. Click **Save changes**.
  * Use the [oci bv volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html) command and required parameters to edit a block volume:
Command
CopyTry It
```
oci bv volume update --volume-id volume_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume) operation to edit a block volume.


Was this article helpful?
YesNo

