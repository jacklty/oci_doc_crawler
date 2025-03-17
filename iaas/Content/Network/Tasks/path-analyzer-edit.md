Updated 2025-02-18
# Editing a Path Analysis Test
Update the configuration information of a path analysis test.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
All saved path analyzer tests are listed.
    2. Select the name of a saved analysis to view its details.
    3. Select **Edit**.
    4. Make changes, and then select **Save**. For information about the options, see [Creating a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-creating_test.htm#top "Use the Network Path Analyzer service to create a test that analyzes the configuration of a virtual network. See how the paths between the source and the destination function or fail.").
  * Use the [path-analyzer-test update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/update.html) command and required parameters to edit a path analyzer test:
Command
CopyTry It
```
oci vn-monitoring path-analyzer-test update --path_analyzer_test-id path_analyzer_test_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePathAnalyzerTest](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTest/UpdatePathAnalyzerTest) operation to edit a path analysis test.


Was this article helpful?
YesNo

