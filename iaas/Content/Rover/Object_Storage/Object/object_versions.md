Updated 2023-08-14
# Object Versioning for Roving Edge Infrastructure
Describes how to enable and manage the versioning of objects in an object storage bucket on your Roving Edge Infrastructure.
You can apply versioning to objects that you upload to your Roving Edge Infrastructure device's object store. The object versioning feature directs object storage to automatically create an object version each time a new object is uploaded, an existing object is overwritten, or when an object is deleted. Roving Edge Infrastructure supports the following object versioning states for objects:
  * **Disabled** : When you upload an object with the same name as an existing object, the object is overwritten and the overwritten object is not retained or recoverable. When you delete an object, the deletion is permanent and objects are not recoverable.
  * **Enabled** : When you upload an object with the same name as an existing object, the existing object becomes a previous version and the newly uploaded object becomes the latest version. Each uploaded object is assigned a unique version identifier. When you delete an object, object storage retains a version of the deleted object.


You enable object versioning when creating a bucket in your Roving Edge Infrastructure device's object storage. A bucket that has the versioning feature enabled can generate and contain many versions of an object. You can only enable versioning in a bucket at the time of its creation. You cannot enable or disable versioning in a bucket that already exists.
**Note**
If you want to apply versioning to your uploaded objects, but none of your available buckets has versioning enabled, you cannot use them. Instead, you must create a new bucket with versioning enabled, and upload your objects to that bucket. See [Creating a Bucket.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#top "Describes how to create a object storage bucket on your Roving Edge Infrastructure devices.")
You can perform the following object versioning tasks:
  * [Enabling Object Versioning](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm#top "Describes how to enable versioning of objects when creating an object storage bucket.")
  * [Listing Object Versions](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list-object-versions.htm#top "Describes how to list the versions of an object in an object storage bucket on your Roving Edge Infrastructure device.")
  * [Getting an Object Version's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm#top "Describes how to get the details for a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.")
  * [Downloading an Objects Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/download-object-versions.htm#top "Describes how to download a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.")
  * [Deleting an Objects Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm#top "Describes how to delete a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.")
  * [Recovering a Deleted Object Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/recover-object-version.htm#top "Describes how to recover a deleted object version contained within an object storage bucket on your Roving Edge Infrastructure devices.")


See [Using Object Versioning](https://docs.oracle.com/iaas/Content/Object/Tasks/usingversioning.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
Was this article helpful?
YesNo

