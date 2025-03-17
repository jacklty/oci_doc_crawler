Updated 2024-06-04
# Working with Block Volumes
Oracle Cloud Infrastructure Block Volume lets you dynamically provision and manage block storage volumes. You can create, attach, connect, and move volumes, as well as change volume performance, as needed, to meet your storage, performance, and application requirements. After you create a volume, you can attach and connect a volume to an instance, and then you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another instance without the loss of data.
This section includes the following tasks:
  * [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service.")
  * [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.")
  * [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance.")
  * [Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm#Listing_Volumes "View a list of the block volumes in your tenancy.")
  * [Listing Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumeattachments.htm#Listing_Volume_Attachments)
  * [Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#top "View a block volume's details.")
  * [Editing a Block Volume's Settings](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm#editvolume "Edit the settings for a block volume in the Block Volume service.")
  * [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.")
  * [Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.")
  * [Disconnecting From a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm#Disconnecting_From_a_Volume)
  * [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.")
  * [Deleting a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm#Deleting_a_Volume "Delete a block volume from the Block Volume service when it's no longer needed.")


## IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Monitoring Resources 🔗 
You can monitor the health, capacity, and performance of your Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
## Tagging Resources 🔗 
Apply tags to your resources to help organize them according to your business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
Was this article helpful?
YesNo

