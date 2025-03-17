Updated 2023-10-06
# Oracle Identity Domains
## Before You Begin 🔗 
### Introduction 🔗 
This document describes how to configure identity domain integration with other identity domains in IAM. For more information identity domains in IAM, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm#overview-identity-domains).
### About Identity Domains 🔗 
An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On (SSO) configuration, and SAML/OAuth based Identity Provider administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings (such as MFA).
### What Do You Need? 🔗 
  * A **paid** Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier).
  * Identity domain administrator or security administrator role for the identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles).


**Note regarding the terminology in this document:** The following terminology is used in this document:
  * **Source Identity Domain** : The identity domain on which you’re creating the integration application.
  * **Target Identity Domain** : The identity domain to which you are pushing the users or syncing the users, groups and user-group memberships.


## Operations Supported 🔗 
Operation| Supported| Description  
---|---|---  
Authoritative Sync| Yes| Syncs users, groups, and user-group memberships from the Target Identity Domain and creates or modifies those identities in the Source Identity Domain.  
Sync| Yes| Syncs users, groups, and user-group memberships from the Target Identity Domain and links those identities in the Source Identity Domain.  
Incremental Authoritative Sync| Yes| Syncs users, groups, and user-group memberships from the Target Identity Domain periodically when a user profile is updated. **Note:** Incremental synchronization supports only user changes and not user-group membership changes.  
Incremental Sync| Yes| syncs users, groups, user-group memberships from the Target Identity Domain periodically when a user profile is update. **Note:** Incremental synchronization supports only user changes and not user-group membership changes.  
Create User| Yes| Creates the user in the Target Identity Domain.  
Update User| Yes| Updates the user in the Target Identity Domain.  
Enable User| Yes| Enables the user in the Target Identity Domain.  
Disable User| Yes| Disables the user in the Target Identity Domain.  
Delete User| Yes| Deletes the user in the Target Identity Domain.  
## Prerequisites 🔗 
### Register a Client Application 🔗 
Create a Confidential application with client credentials on the target identity domain with identity domain administrator permissions. This task is required to obtain the credentials (Client ID and Client Secret) that are used for authentication in REST API calls. The credentials are equivalent to service credentials (ID and password) that your client uses to communicate with an identity domain in IAM. This task also helps you determine which requests are authorized through the REST API.
  1. Access the OCI Console.
  2. Open the navigation menu and click **Identity & Security**. Under **Identity** , click **Domains**.
  3. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  4. On the domain details page, click **Integrated applications**.
  5. Click **Add application.**
  6. In the **Add application** dialog box, select **Confidential Application** , and then click **Launch workflow**.
  7. On the **Add application details** page, enter an application name and description, and then click **Next**.
  8. On the **Configure OAuth** page, under **Client configuration** , select **Configure this application as a client now**.
  9. Under **Authorization** , select only **Client Credentials** as the **Allowed Grant Type**.
  10. At the bottom of the page, select **Add app roles** and then click **Add roles**.
  11. In the **Add app roles** panel, select **Identity Domain Administrator** and **Me** , and then click **Add**.
  12. Click **Next** and then click **Finish**.
  13. On the application detail page, scroll down to **General Information**. Copy the **Client ID** and the **Client Secret** and store them in a safe place. You will use them them when [Registering and Activating the Oracle Identity Domains Application](https://docs.oracle.com/en-us/iaas/Content/identity-domains/identity-domains.htm#registering-and-activating-the-oracle-identity-domains-application)
  14. After the application is created, click **Activate**.


## Configuring the Application in Identity Domains 🔗 
Use this section to register and activate the Oracle Identity Domain application.
### Configurations in Oracle Identity Domains Application 🔗 
Configuration Name| Required| Sample Value| Description  
---|---|---|---  
Host Name| Yes| idcs-1234.identity.oraclecloud.com| Provide the identity domain hostname. You can get the details in the target identity domain page.  
Client Id| Yes| None| Provide the client id for the OAuth application created in target Identity Domain.  
Client Secret| Yes| None| Provide the client secret for the OAuth application created in target Identity Domain.  
Authorization Server URL| No| None| This attribute is not to be configured unless the authorization server is different from the default one.  
### Registering and Activating the Oracle Identity Domains Application 🔗 
  1. Access the OCI Console.
  2. Open the navigation menu and click **Identity & Security**. Under **Identity** , click **Domains**.
  3. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  4. On the domain details page, click **Integrated applications**.
  5. Click **Add application.**
  6. In the **Add application** dialog box, select **Application Catalog** , and then click **Launch app catalog**.
  7. Locate and select the `Oracle Identity Domain` application.
  8. Update any application details as required and then click **Next**.
  9. Turn on **Enable provisioning** and confirm.
  10. Under Configure connectivity section, Provide the required configuration details as listed in [Configuration in Oracle Identity Domains Application](https://docs.oracle.com/en-us/iaas/Content/identity-domains/identity-domains.htm#configuration-in-oracle-identity-domains-application)
  11. Under the Configure attribute mapping section, click Attribute mapping to map identity domain attributes to attributes in your application account. **Important:** Don't provision a Federated user with password mapping.
  12. Under Select provisioning operations, select the required operations needed for your use case.
  13. Turn on **Enable synchronization** and click **Finish**.
  14. Click **Activate** , and then click **Activate application**


## Verifying the Integration 🔗 
Use this section to verify the connection to the target identity domain.
### Verifying Provisioning, Connection, and Configuration 🔗 
  1. Open the application you just activated.
  2. Under Provisioning, click **Test connectivity** to validate the connection with the Target Identity Domain.


## Sync 🔗 
A sync job run to import users, groups and user-group memberships. You can run a manual sync at any time using the following steps.
  1. Open the application.
  2. Under Import, click the Import button.


## Troubleshooting 🔗 
Use this section to locate solutions to common integration issues.
### Known Issues 🔗 
There are no known issues topics at this time.
### Other Issues 🔗 
For other issues, open a support ticket. See [Open a Support Ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm).
Was this article helpful?
YesNo

