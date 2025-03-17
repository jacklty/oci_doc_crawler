Updated 2024-01-18
# Updating a Schedule-Based Autoscaling Policy
On Compute Cloud@Customer, you can update a autoscaling policy display name, either the target pool size or the lifecycle action, and the execution schedule. You can also enable or disable the policy.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-a-schedule-based-autoscaling-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-a-schedule-based-autoscaling-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-a-schedule-based-autoscaling-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click**Autoscaling Configurations**.
    2. At the top of the page, select the compartment that contains the configuration for which you want to update a policy.
    3. Click the name of the autoscaling configuration for which you want to update a policy.
    4. Under **Resources** , click **Autoscaling Policies**.
    5. For the policy that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) and then click **Edit**.
    6. In the **Update Policy** dialog box, change the policy information.
    7. Click **Submit**.
  * Use the [oci autoscaling policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/policy/update.html) command and required parameters to update an autoscaling policy in the specified autoscaling configuration.
Copy
```
oci autoscaling policy update --auto-scaling-configuration-id <autoscaling_config_OCID> --auto-scaling-policy-id <policy_OCID> --policy-type <policy_type> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * See the [AutoScalingPolicy Reference](https://docs.oracle.com/iaas/api/#/en/autoscaling/20181001/AutoScalingPolicy) for API operations that define the criteria that trigger autoscaling actions and the actions to take.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

