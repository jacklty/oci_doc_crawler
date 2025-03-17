Updated 2023-08-29
# Overview of Boot Volume Backups
The backups feature of the Oracle Cloud Infrastructure Block Volume service lets you make a crash-consistent backup, which is a point in time snapshot of a boot volume without application interruption or downtime. You can make a backup of a boot volume while it is attached to a running instance, or you can make a backup of a boot volume while it is detached from the instance. Boot volume backup capabilities are the same as block volume backup capabilities. See [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups) for more information.
There are two ways you can initiate a boot volume backup, the same as block volume backups. You can either manually start the backup, or assign a policy which defines a set backup schedule. See [Manual Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#manual) and [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#policy) for more information.
## Boot Volume Backup Types 🔗 
The Block Volume service supports the same backups types for boot volumes as for block volumes:
  * **Incremental:** This backup type includes only the changes since the last backup. 
  * **Full:** This backup type includes all changes since the volume was created. 


You can restore a boot volume from any of your incremental or full boot volume backups. Both backup types enable you to restore the full boot volume contents to the point-in-time snapshot of the boot volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about. 
**Note** After a boot volume has been resized, the first backup on the resized boot volume will be a full backup. See [Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#Resizing_a_Volume) for more information about volume resizing. 
## Tags 🔗 
When a boot volume backup is created, the source boot volume's tags are automatically included in the boot volume backup. This also includes boot volumes with custom backup policies applied to create backups on a schedule. Source boot volume tags are automatically assigned to all backups when they are created. You can also apply additional tags to volume backups as needed.
When you create an instance from the boot volume backup, the instance is created includes the source boot volume's tags.
## Backing Up a Boot Volume 🔗 
You can create boot volume backups using the Console or the REST APIs/command line interface (CLI). See [Backing Up a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupabootvolume.htm#Backing_Up_a_Boot_Volume) and the [BootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup) API for more information. 
### Boot Volume Backup Size 🔗 
Boot volume backup size may be larger than the source boot volume size. Some of the reasons for this could include the following:
  * Any part of the boot volume that has been written to is considered initialized, so will always be part of the boot volume backup.
  * Many operating systems write or zero out the content, which results in these blocks marked as used. The Block Volume service considers these blocks updated and includes them in the volume backup. 
  * Boot volume backups also include metadata, which can be up to 1 GB in additional data. For example, in a full backup of a 256 GB Windows boot disk, you may see a backup size of 257 GB, which includes an additional 1 GB of metadata.


## Restoring a Boot Volume 🔗 
Before you can use a boot volume backup, you need to restore it. For steps, see [Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingbootvolume.htm#Restoring_a_Boot_Volume).
Making a boot volume backup while an instance is running creates a crash-consistent backup, meaning the data is in the identical state it was in at the time the backup was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases, you can restore a boot volume backup and use it to create an instance. Alternatively you can attach it to an instance as a data volume to repair it or recover data, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance."). To ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).
## Copying Boot Volume Backups Across Regions 🔗 
You can copy boot volume backups between regions using the Console, command line interface (CLI), SDKs, or REST APIs. For steps, see [Copying a Boot Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#Copying_a_Boot_Volume_Backup_Between_Regions). This capability enhances the following scenarios:
  * **Disaster recovery and business continuity:** By copying boot volume backups to another region at regular intervals, it makes it easier for you to restore instances in the destination region if a region-wide disaster occurs in the source region. 
  * **Migration and expansion:** You can easily migrate and expand your instances to another region. 


To copy boot volume backups between regions, you must have permission to read and copy boot volume backups in the source region, and permission to create boot volume backups in the destination region. For more information see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#Required).
Once you have copied the boot volume backup to the new region you can then restore from that backup by creating a new volume from the backup using the steps described in [Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingbootvolume.htm#Restoring_a_Boot_Volume).
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
Was this article helpful?
YesNo

