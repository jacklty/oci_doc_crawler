Updated 2025-02-18
# Deleting a Path Analysis Test
Delete a network path analysis test in the Network Path Analyzer service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-deleting_test.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-deleting_test.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-deleting_test.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
    2. Find the path analysis test that you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    3. Confirm the deletion.
  * Use the [path-analyzer-test delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/delete.html) command and required parameters to delete a path analyzer test:
Command
CopyTry It
```
oci vn-monitoring path-analyzer-test delete --path-analyzer-test-id path_analyzer_test_OCID... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeletePathAnalyzerTest](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTest/DeletePathAnalyzerTest) operation to delete a path analyzer test.


Was this article helpful?
YesNo

