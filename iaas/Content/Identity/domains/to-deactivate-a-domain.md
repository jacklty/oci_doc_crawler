Updated 2025-02-28
# Deactivating an Identity Domain
You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed. An identity domain must be deactivated before it can be deleted.
You can't deactivate the Default identity domain or the identity domain to which you're signed in (the current domain).
Before you deactivate an identity domain, all Cloud, Oracle, Custom, and Enterprise applications must be deactivated. All applications created by App Services in Oracle Cloud Services (for example, AnalyticsINST-OAC1) must also be deactivated, but "entitlement" apps in Oracle Cloud Services (for example, ADWC) don't need to be deactivated.
Immediately after the administrator starts deactivating an identity domain, the identity domain moves to a deactivating state and users can no longer authenticate to it.
**Note** Paid tier identity domains continue to incur costs when **deactivated**. To avoid incurring additional costs, you should **delete** the identity domain.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment that contains the identity domain that you want to deactivate. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select the name of the identity domain you want to deactivate.
    3. Select **More actions** , and then select **Deactivate**.
    4. Confirm the deactivation.
The identity domain is in an **Inactive** status.
  * Use the [oci iam domain deactivate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/deactivate.html) and required parameters to deactivate an identity domain:
Command
CopyTry It
```
oci iam domain deactivate --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeactivateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/DeactivateDomain) operation to deactivate an identity domain.


Was this article helpful?
YesNo

