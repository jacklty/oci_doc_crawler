Updated 2025-01-30
# Getting a Private Endpoint's Details in Object Storage
View the details of an Object Storage private endpoint.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-private-endpoint.htm)


  * On the **Private Endpoints** list page, select the Object Storage private endpoint that you want to work with. If you need help finding the list page or the Object Storage private endpoint, see [Listing Private Endpoints in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/list-private-endpoint.htm).
The details page shows information about the private endpoint, both general information and links to its resources.
  * Use the [oci os private-endpoint get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/get.html) command and required parameters to get the details of a private endpoint in Object Storage:
Command
CopyTry It
```
oci os private-endpoint get --pe-name private_endpoint_name [OPTIONS]
```

For example:
```
oci os private-endpoint get --pe-name pe1
        
{
 "data": {
  "access-targets": [
   {
    "bucket": "*",
    "compartment-id": "*",
    "namespace": "MyNamespace"
   }
  ],
  "additional-prefixes": [],
  "compartment-id": "ocid1.tenancy.oc1..exampleuniqueID",
  "created-by": "ocid1.user.region1..exampleuniqueID",
  "defined-tags": {},
  "etag": "017e1d8f-1013-477a-86a4-d4d03b473f74",
  "fqdns": {
   "additional-prefixes-fqdns": {},
   "prefix-fqdns": {
    "object-storage-api-fqdn": "pe1-MyNamespace.private.objectstorage.us-phoenix-1.oci.customer-oci.com",
    "s3-compatibility-api-fqdn": "pe1-MyNamespace.private.compat.objectstorage.us-phoenix-1.oci.customer-oci.com",
    "swift-api-fqdn": "pe1-MyNamespace.private.swiftobjectstorage.us-phoenix-1.oci.customer-oci.com"
   }
  },
  "freeform-tags": {},
  "id": "ocid1.privateendpoint.region1.sea.exampleuniqueID",
  "lifecycle-state": "ACTIVE",
  "name": "pe1",
  "namespace": "MyNamespace",
  "nsg-ids": [],
  "prefix": "pe1",
  "private-endpoint-ip": "10.0.0.2",
  "subnet-id": "ocid1.subnet.region1.sea.exampleuniqueID",
  "time-created": "2024-06-20T06:33:56.866000+00:00",
  "time-modified": "2024-06-20T06:36:01.820000+00:00"
 },
 "etag": "017e1d8f-1013-477a-86a4-d4d03b473f74"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the following API operation:
```
GET n/object_storage_namespace/pe/peName
```



Was this article helpful?
YesNo

