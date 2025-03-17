Updated 2025-01-17
# Listing Route Distribution Statements
List the statements for an import or export route distribution for a dynamic routing gateway (DRG) in Oracle Cloud Infrastructure.
An import route distribution statement specifies how route advertisements entering the DRG through referenced attachments are inserted into the DRG route table. An export route distribution statement describes how routes are advertised to attachments from their assigned DRG route table.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution for which you want to list statements.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select on the name of the route distribution for which you want to list statements.
On the route distribution details page, the statements are listed in the order in which they're evaluated.
  * Use the [network drg-route-distribution-statement list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/list.html) command and required parameters to list the statements for a specified import or export route distribution:
Command
CopyTry It
```
oci network drg-route-distribution-statement list --route-distribution-id OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/ListDrgRouteDistributionStatements) operation to list the statements for a specified import or export route distribution.


Was this article helpful?
YesNo

