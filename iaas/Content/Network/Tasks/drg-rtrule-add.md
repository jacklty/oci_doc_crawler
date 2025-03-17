Updated 2025-01-17
# Adding Static Route Rules to a DRG Route Table
Add one or more static route rules to a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.
A DRG route rule is a mapping between a destination IP address range (CIDR block) and a DRG attachment. The map is used to route packets that match the rule or rules. Traffic can be routed across the attachments using equal-cost multipath routing (ECMP) if there are several rules with identical destinations and none of the rules conflict.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-add.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route table that you want to add static rules to.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table that you want to add a static route rule to. 
    6. Select **Add static route rules**. 
    7. Enter the following information:
       * **Destination CIDR block:** Enter a destination CIDR block, enable import route distribution, or enter nothing and the default CIDR block 0.0.0.0/0 is applied, allowing all traffic. The route table must always include at least one destination. 
       * **Next hop attachment type:** Select the intended target type of the static rule. 
       * **Next hop attachment:** Select a VCN, cross-tenancy, or remote peering connection (RPC) attachment.
    8. Select **+Another route rule** to add more rules. 
    9. Select **Add route rules**.
  * Use the [network drg-route-rule add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/add.html) command and required parameters to add one or more static route rules to the specified DRG route table:
Command
CopyTry It
```
oci network drg-route-rule add --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [AddDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/AddDrgRouteRules) operation to add one or more static route rules to the specified DRG route table.


Was this article helpful?
YesNo

