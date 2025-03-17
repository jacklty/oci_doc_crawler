Updated 2025-01-15
# Deleting a Security List
Delete a security list in a Virtual Cloud Network (VCN). 
To delete a security list, it must not be associated with a subnet. You can't delete a VCN's default security list.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. For the security list you want to delete, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right side of it, and then select **Terminate**. 
    5. Confirm when prompted.
  * Use the [network security-list delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/delete.html) command and required parameters to delete a security list:
Command
CopyTry It
```
oci network security-list delete --security-list-id securitylist-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/DeleteSecurityList) operation to delete a security list.


Was this article helpful?
YesNo

