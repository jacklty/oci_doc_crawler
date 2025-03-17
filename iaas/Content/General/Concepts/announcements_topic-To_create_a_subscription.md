Updated 2025-01-06
# Creating an Announcement Subscription
Create an announcement subscription to deliver specific announcements to a particular list of recipients.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm)


  *     1. Click the Announcements icon (![Announcements Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/announcements.png)), and then click **Subscriptions**.
    2. Under **List scope** , select **Compartment** , and then choose a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
    3. Click **Create announcement subscription**.
    4. Click **Name** , and then enter a name for the subscription. Avoid entering confidential information.
    5. (Optional) Click **Description** , and then enter a description. Avoid entering confidential information.
    6. Click **Compartment** , and then select the compartment where you want to create the subscription.
    7. Under **Subscription type** , do one of the following:
       * If you want the service to publish all announcements to the Notifications topic that you configure for this subscription, click **All announcements**. Then, skip to step 12 to configure the Notifications topic.
       * If you want the service to publish only the announcements that meet the filter criteria that you specify, click **Selected announcements only**. Then, continue to the next step to configure a filter group and its filters.
    8. If you selected **Selected announcements only** in the previous step, configure a filter group with the filters that you want to apply to announcements for this subscription. Under **Filter group** , click **Filter group name** , and then enter a name for the filter. Avoid entering confidential information.
**Note** Include only alphanumeric, hyphen, underscore, or whitespace characters in the filter group name.
    9. Under **Filters** , click **Type** , and then use the following table to configure a **Value** for what announcements you want to receive:
**Note** You can't have more than one of any particular filter type within a filter group.
Option | Description  
---|---  
**Announcement type** | Specify an announcement type to include in the filter. Every announcement is assigned to a category that helps you understand the relative severity of the information in the announcement. For more information, see [Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Types).  
**Compartment** | Specify a compartment to include in the filter. Not all announcements impact a specific compartment, but this filter lets you include announcements that do. **Note:** If you specify the root compartment, then subscribers receive all announcements for the tenancy. However, if you want all announcements, then we recommend you create a subscription for all announcements instead of creating a subscription for selected announcements only.  
**Platform** | Specify whether you want to see announcements that impact the Oracle Cloud Infrastructure (**IaaS**) platform or announcements that impact Software as a Service (**SaaS**) applications.  
**Region** | Specify a region to include in the filter.  
**Resource OCID** | Specify up to 5 resources that you want to include in the filter by doing the following:
       * Click **Browse** , select the check box next to the resource that you want to include, and then click **Add to filter**. (If needed, to list resources in a different compartment, click **Compartment** and choose a compartment.)
**Note:** You can't combine this filter with any other type of filter in a particular filter group.  
**Service** |  Select the name of the service that you want to include. To narrow the list, you can type or otherwise enter the service name. Not all announcements impact a particular service, but this filter lets you include announcements that do. If a filter specifies more than one service, then the Announcements service notifies subscribers of announcements impacting any of the specified services. **Note:** When you create a subscription based on a service, you get all the announcements for that service. You don't need to separately create a subscription for each region where you use the service.  
    10. (Optional) To add another filter to the filter group, click **+ Another filter** , and then repeat the previous step. (You can't do this if the filter you created in the previous step specified resource OCIDs. You can't combine that type of filter with any other filter in a particular filter group.)
    11. You can create more than one filter group to combine different filters to meet specific criteria. To add another filter group, click **+ Another filter group** , and then repeat steps 8 and 9. (You can't do this if any filters you create specify the service Oracle Fusion Applications. You can't have that filter and have more than one filter group.)
    12. Under **Display preferences** , click **Time zone** , and then choose the time zone that you prefer for announcement time stamps.
    13. If you created a filter that specified the service Oracle Fusion Applications, click **Language** , and then choose the language that you prefer for displaying announcements delivered by email. By default, the language is set to whatever you configured in the Console language selector.
**Note** You can't modify filter groups when a language display preference is part of a subscription. If you need changes to the filter groups later, you must create a new subscription at that time.
    14. Under **Notifications topic** , do one of the following:
       * To use an existing Notifications topic, click **Use existing topic** , and then choose a topic from the currently selected compartment. (If needed, to list resources in a different compartment, click **Compartment** and choose a compartment.)
       * To create a new Notifications topic, click **Create new topic** , and then provide the following:
Option | Description  
---|---  
**Compartment** | Select the compartment where you want to create the topic.  
**Name** | Enter a name for the topic. (Avoid entering confidential information.)  
**Description** | Enter a description for the topic. (Avoid entering confidential information.)  
**Subscription protocol** |  Choose the protocol used by subscription endpoints. The information you must provide about the subscription endpoint depends on the protocol. If you select **Email** , then click **Email address** and enter a valid email address. For more information, see [Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm). If you select **Function** , then specify the Oracle Cloud Infrastructure Functions application and function by selecting an **Oracle Functions application** and then **Function**. (If needed, click **Function compartment** to list resources in a different compartment.) For more information, see [Creating a Function Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-function.htm). If you select **HTTPS custom URL** , then click **URL** and enter a valid HTTPS URL. For more information, see [Creating an HTTPS (Custom URL) Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-https.htm). If you select **PagerDuty** , click **URL** and enter a valid PagerDuty URL. For more information, see [Creating a PagerDuty Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-pagerduty.htm). If you select **Slack** , click **URL** and enter the URL of a valid Slack channel. For more information, see [Creating a Slack Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm). If you select **SMS** , specify a **Country** and **Phone Number**. For more information, see [Creating an SMS Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm). Optionally, to add another subscription protocol to this topic, click **+ Another subscription**.  
    15. When you're ready, click **Create**.
  * Use the [oci announce announcement-subscription create](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/create.html) command and required parameters to create a subscription for announcements:
Command
CopyTry It
```
oci announce announcement-subscription create --compartment-id <compartment_OCID> --display-name <announcement_subscription_name> --ons-topic-id <Notifications_topic_OCID>
```

For example: ```
oci announce announcement-subscription create --compartment-id ocid1.compartment.<realm>..<unique_ID> --display-name newannouncementsubscription --ons-topic-id ocid1.onstopic.<realm>.<region>.<unique_ID>
```

**Note** You can't create a subscription with multiple filter groups when any filter group specifies Oracle Fusion Applications as the service.
For more information about filter group options, see [FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails). For more information about Notifications topic options, see [CreateSubscriptionDetails](https://docs.oracle.com/iaas/api/#/en/notification/latest/datatypes/CreateSubscriptionDetails).
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/CreateAnnouncementSubscription) operation to create a subscription for announcements.


Was this article helpful?
YesNo

