Updated 2023-09-25
# Deleting a Compute Target
Delete a compute (host) target.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_target.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the **Compartment** that contains your target.
    3. Click the **Hosts** tab for the type of target that you want to delete.
    4. Click the name of the target.
    5. Click **Delete**.
    6. When prompted for confirmation, click **Delete**.
  * Use the [oci vulnerability-scanning host scan target delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/delete.html) command and required parameters to delete the compute (host) target identified by the target ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan target delete [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DeleteHostScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/DeleteHostScanTarget) operation to delete the compute (host) target identified by the target ID.


Was this article helpful?
YesNo

