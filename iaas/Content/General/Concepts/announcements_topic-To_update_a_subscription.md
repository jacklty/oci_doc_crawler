Updated 2025-01-06
# Updating an Announcement Subscription
You can update an active subscription by changing its name, description, or Notifications topic.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. In the list of subscriptions, find the subscription you want to update, and then click the subscription name.
    4. Click **Edit**.
    5. (Optional) Click **Name** , and then update the subscription name. Avoid entering confidential information.
    6. (Optional) Click **Description**. and then update the description. Avoid entering confidential information.
    7. (Optional) Under **Display preferences** , click **Time zone** , and then choose the time zone that you prefer for announcement time stamps.
    8. (Optional) If you created a filter that specified the service Oracle Fusion Applications, click **Language** , and then choose the language that you prefer for displaying announcements delivered by email. By default, the language is set to whatever you configured in the Console language selector.
**Note** You can't modify filter groups when a language display preference is part of a subscription. If you need changes to the filter groups later, you must create a new subscription.
    9. (Optional) Under **Notifications topic** , do one of the following:
       * To use an existing Notifications topic, click **Use existing topic** , and then choose a topic from the selected compartment. (If needed, to list resources in a different compartment, click **Compartment** and choose a compartment.)
       * To create a new Notifications topic, click **Create new topic** , and then provide the following:
Option | Description  
---|---  
**Compartment** | Select the compartment where you want to create the topic.  
**Name** | Enter a name for the topic. (Avoid entering confidential information.)  
**Description** | Enter a description for the topic. (Avoid entering confidential information.)  
**Subscription protocol** |  Choose the protocol used by subscription endpoints. The information you must provide about the subscription endpoint depends on the protocol. If you select **Email** , then click **Email address** and enter a valid email address. For more information, see [Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm). If you select **Function** , then specify the Oracle Cloud Infrastructure Functions application and function by selecting an **Oracle Functions application** and then **Function**. (If needed, click **Function compartment** to list resources in a different compartment.) For more information, see [Creating a Function Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-function.htm). If you select **HTTPS custom URL** , then click **URL** and enter a valid HTTPS URL. For more information, see [Creating an HTTPS (Custom URL) Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-https.htm). If you select **PagerDuty** , click **URL** and enter a valid PagerDuty URL. For more information, see [Creating a PagerDuty Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-pagerduty.htm). If you select **Slack** , click **URL** and enter the URL of a valid Slack channel. For more information, see [Creating a Slack Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm). If you select **SMS** , specify a **Country** and **Phone Number**. For more information, see [Creating an SMS Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm). Optionally, to add another subscription protocol to this topic, click **+ Another subscription**.  
    10. When you're ready, click **Save changes**.
  * Use the [oci announce announcement-subscription update](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/update.html) command and required parameters to update an announcement subscription:
Command
CopyTry It
```
oci announce announcement-subscription update --announcement-subscription-id <announcementsubscription_OCID>
```

For example, to change a subscription name: ```
oci announce announcement-subscription update --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --display-name newsubscriptionname
```

Or, to change a subscription description: ```
oci announce announcement-subscription update --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --description "new subscription description"
```

Or, to change the subscription's preferred time zone by specifying the IANA Time Zone Database format:```
oci announce announcement-subscription update --preferred-time-zone "America/Los_Angeles"
```

Or, to change the subscription's Notifications topic: ```
oci announce announcement-subscription update --announcement-subscription-id ocid1.announcementsubscription.<realm>.<region>.<unique_ID> --ons-topic-id ocid1.onstopic.<realm>.<region>.<unique_ID>
```

For more information about Notifications topic options, see [UpdateSubscriptionDetails](https://docs.oracle.com/iaas/api/#/en/notification/latest/datatypes/UpdateSubscriptionDetails).
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/UpdateAnnouncementSubscription) operation to update an announcement subscription.


Was this article helpful?
YesNo

