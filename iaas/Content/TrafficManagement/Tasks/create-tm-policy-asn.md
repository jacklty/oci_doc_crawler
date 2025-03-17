Updated 2025-03-10
# Creating an ASN Steering Policy
Create an ASN traffic management steering policy that steers DNS traffic based on Autonomous System Numbers (ASN). 
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about ASN steering policies.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Under **List scope** , select the compartment in which you want to create the policy.
    3. Select **Create traffic management steering policy**.
    4. For **Policy type** , select **ASN steering**.
    5. Enter the following information:
       * **Policy name:** A unique name that identifies policy. Avoid entering confidential information. 
       * **Policy TTL:** The time to live for responses from the steering policy. If not specified, the system sets this value.
       * **Maximum answer count:** The maximum number of answers returned for the policy. For priority-based policies, the first valid answer is returned.
       * **Answer pool(s):** Answer pools contain the group of answers served in response to DNS queries.
         * **Answer pool name:** A user-friendly name for the answer pool, unique within the steering policy. Avoid entering confidential information.
         * **Name:** A unique name to identify the answer. Avoid entering confidential information.
         * **Type:** The record type provided as the answer.
         * **Rdata:** A valid domain name or IP address to add as an answer.
         * **Eligible:** Select the checkbox to indicate that the answer is available within the pool to be used in response to queries. Or, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Mark pool answers eligible** or **Mark pool answers ineligible**.
       * **ASN steering rules:** ASN steering rules specify the priority of answers that are served in a policy. If the primary answer is unavailable, traffic is steered to the next answer in the list. 
         * **ASN:** Enter an Autonomous System Number (ASN) used to distribute DNS traffic. 
         * **Pool Priority:** Select the priority in which the answers are served.
         * **Global catch-all:** Adding a global catch-all lets you specify answer pools for queries that don't match any of the specified rules that you have added. Select **Add global catch-all** and select the pool priorities.
       * **Attach health check:** Select an existing health check to be included as part of the policy, add a new one, or select **None**.
       * **Attach domain(s)** : The domain name and domain OCID that you want to attach to the policy. You can add more domains as needed.
    6. (Optional) Select **Show Advanced Options:** to apply tags to the policy. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    7. Select **Create policy**.
  * Use the [steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html) command and required parameters to create an ASN steering policy:
Command
CopyTry It
```
oci dns steering-policy create --compartment-id compartment_id --display-name policy_name
--template ROUTE_BY_ASN ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy) operation to create an ASN steering policy. Specify the `TemplateType` parameter as `ROUTE_BY_ASN`. 
See [Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm#api "Use the Oracle Cloud Infrastructure DNS REST API to build and configure Traffic Management policies.") for more information on using the API to create steering policies.


Was this article helpful?
YesNo

