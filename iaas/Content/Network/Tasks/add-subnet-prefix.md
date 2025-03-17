Updated 2025-01-15
# Adding an IPv6 Prefix to a Subnet
Add an IPv6 prefix to a subnet in a Virtual Cloud Network (VCN).
If the subnet is in a VCN that has one or more assigned IPv6 prefixes and the subnet is enabled for IPv6 addressing, you can add an IPv6 prefix unique to the subnet. This assignment can be done when you create the subnet or later.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Click the name of the subnet you're interested in. 
    4. Under **Resources** , click **IPv6 Prefixes**.
    5. Click **Add IPv6 Prefix**. 
Choose a /64 IPv6 prefix. This can be a subset of an Oracle-assigned IPv6 prefix assigned to the VCN, a portion of a BYOIP IPv6 prefix, or a ULA prefix.
You can have up to 3 IPv6 prefixes per subnet, including one allocated by Oracle.
    6. Click **Add IPv6 Prefix**. 
  * Use the [network subnet add-ipv6-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/add-ipv6-subnet-cidr.html) command and required parameters to add an IPv6 prefix to a subnet:
Command
CopyTry It
```
oci network subnet add-ipv6-subnet-cidr --ipv6-cidr-block ipv6-prefix --subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [AddIpv6SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/AddIpv6SubnetCidr) operation to add an IPv6 prefix to a subnet.


Was this article helpful?
YesNo

