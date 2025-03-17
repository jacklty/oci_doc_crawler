Updated 2025-02-03
# Tagging Cluster Networks
Tag cluster networks to help organize the resources.
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks-tagging-resources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks-tagging-resources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks-tagging-resources.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. Click the name of the cluster network that you want to tag.
    3. Click the **Tags** tab to view or edit the existing tags. Or click **Add tags** to add new tags.
  * Use the [cluster-network update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/update.html) command and required parameters to add or edit tags for cluster networks.
Copy
```
oci compute-management cluster-network update [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for Compute cluster networks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork) operation to manage tags for cluster networks.


Was this article helpful?
YesNo

