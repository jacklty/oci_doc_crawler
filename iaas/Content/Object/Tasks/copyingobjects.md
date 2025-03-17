Updated 2025-01-22
# Copying an Object to Another Bucket in Object Storage
Copy an object to another bucket in Object Storage.
**Caution** Object copy doesn't work if you don't authorize the Object Storage service to copy objects on your behalf. See [Service Permissions](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#Service) for more information.
## Copy Object Overwrite Rules 🔗 
Use overwrite rules to control the copying of objects based on their entity tag (ETag) values.
  * **Overwrite destination object** : Use this option when you don't want to limit a copy operation by an ETag value. This option is the default. This option can be used for any copy operation, regardless of whether it involves overwriting an existing object.
  * **Do not overwrite any destination object** : Use this option to prevent the overwriting an existing copy of an object in the destination location, regardless of the destination object's ETag value.
  * **Overwrite destination object only if it matches the specified ETag** : Use this option to prevent the accidental overwriting of an object in the destination location that doesn't have the specified ETag. When you use this option, the copy operation only succeeds if the ETag you supply when starting the copy request matches the ETag of the destination object.
  * **Copy object only if the source matches the specified ETag** : Use this option if you want the copy operation successful only if the ETag you supply when starting the copy request matches the ETag of the source object. For objects that are intentionally updated and overwritten as part of data management activity, this option ensures that only the specified version of the object (as indicated by the ETag) is allowed to be copied. If the object's ETag value changes after the copy work request is created, but before the copy operation is run, the copy operation doesn't complete.


**Caution**
If you overwrite an object, the operation can't be undone.
## Scope and Constraints 🔗 
  * Objects can't be copied directly from [Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm). To copy objects that are in Archive Storage, you must first [restore](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) the object to the Standard Object Storage tier. Objects can be copied directly to Archive tier buckets from the Standard or Infrequent Access tiers. When you copy objects into an Archive Storage bucket, the copy of the object is immediately archived.
  * Specify an existing target bucket for the copy request. The copy operation doesn't automatically create buckets.
  * When an object is copied, the destination object receives a new ETag value.
  * If you rename, overwrite, or delete a source object during a copy operation, the copy operation fails and the destination object is not created or overwritten.
  * Bulk copying isn't supported. Identify a single object in the copy request.


## Service Permissions 🔗 
Because Object Storage is a regional service, you must authorize the Object Storage service for each region carrying out copy operations on your behalf. For example, you might authorize the Object Storage service in region US East (Ashburn) to manage objects on your behalf. After you authorize the Object Storage service, you can copy an object stored in a US East (Ashburn) bucket to a bucket in another region.
To determine the region identifier value of an Oracle Cloud Infrastructure region, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). 
For administrators:
To enable object copy, you must authorize the service to manage objects on your behalf: 
  * You can create a policy that authorizes the service in the specified region to manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy:
Copy
```
Allow service objectstorage-<region_identifier> to manage object-family in tenancy
```

  * Instead of using the [policy verb](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-Verbs.htm) `manage`, you can create a policy that reduces the scope of access by instead using one of the following statements:
Copy
```
Allow service objectstorage-<region_identifier> to manage object-family in tenancy where any {request.permission='OBJECT_READ', request.permission='OBJECT_INSPECT', request.permission='OBJECT_CREATE', request.permission='OBJECT_OVERWRITE', request.permission='OBJECT_DELETE'}
```

Copy
```
Allow service objectstorage-<region_identifier> to manage object-family in compartment <compartment_name> where any {request.permission='OBJECT_READ', request.permission='OBJECT_INSPECT', request.permission='OBJECT_CREATE', request.permission='OBJECT_OVERWRITE', request.permission='OBJECT_DELETE'}
```



## Copying an Object 🔗 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Copy**.
The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you think you have the required policies in place, go ahead and try the copy operation.
    4. Enter the following information:
       * **Destination Namespace** : Enter the namespace of the destination bucket for the copied object. The namespace string of your tenancy is supplied as the default value. See [Understanding Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") for more information.
       * **Destination Region** : Select the OCI region that contains the destination bucket for the copied object from the list. Your tenancy must be [subscribed to a region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#subscribe) for you to copy an object to a bucket in that region.
       * **Destination Bucket** : Enter the name of the destination bucket for the copied object. The destination must be an existing bucket in that you have access to. See [Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#buckets "Learn about Object Storage buckets, in which you can store objects in a compartment.") for more information on how to create a bucket.
       * **Destination Object Name** : (Optional) Enter an alternate name for the object being copied if you don't want to use its original name. By default, the name is the same name as the object that you're copying.
       * **Destination Storage Tier** : (Optional) Specify the storage tier to upload the object to if you want it to be different than the source storage tier. The following storage tiers are supported:
         * [Standard](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier) (default)
         * [Infrequent Access](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access)
         * [Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)
If you don't specify a destination storage tier, the object is stored in the same storage tier as the bucket. See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for more information. 
       * **Overwrite Rule** : Select the overwrite rule appropriate for the copy request:
         * **Overwrite destination object**
         * **Do not overwrite any destination object**
         * **Overwrite destination object only if it matches the specified ETag**
         * **Copy object only if the source matches the specified ETag**
See [Copy Object Overwrite Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#overwrite) for descriptions of each of these rules.
    5. Select **Copy Object**.
The **Work Request Details** dialog box appears and confirms that the copy request is submitted successfully and tracks the status of the request.
  * Use the [oci os object copy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/copy.html) command and required parameters to copy an object to another bucket:
Command
CopyTry It
```
oci os object copy --bucket-name source_bucket_name --source-object-name source_object_name --destination-bucket destination_bucket_name [OPTIONS]
```

For example:
```
oci os object copy --bucket-name photos --source-object-name hummingbird.jpg --destination-namespace ansh8lvru1zp --destination-bucket UK_photos
```

##### Copying an Object to a Different Region 🔗 
Include the `destination-region` parameter and the region identifier to specify a target bucket in region on there than the one where the destination object resides.
For example:
```
oci os object copy --bucket-name photos --source-object-name hummingbird.jpg --destination-bucket UK_photos --destination-region uk-london-1
```
Your tenancy must be [subscribed to a region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#subscribe) for you to copy an object to a bucket in that region.
##### Copying to a Different Destination Storage Tier 🔗 
Include the `destination-object-storage-tier` parameter and a supported storage tier value to copy the object to a different storage tier on the destination bucket than the tier where it resides on the source. 
For example:
```
oci os object copy --bucket-name photos --source-object-name hummingbird.jpg --destination-bucket UK_photos --destination-object-storage-tier Archive
```

Supported values are:
    * `Standard` (default)
    * `InfrequentAccess`
    * `Archive`
    * If you don't specify a destination storage tier, the object is stored in the same storage tier as the bucket. See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for more information.
##### Specifying the Namespace of the Copied Object 🔗 
Include the `destination-namespace` parameter and its value to specify the destination namespace to which the object is copied.
For example:
```
oci os object copy --bucket-name photos --source-object-name hummingbird.jpg --destination-bucket UK_photos --destination-namespace MyNamespace
```
See [Understanding Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") for more information.
##### Specifying an Alternate Name for the Copied Object 🔗 
Include the ``destination-object-name`` parameter and its value to apply an alternate name to the copied object.
For example:
```
oci os object copy --bucket-name photos --source-object-name hummingbird.jpg --destination-bucket UK_photos --destination-object-name hummingbird_brochure.jpg
```

By default, the name is the same name as the object that you're copying.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject) operation to copy an object to another bucket.


Was this article helpful?
YesNo

