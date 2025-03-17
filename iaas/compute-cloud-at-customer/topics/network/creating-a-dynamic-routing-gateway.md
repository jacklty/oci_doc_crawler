Updated 2024-08-06
# Creating a Dynamic Routing Gateway
On Compute Cloud@Customer, a DRG is the equivalent of a general purpose router. A DRG is used to connect a VCN to the data center's IP address space. The router is configured separately from the VCNs, at the compartment level and is not required to be in the same compartment as the VCN (but it typically is).
After the DRG is configured, the DRG can be attached to more than one VCN and, similar to a physical router, can be attached and detached at any time, although perhaps with traffic loss. Also like a physical router, even when attached to a VCN, the DRG must have route table rules to steer traffic to the on-premises data center network's IP address space. 
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, under **Networking** , click **Dynamic Routing Gateway** s (DRGs).
    2. Click **Create Dynamic Routing Gateway**.
    3. Fill in the required information:
       * **Name:** Provide a name or description for the dynamic routing gateway. Avoid using any of the organization's confidential information.
       * **Create in Compartment:** Select the compartment in which to create the dynamic routing Gateway. 
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Dynamic Routing Gateway**.
The Dynamic Routing Gateway is now ready for the addition of DRG attachments. See [Attaching VCNs to a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm#attaching-vcns-to-a-dynamic-routing-gateway "On Compute Cloud@Customer, you can connect many VCNs to a DRG, but each VCN can have only one DRG attached. Ensure that the route tables and security lists allow communication.").
  * Use the [oci network drg create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/create.html) command and required parameters to create a dynamic routing gateway.
Copy
```
oci network drg create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/CreateDrg) operation to create a dynamic routing gateway.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

