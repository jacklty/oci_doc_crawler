Updated 2024-10-07
# Object Storage Security Guidelines
On Compute Cloud@Customer, the Object Storage service stores and provides access to large amounts of unstructured data of any content type. Content stored in object storage can be accessed by compute instances and from the data center through the Compute Cloud@Customer domain name.
The Object Storage service provides these security capabilities:
  * Encrypts data on disk (at rest) using Advanced Encryption Standard (AES) 128-bit algorithm. Encryption is on by default and can't be turned off. The encryption keys are themselves encrypted with a master encryption key.
  * Data in transit between clients (for example, SDKs and CLIs) and Object Storage public endpoints is encrypted with TLS 1.2 by default.
  * Data integrity is facilitated by a checksum generated for each uploaded object and, for multipart uploads, a checksum generated for each part.
  * Objects can have revokable preauthenticated requests built with varying authorization levels.
  * Object versioning is available to retain changes to objects.
  * Write-once Read-many (WORM) retention rules can be set to ensure an object retains its original contents.
  * Users that are authenticated to Compute Cloud@Customer can manage the Object Storage service and resources that are managed within the security policy framework.


For more information about the Object Storage service, see [Object Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/object-storage.htm#object-storage "On Compute Cloud@Customer, the Object Storage service provides reliable and cost-efficient data durability.").
## Assign Least Privileged Access 🔗 
**Attention**
For Compute Cloud@Customer, IAM resources are managed in OCI within your tenancy, and synchronized to Compute Cloud@Customer every ten minutes or so. IAM resources can't be managed on the Compute Cloud@Customer infrastructure.
Assign least privileged access for users and groups to resource types in _object-family_ (such as objectstorage-namespaces, buckets, and objects). 
The following IAM verbs enable you to tailor Object Storage access privileges:
  * `inspect` verb gives the least privilege. It lets you check to see if a bucket exists (`HeadBucket`) and list the buckets in a compartment (`ListBucket`).
  * `manage` verb gives all permissions on the resource. You can create IAM security policies to give appropriate bucket and object access to various IAM groups. 


For more information about IAM verbs and permissions for Object Storage buckets and objects, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#Details_for_Object_Storage_Archive_Storage_and_Data_Transfer). 
For users without IAM credentials, we recommend that you use preauthenticated requests (PARs) to give time-bound access to objects or buckets.
## Preauthenticated Requests 🔗 
Preauthenticated requests provide a mechanism to give access to objects and buckets without requiring the client or user to log into Compute Cloud@Customer. As a result, objects and buckets can be used without an user defined on the Compute Cloud@Customer.
An user with appropriate privileges for accessing objects creates a URL that grants time-bound access to objects. For more information on these grants, see [Using Preauthenticated Requests](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/using-pre-authenticaed-requests.htm#using-pre-authenticaed-requests "On Compute Cloud@Customer, preauthenticated requests provide a way to let users access a bucket or an object without having their own credentials, as long as the request creator has permissions to access those objects."). Note the following points:
  * The creator of a preauthenticated request must have `PAR_MANAGE` permission and the appropriate IAM permissions for the access type that you're granting. You can create a preauthenticated request that grants read, write, or read/write access to one of the following:
    * All objects in the bucket.
    * A specific object in the bucket.
    * All objects in the bucket that have a specified prefix.
For requests that apply to multiple objects, you can also decide whether you want to let users list those objects.
  * Preauthenticated request accesses to a bucket are logged in Audit logs. Preauthenticated request accesses to an object are logged in Service logs.


**Important**
The unique URL provided by the system when you create a preauthenticated request is the only way a user can access the request target. Copy the URL to durable storage. The URL is displayed only at the time of creation, isn't stored in Object Storage, and can't be retrieved later.
## Data Durability and Integrity 🔗 
The Object Storage service provides a variety of ways to ensure data remains consistent and intact when stored. Be aware of the following points:
  * Data loss can be minimized by preventing inadvertent deletes by an authorized user or malicious deletes:
    * Use [Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.") to automatically create an object version each time a new object is uploaded, an existing object is overwritten, or when an object is deleted.
    * Give `BUCKET_DELETE` and `OBJECT_DELETE` permissions to a minimum set of users and groups. Grant delete permissions only to tenancy and compartment administrators.
  * Write once read many (WORM) compliance requires that objects can't be deleted or modified. Use [retention rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/defining-retention-rules.htm#defining-retention-rules "On Compute Cloud@Customer, retention rules provide immutable storage options for data written to Object Storage for data governance, regulatory compliance, and legal hold requirements. Retention rules can also protect your data from accidental or malicious writes or deletion. Retention rules can be locked to prevent rule modification and data deletion or modification even by administrators.") to achieve WORM compliance. Retention rules are configured at the bucket level and are applied to all individual objects in the bucket. You can't update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules).
For an independent assessment of the Object Storage retention rules feature's ability to meet regulatory requirements for record management and retention, see Cohasset Associate's [SEC 17a-4(f), FINRA 4511(c), CFTC 1.31(c)-(d) and MiFID II Compliance Assessment](https://www.oracle.com/a/ocom/docs/oracle-object-storage-compliance-assessment-report.pdf) PDF document.
  * Objects are stored in a ZFS file system with a SHA-256 checksum to avoid phantom reads and detect invalid data returned from devices.


In addition to facilities provided for durability, Object Storage provides mechanisms to ensure data integrity:
  * A checksum is provided for all objects uploaded to Object Storage. The checksum can be used in two ways:
    * To verify that the object stored is the object that was uploaded
    * To verify that the object retrieved is the one that was originally stored
  * Multipart uploads are used by the Object Storage service for efficiency and resiliency on large object uploads. In a multipart upload, a large object is broken up into smaller parts by specifying a part size in MiB. Each part is uploaded separately. Object Storage then combines all the parts to re-create the original object. If any of the parts fail to upload, only the failed parts need to be retried for upload, not the entire object. In a multipart upload, checksum values are computed for each part of the upload, and a single checksum is computed over all the individual checksum values to get the checksum value reported by the object upload. To verify the value returned for a multipart upload, follow the same process for offline checksum calculation. 


Using the checksum returned when the object is stored, the contents of the object can be verified when it's downloaded again or against the original object to verify uploaded object correctness.
OSs have various tools for checksum verification. The checksum returned by an object upload (or viewing an object in the bucket) is a Base-64 encoded value. This value might have to be converted to hexadecimal depending on the tools used for checksum comparison.
Was this article helpful?
YesNo

