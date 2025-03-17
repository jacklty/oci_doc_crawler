Updated 2024-08-14
# Upgrading the Kubernetes Version on Worker Nodes in a Cluster
_Find out about the different ways to upgrade the Kubernetes version on worker nodes in clusters you've created with Kubernetes Engine (OKE)._
You upgrade managed nodes, self-managed nodes, and virtual nodes differently:
  * **Managed node upgrade:** You upgrade worker nodes in one of the following ways:
    * By performing an 'in-place' upgrade of a node pool in the cluster, specifying a more recent Kubernetes version for the existing node pool, and then cycling the nodes to automatically replace all existing worker nodes.
    * By performing an 'in-place' upgrade of a node pool in the cluster, specifying a more recent Kubernetes version for the existing node pool, and then manually replacing each existing worker node with a new worker node.
    * By performing an 'out-of-place' upgrade of a node pool in the cluster, replacing the original node pool with a new node pool for which you've specified a more recent Kubernetes version.
For more information about managed node upgrade, see [Upgrading Managed Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm#Upgrading_the_Kubernetes_Version_on_Worker_Nodes_in_a_Cluster "Find out about the different ways to upgrade the Kubernetes version on managed nodes in clusters you've created with Kubernetes Engine \(OKE\).").
  * **Self-managed node upgrade:** You upgrade self-managed nodes by replacing an existing self-managed node with a new self-managed node hosted on a new compute instance. For more information about self-managed node upgrade, see [Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm#contengupgradingselfmanagednodes "Find out how to upgrade the version of Kubernetes running on a self-managed node in an enhanced cluster created with Kubernetes Engine.").
  * **Virtual node upgrade:** You upgrade virtual nodes by upgrading the control plane nodes in a cluster. When you upgrade the Kubernetes version running on control plane nodes, the virtual nodes in every virtual node pool in the cluster are also automatically upgraded to that Kubernetes version. For more information about virtual node upgrade, see [Upgrading Virtual Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingvirtualnodes.htm#contengupgradingvirtualnodes "Find out how to upgrade the version of Kubernetes running on virtual nodes in an enhanced cluster created with Kubernetes Engine.").


Was this article helpful?
YesNo

