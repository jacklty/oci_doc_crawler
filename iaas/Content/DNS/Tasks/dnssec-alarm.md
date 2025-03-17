Updated 2025-03-10
# Creating a DNSSEC KSK Rollover Alarm
Create an alarm on a DNSSEC enabled zone that lets you know when the zone's key-signing key (KSK) needs to be rolled over.
See [DNS Metrics](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/dnsmetrics.htm#dns_metrics "Learn about the metrics emitted by the metric namespace oci_dns \(the DNS service\).") for more information.
## Using the Console 🔗 
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Alarm Definitions**. 
  2. Select **Create Alarm**. 
  3. Enter a user friendly name for the alarm. For example, "DNSSEC KeyVersion Requires Promotion." Avoid entering confidential information.
  4. For **Severity** , select Critical.
  5. For **Alarm body** , enter the human-readable content of the notification for this condition (trigger rule). For example, "One or more DNSSEC enabled zones has a KSK version that requires promotion. [Follow these instructions](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm#enter-topic-id "DNSSEC key-signing keys \(KSKs\) require annual rollover and key promotion.") to promote KSKs, maintain a strong security posture, and avoid disruptions.
  6. In the **Metric description** area, enter values to specify the metric to evaluate for the alarm.
     * **Compartment** : Select the **compartment** that contains the resources that emit the metrics evaluated by the alarm. The selected compartment is also the storage location of the alarm. By default, the first accessible compartment is selected.
     * **Metric namespace** : `oci_dns`.
     * **Metric name** : `DaysUntilDnssecKeyVersionExpiration`
     * **Interval** : `5 minutes.`
     * **Statistic** : `Count`.
  7. In the **Metric dimensions** area, specify the following filters:
     * **Dimension name** : `requiresPromotion`.
     * **Dimension value** : `true`.
  8. In the **Destination** area under **Define alarm notifications** , select the provider of the destination to use for alarm notifications.
     * **Destination service** : Select one of the following values:
       * **Notifications** : Send alarm notifications to a [topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition). Each [subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition) in the topic receives an [alarm message](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm).
       * **Streaming** : Send [alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm) to a [stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts).
**Note** If you expect more than 60 messages per minute, select **Streaming**. For more information, see [Alarm Message Limits](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits-alarm-messages).
     * **Compartment** : Select the **compartment** that contains the resources that emit the metrics evaluated by the alarm. The selected compartment is also the storage location of the alarm. By default, the first accessible compartment is selected.
     * **Stream** (for **Streaming** only): The [stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#howstreamingworks) to use for alarm notifications.
     * **Topic** (for **Notifications** only): The [topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition) to use for notifications. Each topic supports one or more [subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition) protocols, such as PagerDuty.
     * To create a new topic (and a new subscription) in the selected compartment, select **Create a topic** and then enter the following values:
       * **Topic name** : A user-friendly name for the topic. For example, enter: "Operations Team" for a topic used to notify operations staff of firing alarms. Avoid entering confidential information.
       * **Topic description** : Description of the new topic.
       * **Subscription protocol** : Medium of communication to use for the new topic. Select the type of subscription that you want to create, then enter values in the associated fields. For details about each subscription type, select the links.
         * [**Email**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm): Enter an email address.
         * [**Function**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-function.htm): Select the compartment and application that contain the function that you want, and then select the function.
         * [**HTTPS (Custom URL)**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-https.htm): Enter the URL that you want to use as the endpoint.
         * [**PagerDuty**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-pagerduty.htm): Enter the _integration key_ portion of the URL for the PagerDuty subscription. (The other portions of the URL are hard-coded.)
         * [**Slack**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm): Enter the Slack endpoint, including the webhook token.
         * [**SMS**](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm): Select the country for the phone number, and then enter the phone number, using [E.164 format](https://www.itu.int/rec/T-REC-E.164/en). Example: `+14255550100`
  9. For **Message grouping** , select **Split notifications per metric stream** : Individually track metric status by metric stream. Send a message when metric status for each metric stream changes. For an example, see [Scenario: Split Messages by Metric Stream](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/split-messages.htm).
  10. For **Message Format** , select an option for the appearance of messages that you receive from this alarm (for **Notifications** only).
     * **Send formatted messages** : Simplified, user-friendly layout. To view supported subscription protocols and message types for formatted messages (options other than **Raw**), see [Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
     * **Send Pretty JSON messages (raw text with line breaks)** : JSON with new lines and indents.
     * **Send raw messages** : Raw JSON blob.
  11. Select **Save alarm**.


Was this article helpful?
YesNo

