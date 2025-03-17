Updated 2024-06-04
# Restoring a Boot Volume
You can use a boot volume backup to create an instance or you can attach it to another instance as a data volume. However before you can use a boot volume backup, you need to restore it to a boot volume.
You can restore a boot volume from any of your incremental or full boot volume backups. Both backup types enable you to restore the full boot volume contents to the point-in-time snapshot of the boot volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about. See [Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#backuptypes) for information about full and incremental backup types.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**. 
  2. Choose your **Compartment**. 
  3. In the list of boot volume backups, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the boot volume backup you want to restore and then click **Restore Boot Volume**. 
  4. Specify a name for the boot volume, select the availability domain to use, and optionally select the cluster placement group in which to restore the boot volume to.
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
  5. choose a backup policy for scheduled backups. See [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups) for more information about scheduled backups and volume backup policies. Avoid entering confidential information.
  6. You can restore a boot volume backup to a larger volume size. To do this, check **Custom Block Volume Size (GB)** and then specify the new size. You can only increase the size of the volume, you cannot decrease the size. If you restore the block volume backup to a larger size volume, you need to extend the volume's partition, see [Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extending_the_Partition_for_a_Boot_Volume) for more information.
  7. Click **Create Boot Volume**.
The boot volume will be ready to use once its icon no longer lists it as **PROVISIONING** in the details page for the boot volume.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To restore a boot volume backup, use the [CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume) operation and specify [BootVolumeSourceFromBootVolumeBackupDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/BootVolumeSourceFromBootVolumeBackupDetails) for [CreateBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateBootVolumeDetails).
## Next Steps 🔗 
After you have restored the boot volume backup, you can:
  * Use the boot volume to create an instance, for more information, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
  * Attach the boot volume to an instance as a data volume, for more information, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").


Making a boot volume backup while an instance is running creates a crash-consistent backup, meaning the data is in the identical state it was in at the time the backup was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases you can use the restored boot volume to create an instance, however to ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).
Was this article helpful?
YesNo

