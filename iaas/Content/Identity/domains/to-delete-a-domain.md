Updated 2025-02-28
# Deleting an Identity Domain
Delete an identity domain in a tenancy in IAM.
Before you can delete an identity domain, you must deactivate the apps in the identity domain and then deactivate the identity domain. See [Deactivating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#deactivate-domain "You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed. An identity domain must be deactivated before it can be deleted.").
Deleting an identity domain irreversibly deletes all users, groups, applications, and other resources in the domain. Any policies granting permissions to users, groups, or dynamic groups in the domain are no longer in effect after the domain is deleted. We recommend updating such policies to remove references to the identity domain name or the identity domain's resources, or deleting them altogether. Deleting an identity domain also invalidates any IAM policy that references it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment in which you want to delete the identity domain. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM."). See also [Managing Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm#Managing_Compartments).
    2. Select the name of the identity domain you want to delete.
    3. Select **Delete**.
    4. Read the warning and then type the name of the identity domain to confirm the deletion.
    5. Select **Delete**.
  * Use the [oci iam domain delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/delete.html) command and required parameters to delete an identity domain:
Command
CopyTry It
```
oci iam domain delete --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/DeleteDomain) operation to delete an identity domain.


Was this article helpful?
YesNo

