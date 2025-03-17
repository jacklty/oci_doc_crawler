Updated 2025-01-14
# Adding a SAML Just-in-Time Identity Provider
Set up a SAML identity provider (IdP) that uses just-in-time (JIT) provisioning for an identity domain in IAM. 
  1. Navigate to the identity domain: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Select the name of an identity provider.
  4. On the details page, select **Configure JIT**.
  5. Select **Enable Just-in-Time (JIT) provisioning**.
  6. Select one of the following options:
     * **Create a new identity domain user** : Create an identity user in the identity domain, if the user doesn't exist when sign in with the identity provider.
     * **Update the existing identity domain user** : Merge and overwrite identity domain user account data from the mapped IdP. The existing data is overwritten by the user data from the IdP.
**Note** To enable JIT, you must select one of these options.
  7. In the **Map user attributes** area , map a user account from the IdP to a user account from the identity domain.
    1. Select a value in the **IdP user attribute type** row.
       * If you select **Attribute** , then enter the IdP user attribute name.
       * If you select **NameID** , you don't need to enter the IdP user attribute name.
    2. (Optional) Select the identity domain user attribute.
    3. (Optional) Add more identity domain attributes.
  8. To enable group mapping, select **Assign group mapping**. 
**Note** If you enable group mapping, proceed to the next step. If not, skip to step 10.
  9. For **Group membership attribute name** enter the IdP attribute name that contains group memberships.
  10. To import the group settings, select one of the following options:
     * **Define explicit group mapping** : This option requires you to provide the group name to map between the IdP and identity domain. If you select this option, enter the IdP group name and select an available identity domain group name.
     * **Assign implicit group mapping** : This option maps an IdP group to an identity domain group that has the same name. No other action is required.
  11. (Optional) To assign group memberships from the identity domain, select **Assign domain group memberships** and then perform the following steps:
    1. Select **Add group**.
    2. Select the groups that you want to add, and then select **Add groups**.
  12. Under **Assignment rules** , specify actions to take when assigning group memeberships:
     * If users are assigned to existing groups, select whether to merge with existing group memberships or replace existing group memberships.
  13. When a group isn't found, select to take one of the following actions:
     * **Ignore the missing group** : The user successfully signs in.
     * **Fail the entire request** : The sign-in attempt fails.
  14. Select **Save Changes**.
  15. (Optional) Activate the IdP before adding it to any policies. For more information, see [Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm#activate-identity-provider "Activate or deactivate an identity provider \(IdP\) for an identity domain in IAM.").


Was this article helpful?
YesNo

