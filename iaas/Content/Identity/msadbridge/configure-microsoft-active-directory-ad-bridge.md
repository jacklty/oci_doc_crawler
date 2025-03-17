Updated 2025-01-14
# Configuring an AD Bridge
Configure a bridge between Microsoft Active Directory and an IAM identity domain.
After creating an AD bridge, you configure it by:
  * Selecting the Microsoft Active Directory organizational units (OUs) and groups with which you want IAM to synchronize using the AD bridge. The OUs contain the users that you want to import into IAM. By synchronizing with Microsoft Active Directory, the bridge can transfer new, updated, or deleted user or group records into IAM.
  * Specifying whether, after a user or group is synchronized from Microsoft Active Directory to IAM, if you activate or deactivate a user, change the user's attribute values, or change the group memberships for the user in IAM, these changes are propagated to Microsoft Active Directory.
  * Scheduling how often you want IAM to use the AD bridge to import users and groups from Microsoft Active Directory.
  * Defining custom attribute mappings between Microsoft Active Directory and IAM.
  * Specifying whether users can use their IAM or Microsoft Active Directory passwords, or their federated accounts, to authenticate into IAM to access resources that are protected by IAM, such as the My Profile Console, the IAM Console, or any apps assigned to the users.


You can access the [Managing Security Settings](http://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:13047) infographic to see how to configure an AD bridge.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the AD bridge that you want to configure. 
**Note** The bridge has a status of **Partially Configured**.
  4. In the **Configure the Microsoft Active Directory Domain** page, configure the Microsoft Active Directory domain to poll for changes to users or groups in AD and import those changes into IAM.
    1. In the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes:
      1. Select the **Include Hierarchy** checkbox. If you select a parent OU, then all children OUs is selected. The OUs contain the users and groups that you want to import into IAM.
OR
Clear the checkbox. If you select a parent OU, then children OUs won't be selected.
      2. Select the checkbox for each OU that contains users or groups with which you want IAM to synchronize using the AD Bridge.
**Note**
If you don't see any OUs for users or groups in the **Select organizational units (OUs) for users** and **Select organizational units (OUs) for groups** panes, then refresh your web browser.
To force a full synchronization between Microsoft Active Directory and IAM, clear all checkboxes for selected user or group OUs, select **Save** , and then in the **Save Configuration Changes?** dialog box, select **OK**. Then, select **Import** to import the users and groups from AD.
      3. Optional. In the **Filter** text box, enter a custom filter to search for user or group OUs. For example, entering `(sn=Smith)` returns all users with the last name of Smith. Or, enter `(department=IT)` to return the IT group.
**Tip**
       * To select all users or groups, select the **Include Hierarchy** checkbox, and then select the top-most checkbox in each pane.
       * In the **Filter** text box, you can't enter more than 4,000 characters.
       * The wildcard character `*` is allowed, except when the `AD Attribute` is a DN attribute. For more information about AD filters, select [here](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx).
       * You can use the **Filter** text box to synchronize users from Microsoft Active Directory to IAM based on their group memberships rather than their OUs. To do this, _don't_ clear the checkboxes for the OUs. Instead, in the **Filter** text box, provide the custom group membership filters.
       * If there's a mismatch between the number of users or groups you're expecting to be transferred into IAM and how many users or groups are actually imported, then use Active Directory Users and Computers to test the custom filter in Microsoft Active Directory to verify that the users and groups brought into IAM are correct.
       * The names of the users that you want to import into IAM must contain at least three characters. The names of the groups that you want to import into IAM must contain at least five characters.
       * The telephone numbers of the users that you want to import must meet the requirements of the RFC 3966 specification.
    2. In the **Supported Operations** area, choose which operations for IAM users or groups are propagated to AD:
       * If you activate or deactivate IAM users, and you want these user activation status changes to be reflected in Microsoft Active Directory, then select the **Activate/Deactivate Users** checkbox. Otherwise, leave this checkbox cleared. 
       * If you edit attribute values for IAM users, and you want these modifications to be passed to Microsoft Active Directory, then select the **Update Users Attributes** checkbox. Otherwise, leave this checkbox cleared. 
       * If you change the groups to which IAM users belong, and you want these group membership changes to be propagated to Microsoft Active Directory, then select the **Update Groups** checkbox. Otherwise, leave this checkbox cleared. 
    3. In the **Set import frequency** area, schedule how often, in hours and minutes, you want IAM to use the AD Bridge to import users and groups from Microsoft Active Directory.
**Important** During an incremental synchronization cycle, if there are more than 100,000 group membership changes in Microsoft Active Directory, then the synchronization cycle might take more than one hour. Microsoft Active Directory needs this time to process the change logs. 
    4. In the **Configure Attribute Mappings** area, select **Edit Attribute Mappings** to define custom attribute mappings between Microsoft Active Directory and IAM. See [Define Attribute Mappings for a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/define-custom-attribute-mappings-microsoft-active-directory-ad-bridge.htm#define-custom-attribute-mappings-microsoft-active-directory-ad-bridge "When you create an AD bridge, attribute mappings are defined between Microsoft Active Directory and IAM. Attribute mappings enable the AD bridge to pass values associated with user accounts between Microsoft Active Directory and IAM."). Otherwise, go to the next step.
    5. In the **Authentication Settings** area, select **Enable local authentication** if you want users to use their IAM or their Microsoft Active Directory passwords to authenticate into IAM to access IAM-protected resources.
If you select this option, then configure delegated authentication for this AD bridge. By activating delegated authentication, users transferred into IAM through the bridge will use their Microsoft Active Directory passwords to sign in to IAM. By deactivating delegated authentication, users must use their IAM passwords to authenticate into IAM.
Also, if you select **Enable local authentication** , then keep **Don't send Welcome Notifications** cleared to have IAM notify users by email that they must activate the IAM accounts that are created for them. 
Otherwise, if you don't want users to be notified that IAM created accounts for them, then select the **Don't send Welcome Notifications** checkbox. 
If you want users to use their federated accounts to authenticate into IAM, then select **Enable federated authentication**.
**Note** If you select this option, then configure SSO through the **Identity Providers** page.
**Important** By selecting **Enable federated authentication** , any user accounts that are transferred into IAM through the AD bridge are classified as federated accounts. For referential integrity purposes, you can't deactivate, remove, or change the status of these user accounts to nonfederated.
    6. Select **Save**.
  5. In the **Confirmation** window, select **OK**.
The status of the AD bridge changes from **Partially Configured** to **Configured**. The bridge is created and configured.
**Note** If you use the AD bridge to import a group into IAM, and then delete the group in IAM, you can re-establish a link between the group in Microsoft Active Directory and the group in IAM. To do so:
    1. In the **Select organizational units (OUs) for groups** pane, clear the checkbox for the chosen group, and select **Save**.
    2. Select the checkbox for the group, and select **Save** again.
    3. Run the AD bridge to synchronize the group between IAM and Microsoft Active Directory immediately.


Was this article helpful?
YesNo

