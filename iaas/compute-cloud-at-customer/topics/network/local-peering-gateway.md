Updated 2024-12-16
# Local Peering Gateways (LPGs)
On Compute Cloud@Customer, You can configure local peering gateways. VCN peering is the process of connecting multiple virtual cloud networks (VCNs) so that resources can communicate using private IP addresses.
You can use VCN peering to divide your network into multiple VCNs, for example, based on departments or lines of business, with each VCN having direct private access to the others. You can also place shared resources into a single VCN that all the other VCNs can access privately. Two peered VCNs can be in the same tenancy or different ones.
## Policies 🔗 
Peering between two VCNs requires explicit agreement from both parties in the form of IAM policies that each party implements for their own VCN compartment or tenancy. If the VCNs are in different tenancies, each administrator must provide their tenancy OCID and put in place special coordinated policy statements to enable the peering.
To implement the IAM policies required for peering, the two VCN administrators must designate one administrator as the requester and the other as the acceptor. The requester must be the one to initiate the request to connect the two LPGs. In turn, the acceptor must create a particular IAM policy that gives the requester permission to connect to LPGs in the acceptor's compartment. Without that policy, the requester’s request to connect fails. Either VCN administrator can delete a peering connection by deleting their LPG.
## Routing and Traffic Control 🔗 
As part of configuring the VCNs, each administrator must update the VCN routing to enable traffic to flow between the VCNs. In practice, this looks just like routing you set up for any gateway, such as an internet gateway or dynamic routing gateway. For each subnet that needs to communicate with the other VCN, you update the subnet route table. The route rule specifies the destination traffic's CIDR and your LPG as the target. Your LPG routes traffic that matches that rule to the other LPG, which in turn routes the traffic to the next hop in the other VCN.
You can control packet flow over the peering connection with route tables in your VCN. For example, you can restrict traffic to only specific subnets in the other VCN. Without deleting the peering, you can stop traffic flow to the other VCN by removing route rules that direct traffic from your VCN to the other VCN. You can also effectively stop the traffic by removing any security list rules that enable ingress or egress traffic with the other VCN. This does not stop traffic flowing over the peering connection, but stops it at the VNIC level.
## Security Rules 🔗 
Each VCN administrator must ensure that all outbound and inbound traffic with the other VCN is intended, expected and well-defined. In practice, this means implementing security list rules that explicitly state the types of traffic your VCN can send to the other and accept from the other. If your subnets use the default security list, there are two rules allowing SSH and ICMP ingress traffic from anywhere, thus also the other VCN. Evaluate these rules and whether you want to keep or update them.
In addition to security lists and firewalls, evaluate other OS-based configuration on the instances in your VCN. There could be default configurations that do not apply to your own VCN CIDR, but inadvertently apply to the other VCN CIDR.
## Connecting VCNs through a Local Peering Gateway 🔗 
On Compute Cloud@Customer, a Local Peering Gateway (LPG) is a way to connect VCNs so that elements in each VCN can communicate, even using private IP address.
The following components are required to set up a peering connection:
  * Two VCNs with nonoverlapping CIDRs
  * A local peering gateway (LPG) on each VCN in the peering relationship
  * A connection between the two LPGs
  * Route rules to enable traffic over the peering connection to and from the desired subnets in the respective VCNs
  * Security rules to control the types of traffic allowed to and from the instances in the subnets in question


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/local-peering-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/local-peering-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/local-peering-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, under **Networking** , click **Virtual Cloud Networks**. 
A list of previously configured VCNs in compartments is displayed. If the compartment you're creating the local peering gateway in isn't displayed, use the drop-down menu to select the correct compartment. 
    2. Click the name of the VCN. 
    3. Under the **Resources** menu, click **Local Peering Gateways**.
    4. Click **Create Local Peering Gateway**.
    5. Enter the required information:
       * **Name:** Enter a name. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment in which to create the local peering gateway.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    6. Click **Create Local Peering Gateway**.
The Local Peering Gateway is now ready for connecting VCNs with Establish Peering Connection, and ready for the addition of route rules or security settings.
  * Use the [oci network local-peering-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/create.html) command and required parameters to create a new local peering gateway (LPG) for the specified VCN.
Copy
```
oci network local-peering-gateway create --compartment-id <compartment_OCID> --vcn-id <vcn_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/CreateLocalPeeringGateway) operation create a new local peering gateway (LPG) for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

