Updated 2025-01-17
# Removing an Import Route Distribution from a DRG Route Table
Remove the import route distribution from a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure so that no routes are imported into it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution that you want to remove.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table whose import route distribution you want to remove.
    6. Select **Edit**.
    7. Clear the **Enable import route distribution** checkbox.
    8. Select **Save changes**.
  * Use the [network drg-route-table remove-import-route-distribution](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/remove-import-route-distribution.html) command and required parameters to remove an import route distribution from a DRG route table:
Command
CopyTry It
```
oci network drg-route-table remove-import-route-distribution --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RemoveImportDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/RemoveImportDrgRouteDistribution) operation to remove an import route distribution from a DRG route table.


Was this article helpful?
YesNo

