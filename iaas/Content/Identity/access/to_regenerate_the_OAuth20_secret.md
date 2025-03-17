Updated 2025-02-18
# Regenerating the OAuth 2.0 Client Credential Secret
Use the Console to regenerate an OAuth 2.0 client credential secret.
**IMPORTANT:** When you regenerate the secret for a credential, requests made with the previous secret will be denied access to target scopes.
  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: 
Open the **Profile** menu, and then click **My Profile**.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. On the left side of the page, select **OAuth 2.0 client credentials**.
  3. Select the name of the credential that you want to regenerate the secret for.
  4. Select **Regenerate secret**.
  5. Acknowledge the warning dialog and select **Regenerate secret**.
  6. Copy the token string immediately, because you can't retrieve it again after closing the dialog box.
If you're an administrator creating OAuth 2.0 client credentials for another user, you need to securely deliver them to the user by providing them verbally, printing them out, or sending them through a secure email service.
  7. Select **Close**.


Ensure to update existing token requests with the new secret string.
Was this article helpful?
YesNo

