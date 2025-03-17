Updated 2023-09-25
# Creating a Compute Scan Recipe with an OCI Agent
Create a Compute (host) scan recipe using the OCI agent included with your Oracle Cloud Infrastructure account and then view the results in the Console.
The OCI agent tests compliance with industry-standard benchmarks published by the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/).
**Important**
  * Before you begin, review the policies documentation for Vulnerability Scanning. See [Required IAM Policies for Scanning](https://docs.oracle.com/en-us/iaas/scanning/using/required_iam_policies_scanning.htm#required_iam_policies_scanning "Create IAM policies to control who has access to Oracle Cloud Infrastructure Vulnerability Scanning Service resources, and to control the type of access for each group of users.").
  * After you create an OCI agent or Qualys agent Compute scan recipe, don't change that recipe to change agents. Create another recipe.


To create a Compute scan recipe with an OCI agent, complete the following steps:
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
  7. Select the **OCI** agent. 
  8. (Optional) Configure **CIS benchmark scanning**.
    1. Disable **CIS benchmark scanning** if you don't want the agent to check targets for compliance with industry-standard benchmarks published by the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/) (CIS).
    2. If **CIS benchmark scanning** is enabled, then select the **CIS benchmark profile** for this recipe.
       * **Strict** : If more than 20% of the CIS benchmarks fail, then the target is assigned a risk level of `Critical`.
       * **Medium** (default): If more than 40% of the CIS benchmarks fail, then the target is assigned a risk level of `High`.
       * **Lightweight** : If more than 80% of the CIS benchmarks fail, then the target is assigned a risk level of `High`.
  9. (Optional) Select **Enable file scans** to scan specific folders for vulnerabilities in third-party applications.
**Note** The Vulnerability Scanning service checks for vulnerabilities only in `log4j` and `spring4shell`.
    1. For **Linux folders to scan** , specify at least one folder to scan on target Linux hosts.
Separate multiple folders using semicolons.
    2. For **Windows folders to scan** , specify folders to scan on target Windows hosts.
**Note** **Reserved for future use by Oracle.** File scans aren't available for the Windows OS.
Separate multiple folders using semicolons.
    3. Configure a **File scan schedule**.
This schedule controls how often the files on the targets assigned to this recipe are scanned.
Choose from **Bi-weekly** or **Monthly**.
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

