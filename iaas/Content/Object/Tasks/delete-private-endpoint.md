Updated 2025-01-30
# Deleting a Private Endpoint from Object Storage
Remove an Object Storage private endpoint from your Oracle Cloud Infrastructure tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm)


  *     1. On the **Private Endpoints** list page, select the Object Storage private endpoint that you want to work with. If you need help finding the list page or the Object Storage private endpoint, see [Listing Private Endpoints in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/list-private-endpoint.htm).
    2. From the **Actions** menu for the private endpoint, select **Delete**.
    3. When prompted, confirm the deletion.
The Object Storage private endpoint you deleted no longer appears in the list after it's deletion is complete.
  * Use the [oci os private-endpoint delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/delete.html) command and required parameters to delete a private endpoint from Object Storage:
Command
CopyTry It
```
oci os private-endpoint delete --pe-name private_endpoint_name [OPTIONS]
```

for example:
```
oci os private-endpoint delete --pe-name pe1
Are you sure you want to delete this resource? [y/N]: y
{
 "opc-work-request-id": "b6fc93fd-08cc-47d3-bae2-511ffc27913a"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the following API operation:
```
DELETE n/object_storage_namespace/pe/peName
```



Was this article helpful?
YesNo

