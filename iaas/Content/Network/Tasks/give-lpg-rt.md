Updated 2025-02-06
# Configuring VCN Route Tables to Use an LPG
Update a Virtual Cloud Network (VCN) route table to include a new rule that directs traffic destined for the other VCN's CIDR to flow through the local peering gateway (LPG). 
**Tip** Without the required routing, traffic doesn't flow between the peered LPGs. If a situation occurs in which you need to temporarily stop the peering, you can remove the route rules that enable traffic, you don't need to delete the LPGs.
Each administrator can perform this task before or after the connection is established. 
**Prerequisite:** Each administrator must have the CIDR block or specific subnets for the other VCN. If the connection is already established, look at the **Peer VCN CIDR Block** value for the LPG in the Console. Otherwise, get the information from the other administrator by email or other method.
Decide which subnets in the VCN need to communicate with the other VCN. You need to update the route table for each of those subnets to include a new rule that directs traffic destined for the other VCN's CIDR to the LPG.
**Note** Route tables with route rules that use an LPG as the next hop can be associated with subnets in the VCN, or a DRG, but not to internet gateways, NAT gateways or service gateways. For more about VCN routing, see [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN) or the [Learn routing in OCI Networking with examples (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/learn-routing-in-oci-networking-with-examples.pdf) technical brief.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the VCN that you're interested in. 
    3. Under **Resources** , select **Route Tables**. 
    4. Select the route table that you're interested in.
    5. Select **Add Route Rules** and enter the following values:
       * **Protocol Version:** Select IPv4 or IPv6.
       * **Target Type:** Local Peering Gateway.
       * **Destination CIDR Block:** The other VCN's CIDR block. If you want, you can specify a subnet or particular subset of the peered VCN's CIDR.
       * **Target Local Peering Gateway in <compartment>:** The compartment associated with the other LPG, if not the current compartment.
       * **Description:** An optional description of the rule.
    6. Select **Add Route Rules**.
Any subnet traffic with a destination that matches the rule is routed to the LPG. For general information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
If you no longer need the peering and want to delete the LPG, you must first delete all the route rules in the VCN that specify the LPG as the target.
  * Use the [network route-table update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/update.html) command and required parameters to update the specified route table's route rules:
Command
CopyTry It
```
oci network route-table update --rt-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) operation to update the specified route table's route rules.


Was this article helpful?
YesNo

