Updated 2025-02-13
# Autoscaling
Autoscaling lets you automatically adjust the number or the lifecycle state of compute instances in an instance pool. This helps you provide consistent performance for your end users during periods of high demand, and helps you reduce your costs during periods of low demand.
You can apply the following types of autoscaling to an instance pool:
  * **[Metric-based autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#threshold):** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.
  * **[Schedule-based autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#time):** Autoscaling events take place at the specific times that you schedule.


Autoscaling is supported for virtual machine (VM) and bare metal instance pools that use standard, dense I/O, and GPU [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).
## How Autoscaling Works: the Basics 🔗 
You use autoscaling configurations to automatically manage the size and lifecycle state of your instance pools. When autoscaling automatically provisions instances in an instance pool, the pool _scales out_. When autoscaling removes instances from the pool, the pool _scales in_. You can also use autoscaling to stop and start instances in an instance pool based on a schedule.
When an instance pool scales in, instances are terminated (deleted). Instances are terminated in this order: the number of instances is balanced across [availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm), and then balanced across [fault domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). Finally, within a fault domain, the oldest instance is terminated first.
An autoscaling configuration includes one or more autoscaling policies. These policies define the criteria that trigger autoscaling actions and the actions to take. Each autoscaling configuration can either have one metric-based autoscaling policy, or multiple schedule-based autoscaling policies. You can add a maximum of 50 schedule-based autoscaling policies to an autoscaling configuration.
Each instance pool can have only one autoscaling configuration.
## Metric-Based Autoscaling 🔗 
In metric-based autoscaling, you choose a performance metric to monitor, and set thresholds that the performance metric must reach to trigger an autoscaling event. When system usage meets a threshold, autoscaling dynamically resizes the instance pool in near-real time. As load increases, the pool scales out. As load decreases, the pool scales in.
**Tip** Avoid changing the value assigned to the initial number of instances after the pool has scaled. Lowering this value after the number of instances in the pool size has increased will cause instances in the pool to terminate. If you need to change this value, the new value should equal or exceed the number of instances currently in the pool.
Metric-based autoscaling relies on [performance metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics) that are collected by the [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm), such as CPU utilization. These performance metrics are aggregated into one-minute time periods and then averaged across all instances in the instance pool. When three consecutive values (that is, the average metrics for three consecutive minutes) meet the threshold, an autoscaling event is triggered.
A cooldown period between metric-based autoscaling events lets the system stabilize at the updated level. The cooldown period starts when the instance pool reaches the **Running** state. Autoscaling continues to evaluate performance metrics during the cooldown period. When the cooldown period ends, autoscaling adjusts the instance pool's size again if needed.
## Schedule-Based Autoscaling 🔗 
You can use schedule-based autoscaling to scale the pool size based on demand or to stop and start instances on a schedule.
Schedule-based autoscaling is ideal for instance pools where demand behaves predictably based on a schedule, such a month, date, or time of day. Schedules can be recurring or one-time. For example:
  * An instance pool has heavy use during business hours. The pool has lighter use on evenings and weekends. You can schedule the pool to scale out on weekday mornings, and to scale in on weekday evenings.
  * An instance pool has high demand on New Years Eve. You can schedule the pool to scale out every year on December 30, and to scale in on January 2.
  * You're releasing a new application that runs in the instance pool, and expect that many people will start using the application after the public announcement. In advance, you can schedule the instances in the pool to start on the day of release.


A schedule-based autoscaling configuration can have multiple autoscaling policies, each with a different schedule and target pool size or lifecycle action. To configure scale-in and scale-out events, you must create at least two separate policies. One policy defines the target pool size and schedule for scaling in, and the other policy defines the target pool size and schedule for scaling out. Likewise, if you want to schedule stop and start events, you must create at least two separate policies. One policy defines the lifecycle action and schedule for stopping the instances, and the other policy defines the lifecycle action and schedule for starting the instances.
After a schedule-based autoscaling policy is run, the instance pool stays at the target pool size or lifecycle state until something else changes the pool size or lifecycle state, such as a different autoscaling policy. However, if you manually change the pool size or lifecycle state, schedule-based autoscaling does not readjust the pool size or lifecycle state until the next scheduled autoscaling policy is run.
When you use schedule-based autoscaling to stop or reboot instances, the information on the instances is preserved. When the instances are started after a shutdown, they are returned to the state they were in before the shutdown occurred.
You define autoscaling schedules using cron expressions. Autoscaling uses the [Quartz cron implementation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html). You can use an online cron expression generator to verify your cron expressions; one example is [FREEFORMATTER](https://www.freeformatter.com/cron-expression-generator-quartz.html).
Provide all times in UTC.
**Note** Schedule-based autoscaling configurations include an attribute for cooldown period, which you see in the Console and when using the API, SDKs, and CLI. However, the cooldown period does not impact schedule-based autoscaling configurations.
### Multiple Schedule Management 🔗 
If multiple schedule-based autoscaling policies exist, the schedules might conflict. If a conflict occurs, Oracle chooses one lifecycle state policy and one autoscaling policy to run. The lifecycle state policy runs first.
For the lifecycle state policy, the policy with the highest priority action is chosen. The actions are prioritized as follows, listed from highest to lowest priority:
  * Force reboot
  * Reboot
  * Start
  * Force stop
  * Stop


For the autoscaling policy, the policy with the highest instance count is chosen.
To see how the autoscaling schedule is expected to affect the pool size in the future, [view the pool size forecast](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#poolsize-forecast).
### About Cron Expressions 🔗 
A [cron expression](https://en.wikipedia.org/wiki/Cron) is a string composed of six or seven fields that represent the different parts of a schedule, such as hours or days of the week. Cron expressions use this format:
`<second> <minute> <hour> <day of month> <month>         <day of week> <year>`
The following table lists the values and special characters that are allowed for each field.
Field | Allowed Values | Allowed Special Characters  
---|---|---  
Second |  0 **Note:** When using the API, CLI, or SDKs for autoscaling, you must specify 0 as the value for seconds, even though other values will create a valid cron expression. You don't need to provide any value for seconds when using the Console. | None  
Minute | 0-59 | * - , /  
Hour | 0-23 | * - , /  
Day of the month | 1-31 | * - , ? / L W  
Month | 1-12 or JAN-DEC | * - , /  
Day of the week | 1-7 or SUN-SAT | * - , ? / L #  
Year | 1970-2099 | * - , /  
The special characters are described in the following table.
Special Character | Description | Example  
---|---|---  
* |  Indicates all values for a field. |  * in the month field means every month.  
- | Indicates a range of values. | 8-17 in the hour field means hours 8 through 17, or 8 a.m. through 5 p.m.  
, | Indicates multiple values. | 3,5 in the day-of-the-week field means Tuesday and Thursday.  
? |  Indicates no specific values. When you want to specify a day of the month, use ? in the day-of-the-week field. When you want to specify a day of the week, use ? in the day-of-the-month field. | 0 0 10 ? * MON * means 10 a.m. on every Monday.  
/ | Use _n_ /_m_ to indicate increments. The value before the slash is the start time, and the number after the slash is the value to increment by. | 0/20 in the minute field means the minutes 0, 20, and 40.  
L |  Last day of the week or last day of the month. Use _x_ L in the day-of-the-week field to indicate the last _x_ day of the month. Use L-_n_ in the day-of-the-month field to indicate an offset of _n_ days from the last day of the month. Do not L use with multiple values or a range of values. |  L in the day-of-the-month field means January 31, February 28 in non-leap years, and so on. 6L in the day-of-the-week field means the last Friday of the month. L-5 means 5 days before the last day of the month.  
W |  The weekday (Monday - Friday) that is nearest to the given day. The value does not cross months. You can combine the L and W characters (LW) in the day-of-month field to indicate last weekday of the month. Do not use W with multiple values or a range of values. | 10W means the nearest weekday to the 10th of the month. If the 10th is a Saturday, it means Friday the 9th. If the 10th is a Sunday, it means Monday the 11th. If the 10th is a Wednesday, it means Wednesday the 10th.  
# | Use _x_ #_n_ to indicate the _n_ th _x_ day of the month. | 5#2 means the second Thursday of the month.  
#### Example Cron Expressions
Use these example cron expressions as a starting point to create your own autoscaling schedules. Combine each cron expression with a target pool size to create an autoscaling policy. Then, include one or more autoscaling policies in an autoscaling configuration.
**Goal:** A one-time schedule with only one scaling event. At 11:00 p.m. on December 31, 2020, scale an instance pool to 100 instances. You'll need one autoscaling policy.
  * Policy 1:
    * **Target pool size:** 100 instances
    * **Execution time:** 11:00 p.m. on the 31st day of December, in 2020
    * **Cron expression:** 0 0 23 31 12 ? 2020


**Goal:** A one-time schedule with a scale-out event and a scale-in event. At 10:00 a.m. on March 1, 2021, scale out to 75 instances. At 4 p.m. on March 7, 2021, scale in to 30 instances. You'll need two autoscaling policies.
  * Policy 1 - scale out:
    * **Target pool size:** 75 instances
    * **Execution time:** 10:00 a.m. on the 1st day of March, in 2021
    * **Cron expression:** 0 0 10 1 3 ? 2021


  * Policy 2 - scale in:
    * **Target pool size:** 30 instances
    * **Execution time:** 4:00 p.m. on the 7th day of March, in 2021
    * **Cron expression:** 0 0 16 7 3 ? 2021


**Goal:** A recurring daily schedule. On weekday mornings at 8:30 a.m., scale out to 10 instances. On weekday evenings at 6 p.m., scale in to two instances. You'll need two autoscaling policies.
  * Policy 1 - morning scale out:
    * **Target pool size:** 10 instances
    * **Execution time:** 8:30 a.m. on every Monday through Friday, in every month, in every year
    * **Cron expression:** 0 30 8 ? * MON-FRI *
  * Policy 2 - evening scale in:
    * **Target pool size:** 2 instances
    * **Execution time:** 6:00 p.m. on every Monday through Friday, in every month, in every year
    * **Cron expression:** 0 0 18 ? * MON-FRI *


**Goal:** A recurring weekly schedule. On Tuesdays and Thursdays, scale the pool to 30 instances. On all other days of the week, scale the pool to 20 instances. You'll need two autoscaling policies.
  * Policy 1 - Tuesday and Thursday:
    * **Target pool size:** 30 instances
    * **Execution time:** 1 a.m. on every Tuesday and Thursday, in every month, in every year
    * **Cron expression:** 0 0 1 ? * TUE,THU *
  * Policy 2 - all other days:
    * **Target pool size:** 20 instances
    * **Execution time:** 1 a.m. on Sunday through Monday, Wednesday, and Friday though Saturday, in every month, in every year
    * **Cron expression:** 0 0 1 ? * SUN-MON,WED,FRI-SAT *


**Goal:** A recurring monthly schedule. On all days of the month, set the pool size to 20 instances. On the 15th day of the month, scale out to 40 instances. You'll need two autoscaling policies.
  * Policy 1 - daily pool size:
    * **Target pool size:** 20 instances
    * **Execution time:** Midnight on every day, in every month, in every year
    * **Cron expression:** 0 0 0 * * ? *
  * Policy 2 - scale out:
    * **Target pool size:** 40 instances
    * **Execution time:** 12:05 a.m. on the 15th day of the month, in every month, in every year
    * **Cron expression:** 0 5 0 15 * ? *


## Tracking Autoscaling Events 🔗 
You can use the Events service to monitor autoscaling actions. For example, an event is emitted when a scaling action occurs. For details about autoscaling event types and an example event, see [Autoscaling Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#computeevents__autoscaling).
For steps to create event notifications, see [Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).
As an example, to create an event notification for a scaling action, when you [create the event rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm), do the following:
  1. For **Condition** , select **Event Type**.
  2. For **Service Name** , select **Compute**.
  3. For **Event Type** , select **Autoscaling Configuration - Scaling Action**.


To filter notifications to scaling action errors: 
  1. Click **+ Another Condition** to create an additional condition.
  2. For **Condition** , select **Attribute**.
  3. For **Attribute Name** , select **actionType**.
  4. For **Attribute Values** , enter **ERROR**.


The possible attribute values for actionType are:
  * SCALE_OUT
  * SCALE_IN
  * NO_ACTION
  * ERROR
  * LIMIT_EXCEEDED
  * POWER_ACTION


You can also use the [audit logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm) to track autoscaling actions. If errors occur during autoscaling events, you can find error details in the these logs, and you can use the audit logs to [explore the details of autoscaling events](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm#audit_logs__export-audit).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For a typical policy that gives access to autoscaling configurations, see [Let users manage Compute autoscaling configurations](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#autoscaling).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Before You Begin 🔗 
  * You have an [instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm#Creating_an_Instance_Pool). Optionally, you can attach a load balancer or network load balancer to the instance pool.
  * For metric-based autoscaling, [monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) on the instances in the instance pool, and the [Monitoring service is receiving metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#FindOutIfEnabled) that are emitted by the instance. When you initially create an instance pool using instances that support monitoring, [monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) by default, regardless of the settings in the pool's instance configuration.
  * You have sufficient [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) to create the maximum number of instances that you want to scale to.


## Using the Console 🔗 
[To create a metric-based autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click **Create autoscaling configuration**.
  3. On the **Add basic details** page, do the following:
    1. Enter a name for the autoscaling configuration. Avoid entering confidential information.
    2. Select the compartment to create the autoscaling configuration in.
    3. Select the **Instance pool** to apply the autoscaling configuration to.
    4. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Click **Next**.
  4. On the **Configure autoscaling policy** page, select **Metric-based autoscaling**. Then, do the following:
    1. Enter a name for the autoscaling policy. Avoid entering confidential information.
    2. In the **Cooldown in seconds** box, enter the minimum amount of time to wait between scaling events. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default.
    3. Select the **Performance metric** that triggers an increase or decrease in the number of instances in the instance pool.
    4. In the **Scale-out rule** area, specify the threshold that the performance metric must reach to increase the pool size. Select a **Scale-out operator** and **Threshold percentage**. Then, enter the **Number of instances to add** to the pool.
For example, when CPU utilization is greater than 90%, add 10 instances to the pool.
    5. In the **Scale-in rule** area, specify the threshold that the performance metric must reach to decrease the pool size. Select a **Scale-in operator** and **Threshold percentage**. Then, enter the **Number of instances to remove** from the pool.
For example, when CPU utilization is less than 20%, remove 5 instances from the pool.
    6. In the **Scaling limits** area, specify the number of instances in the instance pool:
       * **Minimum number of instances:** The minimum number of instances that the pool is allowed to decrease to.
       * **Maximum number of instances:** The maximum number of instances that the pool is allowed to increase to.
**Important** The number of instances that can be provisioned is also limited by your tenancy's [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
       * **Initial number of instances:** The number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the scaling limits that you set.
    7. Click **Next**.
  5. Review the autoscaling configuration, and then click **Create**.
Autoscaling runs. The cooldown period starts when the instance pool's state changes from **Scaling** to **Running**.


[To create a schedule-based autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click **Create autoscaling configuration**.
  3. On the **Add basic details** page, do the following:
    1. Enter a name for the autoscaling configuration. Avoid entering confidential information.
    2. Select the compartment to create the autoscaling configuration in.
    3. Select the **Instance pool** to apply the autoscaling configuration to.
    4. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Click **Next**.
  4. On the **Configure autoscaling policy** page, select **Schedule-based autoscaling**. Then, do the following:
    1. Enter a name for the autoscaling policy. Avoid entering confidential information.
    2. For **Action to perform** , select **Scale pool size** or **Change lifecycle state of all instances**.
       * If you select **Scale pool size** , in the **Target pool size** box, enter the number of instances that the pool should scale to at the scheduled time.
**Important** The number of instances that can be provisioned is also limited by your tenancy's [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
       * If you select **Change lifecycle state of all instances** , in the **Lifecycle action** menu, select the action to run on the instance pool.
    3. In the **Execution schedule** area, define the schedule for implementing this autoscaling policy in UTC. Use a Quartz cron expression. For more information about cron expressions, see [About Cron Expressions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#cron).
    4. To schedule more scaling events, click **+ Another Policy** and then repeat the previous steps.
    5. Click **Next**.
  5. Review the autoscaling configuration, and then click **Create**.
Autoscaling runs at the scheduled time.


[To edit an autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
You can change these characteristics of an autoscaling configuration:
  * Name
  * For metric-based autoscaling, the cooldown period between autoscaling actions


  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. Click **Edit**.
  4. Make your updates. Avoid entering confidential information.
  5. Click **Save changes**.


[To edit an autoscaling policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
You can change these characteristics of an autoscaling policy:
  * Name
  * For metric-based autoscaling:
    * Which performance metric triggers an autoscaling action
    * The minimum and maximum number of instances
    * The initial number of instances that the pool should have immediately after you update the autoscaling policy
**Caution** If you specify a smaller initial number of instances than the current pool size, instances will be terminated.
    * Scale-out and scale-in operators and thresholds
    * The number of instances to add or remove
  * For schedule-based autoscaling, you can edit the target pool size, lifecycle action, or schedule for an existing policy, delete an existing policy, or add a new policy


  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. In the **Autoscaling Policies** area, click **Edit**.
  4. Make your updates. Avoid entering confidential information.
  5. Click **Save changes**.


[To view the pool size forecast](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
To see how the autoscaling schedule is expected to affect the pool size in the future, view the pool size forecast.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. Under **Resources** , click **Pool size forecast**.
  4. Optionally, customize the forecast.
     * By default, the forecast shows active schedule-based policies. To see all schedule-based policies, under **Policy** , select **All schedule-based policies**.
     * For **Time zone** , select UTC time or local time.
     * To change the date range displayed in the forecast, click **Start date** or **End date** , and use the calendar picker to select new dates.


[To enable or disable a schedule-based autoscaling policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. In the **Autoscaling policies** area, under **Status** , toggle the **Enabled** or **Disabled** switch.


[To disable an autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. Click **Disable** , and then confirm when prompted.


[To delete an autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
When you delete an autoscaling configuration, the instance pool remains in its most recent state.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. Click **Delete** , and then confirm when prompted.


[To manage tags for an autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. Click the autoscaling configuration that you're interested in.
  3. Click the **Tags** tab to view or edit the existing tags. Or click **Add Tags** to add new ones.


For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [Autoscaling API](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/) to manage autoscaling configurations and policies.
To update the autoscaling configuration with a new instance pool, create a new instance configuration and then point the instance pool to the new configuration:
  * First, create a new instance configuration with the desired settings. You can do this using the Console. For steps, see [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration). To do this using the API, use the [CreateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/CreateInstanceConfiguration) operation.
  * Next, update the instance pool used in the autoscaling configuration to point to the new instance configuration. To do this using the API, use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to change the instanceConfigurationId. You cannot use the Console to update the instance configuration used by the instance pool.


Was this article helpful?
YesNo

