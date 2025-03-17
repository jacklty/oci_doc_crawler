Updated 2025-01-15
# Monitoring Clusters
_Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine (OKE)._
Having created a cluster, you can monitor the overall status of the cluster itself, and the nodes and node pools within it.
In addition to monitoring the overall status of clusters, node pools, and nodes, you can monitor their health, capacity, and performance at a more granular level using **metrics** , **alarms** , and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").
## Using the Console 🔗 
To monitor a Kubernetes cluster:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
The **Status** column on the **Cluster List** page shows a summary status for each individual cluster and its control plane nodes. Clusters can have one of the following statuses:
Cluster Status | Explanation  | Possible Reason  
---|---|---  
Creating | Cluster is in the process of being created. | Application is being deployed.  
Active | Cluster is running normally. | Control plane nodes are running normally.  
Failed | Cluster is not running due to an unrecoverable error. |  Possible reasons:
     * a problem setting up load balancers 
     * conflicts in networking ranges   
Deleting | Cluster is in the process of being deleted. Application no longer required, so resources in the process of being released. | Application no longer required, so resources in the process of being released.   
Deleted | Cluster has been deleted. Application no longer required, so resources have been released. | Application no longer required, so resources have been released.   
Updating | Version of Kubernetes on the control plane nodes is in the process of being upgraded. | A newly supported version of Kubernetes has become available.  
Note that the cluster's summary status is not necessarily directly related to the status of node pools and nodes within the cluster.
  3. On the **Cluster List** page, click the name of the cluster for which you want to see detailed status.
  4. Display the cluster's **Metrics** tab to see more granular information about the health, capacity, and performance of the cluster. See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").
  5. Display the **Node Pools** tab to see the summary status of each node pool in the cluster.
  6. On the **Node Pools** tab, click the name of a node pool for which you want to see detailed status.
Node pools statuses include the following:
Node Pool Status | Explanation  | Possible Reason  
---|---|---  
Creating | Node pool is in the process of being created. | Cluster is in the process of being created.  
Active | Node pool is running normally. | Worker nodes in the node pool are running normally.  
Deleted | Node pool has been deleted. | Application no longer required, so resources have been released.  
Needs attention | At least one of the nodes in the node pool has an issue that requires investigation. | An attempt to terminate a node in the node pool (for example, to scale down the node pool) failed because the node could not be drained and cordoned within the eviction grace period. See [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain).  
  7. Display the node pool's **Metrics** tab to see more granular information about the health, capacity, and performance of the node pool. See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").
  8. Display the **Nodes** tab to see the summary status of each worker node in the node pool.
Worker nodes can have one of the following statuses: 
Node Status | Explanation  | Possible Reason  
---|---|---  
Creating | Node is being created. | Compute instance in the process of being created.  
Active | Node is running normally. | Node is running normally.  
Updating | Node is in the process of being updated. |  Kubernetes Engine is performing an operation on the node.  
Deleting | Node is in the process of being deleted. | Application no longer required, so resources in the process of being released.   
Deleted | Node has been deleted. | Application no longer required, so resources have been released.  
Inactive | Node still exists, but is not running. | Compute resource has a status of Stopped, Stopping, or Down For Maintenance.  
  9. Click **View Metrics** beside a worker node to see more granular information about the health, capacity, and performance of that node. See [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [GetCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/GetCluster) and [GetNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/GetNodePool) operations to monitor the status of Kubernetes clusters. 
Was this article helpful?
YesNo

