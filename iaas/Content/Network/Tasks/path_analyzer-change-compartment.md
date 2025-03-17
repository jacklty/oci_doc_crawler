Updated 2025-02-18
# Moving a Path Analysis Test to a different compartment
You can move a network path analysis to a different compartment in the Network Path Analyzer service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-change-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-change-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-change-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
    2. Find the path analysis test that you want to move, select its the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Resource**.
    3. Select the destination compartment from the list, then select **Move Resource**.
  * Use the [path-analyzer-test change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/change-compartment.html) command and required parameters to move a network path analyzer test to a different compartment:
Command
CopyTry It
```
oci vn-monitoring path-analyzer-test change-compartment --path-analyzer-test-id path_analyzer_test_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangePathAnalyzerTestCompartment](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTest/ChangePathAnalyzerTestCompartment) operation to move a path analyzer test to a different compartment.


Was this article helpful?
YesNo

