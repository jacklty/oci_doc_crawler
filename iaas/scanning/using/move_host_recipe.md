Updated 2023-09-25
# Moving a Compute Scan Recipe Between Compartments
Move a Compute (host) scan recipe from one compartment to another.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_recipe.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_recipe.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_recipe.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Scan Recipes**.
    2. Select the compartment that contains the recipe.
    3. Click the **Hosts** tab.
    4. Click the name of the recipe.
    5. Click **Move resource**.
    6. Choose the destination compartment.
    7. Click **Move resource**.
After you move the recipe to the new compartment, inherent policies apply immediately and affect access to the recipe through the Console. For more information, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
  * Use the [oci vulnerability-scanning host scan recipe change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/recipe/change-compartment.html) command and required parameters to move a host scan recipe into a different compartment:
Command
CopyTry It
```
oci vulnerability-scanning host scan recipe change-compartment [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ChangeHostScanRecipeCompartment](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanRecipe/ChangeHostScanRecipeCompartment) operation to move a host scan recipe into a different compartment.


Was this article helpful?
YesNo

