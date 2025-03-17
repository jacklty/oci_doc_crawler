Updated 2024-08-14
# Considerations when Defining Enhanced Clusters with Large Numbers of Managed Nodes
_Find out about limits and other factors to consider when creating enhanced clusters using Kubernetes Engine (OKE)._
When defining an enhanced cluster, you can specify significantly more managed nodes per cluster than when defining a basic cluster. However, there are several limits to be aware of, including:
  * the maximum number of managed nodes per managed node pool allowed in an enhanced cluster
  * the maximum number of managed nodes allowed in an enhanced cluster


For the current values of these limits, see [Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Container_Engine_for_Kubernetes_Limits).
There are also a number of other factors to consider when you take advantage of the larger numbers of managed nodes allowed with enhanced clusters. We provide the following recommendations:
  * We recommend that you define a larger number of smaller node pools, rather than a smaller number of larger node pools. For example, if you want an enhanced cluster to have 2,000 managed nodes, we recommend that you define four node pools with 500 managed nodes in each, rather than two node pools with 1,000 managed nodes in each.
  * We recommend that you use a custom cloud-init script to configure extra options on the kubelet (see [Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengwritingcustomcloudinitscripts "Find out how to write custom cloud-init scripts to run on worker nodes in clusters you've created using Kubernetes Engine \(OKE\).")). These extra options are sometimes referred to as `kubelet-extra-args`. A number of the `kubelet-extra-args` options are particularly helpful when administering enhanced clusters with large numbers of managed nodes. For a full list of kubelet options, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/). 
  * We always recommend that you select only a subset of worker nodes to include as backend servers in the backend set of a given load balancer or network load balancer. By default, when Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer or network load balancer for a Kubernetes service of type LoadBalancer, all worker nodes in the cluster are included in the backend set as backend servers. However, there are limits on the number of backend servers allowed in a backend set, and the total number of backend servers (see [Limits on Load Balancing Resources](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#LimitsResources) and [Limits on Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#LimitsNLBResources)). Therefore, whether you are defining a basic cluster or an enhanced cluster, we always recommend that you select only a subset of worker nodes in the cluster to include in the backend set. Selecting only a subset of worker nodes is especially important if you are taking advantage of the larger numbers of managed nodes allowed with enhanced clusters. See [Selecting Worker Nodes To Include In Backend Sets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Selecting_worker_nodes_to_include_in_backend_sets).


Was this article helpful?
YesNo

