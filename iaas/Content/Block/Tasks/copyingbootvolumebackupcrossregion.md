Updated 2024-09-24
# Copying a Boot Volume Backup Between Regions
You can copy boot volume backups from one region to another region using the Oracle Cloud Infrastructure Block Volume service. For more information, see [Copying Boot Volume Backups Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#Copying).
**Note**
Limitations for Copying Boot Volume Backups Across Regions
When copying boot volume backups across regions in your tenancy, you can only copy one backup per boot volume at a time from a specific source region.
You can only copy boot volume backups for instances created from [platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm), or custom images built from platform images. If you try to copy a boot volume for an instance based on other image types, such as Marketplace images, the request will fail with an error.
You cannot add compatible shapes in the destination region for boot volume backups, the shape compatibility list is from the source region and cannot be changed.
When you create an instance from the Console and specify a boot volume backup that was copied from another region as the image source, you may encounter a message indicating that there was an error loading the source image. You can ignore this error message and click **Create Instance** to finish the instance creation process and launch the instance.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The first two statements listed in the [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) policy lets the specified group do everything with boot volumes and boot volume backups with the exception of copying boot volume backups across regions. The aggregate resource type `volume-family` does not include the `BOOT_VOLUME_BACKUP_COPY` permission, so to enable copying boot volume backups across regions you need to ensure that you include the third statement in that policy, which is:
Copy
```
Allow group VolumeAdmins to use boot-volume-backups in tenancy where request.permission='BOOT_VOLUME_BACKUP_COPY'
```

To restrict access to just creating and managing boot volume backups, including copying boot volume backups between regions, use the policy in [Let boot volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#boot-volume-backup-admins-manage-only-backups). The individual resource type `boot-volume-backups` includes the `BOOT_VOLUME_BACKUP_COPY` permission, so you do not need to specify it explicitly in this policy.
If you are copying volume backups encrypted using Vault between regions or you want the copied volume backup to use Vault for encryption in the destination region, you need to use a policy that allows the Block Volume service to perform cryptographic operations with keys in the destination region. For a sample policy showing this, see [Let Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, file systems, Kubernetes secrets, and stream pools](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key).
### Restricting Access
The specific permissions needed to copy volume backups across regions are:
  * **Source region** : `BOOT_VOLUME_BACKUP_READ`, `BOOT_VOLUME_BACKUP_COPY`
  * **Destination region** : `BOOT_VOLUME_BACKUP_CREATE`


### Sample Policies
[To restrict a group to specific source and destination regions for copying volume backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm)
In this example, the group is restricted to copying volume backups from the UK South (London) region to the Germany Central (Frankfurt) region.
Copy
```
Allow group MyTestGroup to read boot-volume-backups in tenancy where all {request.region='lhr'}
Allow group MyTestGroup to use boot-volume-backups in tenancy where all {request.permission='BOOT_VOLUME_BACKUP_COPY', request.region = 'lhr', 
Allow group MyTestGroup to manage boot-volume-backups in tenancy where all {request.permission='BOOT_VOLUME_BACKUP_CREATE', request.region = 'fra'}
```

[To restrict some source regions to specific destination regions while enabling all destination regions for other source regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm)
In this example, the following is enabled for the group:
  * Manage volume backups in all regions.
  * Copy volume backups from the US West (Phoenix) and US East (Ashburn) regions to any destination regions.
  * Copy volume backups from the Germany Central (Frankfurt) and UK South (London) regions only to the Germany Central (Frankfurt) or UK South (London) regions.


Copy
```
Allow group MyTestGroup to read boot-volume-backups in tenancy where all {request.region='lhr'}
Allow group MyTestGroup to manage boot-volume-backups in tenancy where any {request.permission!='BOOT_VOLUME_BACKUP_COPY'}
Allow group MyTestGroup to use boot-volume-backups in tenancy where all {request.permission='BOOT_VOLUME_BACKUP_COPY', any {request.region='lhr', request.region='fra'}, any{target.region='fra', target.region='lhr'}}
Allow group MyTestGroup to use boot-volume-backups in tenancy where all {request.permission='BOOT_VOLUME_BACKUP_COPY', any {request.region='phx', request.region='iad'}}
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**. 
A list of the boot volume backups in the compartment you're viewing is displayed. If you don't see the one you're looking for, make sure you're viewing the correct compartment (select from the list on the left side of the page).
  2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the boot volume backup you want to copy to another region.
  3. Click **Copy to Another Region**.
  4. Enter a name for the backup and choose the region to copy the backup to. Avoid entering confidential information.
  5. In the **Encryption** section select whether you want the boot volume backup to use the Oracle-provided encryption key or your own Vault encryption key. If you select the option to use your own key, paste the OCID for encryption key from the destination region.
  6. Click **Copy Boot Volume Backup**. 
  7. Confirm that the source and destination region details are correct in the confirmation dialog and then click **OK**.


## Using the API 🔗 
To copy a boot volume backup to another region, use the following operation:
  * [CopyBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/CopyBootVolumeBackup)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
## Next Steps 🔗 
After copying the boot volume backup, switch to the destination region in the Console and verify that the copied backup appears in the list of boot volume backups for that region. You can then restore the backup using the steps in [Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingbootvolume.htm#Restoring_a_Boot_Volume).
For more information about backups, see [Overview of Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#Overview_of_Boot_Volume_Backups).
Was this article helpful?
YesNo

