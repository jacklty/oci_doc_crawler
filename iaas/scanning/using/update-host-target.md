Updated 2023-09-25
# Editing a Compute Target
Use the Console to update an existing Compute (host) scan target.
**Note** After you create an OCI agent or Qualys agent Compute scan recipe, don't change that recipe to change agents. Create another recipe.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-target.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the **Compartment** that contains your target.
    3. Click the **Hosts** tab if not already selected.
    4. Click the name of the target.
    5. Click **Edit**.
    6. Change any of these settings for the target.
       * **Name**
       * **Description**
       * **Scan recipe**
       * **Target compartment**
Avoid entering confidential information.
    7. Update the Compute instances for this target.
       * **All Compute instances in the selected target compartment and its subcompartments**
       * **Selected Compute instances in the selected target compartment** - Select individual Compute instances
You can't update a target with a compartment or a Compute instance that's already specified in another target. However, multiple targets can scan the same Compute instance.
    8. Click **Save changes**
    9. (Optional) Click **Tags** to manage the tags for this target.
If you have permissions to create a resource, you also have permissions to add free-form tags to that resource.
To add a defined tag, you must have permissions to use the tag namespace.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure if you should add tags, skip this option or ask your administrator. You can add tags later.
  * Use the [oci vulnerability-scanning host scan target update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/update.html) command and required parameters to update the compute (host) target identified by the target ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan target update [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [UpdateHostScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/UpdateHostScanTarget) operation to update the compute (host) target identified by the target ID.


Was this article helpful?
YesNo

