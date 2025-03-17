Updated 2024-01-18
# Editing a Steering Policy
On Compute Cloud@Customer, you can edit steering policies using the Compute Cloud@Customer Console, CLI, and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-steering-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-steering-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/editing-a-steering-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. For the policy that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click **Edit**.
    3. Make the necessary changes on the **Edit Steering Policy** dialog box.
    4. Click **Save Changes**.
The details page for this steering policy is displayed with the updated information.
  * Use the [oci dns steering-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/update.html) command and required parameters to update the configuration of the specified steering policy.
Copy
```
oci dns steering-policy update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/UpdateSteeringPolicy) operation to update the configuration of the specified steering policy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

