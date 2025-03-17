Updated 2025-02-12
# Networking Best Practices
_Find out about best practices for configuring networking options for clusters you've created with Kubernetes Engine (OKE)._
This section contains best practices for networking and Kubernetes Engine.
This section outlines the best practices for configuring networking options for Kubernetes clusters you create with Kubernetes Engine. This section is not intended to introduce Kubernetes networking concepts or terminology, and it assumes that you already have some level of Kubernetes networking knowledge. For more information, see [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).").
## Best Practice: Create separate compartments for each team 🔗 
We recommend that you create a separate compartment for each team if you expect multiple teams to create clusters.
For example, network resources like the Virtual Cloud Network (VCN) and subnets used for Kubernetes Engine can all reside in the root compartment. However, if you expect multiple teams to create clusters, we recommend that you create a separate compartment for each team's cluster resources (for example, as child compartments of the root compartment). The rationale being that since a cluster and its resources do not have to be in the same compartment as the VCN and the subnets, having separate compartments for each team makes it easier and cleaner to segregate clusters and keep them secure. 
See [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).").
## Best Practice: Size your VCN appropriately 🔗 
We recommend that you allow for possible future cluster and node pool scaling requirements when sizing the VCN in which you want to create and deploy Kubernetes clusters.
The VCN must have a CIDR block that is large enough to allocate network addresses to all the resources a cluster requires (subnets, Kubernetes API endpoint, worker nodes, pods, load balancers).
See [VCN Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#vcnconfig) and [IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengcidrblocks.htm#CIDR_Blocks_and_Container_Engine_for_Kubernetes "Find out about the CIDR blocks to specify when using Kubernetes Engine \(OKE\).").
## Best Practice: Select the pod networking CNI plugin that best suits your needs 🔗 
We recommend that you consider pod networking requirements carefully, and then select the pod networking CNI plugin that best suits your needs.
For example:
  * If applications require the use of base networking requirements (and not the use of IP addresses from the VCN), or require a high density of pods per worker node, we recommend using the Flannel CNI plugin. 
  * If applications require pods to have an IP address from the VCN CIDR, and/or require the consistent network performance offered by virtual machines (regardless of the nodes on which the pods are running) with no additional overlay, we recommend using the OCI VCN-Native Pod Networking CNI plugin.


See [Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm#podnetworking "Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine \(OKE\).") and [IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengcidrblocks.htm#CIDR_Blocks_and_Container_Engine_for_Kubernetes "Find out about the CIDR blocks to specify when using Kubernetes Engine \(OKE\).").
## Best Practice: Configure externalTrafficPolicy appropriately when exposing applications 🔗 
We recommend that you carefully consider the most appropriate value for the `externalTrafficPolicy` setting when provisioning a network load balancer for a Kubernetes service of type LoadBalancer:
  * **`externalTrafficPolicy: Cluster`(cluster mode)**
Specify cluster mode if you always want to route traffic to all pods running a service with equal distribution, and you do not want to preserve client IP addresses. In cluster mode, Kubernetes forwards any traffic sent to any worker node on a particular port to one of the pods of that service.
Cluster mode often results in less churn of backends in the cluster because request routing does not depend on the state of the pods in the cluster. Any request can be sent to any node, and Kubernetes handles getting the request to the right place. Cluster mode results in good load-spreading from the network load balancer across worker nodes. When traffic reaches a worker node, the node handles it the same way. The load balancer is not aware of which nodes in the cluster are running pods for its service. If you selected a regional subnet for worker nodes, the load is spread across all nodes in all availability domains for the subnet's region. In cluster mode, traffic is load-balanced across all nodes in the cluster, even nodes not running a relevant pod.
  * **`externalTrafficPolicy: Local`(local mode)**
Specify local mode if you want requests terminated at the client IP addresses specified in the IP packet headers. You only have the option to preserve client IP addresses when requests are terminated at the client IP addresses specified in the IP packet headers. That is, when the `externalTrafficPolicy` setting is set to `Local`.
Local mode removes the extra network hop required in cluster mode, but network traffic can potentially become imbalanced if the network is not configured properly. In local mode, ingress traffic must be sent to nodes that are running the corresponding pods for that service. Otherwise, the traffic is dropped. As a result, some application pods might receive more traffic than other pods.


For more information, see [Terminating Requests at the Receiving Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic-Preserve_source_destination) and [Preserving The Client IP Address](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic_Preserving_client_IP).
## Best Practice: Avoid overlapping pod and service CIDR blocks with an on-premise CIDR block and when using the flannel CNI plugin 🔗 
We recommend that you avoid the situation where the CIDR block used by the flannel overlay network to provision pods and services with IP addresses overlaps with a CIDR block used to provision external compute instances with IP addresses.
Kubernetes clusters require a unique IP address for every pod. Therefore, IP address planning is necessary because addresses cannot overlap with the private IP address space used on-premises or in other connected VCNs. 
When using the flannel CNI plugin, communication between pods in a cluster is encapsulated in the flannel overlay network. The flannel overlay network uses its own CIDR block to provision pods and worker nodes with IP addresses. The pods in the flannel overlay network are only accessible from other pods in the same cluster. External compute instances outside the cluster cannot access pods directly. If a pod attempts to access an external compute instance that has the same IP address as another pod in the cluster, the request will be routed incorrectly and problems will occur.
See [Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm#flannel_CNI_plugin "Find out about using the flannel CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
## Best Practice: Use regional subnets and distribute workloads for high availability 🔗 
We recommend that you select regional subnets for worker nodes to ensure high availability, and distribute workloads between them.
The VCN must have an appropriate number of subnets defined for worker nodes, load balancers, and the Kubernetes API endpoint. Using regional subnets, and distributing workloads between them, ensures high availability and makes failover across availability domains simpler to implement.
See [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig).
## Best Practice: Use topology spread constraints to control how pods are distributed 🔗 
We recommend that you use pod topology spread constraints to control how pods are distributed between availability domains and worker nodes. 
For example, when many worker nodes are available but only two or three pods are required, you typically do not want all the pods to run on the same worker node to avoid the risk of a single point-of-failure if there's a problem. 
However, as more and more pods are required for clients in several availability domains, you typically want to distribute the pods evenly across multiple worker nodes in those different availability domains. In this scenario, distributing the pods to reduce the latency and network costs associated with sending network traffic between availability domains is just as much of a concern as avoiding a single point-of-failure. You might prefer to have a similar number of pods in each availability domain, and have the cluster self-heal if there's a problem. 
Using pod topology spread constraints enables you to configure a cluster to meet the twin goals of high availability and efficient resource utilization.
See [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) in the Kubernetes documentation.
## Best Practice: Plan number of nodes 🔗 
We recommend that you have a plan in place for the number of nodes in a cluster that takes into account node size, the application profile of pods, and the selected pod networking CNI plugin.
When using the flannel CNI plugin, clusters created by Kubernetes Engine reserve a /25 range for pods from the flannel overlay network, and allow up to 110 pods per node. When using the OCI VCN-Native Pod Networking CNI plugin, the same node might have a different range based on the shape selected for worker nodes. Depending on the size of nodes and the application profile of pods, decide on the number of nodes you want in the cluster in advance.
See [Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm#podnetworking "Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
## Best Practice: Use separate subnets and security rules 🔗 
We recommend that you use separate subnets and security rules when configuring network resources. 
The VCN in which you want to create and deploy clusters must have at least two (optionally, more) different subnets:
  * a Kubernetes API endpoint subnet
  * a worker nodes subnet
  * one regional, or two AD-specific, load balancer subnets (optional)
  * a pods subnet (when using the OCI VCN-Native Pod Networking CNI plugin)
  * a bastion subnet (optional)


You can choose to combine the subnets, and also to combine security rules. However, this approach makes security harder to manage and is therefore not recommended unless you are using network security groups to control access to clusters.
See [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig).
## Best Practice: Use separate subnets for load balancers 🔗 
We recommend that you create separate subnets for load balancers to expose services.
If you don't create a separate load balancer subnet, services are exposed using an IP address from the worker node subnet. As a result, allocated space in the worker node subnet might be completely used up before you anticipated, which might prevent the cluster from scaling to the number of nodes you have specified.
The load balancer subnets can be either public or private subnets, depending on how applications deployed on the cluster will be accessed. If applications will be accessed internally from within your VCN, use private subnets for the load balancer subnets. If applications will be accessed from the internet, use public subnets for the load balancer subnets.
See [Load Balancer Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig__section_loadbalancersubnetconfig).
## Best Practice: Use a private worker node subnet for maximum security 🔗 
We recommend that you specify a private subnet as the worker node subnet for maximum security.
The worker node subnet can be either a single regional subnet or multiple AD-specific subnets (one in each of the availability domains). The worker node subnet can be either a public subnet or a private subnet. However, we recommend the worker node subnet is a private subnet for maximum security.
See [Worker Node Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig__section_f3f_p2b_s4b).
## Best Practice: Migrate clusters to be VCN-native to integrate the Kubernetes API endpoint into your VCN 🔗 
We recommend that you migrate clusters that are not already VCN-native to be VCN-native. 
In a VCN-native cluster, worker nodes, load balancers, and the Kubernetes API endpoint are fully integrated into your own VCN, and you can configure them as public or private. You can control access to the Kubernetes API endpoint subnet using security rules defined for network security groups (recommended) or security lists.
To take advantage of the security control offered by VCN-native clusters, migrate a cluster that is not already VCN-native to integrate its Kubernetes API endpoint into your own VCN.
See [Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#migrating_clusters_to_native_vcns "Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine \(OKE\).").
## Best Practice: Create a ConfigMap to override default CoreDNS behavior 🔗 
We recommend that if you want to customize default CoreDNS behavior, you create and apply your own ConfigMap to override settings in the CoreDNS Corefile.
Note that if you do customize default CoreDNS behavior, the customizations are periodically deleted during internal updates to the cluster.
See [Configuring DNS Servers for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringdnsserver.htm#Configuring_DNS_Servers_for_Kubernetes_Clusters "Find out how to configure DNS servers for Kubernetes clusters you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Use readiness and liveness probes for health checks 🔗 
We recommend that you use Kubernetes liveness and readiness probes to check the health of containers in a cluster, and that you customize the probes to meet your requirements. 
Managing large, distributed systems can be complicated, especially when something goes wrong. Kubernetes health checks are an easy way to make sure application instances are working. Creating custom health checks enables you to tailor the health checks to your environment.
In particular, we strongly recommend you consider using readiness and liveness probes to confirm that containers are running and functioning correctly before making them candidates to receive traffic from a service. The specific probe and probe parameters to use will depend on the workload. Strike a balance between making the probe too aggressive and too slow, and tune parameters to meet the needs of the application.
See [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) in the Kubernetes documentation.
## Best Practice: Use load balancer and network load balancer metrics to monitor backends 🔗 
We recommend that you use metrics to monitor the health of the OCI load balancer or network load balancer provisioned for a Kubernetes service of type LoadBalancer.
We also recommend that you set up alarms to alert you if backend availability falls below a threshold of your choosing. For example:
  * Use the load balancer `UnhealthyBackendServers` metric to set up an alarm to alert you if the number of unhealthy backend servers in a backend set rises above zero.
  * Use the load balancer `BackendTimeouts` metric to set up an alarm to alert you if the number of timeouts across all backend servers rises above zero.
  * Use the network load balancer `HealthyBackends` metric to set up an alarm to alert you if the number of backends that Oracle considers healthy falls below one.
  * Use the network load balancer `UnhealthyBackends` metric to set up an alarm to alert you if the number of backends that Oracle considers unhealthy rises above zero.


See [Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm), [Network Load Balancer Metrics](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/Metrics/metrics.htm), and [Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm).
## Best Practice: Use node labels to include a subset of worker nodes in a backend set 🔗 
We recommend that you use the `node-label-selector` annotation to include in the backend set of a given load balancer or network load balancer only that subset of worker nodes that have the required application pods. Including subsets of a cluster's worker nodes in the backend sets of different load balancers and network load balancers enables you to present a single Kubernetes cluster as multiple logical clusters (services).
Having attached a Kubenetes label to the worker nodes you want to include in the backend set of a load balancer or network load balancer, you specify that label in the manifest of the service of type LoadBalancer:
  * for a load balancer, use the annotation `oci.oraclecloud.com/node-label-selector:`
  * for a network load balancer, use the annotation `oci-network-load-balancer.oraclecloud.com/node-label-selector:`


For example:```
apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/node-label-selector: lbset=ServiceA
spec:
 type: LoadBalancer
...
```

You can then use node affinity to ensure application pods only run on worker nodes that are in the backend set of the appropriate load balancer or network load balancer. For example, the following manifest describes a pod that has a `requiredDuringSchedulingIgnoredDuringExecution` node affinity. The pod will only run on nodes that have the `lbset` label set to `ServiceA`:```
apiVersion: v1
kind: Pod
...
spec:
 affinity:
  nodeAffinity:
   requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchExpressions:
     - key: lbset
      operator: In
      values:
      - ServiceA
...
```

See [Selecting Worker Nodes To Include In Backend Sets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Selecting_worker_nodes_to_include_in_backend_sets).
## Best Practice: Install Calico before creating any node pools 🔗 
We recommend that if you want to use [Calico](https://www.tigera.io/project-calico/) to enhance cluster security, you install Calico on a cluster before creating any node pools. 
You can enhance cluster security by implementing Kubernetes network policies. To implement Kubernetes network policies, you have to install and configure a network provider that supports NetworkPolicy resources. One such provider is Calico.
If you install Calico on a cluster that has existing node pools in which pods are already running, you will have to recreate the pods when the Calico installation is complete. For example, by running the `kubectl rollout restart` command. If you install Calico on a cluster before creating any node pools in the cluster (as recommended), you can be sure that there will be no pods to recreate.
Note that only the use of open source Calico is supported. Use of Calico Enterprise is not supported.
See [Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm#Example_Installing_Calico_and_Setting_Up_Network_Policies "Find out how to install Calico and set up network policies on a cluster you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

