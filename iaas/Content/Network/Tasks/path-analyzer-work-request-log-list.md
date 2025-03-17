Updated 2023-05-30
# Listing Path Analysis Work Request Logs
View a list of network path analysis work request logs.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-log-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-log-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-log-list.htm)


  * This task is not available in the Console.
  * Use the [work-request-log list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/work-request-log/list.html) command and required parameters to view a paginated list of logs for the work request with the given ID.:
Command
CopyTry It
```
oci vn-monitoring work-request-log list --work-request-id work_request_OCID... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/WorkRequestLogEntry/ListWorkRequestLogs) operation to list path analyzer work request logs in a compartment.


Was this article helpful?
YesNo

