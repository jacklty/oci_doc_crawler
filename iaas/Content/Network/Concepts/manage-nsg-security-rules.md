Updated 2025-01-15
# Managing Security Rules for an NSG
Add, edit, or remove security rules for a network security group (NSG) in a virtual cloud network (VCN).
After an NSG is created, you can add or remove security rules to allow the types of ingress and egress traffic that the VNICs in the group require.
As mentioned in [Overview of Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#overview), you can specify an NSG as the source (for ingress rules) or destination (for egress rules) in a given NSG's security rule. The two NSGs must be in the same VCN. For example, if both NSG1 and NSG2 belong to the same VCN, you could add an ingress rule to NSG1 that lists NSG2 as the source. If someone deletes NSG2, the rule becomes invalid. The REST API uses an `isValid` Boolean in the `SecurityRule` object to convey that status.
When you manage an NSG's VNIC membership, you do it as part of working with the parent resource, not the NSG itself. For more information, see [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
    4. Click the NSG you're interested in to view its details.
The NSG's security rules are displayed on the page. From there you can add, update, or remove security rules. For information about the fields, see [Creating an NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/create-nsg.htm#create-nsg "Create a network security group \(NSG\) in a Virtual Cloud Network \(VCN\).").
  * Use the [network nsg rules add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/add.html) command and required parameters to add NSG security rules:
Command
CopyTry It
```
oci network nsg rules add --nsg-id nsg-ocid ... [OPTIONS]
```

Use the [network nsg rules update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/update.html) command and required parameters to update NSG security rules:
Command
CopyTry It
```
oci network nsg rules update --nsg-id nsg-ocid ... [OPTIONS]
```

Use the [network nsg rules remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/remove.html) command and required parameters to remove NSG security rules:
Command
CopyTry It
```
oci network nsg rules remove --nsg-id nsg-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * If you're familiar with security lists and use the REST API, note that the model for _updating_ existing security rules is different between security lists and NSGs. With NSGs, each rule in a given group has a unique Oracle-assigned identifier (example: 04ABEC). When you call `UpdateNetworkSecurityGroupSecurityRules`, you provide the IDs of the specific rules that you want to update. For comparison, with security lists, the rules have no unique identifier. When you call `UpdateSecurityList`, you must pass in the _entire_ list of rules, including rules that are not being updated in the call. 
Run the [AddNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/AddNetworkSecurityGroupSecurityRules) operation to add NSG security rules.
Run the [UpdateNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/UpdateNetworkSecurityGroupSecurityRules) operation to update NSG security rules.
Run the [RemoveNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/RemoveNetworkSecurityGroupSecurityRules) operation to remove NSG security rules.


Was this article helpful?
YesNo

