Updated 2025-01-06
# Viewing a List of All Announcements
View a list of all announcements when you want to know what announcements you have for a particular compartment, including the root compartment.
**Note** Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Announcements**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. The **Announcements** page displays all announcements for the selected compartment. From this page, you can do the following:
       * **Filter**. You can filter announcements by event start date, event end date, service, status, or platform. For more information, see [Filtering Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm#filterannouncements "Filter announcements to view only announcements that fit specific criteria. You can filter on criteria such as the announcement type, start or end date, impacted service, resolution status, and impacted platform.").
       * **Sort**. You can sort announcements by summary, status, service, event start time, or publish time (which indicates when the announcement was last updated). For more information, see [Sorting Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm#sortannouncements "Sort announcements when you want to view announcements in a particular order, whether by the event start time, the announcement summary, the announcement type, or the time the announcement was last published.").
       * **Mark as read**. You can mark announcements as read if you want stop seeing them as banners in the Console in later sessions. For more information, see [Marking an Announcement as Read](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_mark_an_announcement_as_read.htm#markannouncementsasread "Mark an announcement as read when you want it to stop displaying as unread.").
       * **Subscribe to announcements like this**. You can create a subscription to receive email delivery of only announcements that meet the criteria that you specify. For more information, see [Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm#subscriptions "Create and manage announcement subscriptions.").
       * **View announcement details**. You can view the details of an announcement. For more information, see [Viewing the Details of an Announcement](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm#viewannouncementdetails "View detailed information when you want to know more about a particular announcement.").
  * Use the [oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html) command and required parameters to list all announcements:
Command
CopyTry It
```
oci announce announcements list --compartment-id <compartment_OCID>
```

For example: ```

oci announce announcements list --compartment-id ocid1.tenancy.oc1..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements) operation to view a list of all announcements.


Was this article helpful?
YesNo

