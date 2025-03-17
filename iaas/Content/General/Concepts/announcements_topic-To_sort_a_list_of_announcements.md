Updated 2025-01-06
# Sorting Announcements
Sort announcements when you want to view announcements in a particular order, whether by the event start time, the announcement summary, the announcement type, or the time the announcement was last published.
**Note** Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Announcements**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. By default, the list displays announcements according to the event start time, from most recent to least. To sort the list another way, do one of the following:
       * Click **Summary**. The list sorts alphabetically, according to the summary of the announcement.
       * Click **Type**. The list sorts according to the importance of the announcement.
       * Click **Event Time**. The list sorts according to the start time of the event described in the announcement. If you begin by viewing the default sort order, the sort order then changes to show the oldest announcement at the beginning of the list.
       * Click **Publish Time**. The list sorts according to the time that an announcement was last updated. You might find it helpful to sort by this column to track an ongoing issue or if an announcement requires action from an administrator.
    4. (Optional) To sort the list again, repeat the previous step.
  * Use the [oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html) command and required parameters to sort a list of announcements:
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --sort-order ASC
```

You can sort a list of announcements in order of time created, either oldest to newest or newest to oldest. You can also sort a list of announcements according to one of the following criteria: announcement type (`announcementType`), reference ticket number (`referenceTicketNumber`), summary (`summary`), time created (`timeCreated`), start time (`timeOneValue`), or end time (`timeTwoValue`).
To sort a list of announcements in ascending order of time created, from oldest to newest: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --sort-order ASC
```

For example: ```

oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --sort-order ASC
```

To sort a list of announcements by other criteria: 
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID> --sort-by <sort_criteria>
```

For example: ```
oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID> --sort-by announcementType
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements) operation to sort a list of announcements.


Was this article helpful?
YesNo

