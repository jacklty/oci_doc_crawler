Updated 2024-10-09
# Creating a Bucket for Roving Edge Infrastructure
Describes how to create a object storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click **Create Bucket**. The **Create Bucket** dialog box appears.
    3. Enter a name in the **Bucket Name** box. The system generates a default bucket name that reflects the current year, month, day, and time, for example **bucket-20190306-1359**. If you change this default to any other bucket name, use letters, numbers, dashes, underscores, and periods. Avoid entering confidential information.
    4. Select **Enable Object Versioning** if you want to apply versioning to all objects that you upload. See [Object Versioning](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/object_versions.htm#ObjectManagement "Describes how to enable and manage the versioning of objects in an object storage bucket on your Roving Edge Infrastructure.").
    5. Click **Create**.
The bucket is created and you can start uploading objects.
  * Use the [oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html) command and required parameters to create a object storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os bucket create --compartment_id compartment_ocid --name name [OPTIONS]
```

For example:
```
oci os bucket create --name sample_test_bucket
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid1.tenancy.orei..exampleuniqueID",
  "created-by": null,
  "defined-tags": null,
  "etag": "87b5810e-ae30-4b02-a5cd-6eede4233259",
  "freeform-tags": null,
  "id": "ocid1.bucket.orei.orei-1..exampleuniqueID",
  "is-read-only": null,
  "kms-key-id": null,
  "metadata": null,
  "name": "sample_test_bucket",
  "namespace": "rover-namespace",
  "object-events-enabled": null,
  "object-lifecycle-policy-etag": null,
  "public-access-type": null,
  "replication-enabled": null,
  "storage-tier": null,
  "time-created": "2023-06-02T12:40:22.195000+00:00",
  "versioning": "Disabled"
 },
 "etag": "87b5810e-ae30-4b02-a5cd-6eede4233259"
}
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation to create a object storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

