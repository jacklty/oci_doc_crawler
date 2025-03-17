Updated 2025-01-15
# Editing a Subnet
Edit the settings for a subnet in a Virtual Cloud Network (VCN).
You can change the following characteristics of a subnet:
  * Name
  * Size of the assigned CIDR block
  * Which set of DHCP options the subnet uses
  * Which route table the subnet uses
  * Which security lists the subnet uses


Be aware of the following considerations:
  * The CIDR block IP range that you specify must be completely within one of the VCN's CIDR block ranges.
  * The new range must use the same network address as the previous range. For example, the previous and new ranges could be 10.0.0.0/25 and 10.0.0.0/24.
  * If you're reducing the CIDR range, ensure that no IP addresses outside of the reduced range are in use.
  * The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the previous CIDR range.
  * You can't create VNICs or private IP addresses for this subnet while a CIDR block update is in progress.
  * After the CIDR block update is complete, the DHCP lease for each host within the subnet must be renewed. Renewal happens automatically within 24 hours. To renew the lease immediately, refer to the applicable OS documentation for guidance on how to renew the lease manually.
  * Ensure that you adjust your secondary VNICs and secondary IP addresses as applicable to match your updated VCN configuration.
  * Once you assign an IPv6 prefix to a subnet, it must always have at least one IPv6 prefix assigned to it.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)


  * Perform the following steps in the Console to edit the subnet.
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Click **Subnets**.
    4. Click the subnet that you're interested in.
    5. On the subnet details page, click **Edit**.
    6. Make your changes. Avoid entering confidential information.
    7. Click **Save changes**.
The changes take effect within a few seconds.
  * Use the [network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and required parameters to edit a subnet:
Command
CopyTry It
```
oci network subnet update --subnet-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet) operation to edit the settings for a subnet.


Was this article helpful?
YesNo

