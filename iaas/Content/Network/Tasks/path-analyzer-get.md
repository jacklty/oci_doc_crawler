Updated 2025-02-18
# Getting a Path Analysis Test's Details
View the details for a network path analysis test in Network Path Analyzer.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
All saved path analyzer tests are listed.
    2. Select the name of a saved analysis to view its details.
The details page contains information about the network path analysis, both general information and links to its resources. Some items on the page are read-only, while other items let you edit and update the path analyzer test's configuration. See [Editing a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm#top "Update the configuration information of a path analysis test.").
  * Use the [path-analyzer-test get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/get.html) command and required parameters to view details about a path analyzer test:
Command
CopyTry It
```
oci vn-monitoring path-analyzer-test get --path_analyzer_test-id path_analyzer_test_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetPathAnalyzerTest](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTest/GetPathAnalyzerTest) operation to view details about a path analyzer test.


Was this article helpful?
YesNo

