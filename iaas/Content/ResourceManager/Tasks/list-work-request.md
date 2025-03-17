Updated 2024-10-08
# Listing Work Requests
List Resource Manager work requests.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm)


  * In the Console, you can list work requests for a stack or a private endpoint.
#### Listing Work Requests for a Stack 🔗 
    1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Work requests**.
#### Listing Work Requests for a Private Endpoint 🔗 
    1. On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. On the private endpoint's details page, select **Work requests**.
  * Use the [oci resource-manager work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/list.html) command and required parameters to list work requests:
Command
CopyTry It
```
oci resource-manager work-request list --compartment-id <compartment_OCID>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/ListWorkRequests) operation to list work requests.


Was this article helpful?
YesNo

