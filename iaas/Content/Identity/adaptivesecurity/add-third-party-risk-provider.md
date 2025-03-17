Updated 2025-01-14
# Creating a Third-Party Risk Provider
Create a risk provider for an identity domain in IAM that you can use to obtain a user's risk score from the Symantec third-party risk engine. 
The Symantec risk score provides intelligence on a user's behavior across heterogeneous systems with which IAM isn't directly involved. Administrators can then use this third-party risk score with identity domain sign-on policies to enforce a remediation action, such as allowing or denying the user from accessing an identity domain and its protected applications and resources, requiring the user to provide a second factor to authenticate, and so on.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Adaptive security**.
  3. Select **Create risk provider**.
  4. On the **Create risk provider** page, enter the following fields:
     * To select the vendor of the risk provider solution, select **Company**. Only Symantec is supported. 
     * Enter a name and description for the risk provider.
     * Enter the risk provider URL that IAM can use to obtain the user's risk score.
     * Select an authentication type: Basic or Token.
If you select **Basic** , the **Username** and **Password** fields appear. Enter the username and password that IAM uses to authenticate against the risk provider.
If you select **Token** , the **Scheme** and **Token** fields appear. Enter the name of the authentication scheme and the authentication token that IAM uses to pass a user's credentials to the risk provider.
     * Enter the username and password for the risk provider.
     * Under **User identifier** , select the unique identifier for user accounts that IAM uses to link the user in the risk provider. This identifier can be the username or the primary email address.
     * Under **Refresh rate** , specify how often, in minutes or hours, IAM calls the risk provider to check for refreshed scores.
  5. In the **Risk range** pane of the **Add risk provider** page, the risk levels configured in the risk provider are shown automatically, if the provider supports an API to get this information.
**Note** If the API isn't available, an administrator can specify the risk ranges manually, as configured in the risk provider. This information provides a reference to the configured risk ranges in the risk provider and has no significance in the risk calculations.
  6. To check if the risk provider information is correct, select **Validate risk provider**.
Verify that you see the message, **The connection to the {risk_provider_name} risk provider has been validated**. 
**Note** If you receive an error message, check the values that you entered or selected for the **Risk provider URL** and **Authentication type** fields.
  7. Select **Create risk provider**.
The risk provider is added in a deactivated state. To activate the risk provider, see [Activating a Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-risk-provider.htm#activate-risk-provider "Activate a risk provider for an identity domain in IAM to collect user risk scores.").


Was this article helpful?
YesNo

