Updated 2023-09-25
# Getting a Compute Scan Recipe's Details
Get a Compute (host) scan recipe's details.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-recipe.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
    2. Select the compartment that contains the recipe.
    3. Click the **Hosts** tab.
    4. Click the name of the recipe to view the details.
  * Use the [oci vulnerability-scanning host scan recipe get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/get.html) command and required parameters to retrieve a host scan recipe identified by the recipe ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe get --host-scan-recipe-id <recipe_ocid>
```

For example:
```
oci vulnerability-scanning host scan recipe get --host-scan-recipe-id ocid1.vsshostscanrecipe.oc1..exampleuniqueID
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetHostScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/GetHostScanRecipe) operation to retrieve a host scan recipe identified by the recipe ID.


Was this article helpful?
YesNo

