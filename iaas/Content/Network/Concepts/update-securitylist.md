Updated 2025-01-15
# Updating Rules in a Security List
Update the rules used in a security list in a Virtual Cloud Network (VCN). 
You can add and remove rules from the security list. A security list can have no rules. Notice that when you update a security list in the API, the new set of rules replaces the entire existing set of rules.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. Click the security list you're interested in.
    5. Under **Resources** , click either **Ingress Rules** or **Egress Rules** , depending on the type of rule you want to work with. 
    6. If you want to add a rule, click **Add Ingress Rules** (or **Add Egress Rules**). See details of adding a rule in [Creating a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm#creating-securitylist "Create a security list in a Virtual Cloud Network \(VCN\)."). 
    7. If you want to delete an existing rule, select the checkbox next to the rule and then click **Remove**.
    8. If you wanted to edit an existing rule, select the checkbox next to the rule, and then click **Edit**.
  * Use the [network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html) command and required parameters to update the rules used in a particular security list:
Command
CopyTry It
```
oci network security-list update --security-list-id securitylist-ocid ... [--egress-security-rules | --ingress-security-rules] rules [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList) operation to update the rules used in a particular security list.


Was this article helpful?
YesNo

