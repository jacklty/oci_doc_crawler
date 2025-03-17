Updated 2024-01-18
# Deleting a Backup Policy Schedule
On Compute Cloud@Customer, you cannot change an Oracle defined backup policy. You can only change or delete the schedules of user defined backup policies.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleteing-a-backup-policy-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleteing-a-backup-policy-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleteing-a-backup-policy-schedule.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Backup Policies**.
    2. At the top of the page, select the compartment that contains the backup policy that has the schedule you want to delete.
    3. Click the name of the backup policy that has the schedule you want to delete.
    4. On the **Backup Policy** page, scroll to the **Resources** section.
    5. For the schedule you want to delete in the **Schedules** list, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Confirm the deletion.
  * Use the [oci bv volume-backup-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/delete.html) command and required parameters to delete a backup policy.
Copy
```
oci bv volume-backup-policy delete \
--policy-id ocid1.volumebackuppolicy. _unique_ID_ --force
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

