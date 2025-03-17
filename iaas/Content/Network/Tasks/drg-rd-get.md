Updated 2025-01-17
# Getting Route Distribution Details
Get information for a specific route distribution.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG for which you want to create a route distribution.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select on the name of the route distribution whose details you're looking for.
  * Use the [network drg-route-distribution get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/get.html) command and required parameters to get information for a specific route distribution:
Command
CopyTry It
```
oci network drg-route-distribution get --route-distribution-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistribution/GetDrgRouteDistribution) operation to get information for a specific route distribution.


Was this article helpful?
YesNo

