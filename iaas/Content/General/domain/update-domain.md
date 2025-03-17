Updated 2025-01-31
# Editing Domains
Edit a domain.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm)


  * You can only update the email address for an active domain:
    1. In the **navigation menu** , select ****Governance & Administration****. Under ****Tenancy Management**** , select **Domain Management**.
    2. In the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) select **Update Email**. An **Update Email** window is displayed. 
    3. In the **Domain Notification Email** field, enter the new email address and select **Save**.
  * Use the [oci organizations domain update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain/update.html) command and required parameters to update a domain:
Command
CopyTry It
```
oci organizations domain update --domain-id [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDomain](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Domain/UpdateDomain) operation to update a domain.


Was this article helpful?
YesNo

