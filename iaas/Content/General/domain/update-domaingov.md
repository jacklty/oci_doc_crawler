Updated 2025-01-31
# Editing Domain Governance
Edit a domain governance entity.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domaingov.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domaingov.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domaingov.htm)


  * For an active domain, you can only enable or disable governance or update the email address. To enable governance for an active domain, see [Enabling Domain Governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#create_domaingov "Enable domain governance for a claimed domain."). For more information on updating an email address, see [Editing Domains](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm#update_domain "Edit a domain.").
  * Use the [oci organizations domain-governance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain-governance/update.html) command and required parameters to update the domain governance entity:
Command
CopyTry It
```
oci organizations domain-governance update --domain-governance-id [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDomainGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/DomainGovernance/UpdateDomainGovernance) operation to update the domain governance entity.


Was this article helpful?
YesNo

