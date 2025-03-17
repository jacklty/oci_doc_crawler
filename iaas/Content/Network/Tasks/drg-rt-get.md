Updated 2025-01-17
# Getting DRG Route Table Information
Get information about the specified Dynamic Routing Gateway (DRG) route table.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with route table information you want to get.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table. 
  * Use the [network drg-route-table get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/get.html) command and required parameters to get information about the specified DRG route table:
Command
CopyTry It
```
oci network drg-route-table get --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/GetDrgRouteTable) operation to get information about the specified DRG route table.


Was this article helpful?
YesNo

