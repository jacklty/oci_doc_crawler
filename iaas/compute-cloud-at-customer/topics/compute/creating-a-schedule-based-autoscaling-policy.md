Updated 2024-01-18
# Creating a Schedule-Based Autoscaling Policy
On Compute Cloud@Customer, you can create schedule-based autoscaling policies.
An autoscaling policy is part of an autoscaling configuration. Each policy of a schedule-based autoscaling configuration has a schedule and either a target pool size or a lifecycle action.
The procedures in this section describe how to create policies separate from creating the autoscaling configuration.
## Designing Policies 🔗 
This section provides some tips for designing and troubleshooting policies.
Create two separate policies to scale a pool in and out or to change the state of the pool between stopped and running.
  * Scale example: One policy specifies a larger size for the pool at the beginning of a high demand period, and a second policy specifies a smaller pool size at the end of the high demand period.
  * State example: One policy stops all instances in the pool at the beginning of a regular compute node maintenance period, and a second policy starts the pool at the end of the maintenance period.


Design the policy schedule as follows:
  * Use `cron` expressions. Autoscaling uses a cron implementation similar to the [Quartz cron implementation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html). All fields require a value. If fields conflict, such as day of month and day of week, use a specific value for one and a question mark for the other.
  * Provide all schedule times in UTC.
  * Use an online `cron` expression generator such as [Quartz cron expression generator](https://www.freeformatter.com/cron-expression-generator-quartz.html) to verify your schedule expressions.
  * Ensure that policy schedules don't conflict. See the descriptions in [Multiple Schedule Management](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/multiple-schedule-management.htm#multiple-schedule-management "On Compute Cloud@Customer,") of which policies run when schedules conflict.


Take the following steps if a policy fails to run, or appears to fail to run:
  * Check that the autoscaling configuration and autoscaling policy are both enabled.
  * Check the schedule expression. Is the policy set to run when you meant for it to run? Remember, all expression times must be provided in UTC.
  * Was the policy set to start instances that were already running, or stop instances that were already stopped?
In addition to a policy conflict, a power action might have been performed on the pool separate from any autoscaling policy. That separate power action could prevent the policy action from succeeding. The policy power action is not retried.
  * Was the policy set to scale out, but not enough resources were available?
The scale policy sets the pool size, and the pool continues to try to reach that size as resources become available.
  * Is the operation specified by the policy still executing or waiting to run?
    * Check whether the pool is in the Scaling, Starting, Stopping, or Rebooting state, which indicates that the policy operation is still running.
    * If a state change operation tries to run while a state change operation is already running on the same pool, the second operation fails to run.
    * A limited number of pools can be changing state concurrently. If too many other pools are already changing state, then the pool must wait to begin changing state. The time to change state is longer when more instances are involved because instances are started, stopped, or rebooted serially.
    * A limited number of pools can be changing size concurrently. If other pools are already changing size, your pool might need to wait to begin scaling. The time to scale is longer when more instances are involved because instances are deleted or created serially. Delete and creating instances are both background operations and take some time to begin after the pool size has been updated by the policy.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click ****Compute**** , then click **Autoscaling Configurations**.
    2. At the top of the page, select the compartment that contains the configuration to which you want to add a policy.
    3. Click the name of the autoscaling configuration to which you want to add a policy.
    4. Under **Resources** , click **Autoscaling Policies** , then click **Create Scheduled Policy**. 
    5. In the **Create policy** dialog box, enter the following information:
       * **Name:** Enter a name for the new autoscaling policy.
       * **Action to perform:** Select Scale pool size or Change lifecycle state of all instances.
         * **Scale pool size:** Enter the number of instances that the pool scales to at the scheduled time.
         * **Change lifecycle state of all instances:** Select the state that all instances in the pool transition to at the scheduled time.
         * **Enable Schedule:** By default, the **Schedule Enabled** box is selected to enable the policy to run at the next scheduled time. Clear the box to disable this policy.
       * **Execution schedule:** Define the schedule for implementing this autoscaling policy. See [Designing Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy__policy-design).
    6. Click **Submit**.
  * Use the [oci autoscaling policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/policy/create.html) command and required parameters to create an autoscaling policy for the specified autoscaling configuration.
Copy
```
oci autoscaling policy create --auto-scaling-configuration-id autoscaling_configuration_OCID --from-json file://policy_definitions.json --policy-type scheduled [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the OCID of the autoscaling configuration where you want to add this autoscaling policy: `oci autoscaling configuration list`
    2. Construct a file that contains the policy definitions.
Use the following command to show the content and format of the file:
```
$ oci autoscaling policy create \
--generate-full-command-json-input > autoscalingPolicyCreate.json
```

**Note**
Don't specify values for `capacity` `min` or `max`. These properties don't apply to schedule-based autoscaling configurations.
The default values for `capacity` `min` and `max` appear in the created autoscaling policy but aren't used for schedule-based autoscaling.
The display name is 1-255 characters, doesn't need to be unique, and can be updated.
Use the references in [Creating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can create schedule-based autoscaling policies.") for help with setting the policy execution schedule. The `timezone` must be `UTC` and the `type` must be `cron`.
The policy is enabled by default.
The policy type must be `scheduled`.
The resource action type must be `power`, and the action must be one of `STOP`, `START`, `SOFTRESET`, `RESET`.
The following is an example autoscaling policy create input file:
```
{
 [
  {
   "capacity": {
    "initial": 10
   },
   "displayName": "size 10",
   "executionSchedule":
    {
     "expression": "0 0 10 ? 1 2#2 *",
     "timezone": "UTC",
     "type": "cron"
    },
   "isEnabled": true,
   "policyType": "scheduled"
  },
   "capacity": {
    "initial": 30
   },
   "displayName": "size 30",
   "executionSchedule":
    {
     "expression": "0 0 7 ? 11 5#1 *",
     "timezone": "UTC",
     "type": "cron"
    },
   "isEnabled": true,
   "policyType": "scheduled"
  },
  {
   "displayName": "stop policy",
   "executionSchedule":
    {
     "expression": "0 0 7 ? JAN,APR,JUL,OCT 4#3 *",
     "timezone": "UTC",
     "type": "cron"
    },
   "isEnabled": true,
   "policyType": "scheduled",
   "resourceAction": {
    "actionType": "power",
    "action": "STOP"
   }
  },
  {
   "displayName": "start policy",
   "executionSchedule":
    {
     "expression": "0 0 13 ? JAN,APR,JUL,OCT 4#3 *",
     "timezone": "UTC",
     "type": "cron"
    },
   "isEnabled": true,
   "policyType": "scheduled",
   "resourceAction": {
    "actionType": "power",
    "action": "START"
   }
  }
 ]
}
```

    3. Run the command to create new policies for the specified autoscaling configuration.
Example:
```
$ oci autoscaling policy create \
--auto-scaling-configuration-id ocid1.autoscalingConfiguration.**_unique_ID_** \
--from-json file://./salesPoolPolicies.json --policy-type scheduled
```

Use the `work-requests work-request get` command to check the status of the autoscaling policy create command.
  * See the [AutoScalingPolicy Reference](https://docs.oracle.com/iaas/api/#/en/autoscaling/20181001/AutoScalingPolicy) for API operations that define the criteria that trigger autoscaling actions and the actions to take.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

