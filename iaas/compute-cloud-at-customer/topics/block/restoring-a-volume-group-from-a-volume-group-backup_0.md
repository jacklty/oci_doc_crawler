Updated 2024-08-06
# Restoring a Volume Group from a Volume Group Backup
On Compute Cloud@Customer, you can restore a volume group from a volume group backup using the Compute Cloud@Customer Console, CLI, and API.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-volume-group-from-a-volume-group-backup_0.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-volume-group-from-a-volume-group-backup_0.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-volume-group-from-a-volume-group-backup_0.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Group Backups**.
    2. At the top of the page, select the compartment that contains the volume group backup that you want to restore.
    3. For the volume group backup that you want to restore, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Restore Volume Group**. 
    4. Enter the following information:
       * **Name** : Enter a descriptive name for the group.
       * **Compartment** : Select the compartment for the volume group.
       * **Backup Policy** : (Optional) Select a backup policy from the drop-down list. You might need to change the compartment.
For more information about backup policies, see [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Volume Group**.
  * Use the [oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html) command and required parameters to create a new volume group from a volume group backup.
Command
CopyTry It
```
oci bv volume-group create --availability-domain <availability_domain_name> --compartment-id <compartment_OCID>--source-details <json_string> or file://<path_to_JSON_file> [OPTIONS]
```

  * Use the [CreateVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CreateVolumeGroupBackup) operation to create a new volume group from a volume group backup.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

