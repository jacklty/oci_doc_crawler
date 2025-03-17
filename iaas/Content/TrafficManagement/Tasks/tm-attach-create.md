Updated 2025-03-10
# Attaching a Domain to a Policy
Create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies and domain attachments.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Select the name of the policy you want to create the domain attachment for.
**Tip** You can use search for a policy by name in the **Search** field. You can also use the **Time Created** sort filter to sort the policies chronologically in ascending or descending order.
    3. Under **Resources** , select **Attached domains**.
    4. Select **Add Attached Domain(s)**
    5. In the **Add Attached Domain(s)** panel, enter the domain and then select a compartment and zone.
    6. Select **Add**.
    7. Select **View changes** to review the attached domain information, and then select **Publish**.
    8. Select **Publish changes**.
  * Use the [steering-policy-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/create.html) command and required parameters to create a steering policy domain attachment:
Command
CopyTry It
```
oci dns steering-policy-attachment create --domain-name domain_name
 --steering-policy-id steering_policy_OCID --zone_id zone_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/CreateSteeringPolicyAttachment) operation to create a steering policy domain attachment. 
See [Traffic Management Steering Policies API Guide](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm#api "Use the Oracle Cloud Infrastructure DNS REST API to build and configure Traffic Management policies.") for more information on using the API to create steering policies.


Was this article helpful?
YesNo

