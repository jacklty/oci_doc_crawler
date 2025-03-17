Updated 2025-03-07
# Editing an Identity Domain's Details
You can edit details for an identity domain in IAM. For example, you can select whether to show the identity domain on the sign-in page or upgrade a domain by changing the domain type.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment in which you want to update an identity domain. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select the name of the identity domain that you want to update.
    3. Select **Edit domain**. 
    4. Change the display name, description, domain type, or whether to show the domain on the sign-in page.
       * For the display name, use only letters, numerals, hyphens, periods, or underscores. The name can contain up to 100 characters.
**Note** Changing an identity domain's display name has consequences; for example, bookmarked URLs must be updated to use the new name.
       * To review all the domains types, see [IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#overview "Learn about identity domain types and the features and limits associated with each.").
    5. (Optional) Under **Remote region disaster recovery** , select **Enable remote region disaster recovery**.
You must be subscribed to the paired region to enable remote region disaster recovery. For example, if your home region is US East (Ashburn), then you must be subscribed to US West (Phoenix). For more information, see [Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings "Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:").
    6. Select **Save**.
  * Use the [oci iam domain update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/update.html) command and required parameters to edit certain details for an identity domain:
Command
CopyTry It
```
oci iam domain update --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/UpdateDomain) operation to edit certain details for an identity domain.


Was this article helpful?
YesNo

