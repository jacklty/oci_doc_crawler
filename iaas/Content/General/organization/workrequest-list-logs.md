Updated 2025-02-11
# Listing Work Request Logs
List all work request logs.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-logs.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-logs.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-logs.htm)


  * See [Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-get.htm#workrequest_get "Get the details of a work request in Organization Management.") for more information on viewing work request details. 
From the work request details page, select **Log Messages** to view the list of work request logs.
  * Use the [oci organizations work-request-log list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/work-request-log/list.html) command and required parameters to return a paginated list of logs for a particular work request:
Command
CopyTry It
```
oci organizations work-request-log list --work-request-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/organizations/latest/WorkRequestLogEntry/ListWorkRequestLogs) operation to return a paginated list of logs for a particular work request.


Was this article helpful?
YesNo

