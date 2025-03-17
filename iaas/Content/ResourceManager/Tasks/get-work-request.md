Updated 2025-01-23
# Getting a Work Request's Details
Get details for a Resource Manager work request.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm)


  * In the Console, you can get details of a work request for a stack or for a private endpoint.
#### Getting Details for a Stack's Work Request 🔗 
    1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Work requests**.
    3. Select the work request that you want.
The details page opens and displays information about the work request.
#### Getting Details for a Private Endpoint's Work Request 🔗 
    1. On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. On the private endpoint's details page, select **Work requests**.
    3. Select the work request that you want.
The details page opens and displays information about the work request.
  * Use the [oci resource-manager work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/get.html) command and required parameters to get details for a work request:
Command
CopyTry It
```
oci resource-manager work-request get --work-request-id <work_request_OCID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/GetWorkRequest) operation to get details for a work request.


Was this article helpful?
YesNo

