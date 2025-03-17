Updated 2024-05-29
# Updating a VCN
You can update the display name and the tags for a VCN.
To manage IP addressing in a VCN, refer to [Adding IP Address Ranges to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add_cidr_to_vcn.htm#top "You can add an IPv4 CIDR block or IPv6 prefix to a Virtual Cloud Network \(VCN\), with some limitations."), [Changing a VCN's IPv4 CIDR blocks](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm#top "You can change the IPv4 CIDR block range assigned to a Virtual Cloud Network \(VCN\), with some restrictions."), and [Removing an IPv4 CIDR Block or IPv6 Prefix from a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm#top "You can remove an IPv4 CIDR block or IPv6 prefix from a Virtual Cloud Network \(VCN\), with some restrictions.").
See [Tagging a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_vcn.htm#top "Add metadata to virtual cloud networks \(VCNs\) in the form of tags. Tags enable you to define keys and values and associate them with resources.") for information on updating tags.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-vcn.htm)


  * Updating the display name is not available in the Console, but you can update the display name in the CLI and API. 
  * Use the [network vcn update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/update.html) command and parameters shown to change the display name of an existing VCN:
Command
CopyTry It
```
oci network vcn update --vcn-id vcn-ocid [. . .] --display-name name [OPTIONS] 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn) operation to update the VCN display name.


Was this article helpful?
YesNo

