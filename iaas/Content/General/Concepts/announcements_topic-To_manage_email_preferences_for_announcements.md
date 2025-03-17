Updated 2023-12-08
# Managing Email Preferences for Tenancy Administrators
Administrator email preferences specify whether the tenancy administrator wants to opt in or opt out of receiving emailed copies of service status announcements. Administrator email preferences have no impact on any announcement subscriptions you might have.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm)


  *     1. In the top navigation bar, click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Click **Manage administrator email preferences**.
    3. Do one of the following:
       * If you want Oracle to send email announcements, click **Opt in to receive email announcements**. By default, Oracle emails only announcements that impact tenancy resources and about outages. If you prefer to receive all announcements, including informational announcements that require no action or that more generally address customers, also click **Send email for all announcements, including informational announcements specific to this tenancy**.
       * If you want Oracle to withhold email copies of announcements, click **Opt out to stop receiving all email announcements**. You must also select the check box to acknowledge that you understand opting out can result in important missed email that could impact the tenancy.
**Note** Regardless what you configure here, the tenancy administrator can still receive email announcements if you create a subscription that includes the administrator's email address as a delivery endpoint. For more information about subscriptions, see [Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm#subscriptions "Create and manage announcement subscriptions.").
    4. In the previous step, if you chose to opt in, also specify the time zone you prefer for announcement time stamps by clicking **Time zone** and choosing a time zone. Otherwise, continue to the next step.
    5. When you're finished, click **Save changes**.
  * **Note** By default, the tenancy administrator receives email announcements. When explicitly specifying email preferences, you can either create or update them. You get the same result. However, you do need the preference ID if you want to update preferences.
Use the [oci announce announcements-preferences create](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/create.html) or [oci announce announcements-preferences update](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/update.html) command and required parameters to specify email preferences for the tenancy administrator.
To use the `oci announce announcements-preferences create` command to create email preferences:
Command
CopyTry It
```
oci announcement announcements-preferences create --preference-type <opt_in_or_opt_out_selection> --type <string_specifying_whether_to_create_or_update_preferences> --preferred-time-zone
 <time_zone_in_IANA_Time_Zone_Database_format> --compartment-id <root_compartment_OCID>
```

For example: ```

oci announce announcements-preferences create --preference-type OPT_IN_TENANT_ANNOUNCEMENTS --type CreateAnnouncementsPreferencesDetails --preferred-time-zone
 "America/Los_Angeles" --compartment-id ocid1.tenancy.oc1..<unique_ID>
```

To use the `oci announce announcements-preferences update` command to update email preferences:
Command
CopyTry It
```
oci announce announcements-preferences update --preference-id <preference_OCID> --preference-type <opt_in_or_opt_out_selection> --type <string_specifying_whether_to_create_or_update_preferences> --preferred-time-zone <time_zone_in_IANA_Time_Zone_Database_format> --compartment-id <compartment_OCID>
```

For example:```

oci announce announcements-preferences update --preference-id ocid1.tenancy.oc1..<unique_ID> --preference-type OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS --type UpdateAnnouncementsPreferencesDetails --preferred-time-zone "America/Los_Angeles" --compartment-id ocid1.tenancy.oc1..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * **Note** By default, the tenancy administrator receives email announcements. When explicitly specifying email preferences, you can either create or update them. You get the same result. However, you do need the preference ID if you want to update preferences.
Run the [CreateAnnouncementsPreference](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferencesSummary/CreateAnnouncementsPreference) operation to create email preferences for the tenancy administrator. Or, run the [UpdateAnnouncementsPreference](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferencesSummary/UpdateAnnouncementsPreference) operation to update existing email preferences.


Was this article helpful?
YesNo

