Updated 2024-10-15
# Policy-Based Backups
The Oracle Cloud Infrastructure Block Volume service provides you with the capability to perform volume backups and volume group backups automatically on a schedule and retain them based on the selected backup policy.
With user defined policies, you can also enable scheduled cross-region backups, so that scheduled volume backups are automatically copied to a second region, see [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).
These features allow you to adhere to your data compliance and regulatory requirements. 
**Caution**
Deleting Block Volumes with Policy-Based Backups 
All policy-based backups will eventually expire, so if you want to keep a volume backup indefinitely, you need to create a [manual backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#manual), see [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backingupavolume.htm#Backing_Up_a_Volume "Create a manual backup for a volume in the Block Volume service.").
Volume backups are point-in-time snapshots of volume data. For more information about volume backups, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups).
There are two kinds of backup policies:
  * **User defined** : Custom backup policies that you create and configure schedules for. 
  * **Oracle defined** : Predefined backup policies that have a set backup frequency and retention period. You cannot modify these policies. 


**Note**
Timing for Scheduled Backups 
Scheduled volume backups are not guaranteed to start at the exact time specified by the backup schedule. You may see up to several hours of delay between the scheduled start time and the actual start time for the volume backup in scenarios where the system is overloaded. This applies to both user defined and Oracle defined backup policies.
## User Defined Backup Policies 🔗 
Oracle Cloud Infrastructure enables you to customize your backup schedules with user defined policies. These are backup policies that you define the backup frequency and retention period for. There are two parts to user defined backup policies, the backup policy itself, and then one or more schedules in the policy.
To get started with user defined backup policies, you need to first create the backup policy, see [To create a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#createcustom). After this step, you have an empty backup policy, so the next step is to define and add schedules to the policy.
### Schedules 🔗 
Schedules define the backup frequency and retention period for a user defined backup policy, just like Oracle defined backup policies. The difference is that you can customize the schedules associated with user defined policies. This gives you control over the backup frequency and retention period.
When defining a schedule for a user defined backup policy, the first thing you configure is the schedule type, this specifies the backup frequency. Oracle Cloud Infrastructure provides the following schedule types:
  * **Daily** : Backups are generated daily. You specify the hour of the day for the backup. 
  * **Weekly** : Backups are generated weekly. You specify the day of the week, and the hour of that day for the backup. 
  * **Monthly** : Backups are generated monthly. You specify the day of the month, and the hour of that day for the backup. 
  * **Yearly** : Backups are generated yearly. You specify the month, the day of that month, and the hour of that day for the backup. 


**Important**
Block Volume runs only one scheduled backup per volume per day. If more than one backup is scheduled for a volume on a particular day, the service runs only one of them, using the following priority:
  1. Yearly
  2. Monthly
  3. Weekly
  4. Daily


In addition to frequency, you also configure the following:
  * **Retention time** : The amount of time to keep the backup, in days, weeks, months, or years. The time period is based the schedule type. 
  * **Backup type** Options are full or incremental, see [Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype) for more information. 
  * **Timezone** The time zone to use for the backup schedule. Options are UTC or the regional data center time zone. 


For more information, see [To add a schedule to a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#addsched).
You can also edit or remove schedules for a user defined policy at any time, see [To edit a schedule for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#editsched) and [To delete a schedule for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#deletesched).
### Duplicating Existing Backup Policies 🔗 
You can create a new backup policy by duplicating any of the existing backup policies.
If one of the Oracle defined policies is close to meeting your volume backup requirements, but with some changes, you can create a new backup policy by duplicating the Oracle defined policy. This creates a new user defined backup policy with schedules already assigned, enabling you to use the Oracle defined policy's settings as a starting point to save time and simplify the process.
You can also duplicate an existing user defined policy. For more information, see [To duplicate a backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#duppol). You can then add, edit, or delete schedules for the new backup policy.
### Scheduling Volume Backup Copies Across Regions 🔗 
The Block Volume service enables you to copy volume backups from one region to another for business continuity and disaster recovery scenarios, for more information, see [Copying Block Volume Backups Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Copying). With user-defined policies, you can automate this process, so that volume backups are copied to another region on a schedule. Enabling the automatic copying of scheduled volume backups is only supported with user-defined policies, so if you need to use this feature for a volume currently configured with an Oracle defined policy, you need to duplicate the policy and then enable cross region copy. The volume backup copy in the target region has the same retention period as the volume backup in the source region.
**Note** Vault encryption keys for volumes aren't copied to the destination region for scheduled volume and volume group backups enabled for cross region copy. Instead, you can specify a Vault encryption key for the backup copied to the destination region when you assign the backup policy. When you assign the backup policy, if it's enabled for cross region backup copies, select **Encrypt using customer-managed keys** for **Cross region backup copy encryption** to encrypt the volume backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
**Note** It might take up to 24 hours for daily scheduled volume backups to be copied to the target region. You can verify that the volume backup was copied by switching to the target region and checking the list of volume backups for that region. If the volume backup hasn't been copied yet, you can perform a manual copy of that volume backup to the target region using the steps described in [Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Copying_a_Volume_Backup_Between_Regions).
#### Cost 🔗 
Once this feature is enabled, your bill will include charges for storing volume backups in both the source region and the destination region. You may also see an increase in network costs. For pricing details, see [Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html). The Object Storage price applies to backup storage. Outbound Data Transfer price will be applicable for network costs with cross-region backup copies.
## Oracle Defined Backup Policies 🔗 
There are three Oracle defined backup policies, Bronze, Silver, and Gold. Each backup policy is comprised of schedules with a set backup frequency and a retention period that you cannot modify. If the backup policy settings for Oracle defined policies don't meet your requirements, you should use [User Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#custom) instead. With user defined backup policies you define and control the schedules. You can also enable the automatic copying of volume backups to a second region, which is not supported with Oracle defined policies.
**Note** Oracle defined backup policies are not supported for scheduled volume group backups.
**Caution**
Full Backups and Oracle Defined Policies
As of November 3, 2021, Oracle defined policies no longer include full backups. See [Full backups removed from Oracle defined backup policies](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic-Full_backups_removed_from_Oracle_defined_policies). Incremental backups are functionally the same as full backups for data recovery purposes. Some compliance scenarios may require scheduled full backups. For these compliance scenarios, configure a user defined backup policy instead. You can create a new user defined policy from an existing backup policy, see [Duplicating Existing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#duplicatepolicy).
### Bronze Policy
The bronze policy includes monthly incremental backups, run on the first day of the month. These backups are retained for twelve months. This policy also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.
### Silver Policy
The silver policy includes weekly incremental backups that run on Sunday. These backups are retained for four weeks. This policy also includes monthly incremental backups, run on the first day of the month and are retained for twelve months. Also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.
### Gold Policy
The gold policy includes daily incremental backups, retained for seven days, along with weekly incremental backups, run on Sunday and retained for four weeks. Includes monthly incremental backups, run on the first day of the month, retained for twelve months. Also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.
## Working with Backup Policies 🔗 
There are two types of tasks when working with backup policies:
  * [Creating and Configuring User Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#configPolicies)
  * [Managing Backup Policy Assignments to Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#assignPolicies)


The linked sections listed above provide information for working with backup policies using the Console, CLI, and REST APIs.
### Required IAM Policy
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
**Important** To view or work with backup policies, you need access to the root compartment, which is where the predefined backup policies are located.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups. The policy in [Let volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-backup-admins-manage-only-backups) further restricts access to just creating and managing backups.
**Tip** When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same **compartment**. However, users must have access to both compartments. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
### Tagging Resources 🔗 
You can apply tags to your resources to help you organize them according to your business needs. You can update the resource later with the desired tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Creating and Configuring User Defined Backup Policies 🔗 
### Using the Console 🔗 
You can use the Console to create and update user defined backup policies.
[To create a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click **Create Backup Policy**.
  3. Specify a name for the backup policy. Avoid entering confidential information.
  4. Select the compartment to create the backup policy in.
While you select a compartment for the backup policy, it's accessible across your tenancy.
  5. Optionally, you can enable cross region copy to the specified region. This automates the copying of the volume backup to a second region after each backup is created. To enable cross region copy, select a target region from the **Cross Region Copy Target** list. This is the region the volume backup will be copied to. For more information, see [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).
When you assign a backup policy with cross region copy enabled to a volume, you can optionally select **Encrypt using customer-managed keys** for **Cross region backup copy encryption** to encrypt the volume backup with a Vault key from the destination region. See [Specifying a Key for Cross-Region Backup Copies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#updatebackupkey__xrrbackupkeys) for more information.
  6. Click **Create Backup Policy** to create the backup policy.


[To add a schedule to a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy you want to add the schedule to.
  3. Click **Add Schedule**.
  4. Specify the backup frequency by selecting from the **Schedule Type** options: **Daily** , **Weekly** , **Monthly** , or **Yearly** , and then configure the additional schedule options. Depending on the schedule type, the additional schedule options will include one or more of the following:
     * Hour of the day
     * Day of the week
     * Day of the month
     * Month of the year
  5. Specify the **Retention Time** , which will be in days, weeks, months, or years, depending on the schedule type you selected in the previous step.
  6. Select **Full** or **Incremental** for **Backup Type**. 
  7. Select the **Timezone** to base the schedule settings on, either **UTC** or **Regional Data Center Time**.
  8. Click **Add Schedule**.


[To enable cross region copy for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy that you want to enable cross region copy for.
  3. On the details page, click **Edit**. 
  4. Select the region you want the volume backup to be copied to in **Cross Region Copy Target** and then click **Save Changes**.


[To enable cross region copy for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy that you want to change the cross region copy target region for.
  3. On the details page, click **Edit**. 
  4. Select the region you want the volume backup to be copied to in **Cross Region Copy Target** and then click **Save Changes**.


[To disable cross region copy for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy that you want to disable cross region copy for.
  3. On the details page, click **Edit**. 
  4. Select **None** in **Cross Region Copy Target** and then click **Save Changes**.


[To duplicate a backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy that you want to duplicate.Both Oracle defined and user defined backup policies can be duplicated.
  3. Click **Duplicate**.
  4. Specify a name for the policy. Avoid entering confidential information.
  5. Select the compartment to create the backup policy in. It does not need to be the same compartment as the backup policy you are duplicating.
  6. Optionally, you can enable cross region copy to the specified region. This automates the copying of the volume backup to a second region that you specify after each backup is created. For more information, see [Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy). 
  7. Click **Duplicate Backup Policy**.


[To edit a schedule for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the backup policy that you want to edit a schedule for.
  3. In **Schedules** , for the schedule you want to edit, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
  4. After making your changes to the schedule, click **Update**.


[To delete a schedule for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the user defined backup policy that you want to delete a schedule for.
  3. In **Schedules** , for the schedule you want to delete, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Delete**.
  4. Click **Delete** in the confirmation dialog.


[To delete a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Backup Policies**.
  2. Click the user defined backup policy you want to delete. 
  3. Click **Delete**.
  4. Enter the name of the backup policy and click **Delete**.


### Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Use the following operations to work with backup policies:
[To create a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy create --compartment-id <compartment_ID> --schedules file//<path>/<scheduleJSON>.json
```

For example:
```
oci bv volume-backup-policy create --compartment-id ocid1.compartment.oc1..<unique_ID> --schedules file//~/input.json
```

[To list the backup policies in a specified compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy list --compartment-id <compartment_ID>
```

For example:
```
oci bv volume-backup-policy list --compartment-id ocid1.compartment.oc1..<unique_ID>
```

[To retrieve a specific backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy get --policy-id <backup-policy-ID>
```

For example:
```
oci bv volume-backup-policy get --policy-id ocid1.volumebackuppolicy.oc1.phx.<unique_ID>
```

[To update the display name for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy update --policy-id <backup-policy_ID> --display-name <backup-policy_name>
```

For example:
```
oci bv volume-backup-policy update --policy-id ocid1.volumebackuppolicy.oc1.phx.<unique_ID> --display-name "new display name"
```

[To update the schedules for a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy update --policy-id <backup-policy_ID> --schedules file//<path>/<scheduleJSON>.json
```

For example:
```
oci bv volume-backup-policy update --policy-id ocid1.volumebackuppolicy.oc1.phx.<unique_ID> --schedules file//~/input.json
```

[To delete a user defined backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy delete --policy-id <backup-policy_ID>
```

You can only delete a user defined backup policy if it is not assigned to any volumes. You cannot delete Oracle defined backup policies.
For example:
```
oci bv volume-backup-policy delete --policy-id ocid1.volumebackuppolicy.oc1.phx.<unique_ID>
```

### Using the API 🔗 
Use the following operations to work with backup policies:
  * [CreateVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy)
  * [DeleteVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/DeleteVolumeBackupPolicy)
  * [UpdateVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/UpdateVolumeBackupPolicy)
  * [ListVolumeBackupPolicies](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/ListVolumeBackupPolicies)
  * [GetVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/GetVolumeBackupPolicy)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
For more information about backups, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups) and [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume).
## Managing Backup Policy Assignments to Volumes 🔗 
If a volume is part of a volume group with a backup policy assignment, the backup policy assignment is managed by the volume group. In this scenario, to update the backup policy assigned you must change the assignment for the volume group or remove the volume from the group.
[To check if a volume's backup policy is managed by a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the volume for which you want to assign a backup policy to.
  3. On the **Block Volume Information** tab, in **Scheduled Backups** , check the **Managed By** field.


### Using the Console 🔗 
You can use the Console to assign, change, or remove both user defined and Oracle defined backup policies for existing volumes.
[To assign a backup policy to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the volume for which you want to assign a backup policy to.
  3. On the **Block Volume Information** tab click **Edit** .
  4. In the **BACKUP POLICIES** section, select the compartment containing the backup policies.
  5. Select the appropriate backup policy for your requirements. 
  6. Optionally, if you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
  7. Click **Save Changes**.


[To change a backup policy assigned to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the volume for which you want to change the backup policy for.
  3. On the **Block Volume Information** tab click **Edit**.
  4. In the **BACKUP POLICIES** section, select the compartment containing the backup policy.
  5. Select the backup policy you want to switch to. 
  6. Optionally, if you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information. 
  7. Click **Save Changes**.


[To remove a backup policy assigned to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the volume for which you want to remove the backup policy for.
  3. On the **Block Volume Information** tab click **Edit** .
  4. In the **BACKUP POLICIES** section, select **None** from the list, and then click **Save Changes**. 


### Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Use the following operations to work with volume backup policy assignments to volumes:
[To assign a backup policy to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment create --asset-id <volume_ID> --policy-id <policy_ID> --xrc-kms-key-id <kms_key_ID>
```

For example:
```
oci bv volume-backup-policy-assignment create --asset-id ocid1.volume.oc1..<unique_ID> --policy-id ocid1.volumebackuppolicy.oc1..<unique_ID> --xrc-kms-key-id ocid1.key.oc1.iad-ad-1.<unique_ID>
```

[To get the backup policy assigned to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id <volume_ID>
```

For example:
```
oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment --asset-id ocid1.volume.oc1..<unique_ID>
```

[To retrieve a specific backup policy assignment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
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

[To delete a backup policy assignment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup-policy-assignment delete ----policy-assignment-id <backup-policy_ID>
```

You can only delete a user defined backup policy if it is not assigned to any volumes. You cannot delete Oracle defined backup policies.
For example:
```
oci bv volume-backup-policy-assignment delete ----policy-assignment-id ocid1.volumebackuppolicyassignment.oc1.phx.<unique_ID>
```

### Using the API 🔗 
Use the following operations to manage backup policy assignments to volumes:
  * [CreateVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment)
  * [DeleteVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/DeleteVolumeBackupPolicyAssignment)
  * [GetVolumeBackupPolicyAssetAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssetAssignment)
  * [GetVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssignment)


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
For more information about backups, see [Overview of Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#Overview_of_Block_Volume_Backups) and [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume).
## Tracking the Status of Backup Operations with Events 🔗 
You can use Oracle Cloud Infrastructure Events to track the status of Block Volume backup operations. See [Block Volume Events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__block_volume) for a list of these event types. All Block Volume event types include a **status** attribute. The **status** attribute value is either **operationFailed** or **operationSucceed** , depending on the whether the backup operation succeeded or failed. 
**Note** You need to manually type the **operationFailed** and **operationSucceed** attribute values into the text box when creating a rule in the Console.
For a walkthrough of how to use the **Create Volume Backup End** event's **status** attribute to notify you when a scheduled volume backup fails, see [Using Events to Notify When a Volume Backup Fails](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm#backupstatusevents).
Was this article helpful?
YesNo

