Updated 2025-01-15
# Listing DRGs
List the dynamic routing gateways (DRGs) in a compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
  * Use the [network drg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/list.html) command and required parameters to list the DRGs in a compartment:
Command
CopyTry It
```
oci network drg list --compartment-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgs](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/ListDrgs) operation to list the DRGs in a compartment.


Was this article helpful?
YesNo

