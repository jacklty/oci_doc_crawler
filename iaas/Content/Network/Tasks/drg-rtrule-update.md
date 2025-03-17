Updated 2025-01-17
# Updating a Route Rule in a DRG Route Table
Update one or more route rules in the specified DRG route table.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route table that you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table whose static rules you want to update.
    6. Check the box to the left of the **Destination CIDR block** for the rule or rules you want to update.
    7. Select **Edit** and make the changes you want. 
    8. When finished, select **Save changes**.
  * Use the [network drg-route-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/update.html) command and required parameters to update one or more route rules in the specified DRG route table:
Command
CopyTry It
```
oci network drg-route-rule update --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/UpdateDrgRouteRules) operation to update one or more route rules in the specified DRG route table.


Was this article helpful?
YesNo

