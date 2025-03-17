Updated 2023-09-25
# Listing the Compute Instances for a Target
View the Compute instances (hosts) associated with an existing target.
  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/view-host-target-instances.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/view-host-target-instances.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/view-host-target-instances.htm)


  *     1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the **Compartment** that contains your target.
    3. Click the **Hosts** tab if not already selected.
    4. Click the name of the target.
The **Compute instances** table displays.
  * Use the [oci vulnerability-scanning host scan target list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/list.html) command and required parameters to retrieve a list of HostScanTargetSummary objects in a compartment:
Command
CopyTry It
```
oci vulnerability-scanning host scan target list --compartment-id <compartment_ocid>
```

For example:
```
oci vulnerability-scanning host scan target list --compartment-id ocid1.compartment.oc1..exampleuniqueID
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListHostScanTargets](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/ListHostScanTargets) operation to retrieve a list of HostScanTargetSummary objects in a compartment.


Was this article helpful?
YesNo

