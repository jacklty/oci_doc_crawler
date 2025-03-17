Updated 2025-01-22
# Searching for Object Storage Objects in a Bucket
Search for objects in an Object Storage bucket.
You can search for objects in a bucket by entering one or more characters matching the objects' name prefixes. For example, if you had 100 objects in a bucket, and 10 of them started with "test," entering "test" in the Console's **Search by prefix** box displays only those object with that "test" prefix. Use the `prefix` parameter when using the CLI or API to perform the same function. See [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix) for more information on using the prefix feature with an object.
**Note**
Searching for an object in a bucket using any other method, such as using segments within an object's name or using wildcards ("*"), isn't supported.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/search-objects.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/search-objects.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/search-objects.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. Enter the characters you want to search the objects for in the **Search by prefix** box and select **Enter**.
All the objects whose name prefix matches the characters you entered appear in the **Objects** list. The more characters you enter that the object names must match, the smaller and more precise the number of objects returned. 
To display all the objects in the bucket, clear **Search by prefix** and select **Enter**.
  * Use the [oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html) command and required parameters to list the objects in a bucket. Include the `prefix` parameter and the prefix value the returned object names must match.
Command
CopyTry It
```
oci os object list --bucket-name bucket_name --prefix prefix ... [OPTIONS]
```

Only those objects whose names match the prefix value you included in the command are displayed in the return.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects) operation to list the objects in a bucket. Include the `prefix` parameter and the prefix value the returned object names must match.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo

