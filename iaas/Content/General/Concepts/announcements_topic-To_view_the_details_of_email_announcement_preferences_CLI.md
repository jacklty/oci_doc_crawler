Updated 2023-12-08
# Viewing the Details of Email Announcement Preferences
View the details of email announcement preferences when you want to verify specific email announcement preferences for the tenancy administrator.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_email_announcement_preferences_CLI.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_email_announcement_preferences_CLI.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_email_announcement_preferences_CLI.htm)


  *     1. In the top navigation bar, click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Click **Manage administrator email preferences**.
Announcements displays the selected email announcement preferences for the tenancy administrator.
  * **Note** To view detailed information about preferences for email announcements, you must provide the preference ID.
Use the [oci announce announcements-preferences get](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/get.html) command and required parameters to view the details of email announcement preferences for the tenancy administrator:
Command
CopyTry It
```
oci announce announcements-preferences get --preference-id <preference_OCID>
```

For example: ```
oci announce announcements-preferences get --preference-id ocid1.tenancy.oc1..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetAnnouncementsPreference](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferences/GetAnnouncementsPreference) operation to view email announcement preferences for the tenancy administrator.


Was this article helpful?
YesNo

