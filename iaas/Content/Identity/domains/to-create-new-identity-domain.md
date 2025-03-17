Updated 2025-03-07
# Creating an Identity Domain
To create an identity domain in IAM, administrators need to know which identity domain type they want to create, in which compartment to create it, and the new identity domain administrator's sign-in credentials, if needed. The domain types that you're allowed to create are based on your subscription.
The default groups created in a new identity domain are All Domain Users, and Domain Administrators. During identity domain creation, if you create an administrative user for the identity domain, that administrator is placed in the Domain Administrators group. The Domain Administrators group can't be deleted and there must be at least one user in the group. Administrators can hide any identity domain that they create from the sign-in page.
When you create an identity domain, the selected region in the Console becomes the identity domain's home region. For example, if the selected region in the Console is **Germany Central (Frankfurt)** and you create an identity domain, the identity domain is created in the **Frankfurt** region as the home region.
**Note** Unlike the Default identity domain, additional identity domains aren't automatically replicated to all subscribed regions. If users in these identity domains need to interact with OCI resources in other regions, ensure that you [enable replication for those domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#manage-domain-regions "You can replicate an identity domain in IAM to additional regions to enable users in that domain to interact with OCI resources in those regions.").
Many Oracle services and applications automatically provision an Oracle Apps identity domain which lets you to use IAM to manage access to the subscribed services. For example, if you order a Fusion App, you also get an Oracle Apps identity domain. You can't create Oracle Apps or Oracle Apps Premium identity domains directly.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment in which you want to create the identity domain. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM."). See also [Managing Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm#Managing_Compartments).
    2. Select **Create domain**.
    3. On the **Create domain** page, enter a display name for the domain, using only letters, numerals, hyphens, periods, or underscores. The name can contain up to 100 characters. 
**Note** Select the display name carefully. Changing the identity domain display name has consequences; for example, bookmarked URLs must be updated to use the new name.
    4. Enter a description.
    5. Select one of the available domain types. For information to help you decide which domain type is appropriate for what you want to do, see [IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#overview "Learn about identity domain types and the features and limits associated with each.").
    6. To use your administrative user account for this identity domain, then clear the **Create an administrative user for this domain** checkbox. Otherwise, enter the details of the user who you want to administer this identity domain.
**Note** Granting users or groups the identity domain administrator role for domains other than the default domain grants them full administrator permissions to only that domain (not to the tenancy). At least one administrator for the identity domain must be granted the identity domain administrator role directly. This is in addition to any identity domain administrator roles granted by group membership. For more information, see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
    7. Verify that the correct compartment is selected. 
    8. To add tagging, select **Show advanced options** and enter the tagging details.
    9. (Optional) Under **Remote region disaster recovery** , select **Enable remote region disaster recovery**.
You must be subscribed to the paired region to enable remote region disaster recovery. For example, if your home region is US East (Ashburn), then you must be subscribed to US West (Phoenix). For more information, see [Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings "Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:").
    10. Select **Create domain**.
Ensure that the identity domain status is **Creating**.
  * Use the [oci iam domain create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/create.html) command and required parameters to create an identity domain:
Command
CopyTry It
```
 oci iam domain create --compartment-id compartment_ocid --description description --display-name display_name --home-region home_region --license-type license_type [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/CreateDomain) operation to create an identity domain.


Was this article helpful?
YesNo

