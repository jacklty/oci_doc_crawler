Updated 2024-05-13
# Cloning a Block Volume
Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.
A cloned volume is a point-in-time direct disk-to-disk deep copy of the source volume, so all the data that is in the source volume when the clone is created is copied to the clone volume. Any subsequent changes to the data on the source volume are not copied to the clone. Because the clone is a copy of the source volume it is the same size as the source volume unless you specify a larger volume size when you create the clone.
The clone operation occurs immediately, and you can attach and use the cloned volume as a regular volume as soon as the state changes to Available. At that point, the volume data is being copied in the background, and can take up to thirty minutes depending on the size of the volume.
There is a single point-in-time reference for a source volume while it is being cloned. If the source volume is attached when you create a clone, you need to wait for the first clone operation to complete from the source volume before creating additional clones. If the source volume is detached, you can create up to ten clones from the same source volume simultaneously.
You can create a clone for a volume only within the same region, availability domain and tenancy. You can create a clone for a volume between compartments if you have the required access permissions for the operation.
For information to help you decide whether to create a backup or a clone of a volume, see [Differences Between Block Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backupsvsclones).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
    2. Under **List scope** , select the compartment that contains the block volume.
    3. In the **Block Volumes** list, click the name of the volume that you want to clone.
    4. Under **Resources** , click **Block Volume Clones**.
    5. Click **Create Clone**.
    6. Specify a name for the clone. Avoid entering confidential information.
    7. Select the compartment to create the clone in, if different from the current compartment. 
    8. (Optional) Select the cluster placement group in which to clone the volume to. 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
    9. To clone the block volume to a larger size volume, or change the performance setting for a clone, select **Custom**. Then perform one or both of the following actions: 
       * In **Volume size (GB)** , enter the new size.
You can only increase the size of the volume; you can't decrease it. If you clone the block volume to a larger-size volume, you need to extend the volume's partition. See [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume).
       * Under **Target volume performance** , select the performance level that you want the volume clone to use. See [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance).
You can also change the performance level after you have cloned the volume. See [Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#Changing_the_Performance_of_a_Volume).
    10. (Optional) Enable asynchronous cross-region replication for the volume clone. Under **Cross region replication** select **ON**. See [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.").
    11. (Optional) Encrypt the data in this volume by using your own Vault encryption key. Select **Encrypt using customer-managed keys** , and then select the vault compartment and vault that contain the master encryption key you want to use. Then, select the master encryption key compartment and master encryption key. 
**Important** The Block Volume service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes. 
    12. Click **Show Tagging Options** to add tags to the volume. 
    13. Click **Create Clone**.
The volume is ready to use when its state is **AVAILABLE** in the volume list. At that point, you can perform various actions on the volume, such as creating a clone from the volume, attaching it to an instance, or deleting the volume.
  * Use the [oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html) command and specify the OCID for the volume you want to clone using the `--source-volume-id` parameter to clone a block volume:
Command
CopyTry It
```
oci bv volume create --source-volume-id <volume_ID>...[OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation and specify [VolumeSourceFromVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/VolumeSourceFromVolumeDetails) for [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails).


Was this article helpful?
YesNo

