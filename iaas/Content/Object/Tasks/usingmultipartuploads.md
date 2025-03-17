Updated 2025-03-04
# Object Storage Multipart Uploads
Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.
The Oracle Cloud Infrastructure Object Storage service supports multipart uploads for more efficient and resilient uploads, especially for large objects. You can perform multipart uploads using the [API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), the [Software and Development Kits (SDKs)](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm), or the [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). The Console uses multipart uploads to upload objects larger than 64 MiB.
With multipart uploads, individual parts of an object can be uploaded in parallel to reduce the amount of time you spend uploading. Multipart uploads performed through the API can also minimize the impact of network failures by letting you retry a failed part upload instead of requiring you to retry an entire object upload.
Multipart uploads accommodate objects that are too large for a single upload operation. We recommend that you use multipart uploads to upload objects larger than 100 MiB. The maximum size for an uploaded object is 10 TiB. Object parts must be no larger than 50 GiB. Using multipart uploads, you have the flexibility of pausing between the uploads of individual parts, and resuming the upload when your schedule and resources allow.
You can use object lifecycle policy rules to automatically delete any uncommitted or failed multipart uploads after a specified number of days. See [Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#object-lifecycle "Learn how to use Object Lifecycle Management to automatically manage the archiving and deletion of objects.") for details.
## Multipart Uploads Tasks 🔗 
You can perform the following multipart upload tasks:
  * [Run a multipart upload](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm#top "Describes how to upload a large object using multipart upload in Object Storage.").
  * [View a list of the multipart uploads in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm#top "View a list of the in-progress multipart uploads for an Object Storage bucket.").
  * [Delete a multipart upload from a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/To_delete_uncommitted_multipart_uploads.htm#top "Cancel and delete an uncommitted or failed multipart upload in Object Storage.").
  * [Run various API operations on multipart uploads and their parts.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-Using_the_Multipart_Upload_API.htm#using_api "Learn how to run multipart uploads for a bucket using the API.").


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you are new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
For administrators:
  * You can create a policy that lets the specified IAM group manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy:
Copy
```
Allow group <IAM_group_name> to manage object-family in tenancy
```

  * You can also create policies that reduce the scope of access. For example, to let the specified group manage only buckets and objects in a particular compartment in the tenancy:
Copy
```
Allow group <IAM_group_name> to manage buckets in compartment <compartment_name>
```



**Important** If you write more restrictive policies, ensure that you include the permissions required for multipart uploads. The user needs a policy that grants both OBJECT_CREATE and OBJECT_OVERWRITE permissions.
For more information about other alternatives for writing policies, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
## Monitoring Resources 🔗 
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
For more information about monitoring multipart uploads, see [Object Storage Metrics](https://docs.oracle.com/en-us/iaas/Content/Object/Reference/objectstoragemetrics.htm#metrics "Learn about the metrics generated by the Object Storage service.").
Was this article helpful?
YesNo

