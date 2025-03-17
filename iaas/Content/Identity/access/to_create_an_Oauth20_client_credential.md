Updated 2025-02-18
# Creating OAuth 2.0 Client Credentials
Use the Console to create a OAuth 2.0 client credentials.
**Note** OAuth 2.0 client credentials are not available in the following **realms** : 
  * the commercial realm (OC1)
  * the United Kingdom Government Cloud (OC4)


  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: 
Open the **Profile** menu, and then click **My Profile**.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: 
Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. Under **Resources** , select **OAuth 2.0 client credentials**.
  3. Select **Generate OAuth 2.0 client credential**.
  4. Select **Name** , and then enter a name for this credential.
  5. Select **Title** , and then enter a description for this credential.
  6. Add the URI for the OAuth 2.0 services that this credential will provide access to.
To **Select an audience-scope pair** :
    1. In **Audience** , enter the URI for the OAuth 2.0 services.
    2. Next, select the **Scope** for this credential. Always select the minimum required privileges.
  7. To add more permissions to this credential, select **+ Another scope** and follow the instructions in the previous step.
  8. Select **Generate**. The new secret string is generated.
Select **Copy** to copy the token string immediately, because you can't retrieve it again after closing the dialog box.
If you're an administrator creating OAuth 2.0 client credentials for another user, you need to securely deliver them to the user by providing them verbally, printing them out, or sending them through a secure email service.
  9. Select **Close**.


You will need the following information from the credential for the token request:
  * The generated secret
  * The OCID of the OAuth 2.0 client credential
  * The scope and audience (fully-qualified scope)


Was this article helpful?
YesNo

