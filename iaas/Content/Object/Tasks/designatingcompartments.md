Updated 2025-03-04
# Object Storage Compartments for the Amazon S3 Compatibility API and Swift API
Learn about how Object Storage provides API support for both Amazon S3 Compatibility API and Swift API. You can choose the default the compartment where this data is stored.
In the Object Storage service, a bucket is a container for storing objects in a **compartment** within an Object Storage [namespace](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks."). A bucket is associated with a single compartment and data is stored as objects in buckets. 
In addition to the native Object Storage APIs, Object Storage provides API support for both Amazon S3 Compatibility API and Swift API. However these APIs don't understand the Oracle Cloud Infrastructure concept of a compartment. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. Instead, you can [designate a different compartment](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm) for the Amazon S3 Compatibility API or Swift API to create buckets in.
When you choose a different compartment to use for the Amazon S3 Compatibility API or Swift API, any new buckets you create using the Amazon S3 Compatibility API or the Swift API are created in this compartment. Buckets created earlier in a different compartment aren't automatically moved to the newly-designated compartment. See [Object Storage Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#buckets "Learn about Object Storage buckets, in which you can store objects in a compartment.") to move buckets you created earlier to this compartment.
You can perform the following tasks for the Amazon S3 Compatibility API and Swift API compartment designations:
  * [View the Amazon S3 Compatibility API and Swift API compartment designations in your tenancy.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_get_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm#top "View the designated compartments for the Amazon S3 Compatibility API and Swift API in your tenancy.")
  * [Change the Amazon S3 Compatibility API and Swift API compartment designations in your tenancy.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm#top "Change your tenancy's Amazon S3 Compatibility API and Swift API compartment designations in your tenancy.")


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
Compartments have **policies** that indicate what actions a user can perform on a bucket and all the objects in the bucket. 
For administrators:
  * To change the default compartments for Amazon S3 Compatibility API and Swift API, a user must belong to a group with `OBJECTSTORAGE_NAMESPACE_UPDATE` permissions.
  * To see the current default compartments for Amazon S3 Compatibility API and Swift API, a user must belong to a group with `OBJECTSTORAGE_NAMESPACE_READ` permissions.
  * To move a bucket to a different compartment, a user must belong to a group with `BUCKET_UPDATE` and `BUCKET_CREATE` permissions in the source compartment, and `BUCKET_CREATE` permissions in the target compartment.


If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). To dig deeper into writing policies for buckets and objects, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm). 
Was this article helpful?
YesNo

