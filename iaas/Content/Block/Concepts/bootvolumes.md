Updated 2024-06-04
# Boot Volumes
When you launch a virtual machine (VM) or bare metal instance based on a [platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm) or [custom image](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm), a new boot volume for the instance is created in the same compartment. That boot volume is associated with that instance until you terminate the instance. When you [terminate the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm), you can preserve the boot volume and its data. This feature gives you more control and management options for your compute instance boot volumes, and enables:
  * **Instance scaling:** When you terminate your instance, you can keep the associated boot volume and use it to launch a new instance using a different instance type or shape. See [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) for steps to launch an instance based on a boot volume. This allows you to switch easily from a bare metal instance to a VM instance and vice versa, or scale up or down the number of cores for an instance. 
  * **Troubleshooting and repair:** If you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume. Then you can attach it to another instance as a data volume to troubleshoot it. After resolving the issue, you can then reattach it to the original instance or use it to launch a new instance. 


Boot volumes are encrypted by default, the same as other block storage volumes. For more information, see [Block Volume Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
**Important** In-transit encryption for boot and block volumes is only available for virtual machine (VM) instances launched from platform images, along with bare metal instances that use the following shapes: BM.Standard.E3.128, BM.Standard.E4.128, BM.DenseIO.E4.128. It is not supported on other bare metal instances. To confirm support for certain Linux-based custom images and for more information, [contact Oracle support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). 
You can group boot volumes with block volumes into the same volume group, making it easy to create a group volume backup or a clone of your entire instance, including both the system disk and storage disks at the same time. See [Working with Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm#Volume_Groups "The Oracle Cloud Infrastructure Block Volume service provides you with the capability to group together many volumes in a volume group. A volume group can include both types of volumes, boot volumes, which are the system disks for your compute instances, and block volumes for your data storage. You can use volume groups to create volume group backups and clones that are point-in-time and crash-consistent.") for more information.
You can move Block Volume resources such as boot volumes and boot volume backups between compartments. For more information, see [Move Block Volume Resources Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm#Move_Block_Volume_Resources_Between_Compartments).
For more information about the Block Volume service and boot volumes, see the[ Block Volume FAQ](https://www.oracle.com/cloud/storage/block-volumes/faq/).
## Custom Boot Volume Sizes 🔗 
When you launch an instance, you can choose whether to use the selected image's default boot volume size, or to specify a custom size up to 32 TB. This capability is available for the following image source options:
  * Platform image
  * Custom image
  * Image OCID


See [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) for more information.
For Linux and Windows images, the custom boot volume size must be larger than the image's default boot volume size or 50 GB, whichever is higher.
**Note** For Windows Server 2012 R2 Datacenter images and Windows platform images published before October 2021, the custom boot volume size must be larger than the image's default boot volume size or 256 GB, whichever is higher.
If you specify a custom boot volume size, you need to extend the volume to take advantage of the larger size. For steps, see [Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extending_the_Partition_for_a_Boot_Volume).
## Boot Volume Performance 🔗 
Boot volume performance varies with volume size, see [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance) for more information. 
The Block Volume service's elastic performance enables you to dynamically change the volume performance for boot volumes. Once an instance has been created, you can change the volume performance of the boot volume to one of the following performance levels:
  * Balanced 
  * Higher Performance
  * Ultra High Performance (See [Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot).)


For how to change the performance for a boot volume, see [Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm#Changing_the_Performance_of_a_Volume)
## Cross-Region Boot Volume Replication 🔗 
The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of boot volumes to other regions. This feature supports disaster recovery, migration, and business expansion scenarios, without requiring boot volume backups. See [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.") for more information.
## Required IAM Service Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to list boot volumes. The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes, boot volumes, and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
Oracle Cloud Infrastructure supports the following browsers and versions:
  * Google Chrome 80 or later
  * Safari 12.1 or later
  * Firefox 62 or later (Private Browsing mode isn't supported)*
  * Edge 104 or later


See the following tasks for managing boot volumes:
  * [Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingbootvolumes.htm#Listing_Boot_Volumes)
  * [Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingabootvolume.htm#Attaching_a_Boot_Volume)
  * [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume)
  * [Listing Boot Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingbootvolumeattachments.htm#Listing_Boot_Volume_Attachments)
  * [Deleting a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingbootvolume.htm#Deleting_a_Boot_Volume)


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage boot volumes:
  * [BootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume)
  * [ListBootVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ListBootVolumes)
  * [GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume)
  * [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)
  * [DetachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DetachBootVolume)
  * [DeleteVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DeleteBootVolume)
  * [BootVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment)
  * [AttachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/AttachBootVolume)
  * [GetBootVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/GetBootVolumeAttachment)
  * [ListBootVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/ListBootVolumeAttachments)


Was this article helpful?
YesNo

