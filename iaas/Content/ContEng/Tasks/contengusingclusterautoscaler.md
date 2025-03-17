Updated 2024-11-04
# Using the Kubernetes Cluster Autoscaler
_Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine (OKE)._
**Note** You cannot use the Kubernetes Cluster Autoscaler with virtual node pools.
You can use the Kubernetes Cluster Autoscaler to automatically resize a cluster's managed node pools based on application workload demands. By automatically resizing a cluster's node pools, you can ensure application availability and optimize costs.
The Kubernetes Cluster Autoscaler:
  * Adds worker nodes to a node pool when a pod cannot be scheduled in the cluster because of insufficient resource constraints.
  * Removes worker nodes from a node pool when the nodes have been underutilized for an extended time, and when pods can be placed on other existing nodes. 


The Kubernetes Cluster Autoscaler increases or decreases the size of a node pool automatically based on resource requests, rather than on resource utilization of nodes in the node pool. 
The Kubernetes Cluster Autoscaler works on a per-node pool basis. You use a configuration file to specify which node pools to target for expansion and contraction, the minimum and maximum sizes for each node pool, and how you want the autoscaling to take place. Node pools not referenced in the configuration file are not managed by the Kubernetes Cluster Autoscaler.
To enable the Kubernetes Cluster Autoscaler to automatically resize a cluster's node pools based on application workload demands, always include resource request limits in pod specifications (`requests:` under `resources:`).
You can deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster in two ways:
  * as a standalone program (see [Working with the Cluster Autoscaler as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#Working_with_the_Cluster_Autoscaler "Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a standalone program to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine \(OKE\)."))
  * as a cluster add-on (see [Working with the Cluster Autoscaler as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on "Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a cluster add-on to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine \(OKE\)."))


For more information about the Kubernetes Cluster Autoscaler, see [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) and [Frequently Asked Questions](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) on GitHub.
## Recommendations when using the Kubernetes Cluster Autoscaler in Production Environments 🔗 
Consider the following recommendations:
  * Always have at least one node pool in a cluster that is not managed by the Kubernetes Cluster Autoscaler. This node pool is required to run critcal cluster add-ons. Also note that it is your responsibility to manually scale any node pools that are not managed by the Kubernetes Cluster Autoscaler.
  * Always define multiple replicas for the Kubernetes Cluster Autoscaler deployment in the configuration file. If there is only one replica and it is evicted and cannot be rescheduled, the Kubernetes Cluster Autoscaler is unable to create more worker nodes.
  * In the configuration file, set `max-node-provision-time` to 25 minutes. Typically, new worker nodes are provisioned and move to the Ready condition in significantly less time than this. However, when many nodes are added to a node pool at the same time, it can take longer to provision them. Note that the Console displays a warning beside worker nodes that take more than 20 minutes to initialize. Assuming worker nodes move to the Ready condition within the time you specify for `max-node-provision-time`, you can ignore the warning.
  * In the configuration file, you specify the maximum number of nodes allowed in the node pool. Make sure the maximum number of nodes you specify does not exceed the tenancy limit for the worker node shape defined for the node pool. The Kubernetes Cluster Autoscaler will never create more nodes than the tenancy limit. If you specify a number greater than the tenancy limit, the Kubernetes Cluster Autoscaler will periodically attempt to create additional nodes, but will not do so until the tenancy limit has been increased.
  * When defining clusters that you want the Kubernetes Cluster Autoscaler to manage, we recommend creating multiple node pools with one availability domain specified per node pool.
  * Always design applications to tolerate the disruptions that can occur when the Kubernetes Cluster Autoscaler removes worker nodes, or moves pods to a different worker node prior to removing an under-utilized worker node. For example, design applications that leverage pod disruption budgets (see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation).
  * Do not manually change node pools that are managed by the Kubernetes Cluster Autoscaler. For example, do not add or remove nodes using `kubectl`, or using the Console (or the Oracle Cloud Infrastructure CLI or API). The Kubernetes Cluster Autoscaler might override such changes, or they might modify its behavior. For example, if you want to remove all the nodes in a node pool managed by the Kubernetes Cluster Autoscaler, always use the Kubernetes Cluster Autoscaler to scale the node pool to zero.


## Supported Kubernetes Cluster Autoscaler Parameters 🔗 
You control how the Kubernetes Cluster Autoscaler resizes a cluster's node pools using configuration parameters. 
The configuration parameters you can use to manage clusters created by Kubernetes Engine, and how to specify them, depend on whether you are using the Kubernetes Cluster Autoscaler as a standalone program or as a cluster add-on.
  * **Using the Kubernetes Cluster Autoscaler as a standalone program**
If you are using the Kubernetes Cluster Autoscaler as a standalone program, you specify the configuration parameters in a configuration file.
When using the Kubernetes Cluster Autoscaler as a standalone program, you cannot use the following configuration parameters to manage clusters created by Kubernetes Engine:
    * `--node-group-auto-discovery `: Not supported (cloud provider specific).
    * `--node-autoprovisioning-enabled=true `: Not supported.
    * `--gpu-total `: Not supported (cloud provider specific).
    * `--expander=price `: Not supported (cloud provider specific).
Except for the above parameters, you can use any of the configuration parameters when using the Kubernetes Cluster Autoscaler as a standalone program.
For a full list of Kubernetes Cluster Autoscaler configuration parameters, see [What are the parameters to CA?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-the-parameters-to-ca) in the [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) on GitHub. 
  * **Using the Kubernetes Cluster Autoscaler as a cluster add-on**
If you are using the Kubernetes Cluster Autoscaler as a cluster add-on, you specify the configuration parameters in a configuration file (when using the CLI or API), or in the Console.
When using the Kubernetes Cluster Autoscaler as a cluster add-on, you cannot use the following configuration parameters to manage clusters created by Kubernetes Engine:
    * `--node-group-auto-discovery `: Not supported (cloud provider specific).
    * `--node-autoprovisioning-enabled=true `: Not supported.
    * `--gpu-total `: Not supported (cloud provider specific).
    * `--expander=price `: Not supported (cloud provider specific).
Note that a number of other Kubernetes Cluster Autoscaler configuration parameters are also not supported when using the Kubernetes Cluster Autoscaler as a cluster add-on.
For a list of the configuration parameters that are supported when using the Kubernetes Cluster Autoscaler as a cluster add-on, along with the names to use when specifying them, see [Cluster Autoscaler add-on configuration arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm#contengconfiguringclusteraddons-configurationarguments_ClusterAutoscaler).


## Notes about the Kubernetes Cluster Autoscaler 🔗 
Note the following:
  * The Kubernetes Cluster Autoscaler adds and removes nodes to and from existing node pools in existing clusters. More specifically, note that the Kubernetes Cluster Autoscaler:
    * Does not create additional clusters.
    * Does not create additional node pools. 
    * Does not create additional pods. Adding pods is supported by the Horizontal Pod Autoscaler (see [Using the Kubernetes Horizontal Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm#Using_Kubernetes_Horizontal_Pod_Autoscaler "Find out how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods on a cluster you've created using Kubernetes Engine \(OKE\).")).
    * Does not adjust CPU and memory requests and limits for containers. Adjusting limits is supported by the Vertical Pod Autoscaler (see [Using the Kubernetes Vertical Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingverticalpodautoscaler.htm#Using_the_Kubernetes_Vertical_Pod_Autoscaler "Find out how to use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in pods on a cluster you've created using Kubernetes Engine \(OKE\).")).
  * When removing worker nodes from a node pool, the Kubernetes Cluster Autoscaler respects pod scheduling and eviction rules. These rules can prevent the Kubernetes Cluster Autoscaler from removing a worker node. 
For example, by default, the Kubernetes Cluster Autoscaler will not remove nodes running kube-system pods (such as coredns pods), with the exception of DaemonSet or mirror pods. You can control this behavior using a configuration parameter (`skip-nodes-with-system-pods` when deployed as a standalone program, `skipNodesWithSystemPods` when deployed as a cluster add-on). The parameter is set to `true` by default.
For more information, see [What types of pods can prevent CA from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node) in the [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) on GitHub. 
  * If you are using both Terraform and the Kubernetes Cluster Autoscaler to manage node pools, note that Terraform might revert changes to the size of a node pool made by the Kubernetes Cluster Autoscaler. To prevent such behavior, use the Terraform `ignore_changes` feature, which is specifically intended for situations in which Terraform shares responsibility for managing a single object with another process. For example, when a resource is created with reference to data that might change in the future, but you don't want those potential data changes to affect the resource after its creation. The `ignore_changes` meta-argument specifies resource attributes that Terraform is to ignore when planning updates to the associated remote object. For more information, see [The Lifecycle Meta-Argument](https://www.terraform.io/docs/language/meta-arguments/lifecycle.html) in the Terraform documentation.
For example:
Copy
```
resource "node_pool_1" "example" {
 # ...
 lifecycle {
  ignore_changes = [
   node_config_details.size
  ]
 }
}
```

  * When you upgrade a cluster to a new version of Kubernetes, it is your responsibility to manually upgrade the Kubernetes Cluster Autoscaler to make it compatible with the cluster's new Kubernetes version. The Kubernetes Cluster Autoscaler is not upgraded automatically.
  * To use the Kubernetes Cluster Autoscaler to manage a cluster you have created with Kubernetes Engine, the cluster must be running certain versions of Kubernetes as follows:
    * When using the Kubernetes Cluster Autoscaler as a standalone program, clusters must be running Kubernetes version 1.17 or later.
    * When using the Kubernetes Cluster Autoscaler as a cluster add-on, clusters must be running Kubernetes version 1.25 or later.
  * You can use the Kubernetes Cluster Autoscaler with managed node pools, but not with virtual node pools.


Was this article helpful?
YesNo

