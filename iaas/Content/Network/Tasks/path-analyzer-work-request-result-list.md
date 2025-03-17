Updated 2023-05-30
# Listing Path Analysis Work Request Results
View a list of results for a successful path analysis work request.
Returns a (paginated) list of results for a successful work request. This information is used to build the final report output.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-result-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-result-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-work-request-result-list.htm)


  * This task is not available in the Console.
  * Use the [work-request-result list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/work-request-result/list.html) command and required parameters to view a paginated list of results for the work request with the given ID.:
Command
CopyTry It
```
oci vn-monitoring work-request-result list --work-request-id work_request_OCID... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestResults](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/WorkRequestResult/ListWorkRequestResults) operation to list path analyzer work request results in a compartment.


Was this article helpful?
YesNo

