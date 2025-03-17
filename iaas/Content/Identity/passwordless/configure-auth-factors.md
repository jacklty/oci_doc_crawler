Updated 2025-01-14
# Configuring Authentication Factors
Configure the authentication factors to use for passwordless authentication.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **MFA**.
  2. In the **Factors** section, select one or more factors that you want users to use.
If authentication factors were enabled before passwordless authentication has been enabled, then you have to disable the authentication factors and save, then enable the authentication factors again and save otherwise they will not appear when you are setting up the IdP policy rule in the next step.
  3. Select **Save changes**.

Next, you update the IdP policy to include a rule for passwordless authentication.
Was this article helpful?
YesNo

