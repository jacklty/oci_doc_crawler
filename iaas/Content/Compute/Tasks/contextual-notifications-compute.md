Updated 2025-02-20
# Setting Up Contextual Notifications for an Instance
You can get messages when something happens with a compute instance. Use _contextual notifications_ in the Console to create event rules and alarms for an instance. Quick start templates are available.
This feature is available in the Console only.
## Before You Begin 🔗 
For administrators: To set up contextual notifications for an instance, use the following policy.
Copy
```
allow group ContextualNotificationsUsers to manage alarms in tenancy
allow group ContextualNotificationsUsers to read metrics in tenancy
allow group ContextualNotificationsUsers to manage ons-topics in tenancy
allow group ContextualNotificationsUsers to manage cloudevents-rules in tenancy
```

## Steps 🔗 
These steps show how to set up a contextual notification for an instance, for the first time.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Select the name of the instance that you're interested in.
  3. Select the **Notifications** tab.
When no notifications exist for the instance, the **Notifications** tab lists quick start templates. 
An example quick start template lets you set up notifications for high CPU usage.
  4. Select the quick start template that you want.
  5. In the **Create Notification** panel, scroll down to **Topics and Subscriptions**.
A new topic is automatically set up for you to add contact information to.
  6. **Contact Information** : Add at least one entry for where you want to receive messages.
     * Email: Enter an email address.
     * Slack: Enter a Slack endpoint.
Endpoint format:
Sends a message to the specified Slack channel by default when you publish a **message** to the subscription's parent **topic**. 
Message contents and appearance vary by message type. See [alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm), [event messages](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm), and [connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm).
Endpoint format (URL): 
```
https://hooks.slack.com/services/<webhook-token>
```

The <webhook-token> portion of the URL contains two slashes (/).
Query parameters aren't permitted in URLs.
To create an endpoint for a Slack subscription (using a webhook for the Slack channel), see [the Slack documentation](https://api.slack.com/incoming-webhooks#create_a_webhook).
     * SMS (for cell phone text messages): Enter a phone number.
  7. (Optional) Modify the default settings listed above **Topic and Subscriptions**.
For example, change the event type or alarm severity.
  8. Select **Create Notification**.
  9. Confirm the new subscriptions if needed.
For more information, see [Confirming a Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/confirm-subscription.htm).


Messages are sent to the contact information entries whenever the condition of the notification is satisfied.
Was this article helpful?
YesNo

