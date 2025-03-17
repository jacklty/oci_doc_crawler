Updated 2025-01-15
# Performing an In-Place Worker Node Update by Manually Replacing Nodes in an Existing Node Pool
_Find out how to update the properties of worker nodes in a node pool by changing properties of the existing node pool, using Kubernetes Engine (OKE)._
**Note** This section applies to managed nodes only.
You can update the properties of worker nodes in a node pool by changing properties of the existing node pool. 
You delete each worker node in turn, selecting appropriate cordon and drain options to prevent new pods starting and to delete existing pods. You start a new worker node to take the place of each worker node you delete. When new worker nodes start in the existing node pool, they have the properties you specified.
## Using the Console 🔗 
To perform an 'in-place' update of a node pool in a cluster:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster where you want to update worker node properties.
  4. On the **Cluster** page, display the **Node Pools** tab, and click the name of the node pool where you want to update worker node properties.
  5. On the **Node Pool** page, specify the required properties for worker nodes.
Note that if you change the Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See [Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).").
  6. Click **Save changes** to save the change.
You now have to delete existing worker nodes so that new worker nodes are started, with the properties you specified.
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the deletion operation. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation.
  7. For the first worker node in the node pool:
    1. On the **Node Pool** page, display the **Nodes** tab and select **Delete Node** from the **Actions** menu beside the node you want to delete.
    2. Either accept the defaults for advanced options, or select **Show Advanced Options** and specify when and how to cordon and drain worker nodes before terminating them:
       * **Eviction grace period (mins):** The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes) or specify an alternative. For example, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
       * **Force terminate after grace period:** Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected. 
Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.
De-select this option if you don't want worker nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that can't be terminated within the eviction grace period have the **Needs attention** status. The status of the work request that initiated the termination operation is set to **Failed** , and the termination operation is cancelled. For more information, see [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
       * **Decrease node pool size:** Do not select this option, so that a new worker node is started (rather than the node pool being scaled down).
For more information, see [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain).
    3. Click **Delete** to delete the worker node.
The worker node is deleted and a new worker node is started that has the properties you specified.
  8. Repeat the previous step for each remaining worker node in the node pool, until all worker nodes in the node pool have the required properties.


Was this article helpful?
YesNo

