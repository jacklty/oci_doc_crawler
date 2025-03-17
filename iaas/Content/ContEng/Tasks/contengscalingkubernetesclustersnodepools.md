Updated 2024-11-07
# Scaling Kubernetes Clusters and Node Pools
_Find out about scaling up and scaling down the Kubernetes node pools and clusters you've created using by Kubernetes Engine (OKE)._
You can scale the clusters you create using Kubernetes Engine to optimize resource usage. 
## Scaling Clusters with Managed Node Pools 🔗 
In the case of managed node pools, you have responsibility for adjusting cluster capacity in response to changing requirements. You can:
  * Change the number of managed node pools in a cluster to scale the cluster up and down (see [Adding and Removing Node Pools to Scale Clusters Up and Down](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm#contengscalingclusters "Find out how to add and remove node pools to scale up and scale down the Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")).
  * Change the number of managed nodes in a managed node pool to scale the node pool up and down (see [Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm#contengscalingnodepools "Find out how to scale up and scale down the node pools you've created using Kubernetes Engine \(OKE\).")).
  * Enable autoscaling to automatically scale managed node pools and pods (see [Autoscaling Kubernetes Node Pools and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengautoscalingclusters.htm#Autoscaling_Kubernetes_Node_Pools_and_Pods "Find out about autoscaling Kubernetes node pools and pods you've created using Kubernetes Engine \(OKE\).")).


## Scaling Clusters with Virtual Node Pools 🔗 
In the case of virtual node pools, much of the operational overhead of cluster capacity management is handled for you.
A virtual node pool scales automatically, and can support up to 500 pods per virtual node. 
In the event that 500 pods per virtual node is insufficient, you can:
  * Increase the number of virtual node pools in a cluster to scale up the cluster (see [Adding and Removing Node Pools to Scale Clusters Up and Down](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm#contengscalingclusters "Find out how to add and remove node pools to scale up and scale down the Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")).
  * Increase the number of virtual nodes in the virtual node pool to scale up the node pool (see [Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm#contengscalingnodepools "Find out how to scale up and scale down the node pools you've created using Kubernetes Engine \(OKE\).")). For the maximum number of virtual nodes, see [Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Container_Engine_for_Kubernetes_Limits).


Note that because virtual nodes automatically scale to support so many pods, it's not necessary to use the Kubernetes Cluster Autoscaler (which is not yet supported with virtual nodes in any case).
Was this article helpful?
YesNo

