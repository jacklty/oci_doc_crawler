Updated 2024-10-15
# Creating a Block Volume
Create a block volume in the Block Volume service. 
Block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance. For more information, see [Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Overview_of_Block_Volume).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**.
    2. Click **Create Block Volume**.
    3. In the **Create block volume** , provide the following values:
       * **Name** : Enter a user-friendly name for the volume. Avoid entering confidential information.
       *          * **Create in compartment** : Select the compartment to create the volume in, if different from the current compartment. 
       * **Availability Domain** : Select the same **availability domain** as the instance you plan to attach the volume to.
       * **Cluster Placement Group** : (Optional) Select the cluster placement group in which to create the volume. 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
       * **Volume size and performance** : Select **Default** or **Custom**. If you select **Custom** , enter the following values
         * **Volume size** : Enter the size of the volume, be between **50 GB** and **32 TB**. You can choose in 1 GB increments within this range. The default size is 1024 GB. If you choose a size outside of your service limit, you might be prompted to request an increase. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
         * **Volume target performance** : Optionally, you can select the appropriate performance level for your requirements. For more information about volume performance options, see [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance). The default option is **Balanced**.
       * **Backup policies** : Optionally, select the appropriate backup policy for your requirements. See [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups). If you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
       * **Cross region replication** : Optionally, enable asynchronous cross-region replication for the volume. See [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains."). If you enable cross-region replication, you can encrypt the volume replica in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region replication encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
       * **Encryption:** Optionally, encrypt the data in this volume by using your own Vault encryption key. Select **Encrypt using customer-managed keys** , and then select the vault compartment and vault that contain the master encryption key you want to use. Then, select the master encryption key compartment and master encryption key. 
**Important** The Block Volume service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes. 
    4. Click **Show Tagging Options** to add tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Click **Create Block Volume**.
The block volume details page opens, and the volume is in the **Provisioning** state. When the state changes to **Available** , the volume is ready to attach to an instance. For more information, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
  * Use the [oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html) command and required parameters to create a block volume:
Command
CopyTry It
```
oci bv volume create [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation to create block volume.


Was this article helpful?
YesNo

