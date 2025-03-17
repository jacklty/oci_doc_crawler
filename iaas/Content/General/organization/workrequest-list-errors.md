Updated 2025-02-11
# Listing Work Request Errors
List all work request errors.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-errors.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-errors.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-errors.htm)


  * See [Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-get.htm#workrequest_get "Get the details of a work request in Organization Management.") for more information on viewing work request details. 
From the work request details page, select **Error Messages** to view the list of work request errors.
  * Use the [oci organizations work-request-error list-errors](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/work-request-error/list-errors.html) command and required parameters to return a paginated list of errors for a particular work request:
Command
CopyTry It
```
oci organizations work-request-error list-errors --work-request-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/organizations/latest/WorkRequestError/ListWorkRequestErrors) operation to return a paginated list of errors for a particular work request.


Was this article helpful?
YesNo

