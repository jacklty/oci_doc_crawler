Updated 2024-08-14
# Deleting Kubernetes Clusters
_Find out about deleting Kubernetes clusters, and notes about cluster deletion, with Kubernetes Engine (OKE)._
You can delete a cluster, with its control plane nodes, worker nodes, and node pools.
Note the following considerations:
  * When you delete a cluster, no other resources created during the cluster creation process or associated with the cluster (such as VCNs, internet gateways, NAT gateways, route tables, security lists, load balancers, and block volumes) are deleted automatically. If you want to delete these resources, you must do so manually.
  * Kubernetes Engine creates the worker nodes in a cluster with automatically generated names. Managed node names have the following format: `oke-c<part-of-cluster-OCID>-n<part-of-node-pool-OCID>-s<part-of-subnet-OCID>-<slot>`. Virtual node names are the same as the node's private IP address. Do not change the automatically generated names of worker nodes. If you were to change the automatically generated name of a worker node and then delete the cluster, the renamed worker node would not be deleted. You would have to delete the renamed worker node manually. 


You can delete a cluster using the Console, the CLI and the API. See [Deleting a Kubernetes Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm#top "Find out how to delete an existing Kubernetes cluster that you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

