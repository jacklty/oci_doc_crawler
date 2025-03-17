Updated 2024-10-30
# Unapproving a Created Child Tenancy for Transfer
Cancel an organization's created child tenancy for transfer.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/unapprove-createdchildtenancy-for-transfer.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/unapprove-createdchildtenancy-for-transfer.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/unapprove-createdchildtenancy-for-transfer.htm)


  * This task can't be performed using the Console.
  * Use the [oci organizations organization-tenancy unapprove-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/unapprove-organization-tenancy-for-transfer.html) command and required parameters to cancel an organization's child tenancy for transfer:
Command
CopyTry It
```
oci organizations organization-tenancy unapprove-organization-tenancy-for-transfer --compartment-id, -c [text] --organization-tenancy-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UnapproveOrganizationTenancyForTransfer](https://docs.oracle.com/iaas/api/#/en/organizations/latest/OrganizationTenancy/UnapproveOrganizationTenancyForTransfer) operation to cancel an organization's child tenancy for transfer.


Was this article helpful?
YesNo

