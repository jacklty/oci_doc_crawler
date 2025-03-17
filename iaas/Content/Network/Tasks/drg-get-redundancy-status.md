Updated 2025-01-15
# Getting the DRG Redundancy Status
Get the redundancy status for a specified Dynamic Routing Gateway (DRG).
For more information, see [Redundancy Remedies](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancy.htm#Redundancy_Remedies).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-redundancy-status.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-redundancy-status.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-redundancy-status.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment containing the DRG you want to find the redundancy status for.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
The redundancy status displays in the **Dynamic routing gateway information** tab. 
  * Use the [network drg-redundancy-status get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-redundancy-status/get.html) command and required parameters to get the redundancy status for a DRG:
Command
CopyTry It
```
oci network drg-redundancy-status get --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDrgRedundancyStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRedundancyStatus/GetDrgRedundancyStatus) operation to get the redundancy status for a DRG.


Was this article helpful?
YesNo

