Updated 2025-02-28
# Changing an Identity Domain's Type
Upgrade an identity domain in IAM.
You can upgrade a domain by changing the domain type. Each **identity domain type** is associated with a different set of features and object limits. For information to help you decide which domain type is appropriate for what you want to do, see [IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#overview "Learn about identity domain types and the features and limits associated with each.").
For more information for what validations to expect when changing domain types, see [Changing your Identity Domain Type](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#changing-domain-type).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment that contains the identity domain for which you want to change the domain type. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select **Edit domain**.
    3. Under Domain type, select **Change domains type**.
    4. Select the domain type to which you want to change.
    5. Select **Change domain type**.
    6. Select **Save**.
  * Use the [oci iam domain change-domain-license-type](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/change-domain-license-type.html) command and required parameters to upgrade an identity domain by changing the domain type:
Command
CopyTry It
```
oci iam domain change-domain-license-type --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeDomainLicenseType](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ChangeDomainLicenseType) operation to upgrade an identity domain by changing the domain type.


Was this article helpful?
YesNo

