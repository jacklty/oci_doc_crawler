Updated 2024-01-18
# Deleting an Autoscaling Policy
On Compute Cloud@Customer, you can delete an autoscaling policy.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-a-autoscaling-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-a-autoscaling-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-a-autoscaling-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Autoscaling Configurations**.
    2. At the top of the page, select the compartment that contains the autoscaling configuration from which you want to delete a policy.
    3. Click the name of the autoscaling configuration for which you want to delete a policy.
    4. Under **Resources** , click **Autoscaling Policies**.
    5. For the policy that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) and then click **Delete**.
  * Use the [oci autoscaling policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/policy/delete.html) command and required parameters to delete an autoscaling policy for the specified autoscaling configuration.
Copy
```
oci autoscaling policy delete --auto-scaling-configuration-id <autoscaling_configuration_OCID> --auto-scaling-policy-id <autoscaling_policy_id> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * See the [AutoScalingPolicy Reference](https://docs.oracle.com/iaas/api/#/en/autoscaling/20181001/AutoScalingPolicy) for API operations that define the criteria that trigger autoscaling actions and the actions to take.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

