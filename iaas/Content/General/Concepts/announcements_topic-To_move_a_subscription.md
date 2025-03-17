Updated 2025-01-06
# Moving an Announcement Subscription to a Different Compartment
You can move an announcement subscription from one compartment to another.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to move, and then click the subscription name.
    4. Click **Move resource**.
    5. Click **Destination compartment** , and then select a new compartment from the list.
    6. When you're ready, click **Move resource**.
  * Use the [oci announce announcement-subscription change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/change-compartment.html) command and required parameters to move an announcement subscription to a different compartment:
Command
CopyTry It
```
oci announce announcement-subscription change-compartment --announcement-subscription-id <announcementsubscription_OCID> --compartment-id <new_compartment_OCID>
```

For example: ```
oci announce announcement-subscription change-compartment --announcement-subscription-id ocid1.announcementsubscription.<realm1>..<unique_ID> --compartment-id ocid1.compartment.<realm>..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeAnnouncementSubscriptionCompartment](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/ChangeAnnouncementSubscriptionCompartment) operation to move an announcement subscription to a different compartment.


Was this article helpful?
YesNo

