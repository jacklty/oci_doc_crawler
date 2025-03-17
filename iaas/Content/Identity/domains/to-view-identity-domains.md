Updated 2025-02-28
# Listing Identity Domains
Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm)


  *     1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
    2. Select the compartment in which you want to list the identity domains. See [Managing Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm#Managing_Compartments).
A table with a list of the identity domains in the compartment is displayed. If you have only one identity domain, it's the Default identity domain. For more information about the Default identity domain, see [The Default Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/the_default_domain.htm#the_default_domain "Each tenancy includes a Default identity domain in the root compartment.").
    3. (Optional) In the table, perform any of the following actions:
       * To see the details of an identity domain, select its name.
       * To access the Users page of the identity domain, select the link in the **Users** column.
       * To access the Groups page of the identity domain, select the link in the **Groups** column.
       * To copy the domain's OCID, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Copy OCID**.
       * To view existing tags for the domains or create tags, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **View tags** or **Add tags**.
  * Use the [oci iam domain list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/list.html) command and required parameters to list the identity domains in a specific compartment in a tenancy:
Command
CopyTry It
```
oci iam domain list --compartment-id compartment_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

