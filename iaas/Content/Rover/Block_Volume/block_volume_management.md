Updated 2024-08-23
# Block Volumes for Roving Edge Infrastructure
Describes how to manage block volume tasks, including creating, updating, and deleting block volumes, on your Roving Edge Infrastructure devices.
You can perform the following block volume tasks:
  * [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm#top "Describes how to create a block volume on your Roving Edge Infrastructure device.")
  * [Listing Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/list_block_volume.htm#top "Describes how to list the blocks volume on your Roving Edge Infrastructure device.")
  * [Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/get_block_volume.htm#top "Describes how to get the details of a block volume on your Roving Edge Infrastructure device.")
  * [Renaming a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/update_block_volume.htm#top "Describes how to rename a block volume on your Roving Edge Infrastructure device.")
  * [Deleting a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm#top "Describes how to delete a block volume from your Roving Edge Infrastructure device.")
  * [Block Volume Attachment Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/volume-attachment_management.htm#BlockVolumeAttachmentManagement "Describes how to manage block volume attachment tasks, including attaching, detaching, and listing block volumes attachments, to a compute instance on your Roving Edge Infrastructure devices.")


The Block Volume service doesn't reserve storage space for block volumes and boot volumes in advance. Instead, storage space is consumed when the data is written to the block volume. For example, if a 100 GB block volume is created, it doesn't mean that 100 GB is reserved from the total available storage space for this block volume. The storage space remains available to all services and can be exhausted before the 100 GB volume is filled with data.
Also, the Block Volume service doesn't validate the specified size of a created block volume against the available storage space. This lack of validation can lead to over subscription when the total size of created volumes exceeds the storage space available on the device. Don't rely on block volume sizes to calculate storage space usage.
**Important**
Plan the total storage needs of your Compute (boot volumes), Block Storage, and Object Storage resources in advance to ensure your storage doesn't exceed 80% of the total available storage. Then regularly monitor the available storage space to avoid oversubscription problems. If your storage capacities reach 80% or higher, see [Avoiding Storage Overages Using Safe Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/safe_mode.htm#SafeMode).
See [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) in the Oracle Cloud Infrastructure documentation for more information on this service.
Was this article helpful?
YesNo

