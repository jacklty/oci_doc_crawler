Updated 2025-01-06
# Marking an Announcement as Read
Mark an announcement as read when you want it to stop displaying as unread.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_mark_an_announcement_as_read.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_mark_an_announcement_as_read.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_mark_an_announcement_as_read.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Announcements**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. Find the announcement that you want to mark as read, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Mark as read**.
  * Use the [oci announce user-status update](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/update.html) command and required parameters to mark an announcement as read:
Command
CopyTry It
```
oci announce user-status update --announcement-id <announcement_OCID> --user-status-announcement-id <announcement_OCID> --user-id <user_OCID> --time-acknowledged <date_and_time>
```

For example: ```

oci announce user-status update --announcement-id ocid1.announcement.region1..<unique_ID> --user-status-announcement-id ocid1.announcement.region1..<unique_ID> --user-id ocid1.user.region1..<unique_ID> --time-acknowledged 2019-01-06T20:14:00+00:00
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateAnnouncementUserStatus](https://docs.oracle.com/iaas/api/#/en/announcements/latest/methods/UpdateAnnouncementUserStatus) operation to mark an announcement as read.


Was this article helpful?
YesNo

