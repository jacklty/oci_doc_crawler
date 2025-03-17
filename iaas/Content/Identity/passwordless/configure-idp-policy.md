Updated 2025-01-14
# Configuring the IdP Policy
Configure the IdP policy to include a new rule for passwordless authentication.
You can create a new IdP Policy, or edit an existing IdP policy.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Under **Security** click **IdP policies**.
  3. In the Identity provider (IdP) policies page, select the policy that you want to update.
  4. Select Add IdP rule, and on the Add identity provider rule page, in **Assign identity providers** choose the authentication factor or factors that you enabled in the previous step. For example, `Email` or `Mobile App Passcode`.
Add all the authentication factor that you enabled in the previous step.
  5. Optionally, choose one or more groups that this rule applies to.
  6. Select **Save changes**.
  7. On the Identity Provider Policy page, if there is more than one IdP rule, ensure that the passwordless authentication rule is the first by selecting **Edit priority**.

Passwordless authentication is now configured.
Was this article helpful?
YesNo

