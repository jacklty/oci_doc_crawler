Updated 2025-01-15
# Tagging Security Lists
Add metadata to security lists, which enables you to define keys and values and associate them with resources.
You can apply tags to your security lists to help you organize them according to your business needs. Apply tags at the time you create a security list, or update the security list with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you are not sure whether to apply tags, ask your administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/tagging-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/tagging-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/tagging-securitylist.htm)


  * Use these steps in [Creating a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm#creating-securitylist "Create a security list in a Virtual Cloud Network \(VCN\).") to add tags while you create a security list. To add tags to an existing security list:
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. Find the security list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Add Tags**.
  * Use the [network security-list create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/create.html) command and required parameters to create a security list that uses tags:
Command
CopyTry It
```
oci network security-list create --compartment-id compartment-ocid --vcn-id vcn-ocid ... [--defined-tags | --freeform-tags] tags [OPTIONS]
```

Use the [network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html) command and required parameters to add tags to a security list:
Command
CopyTry It
```
oci network security-list update --security-list-id securitylist-ocid ... [--defined-tags | --freeform-tags] tags [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList) operation to apply tags when you create a security list.
Run the [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList) operation to apply tags when you update a security list.


Was this article helpful?
YesNo

