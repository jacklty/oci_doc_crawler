Updated 2025-02-18
# Running a Path Analysis Test
Use the Network Path Analyzer service to run a test after it has been saved, or immediately after it has been configured.
**Important** An update on February 12, 2024, requires that any on-premises source or destination IP address must also have the **This IP address is an on-premises endpoint** checkbox selected. If you created a path analysis test with an on-premises IP address before this date that doesn't have the checkbox selected, you must edit the test to select the checkbox, or the test fails See [Editing a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm#top "Update the configuration information of a path analysis test.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-running_test.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-running_test.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-running_test.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
    2. Select the name of the saved analysis test that you want to run.
The details page shows the parameters configured for the test. If you need to edit any of the parameters before running the test, select **Edit** and then save your changes. 
    3. On the details page, select **Analyze**. 
Running the analysis might take up to a minute to complete. Traffic doesn't need to traverse the network. Network Path Analyzer collects and analyzes the network configuration to see how the paths between the source and the destination function or fail. 
After the test runs, the **Discovered paths** section of the details page shows up to eight possible paths discovered between source and destination. Each path tab shows a visualization of the forward path and (if configured) the return path for traffic between the source and destination. 
The diagram for a successful test shows green arrows representing each successful hop between nodes in the overall path. The path status is **Reachable**.
An unsuccessful test shows green arrows representing each successful hop in the overall path, and a red arrow for the hop or network segment that's unreachable.
    4. Select **View diagram information** to see details about each hop. You can see whether a hop failed because of a misconfiguration in a specific node's routing or security configuration. You can also expand the row for a particular hop to get more details. 
Routing information for the hop shows one of the following states:
       * **Forwarded** : The relevant route table allows the traffic
       * **No route** : The route table doesn't explicitly allow the traffic or security blocks traffic
       * **Indeterminate** : The route table can't be analyzed. 
If the node is an OCI resource, a direct link to the relevant route rule is provided. Indeterminate states can be caused by the Console account not having the required permissions, or because the node routing information is unavailable for any other reason.
Security information for the hop shows one of the following states: **Allowed** , **Blocked** , or **Indeterminate**. If the node is an OCI resource, a direct link to the relevant security list or rule is provided. Indeterminate states can be caused by the Console account not having the required permissions, or when the node security information is unavailable for any reason.
  * Use the [get-path-analysis-persisted](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analysis/get-path-analysis-persisted.html) command and required parameters to run a path analyzer test:
Command
CopyTry It
```
oci vn-monitoring path-analysis get-path-analysis-persisted --path-analyzer-test-id path_analyzer_test_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetPathAnalysis](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalysisWorkRequestResult/GetPathAnalysis) operation to run a path analyzer test.


Was this article helpful?
YesNo

