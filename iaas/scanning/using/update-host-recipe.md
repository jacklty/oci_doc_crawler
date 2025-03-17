Updated 2023-09-25
# Editing a Compute Scan Recipe
Edit an existing Compute (host) scan recipe.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-recipe.htm)


  * **Note** After you create an OCI agent or Qualys agent Compute scan recipe, don't change that recipe to change agents. Create another recipe.
    1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
    2. Select the compartment that contains the recipe.
    3. Click the **Hosts** tab if not already selected.
    4. Click the name of the recipe.
    5. Click **Edit**.
    6. Change any of the following settings for the recipe.
       * **Name**
Avoid entering confidential information.
       * **Public IP port scanning**
       * **Agent based scanning**
       * **CIS benchmark scanning** (for **OCI** agents)
       * **CIS benchmark profile** (for **OCI** agents)
       * **Enable file scans** (for **OCI** agents)
       * **Linux folders to scan** (for **OCI** agents)
Separate multiple folders by using semicolons.
       * **Windows folders to scan** (for **OCI** agents)
**Note** **Reserved for future use by Oracle.** File scans aren't available for the Windows operating system.
       * **Vault** (for **Qualys** agents)
       * **Secret** (for **Qualys** agents)
       * **File scan schedule**
       * **Schedule**
The Vulnerability Scanning agent checks the OS configuration of targets for vulnerabilities, such as missing patches. The agent can also check targets for the following information:
       * Compliance with industry-standard benchmarks published by the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/) (CIS)
       * Vulnerabilities in third-party applications within specific folders
The schedule controls how often the targets assigned to this recipe are scanned.
    7. Click **Save changes**.
    8. (Optional) Click the **Tags** tab to manage the tags for this recipe.
If you have permissions to create a resource, you also have permissions to add free-form tags to that resource.
To add a defined tag, you must have permissions to use the tag namespace.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure if you should add tags, skip this option or ask your administrator. You can add tags later.
  * Use the [oci vulnerability-scanning host scan recipe update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/update.html) command and required parameters to updates the host scan recipe identified by the recipe ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe update [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [UpdateHostScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/UpdateHostScanRecipe) operation to updates the host scan recipe identified by the recipe ID.


Was this article helpful?
YesNo

