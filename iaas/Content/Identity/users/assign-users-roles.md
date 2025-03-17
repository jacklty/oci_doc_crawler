Updated 2025-01-14
# Assigning Users to Roles
Assign users in an OCI IAM identity domain to a role.
By default, all users can perform self-service capabilities such as updating their profiles, resetting their passwords, and changing their email preferences. You might want to provide a user account with administrative capabilities. For example, you might want a user to manage applications. So, you would assign the user account to the application administrator role.
A user account can be assigned to more than one administrator role. The user account inherits the privileges for each administrator role assigned to the account. If a user account is assigned to both the application administrator role and the user administrator role, then the user can manage applications, users, groups, and group memberships.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Administrators**.
  3. Expand the node for the administrator role for which you want to add or remove a user account, and then perform one of the following:
     * To add a user account to an administrator role, select **Add user** , select the checkbox for each user account that you want to add, and then select **Add users**.
If you're adding users to the user manager role, then after selecting the checkbox for each user that you're adding to this role, you must also select one of the following options:
       * **Manage all users** : These users can manage all users in the IAM identity domain.
       * **Manage selected groups of users** : These users can manage only those users who belong to the groups that you select. After selecting this option, enter or select the groups to be managed by these users.
After making this selection, select **Add users**. If you want to modify either the users who are assigned to the user manager role or the groups that these users can manage, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Edit** from the that appears.
     * To remove a user account from an administrator role, select the user account that you want to remove, select **Remove** , and then in the **Confirmation** window, select **Remove user**.


Was this article helpful?
YesNo

