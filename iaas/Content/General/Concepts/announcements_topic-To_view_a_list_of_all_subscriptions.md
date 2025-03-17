Updated 2025-01-06
# Viewing a List of All Announcement Subscriptions
Viewing a list of all announcement subscriptions lets you see all subscriptions in one place and take action in various ways.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. The **Subscriptions** page displays all announcement subscriptions for the selected compartment. From this page, you can do the following:
       * **Create a subscription**. You can create an announcement subscription to receive email delivery of only announcements that meet your criteria. For more information, see [Creating an Announcement Subscription](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm#createsubscription "Create an announcement subscription to deliver specific announcements to a particular list of recipients.").
       * **Manage administrator email preferences**. You can manage email preferences for the tenancy administrator. For more information, see [Email Delivery](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Email_Delivery.htm#email "As part of an organization's service agreement, Oracle Cloud Infrastructure also contacts the tenancy administrator with service status announcements through email.").
       * **View subscription details**. You can view the details of an announcement subscription. For more information, see [Viewing the Details of an Announcement Subscription](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm#viewsubscriptiondetails "View detailed information about an announcement subscription when you want to learn more about a particular subscription.").
       * **Delete subscriptions**. You can delete announcement subscriptions. For more information, see [Deleting an Announcement Subscription](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_a_subscription.htm#deletesubscription "Delete an announcement subscription when you no longer need it.").
  * Use the [oci announce announcement-subscription list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/list.html) command and required parameters to view a list of all announcement subscriptions:
Command
CopyTry It
```
oci announce announcement-subscription list --compartment-id <compartment_OCID>
```

For example: ```
oci announce announcement-subscription list --compartment-id ocid1.compartment.<realm>..<unique_ID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListAnnouncementSubscriptions](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/ListAnnouncementSubscriptions) operation to view a list of all announcement subscriptions.


Was this article helpful?
YesNo

