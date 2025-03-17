Updated 2024-01-18
# Creating a Manual Boot or Block Volume Backup
On Compute Cloud@Customer, you can create a block or boot volume backup manually using the Compute Cloud@Customer Console, CLI, and API.
To create scheduled backups, see [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.")
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-manual-volume-backup.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click either **Block Volumes** or **Boot Volumes**.
    2. At the top of the page, select the compartment that contains the volume that you want to back up.
    3. For the volume you plan to back up, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Create Manual Backup**.
    4. Enter the following information:
       * **Name:** Enter a descriptive name for the backup.
       * **Compartment:** For a boot volume backup, select the compartment where you want this backup created.
       * **Tagging:**(Optional) Add defined or free-form tags for this backup as described in [Tagging Resources on Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/tagging.htm#tagging "On Compute Cloud@Customer, tagging enables you to add metadata to resources by defining key/value pairs that are assigned to resources. You can use the tags to organize and list resources based on your business needs."). Tags can also be applied later.
    5. For a block volume backup, click **Create Manual Backup**. For a boot volume backup, click **Create**.
  * Use the [oci bv backup create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/create.html) command and required parameters to create a manual backup.
Command
CopyTry It
```
oci bv backup create --volume-id <block_volume_OCID> --display-name <Backup_Name> --type FULL|INCREMENTAL [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CreateVolumeBackup) operation to create a manual backup.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

