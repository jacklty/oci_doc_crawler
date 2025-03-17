Updated 2024-08-14
# Managing Worker Node Capacity Types
_Find out about the different capacity types available for worker nodes when creating clusters using Kubernetes Engine (OKE)._
When using Kubernetes Engine, you choose a capacity type for the compute instances hosting worker nodes in node pools in the cluster. The capacity type you choose determines the availability of compute capacity to run workloads, and how much you pay for that compute capacity.
When defining a node pool, you choose from the following capacity types supported by the Compute service:
  * **On-demand capacity:** The default. Pay for only the compute capacity that you use. With on-demand capacity, you pay for compute capacity by the second, and [depending on the shape](https://docs.oracle.com/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm), you pay only for the seconds that your instances are running. Capacity availability is not guaranteed when launching large workloads.
  * **Reserved capacity:** Reserve capacity for future usage, and ensure that capacity is available to create Compute instances whenever you need them. The reserved capacity is used when you launch instances against the reservation. When these instances are terminated, the capacity is returned to the reservation, and the unused capacity in the reservation increases. Unused reserved capacity is metered differently than used reserved capacity. For more information, see [Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm#contengmakingcapacityreservations "Find out how to reserve compute capacity for clusters you've created using Kubernetes Engine \(OKE\).").
  * **Preemptible capacity:** Preemptible capacity allows you to save money by using preemptible instances to run workloads that only need to run for brief periods or that can be interrupted when the capacity is reclaimed. Preemptible instances behave the same as regular compute instances, but the capacity is reclaimed when it's needed elsewhere, and the instances are terminated. For more information, see [Using Preemptible Capacity to Provision Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpreemptiblecapacity.htm#contengusingpreemptiblecapacity "Find out how to specify preemptible capacity for compute instances hosting worker nodes in the node pools of clusters you've created using Kubernetes Engine \(OKE\).").


Note the following:
  * When using the Console to create a cluster, you can explicitly specify a node pool's **Capacity type** when using the 'Custom Create' workflow. When using the 'Quick Create' workflow, the default capacity type (On-demand capacity) is implicitly selected.
  * If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity type for each availability domain. However, Oracle recommends all worker nodes in the node pool have the same capacity type to make node pool management easier.
  * Any changes you make to worker node properties only apply to new worker nodes. Updating the capacity type associated with a node pool does not impact the properties of existing worker nodes.


Was this article helpful?
YesNo

