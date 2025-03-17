Updated 2024-12-16
# Viewing Volume Backups
On Compute Cloud@Customer, you can view volume backups using the Compute Cloud@Customer Console, CLI, and API.
Backups that are created by backup policies (also called automatic or scheduled backups) can take up to five minutes to show in the backups list.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-volume-backups_0.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-volume-backups_0.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-volume-backups_0.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes** , **Boot Volumes** , or **Volume Groups**.
Both automatic and manual backups are listed.
    2. If you don't see your backup listed, ensure you're viewing the correct compartment, which is displayed at the top of the page.
    3. To view the details of a backup, click the backup name.
  * Use the [oci bv backup list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/list.html) command and required parameters to view the volume backups.
Command
CopyTry It
```
oci bv backup list --compartment-id <Compartment_OCID> [OPTIONS]
```

Use the [oci bv backup get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/get.html) command and required parameters to view the details of a volume backup.
Command
CopyTry It
```
oci bv volume-group-backup list --compartment-id <Compartment_OCID>
```

When there are many volume backups, for example hundreds of backups, it can take a long time to list. The `backup list` commands support pagination of results. Use the `--limit` option to specify the number of backups to list. To show the next page of results, use the value of the `opc-next-page` property with the `--page` option. Specify the `--limit` option again for each new page command. Otherwise, all remaining resources are listed. When no `opc-next-page` property is shown, all results have been listed.
By default, the list is shown in ascending order by display name, and the display name is case sensitive. You can change the list order to try to move specific resources closer to the top of the list. You can sort by (`--sort-by`) `displayname` or `timecreated` and set the sort order (`--sort-order`) to either `asc` (ascending) or `desc` (descending). The default sort order for `timecreated` is descending.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListVolumeBackups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ListVolumeBackups) operation to view the volume backups.
Use the [GetVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/GetVolumeBackup) command and required parameters to view the details of a volume backup.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

