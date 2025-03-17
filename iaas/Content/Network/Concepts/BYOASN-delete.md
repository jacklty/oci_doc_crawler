Updated 2025-01-22
# Deleting ASN
Delete an ASN and disassociate your BYOIP CIDR block from the deleted ASN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm)


  *     1. Open the navigation menu and click **Networking**. Under **IP management** , click **BYOASN**.
    2. Click the name of the ASN you want to delete. The details page for that ASN appears.
    3. Click **Delete**. A confirmation window appears stating a default ASN will be used to used to associate with your BYOIP CIDR block.
    4. Click ****Advertise**** to confirm that you want to advertise your BYOIP CIDR block with the default ASN.
    5. Click **Update Origin ASN** to confirm disassociation of your BYOIP CIDR block from the deleted ASN.
  * Use the `network byoasn delete` command and required parameters to rename your ASN:
Command
CopyTry It
```
oci network byoasn delete
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/DeleteByoasn) operation to delete an ASN.


Was this article helpful?
YesNo

