Updated 2024-08-14
# Updating Cluster Properties
_Find out how to modify properties of existing Kubernetes clusters you've created using Kubernetes Engine (OKE)._
You can use Kubernetes Engine to modify the properties of existing Kubernetes clusters.
You can change:
  * the name of a cluster
  * the number of node pools in a cluster by adding new node pools, or deleting existing node pools
  * the version of Kubernetes to run on control plane nodes
  * the enforcement of pod security policies
  * access details for a cluster's Kubernetes API endpoint
  * some properties of node pools and worker nodes (see [Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\)."))


However, note that you cannot change the master encryption key (if specified when the cluster was created).
Also note that you must not change the auto-generated names of resources that Kubernetes Engine has created (such as the names of worker nodes).
You can modify the properties of a cluster using the Console, the CLI and the API. See [Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm#update-cluster "Find out how to update a cluster using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

