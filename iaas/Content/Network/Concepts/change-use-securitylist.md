Updated 2025-01-15
# Changing Which Security Lists a Subnet Uses
Change which security lists are used in a particular subnet in a virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Click **Subnets**.
    4. Click the subnet you're interested in.
    5. Under **Resources** , click **Security Lists**.
    6. To add a security list, click **Add Security List** , and select the new security list you want the subnet to use.
    7. To remove a security list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right side of it, and then select **Remove**. Remember that a subnet must always have at least one security list associated with it.
The changes take effect within a few seconds.
  * Use the [network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and described parameters to change which security list a subnet uses:
Command
CopyTry It
```
oci network subnet update --subnet-id ocid --security-list-ids securitylist-ocids ... [OPTIONS]
```

The security-list-ids are OCIDs of the security list or lists the subnet will use. This replaces the entire current set of security lists. Remember that security lists are associated _with the subnet_ , but the rules are applied to the individual VNICs in the subnet. This is a complex type whose value must be valid JSON.
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet) operation to change which security lists are used in a particular subnet.


Was this article helpful?
YesNo

