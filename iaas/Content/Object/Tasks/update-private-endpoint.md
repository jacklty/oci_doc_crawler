Updated 2025-01-30
# Editing a Private Endpoint in Object Storage
Update an Object Storage private endpoint's configuration.
You can update the following settings for a private endpoint:
  * Access targets
  * Tagging


You can't update the following:
  * The compartment where the private endpoint resides.
  * Private endpoint name
  * DNS prefix
  * Network security group


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm)


  *     1. On the **Private Endpoints** list page, select the Object Storage private endpoint that you want to work with. If you need help finding the list page or the Object Storage private endpoint, see [Listing Private Endpoints in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/list-private-endpoint.htm).
    2. From the **Actions** menu for the private endpoint, select **Edit**.
    3. Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#top "Create a private endpoint to reach Object Storage using a private IP address within your VCN without accessing the public internet.").
    4. Select **Save Changes**.
  * Use the [oci os private-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/update.html) command and required parameters to edit a private endpoint in Object Storage:
```
oci os private-endpoint update --pe-name private_endpoint_name --name private_endpoint_name --access-targets access_targets [OPTIONS]
```

where `access_targets` lists one or more access targets being updated to the new settings using the following syntax:
```
'[{"namespace":"namespace", "compartmentId":"compartment_ocid", "bucket":"bucket"}]'
```

For example:
```
oci os private-endpoint update --pe-name pe1 --name pe1 --access-targets '[{"namespace":"MyNamespace", "compartmentId":"ocid1.tenancy.oc1..exampleuniqueID", "bucket":"*"}]'
{
 "opc-work-request-id": "f52e20e6-2c21-4544-be98-c7f9b590c9db"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the following API operation:
```
POST n/object_storage_namespace/pe/peName
```



Was this article helpful?
YesNo

