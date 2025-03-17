Updated 2025-01-14
# Removing an Identity Domain Administrator
Remove a user as an administrator in an identity domain in IAM.
Each identity domain requires at least one administrator which is granted the identity domain administrator role directly and not indirectly. In a direct grant, the role is assigned to the user post creation. The user isn't part of any group which grants the role. In an indirect grant, the role is granted through a group mapping to the Administrator Group. Ensure that the identity domain has at least one administrator which is granted the identity domain administrator role directly. If you need to grant a user the identity domain administrator role directly, see [Adding Identity Domain Administrators](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/iam-identity-adding-admin.htm#iam-identity-adding-admin "Assign users as administrators in an identity domain in IAM.").
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. On the domain details page, click **Security**.
  3. Select **Administrators**.
  4. Select the user, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Remove**.


Was this article helpful?
YesNo

