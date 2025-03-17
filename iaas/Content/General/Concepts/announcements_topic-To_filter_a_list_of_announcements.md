Updated 2025-01-06
# Filtering Announcements
Filter announcements to view only announcements that fit specific criteria. You can filter on criteria such as the announcement type, start or end date, impacted service, resolution status, and impacted platform.
**Note** Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Announcements**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. By default, the page displays a list of all announcements for the selected compartment. To see announcements filtered by announcement type, click the following tabs:
       * **Required actions**. Announcements that require you to take specific action within the current environment.
       * **Recommended actions**. Announcements that describe specific action to take within the current environment, but the action isn't required.
       * **Planned maintenance**. Announcements that describe a time period during which planned maintenance activities are performed on the current environment. Maintenance activities can include restarting services or other similarly impactful actions.
       * **Other**. All announcements of a different type from the three preceding announcement types.
    4. (Optional) To filter the list of announcements further, under **Filters** , do one or more of the following:
       * To see events that started at or after a particular time and date, click **Earliest event start date** , and then choose a date.
       * To see events that ended at or before a particular time and date, click **Earliest event end date** , and then choose a date.
       * To see announcements that impact a particular service, click **Service** , and then enter a service name. Ensure that you type the name of the service as it appears in the Console. 
**Note** If you include more than one service, then the filter effectively screens for announcements that impact all specified services.
       * To see announcements that match a particular status, click **Status** , and then choose an option.
       * To see announcements by platform, click **Platform** , and then choose either announcements that impact the Oracle Cloud Infrastructure (**IaaS**) platform or announcements that impact Software as a Service (**SaaS**) applications.
    5. (Optional) To clear all filters on the list of announcements, click **Reset**.
  * Use the [oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html) command and required parameters to filter a list of announcements. When using the command line, you can filter a list of announcements by announcement type, environment name, lifecycle state, platform type, service, and time (earliest start time and latest start time).
To filter a list of announcements by announcement type: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --announcement-type <announcement_type>
```

For example: ```

oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --announcement-type ACTION_REQUIRED
```

To filter a list of announcements by environment name: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --environment-name <environment_name>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --environment-name testenv
```

To filter a list of announcements by lifecycle state: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --lifecycle-state <lifecycle_state>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --lifecycle-state ACTIVE
```

To filter a list of announcements by platform type: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --platform-type <platform_type>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --platform-type IAAS
```

To filter a list of announcements by service: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --service <service_name>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --service "Oracle Cloud Infrastructure Networking""
```

**Note** If you include more than one service, then the filter effectively screens for announcements that impact all specified services.
To filter a list of announcements by time: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --time-one-earliest-time <earliest_start_time> --time-one-latest-time <latest_start_time>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --time-one-earliest-time "2022-01-01T20:08:00+00:00" --time-one-latest-time "2022-02-25T20:08:00+00:00"
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements) operation to filter a list of announcements.


Was this article helpful?
YesNo

