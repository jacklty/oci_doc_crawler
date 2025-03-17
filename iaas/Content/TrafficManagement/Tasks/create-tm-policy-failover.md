Updated 2025-03-10
# Creating a Failover Policy
Create a failover traffic management policy to prioritize the order in which you want answers served in response to DNS queries.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about failover policies.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Under **List scope** , select the compartment in which you want to create the policy.
    3. Select **Create traffic management steering policy**.
    4. For **Policy type** , select **Failover**.
    5. Enter the following information:
       * **Policy name:** A unique name that identifies policy. Avoid entering confidential information.
       * **Policy TTL** : The time to live for responses from the policy. If not specified, the system sets this value.
       * **Maximum answer count** : The maximum number of answers returned for the policy. For priority-based policies, the first valid answer is returned.
       * **Answer pool(s):** Answer pools contain the group of answers that are served in response to DNS queries.
         * **Answer pool name:** : A user-friendly name for the answer pool, unique within the steering policy. Avoid entering confidential information.
         * **Name:** A unique name to identify the answer. Avoid entering confidential information.
         * **Type:** The record type to provide as the answer.
         * **Rdata:** A valid domain name or IP address to add as an answer.
         * **Weight:** A number between 0 and 255 used to decide how often an answer is served in relation to other answers. Answers with higher values are more likely to be served.
         * **Eligible:** Select the checkbox to indicate that the answer is available within the pool to be used in response to queries. Or, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Mark pool answers eligible** or **Mark pool answers ineligible**.
       * **Pool priority** : Failover priority rules specify the priority of answers that are served in a policy. If the primary answer is unavailable, traffic is steered to the next answer in the list.
         * **Pool:** : Select the priority in which the answers are served.
       * **Attach health check** : Select an existing health check to be included as part of the policy, add a new one, or select **None**.
       * **Attach domain(s)** : The domain name and domain OCID that you want to attach to the policy. You can add more domains as needed.
    6. (Optional) Select **Show Advanced Options:** to apply tags to the policy. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    7. Select **Create policy**.
  * Use the [steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html) command and required parameters to create a failover steering policy:
Command
CopyTry It
```
oci dns steering-policy create --compartment-id compartment_id --display-name policy_name
--template FAILOVER ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy) operation to create a failover steering policy. Specify the `TemplateType` parameter as `FAILOVER.`
See [Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm#api "Use the Oracle Cloud Infrastructure DNS REST API to build and configure Traffic Management policies.") for more information on using the API to create steering policies.


Was this article helpful?
YesNo

