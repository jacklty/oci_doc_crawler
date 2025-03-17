Updated 2025-01-15
# Getting a VCN's Details
View the settings for a particular Virtual Cloud Network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get_vcn_details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get_vcn_details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get_vcn_details.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in. You might need to change the compartment to find the VCN that you want. 
  * Use the [network vcn get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/get.html) command and required parameters to get configuration details for a VCN:
Command
CopyTry It
```
oci network vcn get --vcn-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/GetVcn) operation to get configuration details about a VCN.


Was this article helpful?
YesNo

