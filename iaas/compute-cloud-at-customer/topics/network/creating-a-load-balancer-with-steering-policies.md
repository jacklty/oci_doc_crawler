Updated 2024-08-06
# Creating a Load Balancer with Steering Policies
On Compute Cloud@Customer, if you have more than one DNS server, you can distribute traffic in a load balancing fashion, based on the weight you assign to each of them.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-load-balancer-with-steering-policies.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-load-balancer-with-steering-policies.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-load-balancer-with-steering-policies.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **Steering Policies**.
    2. Click **Create Steering Policy**.
    3. Select **Load Balancer** to create a load balancer steering policy.
    4. Enter the required information:
       * **Name:** Enter a name to display for the load balancer steering policy. Do not use confidential information.
       * **Policy TTL:** Enter a TTL in seconds for responses to steering policy requests. The maximum is 604800 seconds (equal to 168 hours or 7 days).
       * **Answers:** Supply the answer or answers to the DNS request for FILTER, WEIGHED, and LIMIT rules. You don't have to specify which condition the answers is for: that's all done by the load balancer template. 
         * **Name:** Enter a name for the RData returned, such as Server1.
         * **Type:** Choose the type of resource record to return for the request from the drop-down list. Choices are items such as A (IPv4 address) or CNAME (canonical name).
         * **RData:** Enter the resource record RData that is returned that corresponds to the Type selected. For example, for Type = A, the RData would be an IPv4 address.
         * **Weight:** Enter a weight for this policy to use for load balancing. Values up to 256 are supported. The default is 10. Higher weights mean that policy answer is used more often. For example, if `dns-server1` and `dns-server2` have equal weights, DNS requests are split evenly between them. If `dns-server1` has a weight twice that of `dns-server2`, then `dns-server1` is used twice as often as `dns-server2`.
    5. **Disabled:** The steering policy answer is enabled at creation by default. To disable this steering policy answer, click the toggle to change the Disabled value to TRUE. 
    6. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Save Changes**. 
The load balancing steering policy is created.
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

