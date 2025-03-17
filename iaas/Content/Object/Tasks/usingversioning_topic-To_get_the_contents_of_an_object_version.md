Updated 2025-01-22
# Getting an Object Storage Object Version's Details
View the details for an object version in an Object Storage bucket.
See [Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm#top "View a list the versions of an object in an Object Storage bucket.") for information on getting an object version's ID.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. Select the down arrow (**Show Object Versions**) next to the object entry. The list of versions of the object appears. The latest version appears at the top of the list.
    4. From the **Actions** menu for the object you want, select **View Object Version Details**.
The **Object Version Details** dialog box opens. Here you can view the details for the object version, including its basic information and response headers.
  * Get the details of an object as described in [Getting a Replication Policy's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm#top "View the details of the replication policy for an Object Storage bucket."). Include the `version-id` parameter and the ID of the object version:
Command
CopyTry It
```
oci os object head --bucket-name bucket_name --name object_name --version-id version_id [OPTIONS]
```

For example:
```
oci os object head --bucket-name MyStandardBucket --name MyTextDocument.txt --version-id 2d528a44-5b15-40dc-b303-20993d1ade66
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Get the details of an bucket using the [HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject) operation as described in [Getting a Replication Policy's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm#top "View the details of the replication policy for an Object Storage bucket."). Include the `versionId` attribute and the ID of the object version.


Was this article helpful?
YesNo

