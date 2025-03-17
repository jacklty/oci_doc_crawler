Updated 2025-03-10
# Listing Steering Policy Domain Attachments
View a list of steering policy domain attachments.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies and domain attachments.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Select a compartment from the list.
    3. Select the name of the policy you want to view domain attachments for.
**Tip** You can use search for a policy by name in the **Search** field. You can also use the **Time Created** sort filter to sort the policies chronologically in ascending or descending order.
    4. Under **Resources** , select **Attached domains**.
Domain attachments are listed in tabular form.
  * Use the [steering-policy-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/list.html) command and required parameters to view a list of steering policy domain attachments in a compartment.
Command
CopyTry It
```
oci dns steering-policy-attachment list --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListSteeringPolicyAttachments](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/ListSteeringPolicyAttachments) operation to view all steering policy domain attachments in a compartment.


Was this article helpful?
YesNo

