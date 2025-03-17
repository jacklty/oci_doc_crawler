Updated 2025-01-17
# Updating a Route Distribution
Update a route distribution for a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
The following steps describe how to change the name of a route distribution. To add or update a statement for an import or export route distribution, see [Adding a Route Distribution Statement](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm#drg-rds-add "Add a statement to an import or export route distribution for a dynamic routing gateway \(DRG\) in Oracle Cloud Infrastructure.") or [Updating a Route Distribution Statement](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-update.htm#drg-rds-update "Update one or more route distribution statements in the specified route distribution."). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select the name of the route distribution that you want to update.
    6. Select **Edit**.
    7. Enter a new name, then select **Save changes**.
  * Use the [network drg-route-distribution update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/update.html) command and required parameters to update the specified route distribution:
Command
CopyTry It
```
oci network drg-route-distribution update --route-distribution-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistribution/UpdateDrgRouteDistribution) operation to update the specified route distribution.


Was this article helpful?
YesNo

