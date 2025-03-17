Updated 2025-03-04
# Object Storage Objects
Learn about how to manageObject Storage objects, which are files or unstructured data that you can upload to an Object Storage bucket to a compartment.
In the Object Storage service, an object is a file or unstructured data you upload to a bucket within a **compartment** within an Object Storage [namespace](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks."). The object can be any type of data, for example, multimedia files, data backups, static web content, or logs. You can store objects that are up to 10 TiB. Objects are processed as a single entity. You can't edit or append data to an object, but you can replace the entire object.
Object Storage allows versioning of objects, which creates an accessible and downloadable copy of a particular version of an object you uploaded to a bucket. Object versioning protects objects from accidental or malicious overwrite or deletion. For more information, see [Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#object-versioning "Learn how to use object versioning to apply data protection against the accidental or malicious object updating or deleting of Object Storage objects.").
These topics describes how to manage objects within a single bucket. For information on copying an object to another bucket, see [Copying Objects](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#copying_objects "Copy an object to another bucket in Object Storage.").
## Object Tasks 🔗 
You can perform the following Object Storage object tasks:
  * [List the objects in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm#top "View a list of the objects in an Object Storage bucket.")
  * [Create and delete folders and subfolders in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_create_a_new_folder.htm#top "Create and delete folders and subfolders in an Object Storage bucket to organize objects.")
  * [Upload an object to a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm#top "Upload an object to a bucket or folder in Object Storage.")
  * [Search for objects in a bucket based on the object name's prefix](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/search-objects.htm#top "Search for objects in an Object Storage bucket.")
  * [Get a bucket's details, such as its entity tag or storage tier](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm#top "View the details for an object in an Object Storage bucket.")
  * [Update the storage tier to which an object is assigned](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_update_the_storage_tier_of_an_object.htm#top "Update the storage tier for an object in that reside in the Standard and Infrequent Access tiers in an Object Storage bucket.")
  * [Rename an object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm#top "Rename an object in an Object Storage bucket.")
  * [Re-encrypt an object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm#top "Re-encrypt an object's data encryption keys with a different master encryption key in an Object Storage bucket.")
  * [Copy an object to another bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#copying_objects "Copy an object to another bucket in Object Storage.")
  * [Restore an object from Archive Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_restore_objects_from_Archive_Storage.htm#top "Restore an object from Archive Storage to Object Storage.")
  * [Check the status of an object being restored from Archive Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_check_the_status_of_an_Archive_Storage_object_restoration.htm#top "Check the status of an Archive Storage object restoration.")
  * [Download an object to your computer](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm#top "Download an object from an Object Storage bucket or folder to your computer.")
  * [Synchronize a file system directory with objects in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/sync-object.htm#top "Synchronize a file system directory with objects in a bucket.")
  * [Delete an object from a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm#top "Delete one or more objects from an Object Storage bucket")
  * [Restore a deleted object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm#top "Recover a deleted object to an Object Storage bucket.")


You can perform certain tasks on a group of objects at a time using the Command Line Interface. See [Bulk Object Tasks](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bulk-tasks.htm#bulk-object-tasks "Learn how to perform certain tasks for Object Storage objects in bulk.") for more information.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
For administrators:
  * The policy [Let Object Storage admins manage buckets and objects](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#object-storage-admins-manage-buckets-objects) lets the specified group do everything with buckets and objects. Objects always reside in the same compartment as the bucket.
  * If you need to write a more restrictive policy for objects, the `inspect objects` lets you list all the objects in a bucket and do a HEAD operation for a particular object. In comparison, `read objects` lets you download the object itself.
  * To create more restrictive policies that grant individual permissions:
    * OBJECT_VERSION_DELETE is required to delete previous object versions on your behalf using lifecycle policies.
    * OBJECT_UPDATE_TIER is required to change the storage tier of an object.


See [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm) for more information on Object Storage user permissions.
### IAM Policies for Objects 🔗 
Sometimes having bucket-level access control is insufficient for your security needs. Instead, having a more granular control at an individual or prefix- or suffix-based group of objects is required. For example, if you're part of a group which is authorized for a specific object to get a work request, you need an Identity and Access Management IAM policy that gives permission for that operation explicitly.
Object-level IAM policies let you grant permission to specific objects and subsets of objects within an Object Storage bucket. The IAM policy variable `target.object.name` gives you the ability to apply authorization and permissions to objects, similar to what you can do with tenancies, compartments, and buckets. For example:
Copy
```
ALLOW GROUP object-authZ-op-group-ost-object TO manage objects IN TENANCY where any {target.object.name = 'ost-object-*', request.operation = 'GetObject'}
```

Object-level IAM policies are especially useful to big data and data lake use cases where a single bucket has many different datasets and is accessed by several teams or workloads.
To create object-level IAM policies, follow the steps as described in [Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm). Add policy statements for object-level IAM using the following syntax:
Copy
```
ALLOW GROUP <group> TO manage objects IN TENANCY where all {target.object.name = '<object-pattern>', target.bucket.name = '<bucket_name>'}
```

Authorization is evaluated for object-level IAM policies when the request arrives for an object on the server.
**Note**
You need permissions for listing the buckets in a compartment and listing the objects in a bucket to list the specific object or object patterns when using the Console. You must have READ permissions to access the objects that are listed.
If the object name or path is already known and is being accessed using the CLI or API, you don't need these compartment or bucket access permissions.
**Note**
There might be a delay of several minutes for any object policies you apply to become effective. This delay is applicable to all policies you create or update that control the access to Object Storage resources.
You can also update an existing policy to include object-level IAM permissions. See [Updating a Policy's Statements](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_update_the_statements_in_an_existing_policy.htm). Object-level IAM policies are compatible with all existing policy constructs.
**Example 1: Allowing full access to a group for a folder in a bucket:**
Copy
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*'} 
```

**Example 2: Allowing read-only access to a group for a folder in a bucket:**
Copy
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_INSPECT', request.permission='OBJECT_READ'}}
```

**Example 3: Allowing write-once (no overwrites) and no read or delete access to a group for a folder:**
Copy
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_CREATE'}}
```

**Example 4: Allowing read and write access to a group for a folder in a bucket (no listing or overwriting):**
Copy
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_CREATE', request.permission='OBJECT_READ'}}
```

**Example 5: Allowing all access for a specific user for an object pattern in a bucket:**
Copy
```
ALLOW any-user TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = '*.pdf', request.user.id='ocid1.user.oc1..exampleuniqueID'}
```

## Pre-Authenticated Requests 🔗 
Pre-authenticated requests provide a way to let users access a bucket or object without having their own credentials. For example, you can create a request that lets a user upload backups to a bucket without owning API keys. See [Object Storage Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm#pre-auth-req "Learn about how to use the pre-authenticated request feature to give users access a bucket or an object without providing their sign-on credentials.") for details.
## Object Names 🔗 
Unlike other resources, objects don't have Oracle Cloud Identifiers (OCIDs). Instead, users define an object name when they upload an object.
Use the following guidelines when naming an object:
  * Use from 1 to 1024 characters.
  * Valid characters are letters (upper or lowercase), numbers, and characters other than line feed, carriage return, and NULL.
**Important**
Bucket names and object names are case-sensitive. Object Storage handles q3-field-assets.xslx and Q3-Field-Assets.XSLX as separate objects.
  * Use only Unicode characters for which the UTF-8 encoding doesn't exceed 1024 bytes. Clients are responsible for URL-encoding characters.
  * Avoid entering confidential information.
  * Make the name unique within the bucket. Don't use the name of an existing object within the bucket when naming an object unless you intend to overwrite the existing object with the contents of the new or renamed object.


**Tip**
Object names can include one or more forward slash (/) characters in the name. See [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix) for more information on using the forward slash in object names to create hierarchies.
## Object Naming Using Prefixes and Hierarchies 🔗 
Within an Object Storage namespace, buckets and objects exist in a flat structure. However, you can simulate a directory structure by adding a prefix string that includes one or more forward slashes (/) to an object name. Doing so lets you list one directory at a time, which is helpful when navigating a large set of objects.
For example:
```
marathon/finish_line.jpg
marathon/participants/p_21.jpg
```

If you added prefixes to object names, you can:
  * Use the CLI or API to perform bulk downloads and bulk deletes of all objects at a specified level of the hierarchy.
  * Use the Console to display a hierarchical view of your objects in virtual folders. In the previous example, `marathon` would be displayed as a folder containing an object named `finish_line.jpg` and `participants` would be a subfolder of `marathon`, containing an object named `p_21.jpg`. You can bulk upload objects to any level of the hierarchy and perform bulk deletes of all the objects in a bucket or folder.


Bulk operations at a specified level of the hierarchy don't affect objects in any preceding level.
When naming objects, you can also use prefix strings without a delimiter. No delimiters would allow search operations in the Console and certain bulk operations in the CL or API to match on the prefix portion of the object name. For example, in the object names below, the string `gloves_27_` can serve as a prefix for matching purposes when performing bulk operations:
```
gloves_27_dark_green.jpg
gloves_27_light_blue.jpg	
```

When you perform bulk uploads with the Console, CLI, or API, you can prepend a prefix string to the names of the files you're uploading.
For hierarchy and prefix string details for a particular management interface, see the individual tasks in [Object Storage Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#buckets "Learn about Object Storage buckets, in which you can store objects in a compartment.").
## Optional Response Headers and Metadata 🔗 
When you upload objects, you can provide optional response headers and user-defined metadata. Response headers are HTTP headers sent from Object Storage to Object Storage clients when objects are downloaded. User-defined metadata are name-value pairs stored with an object. You can use the Console, REST API, or CLI to provide these optional attributes.
**Important** No validation is performed on the response headers or metadata you provide. 
You can specify values for the following response headers:
  * Content-Disposition
Defines presentation only information for the object. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object decide what to do based on the value provided. For example, you could use this header to let users download objects with custom file names in a browser:
Copy
```
attachment; filename="fname.ext"
```

See <https://tools.ietf.org/html/rfc2616#section-19.5.1> for more information.
  * Cache-Control
Defines the caching behavior for the object. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object decide what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions:
Copy
```
no-cache, no-store
```

See <https://tools.ietf.org/html/rfc2616#section-14.9> for more information.


You specify user-defined metadata in the form of name-value pairs. User-defined metadata names are stored and returned to Object Storage clients with the mandatory prefix of **opc-meta-**.
## Object Lifecycle Management 🔗 
Object Lifecycle Management lets you automatically manage the deletion of uncommitted multipart uploads, the movement of objects to a different storage tier, and the deletion of supported resources on your behalf within a given bucket. These automated actions are based on rules that you define and manage. See [Object Storage Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#object-lifecycle "Learn how to use Object Lifecycle Management to automatically manage the archiving and deletion of objects.") for more information about this feature.
## Multipart Uploading and Downloading 🔗 
The Oracle Cloud Infrastructure Object Storage service supports multipart uploading and downloading for objects. 
  * For information about the API and CLI multipart uploading functionality, see [Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.").
  * For CLI information on multipart downloading, see [downloading an object using multipart download](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm#top "Download an object from an Object Storage bucket or folder to your computer.").
  * For API documentation related to multipart downloading, see the [GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) API call and its **range** parameter.


## Monitoring Resources 🔗 
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
For more information about monitoring objects, see [Object Storage Metrics](https://docs.oracle.com/en-us/iaas/Content/Object/Reference/objectstoragemetrics.htm#metrics "Learn about the metrics generated by the Object Storage service.").
## Creating Automation for Objects Using the Events Service 🔗 
You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
Was this article helpful?
YesNo

