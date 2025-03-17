Updated 2025-01-15
# Removing an IPv6 Prefix from a Subnet
Remove an IPv6 prefix from a subnet in a Virtual Cloud Network (VCN).
After a subnet has an IPv6 prefix assigned to it, it must always have at least one IPv6 prefix assigned to it. This means that you might need to add another IPv6 prefix before you can remove an IPv6 prefix. See [Adding an IPv6 Prefix to a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm#top "Add an IPv6 prefix to a subnet in a Virtual Cloud Network \(VCN\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Click the name of the subnet.
    4. Under **Resources** , click **IPv6 Prefixes**. 
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the subnet, and select **Unassign**. 
  * Use the [network subnet remove-ipv6-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/remove-ipv6-subnet-cidr.html) command and required parameters to remove an IPv6 prefix from a subnet:
Command
CopyTry It
```
oci network subnet remove-ipv6-subnet-cidr --ipv6-cidr-block ipv6-prefix --subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RemoveIpv6SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/RemoveIpv6SubnetCidr) operation to remove an IPv6 prefix from a subnet.


Was this article helpful?
YesNo

