Updated 2024-10-09
# Deleting a Bucket from Roving Edge Infrastructure
Describes how to delete an object storage bucket on your Roving Edge Infrastructure devices.
The bucket must be empty before you can delete it. See [Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#top "Describes how to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices."). If your bucket has versioning enabled, you must delete each version of all the objects contained in the bucket before you can delete the bucket. See [Deleting an Object Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm#top "Describes how to delete a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm)


  *     1. In the Device Console, open the navigation menu and select **Storage > Object Storage & Archive Storage**. The **Buckets** page is displayed. All buckets are listed in tabular form.
    2. Click the bucket that you want to delete. The bucket's **Details** page appears.
    3. Click **Delete**.
    4. Confirm the deletion when prompted.
  * Use the [oci os bucket delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/delete.html) command and required parameters to delete an object storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os bucket delete --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os bucket delete --bucket-name my_bucket
Are you sure you want to delete this bucket? [y/N]: y 
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/DeleteBucket) operation to delete an object storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

