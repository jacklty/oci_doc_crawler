Updated 2023-12-08
# Getting the Reachable IP Address for a Private Endpoint
Get the reachable IP address of a private endpoint in Resource Manager.
**Note** To troubleshoot error code 431 related to this request, see [Error Code 431 When Getting Reachable IP Address](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/431-reachable.htm#top "Troubleshoot error code 431 when getting a reachable IP address for a private endpoint.").
## Using a Terraform Configuration 🔗 
Get reachable IP addresses by referencing them from Terraform configurations.
Add code to the Terraform configuration that references an existing reachable IP address.
For an example, see [Example Usage (Data Source: oci_resourcemanager_private_endpoint_reachable_ip)](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/resourcemanager_private_endpoint_reachable_ip#example-usage).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm)


  * This task can't be performed using the Console.
  * Use the `oci resource-manager private-endpoint get-reachable-ip[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/get-reachable-ip.html)` command to get a reachable IP address for a private endpoint.
Command
CopyTry It
```
oci resource-manager private-endpoint get-reachable-ip --private-endpoint-id <private_endpoint_ocid> --private-ip <ip_address>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetReachableIp](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ReachableIp/GetReachableIp) operation to get the reachable IP address of a private endpoint.


Was this article helpful?
YesNo

