Updated 2024-08-06
# Creating an IP Prefix Steering Policy
On Compute Cloud@Customer, an IP prefix steering policy dynamically routes DNS request traffic to different servers based on the originating IP prefix. 
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-an-ip-prefix-steering-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-an-ip-prefix-steering-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-an-ip-prefix-steering-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu click **DNS** , then click **Steering Policies**.
    2. Click **Create Steering Policy**.
    3. Select IP Prefix Steering and enter the following information:
       * **Name:** The name for the new steering policy.
       * **Policy TTL:** The Time To Live (TTL) for responses from the steering policy, in seconds. The maximum value is 604800 (equal to 168 hours or 7 days).
    4. In the Answers box, supply the following properties:
       * **Name:** The name for response to requests sent to the new steering policy.
       * **Type:** The type of request and response. The choices are A, AAA, or CNAME.
       * **RData:** The zone record data to return for the query. It must match the type expected by the type chosen.
       * **Pool:** Select the IP address pool to use of the policy from the drop-down list. 
       * **+Add Answer:** Click this box to add more answers to the requests received by the steering policy.
       * **Disabled:** This toggle determines if the IP prefix answer is enabled at creation or not. The default is enabled.
    5. In the IP Prefix Steering Rules box, supply the following properties: 
       * **+Add Rule:** Click this box to add rules to the IP prefix steering policy. 
       * **Order:** Use the directional arrows to order the rule in the sequence of configured rules.
       * **Subnet Address:** Enter the IP subnet prefix to apply to this steering policy.
       * You can add more rules to this steering policy by clicking **+Add Rule**.
    6. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Save Changes**. 
The IP prefix steering policy is created.
  * Use the [oci dns steering-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/create.html) command and required parameters to create a new steering policy in the specified compartment.
Copy
```
oci dns steering-policy create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy) operation to create a new steering policy in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

