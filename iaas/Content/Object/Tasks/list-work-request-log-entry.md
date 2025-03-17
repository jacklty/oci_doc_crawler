Updated 2024-03-04
# Listing an Object Storage Work Request's Logs
View a list of the logs for an Object Storage work request.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-log-entry.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-log-entry.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-log-entry.htm)


  * This task can't be performed using the OCI Console.
  * Use the [oci os work-request-log-entry list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/work-request-log-entry/list.html) command and required parameters to list the logs of a Object Storage work request:
Command
CopyTry It
```
oci os work-request-log-entry list --work-request-id work_request_id [OPTIONS]
```

List the work requests in a compartment to get their IDs. See [Listing Work Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm#top "View a list of the Object Storage work requests in a Oracle Cloud Infrastructure compartment.") for more information.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequestLogEntry/ListWorkRequestLogs) operation to list the logs of a Object Storage work request.


Was this article helpful?
YesNo

