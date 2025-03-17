Updated 2025-01-06
# Viewing the Details of an Announcement Subscription
View detailed information about an announcement subscription when you want to learn more about a particular subscription.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. The **Subscriptions** page displays all announcement subscriptions for the selected compartment. Under the **Name** column, click the name of the subscription that you want to view in detail.
    4. On the **Subscription details** page, you can view the following information:
       * **Name**. The name of the announcement subscription.
       * **Lifecycle state**. The current lifecycle state of the announcement subscription resource itself.
       * **OCID**. The announcement subscription's unique, Oracle-assigned identifier.
       * **Compartment**. The compartment where the announcement subscription exists.
       * **Description**. A description of the announcement subscription.
       * **Notifications topic**. The Notifications topic used by the announcement subscription to publish announcements to subscribers.
       * **Filter group details**. Information about the filter groups configured for the announcement subscription.
       * **Tags**. Any defined or freeform tags added to the announcement subscription resource.
  * Use the [oci announce announcement-subscription get](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/get.html) command and required parameters to view the details of an announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription get --announcement-subscription-id <announcementsubscription_OCID>
```

For example: ```
oci announce announcement-subscription get --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID>
```

Viewing the details of an announcement subscription provides you with the following information:
    * **Name**. The name of the announcement subscription.
    * **Lifecycle state**. The current lifecycle state of the announcement subscription resource itself.
    * **OCID**. The announcement subscription's unique, Oracle-assigned identifier.
    * **Compartment**. The compartment where the announcement subscription exists.
    * **Description**. A description of the announcement subscription.
    * **Notifications topic**. The Notifications topic used by the announcement subscription to publish announcements to subscribers.
    * **Filter group details**. Information about the filter groups configured for the announcement subscription.
    * **Tags**. Any defined or freeform tags added to the announcement subscription resource.
    * **Time created**. When the announcement subscription was created.
    * **Time updated**. When the announcement subscription was last updated.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/GetAnnouncementSubscription) operation to view the details of an announcement subscription.


Was this article helpful?
YesNo

