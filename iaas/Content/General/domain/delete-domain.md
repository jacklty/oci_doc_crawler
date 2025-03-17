Updated 2025-01-31
# Removing Domains
Release a domain, making it available to be claimed again by another tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm)


  * To remove a domain:
    1. In the **navigation menu** , select ****Governance & Administration****. Under ****Tenancy Management**** , select **Domain Management**.
    2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Remove Domain**. A confirmation is displayed confirming which domain you're removing.
    3. Click **Remove Domain**. The **Status** field changes to **Releasing**. The status changes to **Released** after the [work request](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") is complete, and will be removed from the **Domain Management** page after seven days.
  * Use the [oci organizations domain delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain/delete.html) command and required parameters to remove a domain:
Command
CopyTry It
```
oci organizations domain delete --domain-id [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDomain](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Domain/DeleteDomain) operation to remove the domain.


Was this article helpful?
YesNo

