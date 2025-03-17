Updated 2025-01-15
# Performing an In-Place Managed Node Kubernetes Upgrade by Manually Replacing Nodes an Existing Node Pool
_Find out how to upgrade the Kubernetes version on managed nodes in a node pool by changing properties of the existing node pool, and then manually replacing each managed node in turn, using Kubernetes Engine (OKE)._
**Note** This section applies to managed nodes only. For information about upgrading self-managed nodes, see [Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm#contengupgradingselfmanagednodes "Find out how to upgrade the version of Kubernetes running on a self-managed node in an enhanced cluster created with Kubernetes Engine.").
You can upgrade the version of Kubernetes running on managed nodes in a node pool by specifying a more recent Kubernetes version for the existing node pool. 
You delete each managed node in turn, selecting appropriate cordon and drain options to prevent new pods starting and to delete existing pods. You start a new managed node to take the place of each managed node you delete. When new managed nodes start in the existing node pool, they run the more recent Kubernetes version you specified.
## Using the Console 🔗 
To perform an 'in-place' upgrade of a node pool in a cluster, by specifying a more recent Kubernetes version for the existing node pool:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster where you want to change the Kubernetes version running on managed nodes.
  4. On the **Cluster** page, display the **Node Pools** tab, and click the name of the node pool where you want to upgrade the Kubernetes version running on the managed nodes.
  5. On the **Node Pool** page, click **Edit** and in the **Version** field, specify the required Kubernetes version for managed nodes.
The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.
  6. Click **Save changes** to save the change.
You now have to delete existing managed nodes so that new managed nodes are started, running the Kubernetes version you specified.
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the deletion operation. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation.
  7. For the first managed node in the node pool:
    1. On the **Node Pool** page, display the **Nodes** tab and select **Delete Node** from the **Actions** menu beside the node you want to delete.
    2. Either accept the defaults for advanced options, or click **Show Advanced Options** and specify when and how to cordon and drain managed nodes before terminating them:
       * **Eviction grace period (mins):** The length of time to allow to cordon and drain managed nodes before terminating them. Either accept the default (60 minutes) or specify an alternative. For example, you might want to allow 30 minutes to cordon managed nodes and drain them of their workloads. To terminate managed nodes immediately, without cordoning and draining them, specify 0 minutes.
       * **Force terminate after grace period:** Whether to terminate managed nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected. 
Select this option if you always want managed nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.
De-select this option if you don't want managed nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing managed nodes that can't be terminated within the eviction grace period have the **Needs attention** status. The status of the work request that initiated the termination operation is set to **Failed** , and the termination operation is cancelled. For more information, see [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
       * **Decrease node pool size:** Do not select this option, so that a new worker node is started (rather than the node pool being scaled down).
For more information, see [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain).
    3. Click **Delete** to delete the managed node.
The managed node is deleted and a new managed node is started, running the Kubernetes version you specified.
  8. Repeat the previous step for each remaining managed node in the node pool, until all managed nodes in the node pool are running the Kubernetes version you specified.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
### To perform an 'in-place' managed node Kubernetes upgrade by manually terminating and replacing nodes 🔗 
First, update the node pool's worker node Kubernetes version property, and specify the OCID of the corresponding image:
Command
CopyTry It
```
oci ce node-pool update --node-pool-id <node-pool-ocid> --kubernetes-version <version> --node-image-id <image-ocid>
```

Then, delete each managed node in the node pool in turn, specifying that you want to start a new managed node to replace the managed node you have deleted
Command
CopyTry It
```
oci ce node-pool delete-node --node-pool-id <node-pool-ocid> --node-id <node-ocid> --is-decrement-size false
```

Was this article helpful?
YesNo

