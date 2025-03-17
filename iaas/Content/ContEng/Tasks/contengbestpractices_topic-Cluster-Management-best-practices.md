Updated 2025-03-06
# Cluster Management Best Practices
_Find out about best practices for managing clusters you've created by Kubernetes Engine (OKE)._
This section contains best practices for cluster management and Kubernetes Engine.
## Best Practice: Use Kubernetes labels 🔗 
We recommend that you use Kubernetes labels to organize the many Kubernetes resources (such as services, pods, containers, networks) that comprise a cluster. 
Kubernetes labels are key-value pairs that help you to maintain these resources and keep track of how they interact with each other in a cluster.
For example, you can use the `oci.oraclecloud.com/oke-is-preemptible=true label` (which Kubernetes Engine applies to worker nodes hosted on preemptible instances) with Kubernetes node selectors and node affinity/anti-affinity to control which pods are scheduled on those worker nodes.
See [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/) in the Kubernetes documentation.
## Best Practice: Use OCI resource tagging 🔗 
We recommend that you use OCI resource tagging to organize the many resources (such as worker nodes, VCNs, load balancers, and block volumes) used by the Kubernetes clusters you create with Kubernetes Engine. When there are a large number of resources spread across multiple compartments in a tenancy, you can find it difficult to track the resources used for specific purposes. Equally, you can find it difficult to aggregate the resources, report on them, and take bulk actions on them. 
Tagging enables you to define keys and values, and associate them with resources. You can then use the tags to organize and list resources based on your business needs.
See [Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm#contengtaggingclusterresources "Find out about tagging cluster-related resources you create using Kubernetes Engine \(OKE\).").
## Best Practice: Set resource requests and limits 🔗 
We recommend that you set:
  * resource requests, to specify the minimum amount of resources a container can use
  * resource limits, to specify the maximum amount of resources a container can use


When working with a Kubernetes cluster, a common challenge is the occasional failure of an application to deploy on a cluster due to limited availability of resources on that cluster. The failure is caused by resource requests and resource limits not having been set.
If you do not set resource requests and limits, pods in a cluster can start utilizing more resources than necessary. If a pod starts consuming more CPU or memory on a node, then the kube-scheduler might not be able to place new pods on the node, and the node itself might even crash.
See [Requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) in the Kubernetes documentation.
## Best Practice: Reserve resources for Kubernetes and OS system daemons 🔗 
We recommend that you use the `--kube-reserved` and `--system-reserved` kubelet flags to reserve CPU and memory resources for Kubernetes system daemons (such as `kubelet` and `container runtime`) and OS system daemons (such as `sshd` and `systemd`) respectively. For example:
  * `--kube-reserved=cpu=500m,memory=1Gi`
  * `--system-reserved=cpu=100m,memory=100Mi`


Pods running on a worker node can consume all available CPU and memory resources, and so prevent other essential processes (such as the Kubernetes and OS system daemons) from running on the node. When Kubernetes and OS system daemons cannot run, the worker node can become unresponsive, unstable, and unexpectedly crash under heavy load. 
To prevent pods requesting resources that are required by the Kubernetes and OS system daemons, include the `--kube-reserved` and `--system-reserved` kubelet flags as `kubelet-extra-args` options in a custom cloud-init script. For more information and an example, see [Example 4: Using a Custom Cloud-init Script to Reserve Resources for Kubernetes and OS System Daemons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases__CustomCloudinitScriptExampleReserveResources).
When using the `--kube-reserved` kubelet flag to reserve a portion of a worker node's CPU and memory resources for use by Kubernetes system daemons, consider the following recommendations:
  * The amount of CPU resource that we recommend you reserve for Kubernetes system daemons depends on the number of CPU cores on the worker node, as shown in the following table:
Number of CPU cores on worker node | 1 | 2 | 3 | 4 | 5 | More than 5  
---|---|---|---|---|---|---  
Recommended CPU to reserve, in millicore (m) | 60 m | 70 m | 80 m | 85 m | 90 m | An additional 2.5 m for every additional core on worker node  
  * The amount of memory resource that we recommend you reserve for Kubernetes system daemons depends on the amount of memory on the worker node, as shown in the following table:
Memory on worker node, in GiB | 4 GiB | 8 GiB | 16 GiB | 128 GiB | More than 128 GiB  
---|---|---|---|---|---  
Recommended memory to reserve, in GiB |  1 GiB | 1 GiB | 2 GiB | 9 GiB | An additional 20 MiB for every additional GiB of worker node memory  


When using the `--system-reserved` kubelet flag to reserve a portion of a node's CPU and memory resources for use by OS system daemons, consider the following recommendations:
  * The amount of CPU resource that we recommend you reserve for OS system daemons (regardless of node shape) is 100 m (millicore).
  * The amount of memory resource that we recommend you reserve for OS system daemons (regardless of node shape) is 100 Mi (mebibytes).


Note that our CPU and memory recommendations for the `--kube-reserved` and `--system-reserved` kubelet flags might not be optimal for the workloads you intend to run, so you might need to alter the values accordingly. You might also need to adjust the values over time.
To see the difference between the total resources on a worker node and the resources on the node that workloads can use, run the following command:
```
kubectl get node <NODE_NAME> -o=yaml | grep -A 6 -B 7 capacity
```

Example output:
```
 allocatable:
  cpu: 15743m
  ephemeral-storage: "34262890849"
  hugepages-1Gi: "0"
  hugepages-2Mi: "0"
  memory: 234972476Ki
  pods: "110"
 capacity:
  cpu: "16"
  ephemeral-storage: 37177616Ki
  hugepages-1Gi: "0"
  hugepages-2Mi: "0"
  memory: 257197372Ki
  pods: "110"
```

The difference between the "capacity" and "allocatable" CPU and memory in the example output includes the CPU and memory reservations for the Kubernetes and OS system daemons.
**Note**
From June 2024, the recommendations for the CPU and memory resource reservations for Kubernetes and OS system daemons described in this section are used as the defaults for all OKE images, for all supported Kubernetes versions. The recommendations are also used as the defaults for all platform images for Kubernetes version 1.30 and later. The defaults apply both when you specify an OKE image released in June 2024 (or later), and when you upgrade the version of Kubernetes running on a cluster to version 1.30 (or later). If you specify an OKE image released in June 2024 (or later) or if you upgrade a cluster to Kubernetes version 1.30, we recommend that you check the default reservations are appropriate for the workloads you intend to run. 
Additional recommendations:
  * Before applying reservation changes to production clusters, always benchmark and test the impact of the reservation changes in a non-production environment.
  * Use the `--eviction-hard` or `--eviction-soft` kubelet flags to set appropriate thresholds for memory and disk pressure. When you set these thresholds, the Kubernetes system can protect system stability by evicting less important pods when necessary. For more information, see [Node-pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) in the Kubernetes documentation.
  * Be aware that reserving too many resources can lead to the under-utilization of nodes. Your goal is to find an appropriate balance between guaranteeing resource availability for critical components, and maximizing resource availability for workloads. We recommend that you start with larger resource reservations and gradually reduce reservation sizes based on observation, rather than starting with smaller resource reservations that are too low and run the risk of system instability. Use metrics from monitoring and alerting tools to observe the usage of resources by Kubernetes and system components over time.
  * When reserving resources, take account of differences in node shape and workload type. Large nodes might require larger absolute reservations than smaller nodes. Workloads with specific resource needs or known burst patterns might require larger or smaller resource reservations.


For more information about reserving resources, see [Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/) in the Kubernetes documentation.
## Best Practice: Provide dedicated nodes using taints and tolerations 🔗 
We recommend that you use Kubernetes taints and tolerations to limit resource-intensive applications to specific worker nodes. 
Using taints and tolerations enables you to keep node resources available for workloads that require them, and prevents the scheduling of other workloads on the nodes.
For example, when you create a cluster using Kubernetes Engine, you can define worker nodes to have a GPU shape, or a shape with a large number of powerful CPUs. These well-specified worker nodes are ideal for large data processing workloads. However, such specialized hardware is normally expensive to deploy. Consequently, you'll typically want to limit the workloads that can be scheduled on these nodes. To limit the workloads that can be scheduled on the well-specified worker nodes, add a taint to the nodes. For example, by running one of the following commands:
  * `kubectl taint nodes <node-name> special=true:NoSchedule`
  * `kubectl taint nodes <node-name> special=true:PreferNoSchedule`


Having added a taint to the well-specified worker nodes, add a corresponding toleration to the pods that you want to allow to use the nodes.
Similarly, you can use the `oci.oraclecloud.com/oke-is-preemptible=true label` (which Kubernetes Engine applies to worker nodes hosted on preemptible instances) with Kubernetes tolerations to control which pods are scheduled on those worker nodes.
See [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation.
## Best Practice: Control pod scheduling using node selectors and affinity 🔗 
There are several ways to constrain a pod to run on particular node(s), or to specify a preference for a pod to run on particular node(s). The recommended approaches all use label selectors to facilitate the selection. Often, the kube-scheduler will automatically do a reasonable placement without such constraints or preferences. However, there are some circumstances where you might want to control the node on which a pod runs.
In these situations, we recommend that you control the scheduling of pods on nodes using Kubernetes node selectors, node affinity, and inter-pod affinity.
Using node selectors, node affinity, and inter-pod affinity enables the kube-scheduler to logically isolate workloads, such as by the node's hardware. 
For example, you might give nodes a label to indicate that they have locally attached SSD storage. To specify a pod is to run only on nodes with locally attached SSD storage, you then include that label as a node selector in the pod specification. Kubernetes only schedules the pods on nodes with matching labels.
See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
## Best Practice: Use the OCI Full Stack Disaster Recovery service for backup and disaster recovery 🔗 
We recommend that you use the OCI Full Stack Disaster Recovery service with Kubernetes Engine for backup and disaster recovery. Full Stack Disaster Recovery is a cloud-native disaster recovery orchestration and management service that provides comprehensive disaster recovery capabilities for all layers of an application stack, including infrastructure, middleware, database, and applications.
When using Full Stack Disaster Recovery, you can add Kubernetes clusters that you have created with Kubernetes Engine to disaster recovery protection groups, enabling you to automate the end-to-end recovery orchestration of your Kubernetes system between OCI regions.
For more information, see the [Full Stack Disaster Recovery documentation](https://docs.oracle.com/iaas/disaster-recovery/index.html), and the following sections in particular:
  * [Preparing Kubernetes Engine (OKE) for Disaster Recovery](https://docs.oracle.com/iaas/disaster-recovery/doc/prepare-oke-disaster-recovery.html#CSSGM-GUID-8DD826BB-199D-4581-A23B-CA8B043E6509)
  * [Add an OKE Cluster to a Disaster Recovery Protection Group](https://docs.oracle.com/iaas/disaster-recovery/doc/add-oke-cluster-protection-group.html#CSSGM-GUID-040A10A8-4AC0-447F-815F-61B461B74C88)
  * the tutorial [Automate Switchover and Failover Plans for OCI Kubernetes Engine (Stateful) with OCI Full Stack Disaster Recovery](https://docs.oracle.com/en/learn/ocioke-plan-ocifsdr/index.html)


Note that before Full Stack Disaster Recovery was released, we previously recommended the use of third-party tools (such as [Kasten](https://www.kasten.io), [Rancher](https://www.rancher.com/), [Trilio](https://trilio.io/), or [Velero](https://velero.io/)) with Kubernetes Engine for backup and disaster recovery. If a third-party disaster recovery tool is already in place, you can continue to use it. However, we recommend you consider the benefits of OCI Full Stack Disaster Recovery as an alternative to third-party tools.
Was this article helpful?
YesNo

