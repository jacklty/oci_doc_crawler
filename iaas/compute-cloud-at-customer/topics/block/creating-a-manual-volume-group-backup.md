Updated 2024-01-18
# Creating a Manual Backup of a Volume Group
On Compute Cloud@Customer, you can create a volume group backup manually using the Compute Cloud@Customer Console, CLI, and API.
A volume group backup provides coordinated point-in-time-consistent backups of all the volumes in a volume group automatically. You can perform most of the same backup operations and tasks with volume groups that you can perform with individual block volumes and boot volumes. 
You can restore a volume group backup to a volume group, or you can restore individual volumes in the volume group from volume backups. With volume group backups, you can manage the backup settings for several volumes in one place, consistently. This simplifies the process to create time-consistent backups of running enterprise applications that span multiple storage volumes across multiple instances. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-group-backup.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-group-backup.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-group-backup.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume group that you want to back up.
    3. For the volume group you want to back up, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Create Volume Group Backup**.
    4. Enter a descriptive name for the backup. Avoid entering confidential information.
    5. Click **Create Volume Group Backup**.
  * Use the [oci bv volume-group-backup create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/create.html) command and required parameters to back up a volume group.
Command
CopyTry It
```
oci bv volume-group-backup create --volume-group-id <volume_group_OCID> --compartment-id <compartment_OCID> --display-name <display_name> --type FULL [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CreateVolumeGroupBackup) operation to back up a volume group.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

