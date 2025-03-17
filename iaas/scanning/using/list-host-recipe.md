Updated 2023-09-25
# Listing Compute Scan Recipes
View a list of Compute (host) scan recipes for a compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/list-host-recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/list-host-recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/list-host-recipe.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
    2. Select the compartment that contains the recipes.
    3. Click the **Hosts** tab.
A list of the recipes for that compartment is displayed in a table. 
  * Use the [oci vulnerability-scanning host scan recipe list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/list.html) command and required parameters to retrieve a list of host scan recipes in a compartment:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe list --compartment-id <compartment_ocid>
```

For example:
```
oci vulnerability-scanning host scan recipe list --compartment-id ocid1.compartment.oc1..exampleuniqueID
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListHostScanRecipes](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/ListHostScanRecipes) operation to retrieve a list of host scan recipes in a compartment.


Was this article helpful?
YesNo

