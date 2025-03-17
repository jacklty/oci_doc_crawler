Updated 2024-05-13
# Cloning a Boot Volume
You can create a clone from a boot volume using the Oracle Cloud Infrastructure Block Volume service. Cloning enables you to make a copy of an existing boot volume without needing to go through the backup and restore process. For more information about the Block Volume service, see [Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Overview_of_Block_Volume) and the[ Block Volume FAQ](https://cloud.oracle.com/infrastructure/storage/block-volume/faq).
A boot volume clone is a point-in-time direct disk-to-disk deep copy of the source boot volume, so all the data that is in the source boot volume when the clone is created is copied to the boot volume clone. Any subsequent changes to the data on the source boot volume are not copied to the boot volume clone. Since the clone is a copy of the source boot volume it will be the same size as the source boot volume unless you specify a larger volume size when you create the clone.
The clone operation occurs immediately and you can use the cloned boot volume as soon as the state changes to available. 
There is a single point-in-time reference for a source boot volume while it is being cloned, so if you clone a boot volume while the associated instance is running, you need to wait for the first clone operation to complete from the source before creating additional clones. You also need to wait for any backup operations to complete as well.
You can only create a clone for a boot volume within the same region, availability domain, and tenant. You can create a clone for a boot volume between compartments as long as you have the required access permissions for the operation.
## Differences Between Boot Volume Backups and Clones 🔗 
Consider the following criteria when you decide whether to create a backup or a clone of a volume.
Volume Backup | Volume Clone  
---|---  
Description | Creates a point-in-time backup of data on a volume. You can restore multiple new volumes from the backup later in the future. | Creates a single point-in-time copy of a volume without having to go through the backup and restore process.  
Use case |  Retain a backup of the data in a volume, so that you can duplicate an environment later or preserve the data for future use. Meet compliance and regulatory requirements, because the data in a backup remains unchanged over time. Support business continuity requirements. Reduce the risk of outages or data mutation over time. |  Rapidly duplicate an existing environment. For example, you can use a clone to test configuration changes without impacting your production environment.  
Speed | Slower (minutes or hours) | Faster (seconds)  
Cost | Lower cost | Higher cost  
Storage location | Object Storage  | Block Volume   
Retention policy | Policy-based backups expire, manual backups do not expire | No expiration  
Volume groups | Supported. You can back up a volume group. | Supported. You can clone a volume group.  
For more information about boot volume backups, see [Overview of Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#Overview_of_Boot_Volume_Backups) and [Backing Up a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupabootvolume.htm#Backing_Up_a_Boot_Volume).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. In the **Boot Volumes** list, click the boot volume that you want to clone.
  3. In **Resources** , click **Boot Volume Clones**.
  4. Click **Create Clone**.
  5. Specify a name for the clone. Avoid entering confidential information.
  6. (Optional) Select the cluster placement group in which to clone the boot volume. 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
  7. To clone the boot volume to a larger size volume, select **Custom Boot Volume Size (GB)** and then specify the new size. You can only increase the size of the volume, you can't decrease the size. If you clone the boot volume to a larger size volume, you need to extend the volume's partition. See [Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extending_the_Partition_for_a_Boot_Volume) for more information.
  8. Click **Create Clone**.


The boot volume is ready use when its icon lists it as **AVAILABLE** in the **Boot Volumes** list. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To create a clone from a boot volume, use the [CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume) operation and specify [BootVolumeSourceFromBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/BootVolumeSourceFromBootVolumeDetails) for [CreateBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateBootVolumeDetails).
## Next Steps 🔗 
After you have cloned a boot volume backup, you can:
  * Use the boot volume to create an instance. For more information, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
  * Attach the boot volume to an instance as a data volume. For more information, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").


Making a boot volume clone while an instance is running creates a crash-consistent clone, meaning the data is in the identical state it was in at the time the clone was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases you can use the cloned boot volume to create an instance, however to ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).
Was this article helpful?
YesNo

