Updated 2024-01-18
# Editing a Compute Cloud@Customer Upgrade Schedule
Edit an upgrade schedule to change the time periods during which Oracle may upgrade Compute Cloud@Customer hardware and software.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-upgrade-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-upgrade-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-upgrade-schedule.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Upgrade Schedules**.
    3. Click the name of the schedule that you want to edit. If you don't see the schedule that you want, you might need to change compartments.
    4. Click **Edit** and make the necessary changes. For a description of the fields, see [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.").
    5. Click **Update upgrade schedule**.
See also [Creating an Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule-console). 
  * Use the [ccc upgrade-schedule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/upgrade-schedule/update.html) command and required parameters to update an existing upgrade schedule:
Supply a list of upgrade windows, each as a separate UpdateCccScheduleEvent item, as a list with the --events option.
Command
CopyTry It
```
oci ccc upgrade-schedule update --upgrade-schedule-id <upgrade schedule ocid> --display-name <Descriptive name> --events <List of upgrade windows, of type UpdateCccScheduleEvent>... [OPTIONS]
```

Avoid entering confidential information.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateCccUpgradeSchedule](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccUpgradeSchedule/UpdateCccUpgradeSchedule) operation to update a Compute Cloud@Customer upgrade schedule.
Avoid entering confidential information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

