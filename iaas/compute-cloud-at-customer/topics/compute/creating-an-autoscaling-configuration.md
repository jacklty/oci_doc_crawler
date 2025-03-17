Updated 2024-08-06
# Creating an Autoscaling Configuration
On Compute Cloud@Customer, an autoscaling configuration contains policies that schedule adding or removing instances in a specified pool, or stopping, starting, or rebooting all the instances in the pool.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-autoscaling-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-autoscaling-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-autoscaling-configuration.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Autoscaling Configurations**.
    2. Click **Create Autoscaling Configuration**.
    3. In the **Create Autoscaling Configuration** dialog box, enter the following information:
       * **Name** : Enter a name for the autoscaling configuration.
       * **Create in Compartment** : Select the compartment where you want to create the autoscaling configuration.
       * **Instance Pool** : Select the instance pool that you want to scale with this autoscaling configuration.
       * **Autoscaling Policies** : For each policy, provide the following information:
         * **Action To Perform** : Select either Change Lifecycle State or Scale Pool Size.
         * **Policy Name** : Enter a name for the policy.
         * **Lifecycle Action** : If you selected Change Lifecycle State for Action To Perform, then select one of the following states to which to transition all instances of the pool when this policy is executed: Start, Stop, Soft Reset, Reset.
         * **Instance Pool Limit** : If you selected Scale Pool Size for Action To Perform, then enter a value for the pool size.
         * **Enable Schedule** : By default, the Schedule Enabled box is selected to enable the policy to execute at the next scheduled time. Clear the box to disable this policy.
         * **Policy Schedule** : Enter values for Minute, Hour, Day Of Month, Month, Day Of Week, and Year. Provide all schedule times in UTC. For more information, see [Creating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can create schedule-based autoscaling policies.").
To add another policy, click **Add Policy**. You can also add policies after the autoscaling configuration is created, as described in [Creating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can create schedule-based autoscaling policies.").
To delete a policy, click the trash can icon for that policy.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
       * Click **Submit**.
The details page for the new autoscaling configuration is displayed.
On the details page, ignore the Cooldown Period value. Cooldown period doesn't apply to schedule-based autoscaling configurations.
The new autoscaling configuration is enabled by default. To disable the configuration, see [Updating an Autoscaling Configuration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-autoscaling-configuration.htm#updating-an-autoscaling-configuration "On Compute Cloud@Customer, you can change the display name of the autoscaling configuration, the tags, and whether the autoscaling configuration is enabled.").
  * Use the [oci autoscaling configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/create.html) command and required parameters to create an autoscaling configuration.
Copy
```
oci autoscaling configuration create --compartment-id compartment_OCID --from-json file://input_file.json [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the following information:
       * The OCID of the compartment where you want to create this autoscaling configuration: `oci iam compartment list`
       * The OCID of the instance pool that will be managed by this autoscaling configuration: `oci compute-management instance-pool             list`
    2. Construct a file that contains all the input for the command.
Use the following command to show the content and format of the command input:
```
$ oci autoscaling configuration create \
--generate-full-command-json-input > autoscalingCfgCreate.json
```

The `resource` property is required and is the OCID of the instance pool that will be managed by this autoscaling configuration. The `type` of this resource must be `instancePool`.
At least one policy is required to create an autoscaling configuration. To add policies after the autoscaling configuration is created, see [Creating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can create schedule-based autoscaling policies.").
The optional display name is 1-255 characters, doesn't need to be unique, and can be updated. If you don't provide a value for `-displayName`, the default name of the autoscaling configuration is `autoscalingConfiguration**_YYYYMMDDhhmmss_**`, where`instanceconfiguration** _YYYYMMDDhhmmss_**`is the creation date and time.
The autoscaling configuration is enabled by default. To disable the configuration, set `isEnabled` to `false`.
**Note**
Don't specify values for `coolDownInSeconds` or `capacity` `min` or `max`. These properties do not apply to schedule-based autoscaling configurations.
The default values for `cool-down-in-seconds` and `capacity` `min` and `max` appear in the created autoscaling configuration but aren't used for schedule-based autoscaling.
The following is an example autoscaling configuration create input file with one policy:
```
{
 "compartmentId": "ocid1.compartment.**_unique_ID_**",
 "displayName": "salesPoolCfg",
 "policies":
   {
    "displayName": "reboot policy",
    "executionSchedule":
     {
      "expression": "0 0 2 ? * 1#1 *",
      "timezone": "UTC",
      "type": "cron"
     },
    "policyType": "scheduled",
    "resourceAction": {
     "actionType": "power",
     "action": "SOFTRESET"
    }
   },
 "resource":
  {
   "id": "ocid1.instancePool.**_unique_ID_**",
   "type": "instancePool"
  }
}
```

    3. Run the command to create the autoscaling configuration.
Syntax:
```
oci autoscaling configuration create --compartment-id **_compartment_OCID_** \
--from-json file://**_input_file_**.json
```

Example:
```
$ oci autoscaling configuration create --c ocid1.compartment.**_unique_ID_** \
--from-json file://./salesPoolCfg.json
{
 "data": {
  "compartment-id": "ocid1.compartment.**_unique_ID_**",
  "cool-down-in-seconds": 300,
  "defined-tags": {},
  "display-name": "salesPoolCfg",
  "freeform-tags": {},
  "id": "ocid1.autoScalingConfiguration.**_unique_ID_**",
  "is-enabled": true,
  "max-resource-count": null,
  "min-resource-count": null,
  "policies":
   {
    "capacity": null,
    "displayName": "reboot policy",
    "executionSchedule":
     {
      "expression": "0 0 2 ? * 1#1 *",
      "timezone": "UTC",
      "type": "cron"
     },
    },
    "id": "**_unique_ID_**",
    "is-enabled": true,
    "policy-type": "scheduled",
    "resourceAction": {
     "actionType": "power",
     "action": "SOFTRESET"
    },
    "time-created": "2023-01-25T21:28:56.131801+00:00"
   },
  "resource": {
   "id": "ocid1.instancePool.**_unique_ID_**",
   "type": "instancePool"
  },
  "time-created": "2023-01-25T21:28:56.140747+00:00"
 },
 "etag": "7c70532a-1d41-4861-a40f-bf840136a9c5"
}
```

Use the `work-requests work-request get` command to check the status of the autoscaling configuration creation.
  * Use the [AutoScalingConfiguration](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/) operation to create an autoscaling configuration.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

