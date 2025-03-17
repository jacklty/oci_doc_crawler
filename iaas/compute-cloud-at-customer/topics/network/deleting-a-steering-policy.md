Updated 2024-01-18
# Deleting a Steering Policy
On Compute Cloud@Customer, you can delete a steering policy that isn't attached to any zones.
To detach a policy from a zone, see [Deleting a Steering Policy Attachment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy-attachment.htm#deleting-a-steering-policy-attachment "On Compute Cloud@Customer, you can delete a steering policy attachment.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. At the top of the page, select the compartment that contains the steering policy.
    3. Click the name of the policy that you want to delete.
    4. Under **Resources** , click **Attached Domains** , and ensure that this policy has no attached domains.
To deleted attached domains, see [Deleting a Steering Policy Attachment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-steering-policy-attachment.htm#deleting-a-steering-policy-attachment "On Compute Cloud@Customer, you can delete a steering policy attachment.").
    5. At the top of the steering policy details page, click **Delete**.
    6. Confirm the deletion.
  * Use the [oci dns steering-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/delete.html) command and required parameters to delete the specified policy.
Copy
```
oci dns steering-policy delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/DeleteSteeringPolicy) operation to delete the specified policy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

