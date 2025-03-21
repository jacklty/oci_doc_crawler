Updated 2024-08-23
# Kubernetes Engine (OKE) and Kubernetes Concepts
_Find out about the key concepts you need to understand before using Kubernetes Engine (OKE)._
This topic describes key concepts you need to understand when using Kubernetes Engine.
## Kubernetes Clusters 🔗 
A Kubernetes cluster is a group of nodes (machines running applications). Each node can be a physical machine or a virtual machine. The node's capacity (its number of CPUs and amount of memory) is defined when the node is created. A cluster comprises:
  * Control plane nodes (previously referred to as 'master nodes'). Typically, there will be three control plane nodes for high availability.
  * Worker nodes, organized into node pools.


When creating a cluster using Kubernetes Engine, you can create the new cluster as a basic cluster or as an enhanced cluster.
## Enhanced and Basic Clusters 🔗 
When creating a new cluster with Kubernetes Engine, you specify the type of cluster to create. You can specify:
  * **Enhanced cluster:** Enhanced clusters support all available features, including features not supported by basic clusters (such as virtual nodes, cluster add-on management, workload identity, and additional worker nodes per cluster). Enhanced clusters come with a financially-backed service level agreement (SLA).
  * **Basic cluster:** Basic clusters support all the core functionality provided by Kubernetes and Kubernetes Engine, but none of the enhanced features that Kubernetes Engine provides. Basic clusters come with a service level objective (SLO), but not a financially-backed service level agreement (SLA).


Note the following when creating clusters:
  * When using the Console to create a cluster, if you don't select any enhanced features during cluster creation, you have the option to create the new cluster as a basic cluster. A new cluster is created as an enhanced cluster by default, unless you explicitly choose to create a basic cluster.
  * When using the CLI or the API to create a cluster, you can specify whether to create a basic cluster or an enhanced cluster. If you don't explicitly specify the type of cluster to create, a new cluster is created as a basic cluster by default.


Creating a new cluster as an enhanced cluster enables you to easily add enhanced features later, even if you didn't select any enhanced features initially. If you do choose to create a new cluster as a basic cluster, you can still choose to upgrade the basic cluster to an enhanced cluster later on. However, you cannot downgrade an enhanced cluster to a basic cluster.
See [Comparing Enhanced Clusters with Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic "Find out about the differences between the enhanced clusters and basic clusters you can create using Kubernetes Engine \(OKE\).").
Note that all references to 'clusters' in the Kubernetes Engine documentation refer to both enhanced clusters and basic clusters, unless explicitly stated otherwise.
## Kubernetes Cluster Control Plane and Kubernetes API 🔗 
The Kubernetes cluster control plane implements core Kubernetes functionality. It runs on compute instances (known as 'control plane nodes') in the Kubernetes Engine service tenancy. The cluster control plane is fully managed by Oracle.
The cluster control plane runs a number of processes, including:
  * kube-apiserver to support Kubernetes API operations requested from the Kubernetes command line tool (kubectl) and other command line tools, as well as from direct REST calls. The kube-apiserver includes admissions controllers required for advanced Kubernetes operations. 
  * kube-controller-manager to manage different Kubernetes components (for example, replication controller, endpoints controller, namespace controller, and serviceaccounts controller)
  * kube-scheduler to control where in the cluster to run jobs
  * etcd to store the cluster's configuration data
  * cloud-controller-manager to update and delete worker nodes (using the node controller), to create load balancers when Kubernetes services of `type: LoadBalancer` are created (using the service controller), and to set up network routes (using the route controller). The oci-cloud-controller-manager also implements a container-storage-interface, a flexvolume driver, and a flexvolume provisioner (for more information, see the [OCI Cloud Controller Manager (CCM) documentation](https://github.com/oracle/oci-cloud-controller-manager) on GitHub). 


The Kubernetes API enables end users to query and manipulate Kubernetes resources (such as pods, namespaces, configmaps, and events). 
You access the Kubernetes API on the cluster control plane through an endpoint hosted in a subnet of your VCN. This Kubernetes API endpoint subnet can be a private or public subnet. If you specify a public subnet for the Kubernetes API endpoint, you can optionally expose the endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). You control access to the Kubernetes API endpoint subnet using security rules defined for network security groups (recommended) or security lists.
**Note**
In earlier releases, clusters were provisioned with public Kubernetes API endpoints that were not integrated into your VCN.
You can continue to create such clusters using the CLI or API, but not the Console. Note that you can only create these clusters as basic clusters, not as enhanced clusters.
## Kubernetes Worker Nodes, Node Pools, and the Cluster Data Plane 🔗 
Worker nodes constitute the cluster data plane. Worker nodes are where you run the applications that you deploy in a cluster.
Each worker node runs a number of processes, including:
  * kubelet to communicate with the cluster control plane
  * kube-proxy to maintain networking rules


The cluster control plane processes monitor and record the state of the worker nodes and distribute requested operations between them.
A node pool is a subset of worker nodes within a cluster that all have the same configuration. Node pools enable you to create pools of machines within a cluster that have different configurations. For example, you might create one pool of nodes in a cluster as virtual machines, and another pool of nodes as bare metal machines. A cluster must have a minimum of one node pool, but a node pool need not contain any worker nodes.
Worker nodes in a node pool are connected to a worker node subnet in your VCN.
When creating a node pool, you specify that the worker nodes in the node pool are either all created as virtual nodes, or all created as managed nodes. 
## Virtual Nodes and Managed Nodes 🔗 
When creating a node pool with Kubernetes Engine, you specify that the worker nodes in the node pool are to be created as one or other of the following:
  * Virtual nodes, fully managed by Oracle. Virtual nodes provide a 'serverless' Kubernetes experience, enabling you to run containerized applications at scale without the operational overhead of upgrading the data plane infrastructure and managing the capacity of clusters. You can only create virtual nodes in enhanced clusters.
  * Managed nodes, running on compute instances (either bare metal or virtual machine) in your tenancy, and at least partly managed by you. As you are responsible for managing managed nodes, you have the flexibility to configure them to meet your specific requirements. You are responsible for upgrading Kubernetes on managed nodes, and for managing cluster capacity. You can create managed nodes in both basic clusters and enhanced clusters.


See [Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengusingvirtualormanagednodes_topic "Find out about the differences between the virtual nodes and managed nodes you can create using Kubernetes Engine \(OKE\).").
Note that all references to 'nodes' and 'worker nodes' in the Kubernetes Engine documentation refer to both virtual nodes and managed nodes, unless explicitly stated otherwise.
## Self-Managed Nodes 🔗 
A self-managed node is a worker node hosted on a compute instance (or instance pool) that you've created yourself in Compute service, rather than on a compute instance that Kubernetes Engine has created for you. Self-managed nodes are often referred to as Bring Your Own Nodes (BYON). Unlike managed nodes and virtual nodes (which are grouped into managed node pools and virtual node pools respectively), self-managed nodes are not grouped into node pools. 
You use the Compute service to create the compute instances on which to host self-managed nodes. Using the Compute service enables you to configure compute instances for specialized workloads, including compute shape and image combinations that are not available for managed nodes and virtual nodes. For example, you might want instances with shapes designed for hardware-accelerated workloads (such as GPU shapes), or shapes designed for high-performance computing (HPC) workloads that require high frequency processor cores (such as HPC and Optimized shapes). You might want to connect many such instances with a high-bandwidth, ultra low-latency network to form an Oracle Cloud Infrastructure cluster network (see [Using RDMA Cluster Networks](https://docs.oracle.com/iaas/Content/Compute/References/high-performance-compute.htm#cluster-networks)). 
If you want to simplify administration and manage multiple self-managed nodes as a group, use the Compute service to create a compute instance pool to host one or more self-managed nodes.
When creating a compute instance (or instance pool) to host a self-managed node, you specify the Kubernetes cluster to which to add the instance. You can only add self-managed nodes to enhanced clusters.
For more information, see [Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm#contengworkingwithselfmanagednodes "Find out how to set up and use self-managed nodes with Kubernetes Engine.").
Note that all references to 'nodes' and 'worker nodes' in the Kubernetes Engine documentation cover self-managed nodes, unless explicitly stated otherwise.
## Pods 🔗 
Where an application running on a worker node comprises multiple containers, Kubernetes groups the containers into a single logical unit called a pod for easy management and discovery. The containers in the pod share the same networking namespace and the same storage space, and can be managed as a single object by the cluster control plane. A number of pods providing the same functionality can be grouped into a single logical set known as a service.
Kubernetes clusters use Container Network Interface (CNI) plugins to implement network connectivity for pods running on worker nodes. CNI plugins configure network interfaces, provision IP addresses, and maintain connectivity.
For more information about pods, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/).
## Services 🔗 
In Kubernetes, a service is an abstraction that defines a logical set of pods and a policy by which to access them. The set of pods targeted by a service is usually determined by a selector.
For some parts of an application (for example, frontends), you might want to expose a service on an external IP address outside of a cluster.
Kubernetes `ServiceTypes` enable you to specify the kind of service you want to expose. A `LoadBalancer ServiceType` creates an Oracle Cloud Infrastructure load balancer on load balancer subnets in your VCN.
For more information about services in general, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/). For more information about creating load balancer services with Kubernetes Engine, see [Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer.htm#Creating_Load_Balancers_to_Distribute_Traffic_Between_Cluster_Nodes "Find out how to create different types of load balancer to distribute traffic between the nodes of a cluster you've created using Kubernetes Engine \(OKE\).").
## Container Network Interface (CNI) plugins 🔗 
Kubernetes has adopted the Container Network Interface (CNI) specification for network resource management. The CNI consists of a specification and libraries for writing plugins to configure network interfaces in Linux containers, along with a number of supported plugins.
Kubernetes clusters use Container Network Interface (CNI) plugins to implement network connectivity for pods running on worker nodes. CNI plugins configure network interfaces, provision IP addresses, and maintain connectivity.
For more information, see the [CNI documentation on GitHub](https://github.com/containernetworking/cni).
## Manifest Files (or Pod Specs) 🔗 
A Kubernetes manifest file comprises instructions in a yaml or json file that specify how to deploy an application to the node or nodes in a Kubernetes cluster. The instructions include information about the Kubernetes deployment, the Kubernetes service, and other Kubernetes objects to be created on the cluster. The manifest is commonly also referred to as a pod spec, or as a deployment.yaml file (although other filenames are allowed). The parameters to include in a Kubernetes manifest file are described in the [Kubernetes documentation](https://kubernetes.io/docs/home/).
## Admission Controllers 🔗 
A Kubernetes admission controller intercepts authenticated and authorized requests to the Kubernetes API server before admitting an object (such as a pod) to the cluster. An admission controller can validate an object, or modify it, or both. Many advanced features in Kubernetes require an enabled admission controller. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).
The Kubernetes version you select when you create a cluster using Kubernetes Engine determines the admission controllers supported by that cluster. To find out the supported admission controllers, the order in which they run in the Kubernetes API server, and the Kubernetes versions in which they are supported, see [Supported Admission Controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengadmissioncontrollers.htm#Supported_Admission_Controllers "Find out about the admission controllers that are turned on in Kubernetes clusters you create using Kubernetes Engine \(OKE\).").
## Namespaces 🔗 
A Kubernetes cluster can be organized into namespaces, to divide the cluster's resources between multiple users. Initially, a cluster has the following namespaces:
  * default, for resources with no other namespace
  * kube-system, for resources created by the Kubernetes system
  * kube-node-lease, for one lease object per node to help determine node availability
  * kube-public, usually used for resources that have to be accessible across the cluster


For more information about namespaces, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).
Was this article helpful?
YesNo

