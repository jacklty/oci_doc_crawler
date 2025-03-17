Updated 2025-03-04
# Object Storage Versioning
Learn how to use object versioning to apply data protection against the accidental or malicious object updating or deleting of Object Storage objects.
Object versioning is enabled at the bucket level. Versioning directs Object Storage to automatically create an object version each time a new object is uploaded, an existing object is overwritten, or when an object is deleted. You can enable object versioning at bucket creation time or enable it on an existing bucket that either never had object versioning enabled before, or one that had its object versioning suspended.
A bucket that's versioning-enabled can have many versions of an object. There's always one _latest_ version of the object and zero or more _previous_ versions. 
Each object version has a unique version ID. Certain tasks when using the Command Line Interface (CLI) or API, such as deleting or recovering an object version, require you include the object version ID. You can find the version ID by running the following commands or operations:
  * CLI: [oci os object list-object-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list-object-versions.html)
  * API: [ListObjectVersions](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjectVersions)


See [Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm#top "View a list the versions of an object in an Object Storage bucket.") for more information on getting an object's version ID.
**Important**
Standard Oracle Cloud Infrastructure pricing applies to each bucket that's enabled for versioning. You're charged for all latest object versions and previous object versions (including deleted versions) stored in the bucket. Previous object versions are retained until you explicitly delete them.
Object versioning does increase your storage costs. Consider using [Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#object-lifecycle "Learn how to use Object Lifecycle Management to automatically manage the archiving and deletion of objects.") to help you manage object versions automatically.
## Versioning Tasks 🔗 
You can perform the following object versioning tasks:
  * [List the objects and their versions in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm#top "View a list the versions of an object in an Object Storage bucket.")
  * [Enable object versioning when creating a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm#top "Enable object versioning when you create an Object Storage bucket.")
  * [Get an object version's details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm#top "View the details for an object version in an Object Storage bucket.")
  * [Enable or disable versioning in an existing bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm#top "Enable or suspend object versioning on an Object Storage bucket.")
  * [Deleting an object version](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm#top "Delete an object's version from an Object Storage bucket.")


## Object Versioning Status 🔗 
Each Object Storage bucket has object versioning status of disabled, enabled, or suspended. By default, object versioning is disabled on a bucket. It's important to understand the behavior associated with each object versioning status.
### Disabled 🔗 
If object versioning is disabled on a bucket:
  * Object versioning has never been enabled on the bucket.
  * When you upload an object with the same name as an existing object, the object is overwritten and the overwritten object is not retained or recoverable.
  * When you delete an object, the deletion is permanent and objects aren't recoverable.


### Enabled 🔗 
If object versioning is enabled on a bucket:
  * When you upload an object with the same name as an existing object, the existing object becomes a previous version and the newly uploaded object becomes the latest version.
  * Each uploaded object is assigned a unique version identifier. The identifier lets you direct Object Storage actions to a specific version.
  * When you delete an object, Object Storage retains a version of the deleted object. For more information about object deletion, see [Object Version Deletion](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#Understa).
  * You can't disable object versioning. You can, however, suspend versioning.


### Suspended 🔗 
If object versioning is suspended on a bucket:
  * Upload and delete behavior is the same as a bucket that has versioning disabled.
  * Object versions created before versioning suspension are retained, unless you take explicit action to delete them.
  * You can re-enable object versioning at any time.


## Object Version Deletion 🔗 
No object is physically deleted from a bucket that has versioning enabled until you take explicit action to do so. When you delete an object without targeting a specific version, the latest object version becomes a previous object version and a special _delete marker_ is created that _marks_ the deletion point. A delete marker contains only minimal metadata. If you delete a [folder](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#objects "Learn about how to manageObject Storage objects, which are files or unstructured data that you can upload to an Object Storage bucket to a compartment."), a delete marker is created for each object in the folder. Delete the delete marker to make that deleted version become the latest object version.
When you upload an object with the same name as the delete marker, the uploaded object becomes the latest version of the object. The delete marker remains. There can be multiple delete markers for an object and you can recover any of the previous object versions.
Object version deletion is different. When you delete an object version, the version is permanently deleted. **Permanent deletion also happens if you explicitly delete the latest version by version ID**. All delete operations that target a specific object version ID permanently deletes the data.
## Required IAM Policies 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
For administrators:
  * You can create a policy that lets the specified IAM group manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy. For example, to let the IAM group StorageAdmins do everything in the tenancy:
Copy
```
Allow group StorageAdmins to manage object-family in tenancy
```

  * Alternatively, you can create policies that reduce the scope of access. For example, you can create the policies to let the StorageAdmins group manage only buckets and objects in a compartment called ObjectStore in the tenancy:
Copy
```
Allow group StorageAdmins to manage buckets in compartment ObjectStore
Allow group StorageAdmins to manage objects in compartment ObjectStore
```

  * If you create more restrictive policies that grant individual permissions, BUCKET_UPDATE is required to enable versioning. Uploading objects, overwriting existing objects, or deleting objects require the regular permissions necessary for those operations. OBJECT_VERSION_DELETE is required to delete object versions. For example, to allow a group called StorageSupport to manage Object Storage resources, but prevent that group from permanently removing object versions:
Copy
```
Allow group StorageSupport to manage object-family in tenancy where request.operation != 'DeleteObjectVersion'
```



For more information about other alternatives for writing policies, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
## Scope and Constraints 🔗 
  * Versioning can be enabled on a bucket in the Standard ([Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#overview "Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.")) or [Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) tier.
  * Restoring an archived object is an in-place operation and does not create an object version.
  * You can rename the latest version of an object, but you cannot rename a previous object version. Renaming an object creates a new object.


## Interaction Between Versioning and Other Object Storage Features 🔗 
This section describes some key things you need to know about the interaction between object versioning and other Object Storage features. 
### Bucket Re-Encryption
Bucket re-encryption (using either Oracle or your own master encryption key) also re-encrypts any existing object versions. 
### Lifecycle Management
Lifecycle policies can archive the latest version or previous versions of an object. When Lifecycle policies delete the latest version of an object, that object becomes a previous version and a delete marker is created. When Lifecycle policies delete a previous version of an object, that deletion is permanent.
### Copying Objects
If you copy the latest version of an object to a different bucket, only the object is copied. None of the object's previous versions are copied. You can copy a previous version of an object to another bucket, but that action creates either the latest version of a new object or a new object version in the destination bucket.
### Replication
  * Replication cannot replicate previous object versions.
  * You cannot enable versioning on a replication destination bucket. A destination bucket is read-only.


### Retention Rules
  * You cannot add retention rules to a bucket that has versioning enabled.
  * You cannot enable versioning on a bucket with active retention rules.
  * You can add retention rules to bucket that has versioning suspended. However, you cannot resume versioning with active retention rules.


Was this article helpful?
YesNo

