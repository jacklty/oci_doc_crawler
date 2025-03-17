Updated 2025-01-17
# Deleting a DRG Route Table
Delete a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.
Before you try to delete a DRG route table, verify that no attachments in the DRG use that route table.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route table that you want to delete.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table that you want to delete. 
    6. Select **Delete**.
    7. Verify that you want to delete the route table by selecting **Delete**.
The route table is briefly in the Terminating state. When the process is complete it's removed from the list of route tables. 
  * Use the [network drg-route-table delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/delete.html) command and required parameters to delete the specified DRG route table:
Command
CopyTry It
```
oci network drg-route-table delete --drg-route-table-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternalPublicIp/DeleteDrgRouteTable) operation to delete a DRG route table.


Was this article helpful?
YesNo

