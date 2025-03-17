Updated 2025-01-17
# Delete a Route Distribution Statement
Remove or delete one or more route distribution statements from a route distribution for a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution statement for which you want to remove a statement.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select the name of the route distribution from which you want to remove a statement.
    6. Confirm the removal.
  * Use the [network drg-route-distribution-statement remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/remove.html) command and required parameters to delete one or more route distribution statements from the specified route distribution:
Command
CopyTry It
```
oci network drg-route-distribution-statement remove --route-distribution-id ocid --statement-ids [complex type] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RemoveDrgRouteDistributionStatements ](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/RemoveDrgRouteDistributionStatements) operation to delete one or more route distribution statements from the specified route distribution.


Was this article helpful?
YesNo

