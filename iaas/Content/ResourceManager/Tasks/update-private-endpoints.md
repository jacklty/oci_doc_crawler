Updated 2024-10-08
# Updating a Private Endpoint
Update a private endpoint in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoints.htm)


  *     1. On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. On the private endpoint's details page, select **Edit**.
    3. On the **Edit private endpoint** panel, update the values as needed.
For more information about the fields, see [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#top "Create a private endpoint in Resource Manager.").
    4. Select **Edit**.
  * Use the `oci resource-manager private-endpoint update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/update.html)` command to update a private endpoint. The following example updates the display name of the private endpoint.
Command
CopyTry It
```
oci resource-manager private-endpoint update --display-name <text> --private-endpoint-id <private_endpoint_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/UpdatePrivateEndpoint) operation to update a private endpoint.


Was this article helpful?
YesNo

