Updated 2024-03-19
# Example of Creating an Alarm on Compute Cloud@Customer
On Compute Cloud@Customer, you can create alarms to notify you when Compute Cloud@Customer infrastructure metrics meet specified triggers. 
This example shows how to create a basic alarm that's based on Compute Cloud@Customer metrics. This example creates a critical alarm when the total storage utilization on the Compute Cloud@Customer infrastructure crosses the specified threshold. The alarm is configured to email the administrators if an alarm is triggered.
For information about managing alarms, see [Managing Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm).
For detailed descriptions about each alarm option, see [Creating a Basic Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm). 
To see the Compute Cloud@Customer infrastructure metrics you can use to create alarms, see [Compute Cloud@Customer Metrics Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/metrics-reference.htm#metrics-reference "See a list of metrics emitted by Compute Cloud@Customer using the oci_ccc metric namespace.").
Example values are shown in parenthesis like this: (**`value`**)
  1. In the Oracle Cloud Console, open the navigation menu and click **Observability & Management**.
  2. Under **Monitoring** , click **Alarm Definitions**. 
  3. Click **Create Alarm**.
  4. Enter the following information:
     * **Define alarm** : 
       * **Alarm name:** Enter a descriptive name. Avoid entering confidential information. (**`Storage space alarm`**)
       * **Alarm severity:** Select the alarm level. (**`Critical`**)
       * **Alarm body:** Enter the notification content. (`**Low                     storage space in your Compute Cloud@Customer instance. See                     action plan instructions at                     https://example.us.runbook-lowstorage.**`)
     * **Tags** : No tags are applied for this example.
     * **Metric description** :
       * **Compartment:** Select the name of the compartment where the Compute Cloud@Customer infrastructure was created. The selected compartment also becomes the compartment for the alarm that create. (**`ccc-compartment`**)
       * **Metric namespace:** Select the metric namespace. For alarms that are based on Compute Cloud@Customer metrics, the namespace is `oci_ccc`. See [Compute Cloud@Customer Metrics Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/metrics-reference.htm#metrics-reference "See a list of metrics emitted by Compute Cloud@Customer using the oci_ccc metric namespace.") (**`oci_ccc`**)
       * **Resource group:** No resource group is selected for this example.
       * **Metric name:** Select the metric name. The drop-down menu gives you the choice to select any valid Compute Cloud@Customer metric name. (**`StorageSpaceAvailable`**)
       * **Interval:** Select the interval to check this metric. The interval should be longer than the collection frequency. See [Compute Cloud@Customer Metrics Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/metrics/metrics-reference.htm#metrics-reference "See a list of metrics emitted by Compute Cloud@Customer using the oci_ccc metric namespace."). (**`1 hour`**)
       * **Statistic:** Select the statistic type. This example uses min, but you can select other values. See [Selecting the Statistic for an Alarm Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-statistic.htm#top). (**`min`**)
     * **Metric dimensions:**
       * **Dimension name:** Select a dimension. For this example, the alarm dimension is set to `ressourceid` which requires you to specify the resource ID in the next field. (**`resourceid`**)
       * **Dimension value:** From the drop-down menu, select the ID of the Compute Cloud@Customer infrastructure. (**`uniqueID`**)
     * **Trigger rule** : 
       * **Operator** : Select the operator used in the condition threshold. Less than is selected in this example to trigger when `StorageSpaceAvailable` drops below the specified value. (**`less                         than`**)
       * **Value** : Select the value to use for the condition threshold. The field automatically displays the unit such as GB. (**`10000`**)
       * **Trigger delay minutes** : Select the number of minutes that the condition must be maintained before the alarm is in the firing state. (**`75`**)
     * **Define alarm notifications:**
       * **Destination service:** Select Notifications to send alarm notifications to a topic. (**`Notifications`**)
       * **Compartment:** Select a compartment that you want to store the new topic in. This compartment can be a different compartment than the one specified for the alarm and metric. By default, the first accessible compartment is selected. (**`my-compartment`**)
       * **Topic:****Click Create a topic** , and fill in these fields:
         * **Topic Name:** Enter a descriptive name. Avoid entering confidential information. (**`notify_administrators`**)
         * **Topic description:** Enter a topic description. (**`Email alarm                          notifications to the administrators when storage                          space is low.`**)
         * **Subscription protocol:** Select a protocol. (**`Email`**)
         * **Subscription Email:** Enter the email address. (`**admins@example.com**`)
     * **Message grouping:** Select `Group notifications across metric                 streams` to collectively track metric status across all metric streams. Send a message when metric status across all metric streams changes. If you're monitoring many resources, this selection is less likely to flood the subscription protocol. (`**Group                   notifications across metric streams**`)
     * **Message Format:** Select an option for the appearance of messages that you receive. (`**Send formatted messages**`)
     * Don't select **Repeat notification** or **Suppress notifications**.
  5. Ensure that **Enable this alarm** is selected.
  6. Click **Save alarm**.


**More alarm resources:**
  * [Monitoring Overview](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)
  * [Viewing an Alarm Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-chart.htm)
  * [Best Practices for Your Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/alarmsbestpractices.htm)


Was this article helpful?
YesNo

