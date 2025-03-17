Updated 2025-01-15
# Getting a Subnet's Details 
Get configuration details for a specific subnet in a virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-subnet.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
The subnets in this VCN are listed in a table below the VCN details.
    3. Click the name of the subnet you're interested in.
  * Use the [network subnet get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/get.html) command and required parameters to get configuration details for a specific subnet:
Command
CopyTry It
```
oci network subnet get --subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/GetSubnet) operation to get configuration details for a specific subnet.


Was this article helpful?
YesNo

