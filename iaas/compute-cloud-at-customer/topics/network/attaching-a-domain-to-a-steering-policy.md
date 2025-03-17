Updated 2024-01-18
# Attaching a Domain to a Steering Policy
On Compute Cloud@Customer, a steering policy must be attached to a domain for the policy to answer DNS queries for that domain. The attachment is automatically placed into the same compartment as the domain's zone.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-a-domain-to-a-steering-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-a-domain-to-a-steering-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-a-domain-to-a-steering-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. At the top of the page, select the compartment that contains the steering policy.
    3. Click the name of the policy to which you want attach a domain.
    4. Under **Resources** , click **Attached Domains**.
    5. In the list of attached domains, click **Add Attached Domain**.
    6. In the Add Attached Domain dialog box, enter the domain name and select a zone.
    7. Click **Submit**.
The new domain is added to the **Attached Domains** list for this steering policy.
  * Use the [oci dns steering-policy-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy-attachment/create.html) command and required parameters to create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. 
Copy
```
oci dns steering-policy-attachment create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateSteeringPolicyAttachment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicyAttachment/CreateSteeringPolicyAttachment) operation to create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

