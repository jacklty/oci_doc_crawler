Updated 2024-07-04
# Identity Lifecycle Management Between OCI IAM and Entra ID
Configure provisioning between OCI IAM and Entra ID using three different methods.
This set of tutorials will take around 30 minutes. Use the following scenarios to determine which method to use:
[Tutorial 1:](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm#config-azure-template "Configure Entra ID as the authoritative identity store to manage identities in OCI IAM using an application template from Entra ID Gallery.") Configure Entra ID as the authoritative identity store to manage identities in OCI IAM using an application template from the Entra ID gallery. User accounts are pushed from Entra ID to OCI IAM.
[Tutorial 2:](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/02-config-azure-iam-template.htm#config-azure-iam-template "Configure Entra ID as the authoritative identity store to manage identities in OCI IAM and pull users, groups, and group membership from Entra ID into OCI IAM.") Configure Entra ID as the authoritative identity store to manage identities in OCI IAM using the app template from OCI IAM Application Catalog. OCI IAM pulls users, groups, and group membership from Entra ID into OCI IAM.
[Tutorial 3:](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/03-config-iam.htm#config-iam "Configure OCI IAM as the authoritative identity store to manage identities, along with entitlements in Entra ID") Configuring OCI IAM as the authoritative identity store to manage identities. OCI IAM pushes users, groups, and licenses to Entra ID.
**Note** These tutorials are specific to IAM with Identity Domains.
## Before You Begin 🔗 
To perform this set of tutorials, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Entra ID account with one of the following Entra ID roles:
    * Global Administrator
    * Cloud Application Administrator
    * Application Administrator


[Tutorial 1: Entra ID as Authoritative Source to Manage Identities Using Entra ID Gallery Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm#config-azure-template "Configure Entra ID as the authoritative identity store to manage identities in OCI IAM using an application template from Entra ID Gallery.")
[Tutorial 2: Entra ID as Authoritative Source to Manage Identities Using the OCI IAM Application Catalog](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/02-config-azure-iam-template.htm#config-azure-iam-template "Configure Entra ID as the authoritative identity store to manage identities in OCI IAM and pull users, groups, and group membership from Entra ID into OCI IAM.")
[Tutorial 3: OCI IAM as Authoritative Source to Manage Identities in Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/03-config-iam.htm#config-iam "Configure OCI IAM as the authoritative identity store to manage identities, along with entitlements in Entra ID")
Was this article helpful?
YesNo

