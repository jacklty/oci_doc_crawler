Updated 2023-09-25
# Getting a Compute Target's Details
View a Compute target's details.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-target.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the compartment that contains the target.
    3. Click the **Hosts** tab if not already selected.
    4. Click the name of the target.
    5. In the **Compute instances** table, click the name of a specific instance to view its details.
  * Use the [oci vulnerability-scanning host scan target get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/get.html) command and required parameters to retrieve a compute (host) target identified by the target ID:
Command
CopyTry It
```
oci vulnerability-scanning host scan target get --host-scan-target-id <target_ocid>
```

For example:
```
oci vulnerability-scanning host scan target get --host-scan-target-id ocid1.vsshostscantarget.oc1..exampleuniqueID
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetHostScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/GetHostScanTarget) operation to retrieve a compute (host) target identified by the target ID.


Was this article helpful?
YesNo

