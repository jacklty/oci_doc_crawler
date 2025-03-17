Updated 2025-03-10
# Viewing a Steering Policy's Details
View details about a Traffic Management steering policy.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Under **List scope** , select the compartment that contains the policy.
    3. Select the name of the policy in the list to open its details page.
The policy details page contains information about the policy, both general information and links to its resources. Some items in the page are read-only, and other items are editable. See [Editing a Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm#top "Edit information for a Traffic Management steering policy such as name, TTL, answers, health checks, and tags.").
  * Use the [steering-policy get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/get.html) command and required parameters to view details about a steering policy in a compartment.
Command
CopyTry It
```
oci dns steering-policy get --steering-policy-id steering_policy_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/GetSteeringPolicy) operation to view details about a steering policy.


Was this article helpful?
YesNo

