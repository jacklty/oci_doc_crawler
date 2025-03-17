Updated 2024-01-18
# Deleting a Steering Policy Attachment
On Compute Cloud@Customer, you can delete a steering policy attachment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy-attachment.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. At the top of the page, select the compartment that contains the steering policy.
    3. Click the name of the policy for which you want to delete an attachment.
    4. Under **Resources** , click **Attached Domains**.
    5. For the attached domain that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Confirm the deletion.
The steering policy attachment is removed from the **Attached Domains** list.
  * Use the [oci dns steering-policy-attachment delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/delete.html) command and required parameters to delete the specified steering policy attachment. A _204_ response indicates that the delete has been successful.
Copy
```
oci dns steering-policy-attachment delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/DeleteSteeringPolicyAttachment) operation to delete the specified steering policy attachment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

