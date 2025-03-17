Updated 2023-09-25
# Moving a Compute Target Between Compartments
Move a compute (host) target into a different compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_target.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the **Compartment** that contains your target.
    3. Click the **Hosts** tab.
    4. Click the name of the target.
    5. Click **Move resource**.
    6. Choose the destination compartment.
    7. Click **Move resource**.
  * Use the [oci vulnerability-scanning host scan target change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/change-compartment.html) command and required parameters to move a compute (host) target into a different compartment:
Command
CopyTry It
```
oci vulnerability-scanning host scan target change-compartment [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ChangeHostScanTargetCompartment](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/ChangeHostScanTargetCompartment) operation to delete the compute (host) target identified by the target ID.


Was this article helpful?
YesNo

