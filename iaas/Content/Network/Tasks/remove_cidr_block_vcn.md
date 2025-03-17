Updated 2025-01-15
# Removing an IPv4 CIDR Block or IPv6 Prefix from a VCN
You can remove an IPv4 CIDR block or IPv6 prefix from a Virtual Cloud Network (VCN), with some restrictions.
  * You can't remove an IPv4 CIDR block if an IP address in that range is in use.
  * While the VCN is being updated, you can't create or update the VCN's subnets, VLANs, local peering gateways (LPGs), or route tables.
  * After you assign an IPv6 prefix to a VCN, the VCN must always have at least one IPv6 prefix assigned to it. Additionally, a VCN must have at least one CIDR block assigned to it.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to update. You might need to change the compartment to find the VCN that you want.
    3. Under **Resources** , click **CIDR Blocks/Prefixes**.
    4. Find the IPv4 CIDR block or IPv6 prefix in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Remove CIDR Block**.
    5. Click **Remove CIDR Block**.
The VCN's state changes to UPDATING. The time to completion can vary depending on the size of the network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can view work requests to monitor the status of the update.
  * Use the [network vcn remove-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/remove-vcn-cidr.html) command and required parameters to remove an IPv4 CIDR block from a VCN:
Command
CopyTry It
```
oci network vcn remove-vcn-cidr --cidr-block cidr --vcn-id vcn-ocid [OPTIONS]
```

Use the [network vcn remove-ipv6-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/remove-ipv6-vcn-cidr.html) command and required parameters to remove an IPv6 prefix from a VCN:
Command
CopyTry It
```
oci network vcn remove-ipv6-vcn-cidr --vcn-id vcn-ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RemoveVcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/RemoveVcnCidr) operation to remove an IPv4 CIDR block from a VCN.
Run the [RemoveIpv6Cidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/RemoveIpv6Cidr) operation to remove an IPv6 prefix from a VCN.


Was this article helpful?
YesNo

