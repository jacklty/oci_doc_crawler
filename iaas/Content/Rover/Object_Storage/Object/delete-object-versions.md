Updated 2024-03-22
# Deleting an Object Version for Roving Edge Infrastructure
Describes how to delete a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.
Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for deleting.
To delete object versions in bulk using the command line interface (CLI), see [Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top "Describes how to upload, download, and delete objects in bulk on your Roving Edge Infrastructure devices.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm)


  *     1. Open the navigation menu and select **Object Storage > Object Storage**. The **Buckets** page appears. All buckets are listed in tabular form.
    2. Click the bucket containing the object whose version you want to delete. The bucket's **Details** page appears. All objects are listed in tabular form.
    3. (optional) Enable **Show Deleted Objects** to display those objects that were versioned, but subsequently deleted.
    4. Click the Down arrow at the right side of the object's entry to display the versions.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) of the version you want to delete and click **Delete**.
    6. Confirm the deletion.
The list of versions of the object no longer includes the version you deleted.
  * Run the `oci os object delete` command to delete an object from a bucket using the CLI as described in [Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#top "Describes how to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices."). Include the `--version-id` parameter in the command to specify the version being deleted. For example:
Copy
```
oci os object delete ... --version-id version-id ...
```

  * Run the `DeleteObject` operation to delete the version of an object in the Roving Edge Infrastructure device's object storage bucket as described in [Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#top "Describes how to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices."). Include the `versionId` attribute to specify the object version being delete.


Was this article helpful?
YesNo

