Updated 2025-01-15
# Upgrading a Basic Cluster to an Enhanced Cluster
_Find out how to upgrade a basic cluster to an enhanced cluster using Kubernetes Engine (OKE)._
You can upgrade a basic cluster to an enhanced cluster, provided it is [VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters). A VCN-native cluster is a cluster with a Kubernetes API endpoint that is completely integrated into your own VCN. You cannot upgrade a basic cluster to an enhanced cluster if it is not VCN-native. For information about migrating a cluster to be VCN-native, see [Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#migrating_clusters_to_native_vcns "Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine \(OKE\).").
Note that after you upgrade a basic cluster to an enhanced cluster, you can't downgrade the enhanced cluster back to a basic cluster.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the basic cluster that you want to upgrade to an enhanced cluster.
The cluster details page shows **Cluster type: Basic**.
    4. Click **Upgrade to Enhanced Cluster**.
    5. Select the **Upgrade to Enhanced Cluster** option to confirm that want to upgrade the basic cluster to an enhanced cluster.
Note that after you upgrade a basic cluster to an enhanced cluster, you can't downgrade the enhanced cluster back to a basic cluster.
    6. Click **Upgrade**.
The basic cluster is upgraded to an enhanced cluster.
The cluster details page now shows **Cluster type: Enhanced**.
  * Use the [oci ce cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update.html) command and required parameters to upgrade a basic cluster to an enhanced cluster:
Command
CopyTry It
```
oci ce cluster update --cluster-id <cluster-ocid> --type ENHANCED_CLUSTER [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce cluster update --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --type ENHANCED_CLUSTER
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operation to upgrade a basic cluster to an enhanced cluster.


Was this article helpful?
YesNo

