Updated 2025-01-23
# Moving a Private Endpoint to a Different Compartment
Move a Resource Manager private endpoint to another compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm)


  *     1. On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. On the private endpoint's details page, select **Move resource**.
    3. In the **Move resource** panel, select the destination compartment from the list.
    4. Select **Move resource**.
  * Use the `oci resource-manager private-endpoint change-compartment[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/change-compartment.html)` command to move a private endpoint to another compartment.
Command
CopyTry It
```
oci resource-manager private-endpoint change-compartment --compartment-id <compartment_ocid> --private-endpoint-id <private_endpoint_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ChangePrivateEndpointCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/ChangePrivateEndpointCompartment) operation to move a private endpoint to another compartment.


Was this article helpful?
YesNo

