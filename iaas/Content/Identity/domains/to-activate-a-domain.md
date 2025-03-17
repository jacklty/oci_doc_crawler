Updated 2025-02-28
# Activating an Identity Domain
You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment that contains the identity domain that you want to activate. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select the name of the identity domain that you want to activate. 
    3. Select **More actions** , and then select **Activate**.
    4. Confirm the activation.
  * Use the [oci iam domain activate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/activate.html) command and required parameters to activate an identity domain:
Command
CopyTry It
```
oci iam domain activate --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ActivateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ActivateDomain) operation to activate an identity domain.


Was this article helpful?
YesNo

