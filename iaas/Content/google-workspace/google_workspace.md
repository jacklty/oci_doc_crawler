Updated 2023-10-06
# Google Workspace Authoritative Sync
## Before You Begin 🔗 
### Introduction 🔗 
This document describes how to configure Google Workspace for Authoritative Sync with identity domains in IAM. For more information identity domains in IAM, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm#overview-identity-domains).
### About Google Workspace 🔗 
Google Workspace is a brand of cloud computing software, and productivity and collaboration tools. Google Workspace includes tools such as Gmail, Hangouts, Calendar, Drive for storage, Docs, Sheets, Slides, Forms, and Sites for collaboration.
### What Do You Need? 🔗 
  * A **paid** Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier).
  * Identity domain administrator or security administrator role for the identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles).
  * A Google Workspace account with authorization rights for users and groups.


## Scopes Used for Google Workspace Integration with Identity Domains 🔗 
Scope| Description  
---|---  
https://www.googleapis.com/auth/admin.directory.group.readonly| Scope for only retrieving group, group alias, and member information.  
https://www.googleapis.com/auth/admin.directory.user.readonly| Scope for only retrieving users or user aliases.  
## Operations Supported 🔗 
Operation| Description  
---|---  
Authoritative Sync| Configures Google Workspace as an authoritative source of an identity domain. The operation synchronizes users, groups, user-group memberships from Google Workspace and creates or modifies those identities in an identity domain.  
**Note:** Google Workspace does not support delta or incremental changes to users, groups, and user-group membership changes.
## Configuring Google Workspace in Identity Domains 🔗 
Use this section to register and activate the Google Workspace App.
### Registering and Activating the Google Workspace App 🔗 
  1. Access the OCI Console.
  2. Open the navigation menu and click **Identity & Security**. Under **Identity** , click **Domains**.
  3. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  4. Click **Add application**.
  5. In the **Add application** window, click **Application Catalog** , and then **Launch app catalog**.
  6. Find and select the `Google Workspace Authoritative Sync` application.
  7. Update any application details as required and then click **Next**.
  8. Turn on **Enable provisioning** and confirm.
  9. Click **Authorize with Google Workspace Authoritative Sync**. A new window for Authorization for accessing users and groups opens.
    1. Provide the Google credentials and then click sign-in. A set of scopes displays. See the scope details [Scopes used for Google Workspace integration](https://docs.oracle.com/en-us/iaas/Content/google-workspace/google_workspace.htm#scopes-used-for-google-workspace-integration-with-identity-domains).
    2. Click **Authorize**. The window will close.
  10. Under Select provisioning operations, select **Authoritative sync**.
  11. Turn on **Enable synchronization** and click **Finish**.
  12. Click **Activate** , and then click **Activate application**.


### Configuring Google Workspace Application 🔗 
Configuration Name| Required| Sample Value| Description  
---|---|---|---  
Groups List| No| developers@example.comadmins@example.com| Provide the list of the groups to synchronize users belonging to those groups. If no list is provided, then the application synchronizes all users, groups, and user-group memberships.  
## Verifying the Integration 🔗 
Use this section to verify the connection to Google Workspace.
### Verifying Provisioning, Connection, and Configuration 🔗 
  1. Open the application you just activated.
  2. Under Provisioning, click **Test connectivity** to validate the connection with Google Workspace.


## Sync 🔗 
Run a manual sync job run to import users, groups and user group memberships at any time using the following steps.
**Note:** Google Workspace doesn’t support incremental sync.
  1. Open the application.
  2. Under Import, click the Import button.


## Troubleshooting 🔗 
Use this section to locate solutions to common integration issues.
### Known Issues 🔗 
#### "Google hasn't verified this app" message while authorizing with Google 🔗 
Application verification is in progress with Google.
### Getting Help and Contacting Support 🔗 
For any other issues, open a support ticket. See [Open a Support Ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm).
Was this article helpful?
YesNo

