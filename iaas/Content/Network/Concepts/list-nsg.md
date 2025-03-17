Updated 2025-01-15
# Listing NSGs
List the network security groups (NSGs) in a Virtual Cloud Network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/list-nsg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
  * Use the [network nsg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/list.html) command and required parameters to list the NSGs in a VCN:
Command
CopyTry It
```
oci network nsg list [ --compartment-id compartment-ocid | --vlan-id vlan-ocid ] ... [OPTIONS]
```

You must specify either a `--vlan-id` or a `--compartment-id`, but can't specify both. If you specify a `--vlan-id`, all other parameters are ignored.
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListNetworkSecurityGroups](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/ListNetworkSecurityGroups) operation to list the NSGs in your compartment.


Was this article helpful?
YesNo

