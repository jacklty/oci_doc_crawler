Updated 2025-01-15
# Listing Subnets
List the subnets available in a given VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-subnets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-subnets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-subnets.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
The subnets in this VCN are listed in a table below the VCN details.
  * Use the [network subnet list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/list.html) command and required parameters to list the subnets in a compartment:
Command
CopyTry It
```
oci network subnet list --compartment-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListSubnets](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ListSubnets) operation to list the subnets in a VCN.


Was this article helpful?
YesNo

