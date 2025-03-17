Updated 2025-02-11
# Listing Organization Tenancies
View a list of tenancies in the organization.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm)


  * Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Tenancies**.
The **Tenancies** list page lists all the tenancies in the organization. The parent tenancy is labeled as such, in comparison to the child tenancies subsumed under the parent.
  * Use the [oci organizations organization list-organization-tenancies](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization/list-organization-tenancies.html) command and required parameters to list tenancies in an organization:
Command
CopyTry It
```
oci organizations organization list-organization-tenancies --organization-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListOrganizationTenancies](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Organization/ListOrganizationTenancies) operation to list tenancies in an organization.


Was this article helpful?
YesNo

