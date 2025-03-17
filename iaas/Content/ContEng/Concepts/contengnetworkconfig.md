Updated 2025-02-12
# Network Resource Configuration for Cluster Creation and Deployment
_Find out how to configure network resources to use Kubernetes Engine (OKE)._
Before you can use Kubernetes Engine to create and deploy clusters in the regions in a tenancy:
  * Within the tenancy, there must already be a compartment to contain the necessary network resources (such as a VCN, subnets, internet gateway, route table, network security groups and/or security lists). If such a compartment does not exist already, you will have to create it. Note that the network resources can reside in the root compartment. However, if you expect multiple teams to create clusters, best practice is to create a separate compartment for each team. 
  * Within the compartment, network resources (such as a VCN, subnets, internet gateway, route table, network security groups and/or security lists) must be appropriately configured in each region in which you want to create and deploy clusters. When creating a new cluster, you can have Kubernetes Engine automatically create and configure new network resources in the 'Quick Create' workflow. Alternatively, you can explicitly specify the existing network resources to use in the 'Custom Create' workflow. If you specify existing network resources, you or somebody else must have already configured those resources appropriately, as described in this topic.


This topic describes the necessary configuration for each network resource. To see details of a typical configuration, see [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
A number of related [Developer Tutorials](https://docs.oracle.com/iaas/developer-tutorials/tutorials/home.htm#home__kubernetes) are available.
## VCN Configuration 🔗 
The VCN in which you want to create and deploy clusters must be configured as follows:
  * The VCN must have a CIDR block defined that is large enough for all the resources a cluster requires (Kubernetes API endpoint, worker nodes, pods, load balancers). For example, for a VCN that supports IPv4-only addressing, a /16 CIDR block would be large enough for almost all use cases (10.0.0.0/16 for example). The CIDR block you specify for the VCN must not overlap with the CIDR block you specify for pods when using the flannel CNI plugin (see [Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm#flannel_CNI_plugin "Find out about using the flannel CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).")), and for the Kubernetes services (see [IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengcidrblocks.htm#CIDR_Blocks_and_Container_Engine_for_Kubernetes "Find out about the CIDR blocks to specify when using Kubernetes Engine \(OKE\).")).
  * The VCN must have an appropriate number of subnets defined for worker nodes, for load balancers, for the Kubernetes API endpoint, and for pods when using the OCI VCN-Native Pod Networking CNI plugin (see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).")). Best practice is to use regional subnets to make failover across availability domains simpler to implement. See [Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig).
  * The VCN must have security rules defined (in either or both network security groups and/or security lists for each subnet). See [Security Rule Configuration in Network Security Groups and/or Security Lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig). 
  * Oracle recommends DNS Resolution is selected for the VCN.
  * If you are using public subnets, the VCN must have an internet gateway. See [Internet Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#internetgatewayconfig).
  * If you are using private subnets, the VCN must have a NAT gateway and a service gateway. See [NAT Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#natgatewayconfig) and [Service Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#servicegatewayconfig).
  * If the VCN has a NAT gateway, service gateway, or internet gateway, it must have a route table with appropriate rules defined. See [Route Table Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#routetableconfig).


See [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
## Internet Gateway Configuration 🔗 
If you intend to use public subnets (for worker nodes, load balancers, and/or the Kubernetes API endpoint) and the subnets require access to/from the internet, the VCN must have an internet gateway. The internet gateway must be specified as the target for the destination CIDR block 0.0.0.0/0 as a route rule in a route table.
See [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
## NAT Gateway Configuration 🔗 
If you intend to use private subnets (for worker nodes, the Kubernetes API endpoint, or pods when using the OCI VCN-Native Pod Networking CNI plugin) and the subnets require access to the internet, the VCN must have a NAT gateway. For example, if you expect deployed applications to download software or to access third party services. 
The NAT gateway must be specified as the target for the destination CIDR block 0.0.0.0/0 as a route rule in a route table.
See [NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
## Service Gateway Configuration 🔗 
If you intend to use private subnets for worker nodes, the Kubernetes API endpoint, or pods when using the OCI VCN-Native Pod Networking CNI plugin, the VCN must have a service gateway.
Create the service gateway in the same VCN and compartment as the worker nodes subnet, the Kubernetes API endpoint subnet, or the pods subnet, and select the **All <region> Services in Oracle Services Network** option.
The service gateway must be specified as the target for **All <region> Services in Oracle Services Network** as a route rule in a route table.
See [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
## Route Table Configuration 🔗 
### Route Table for Worker Nodes Subnets 🔗 
If you intend to deploy worker nodes in a public subnet, the subnet route table must have a route rule that specifies the internet gateway as the target for the destination CIDR block 0.0.0.0/0.
If you intend to deploy worker nodes in a private subnet, the subnet route table must have:
  * a route rule that specifies the service gateway as the target for **All <region> Services in Oracle Services Network**
  * a route rule that specifies the NAT gateway as the target for the destination CIDR block 0.0.0.0/0


### Route Table for Kubernetes API Endpoint Subnets 🔗 
If you intend to deploy the Kubernetes API endpoint in a public subnet, the subnet route table must have a route rule that specifies the internet gateway as the target for the destination CIDR block 0.0.0.0/0.
If you intend to deploy the Kubernetes API endpoint in a private subnet, the subnet route table must have:
  * a route rule that specifies the service gateway as the target for **All <region> Services in Oracle Services Network**
  * a route rule that specifies the NAT gateway as the target for the destination CIDR block 0.0.0.0/0


### Route Table for Load Balancer Subnets 🔗 
If you intend to deploy load balancers in public subnets, the subnet route table must have a route rule that specifies the internet gateway as the target for the destination CIDR block 0.0.0.0/0.
If you intend to deploy load balancers in private subnets, the subnet route table can be empty.
### Route Table for Pods Subnet
If you intend to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, deploy pods in a private subnet. The subnet route table must have:
  * a route rule that specifies the service gateway as the target for **All <region> Services in Oracle Services Network**
  * a route rule that specifies the NAT gateway as the target for the destination CIDR block 0.0.0.0/0


If you intend to use the flannel CNI plugin for pod networking, a pod subnet is not required.
### Notes about Route Table Configuration 🔗 
  * To avoid the possibility of asymmetric routing, a route table for a public subnet cannot contain both a route rule that targets an internet gateway as well as a route rule that targets a service gateway (see [Issues with access to your public instances from Oracle services through a service gateway](https://docs.oracle.com/iaas/Content/Network/Reference/known_issues_for_networking.htm#sgw-route-rule-conflict)).
  * For more information about setting up route tables, see:
    * [Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)
    * [NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)
    * [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)
    * [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).")


## DHCP Options Configuration 🔗 
The VCN in which you want to create and deploy clusters must have DHCP Options configured. The default value for **DNS Type** of Internet and VCN Resolver is acceptable.
See [DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
## Subnet Configuration 🔗 
The characteristics of the cluster you want to create will determine the number of subnets to configure. Best practice is to use regional subnets to make failover across availability domains simpler to implement.
The VCN in which you want to create and deploy clusters must have at least two (optionally, more) different subnets:
  * a Kubernetes API endpoint subnet
  * a worker nodes subnet
  * one regional, or two AD-specific, load balancer subnets (optional) 
  * a pods subnet (when using VCN-native pod networking)
  * a bastion subnet (optional)


You can choose to combine the subnets, and also to combine security rules. However, this approach makes security harder to manage and is therefore not recommended unless you are using network security groups to control access to clusters.
The subnet CIDR blocks must not overlap with CIDR blocks you specify for pods running in the cluster (see [IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengcidrblocks.htm#CIDR_Blocks_and_Container_Engine_for_Kubernetes "Find out about the CIDR blocks to specify when using Kubernetes Engine \(OKE\).")).
Virtual nodes and managed nodes have different requirements, so you have to configure worker node subnets and pod subnets slightly differently when using virtual nodes rather than managed nodes.
The subnets must be configured with the following properties:
  * **Route Table:** see [Route Table Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#routetableconfig)
  * **DHCP options:** see [DHCP Options Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#dhcpconfig)
  * **Network Security Groups and/or Security List:** see [Security Rule Configuration in Network Security Groups and/or Security Lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig)


See [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm) and [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).").
### Kubernetes API Endpoint Subnet Configuration 🔗 
The Kubernetes API endpoint subnet hosts an endpoint that provides access to the Kubernetes API on the cluster control plane.
The Kubernetes API endpoint subnet must be a regional subnet, and can be a private or a public subnet:
  * If you specify a public subnet for the Kubernetes API endpoint, you can optionally expose the endpoint to the internet by assigning a public IP address to the endpoint. The public IP address enables third party cloud services (such as SaaS CI/CD services) to access the Kubernetes API endpoint. Note the following:
    * If the Kubernetes API endpoint has a public IP address, route rules and security rules must exist to enable access to the endpoint using an internet gateway (see [Example 1: Cluster with Flannel CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-flannel-cni-publick8sapi_privateworkers_publiclb) and [Example 3: Cluster with OCI CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-oci-cni-publick8sapi_privateworkers_publiclb)). 
    * If the Kubernetes API endpoint does not have a public IP address, route rules and security rules must exist to enable access to the endpoint using a service gateway and a NAT gateway ( see [Example 2: Cluster with Flannel CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-flannel-cni-privatek8sapi_privateworkers_publiclb) and [Example 4: Cluster with OCI CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-oci-cni-privatek8sapi_privateworkers_publiclb)).
    * After you have created a cluster, you can subsequently change whether a public IP address is assigned to the Kubernetes API endpoint. If you do change whether a public IP address is assigned to the endpoint, note that you also have to update route rules and security rules appropriately.
  * If you specify a private subnet for the Kubernetes API endpoint, traffic can access the Kubernetes API endpoint subnet from another subnet in your VCN, from another VCN, or from your on-premise network (peered with FastConnect). You can also set up a bastion host on a public subnet to reach the Kubernetes API endpoint (see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).")).


### Worker Node Subnet Configuration 🔗 
A worker node subnet hosts worker nodes. All the managed nodes in a node pool belong to the same worker node subnet.
The worker node subnet can be either a single regional subnet or multiple AD-specific subnets (one in each of the availability domains). 
**Managed/Self-managed nodes:** The worker node subnet can be either a public subnet or a private subnet. However, we recommend the worker node subnet is a private subnet for maximum security.
**Virtual nodes:** The worker node subnet can be either a public subnet or a private subnet. However, we recommend the worker node subnet is a private subnet for maximum security. We also recommend the worker node subnet and the pod subnet are the same subnet (in which case, the worker node subnet must be a private subnet because virtual nodes require that the pod subnet is a private subnet).
### Pod Subnet Configuration
A pod subnet hosts the pods on the worker nodes in a node pool when using VCN-native pod networking (see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).")).
The pod subnet must be a single regional subnet.
**Managed nodes:** The pod subnet must be a private subnet.
**Virtual nodes:** The pod subnet must be a private subnet. We recommend the pod subnet and the worker node subnet are the same subnet (in which case, the worker node subnet must also be a private subnet).
### Load Balancer Subnet Configuration 🔗 
Load balancer subnet(s) connect Oracle Cloud Infrastructure load balancers created by Kubernetes services of type `LoadBalancer`. 
The load balancer subnets can be single regional subnets or AD-specific subnets (one in each of the availability domains). However, we recommend regional subnets. 
The load balancer subnets can be either public or private subnets, depending on how applications deployed on the cluster will be accessed. If applications will be accessed internally from within your VCN, use private subnets for the load balancer subnets. If applications will be accessed from the internet, use public subnets for the load balancer subnets.
### Bastion Subnet Configuration (Optional) 🔗 
An optional bastion in a bastion subnet can provide secure access to the Kubernetes API endpoint, and SSH access to worker nodes. See [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").
## Security Rule Configuration in Network Security Groups and/or Security Lists  🔗 
The VCN in which you want to create and deploy clusters must have security rules defined. You can define the security rules in either or both the following ways:
  * In **Network security groups** (recommended) that you select for node pools, for the Kubernetes API endpoint, for pods (when using VCN-native pod networking), and for load balancers (if specified) when you create a cluster.
  * In **Security lists** that are already associated with the subnets that you select for the worker nodes, for the Kubernetes API endpoint, for pods (when using VCN-native pod networking), and for load balancers (if specified) when you create a cluster.


The worker nodes, Kubernetes API endpoint, pods (when using VCN-native pod networking), and load balancer have different security rule requirements, as described in this topic. You can add additional rules to meet your specific needs.
If you specify security rules in both network security groups and security lists, all the security rules are applied (that is, the union of the security rules).
For more information, see:
  * [Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#Example_Network_Resource_Configurations "Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine \(OKE\).")
  * [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
  * [Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)
  * [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)


### Security Rules for the Kubernetes API Endpoint 🔗 
The following ingress rules must be defined for the Kubernetes API endpoint, in a network security group (recommended) and/or in a security list:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Worker Nodes CIDR | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | Worker Nodes CIDR | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | Pods CIDR | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | Pods CIDR | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | Worker Nodes CIDR | ICMP 3,4 | Path Discovery.  
The following optional ingress rules can be defined for the Kubernetes API endpoint, in a network security group (recommended) and/or in a security list:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or specific subnets | TCP/6443 | Client access to Kubernetes API endpoint  
The following egress rules must be defined for the Kubernetes API endpoint, in a network security group (recommended) and/or in a security list:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | All <region> Services in Oracle Services Network | TCP/443 | Allow Kubernetes API endpoint to communicate with OKE.  
Stateful | Worker Nodes CIDR | TCP/ALL | All traffic to worker nodes (when using flannel for pod networking).  
Stateful | Pods CIDR | ALL/ALL |  Kubernetes API endpoint to pod communication (when using VCN-native pod networking).  
Stateful | Worker Nodes CIDR | ICMP 3,4 | Path Discovery.  
Stateful | Worker Nodes CIDR | TCP 10250,ICMP | Kubernetes API endpoint to worker node communication (when using VCN-native pod networking).   
### Security Rules for Worker Nodes 🔗 
Worker nodes are created with public or private IP addresses, according to whether you specify public or private subnets when defining the node pools in a cluster. Kubernetes Engine must be able to access worker nodes.
The following ingress rules must be defined for worker nodes, in a network security group (recommended) and/or in a security list:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Worker Nodes CIDR | ALL/ALL | Allows communication from (or to) worker nodes.  
Stateful | Pods CIDR | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes (when using VCN-native pod networking).  
Stateful | Kubernetes API Endpoint CIDR | TCP/ALL | Allow Kubernetes API endpoint to communicate with worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | Kubernetes API Endpoint CIDR | TCP 10250,ICMP | Kubernetes API endpoint to worker node communication (when using VCN-native pod networking).   
The following optional ingress rules can be defined for worker nodes (managed nodes only), in a network security group (recommended) and/or in a security list:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or subnet CIDR | TCP/22 | (optional) Allow inbound SSH traffic to worker nodes.  
The following egress rules must be defined for worker nodes, in a network security group (recommended) and/or in a security list:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Worker Nodes CIDR | ALL/ALL | Allows communication from (or to) worker nodes.  
Stateful | Pods CIDR | ALL/ALL | Allow worker nodes to communicate with pods on other worker nodes (when using VCN-native pod networking).  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow nodes to communicate with OKE.  
Stateful | Kubernetes API Endpoint CIDR | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | Kubernetes API Endpoint CIDR | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
The following optional egress rules can be defined for worker nodes, in a network security group (recommended) and/or in a security list:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 | TCP/ALL | (optional) Allow worker nodes to communicate with internet.  
### Security Rules for Pod Subnets 🔗 
When using the OCI VCN-Native Pod Networking CNI plugin for pod networking:
  * the security rules defined for the worker node subnet, in a network security group (recommended) and/or in a security list, must include:
    * Stateful ingress and egress rules that allow all traffic between worker nodes
    * Stateful ingress and egress rules that allow all traffic between worker nodes and load balancer
    * Stateful egress rules that allow traffic between worker nodes and Kubernetes Engine
  * the security rules defined for the pod subnet, in a network security group (recommended) and/or in a security list, must include stateful ingress and egress rules that allow all traffic between pods


The following ingress rules must be defined for pod subnets, in a network security group (recommended) and/or in a security list:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Kubernetes API Endpoint CIDR | ALL/ALL | Kubernetes API endpoint to pod communication (when using VCN-native pod networking).  
Stateful | Worker Nodes CIDR | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes.  
Stateful | Pods CIDR | ALL/ALL | Allow pods to communicate with each other.  
The following egress rules must be defined for pod subnets, in a network security group (recommended) and/or in a security list:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Pods CIDR | ALL/ALL | Allow pods to communicate with each other.  
Stateful | All <region> Services in Oracle Services Network | ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow worker nodes to communicate with OCI services.  
Stateful | Kubernetes API Endpoint CIDR | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | Kubernetes API Endpoint CIDR | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
The following optional egress rules can be defined for a pod subnet, in a network security group (recommended) and/or in a security list:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 | TCP/443 | (optional) Allow pods to communicate with internet.  
### Security Rules for Load Balancers and Network Load Balancers 🔗 
When Kubernetes Engine provisions an OCI load balancer or network load balancer for a Kubernetes service of type LoadBalancer, appropriate security rules must exist to allow inbound and outbound traffic to and from the load balancer's or network load balancer's subnet. In the case of managed nodes (not virtual nodes), these security rules are created automatically by default for load balancers, but are not created automatically by default for network load balancers. For more information about provisioning an OCI load balancer or network load balancer for a Kubernetes service of type LoadBalancer, see [Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer.htm#Creating_Load_Balancers_to_Distribute_Traffic_Between_Cluster_Nodes "Find out how to create different types of load balancer to distribute traffic between the nodes of a cluster you've created using Kubernetes Engine \(OKE\).").
You can define ingress and egress security rules for the subnet in a network security group (recommended) and/or in a security list. For more information, see:
  * [Specifying Network Security Groups (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Load_Balancer_Network_Security_Group)
  * [Specifying Security List Management Options When Provisioning an OCI Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#listmgmt)
  * [Specifying Security List Management Options When Provisioning an OCI Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingloadbalancer_topic_Specifying_Network_Load_Balancer_Security_List_Management_Options)


Define the following ingress security rule in either or both:
  * a network security group (recommended) to which the load balancer or network load balancer resource have been added
  * a security list associated with the load balancer's or network load balancer's subnet


State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or specific CIDR | TCP/443 | Allow inbound traffic to Load Balancer.  
Set the ingress rule's **Protocol** and **Destination Port** appropriately for specific application requirements. For example, specify UDP as the protocol for an application that handles UDP traffic.
Define the following egress security rule in either or both:
  * a network security group (recommended) to which the load balancer or network load balancer resource have been added
  * a security list associated with the load balancer's or network load balancer's subnet


State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Worker nodes CIDR | ALL/30000-32767 | Allow traffic to worker nodes.  
By default, OCI load balancers or network load balancers provisioned by Kubernetes Engine proxy requests to all worker nodes in the cluster. When requests are proxied to worker nodes in the cluster, the following ingress and egress security rules must exist (in a network security group (recommended) and/or in a security list) for the load balancer or network load balancer to communicate with the worker nodes on port 10256 (the kube-proxy health port):
  * Ingress security rule for worker node subnet's security list (or network security group) to enable the load balancer or network load balancer to communicate with kube-proxy on worker nodes:
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Load balancer or network load balancer subnet CIDR | ALL/10256 | Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes.  
  * Egress security rule for load balancer or network load balancer subnet's security list (or network security group) to enable the load balancer or network load balancer to communicate with kube-proxy on worker nodes:
State | Destination | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | Worker node subnet CIDR | ALL/10256 | Allow OCI load balancer or network load balancer to communicate with kube-proxy on worker nodes.  


When provisioning a network load balancer for a Kubernetes service of type LoadBalancer:
  * You can specify that requests terminate at the client IP address specified in the headers of IP packets, rather than being proxied to other worker nodes in the cluster (by setting `externalTrafficPolicy: Local`). See [Terminating Requests at the Receiving Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic-Preserve_source_destination). 
  * If you specify that requests terminate at the client IP address, you can also specify whether to preserve the client IP address in the headers of IP packets (by using the `oci-network-load-balancer.oraclecloud.com/is-preserve-source` annotation). See [Preserving The Client IP Address](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingnetworkloadbalancers.htm#contengcreatingnetworkloadbalancer_topic_Preserving_client_IP).


Note that in both cases, you must have set up a security rule (in a network security group (recommended) and/or in a security list) for the worker nodes in the cluster to allow ingress traffic from the CIDR block where the client connections are made, to all node ports (30000 to 32767). If the application is exposed to the Internet, set the security rule's **Source** CIDR block to 0.0.0.0/0. Alternatively, set the security rule's **Source** CIDR block to a specific CIDR block (for example, if the client connections come from a specific subnet).
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 or subnet CIDR | ALL/30000-32767 | Allow worker nodes to receive connections through OCI Network Load Balancer.  
### Security Rules for Bastion Subnets 🔗 
An optional bastion in a bastion subnet can provide secure access to the Kubernetes API endpoint, and SSH access to worker nodes. For information about the ingress and egress security rules to define, see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

