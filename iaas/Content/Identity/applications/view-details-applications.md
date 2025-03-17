Updated 2025-01-14
# Viewing Details About Applications
By default, you can see the name and description for each application in IAM.
By selecting an application name, you can view high-level and configuration information about the application. For Oracle applications, you can also see the roles associated with the application, and the IAM groups and users assigned to the application.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application name for which you want additional information.
**Tip** To search for applications, enter all or part of the beginning of the application name that you want to locate in the search field, and then press **Enter**. To fine-tune your search, select the search field again, and then select a status.
  4. To view high-level information about the application, such as the application type, name, description, icon, URL, links, and whether the application will appear on the **My Apps** page, select **Details**.
  5. To view configuration information about the application, select **Configuration**. For custom SAML applications, this tab is labeled **SSO configuration** because, by granting SAML applications to users, they can single sign-on (SSO) into SaaS applications that support SAML for SSO. See [Add a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server."), [Add a Mobile Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-mobile-application.htm#add-mobile-application "Add mobile applications that use OAuth 2.0 and they can't maintain the confidentiality of their client secrets."), and [Add a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-saml-application.htm#add-saml-application "Create a Security Assertion Markup Language \(SAML\) application and grant it to users so that your users can single sign-on \(SSO\) into your SaaS applications that support SAML for SSO.").
  6. For Oracle applications, to view roles associated with the application, select **Application roles**. You can assign users and groups to an application role or remove users and groups from the application role. See [Editing an Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-applications.htm#modify-applications "Change Oracle and custom applications in an identity domain in IAM. Assign users and groups, edit high-level information, import users and groups into the applications, export users and groups from applications, and perform specific configuration tasks for custom applications.").
  7. For Oracle applications, to view the names and descriptions of any groups assigned to the application, select **Groups**.
  8. For Oracle applications, to view the names, email addresses, and phone numbers of any users assigned to the application, select **Users**. You can filter and sort this list of users.
     * To display only those users who are assigned to a particular application role, select **Show** , and then select the application role.
     * To display users who are assigned to any application role, select **Show** , and then select **All role members**.
     * To sort the users in ascending order by their names or email addresses, select **Sort By** , and then select **Name** or **Email**.


Was this article helpful?
YesNo

