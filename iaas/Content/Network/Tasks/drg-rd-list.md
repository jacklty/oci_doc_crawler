Updated 2025-01-17
# Listing Route Distributions
Get a list of route distributions in the specified DRG.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with route distributions you want to list.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
  * Use the [network drg-route-distribution list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/list.html) command and required parameters to get a list of route distributions in a specified DRG:
Command
CopyTry It
```
oci network drg-route-distribution list --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgRouteDistributions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistribution/ListDrgRouteDistributions) operation to get a list of route distributions in a specified DRG.


Was this article helpful?
YesNo

