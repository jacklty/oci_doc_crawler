Updated 2023-05-30
# Getting a Path Analysis Work Request's Details
View details about a path analysis work request.
Work requests allow you to monitor long-running operations. When you launch such an operation, the service spawns a **work request**. A work request is an activity log that enables you to track each step in the operation's progress. Each work request has an OCID (Oracle Cloud Identifier) that allows you to interact with it programmatically and use it for automation. Work requests are retained for 12 hours.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-get.htm)


  * This task is not available in the Console.
  * Use the [work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/work-request/get.html) command and required parameters to view details for a path analyzer work request:
Command
CopyTry It
```
oci vn-monitoring work-request get --work-request-id work_request_OCID... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/WorkRequest/GetWorkRequest) operation to view details about a path analyzer work request.


Was this article helpful?
YesNo

