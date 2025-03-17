Updated 2025-01-17
# Listing Route Rules in a DRG Route Table
List the static and dynamic route rules in a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.
Listing route rules helps you validate and troubleshoot the next hop behavior of traffic entering the DRG. For example, you can confirm the behavior of traffic destined for an on-premises network by validating the routes received by way of a Site-to-Site VPN IPSec tunnel or FastConnect virtual circuit.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route table that you want to list rules for.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG with the route table you're interested in.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG.
    6. Under **Resources** , select **DRG route Tables**. 
    7. Select **Get all route rules**. 
The list of routes includes static routes inserted into the table and all dynamic routes that have been imported from other attachments and inserted by using an import route distribution. 
    8. When you're finished, select **Close**.
  * Use the [network drg-route-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/list.html) command and required parameters to list the route rules in a specified DRG route table:
Command
CopyTry It
```
oci network drg-route-rule list --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/ListDrgRouteRules) operation to list the route rules in a specified DRG route table.


Was this article helpful?
YesNo

