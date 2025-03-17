Updated 2024-08-06
# Updating an OKE Cluster
On Compute Cloud@Customer, when you update an OKE cluster, you can change the cluster name, Kubernetes version, and tags.
**Note**
If you set or modify any of the following tags, the new values are ignored: SSH key (`OraclePCA`.sshkey), number of nodes (`OraclePCA`.cpNodeCount), node shape (`OraclePCA`.cpNodeShape), or node shape configuration (`OraclePCA`.cpNodeShapeConfig). These values can be set only when you create the cluster.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-kubernetes-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-kubernetes-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-a-kubernetes-cluster.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Containers** , then click **Kubernetes Clusters**.
    2. Click the name of the cluster that you want to update.
    3. At the top of the cluster details page, click **Edit**.
Don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the cluster resource.
    4. When you're finished making changes, click **Save Changes**.
    5. If a Kubernetes version update is available, a link labeled "Upgrade Available" is displayed next to the Kubernetes Version number on the cluster details page. Click that link to display a drop-down menu of versions that you can select.
  * Use the [oci ce cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update.html) command and required parameters to update the details of a cluster.
Copy
```
oci ce cluster update --cluster-id <cluster_OCID> [OPTIONS]
```

    1. Get the OCID of the cluster that you want to update: `oci ce cluster               list`
    2. Run the update cluster command.
If you specify the `--defined-tags` or `--freeform-tags` options, don't specify values for the `OraclePCA-OKE.cluster_id` defined tag or for the `ClusterResourceIdentifier` free-form tag. These tag values are system-generated and only applied to nodes (instances), not to the cluster resource.
Example:
Copy
```
$ oci ce cluster update --cluster-id ocid1.cluster.unique_ID \
--kubernetes-version newer_kubernetes_version --name new_cluster_name
        
```

For the value of the `--kubernetes-version` option, check [Supported Versions of Kubernetes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/container-engine-for-kubernetes.htm#container-engine-for-kubernetes__k8s-versions).
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operation to update the details of a cluster.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

