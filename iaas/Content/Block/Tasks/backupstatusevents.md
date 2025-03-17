Updated 2023-05-22
# Using Events to Notify When a Volume Backup Fails
You can use Oracle Cloud Infrastructure Events to track the status of Block Volume backup operations. See [Block Volume Backup Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__blockvolume_backup) for a list of these event types. Block Volume event types include a **status** attribute you can use to trigger actions based on the result of the backup operation. The **status** attribute value is either **operationFailed** or **operationSucceed**.
This topic describes how to create a rule in the Console that triggers an action when the backup operation fails for a volume.
**Note** You need to manually type the **operationFailed** and **operationSucceed** attribute values into the text box when creating a rule in the Console.
For more information about Events, see the following topics: 
  * [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm)
  * [Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm)
  * [Events and IAM Policies](https://docs.oracle.com/iaas/Content/Events/Concepts/eventspolicy.htm)
  * [Managing Rules for Events](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm)
  * [Block Volume Events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__block_volume)


## Prerequisites 🔗 
Before you can create a rule that triggers an action when a volume backup operation fails, you should ensure that you have the completed the prerequisites outlined in [Prerequisites for Creating Rules](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm#prereq).
You should also review the information in [Setting Up for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Setup), particularly:
  * Create IAM Policy for Events
  * Create Notifications Topic and Subscription


## Using the Console 🔗 
  1. Open the navigation menu and click **Observability & Management**. Under **Events Service** , click **Rules**. 
  2. Choose a **Compartment** you have permission to work in, and then click **Create Rule**.
Events compares the rules you create in this compartment to event messages emitted from resources in this compartment and any child compartments. 
  3. Enter the following. 
     * **Display Name:** Specify a friendly name for the rule. You can change this name later. Avoid entering confidential information.
     * **Description:** Specify a description of what the rule does. You can change this description later.
  4. In **Rule Conditions** , create a filter that triggers when a volume backup operation completes with **operationFailed** for the status attribute. 
**To add the volume backup create ends event type**
    1. Select **Event Type** from **Condition**. 
    2. Select **Service Name** from **Service Name**. 
    3. In **Event Type** , select **Create Volume Backup End**. 
**To add the status attribute**
    1. After adding an event type, click **+ Another Condition**.
    2. Select **Attribute** from **Condition**.
    3. Select **status** for **Attribute Name**. 
    4. Type **operationFailed** for **Attribute Values**. 
This filter matches **Create Volume Backup End** events where the **status** attribute is **operationFailed** , indicating that the backup operation did not complete successfully.
  5. In **Actions** , specify the actions resources to trigger when the filter finds a match. Select the action resource appropriate for what you configured for Events in [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm#backupstatusevents_topic-Prerequisites). For more information, see [Prerequisites for Creating Rules](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm#prereq) and [Setting Up for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Setup). 
**To select a topic**
    1. Select **Notifications**.
    2. Select the **Notifications Compartment**. 
    3. Select the **Topic**. 
    4. Click **+ Another Action** and select **Notifications** to add another topic. 
**To select a stream**
    1. Select **Streaming**.
    2. Select the **Stream Compartment**. 
    3. Select the **Stream**.
    4. Click **+ Another Action** and select **Streaming** to add another stream. 
**To select a function**
    1. Select **Functions**.
    2. Select the **Function Compartment**. 
    3. Select a **Function Application**. 
    4. Select the **Function**. 
    5. Click **+ Another Action** and select **Functions** to add another function. 
  6. Click **Create Rule**.


Was this article helpful?
YesNo

