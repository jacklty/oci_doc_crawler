Updated 2024-09-24
# Copying a Volume Backup Between Regions
You can copy volume backups and volume group backups from one region to another region using the Oracle Cloud Infrastructure Block Volume service. For more information, see [Copying Block Volume Backups Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Copying). You can also enable scheduled cross-region automated backups with user defined policies, see [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).
**Note**
When copying block volume backups across regions in your tenancy, you can copy up to ten concurrent backups per tenancy at a time from a specific source region.
## Volume Backup Type Considerations 🔗 
When volume backups are copied to another region, the volume backup type in the destination region will always match the source [volume backup types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype), except for certain scenarios for incremental backups.
Incremental backups will be copied as full volume backups in the following scenarios:
  * When the volume backup being copied is the first volume backup taken after a volume has been resized. This applies to volume backups copied on a schedule and volume backups copied manually.
  * Volume backups that were the result of a cross region copy, if they are then copied back to their source region. This applies to volume backups copied on a schedule and volume backups copied manually.
  * When the volume backup is being copied to a destination region where the previous incremental backup copy is in the TERMINATING, TERMINATED, or FAULTY state. This applies to volume backups copied on a schedule and volume backups copied manually.
  * When the volume backup is copied out of order. For example, in the scenario where you have incremental volume backups #1 through #5, and you copy volume backup #3 and then volume backup #1, the volume backups may be copied as full backups to the destination region. This only applies to volume backups that are copied manually. This does not apply to volume backups created and copied using backup policies, as scheduled volume backups are always copied in sequential order.
  * When volume backups are copied out of order after resizing a volume. For example, in the scenario where you have incremental volume backups #1 through #7, with the volume being resized after backup #3 was taken. As previously stated, the first backup copied after the volume resize, in this case backup #4, is copied as a full backup. Backups #5 and #6 are copied as incremental backups. If you then copy a backup out of order, for example backup #2, it is copied as full backup. The next backup in the order, #7, is also copied as a full backup.


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The first two statements listed in the [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) policy lets the specified group do everything with block volumes and backups with the exception of copying volume backups across regions. The aggregate resource type `volume-family` does not include the `VOLUME_BACKUP_COPY` permission, so to enable copying volume backups across regions you need to ensure that you include the third statement in that policy, which is:
Copy
```
Allow group VolumeAdmins to use volume-backups in tenancy where request.permission='VOLUME_BACKUP_COPY'
```

To restrict access to just creating and managing volume backups, including copying volume backups between regions, use the policy in [Let boot volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#boot-volume-backup-admins-manage-only-backups). The individual resource type `volume-backups` includes the `VOLUME_BACKUP_COPY` permission, so you do not need to specify it explicitly in this policy.
If you are copying volume backups encrypted using Vault between regions or you want the copied volume backup to use Vault for encryption in the destination region, you need to use a policy that allows the Block Volume service to perform cryptographic operations with keys in the destination region. For a sample policy showing this, see [Let Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, file systems, Kubernetes secrets, and stream pools](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key).
### Restricting Access
The specific permissions needed to copy volume backups across regions are:
  * **Source region** : `VOLUME_BACKUP_READ`, `VOLUME_BACKUP_COPY`
  * **Destination region** : `VOLUME_BACKUP_CREATE`


### Sample Policies
[To restrict a group to specific source and destination regions for copying volume backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm)
In this example, the group is restricted to copying volume backups from the UK South (London) region to the Germany Central (Frankfurt) region.
Copy
```
Allow group MyTestGroup to read volume-backups in tenancy where all {request.region='lhr'}
Allow group MyTestGroup to use volume-backups in tenancy where all {request.permission='VOLUME_BACKUP_COPY', request.region = 'lhr', 
Allow group MyTestGroup to manage volume-backups in tenancy where all {request.permission='VOLUME_BACKUP_CREATE', request.region = 'fra'}
```

[To restrict some source regions to specific destination regions while enabling all destination regions for other source regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm)
In this example, the following is enabled for the group:
  * Manage volume backups in all regions.
  * Copy volume backups from the US West (Phoenix) and US East (Ashburn) regions to any destination regions.
  * Copy volume backups from the Germany Central (Frankfurt) and UK South (London) regions only to the Germany Central (Frankfurt) or UK South (London) regions.


Copy
```
Allow group MyTestGroup to read volume-backups in tenancy where all {request.region='lhr'}
Allow group MyTestGroup to manage volume-backups in tenancy where any {request.permission!='VOLUME_BACKUP_COPY'}
Allow group MyTestGroup to use volume-backups in tenancy where all {request.permission='VOLUME_BACKUP_COPY', any {request.region='lhr', request.region='fra'}, any{target.region='fra', target.region='lhr'}}
Allow group MyTestGroup to use volume-backups in tenancy where all {request.permission='VOLUME_BACKUP_COPY', any {request.region='phx', request.region='iad'}}
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
This procedure applies to volume backups. For volume group backups, see [To copy a volume group backup to a new region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm#Volume_group_backup_cross_region_copy).
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**. 
A list of the block volume backups in the compartment you're viewing is displayed. If you don't see the one you're looking for, make sure you're viewing the correct compartment (select from the list on the left side of the page).
  2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the block volume backup you want to copy to another region.
  3. Click **Copy to Another Region**.
  4. Enter a name for the backup and choose the region to copy the backup to. Avoid entering confidential information.
  5. In the **Encryption** section select whether you want the volume backup to use the Oracle-provided encryption key or your own Vault encryption key. If you select the option to use your own key, paste the OCID for encryption key from the destination region.
  6. Click **Copy Block Volume Backup**. 
  7. Confirm that the source and destination region details are correct in the confirmation dialog and then click **OK**.


## Using the API 🔗 
To copy a volume backup to another region, use the following operation:
  * [CopyVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CopyVolumeBackup)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
## Next Steps 🔗 
After copying the block volume backup, switch to the destination region in the Console and verify that the copied backup appears in the list of block volume backups for that region. You can then restore the backup by creating a new block volume from it using the steps in [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume).
For more information about backups, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups).
Was this article helpful?
YesNo

