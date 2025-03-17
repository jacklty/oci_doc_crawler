Updated 2023-09-25
# Creating a Compute Scan Recipe
Create a Compute (host) scan recipe with or without a host agent.
You have the following options for creating a Compute scan recipe:
  * To create a recipe without an agent, follow the instructions in this topic.
  * To create a recipe with a free OCI agent, see [Creating a Compute Scan Recipe with an OCI Agent](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-oci-agent.htm#create-host-recipe-oci-agent "Create a Compute \(host\) scan recipe using the OCI agent included with your Oracle Cloud Infrastructure account and then view the results in the Console.").
  * To create a recipe with a Qualys agent using your Qualys license, see [Creating a Compute Scan Recipe with a Qualys Agent](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-qualys-agent.htm#create-host-recipe-qualys-agent "Create a Compute \(host\) scan recipe using your own Qualys license and then view the results in the Console or the Qualys dashboard.").


**Important**
  * Before you begin, review the policies documentation for Vulnerability Scanning. See [Required IAM Policies for Scanning](https://docs.oracle.com/en-us/iaas/scanning/using/required_iam_policies_scanning.htm#required_iam_policies_scanning "Create IAM policies to control who has access to Oracle Cloud Infrastructure Vulnerability Scanning Service resources, and to control the type of access for each group of users.").
  * After you create an OCI agent or Qualys agent Compute scan recipe, don't change that recipe to change agents. Create another recipe.


  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe.htm)


  * To create a Compute scan recipe without an agent, complete the following steps:
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
    7. Clear the **Agent based scanning** check box. Disabling agent based scanning means that you don't want to activate the Vulnerability Scanning agent plugin on the targets assigned to this recipe.
The Vulnerability Scanning agent runs on the selected targets and checks the OS configuration of targets for vulnerabilities, such as missing patches.
If you enable both agent based scanning and public IP port scanning, the agent also checks for open ports that aren’t accessible from public IP addresses.
**Note** If you disable both **Public IP port scanning** and **Agent based scanning** in this recipe, then the Vulnerability Scanning service doesn't scan any targets assigned to this recipe.
    8. In **Schedule** , select a schedule for public IP port scanning.
The schedule controls how often the targets assigned to this recipe are scanned. Choose **Daily** or one of the **Weekly** values.
**Note**
To configure the Qualys agent scanning schedule or any other Qualys agent configurations, go to the Qualys dashboard.
    9. (Optional) Click **Show advanced options** to assign tags to the recipe.
If you have permissions to create a resource, you also have permissions to add free-form tags to that resource.
To add a defined tag, you must have permissions to use the tag namespace.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure if you should add tags, skip this option or ask your administrator. You can add tags later.
    10. Save the recipe using one of the following methods.
      1. Click **Create scan recipe** to create the recipe in the Vulnerability Scanning service.
      2. Click **Save as stack** to manage the stack through the Resource Manager service. On the **Save as stack** window, complete the fields, and then click **Save**. For more information about stacks, see [Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
After creating a recipe, you can create scan targets and associate them with the recipe. See [Creating a Compute Target](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm#create_host_target "Create a Compute \(host\) scan target.").
  * Use the [oci vulnerability-scanning host scan recipe create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/create.html) command and required parameters to create a new host scan recipe:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe create --display-name <name> --compartment-id <compartment_ocid> --agent-settings '{"scanLevel": "<agent_scan_level>"}' --cis-benchmark-settings '{"scanLevel": "<CIS_scan_level>"}' --port-settings '{"scanLevel": "<port_scan_level>"}' --schedule '{"type":"<daily_or_weekly>"}'
```

For example:
```
oci vulnerability-scanning host scan recipe create --display-name MyRecipe --compartment-id ocid1.compartment.oc1..exampleuniqueID --agent-settings '{"scanLevel": "STANDARD"}' --cis-benchmark-settings '{"scanLevel": "MEDIUM"}' --port-settings '{"scanLevel": "STANDARD"}' --schedule '{"type":"DAILY"}'
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateHostScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/CreateHostScanRecipe) operation to create a new host scan recipe.
**Note**
The `HostEndpointProtectionSettings` have no effect and are reserved for future use.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm).


Was this article helpful?
YesNo

