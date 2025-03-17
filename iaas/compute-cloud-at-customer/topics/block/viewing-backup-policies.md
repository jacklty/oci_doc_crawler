Updated 2024-01-18
# Viewing Backup Policies
On Compute Cloud@Customer, after creating a backup policy, you can use the Compute Cloud@Customer Console, CLI, or API to view the policy.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-backup-policies.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-backup-policies.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/viewing-backup-policies.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Backup Policies**.
At a minimum, the Oracle defined policies are listed. If the compartment has any user defined policies, then both Oracle defined and user defined policies are listed.
    2. To view a particular user defined policy, you might need to select a different compartment from the top of the page.
    3. To see details about a policy, click the policy name. Scroll to the **Resources** section to see the schedules.
  * Use the [oci bv volume-backup-policy list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/list.html) command and required parameters to list all the volume backup policies available in the specified compartment.
Command
CopyTry It
```
oci bv volume-backup-policy list --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListVolumeBackupPolicies](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/ListVolumeBackupPolicies) operation to list all the volume backup policies available in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

