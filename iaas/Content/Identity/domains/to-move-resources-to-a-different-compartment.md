Updated 2025-02-28
# Moving an Identity Domain Between Compartments
Move identity domains between compartments in IAM.
You can move any identity domain between compartments within the same tenancy, except the Default identity domain. The Default identity domain can't be moved from the root compartment of the tenancy.
When you move a domain, all its resources are moved with it. For information about moving resources, see [Moving a Resource Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_resource_to_a_different_compartment.htm#To_move_a_resource_to_a_different_compartment "Most resources can be moved after they're created.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm)


  *     1. On the **Domains** list page, under **List scope** , select the compartment that contains the identity domain you want to move. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM."). 
    2. Select the name of the identity domain that you want to move. 
    3. Select **Move resource**.
    4. Select a new compartment and then select **Move resource**.
  * Use the [oci iam domain change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/change-compartment.html) command and required parameters to move an identity domain between compartments within the same tenancy:
Command
CopyTry It
```
oci iam domain change-compartment --compartment-id compartment_ocid --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeDomainCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ChangeDomainCompartment) operation to move an identity domain between compartments within the same tenancy.


Was this article helpful?
YesNo

