Updated 2023-09-25
# Defining a Secret for a Compute Scan Recipe
Create a secret for a Compute (host) scan recipe to store the Qualys license information.
**Prerequisites:**
  * Create an account in Qualys with a license to use Vulnerability Management, Detection, and Response (VMDR). You must have a Qualys account with a license to use VMDR before you can complete the steps to define a secret for a scan recipe. See the [Qualys VMDR](https://www.qualys.com/forms/vmdr/) sign-up page to get started. After you have a license, you must generate a cloud agent activation key, and enable OCI for the agent. Perform these tasks using the Qualys platform. For instructions, see the [Qualys Cloud Platform](https://www.qualys.com/documentation/) documentation.
  * Create a vault with a vault master encryption key in which to store your Qualys license information. See [Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm).

When creating a Compute scan recipe with a Qualys agent, you need to add an existing secret from a vault or define a new secret for the Compute scan recipe. You can also edit a secret for an existing Compute scan recipe.
  1. To define a new secret, access the **Create secret** window in one of the following ways:
     * When creating a new Compute scan recipe with a Qualys agent. See [Creating a Compute Scan Recipe with a Qualys Agent](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-qualys-agent.htm#create-host-recipe-qualys-agent "Create a Compute \(host\) scan recipe using your own Qualys license and then view the results in the Console or the Qualys dashboard.").
     * When updating an existing Compute scan recipe with a Qualys agent. See [Editing a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-recipe.htm#update_host_recipe "Edit an existing Compute \(host\) scan recipe.").
  2. In the Oracle Cloud Console, on the **Create scan recipe** or the **Edit compute scan recipe** pane, choose a vault in which to create the secret.
  3. Under **Define a secret** , choose **Create new**.
  4. (Optional) On the **Create secret** pane, create the secret in the compartment shown or choose another compartment.
  5. Enter a name and description for the secret.
  6. Choose an encryption key. Change the compartment, if necessary.
  7. In a separate browser window, sign in to the Qualys dashboard.
    1. Copy the license code and store it in a safe place.
    2. Generate a cloud agent activation key and enable OCI for the agent.
**Note** You must have a Qualys license to generate a cloud agent activation key. If you don't have a license code, you need to create one using the Qualys platform. To get a license, see the [prerequisites](https://docs.oracle.com/en-us/iaas/scanning/using/define-secret-for-scan-recipe.htm#define-secret-for-scan-recipe__prereq_qualys_license) at the beginning of this topic.
    3. Return to the Oracle Cloud Console.
  8. Select the secret template for your secret. The secret template that you select depends whether the secret is already Base64-encoded. If you know that the secret is already Base64-encoded, select **Base64**. If you know that the secret isn’t Base64-encoded, choose **Plain-Text**. Use the following examples as a guide: 
     * If the secret looks like the following example, select **Plain-Text** :
`{"cid":"qualys-customer-id","aid":"qualys-account-id", "pwsUrl":"https://qualys-endpoint/CloudAgent","pwsPort":"port-num"}`
     * If the secret looks like the following example, select **Base64** :
`eyJjaWQiOiJxdWFseXMtY3VzdG9tZXItaWQiLCJhaWQiOiJxdWF seXMtYWNjb3VudC1pZCIsInB3c1VybCI6Imh0dHBzOi8vcXVhbHlzLWVuZHBvaW50L0Nsb 3VkQWdlbnQiLCJwd3NQb3J0IjoicG9ydC1udW0ifQ==`
  9. In the **Create secret** window, add secret contents. Paste the secret contents for the license code that you’ve copied from the Qualys dashboard.
  10. Click **Create secret**.


Was this article helpful?
YesNo

