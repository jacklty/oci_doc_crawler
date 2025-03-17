Updated 2024-01-18
# Updating an Autoscaling Configuration
On Compute Cloud@Customer, you can change the display name of the autoscaling configuration, the tags, and whether the autoscaling configuration is enabled.
To add policies to an autoscaling configuration or update existing policies, see [Creating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-a-schedule-based-autoscaling-policy.htm#creating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can create schedule-based autoscaling policies.") and [Updating a Schedule-Based Autoscaling Policy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-a-schedule-based-autoscaling-policy.htm#updating-a-schedule-based-autoscaling-policy "On Compute Cloud@Customer, you can update a autoscaling policy display name, either the target pool size or the lifecycle action, and the execution schedule. You can also enable or disable the policy.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-autoscaling-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-autoscaling-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-autoscaling-configuration.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Autoscaling Configurations**.
    2. At the top of the page, select the compartment that contains the autoscaling configuration that you want to update.
    3. For the autoscaling configuration that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) and click **Edit**.
    4. In the **Update Autoscaling Configuration** dialog box, make the changes. Ignore the Cooldown Period value.
    5. Click **Submit**.
  * Use the [oci autoscaling configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/update.html) command and required parameters to update certain fields on the specified autoscaling configuration, such as the name, and whether the autoscaling configuration is enabled.
Copy
```
oci autoscaling configuration update --auto-scaling-configuration-id autoscalingConfiguration_OCID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * See the [ AutoScaling API Reference](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/) for API operations that enable you to dynamically scale compute resources to meet application requirements.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

