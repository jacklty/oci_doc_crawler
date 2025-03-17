Updated 2024-02-05
# Deleting a Compute Cloud@Customer Upgrade Schedule
When you delete a schedule, all upgrade windows in the schedule are deleted.
**Note**
You can't delete an upgrade schedule that's being used by an infrastructure. However, you can change an upgrade schedule to be an _any time_ schedule. An any time schedule enables an upgrade to occur anytime, which provides the same functionality as not having an upgrade schedule. To create an any time schedule, see [Editing a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-upgrade-schedule.htm#edit-upgrade-schedule "Edit an upgrade schedule to change the time periods during which Oracle may upgrade Compute Cloud@Customer hardware and software."), and set the schedule to use an any time recurrence pattern as shown in [Upgrade Window Recurrence Patterns](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/upgrade-window-recurrence.htm#upgrade-window-recurrence "Examples of RFC 5545 recurrence pattern definitions. Use these when setting upgrade windows.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-upgrade-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-upgrade-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-upgrade-schedule.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Upgrade Schedules**.
    3. Click the name of the upgrade schedule that you want to delete. If you don't see the upgrade schedule that you want, you might need to change compartments.
    4. Click **Delete** , and then click **Delete** to confirm.
  * Use the [ccc upgrade-schedule delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/upgrade-schedule/delete.html) command and required parameters to delete an upgrade schedule and the upgrade windows associated with it:
Command
CopyTry It
```
oci ccc upgrade-schedule delete --upgrade-schedule-id <upgrade schedule ocid> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteCccUpgradeSchedule](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/DeleteCccUpgradeSchedule) operation to delete a Compute Cloud@Customer upgrade schedule.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

