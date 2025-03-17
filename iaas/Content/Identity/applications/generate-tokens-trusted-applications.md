Updated 2025-01-14
# Generating Tokens for Confidential Applications
When you create a confidential application and you configure the client to use the **JWT Assertion** grant type, you can generate access tokens at any time using the identity domain Console.
**Before You Begin:**
Create an confidential application with the client configured to use the **JWT Assertion** grant type and activate it. See [Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server.").
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select the confidential application that's configured to use the **JWT Assertion** grant type.
  4. Select **Access token**.
  5. In the **Access token** section, use the following table to configure which scopes are included in the access token:
Option | Description  
---|---  
**Available scopes** |  Select **Available scopes** to get the access token to access any resources configured for the application.  If the scopes are defined from multiples resource servers, the token can't be generated. Use the **Customized scopes** option and ensure that the selected scopes are from the same resource server.  
**Customized scopes** using **Invokes identity domain APIs** | 
    1. Select **Customized scopes** and **Invokes identity domain APIs**.
    2. From the list of roles that are assigned to the client application, select those roles that you want to include or remove to limit the scopes to be populated in the resulting token.  
**Customized scopes** using **Invokes other APIs** | 
    1. Select **Customized scopes** and **Invokes other APIs**.
    2. The UI displays a list of all the scopes assigned to the application. You can select any scopes as long as those scopes are from the same resource server.  
**Include refresh token** |  The **Include refresh token** checkbox is enabled if the **Refresh token** grant type is configured for your client application and the resource server to which the scopes belong to allows refresh token generation. The refresh token is used to obtain a new access token without requiring the user to reauthenticate.  
  6. Select **Download token**.
**Note** The downloaded token gets saved as a `tokens<n>.tok` file in the download folder of your browser.


Was this article helpful?
YesNo

