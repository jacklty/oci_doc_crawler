Updated 2025-01-22
# Listing Private Endpoints in Object Storage
View a list of the Object Storage private endpoints in a Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm)


  *     1. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Private Endpoints**.
The **Private Endpoints** list page opens. All existing Object Storage private endpoint resources in the selected compartment are displayed in a list table.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
  * Use the [oci os private-endpoint list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/list.html) command and required parameters to list the private endpoints in a compartment in Object Storage:
Command
CopyTry It
```
oci os private-endpoint list --compartment-id compartment_ocid [OPTIONS]
```

For example:
```
oci os private-endpoint list --compartment-id ocid1.tenancy.oc1..exampleuniqueID
        
{
 "data": [
  {
   "compartment-id": "ocid1.tenancy.oc1..exampleuniqueID",
   "created-by": "ocid1.user.region1..exampleuniqueID",
   "etag": "d8021157-3221-489d-ab8a-9e3fb36cdce4",
   "fqdns": {
    "additional-prefixes-fqdns": {},
    "prefix-fqdns": {
     "object-storage-api-fqdn": "pe1-MyNamespace.private.objectstorage.us-phoenix-1.oci.customer-oci.com",
     "s3-compatibility-api-fqdn": "pe1-MyNamespace.private.compat.objectstorage.us-phoenix-1.oci.customer-oci.com",
     "swift-api-fqdn": "pe1-MyNamespace.private.swiftobjectstorage.us-phoenix-1.oci.customer-oci.com"
    }
   },
   "lifecycle-state": "ACTIVE",
   "name": "pe1",
   "namespace": "MyNamespace",
   "prefix": "pe1",
   "time-created": "2024-06-20T06:33:56.866000+00:00",
   "time-modified": null
  },
  {
   "compartment-id": "ocid1.tenancy.oc1..exampleuniqueID",
   "created-by": "ocid1.user.region1..exampleuniqueID",
   "etag": "41958c18-7172-416c-8c22-7c3107c76cc0",
   "fqdns": {
    "additional-prefixes-fqdns": {},
    "prefix-fqdns": {
     "object-storage-api-fqdn": "pe2-MyNamespace.private.objectstorage.us-phoenix-1.oci.customer-oci.com",
     "s3-compatibility-api-fqdn": "pe2-MyNamespace.private.compat.objectstorage.us-phoenix-1.oci.customer-oci.com",
     "swift-api-fqdn": "pe2-MyNamespace.private.swiftobjectstorage.us-phoenix-1.oci.customer-oci.com"
    }
   },
   "lifecycle-state": "ACTIVE",
   "name": "pe2",
   "namespace": "MyNamespace",
   "prefix": "pe2",
   "time-created": "2024-06-20T06:40:42.865000+00:00",
   "time-modified": null
  }
 ]
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the following API operation:
```
GET n/object_storage_namespace/pe/
```



Was this article helpful?
YesNo

