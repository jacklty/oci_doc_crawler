Updated 2025-01-14
# Editing an Application
Change Oracle and custom applications in an identity domain in IAM. Assign users and groups, edit high-level information, import users and groups into the applications, export users and groups from applications, and perform specific configuration tasks for custom applications.
To modify applications:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application you want to change. The **Applications** page expands to open a sub page that displays high-level information about the application.
You can perform the following tasks in Oracle and custom applications:
     * **Oracle applications** :
       * Assign users and groups.
       * Remove users and groups.
The **Groups** and **Users** tabs are used to display groups and users assigned to application roles of an Oracle application. Although you can filter and sort this list of users and groups, you can't change the list. You can't edit values in these tabs.
       * Import Users and Groups for Oracle Application Roles.
       * Export Users and Groups for Oracle Application Roles.
**Note** If you assign users to Oracle application roles and then deactivate the accounts, IAM prevents the users from accessing the roles. To enable the users to access the Oracle application roles to which they're assigned, activate the users.
       * View High-Level Information
See [Modify Oracle Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-oracle-applications.htm#modify-oracle-applications "You can assign and remove users and groups to Oracle Applications, and import and export users and groups for Oracle Application Roles. You can view the high-level information but can't edit any of the values in Oracle Applications.").
     * **Custom applications:**
       * Assign users and groups.
       * Remove users and groups.
       * Edit high-level information and configuration information.
       * Edit Web Tier Policies for Trusted Applications.
       * Regenerating a Client Secret and generating tokens for Trusted Applications
       * Edit single sign-on (SSO) configuration for SAML Applications.
See [Modify Custom Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-custom-applications.htm#modify-custom-applications "You can assign and remove users and edit high-level information in custom applications.").


Was this article helpful?
YesNo

