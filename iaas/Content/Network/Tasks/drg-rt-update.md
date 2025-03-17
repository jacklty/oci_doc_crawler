Updated 2025-01-17
# Updating a DRG Route Table
Update the settings for a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route table you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select the name of the DRG route table that you want to update.
    6. Select **Edit**. 
    7. Make the necessary changes, and then select **Save changes**.
  * Use the [network drg-route-table update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/update.html) command and required parameters to update settings for a DRG route table:
Command
CopyTry It
```
oci network drg-route-table update --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/UpdateDrgRouteTable) operation to update settings for a DRG route table.


Was this article helpful?
YesNo

