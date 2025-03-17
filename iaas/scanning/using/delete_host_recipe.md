Updated 2023-09-25
# Deleting a Compute Scan Recipe
Delete a Compute (host) scan recipe.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_recipe.htm)


  * To delete a scan recipe, it must not be associated with any scan targets. See [Deleting a Container Image Target](https://docs.oracle.com/en-us/iaas/scanning/using/delete-image-target.htm#delete_target "Delete a target.").
    1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
    2. Select the compartment that contains the recipe.
    3. Click the **Hosts** tab.
    4. Click the name of the recipe.
    5. Click **Delete**.
    6. When prompted for confirmation, click **Delete**.
  * Use the [oci vulnerability-scanning host scan recipe delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/delete.html) command and required parameters to delete the host scan recipe identified by the recipe ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe delete [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DeleteHostScanRecipe](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/DeleteHostScanRecipe) operation to delete the host scan recipe identified by the recipe ID.


Was this article helpful?
YesNo

