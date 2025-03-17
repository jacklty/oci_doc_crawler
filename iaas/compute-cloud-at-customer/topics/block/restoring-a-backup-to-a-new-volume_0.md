Updated 2024-08-06
# Restoring a Backup to a New Volume
On Compute Cloud@Customer, you can restore a volume backup to a new volume using the Compute Cloud@Customer Console, CLI, and API.
You can restore a volume from any of your incremental or full volume backups. Both backup types enable you to restore the full volume contents to the point-in-time snapshot of the volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about. 
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-backup-to-a-new-volume_0.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-backup-to-a-new-volume_0.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/restoring-a-backup-to-a-new-volume_0.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volume Backups**.
    2. At the top of the page, select the compartment that contains the block volume backup that you want to restore.
    3. For the block volume backup that you want to restore, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Restore Block Volume**.
    4. Enter the following information:
       * **Name:** A name or description for the volume. Avoid entering confidential information.
       * **Compartment:** Select the compartment in which to restore the block volume.
       * **Size (in GBs):** To change the size, enter a value from 50 to 32768 (50 GB to 32 TB) in 1 GB increments. You cannot enter a smaller value than the value that is shown.
       * **High Performance Volume:** (Optional) By default, the volume uses balanced performance. To create a block volume that uses the high performance feature, click the Enable High Performance button.
This selection can't be changed after the volume is created.
       * **Backup Policy:** (Optional) Select a backup policy from the drop-down list. You might need to change the compartment.
For more information about backup policies, see [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.").
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Block Volume**.
The volume is ready to attach after its icon no longer lists it as PROVISIONING in the volume list.
  * Use the [oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html) command and required parameters to restore a backup to a new volume.
Command
CopyTry It
```
oci bv volume create --availability-domain <availability_domain_name> --volume-backuup-id <source_volume_backup_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation to restore a backup to a new volume. The API has an optional `volumeBackupId` parameter that you can use to define the backup from which the data should be restored on the newly created volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

