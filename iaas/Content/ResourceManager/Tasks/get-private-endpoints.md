Updated 2025-01-23
# Getting a Private Endpoint's Details
Get details for a private endpoint in Resource Manager.
## Using a Terraform Configuration 🔗 
Get details for an existing private endpoint by adding code to reference it from a Terraform configuration.
For an example, see [Example Usage (Data Source: oci_resourcemanager_private_endpoint)](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/resourcemanager_private_endpoint#example-usage).
**Tip**
  * To create a stack that retrieves a Resource Manager private endpoint, use the **Resource Manager get private endpoint** [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.").
  * For example Terraform configurations that use Resource Manager private endpoints, see [Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm)


  * To get details for a private endpoint by using the Console, follow these steps.
On the **Private endpoints** list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
The details page opens and displays information about the private endpoint. Access the various resources associated with the private endpoint by selecting their links or tabs.
  * Use the `oci resource-manager private-endpoint get[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/get.html)` command to get a private endpoint.
Command
CopyTry It
```
oci resource-manager private-endpoint get --private-endpoint-id <private_endpoint_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/GetPrivateEndpoint) operation to get a private endpoint.


Was this article helpful?
YesNo

