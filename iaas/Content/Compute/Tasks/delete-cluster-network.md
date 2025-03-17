Updated 2025-02-03
# Deleting a Cluster Network with Instance Pools
Delete (terminate) a cluster network that you no longer need.
**Caution** When you delete a cluster network, you permanently delete all resources within the cluster network, including associated instances and instance pools, attached boot volumes, and block volumes.
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. In the **List scope** section, select the compartment that contains the cluster network.
    3. Click the name of the cluster network that you want to delete.
    4. Click **Terminate** , and then confirm when prompted.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [cluster-network terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/terminate.html) command to delete a cluster network.
Copy
```
oci compute-management cluster-network terminate [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for compute management tasks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [TerminateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/TerminateClusterNetwork) operation to delete a cluster network and all of its associated resources.


Was this article helpful?
YesNo

