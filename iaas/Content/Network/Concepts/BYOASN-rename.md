Updated 2025-01-22
# Renaming ASN
Change the display name of an ASN in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm)


  *     1. Open the navigation menu and click **Networking**. Under **IP management** , click **BYOASN**.
    2. For the ASN that you want to change, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Rename**. 
    3. On the **Rename** page, enter a new ASN name. The name doesn't have to be unique. Avoid entering confidential information.
    4. Click **Save changes**. 
View the work request to see the status.
  * Use the `network byoasn update` command and required parameters to rename your ASN:
Command
CopyTry It
```
oci network byoasn update
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

