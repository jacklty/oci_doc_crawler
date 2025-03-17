Updated 2024-06-04
# Backing Up a Boot Volume
You can create a backup of a boot volume using the Oracle Cloud Infrastructure Block Volume service. Boot volume backups are point-in-time snapshots of a boot volume. For more information about boot volume backups, see [Overview of Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#Overview_of_Boot_Volume_Backups).This topic describes how to create a manual boot volume backup. 
You can also configure a backup policy that creates backups automatically based on a specified schedule and retention policy. This works the same as block volumes. See [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups) for more information.
For information to help you decide whether to create a backup or a clone of a boot volume, see [Differences Between Boot Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#backupsvsclones).
**Note** Boot volume backup size may be larger than the source boot volume size. See [Boot Volume Backup Size](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#Size) for more information. See also [Boot volume backup size larger than expected](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#bootBackupSize).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
**Tip** When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same **compartment**. However, users must have access to both compartments. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to create a backup for.
  3. Click **Create Manual Backup**.
  4. Enter a name for the backup. Avoid entering confidential information.
  5. Select the backup type, either incremental or full. See [Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#backuptypes) for information about backup types. 
  6. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  7. Click **Create Backup**.
The backup is completed when its icon no longer lists it as **CREATING** in the **Boot Volume Backup** list.


## Using the API 🔗 
To back up a boot volume, use the following operation:
  * [CreateBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/CreateBootVolumeBackup)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
For more information about backups, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups) and [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume).
Was this article helpful?
YesNo

