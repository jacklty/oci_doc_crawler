Updated 2024-07-17
# Overview of Block Volume Backups
The Oracle Cloud Infrastructure Block Volume offers a secure, cost-effective, policy-based, fully-managed backup solution. Block volumes, boot volumes, and volume groups can be backed up while attached to or detached from an instance, and are then encrypted and regionally stored in OCI-managed [Oracle Cloud Infrastructure Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm). Backups can be restored to existing or new volumes in any availability domain, irrespective of the availability of the source volume or volume group. This capability allows you to easily restore the volumes or volume groups in the event of a disaster. You can create up to 100,000 backups.
**Note** While a backup is in progress, the volume being backed up can't be deleted.
## Required IAM Policy for Volume Backups 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
To get started with the volume backups, an administrator needs to grant user access through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
The following is an example policy to allow block volume administrators to manage block volumes, backups, and volume groups across regions: 
Copy
```
Allow group VolumeBackupAdmins to use volumes in tenancy
Allow group VolumeBackupAdmins to manage volume-backups in tenancy
Allow group VolumeBackupAdmins to inspect volume-attachments in tenancy
Allow group VolumeBackupAdmins to inspect instances in tenancy
Allow group VolumeBackupAdmins to manage backup-policies in tenancy
Allow group VolumeBackupAdmins to manage backup-policy-assignments in tenancy
Allow group VolumeBackupAdmins to use volume-backups in tenancy where request.permission='VOLUME_BACKUP_COPY'
```

The following is an example policy to allow boot volume backup administrators to create and manage only boot volume backups:```
Allow group BootVolumeBackupAdmins to use volumes in tenancy
Allow group BootVolumeBackupAdmins to manage boot-volume-backups in tenancy
Allow group BootVolumeBackupAdmins to inspect instances in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policies in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policy-assignments in tenancy
Allow group BootVolumeBackupAdmins to use boot-volume-backups in tenancy where request.permission='BOOT_VOLUME_BACKUP_COPY'
```

**Tip** When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same **compartment**. However, users must have access to both compartments. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Volume Backup Types 🔗 
There are two backup types available in the Block Volume service:
  * **Incremental:** This backup type includes only the changes since the last backup. 
  * **Full:** This backup type includes all changes since the volume was created. 


### Volume Group Backups
A volume group is a consistent group of volumes. You can use volume group backups to create creating point-in-time snapshots for multiple block volumes such as large filesystems and databases. These snapshots are stored in OCI-managed object storage. For more information, see [Working with Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/blockvolumes.htm#blockvolumes "Oracle Cloud Infrastructure Block Volume lets you dynamically provision and manage block storage volumes. You can create, attach, connect, and move volumes, as well as change volume performance, as needed, to meet your storage, performance, and application requirements. After you create a volume, you can attach and connect a volume to an instance, and then you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another instance without the loss of data.").
### Backup Details 🔗 
For data recovery purposes, there is no functional difference between an incremental backup and a full backup. Because both backup types enable you to restore the full contents to the point-in-time snapshot, you don't need to retain the initial full backup or subsequent incremental backups. A volume backup retains all of that volume's contents, regardless of the time of its snapshot. If you delete a full backup of a volume, (for example, due to retention policies), the size of the incremental backup for that volume will increase in order to restore the volume successfully.
### Example
You create a 50 GB block volume, write 25 GB to the volume, and then launch a full backup of the volume on Day 1 with a two-day retention period. Upon completion, the backup size is 25 GB.![](https://docs.oracle.com/en-us/iaas/Content/Block/Images/volume_backup_types_day_1.png)
On Day 2, you then modify 2GB of existing data, write 3GB of new data and create an incremental backup. The unique size of the incremental backup totals 5 GB.![](https://docs.oracle.com/en-us/iaas/Content/Block/Images/volume_backup_types_day_2.png)
On Day 3, another incremental backup is made with modified 3G of existing data and added 2 GB of new data, totaling 5GB.![](https://docs.oracle.com/en-us/iaas/Content/Block/Images/volume_backup_types_day_3.png)
On Day 4, the full backup is be deleted as the retention expires. The incremental backup size is now totals 28GB, the contents of which are required to restore the volume contents to the time the incremental backup was taken. ![](https://docs.oracle.com/en-us/iaas/Content/Block/Images/volume_backup_types_day_4.png)
On Day 5, the first incremental backup retention expires. The backup size for this second incremental backup totals 30GB, the actual size of the volume contents at the time the second incremental backup was made. Because the blocks are retained even after the full backup was deleted, the volume can still be restored from an incremental backup.![](https://docs.oracle.com/en-us/iaas/Content/Block/Images/volume_backup_types_day_5.png)
## Volume Backup Size 🔗 
Volume backup size may be larger than the current volume usage. Possible reasons for this could include:
  * Any part of a volume that has been written to is considered initialized, and will always be included in a volume backup.
  * Many operating systems write or zero out the content, which marks these blocks as used. Block Volume service considers these blocks updated and includes them in the volume backup. 
  * Volume backups also include metadata, which can be up to 1 GB in additional data. For example, in a full backup of a 256 GB Windows boot disk, you might see a backup size of 257 GB, which includes an additional 1 GB of metadata.


**Note** After a volume has been resized, the first backup on the resized volume will be a full backup. See [Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#Resizing_a_Volume) for more information about volume resizing. 
## Backup Methods 🔗 
Overview/container topic for methods of backing up block volumes.
Backups can be initiated manually or by assigning a backup policy. The backups for a volume will be created in the same compartment as the volume. If volumes in a volume group are located in different compartments, the volume backups will be stored in the volume's compartment and not in volume group's compartment. Volume group backup resources will be in the volume group's compartment.
### Manual Backups 🔗 
You can perform single incremental or full backups for volumes or volume groups. See [Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype) for more information.
To manually back up a volume, see [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm#Backing_Up_a_Volume "Create a manual backup for a volume in the Block Volume service.").
**Note**
Backups can take hours during peak times, and completion times can vary based on the time the backups are initiated and by region. Large full and incremental backups the backups can take longer based on the amount of data that has to be copied.
### Policy-Based Backups 🔗 
You can also define backup policies to simplify and automate the snapshot management and scheduling for a volume or volume group without affecting application performance. 
There are two kinds of backup policies:
  * **Oracle defined** : Predefined backup policies that have a set backup frequency and retention period. You cannot modify these policies. For more information, see [Oracle Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#Oracle). 
**Note** As of November 23, 2021, Oracle defined policies no longer include full backups. For more information, see [Full backups removed from Oracle defined backup policies](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic-BlockVolume).
  * **User defined** : Custom backup policies that you create and configure schedules and retention periods for. You can also enable scheduled cross-region automated backups with user defined policies. For more information, see [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy). For more information on customizing your own policies, see [User Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#custom). 


See [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups) for more information.
## Copying Block Volume Backups Across Regions 🔗 
You can copy block volume backups between regions using the Console, command line interface (CLI), SDKs, or REST APIs. For steps, see [Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Copying_a_Volume_Backup_Between_Regions). This capability enhances the following scenarios:
  * **Disaster recovery and business continuity:** By copying block volume backups to another region at regular intervals, you can easily rebuild applications and data in the destination region if a region-wide disaster occurs in the source region. 
  * **Migration and expansion:** You can easily migrate and expand your applications to another region. 


You can also enable scheduled cross-region automated backups with user defined policies. See [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).
To copy volume backups between regions, you must have permission to read and copy volume backups in the source region, and permission to create volume backups in the destination region. For more information, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#Required).
After you copy the volume backup to the new region, you can restore from that backup by creating a new volume from the backup using the steps described in [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume).
## Volume Backup Encryption 🔗 
The Oracle Cloud Infrastructure Block Volume service always encrypts all block volumes, boot volumes, and volume backups at rest by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption.
The Oracle Cloud Infrastructure Vault service enables you to bring and manage your own keys to use for encrypting volumes and their backups. When you create a volume backup, the encryption key used for the volume is also used for the volume backup.
You can change the encryption key for the volume backup to another Vault encryption key, or to an Oracle-managed key. See [Changing the Encryption Key for a Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#managingblockencryptionkeys__backupkeychange) for more information.
When you restore the backup to create a new volume you configure a new key, see [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume). See also [Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). 
**Important**
By default, volumes restored from a volume backup or a volume group backup are configured to use Oracle-provided keys for encryption. For volumes restored from a volume backup, you can specify a customer-managed key for the new volume during the restore process. This option is not available for volumes restored from volume group backups, so the new volumes are restored with Oracle-provided keys. You can update the encryption keys for these volumes after they are restored, see [Editing a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm).
If you don't configure a volume to use the Vault service, the Block Volume service uses the Oracle-provided encryption key instead. This applies to both encryption at-rest and in-transit encryption.
## Monitoring Backups 🔗 
You can monitor backups using backup events, which are generated on all successful/failed backups. For more information, see [Using Events to Notify When a Volume Backup Fails](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm#backupstatusevents).
## Tags 🔗 
When a volume backup is created, the source volume's tags are automatically included. This also includes volumes with custom backup policies applied to create scheduled backups. Source volume tags are automatically assigned to all backups when they are created. You can also apply additional tags to volume backups as needed.
When a volume backup is copied to a new region, tags are also automatically copied with the volume backup. When the volume is restored from a backup, the volume is restored with the source volume's tags.
## Best Practices When Creating Block Volume Backups 🔗 
When creating and restoring from backups, keep in mind the following:
  *     * **Backup your critical application volumes multiple times daily**. For mission-critical applications, we recommend that you take multiple backups per day for to minimize the possible recovery point objective (RPO). 
**Note** With policy-based backups you can only schedule one backup and copy per day. Users can use manual backups to initiate multiple backups in a day. For cross region copy, it is recommended to only copy one backup per day to the remote region. For even smaller RPO, please take a look into our replication support.
    * **Configure retention and expiry times for your backups.** Backups will be automatically purged after the set expiry time to free storage space and costs. Manual backups do not expire.
    * **Schedule or create your backups during off-peak hours.** if you notice your backups are not completing at the expected time, consider changing your scheduled or manual backup times to a different time of day. A daily backup will still complete in less than 24 hours. 
    * **Organize critical and non-critical data.** To reduce the amount of backups needing to be managed, we recommend using separate creation, backup and recovery operations for critical and non-critical data. Critical data typically includes all the data that is required for application recovery and use, and should be kept in a secondary block volume instead of your boot volume. Non-critical data includes swap, temporary, cache or page files and non-critical logs, and tends to be larger in size.
    * **Use volume groups to create cross-volume, crash-consistent backups.** When your data is spread across multiple volumes, you can create and back them up as a volume group. Because the volume group backups consistently capture all of the data synced to each volume, you no longer have to shut down your instances to take individual snapshots. This method is ideal for filesystems and applications that support journaling. 
    * **Maximize data recoverability and recover time with app-consistent backups.** You can achieve app-consistent backups by pausing or quiescing your service before initiating a backup. This can include stopping all I/O operations, syncing all memory buffers, and flushing in-flight transactions. You can then send an API call to take a backup of a volume or volume group. 
  * Before creating a backup, you should ensure that the data is consistent: Sync the file system, unmount the file system if possible, and save your application data. Only the data on the disk will be backed up. When creating a backup, after the backup state changes from REQUEST_RECEIVED to CREATING, you can return to writing data to the volume. While a backup is in progress, the volume that is being backed up cannot be deleted.
  * If you want to attach a restored volume that has the original volume attached, be aware that some operating systems do not allow you to restore identical volumes. To resolve this, you should change the partition IDs before restoring the volume. The steps to change an operating system's partition ID vary by operating system. For instructions, see your operating system's documentation.


See [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm#Backing_Up_a_Volume "Create a manual backup for a volume in the Block Volume service.") and [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume) for more information. 
## Planning Your Backup 🔗 
The primary use of backups is to support business continuity, disaster recovery, and long-term archiving requirements. When determining a backup schedule, your backup plan and goals should consider the following:
  * **Frequency:** How often you want to back up your data.
  * **Recovery time:** How long you can wait for a backup to be restored and accessible to the applications that use it. The time for a backup to complete varies on several factors, but it will generally take a few minutes or longer, depending on the size of the data being backed up and the amount of data that has changed since your last backup.
  * **Number of stored backups:** How many backups you need to keep available and the deletion schedule for those you no longer need. You can only create one backup at a time, so if a backup is underway, it will need to complete before you can create another one. For details about the number of backups you can store, see [Block Volume Capabilities and Limits](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Capabil).


The common use cases for using backups are:
  * Needing to create multiple copies of the same volume. Backups are highly useful in cases where you need to create many instances with many volumes that need to have the same data formation.
  * Taking a snapshot of your work that you can restore to a new volume at a later time.
  * Ensuring you have a spare copy of your volume in case something goes wrong with your primary copy.


## Reducing Volume Backup Sizes with SCSI UNMAP 🔗 
Oracle Cloud Infrastructure Block Volume supports SCSI UNMAP commands for both boot volumes and block volumes to reclaim unused space. Use these commands to reduce your backup sizes, resulting in faster backup restore times. See [Support for SCSI UNMAP](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/reducingbackupsizewithtrim.htm#reducingbackupsizewithtrim) for more information. 
## Differences Between Block Volume Backups and Clones 🔗 
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
For background information and steps to clone a block volume, see [Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.").
## Using the CLI or REST APIs to Customize and Manage the Lifecycle of Volume Backups 🔗 
You can use the CLI, REST APIs, or the SDKs to automate, script, and manage volume backups and their lifecycle. 
### Using the CLI 🔗 
This section provides basic sample CLI commands that you can use in a script, such as a cron job run by the cron utility on Linux-based operating systems, to perform automatic backups at specific times. For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
[To create a manual backup of the specified block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv backup create --volume-id <block_volume_OCID> --display-name <Name> --type <FULL|INCREMENTAL>
```

For example:
```
oci bv backup create --volume-id ocid1.volume.oc1..<unique_ID> --display-name "backup display name" --type FULL
```

[To delete a block volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv backup delete --volume-backup-id <volume_backup_OCID>
```

For example:
```
oci bv backup delete --volume-backup-id ocid1.volume.oc1..<unique_ID>
```

[To create a manual backup of the specified boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume-backup create --volume-id <boot_volume_OCID> --display-name <Name> --type <FULL|INCREMENTAL>
```

For example:
```
oci bv boot-volume-backup create --volume-id ocid1.volume.oc1..<unique_ID> --display-name "backup display name" --type FULL
```

[To delete a boot volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv backup delete --boot-volume-backup-id <boot_volume__backup_OCID>
```

For example:
```
oci bv backup delete --boot-volume-backup-id ocid1.volume.oc1..<unique_ID>
```

[To list the Oracle-defined backup policies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy list
```

[To assign an Oracle-defined backup policy to a boot or block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment create --asset-id <volume_OCID> --policy-id <policy_OCID>
```

For example:
```
oci bv volume-backup-policy-assignment create --asset-id ocid1.volume.oc1..<unique_ID> --policy-id ocid1.volumebackuppolicy.oc1..<unique_ID>
```

[To un-assign an Oracle-defined backup policy from a boot or block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment delete --policy-assignment-id <policy_assignment_OCID>
```

For example:
```
oci bv volume-backup-policy-assignment delete --policy-assignment-id ocid1.volumebackuppolicyassign.oc1..<unique_ID>
```

[To retrieve the backup policy assignment ID for a boot or block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id <volume_OCID>
```

For example:
Copy
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id ocid1.volume.oc1..<unique_ID>
```

### Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations for working with block volume backups, boot volume backups, and backup policies.
#### Block Volume Backups
  * [CreateVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CreateVolumeBackup)
  * [DeleteVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/DeleteVolumeBackup)
  * [GetVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/GetVolumeBackup)
  * [ListVolumeBackups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ListVolumeBackups)
  * [UpdateVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/UpdateVolumeBackup)


#### Boot Volume Backups
  * [CreateBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/CreateBootVolumeBackup)
  * [DeleteBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/DeleteBootVolumeBackup)
  * [GetBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/GetBootVolumeBackup)
  * [ListBootVolumeBackups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/ListBootVolumeBackups)
  * [UpdateBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/UpdateBootVolumeBackup)


#### Volume Backup Policies and Policy Assignments
  * [GetVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/GetVolumeBackupPolicy)
  * [ListVolumeBackupPolicies](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/ListVolumeBackupPolicies)
  * [CreateVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment)
  * [DeleteVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/DeleteVolumeBackupPolicyAssignment)
  * [GetVolumeBackupPolicyAssetAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssetAssignment)
  * [GetVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssignment)


Was this article helpful?
YesNo

