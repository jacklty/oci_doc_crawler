Updated 2025-01-14
# Registering a Client Application
Before you configure multifactor authentication (MFA) in an identity domain in IAM, register a client application so that you have the credentials (client ID and client secret) that are used for authentication in REST API calls. Oracle Support can use your client ID and client secret to help you troubleshoot if you have issues, for example, if you lock yourself out of an identity domain when configuring MFA.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select **Add application.**
  4. In the **Add application** dialog box, select **Confidential Application** , and then select **Launch workflow**.
  5. On the **Add application details** page, enter an application name and description, and then select **Next**.
  6. On the **Configure OAuth** page, under **Client configuration** , select **Configure this application as a client now**.
  7. Under **Authorization** , select only **Client Credentials** as the **Allowed Grant Type**.
  8. At the bottom of the page, select **Add app roles** and then select **Add roles**.
  9. In the **Add app roles** panel, select **Identity Domain Administrator** , and then select **Add**.
  10. Select **Next** and then select **Finish**.
  11. On the application detail page, scroll down to **General Information**. Copy the **Client ID** and the **Client Secret** and store it in a safe place.
  12. After the application is created, select **Activate**.


Was this article helpful?
YesNo

