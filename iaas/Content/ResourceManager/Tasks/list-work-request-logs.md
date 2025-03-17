Updated 2024-10-08
# Listing Logs for a Work Request
List logs for a Resource Manager work request.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)


  * In the Console, you can list logs for a work request related to a stack or a private endpoint.
#### Listing Logs for a Work Request Related to a Stack 🔗 
    1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Work requests**.
    3. Select the work request that you want.
The work request's details page opens.
    4. Select **Log messages**.
#### Listing Logs for a Work Request Related to a Private Endpoint 🔗 
    1. On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. On the private endpoint's details page, select **Work requests**.
    3. Select the work request that you want.
The work request's details page opens.
    4. Select **Log messages**.
  * Use the [oci resource-manager work-request list-work-request-logs](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/list-work-request-logs.html) command and required parameters to list logs for a work request:
Command
CopyTry It
```
oci resource-manager work-request list-work-request-logs --work-request-id <work_request_OCID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/ListWorkRequestLogs) operation to list logs for a work request.


Was this article helpful?
YesNo

