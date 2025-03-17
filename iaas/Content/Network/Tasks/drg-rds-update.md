Updated 2025-01-17
# Updating a Route Distribution Statement
Update one or more route distribution statements in the specified route distribution.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select on the name of the route distribution with a statement you want to you want to update.
  * Use the [network drg-route-distribution-statement update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/update.html) command and required parameters to update one or more route distribution statements:
Command
CopyTry It
```
oci network drg-route-distribution-statement update --route-distribution-id OCID --statements [complex type] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/UpdateDrgRouteDistributionStatements) operation to update one or more route distribution statements.


Was this article helpful?
YesNo

