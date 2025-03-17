Updated 2025-01-14
# Testing an Identity Provider
After adding and activating an identity provider, you can test it. You can verify that you can use your federated SSO credentials to sign in to the identity domain through an external website.
  1. If you assigned the identity provider to an identity provider policy, then go to step 2. Otherwise, assign the identity provider to an identity provider policy. See [Assign Identity Providers to the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/assign-identity-providers-policy.htm#assign-identity-providers-policy "You can assign identity providers to an IdP policy. These identity providers will appear in the Sign In page, and a user can use them to access resources that are protected by IAM, such as the My profile console or the IAM console.").
  2. Sign out of the identity domain.
  3. In the **Sign In** page, verify that you see a link called **< Identity_Provider_Name>**.
The **< Identity_Provider_Name>** placeholder represents the name you entered for the identity provider that you created.
If, for example, you created an identity provider called Google, then the link appears as **Google**.
  4. Select the **< Identity_Provider_Name>** link.
  5. Sign in to the external website with your federated SSO credentials.
The identity provider evaluates the user's sign-on credentials, verifies that the user is an authorized user, and returns this information to the identity domain. 
**Tip** If you no longer want to display the link to the identity provider in the Sign In page, then remove the identity provider from all identity provider policies and deactivate the identity provider. See [Removing Identity Providers from the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/remove-identity-providers-policy.htm#remove-idp-from-policy "You can remove identity providers from an identity provider policy. These identity providers will no longer appear in the Sign In page, and a user can't use them to access resources protected by the identity domain.") and [Deleting an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/delete-identity-provider.htm#delete-identity-provider "Delete an identity provider \(IdP\) for an identity domain in IAM.").


Was this article helpful?
YesNo

