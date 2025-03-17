Updated 2025-02-03
# Generating an Access Token
An access token is an authorization that's used by a client application to access an API or a resource application within a limited period.
The time-bound access tokens inform the resource application that the client is authorized to access the application and perform specific actions specified by the scope that's granted.
You can download access tokens only if an identity domain administrator assigns administrator roles or resource applications to your account.
To generate personal access tokens:
  1. In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see. In the **My profile** console, select **My access tokens**.
  2. You can download an access token in the following ways:
     * Select **Invokes Identity Domains APIs** to specify the available administrator roles that are assigned to you. The APIs from the specified administrator roles will be included in the token.
     * Select **Invokes other APIs** to select confidential applications that are assigned to your account.
       1. Select **Select an application** to add a configured confidential resource application. On the **Select an application** window, the list of assigned confidential applications displays.
       2. Select applications to select them, and then select **Add**. The **My access tokens** page lists the added applications.
  3. In the **Token Expires in mins** field, select or enter how long (in minutes) the access token you're generating can be used before it expires. You can choose to keep the default number or specify between **1** and **527,040**.
  4. Select **Download token**. The access token is generated and downloaded to your local machine as a **tokens.tok** file.


Was this article helpful?
YesNo

