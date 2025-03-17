Updated 2024-08-14
# Autoscaler Best Practices
_Find out about best practices for using the Kubernetes Cluster Autoscaler (CA), Horizontal Pod Autoscaler (HPA), and Vertical Pod Autoscaler (VPA) with clusters you've created by Kubernetes Engine (OKE)._
This section contains best practices for using the Kubernetes Cluster Autoscaler (CA), Horizontal Pod Autoscaler (HPA), and Vertical Pod Autoscaler (VPA) with clusters created by Kubernetes Engine.
Autoscaling is a way to dynamically scale (both up and down) the number of computing resources that are being allocated to an application, based on the application's needs. You can use:
  * the Kubernetes Cluster Autoscaler to automatically resize a cluster's node pools based on application workload demands. 
  * the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods in a deployment.
  * the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits (such as CPU and Memory attributes) for containers running in a deployment's pods.


For more information, see [Autoscaling Kubernetes Node Pools and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengautoscalingclusters.htm#Autoscaling_Kubernetes_Node_Pools_and_Pods "Find out about autoscaling Kubernetes node pools and pods you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Manually manage at least one node pool for critical cluster add-ons 🔗 
We recommend that you always have at least one node pool in a cluster that is not managed by the Kubernetes Cluster Autoscaler. This node pool is required to run critical cluster add-ons. Also note that it is your responsibility to manually scale any node pools that are not managed by the Kubernetes Cluster Autoscaler.
We also recommend that you schedule application pods to run on user node pools, and run critical system pods (such as coredns pods) on dedicated system node pools. Separating application pods and system pods in this way prevents rogue application pods from accidentally killing system pods. Enforce this behavior by using the `CriticalAddonsOnly=true:NoSchedule` taint for system node pools.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Define multiple replicas 🔗 
We recommend that you always define multiple replicas for the Kubernetes Cluster Autoscaler deployment in the configuration file. If there is only one replica and it is evicted and cannot be rescheduled, the Kubernetes Cluster Autoscaler is unable to create more worker nodes.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Set max-node-provision-time 🔗 
We recommend that you set `max-node-provision-time` to 25 minutes in the configuration file. Typically, new worker nodes are provisioned and move to the Ready condition in significantly less time than this. However, when many nodes are added to a node pool at the same time, it can take longer to provision them. Note that the Console displays a warning beside worker nodes that take more than 20 minutes to initialize.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Specify maximum number of nodes in a node pool 🔗 
We recommend that you specify the maximum number of nodes allowed in the node pool in the configuration file. Make sure the maximum number of nodes you specify does not exceed the tenancy limit for the worker node shape defined for the node pool. The Kubernetes Cluster Autoscaler will never create more nodes than the tenancy limit. If you specify a number greater than the tenancy limit, the Kubernetes Cluster Autoscaler will periodically attempt to create additional nodes, but will not do so until the tenancy limit has been increased.
When defining clusters that you want the Kubernetes Cluster Autoscaler to manage, we recommend creating multiple node pools with one availability domain specified per node pool.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Specify multiple node pools with a different availability domain for each node pool 🔗 
We recommend that you specify multiple node pools (with a different availability domain for each node pool) when defining clusters that you want the Kubernetes Cluster Autoscaler to manage.
Specifying multiple node pools in different availability domains reduces the likelihood of the Kubernetes Cluster Autoscaler being unable to create worker nodes because a selected node shape is not available in a particular availability domain.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Use capacity reservations to provision worker nodes 🔗 
We recommend that you use capacity reservations to provision worker nodes. Using capacity reservations ensures that compute capacity is available for workloads when required during critical events, such as disaster recovery or unexpected workload spikes.
See [Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm#contengmakingcapacityreservations "Find out how to reserve compute capacity for clusters you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Design applications that leverage pod disruption budgets 🔗 
We recommend that you design applications to tolerate the disruptions that can occur when the Kubernetes Cluster Autoscaler removes worker nodes, or moves pods to a different worker node prior to removing an under-utilized worker node. 
For example, design applications that leverage pod disruption budgets.
See [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation.
## Best Practice: Avoid manually configuring node pools managed by the Kubernetes Cluster Autoscaler 🔗 
Avoid manually changing node pools that are managed by the Kubernetes Cluster Autoscaler. For example, do not add or remove nodes using `kubectl`, or using the Console (or the Oracle Cloud Infrastructure CLI or API). The Kubernetes Cluster Autoscaler might override such changes, or the changes might modify its behavior. 
If you want to remove all the nodes in a node pool managed by the Kubernetes Cluster Autoscaler, always use the Kubernetes Cluster Autoscaler to scale the node pool to zero.
See [Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler "Find out how to use the Kubernetes Cluster Autoscaler to automatically resize the managed node pools on a cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Avoid using the Kubernetes Horizontal Pod Autoscaler and Vertical Pod Autoscaler together 🔗 
We recommend that you do not use the Horizontal Pod Autoscaler and Vertical Pod Autoscaler together.
The Vertical Pod Autoscaler automatically adjusts the configuration of requests and limits, and aims to reduce overheads and achieve cost-savings. 
The Horizontal Pod Autoscaler scales the number of pods based on CPU or memory utilization, or on other metrics. The Horizontal Pod Autoscaler is more likely to increase rather than decrease the number of pods.
If you do use the Horizontal Pod Autoscaler and Vertical Pod Autoscaler together, double-check that their respective policies are not interfering with each other.
## Best Practice: Create recommendations without applying them during application development 🔗 
We recommend that you consider using the Vertical Pod Autoscaler when you are in the early stages of writing an application, simply to create recommendations (without updating pods). 
To simply create recommendations without applying them, set `updateMode: "Off"` in the `updatePolicy` section of the `VerticalPodAutoscaler` manifest. When pods are created, the Vertical Pod Autoscaler analyzes the CPU and memory needs of the containers and records those recommendations in its `Status` field. The Vertical Pod Autoscaler does not take any action to update the resource requests for the running containers.
See [Using the Kubernetes Vertical Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingverticalpodautoscaler.htm#Using_the_Kubernetes_Vertical_Pod_Autoscaler "Find out how to use the Kubernetes Vertical Pod Autoscaler to automatically adjust the resource requests and limits for containers running in pods on a cluster you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

