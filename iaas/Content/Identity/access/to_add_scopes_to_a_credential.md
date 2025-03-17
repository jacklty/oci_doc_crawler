Updated 2025-02-18
# Adding Scopes to an Existing OAuth 2.0 Client Credential
Use the Console to add scopes to an existing OAuth 2.0 client credential.
  1. View the user's details:
     * If you're creating an OAuth 2.0 client credential for yourself: 
Open the **Profile** menu, and then click **My Profile**.
     * If you're an administrator creating an OAuth 2.0 client credential for another user: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then select the user's name to view the details.
  2. Under **Resources** , select **OAuth 2.0 client credentials**.
  3. Select the name of the credential that you want to add scopes to.
  4. Select **Add scopes**.
  5. Add the URI for the OAuth 2.0 services that you want to add access to.
To **Select a resource-scope pair** :
    1. Select the **Select a resource-scope pair** option.
    2. The **Resource** list displays the resources you have permission to view. Select the resource you want to add credentials for. After you select the resource, the **Audience** field is automatically populated.
    3. Next, select the **Scope** for this credential. Always select the minimum required privileges.
To **Enter fully qualified Scope** :
    1. Select the **Enter fully qualified scope** option.
    2. Enter the **Audience** and **Scope** for this credential.
  6. To add more permissions to this credential, select **+ Another scope** and follow the instructions in the previous step.
  7. Select **Save**.


Was this article helpful?
YesNo

