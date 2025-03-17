Updated 2025-01-15
# Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster
_Find out how to upgrade the version of Kubernetes running on the control plane nodes of clusters that you create using Kubernetes Engine (OKE)._
When Kubernetes Engine supports a newer version of Kubernetes than the version currently running on the control plane nodes in a cluster, you can upgrade the Kubernetes version running on the control plane nodes.
To upgrade the Kubernetes version running on the control plane nodes in a cluster, all the worker nodes must be in a READY state. If the upgrade fails, review the failed CLUSTER_UPDATE work request for more information. See [Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.").
Note that when you upgrade the Kubernetes version running on control plane nodes, the virtual nodes in every virtual node pool in the cluster are also automatically upgraded to that Kubernetes version. For more information about virtual node upgrade, see [Upgrading Virtual Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingvirtualnodes.htm#contengupgradingvirtualnodes "Find out how to upgrade the version of Kubernetes running on virtual nodes in an enhanced cluster created with Kubernetes Engine.").
**Important** After you upgrade control plane nodes to a newer Kubernetes version, you can't downgrade the control plane nodes to an earlier Kubernetes version. So, before you upgrade the Kubernetes version running on the control plane nodes, test that applications deployed on the cluster are compatible with the new Kubernetes version.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster for which you want to upgrade the Kubernetes version running on the control plane nodes.
If a newer Kubernetes version than the one running on the control plane nodes in the cluster is available, the **New Kubernetes version available** button is enabled at the top of the cluster details page. 
    4. To upgrade the control plane nodes to a newer version, click **New Kubernetes version available** .
    5. In the **Upgrade cluster control plane** dialog box, select the Kubernetes version to which to upgrade the control plane nodes, and click **Upgrade**.
The Kubernetes version running on the control plane nodes is upgraded. The new Kubernetes version appears as an option when you're defining new node pools for the cluster.
  * Use the `ce cluster update` command and required parameters to upgrade control plane nodes:
Command
CopyTry It
```
oci ce cluster update --cluster-id <cluster-ocid> --kubernetes-version <kubernetes-version-number> [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce cluster update --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --kubernetes-version v1.24.1
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operation to upgrade the version of Kubernetes running on the control plane nodes.


Was this article helpful?
YesNo

