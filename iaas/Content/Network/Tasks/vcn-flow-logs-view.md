Updated 2025-02-18
# Viewing Flow Logs
View flow logs from the Network Command Center.
You can view captured logging information from the Network Command Center, or from the [Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). This page documents how to view flow logs from the Network Command Center.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Flow logs**.
    2. Under **List scope** , select the compartment that contains the flow log.
    3. Under **Filter** , select a lifecycle state and log group that contains the flow log.
    4. Select the flow log to view details about its configuration
    5. To view the captured flow log data, select **To view more logging data, click here**.
  * Use the [oci logging log list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/list.htm) command and required parameters to list the logs in a log group.
Command
CopyTry It
```
oci logging log list --log-group-id log_group_ocid [OPTIONS]
```

For a complete list of parameters and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListLogs](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSummary/ListLogs) operation to list the logs in a log group.


Was this article helpful?
YesNo

