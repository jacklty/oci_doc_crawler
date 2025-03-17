Updated 2025-01-17
# Deleting a Route Distribution
Delete a specified route distribution.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution that you want to delete.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select on the name of the route distribution you want to delete.
    6. To delete the route distribution, select **Terminate**.
    7. Confirm the deletion by selecting **Terminate**.
  * Use the [network drg-route-distribution delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/delete.html) command and required parameters to delete the specified route distribution:
Command
CopyTry It
```
oci network drg-route-distribution delete --route-distribution-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/DeleteDrgRouteDistribution) operation to <task-being-performed>.


Was this article helpful?
YesNo

