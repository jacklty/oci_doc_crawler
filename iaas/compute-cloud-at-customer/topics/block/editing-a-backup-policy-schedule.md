Updated 2024-01-18
# Editing a Backup Policy Schedule
On Compute Cloud@Customer, you cannot edit an Oracle defined backup policy. You can only edit user defined backup policies.
Avoid entering confidential information.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-backup-policy-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-backup-policy-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/editing-a-backup-policy-schedule.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Backup Policies**.
    2. At the top of the page, select the compartment that contains the backup policy.
    3. Click the name of the backup policy that has the schedule you want to edit.
    4. On the backup policy details page, scroll to the **Resources** section.
    5. For the schedule that you want to edit in the **Schedules** list, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Make your changes. See [Creating a Backup Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-backup-policy.htm#creating-a-backup-policy "On Compute Cloud@Customer, you can use an Oracle defined backup policy, or you can follow the procedures described in this section to create your own backup policy.") for details.
    7. Click **Update Schedule**.
  * Use the [oci bv volume-backup-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/update.html) command and required parameters to update a user defined backup policy.
**Caution**
Running this command replaces all schedule items with the items you specify in the --schedule JSON. Include all the schedule parameters, not just the schedule parameter changes.
Command
CopyTry It
```
oci bv volume-backup-policy update --policy-id <backup_policy_OCID> --schedule <json_string> or file://<path_to_JSON_file> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/UpdateVolumeBackupPolicy) operation to update a user defined backup policy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

