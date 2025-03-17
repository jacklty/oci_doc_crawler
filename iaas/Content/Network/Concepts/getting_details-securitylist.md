Updated 2025-01-15
# Getting Details for a Security List
Get the details for a security list in a Virtual Cloud Network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. Click the security list you're interested in to view its details, including the ingress and egress security rules used. This could be the default security list for the VCN or another security list.
Under **Resources** , you can click **Ingress Rules** or **Egress Rules** to switch between the different types of rules.
  * Use the [network security-list get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/get.html) command and required parameters to get details for a security list:
Command
CopyTry It
```
oci network security-list get --security-list-id securitylist-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/GetSecurityList) operation to get details for a security list.


Was this article helpful?
YesNo

