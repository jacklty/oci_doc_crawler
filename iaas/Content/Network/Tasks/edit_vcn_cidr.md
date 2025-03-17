Updated 2025-01-15
# Changing a VCN's IPv4 CIDR blocks
You can change the IPv4 CIDR block range assigned to a Virtual Cloud Network (VCN), with some restrictions.
  * The CIDR block range you specify must not overlap with any other CIDR block in this VCN or in a peered VCN.
  * You can't change the CIDR block to a range that excludes an IP address in use in the current CIDR block range.
  * While the VCN is being updated, you can't create or update the VCN's subnets, VLANs, local peering gateways (LPGs), or route tables.


**Note** You can't edit an IPv6 prefix that's been added to a VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to update. You might need to change the compartment to find the VCN that you want.
    3. Under **Resources** , click **CIDR Blocks/Prefixes**.
    4. Find the IPv4 CIDR block in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit CIDR Block**.
    5. Make the applicable change or changes.
    6. Click **Save Changes**.
The VCN's state changes to UPDATING. The time to completion can vary depending on the size of the network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can view work requests to monitor the status of the update.
  * Use the [network vcn modify-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/modify-vcn-cidr.html) command and required parameters to update the specified CIDR block of a VCN: 
Command
CopyTry It
```
oci network vcn modify-vcn-cidr --new-cidr-block cidr-block --original-cidr-block cidr-block --vcn-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ModifyVcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ModifyVcnCidr) operation to update the specified CIDR block of a VCN.


Was this article helpful?
YesNo

