Updated 2025-02-03
# Renaming a Cluster Network with Instance Pools
Edit a cluster network with instance pools to give it a new name. 
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. In the **List scope** section, select the compartment that contains the cluster network.
    3. Click the name of the cluster network that you want to rename.
    4. Click **Edit**.
    5. Enter a new name. Avoid entering confidential information.
    6. Click **Save changes**.
  * Use the [cluster-network update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/update.html) command to rename a cluster network.
Copy
```
oci compute-management cluster-network update [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for compute management tasks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork) operation to rename a cluster network.


Was this article helpful?
YesNo

