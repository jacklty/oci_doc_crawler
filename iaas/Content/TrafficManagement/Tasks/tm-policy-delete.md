Updated 2025-03-10
# Deleting a Steering Policy
Delete a Traffic Management steering policy.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Under **List scope** , select the compartment that contains the policy.
    3. Select the name of the policy in the list to open its details page.
    4. Select **Delete**.
The policy is staged for deletion, along with any associated domain attachments.
    5. Review the policy deletion information, and then select **Delete**.
    6. When the deletion is complete, select **Close**. 
  * Use the [steering-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/delete.html) command and required parameters to delete a steering policy:
Command
CopyTry It
```
oci dns steering-policy delete --steering-policy-id steering_policy_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/DeleteSteeringPolicy) operation to delete a steering policy.


Was this article helpful?
YesNo

