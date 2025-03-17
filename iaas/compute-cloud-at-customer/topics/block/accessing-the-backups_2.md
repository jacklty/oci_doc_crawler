Updated 2024-01-18
# Accessing the Backups
On Compute Cloud@Customer, after a manual or automatic backup takes place, you can use the topics in this section to locate the backup.
**Note**
For scheduled or policy-based backups, there might be a delay of up to 5 minutes for backups to show up in the list. This delay applies to viewing backups in the Compute Cloud@Customer Console, CLI, and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/accessing-the-backups_2.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/accessing-the-backups_2.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/accessing-the-backups_2.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then select one of the following items:
       * **Block Volume Backups**
       * **Volume Group Backups**
The manual and automatic backups are displayed.
    2. To see the details of a backup, click the backup name.
  * Use the [oci bv backup list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/list.html) command and required parameters to list the volume backups in the specified compartment.
Command
CopyTry It
```
oci bv backup list --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListVolumeBackups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ListVolumeBackups) operation to list the volume backups in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

