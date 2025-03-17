Updated 2024-10-15
# Working with Volume Groups
The Oracle Cloud Infrastructure Block Volume service provides you with the capability to group together many volumes in a volume group. A volume group can include both types of volumes, boot volumes, which are the system disks for your compute instances, and block volumes for your data storage. You can use volume groups to create volume group backups and clones that are point-in-time and crash-consistent.
## Tasks 🔗 
This section includes the following tasks:
  * [Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#top "Create a volume group in the Block Volume service.")
  * [Cloning a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm#top "Clone a volume group in the Block Volume service.")
  * [Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm#top "List volume groups in the Block Volume service.")
  * [Getting a Volume Group's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm#top "Get details for a volume group in the Block Volume service, including a list of the block volumes and boot volumes in the volume group.")
  * [Updating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm#top "Update a volume group in the Block Volume service. For example, add or remove block volumes or boot volumes.")
  * [Moving a Volume Group to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm#top "Move a volume group in the Block Volume service to another compartment.")
  * [Tagging a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-volume-group.htm#top "Add metadata to a volume group in the Block Volume service.")
    * [Tagging a Volume Group at Creation](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-create-volume-group.htm#top "Add metadata to a volume group when you first create it. This metadata enables you to define keys and values and to associate them with resources.")
    * [Tagging a Volume Group When Updating](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/tag-update-volume-group.htm#top "Add metadata to a volume group when you update it. This metadata enables you to define keys and values and to associate them with resources.")
  * [Deleting a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm#top "Delete a volume group in the Block Volume service.")


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes, backups, and volume groups.
See the following policy examples for working with volume groups: 
  * [Let users create a volume group](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-creators-create-volume-groups) lets the specified group create a volume group from a set of volumes.
  * [Let users clone a volume group](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-cloners-clone-volume-groups) lets the specified group clone a volume group from an existing volume group.
  * [Let users create a volume group backup](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#backup-volume-groups) lets the specified group create a volume group backup.
  * [Let users restore a volume group backup](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#restore-volume-group-backup) lets the specified group create a volume group by restoring a volume group backup.


**Tip** When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same **compartment**. However, users must have access to both compartments. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## About Volume Groups 🔗 
Volume groups simplify the process to create time-consistent backups of running enterprise applications that span several storage volumes across several instances. You can then restore an entire group of volumes from a volume group backup.
Similarly, you can also clone an entire volume group in a time-consistent and crash-consistent manner. A deep disk-to-disk and fully isolated clone of a volume group, with all the volumes associated in it, becomes available for use within a matter of seconds. This speeds up the process of creating new environments for development, quality assurance, user acceptance testing, and troubleshooting.
For more information about Block Volume-backed system disks, see [Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm#Boot_Volumes). For more information about Block Volume backups see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups). See [Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.") for more information about Block Volume clones.
This capability is available using the Console, CLI, SDKs, or REST APIs.
Volume groups and volume group backups are high-level constructs that allow you to group together several volumes. When working with volume groups and volume group backups, keep the following in mind:
  * You can only add a volume to a volume group when the volume status is available.
  * You can add up to 32 volumes in a volume group, up to a maximum size limit of 128 TB. For example, if you wanted to add 32 volumes of equal size to a volume group, the maximum size for each volume would be 4 TB. Or you could add volumes that vary in size, however the overall combined size of all the block and boot volumes in the volume group must be 128 TB or less. Ensure you account for the size of any boot volumes in your volume group when considering volume group size limits.
  * Each volume can only be in one volume group.
  * When you clone a volume group, a new group with new volumes is created. For example, if you clone a volume group containing three volumes, then at completion of the operation, you have two separate volume groups and six different volumes with nothing shared between the volume groups.
  * When you update a volume group using the CLI, SDKs, or REST APIs, you need to specify all the volumes to include in the volume group each time you use the update operation. If you don't include a volume ID in the update call, that volume is removed from the volume group.
  * When you delete a volume group, the individual volumes in the group aren't deleted, only the volume group is deleted.
  * When you delete a volume that's part of a volume group, you must first remove it from the volume group before you can delete it.
  * When you delete a volume group backup, all the volume backups in the volume group backup are deleted.


## Volume Group Replication 🔗 
The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of volume groups to other regions. This feature supports the following scenarios without requiring volume group backups:
  * Disaster recovery
  * Migration
  * Business expansion


For more information, see [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains."). For specific details about volume groups, including step-by-step procedures using the Console and CLI, see [Volume Group Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication "You can use the Block Volume service's replication feature for volume groups.").
## Volume Group Backups 🔗 
A volume group backup provides coordinated point-in-time-consistent backups of all the volumes in a volume group automatically. You can perform most of the same backup operations and tasks with volume groups that you can perform with individual block volumes and boot volumes. You can restore a volume group backup to a volume group, or you can restore individual volumes in the volume group from volume backups. With volume group backups, you can manage the backup settings for several volumes in one place, consistently. This simplifies the process to create time-consistent backups of running enterprise applications that span multiple storage volumes across multiple instances. 
For a general overview of the Block Volume's service backup functionality, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups). 
### Source Region 🔗 
Volume group backups include a **Source Region** field. This specifies the region for the volume group that the backup was created from. For volume group backups copied from another region, this field will show the region the volume group backup was copied from.
### Manual Volume Group Backups 🔗 
Manual backups are on-demand one-off backups that you can launch immediately for volume groups by following the steps outlined in the procedures in this section. For general information about the manual backups feature for the Block Volume service, see [Manual Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#manual).
#### Using the Console 🔗 
[To create a backup of the volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. In the **Volume Groups** list, click **Create Volume Group Backup** in the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the volume group you want to create a backup for.


[To restore a volume group from a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Group Backups**.
  2. In the **Volume Group Backups** list, click the volume group backup you want to restore.
  3. Click **Create Volume Group**.
  4. Fill in the required volume information:
     * **Name** : A user-friendly name or description. Avoid entering confidential information.
     * **Compartment** : The compartment for the volume group.
     * **Availability Domain** : The availability domain for the volume group.
     * **Cluster Placement Group** : (Optional) Select the cluster placement group in which to restore the volume group to. 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases.").
  5. Click **Create Volume Group**.


[To copy a volume group backup to a new region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
For more information about copying volume backups and volume group backups to new regions, see [Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Copying_a_Volume_Backup_Between_Regions). Before you can copy a volume group backup to a new region, ensure that you have configured the requred permissions, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Required).
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Group Backups**.
  2. In the **Volume Group Backups** list, click the volume group backup you want to copy to a new region.
  3. Click **Copy to Another Region**.
  4. Enter a name for the backup and choose the region to copy the backup to. Avoid entering confidential information.
  5. In the **Encryption** section select whether you want the volume group backup to use the Oracle-provided encryption key or your own Vault encryption key. If you select the option to use your own key, paste the OCID for encryption key from the destination region.
  6. Click **Copy Block Volume Backup**.
  7. Confirm that the source and destination region details are correct in the confirmation dialog and then click **OK**.


#### Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
[To list volume backup groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup list --compartment-id <compartment_ID>
```

For example:
```
oci bv volume-group-backup list --compartment-id ocid1.compartment.oc1..<unique_ID>
```

[To create a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup create --volume-group-id <volume-group_ID>
```

For example:
```
oci bv volume-group-backup create --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID>
```

[To retrieve a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup get --volume-group-backup-id <volume-group-backup_ID>
```

For example:
```
oci bv volume-group-backup get --volume-group-backup-id ocid1.volumegroupbackup.oc1.phx.<unique_ID>
```

[To update display name for a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup update --volume-group-backup-id <volume-group-backup_ID> --display-name <new_display_name>
```

You can only update the display name for the volume group backup.
For example:
```
oci bv volume-group-backup update --volume-group-backup-id ocid1.volumegroupbackup.oc1.phx.<unique_ID> --display-name "new display name"
```

[To restore a volume group from a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group create --compartment-id <compartment_ID> --availability-domain <external_AD> --source-details <Source_details_JSON>
```

For example:
Command
CopyTry It
```
oci bv volume-group create --compartment-id ocid1.compartment.oc1..<unique_ID> --availability-domain ABbv:PHX-AD-1 --source-details '{"type": "volumeGroupBackupId", "volumeGroupBackupId": "ocid1.volumegroup.oc1.sea.<unique_ID>"}'
```

[To delete a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup delete --volume-group-backup-id <volume-group-backup_ID>
```

When you delete a volume group backup, all volume backups in the group are deleted.
For example:
```
oci bv volume-group-backup delete --volume-group-backup-id ocid1.volumegroupbackup.oc1.phx.<unique_ID>
```

#### Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations for working with volume group backups:
  * [ListVolumeGroupBackups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/ListVolumeGroupBackups)
  * [CreateVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CreateVolumeGroupBackup)
  * [DeleteVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/DeleteVolumeGroupBackup)
  * [GetVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/GetVolumeGroupBackup)
  * [UpdateVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/UpdateVolumeGroupBackup)
  * [CopyVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CopyVolumeGroupBackup)


### Policy-Based Volume Group Backups 🔗 
These are automated scheduled backups as defined by the backup policy assigned to the volume group. Policy-based backups for volume groups are the same as policy-based backups for block volumes, the main difference is that the backup policy is applied to all the volumes in the volume group instead of a single volume. For general information about policy-based backups, see [Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#PolicyBased_Backups). The process to create and configure user defined backup policies are the same for volume groups as they're for volumes, see [Creating and Configuring User Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#configPolicies) for these procedures.
**Note** Vault encryption keys for volumes aren't copied to the destination region for scheduled volume and volume group backups enabled for cross region copy. Instead, you can specify a Vault encryption key for the backup copied to the destination region when you assign the backup policy. When you assign the backup policy, if it's enabled for cross region backup copies, select **Encrypt using customer-managed keys** for **Cross region backup copy encryption** to encrypt the volume or volume group backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
**Note** Oracle defined backup policies aren't supported for scheduled volume group backups.
#### Managing Backup Policy Assignments to Volume Groups 🔗 
The backup policy assigned to a volume group defines the frequency and schedule for volume group backups. This section covers how to perform tasks related to managing the backup policy assignments for your volume groups using the Console, command line interface (CLI), and REST APIs. 
If a volume group has an assigned backup policy, you must remove any backup policy assignments from volumes before you can add them to the volume group. 
Before you can assign a backup policy to an existing volume group containing one or more volumes with assigned backup policies, you must remove those policy assignments from the invidual volumes before you can assign the policy to the volume group.
##### Using the Console 🔗 
[To assign a backup policy to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group for which you want to assign a backup policy to.
  3. On the **Volume Group Details** page click **Edit** .
  4. In the **BACKUP POLICIES** section, select the compartment containing the backup policies.
  5. Select the appropriate backup policy for your requirements. 
  6. Optionally, if you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  7. Click **Save Changes**.


[To change a backup policy assigned to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group for which you want to change the backup policy for.
  3. On the **Volume Group Details** page click **Edit**.
  4. In the **BACKUP POLICIES** section, select the compartment containing the backup policy.
  5. Select the backup policy you want to switch to. 
  6. Optionally, if you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, for more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  7. Click **Save Changes**.


[To remove a backup policy assigned to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group for which you want to remove the backup policy for.
  3. On the **Volume Group Details** page click **Edit** .
  4. In the **BACKUP POLICIES** section, select **None** from the list, and then click **Save Changes**. 


##### Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
[To assign a backup policy to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment create --asset-id <volume_group_ID> --policy-id <policy_ID> --xrc-kms-key-id <kms_key_ID>
```

For example:
```
oci bv volume-backup-policy-assignment create --asset-id ocid1.volumegroup.oc1..<unique_ID> --policy-id ocid1.volumebackuppolicy.oc1..<unique_ID> --xrc-kms-key-id ocid1.key.oc1.iad-ad-1.<unique_ID>
```

[To get the backup policy assigned to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id <volume_group_ID>
```

For example:
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id ocid1.volumegroup.oc1..<unique_ID>
```

[To change a backup policy assigned to a volume group using the CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment create --asset-id <volume_group_ID> --policy-id <policy_ID> --xrc-kms-key-id <kms_key_ID>
```

For example:
```
oci bv volume-backup-policy-assignment create --asset-id ocid1.volumegroup.oc1..<unique_ID> --policy-id ocid1.volumebackuppolicy.oc1..<unique_ID> --xrc-kms-key-id ocid1.key.oc1.iad-ad-1.<unique_ID>
```

[To retrieve a specific backup policy assignment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment get --policy-assignment-id <backup-policy-ID>
```

For example:
```
oci bv volume-backup-policy-assignment get --policy-assignment-id ocid1.volumebackuppolicyassignment.oc1.phx.<unique_ID>
```

##### Using the API 🔗 
Use the following operations to manage backup policy assignments to volume groups:
  * [CreateVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment)
  * [DeleteVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/DeleteVolumeBackupPolicyAssignment)
  * [GetVolumeBackupPolicyAssetAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssetAssignment)
  * [GetVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssignment)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Was this article helpful?
YesNo

