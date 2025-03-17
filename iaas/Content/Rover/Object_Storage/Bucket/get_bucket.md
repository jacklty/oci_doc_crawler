Updated 2024-10-09
# Getting a Bucket's Details for Roving Edge Infrastructure
Describes how to get the details of an object storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/get_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/get_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/get_bucket.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket whose details you want to get. The bucket's **Details** page appears.
  * Use the [oci os bucket get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/get.html) command and required parameters to get the details of an object storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os bucket get --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os bucket get --bucket-name my_bucket
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid1.tenancy.orei..exampleuniqueID",
  "created-by": null,
  "defined-tags": null,
  "etag": "3a4abb1c-0d4d-4760-b756-2fb69f46b73f",
  "freeform-tags": null,
  "id": "ocid1.bucket.orei.orei-1..exampleuniqueID",
  "is-read-only": null,
  "kms-key-id": null,
  "metadata": null,
  "name": "os_test",
  "namespace": "rover-namespace",
  "object-events-enabled": null,
  "object-lifecycle-policy-etag": null,
  "public-access-type": null,
  "replication-enabled": null,
  "storage-tier": null,
  "time-created": "2023-05-30T05:21:33+00:00",
  "versioning": "Disabled"
 },
 "etag": "3a4abb1c-0d4d-4760-b756-2fb69f46b73f"
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket) operation to get the details of an object storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

