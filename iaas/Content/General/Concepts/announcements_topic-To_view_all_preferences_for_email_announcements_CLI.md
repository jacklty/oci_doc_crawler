Updated 2023-12-08
# Viewing All Preferences for Email Announcements
View all preferences when you want to verify email announcement preferences for the tenancy administrator.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_all_preferences_for_email_announcements_CLI.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_all_preferences_for_email_announcements_CLI.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_all_preferences_for_email_announcements_CLI.htm)


  *     1. In the top navigation bar, click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Click **Manage administrator email preferences**.
Announcements displays the selected email announcement preferences for the tenancy administrator.
  * **Note** To view all preferences for email announcements, you must provide the compartment ID.
Use the [oci announce announcements-preferences list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/list.html) command and required parameters to list all email announcement preferences for the tenancy:
Command
CopyTry It
```
oci announce announcements-preferences list --compartment-id <root_compartment_OCID>
```

For example: ```
oci announce announcements-preferences list --compartment-id ocid1.tenancy.oc1..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncementsPreferences](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferencesSummary/ListAnnouncementsPreferences) operation to view all email announcement preferences for the tenancy administrator.


Was this article helpful?
YesNo

