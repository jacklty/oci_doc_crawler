Updated 2025-01-30
# Editing the Object Lifecycle Policy in Object Storage
Update the object lifecycle policy for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Lifecycle Policy Rules**.
    3. From the **Actions** menu for the lifecycle policy rule you want, select **Edit**.
    4. Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see [Creating the Object Lifecycle Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#top "Create the object lifecycle policy for an Object Storage bucket.") for descriptions of the settings.
    5. Select **Save Changes**.
  * Use the [oci os object-lifecycle-policy put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/put.html) command and required parameters to edit the object lifecycle policy for a bucket:
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name bucket_name [OPTIONS]
```

Running this command for an existing lifecycle policy replaces the existing policy rules with an updated version that includes whatever changes to the configuration you make. See [Creating the Object Lifecycle Policy in Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#top "Create the object lifecycle policy for an Object Storage bucket.") for more information on configuring a lifecycle policy for a bucket.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [PutObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/PutObjectLifecyclePolicy) operation to edit the object lifecycle policy for a bucket. Running this operation for an existing lifecycle policy replaces the existing policy rules with an updated version that includes whatever changes to the configuration you make.
See [Creating the Object Lifecycle Policy in Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#top "Create the object lifecycle policy for an Object Storage bucket.") for more information on configuring a lifecycle policy for a bucket.


Was this article helpful?
YesNo

