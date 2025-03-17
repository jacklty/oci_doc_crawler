Updated 2024-05-14
# Creating Alarms
Create alarms and be notified when IP utilization of a subnet crosses a utilization threshold.. 
## Using the Console 🔗 
  1. Open the navigation menu and click **Networking**. Under **IP management** , click **IP Address Insights**.
  2. Under **Filters** , use each option to refine search. You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources.
  3. Expand the name of the VCN that contains the subnet.
  4. Click the name of the subnet to access the **Subnet Details** page.
  5. In the **Subnet Details** page, click **Alarms** tab.
The **Create Alarm** page opens.
  6. Enter a user-friendly name for the alarm. Avoid entering confidential information.
  7. For **Alarm severity** , select the perceived type of response required when the alarm is in the firing state.
  8. In the **Metric description** area, enter values to specify the metric to evaluate for the alarm.
     * **Metric name** : Select the name of the metric that you want to evaluate for the alarm. You can select any OCI metric or custom metric if the data exists in the selected compartment and metric namespace.
     * **Interval** : Select the aggregation window, or the frequency at which the alarm needs to be triggered.
     * **Statistic** : Select the function to use to trigger the alarm.
       * **Mean** - The value of Sum divided by Count during the specified time period.
       * **Rate** - The per-interval average rate of change.
       * **Sum** - All values added together.
       * **Max** - The highest value observed during the specified time period.
       * **Min** - The lowest value observed during the specified time period.
       * **Count** - The number of observations received in the specified time period.
       * **P50** - The value of the 50th percentile.
       * **P90** - The value of the 90th percentile.
       * **P95** - The value of the 95th percentile.
       * **P99** - The value of the 99th percentile.
  9. In the **Trigger rule** area, specify the condition that must be satisfied for the alarm to be in the firing state. The condition can specify a threshold, such as 90% for CPU utilization, or an absence.
     * **Operator** : Select the operator to use in the condition threshold.
     * **Value** : Enter the value to use for the condition threshold. For the **between** and **outside** operators, enter both values for the range.
     * **Trigger delay minutes** : Enter the number of minutes that the condition must be maintained before the alarm is in the firing state.
  10. In the **Topic and subscription** area, specify the type of communication channel preferred to receive the alarm notification. 
     * Choose **Create new topic** to create a new communication channel and subscription to receive alarm notofocations. **Select existing topic** to use an existing topic name and subscritption. 
     * Choose the compartment where the subnet resides.
     * Provide a **Topic name**.
     * In the **Subscription** area, choose a preferred type of communication channel to receive the alarm notification under **Subscription protocol** and provide the respective email addresses, phone numbers, or slack channels.
  11. Click **Create Alam**.
The created alarm is listed under the **Alarms** tab of the **Subnet Details** page.


Was this article helpful?
YesNo

