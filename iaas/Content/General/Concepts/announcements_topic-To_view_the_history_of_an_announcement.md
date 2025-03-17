Updated 2023-12-08
# Viewing the History of an Announcement
View the history of an announcement for which you have related updates.
**Note** Only announcements published with a chain ID show related messages that share the same chain ID in their announcement history.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm)


  *     1. Do one of the following:
       * If you're viewing a banner, click the link embedded in the text of the banner.
       * If you're viewing a list of announcements, under the **Announcements** column, click the announcement summary.
    2. On the **Announcement details** page, under **Resources** , click **Announcement history**.
    3. (Optional) To view the contents of any related announcements, in the **Announcement history** list, under **Summary** , click the announcement summary.
  * Use the [oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html) command and required parameters to view the history of an announcement that has a chain of related messages:
Command
CopyTry It
```
oci announce announcements list --announcement-id <announcement_OCID> --chain-id <chain_ID>
```

For example: ```

oci announce announcements list --announcement-id ocid1.announcement.region1..<unique_ID> --chain-id <unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements) operation to view the history of an announcement that has related messages that share the same chain ID.


Was this article helpful?
YesNo

