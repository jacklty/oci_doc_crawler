Updated 2024-12-18
# OKE Best Practices
Learn about OKE best practices for Compute Cloud@Customer. 
Use the best practices described in this topic to get the most from your Kubernetes Engine clusters.
## Cluster Management Best Practices 🔗 
**Use Kubernetes labels.**
Use Kubernetes labels to organize the many Kubernetes resources (such as services, pods, containers, and networks) that comprise a cluster.
Kubernetes labels are key-value pairs that help you to maintain these resources and keep track of how they interact with each other in a cluster.
**Use resource tagging.**
Use resource tagging to organize the many resources (such as worker nodes, VCNs, load balancers, and block volumes) used by the Kubernetes clusters you create with Kubernetes Engine.
When a large number of resources is spread across multiple compartments in a tenancy, it can be challenging to track the resources that are used for specific purposes. It can also be challenging to aggregate the resources, report on them, and take bulk actions on them.
Tagging enables you to define keys and values, and associate those tags with resources. You can then use the tags to organize and list resources based on your business needs.
For more information, see [Tagging Resources on Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/tagging.htm#tagging "On Compute Cloud@Customer, tagging enables you to add metadata to resources by defining key/value pairs that are assigned to resources. You can use the tags to organize and list resources based on your business needs.").
**Set resource requests and limits.**
  * Set resource requests to specify the minimum amount of resources a container can use.
  * Set resource limits to specify the maximum amount of resources a container can use.


Sometimes an application fails to deploy on a Kubernetes cluster due to limited availability of resources on that cluster. The failure of the application to deploy can be avoided by correctly setting resource requests and resource limits.
If you do not set resource requests and limits, pods in a cluster can start utilizing more resources than necessary. If a pod starts consuming more CPU or memory on a node, then the Kubernetes scheduler (`kube-scheduler`) might not be able to place new pods on the node, and the node might even crash.
For more information, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) on the `kubernetes.io` site.
**Provide dedicated nodes by using taints and tolerations.**
Use Kubernetes taints and tolerations to limit resource-intensive applications to specific worker nodes.
Using taints and tolerations enables you to keep node resources available for workloads that require them, and prevents the scheduling of other workloads on the nodes.
For more information, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) on the `kubernetes.io` site.
**Control pod scheduling by using node selectors and affinity.**
Several different methods are available to constrain a pod to run on particular nodes, or to specify a preference for a pod to run on particular nodes. The recommended approaches all use label selectors to specify the node selection.
Often, the `kube-scheduler` makes a reasonable placement when constraints and preferences are not specified. However, there are some circumstances where you might want to control the node on which a pod runs. In these situations, best practice is to control the scheduling of pods on nodes using Kubernetes node selectors, node affinity, and inter-pod affinity.
Using node selectors, node affinity, and inter-pod affinity enables the `kube-scheduler` to logically isolate workloads, such as according to the node's hardware.
**Use third-party tools for backup and disaster recovery.**
Use third-party tools such as [Velero](https://velero.io/) with Kubernetes Engine for backup and disaster recovery.
The combined backup and disaster recovery capabilities of these tools and Kubernetes Engine can provide a reliable, robust, and scalable Kubernetes platform that is production-ready.
## Networking Best Practices 🔗 
**Create separate compartments for each team.**
If you expect multiple teams to create clusters, create a separate compartment for each team.
**Size your VCN appropriately.**
Allow for possible future cluster and node pool scaling requirements when sizing the VCN in which you want to create and deploy Kubernetes clusters.
Ensure that the VCN has a CIDR block that is large enough to allocate network addresses to all the resources that a cluster requires: subnets, Kubernetes API endpoint, worker nodes, pods, load balancers.
**Select the pod networking CNI plugin that best suits your needs.**
Consider pod networking requirements carefully, and then select the pod networking CNI plugin that best suits your needs.
  * If applications require the use of base networking requirements (and not the use of IP addresses from the VCN), or require a high density of pods per worker node, best practice is to use the Flannel CNI plugin.
  * If applications require pods to have an IP address from the VCN CIDR, or require the consistent network performance offered by virtual machines (regardless of the nodes on which the pods are running) with no additional overlay, best practice is to use the OCI VCN-Native Pod Networking CNI plugin.


**Configure externalTrafficPolicy appropriately when exposing applications.**
Carefully consider the most appropriate value for the `externalTrafficPolicy` setting when provisioning a network load balancer for a Kubernetes service of type LoadBalancer.
**Avoid overlapping pod and service CIDR blocks with an on-premise CIDR block and when using the flannel CNI plugin.**
Avoid the situation where the CIDR block used by the flannel overlay network to provision pods and services with IP addresses overlaps with a CIDR block used to provision external compute instances with IP addresses.
Kubernetes clusters require a unique IP address for every pod. Therefore, IP address planning is necessary because addresses cannot overlap with the private IP address space used on-premises or in other connected VCNs.
**Plan the number of nodes you will need.**
Create a plan for the number of nodes in a cluster that takes into account node size, the application profile of pods, and the selected pod networking CNI plugin.
**Use separate subnets and security rules.**
Use separate subnets and security rules when configuring network resources. The VCN in which you want to create and deploy clusters must have at least two different subnets, and can have more:
  * A Kubernetes API endpoint subnet
  * A worker nodes subnet
  * One regional, or two AD-specific, load balancer subnets (optional)
  * A pods subnet (when using the OCI VCN-Native Pod Networking CNI plugin)
  * A bastion subnet (optional)


You can choose to combine the subnets, and also to combine security rules. However, this approach makes security harder to manage and is therefore not recommended unless you are using network security groups to control access to clusters.
## Security Best Practices 🔗 
**Plan exposure level.**
Answer the following questions before implementing a security plan for the clusters you create with Kubernetes Engine:
  * How much internet exposure do you want clusters to have?
  * How do you plan to expose workloads internally to your VCN, and externally to the internet?
  * How do you plan to scale workloads?
  * Which types of Oracle services will the cluster consume?


**Create private clusters.**
To expose workloads only internally to your VCN and not to the internet, create VCN-native clusters, with the Kubernetes API endpoint in a private subnet. Such clusters are sometimes referred to as private clusters.
**Place all applications in private subnets.**
To reduce the exposure of a service to the internet, place worker node compute instances running application workloads in private subnets and set up load balancers to access them.
**Restrict cluster traffic using Network Security Groups.**
Define security rules in network security groups (NSGs), rather than in security lists, for the VCN in which you want to create and deploy clusters.
**General security best practices.**
  * Apply security patches regularly.
  * Use a combination of Kubernetes network policies and NSGs.
  * Use NSGs in conjunction with infrastructure-as-code tools (such as Terraform).
  * Rotate secrets and certificates regularly.
  * Run all applications as a non-privileged user.
  * Treat containers as immutable.


**Auditing, logging, and monitoring.**
  * Check logs regularly.
  * Enable audit logging.
  * Use Kubernetes cluster-based logging.
  * Monitor cluster components.
  * Log network traffic metadata and analyze it regularly.
  * Use small and secure container images.
  * Limit credential exposure.


## Storage Best Practices 🔗 
  * Choose the appropriate storage type.
  * Create and use storage classes to define application needs.
  * Create and use volumes for persistent storage.
  * Limit storage resource consumption.
  * Secure and back up data.


## Upgrade Best Practices 🔗 
  * Use the latest supported version of Kubernetes.
  * Set up test and production environments.
  * Cordon and drain worker nodes in preparation for maintenance.
  * Treat worker nodes as immutable.


Was this article helpful?
YesNo

