Updated 2025-02-28
# Getting an Identity Domain's Details
View the details of an identity domain in IAM.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment in which you want to view the details of an identity domain. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select the name of the identity domain for which you want to see the details.
The **Overview** page opens by default. Here you can view and copy, if needed, the domain's OCID, description, and URL. You can also select the links in the left-side menu to get more information about the domain, such as its users, groups, and settings.
  * Use the [oci iam domain get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/get.html) command and required parameters to get identity domain information:
Command
CopyTry It
```
oci iam domain get --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/GetDomain) operation to get identity domain information.


Was this article helpful?
YesNo

