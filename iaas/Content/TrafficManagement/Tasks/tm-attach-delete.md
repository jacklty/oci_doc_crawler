Updated 2025-03-10
# Deleting a Domain Attachment
Delete a domain attachment to a Traffic Management steering policy.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies and domain attachments.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Select a compartment from the list.
    3. Select the name of the policy you want to view domain attachments for.
**Tip** You can use search for a policy by name in the **Search** field. You can also use the **Time Created** sort filter to sort the policies chronologically in ascending or descending order.
    4. Under **Resources** , select **Attached domains**.
Domain attachments are listed in tabular form.
    5. Select the domain attachment in the list you want to delete, and then select **Delete** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)).
The domain attachment is staged for deletion.
    6. Select **View changes** to review the attached domain deletion information, and then select **Publish**.
    7. Select **Publish changes**.
  * Use the [steering-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/delete.html) command and required parameters to delete a steering policy attachment.
Command
CopyTry It
```
oci dns steering-policy-attachment delete --steering-policy-attachment-id steering_policy_attachment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/DeleteSteeringPolicyAttachment) operation to delete a steering policy domain attachment.


Was this article helpful?
YesNo

