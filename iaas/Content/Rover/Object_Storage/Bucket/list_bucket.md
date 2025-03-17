Updated 2024-10-09
# Listing Buckets for Roving Edge Infrastructure
Describes how to list the object storage buckets on your Roving Edge Infrastructure devices.
**Note**
The list contains only summary fields for the bucket and does not contain fields like the user-defined metadata.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm)


  * In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
  * Use the [oci os bucket list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/list.html) command and required parameters to list the object storage buckets on your Roving Edge Infrastructure devices:
Copy
```
oci os bucket list --compartment-id compartment_ocid [OPTIONS]
```

For example:
```
oci os bucket list
{
 "data": [
  {
   "compartment-id": "ocid1.tenancy.orei..exampleuniqueID",
   "created-by": "First User",
   "defined-tags": null,
   "etag": "72d614f7-618c-476b-8d4d-41f8ee354083",
   "freeform-tags": null,
   "name": "provisioned-oci-custom-images",
   "namespace": "rover-namespace",
   "time-created": "2023-05-15T08:41:16.430000+00:00"
  },
  {
   "compartment-id": "ocid1.tenancy.orei..exampleuniqueID",
   "created-by": "First User",
   "defined-tags": null,
   "etag": "76ef7213-1118-4748-97f7-09738f9f353b",
   "freeform-tags": null,
   "name": "rover-system-upgrade-staging",
   "namespace": "rover-namespace",
   "time-created": "2023-05-15T08:32:19.484000+00:00"
  }
 ],
 "opc-next-page": "rover-system-upgrade-staging"
}
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListBuckets](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ListBuckets) operation to list the object storage buckets on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

