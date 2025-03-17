Updated 2024-05-22
# Creating a Compute Cloud@Customer Upgrade Schedule
Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.
You must set at least one 48 hour window every quarter for upgrades. This means that at least one of the upgrade windows must be at least 48 hours in duration with a recurrence pattern of every 3rd month or shorter. You can also define shorter windows, either recurring or one-off, to accommodate smaller upgrades at convenient times. We recommend having several upgrade windows per calendar quarter.
If you don't set an upgrade schedule, Oracle can upgrade the infrastructure at any time.
All times in Compute Cloud@Customer are in UTC.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Upgrade Schedules**.
    3. Select the compartment that you want to create the upgrade schedule in.
    4. Click **Create upgrade schedule**.
    5. In the Create upgrade schedule dialog box, enter the following information:
      1. **Name:** Enter a name for the schedule so it can be assigned to one or more infrastructures. Avoid entering confidential information.
      2. **Description:** Enter an optional description. Avoid entering confidential information.
      3. **Compartment:** Select the compartment you want to create the schedule in.
    6. Under **Upgrade windows:** Define the following upgrade window parameters. These are time periods during which Oracle can upgrade the infrastructure. You're likely to need several upgrade windows in a schedule.
      1. Click **Add upgrade window**.
      2. **Description:** enter a description to identify the upgrade window. Avoid entering confidential information.
      3. **Start time:** Click the calendar icon and choose the start date and time for the window.
      4. **Duration:** Enter the duration in days and hours.
      5. To repeat the time window on a regular schedule, select **Recurring window** ; otherwise select **Single window**.
      6. To enter a recurrence pattern, either type an [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545) string or click **Build** to set up the frequency and increment of the window. In either case, you need the unit of frequency, repeat cycle, and calculation of day. The start time and duration set in the previous steps is used for each recurrence. For example, a window that recurs on the first Monday of every month would be defined as FREQ=MONTHLY;INTERVAL=1;BYDAY=MO; For more examples, see [Upgrade Window Recurrence Patterns](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/upgrade-window-recurrence.htm#upgrade-window-recurrence "Examples of RFC 5545 recurrence pattern definitions. Use these when setting upgrade windows.").
      7. Click **Create new upgrade window**.
    7. (Optional) Click **Show advanced options** to add tags to the upgrade schedule if required.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags).
    8. Click **Create upgrade schedule**.
    9. Attach the upgrade schedule to the infrastructure:
      1. Click **Infrastructures**. The Infrastructures page is displayed.
      2. On the infrastructure line, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and select **Edit**.
      3. Under **Select upgrade schedule** , use the drop-down menu to select the upgrade schedule you created. 
      4. Click **Save**.
**What's Next?**
Subscribe to upgrade notifications. See [Subscribing to Upgrade Notifications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/subscribe-to-the-notification-service.htm#enable-the-notification-service).
  * Use the [ccc upgrade-schedule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/upgrade-schedule/create.html) command and required parameters to create an upgrade schedule:
Create each upgrade window as a separate CreateCccScheduleEvent item, and supply these as a list with the --events option.
Command
CopyTry It
```
oci ccc upgrade-schedule create --compartment-id <compartment ocid> --display-name <Descriptive name> --events <List of upgrade windows, of type CreateCccScheduleEvent>... [OPTIONS]
```

Avoid entering confidential information.
After the upgrade schedule is created, attach the schedule to the infrastructures you want associated with this schedule. To attach a schedule, use the `oci ccc infrastructure update` command with the `--upgrade-schedule-id` option. For more information, see the [ccc infrastructure update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/update.html) command reference page.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next?**
Subscribe to upgrade notifications. See [Subscribing to Upgrade Notifications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/subscribe-to-the-notification-service.htm#enable-the-notification-service).
  * Use the [CreateCccUpgradeSchedule](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccUpgradeSchedule/CreateCccUpgradeSchedule) operation to create a Compute Cloud@Customer upgrade schedule.
Avoid entering confidential information.
After the upgrade schedule is created, attach the schedule to the infrastructures you want associated with this schedule. To attach a schedule, use the [UpdateCccInfrastructure](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/UpdateCccInfrastructure) API operation.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
**What's Next?**
Subscribe to upgrade notifications. See [Subscribing to Upgrade Notifications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/subscribe-to-the-notification-service.htm#enable-the-notification-service).


Was this article helpful?
YesNo

