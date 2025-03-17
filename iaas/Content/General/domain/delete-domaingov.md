Updated 2025-01-31
# Disabling Domain Governance
Disable domain governance on a claimed domain. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm)


  * The domain must already be active before you can disable governance.
    1. In the **navigation menu** , select ****Governance & Administration****. Under ****Tenancy Management**** , select **Domain Management**.
    2. In the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), select **Disable Governance**. A **Turn off Domain Governance** confirmation is displayed, indicating which domains are to be disabled.
    3. Select **Confirm**. After refreshing the page, the **Status** field changes to **Disabled** to indicate the domain is verified but not governed.
To enable governance, see [Enabling Domain Governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#create_domaingov "Enable domain governance for a claimed domain.").
  * Use the [oci organizations domain-governance delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain-governance/delete.html) command and required parameters to remove domain governance from a claimed domain:
Command
CopyTry It
```
oci organizations domain-governance delete --domain-governance-id [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDomainGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/DomainGovernance/DeleteDomainGovernance) operation to remove domain governance from a claimed domain.


Was this article helpful?
YesNo

