Updated 2024-01-18
# Deleting a Backup Policy
On Compute Cloud@Customer, you cannot delete an Oracle defined backup policy. You can only delete user defined backup policies.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-backup-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-backup-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-backup-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Backup Policies**.
    2. At the top of the page, select the compartment that contains the backup policy.
    3. For the policy you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    4. Confirm the deletion.
  * Use the [oci bv volume-backup-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/delete.html) command and required parameters to delete a user defined backup policy.
Command
CopyTry It
```
oci bv volume-backup-policy delete --policy-id <policy_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteVolumeBackupPolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/DeleteVolumeBackupPolicy) operation to delete a user defined backup policy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

