Updated 2025-03-10
# Editing a Steering Policy
Edit information for a Traffic Management steering policy such as name, TTL, answers, health checks, and tags.
Domain attachments are added and published in a different workflow. See [Attaching a Domain to a Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm#top "Create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.") for more information. See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and general information.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Under **List scope** , select the compartment that contains the policy.
    3. Select the name of the policy in the list to open its details page.
    4. Select **Edit**.
    5. Update the policy information.
For descriptions of the fields, see [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") and select the task that pertains to the type of policy you're editing.
    6. Select **Save changes**.
    7. On the policy details page, edit, add, or delete tags as follows:
       * To edit or remove a tag, select the **Tags** tab, select the edit icon next to a tag, and change its value or remove it.
       * To add one or more tags, select **Add tags** and enter the tag namespace (for a defined tag), key, and value.
  * Use the [steering-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/update.html) command and required parameters to edit a steering policy:
Command
CopyTry It
```
oci dns steering-policy edit --steering-policy-id steering_policy_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/UpdateSteeringPolicy) operation to edit details about a steering policy.


Was this article helpful?
YesNo

