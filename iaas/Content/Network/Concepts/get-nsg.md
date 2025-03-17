Updated 2025-01-15
# Getting an NSG's Details
Get details for a network security group (NSG) in a virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
    4. Click the NSG you're interested in to view its details.
The NSG's security rules are displayed on the page. From there you can add, edit, or remove rules.
    5. Under **Resources** , click **VNICs** to see the parent resources that belong to the NSG.
If the [parent resource](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison) is a compute instance, the corresponding VNICs from that instance are also listed on the page. 
For other types of parent resources, the relevant service manages the VNICs on your behalf. Therefore, only the parent resource (and not its corresponding VNICs) is listed on the page.
  * Use the [network nsg get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/get.html) command and required parameters to get an NSG's details:
Command
CopyTry It
```
oci network nsg get --nsg-id nsg-ocid ... [OPTIONS]
```

Use the [network nsg vnics list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/vnics/list.html) command and required parameters to list the VNICs in the specified NSG:
Command
CopyTry It
```
oci network nsg vnics list --nsg-id nsg-ocid ... [OPTIONS]
```

Use the [network nsg rules list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/list.html) command and required parameters to list the security rules for the specified NSG:
Command
CopyTry It
```
oci network nsg rules list --nsg-id nsg-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/GetNetworkSecurityGroup) operation to get an NSG's details.
Run the [ListNetworkSecurityGroupVnics](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroupVnic/ListNetworkSecurityGroupVnics) operation to list the VNICs in the specified NSG.
Run the [ListNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/ListNetworkSecurityGroupSecurityRules) operation to list the security rules for the specified NSG.


Was this article helpful?
YesNo

