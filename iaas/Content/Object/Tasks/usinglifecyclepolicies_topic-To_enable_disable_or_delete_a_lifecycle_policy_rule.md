Updated 2025-01-22
# Deleting or Disabling the Object Lifecycle Policy from Object Storage
Delete or disable a lifecycle policy for an Object Storage bucket.
The system stops running disabled or deleted rules immediately.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Lifecycle Policy Rules**.
    3. From the **Actions** menu for the lifecycle policy rule you want, select one of the following options:
       * **Disable** (is displayed only if the rule is enabled)
       * **Delete**
    4. (Delete only) When prompted, confirm the deletion.
If you disabled the lifecycle policy rule, the rule appears in the **Lifecycle Policy Rules** list displaying **Disabled** under the **State** column. If you deleted the rule, it no longer appears in the list.
  * Use the [oci os object-lifecycle-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/delete.html) command and required parameters to delete the object lifecycle policy of a bucket:
Command
CopyTry It
```
oci os object-lifecycle-policy delete --bucket-name bucket_name
```

For example:
Command
CopyTry It
```
oci os object-lifecycle-policy delete --bucket-name MyStandardTierBucket
Are you sure you want to delete this resource? [y/N]: y
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/DeleteObjectLifecyclePolicy) operation to delete the object lifecycle policy of a bucket.


Was this article helpful?
YesNo

