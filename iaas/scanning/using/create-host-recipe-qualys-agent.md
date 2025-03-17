Updated 2023-09-25
# Creating a Compute Scan Recipe with a Qualys Agent
Create a Compute (host) scan recipe using your own Qualys license and then view the results in the Console or the Qualys dashboard.
[Before You Begin:](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-qualys-agent.htm)
Complete the following prerequisites before creating a Compute scan recipe with a Qualys agent.
  1. **Create an account in Qualys with a license to use VMDR.** You must have a Qualys account with a license to use VMDR before you can create a Compute scan recipe with a Qualys agent. See the [Qualys VMDR](https://www.qualys.com/forms/vmdr/) sign-up page to get started. After you have a license, you must generate a Cloud Agent Activation Key, and enable OCI for the agent. Perform these tasks using the Qualys platform. See the [Qualys Cloud Platform](https://www.qualys.com/documentation/) documentation for instructions.
  2. **Create a dynamic group.** Create a dynamic group of instances that you want to scan. See [Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).
  3. **Write policies.** Write Agent-Based Standard Policies and Agent-Based Qualys Policies. See [Required IAM Policy for Compute Scanning Recipes](https://docs.oracle.com/en-us/iaas/scanning/using/required-iam-policy-host-scan.htm#required_iam_policy_host_scan "To use Oracle Cloud Infrastructure, you must be granted the required type of access in a written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool.").
  4. **Create a vault.** Create a vault to store your Qualys license information. See [Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm).
  5. **Define a secret.** Create a secret to store your Qualys license information in the vault. See [Defining a Secret for a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/define-secret-for-scan-recipe.htm#define-secret-for-scan-recipe "Create a secret for a Compute \(host\) scan recipe to store the Qualys license information.").
  6. Review the following important information about Qualys scans:
     * After you create an OCI agent or Qualys agent Compute scan recipe, don't change that recipe to change agents. Create another recipe.
     * Qualys performs scans OCI hosts every four hours. Scanning OCI hosts count toward your Qualys license usage. Contact Qualys for any issues with your license or usage.
     * Viewing Qualys scan results:
       * View Qualys scan results in the Qualys portal about four hours after you’ve created the new scan target.
       * View Qualys scan results in the OCI Console within 12 hours of creating the new scan target.


To create a Compute scan recipe with a Qualys agent, complete the following steps:
  1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
  2. Open the **Create scan recipe** panel in one of the following ways:
     * If no scan recipes exist, the **Welcome** page is displayed, which includes an introduction to the service. Click **Create scan recipe** , and then select the compartment in which you want to create the recipe.
     * If scan recipes exist, select the compartment in which you want to create the recipe, Click the **Hosts** tab, and then click **Create**.
  3. Verify that the recipe type is **Compute**.
  4. Enter a name for the recipe.
Avoid entering confidential information.
  5. (Optional) Change the compartment in which the recipe is created.
  6. Select the level of public IP port scanning for this recipe.
     * **Standard** : Check the 1,000 most common port numbers.
     * **Light** (default): Check the 100 most common port numbers.
     * **None** : Don’t check for open ports.
The Vulnerability Scanning service uses a network mapper that searches your **public IP addresses**. See [Ports that are Scanned](https://docs.oracle.com/en-us/iaas/scanning/using/port-numbers.htm#port_numbers "Lists the top 100 and top 1000 ports that Vulnerability Scanning scans.").
  7. Select the **Qualys** agent. 
  8. Select a **Vault** in the current compartment. Change the compartment if necessary.
  9. Choose a defined secret from the vault or create a new one. See [Defining a Secret for a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/define-secret-for-scan-recipe.htm#define-secret-for-scan-recipe "Create a secret for a Compute \(host\) scan recipe to store the Qualys license information."). 
  10. In **Schedule** , select a schedule for public IP port scanning.
The schedule controls how often the targets assigned to this recipe are scanned. Choose **Daily** or one of the **Weekly** values.
**Note**
To configure the Qualys agent scanning schedule or any other Qualys agent configurations, go to the Qualys dashboard.
  11. (Optional) Click **Show advanced options** to assign tags to the recipe.
If you have permissions to create a resource, you also have permissions to add free-form tags to that resource.
To add a defined tag, you must have permissions to use the tag namespace.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure if you should add tags, skip this option or ask your administrator. You can add tags later.
  12. Save the recipe using one of the following methods.
    1. Click **Create scan recipe** to create the recipe in the Vulnerability Scanning service.
    2. Click **Save as stack** to manage the stack through the Resource Manager service. On the **Save as stack** window, complete the fields, and then click **Save**. For more information about stacks, see [Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).


After creating a recipe, you can create scan targets and associate them with the recipe. See [Creating a Compute Target](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm#create_host_target "Create a Compute \(host\) scan target.").
Was this article helpful?
YesNo

