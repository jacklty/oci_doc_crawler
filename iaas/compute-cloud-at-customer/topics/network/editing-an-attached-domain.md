Updated 2024-01-18
# Editing an Attached Domain
On Compute Cloud@Customer, you can update a steering policy attachment with new information.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-an-attached-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-an-attached-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-an-attached-domain.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. At the top of the page, select the compartment that contains the steering policy.
    3. Click the name of the policy for which you want to edit an attached domain.
    4. Under **Resources** , click **Attached Domains**.
    5. Click the name of the attached domain that you want to edit.
    6. On the top of the details page for the attached domain, click **Edit**.
    7. Make the necessary changes on the **Edit Steering Policy Attachment** dialog box.
    8. Click **Save Changes**.
The details page for this steering policy attachment is displayed with the updated information.
  * Use the [oci dns steering-policy-attachment update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/update.html) command and required parameters to update the specified steering policy attachment with new information.
Copy
```
oci dns steering-policy-attachment update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/UpdateSteeringPolicyAttachment) operation to update the specified steering policy attachment with new information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

