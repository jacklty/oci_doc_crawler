Updated 2025-01-17
# Listing DRG Route Tables
List the Dynamic Routing Gateway (DRG) route tables in a DRG.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with route table information you want to get.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
  * Use the [network drg-route-table list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/list.html) command and required parameters to get a list of DRG route tables in a DRG:
Command
CopyTry It
```
oci network drg-route-table list --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgRouteTables](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/ListDrgRouteTable) operation to get a list of DRG route tables in a DRG.


Was this article helpful?
YesNo

