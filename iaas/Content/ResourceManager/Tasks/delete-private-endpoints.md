Updated 2025-01-07
# Deleting a Private Endpoint
Delete a Resource Manager private endpoint.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-private-endpoints.htm)


  *     1. On the **Private endpoints** list page, find the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the private endpoint, select **Delete private endpoint**.
    3. When prompted, confirm the deletion.
  * Use the `oci resource-manager private-endpoint delete[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/delete.html)` command to delete a private endpoint.
Command
CopyTry It
```
oci resource-manager private-endpoint delete --private-endpoint-id <private_endpoint_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [DeletePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/DeletePrivateEndpoint) operation to delete a private endpoint.


Was this article helpful?
YesNo

