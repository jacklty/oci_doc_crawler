Updated 2025-02-03
# Tagging Resources
Apply tags to instance pools.
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-Tagging_Resources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-Tagging_Resources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-Tagging_Resources.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. Click the name of the instance pool for which you want to manage tags.
    3. Click the **Tags** tab to view or edit the existing tags. Or click **More Actions** , and then click **Add tags** to add new ones.
  * Use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command to add or manage tags for an instance pool.
Copy
```
oci compute-management instance-pool update --defined-tags [complex type]
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to add or manage tags for an instance pool.


Was this article helpful?
YesNo

