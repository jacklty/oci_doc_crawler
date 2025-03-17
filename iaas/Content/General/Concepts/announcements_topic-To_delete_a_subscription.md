Updated 2025-01-06
# Deleting an Announcement Subscription
Delete an announcement subscription when you no longer need it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to delete, and then click the subscription name.
    4. Click **Delete**.
    5. To confirm, click **Delete subscription**.
  * Use the [oci announce announcement-subscription delete](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/delete.html) command and required parameters to delete an announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription delete --announcement-subscription-id <announcementsubscription_OCID>
```

For example: ```
oci announce announcement-subscription delete --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/DeleteAnnouncementSubscription) operation to delete an announcement subscription.


Was this article helpful?
YesNo

