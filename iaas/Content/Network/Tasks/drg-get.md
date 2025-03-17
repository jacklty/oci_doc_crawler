Updated 2025-01-15
# Getting a DRG's Details
View the settings for a particular Dynamic Routing Gateway (DRG).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment containing the DRG you want to list details for.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
  * Use the [network drg get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/get.html) command and required parameters to view the settings for a DRG:
Command
CopyTry It
```
oci network drg get --drg-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetDrg) operation to view the settings for a DRG.


Was this article helpful?
YesNo

