Updated 2025-02-21
# Deleting a Capture Filter
Delete a capture filter.
**Important** You can't delete a capture filter if it's associated with a VTAP or Flow Log.
For more information about capture filters and feature overviews, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.") and [Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/vcn-flow-logs.htm#vcn_flow_logs "Use VCN flow logs to capture network traffic information to support monitoring and security needs.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Capture filters**.
    2. Find the capture filter that you want to delete, select its the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    3. Confirm the deletion.
  * Use the [capture-filter delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/delete.html) command and required parameters to delete a capture filter:
Command
CopyTry It
```
oci network capture-filter delete --capture-filter-id capture-filter_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteCaptureFilters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/DeleteCaptureFilter) operation to delete a capture filter.


Was this article helpful?
YesNo

