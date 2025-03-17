Updated 2025-01-22
# Renaming an Object Storage Object
Rename an object in an Object Storage bucket.
For information about object naming, see [Object Names](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Rename**.
    4. Enter the new name for the object in the **Object Name** box. You can include an optional delimited directory structure prefix. For example, `p_94.jpg` or `/marathon/participants/p_94.jpg`. Avoid entering confidential information.
**Caution**
Buckets can't store two objects that use identical names (case-sensitive). If you rename an object using the name of another object in the same bucket, the object that originally used the name is overwritten.
    5. Select **Save Changes**.
  * Use the [oci os object rename](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/rename.html) command and required parameters to rename an object in a bucket:
Command
CopyTry It
```
oci os object rename --bucket-name bucket_name --name object_original_name --new-name object_new_name [OPTIONS]
```

For example:
```
oci os object rename --bucket-name MyBucket --name MyFile.txt --new-name MyRenamedFile.txt
{
 "etag": "3504606b-8412-4b5d-924a-aeaeacf1df1e"
}
```

#### Renaming an Object having a Specific Entity Tag 🔗 
To make the rename operation dependent on the object having a specific entity tag, use the `--src-obj-if-match-e-tag` option.
For example:
```
oci os object rename --bucket-name MyBucket --name MyFile.txt --new-name MyRenamedFile.txt --src-obj-if-match-e-tag 6672BECB67CCFFBCE0530292F20ZBACE
```

#### Overwriting an Object 🔗 
For rename operations where you intend to overwrite one object in a bucket with another, you can make the renaming dependent on having a specific entity tag. To do so, use the `--new-obj-if-match-e-tag` option.
For example:
```
oci os object rename --bucket-name MyBucket --name MyFile.txt --new-name MyRenamedFile.txt --new-obj-if-match-e-tag 6672BECB67CCFFBCE0530292F20ZBACE
```

#### Preventing Overwriting an Object 🔗 
When renaming an object, you can prevent the system from overwriting another object in the same bucket by using the `--new-obj-if-none-match-e-tag *` option. This option prevents the renaming operation from completing if an object exists with the `--new-name` value specified and the same entity tag of the source object.
For example:
Command
CopyTry It
```
oci os object rename --bucket-name MyBucket --name MyFile.txt --new-name MyRenamedFile.txt --new-obj-if-none-match-e-tag *
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RenameObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/RenameObject) operation to rename an object in a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo

