Updated 2024-08-23
# Example Network Resource Configurations
_Find out about examples of how you might configure network resources for highly available cluster creation and deployment in a region with three availability domains when using Kubernetes Engine (OKE)._
When creating a new cluster, you can use the 'Quick Create' workflow to create new network resources automatically. Alternatively, you can use the 'Custom Create' workflow to explicitly specify existing network resources. For more information about the required network resources, see [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).").
This topic gives examples of how you might configure network resources when using the 'Custom Create' workflow to create highly available clusters in a region with three availability domains:
  * [Example 1: Cluster with Flannel CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-flannel-cni-publick8sapi_privateworkers_publiclb)
  * [Example 2: Cluster with Flannel CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-flannel-cni-privatek8sapi_privateworkers_publiclb)
  * [Example 3: Cluster with OCI CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-oci-cni-publick8sapi_privateworkers_publiclb)
  * [Example 4: Cluster with OCI CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm#example-oci-cni-privatek8sapi_privateworkers_publiclb)


A number of related [Developer Tutorials](https://docs.oracle.com/iaas/developer-tutorials/tutorials/home.htm#home__kubernetes) are available.
**Note** The examples in this section show the use of security rules in security lists to control access to clusters. If you prefer to use network security groups (which are recommended) over security lists, you can specify identical security rules for network security groups.
## Example 1: Cluster with Flannel CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers 🔗 
This example assumes you want the Kubernetes API endpoint and load balancers accessible directly from the internet. The worker nodes are accessible within the VCN.
Note that the Kubernetes API endpoint is assigned a private IP address by default. To expose the Kubernetes API endpoint to the internet, do both of the following:
  * Select a public subnet to host the Kubernetes API endpoint.
  * Specify that you want a public IP address assigned to the Kubernetes API endpoint (as well as the private IP address).


[![This image shows an example cluster configuration with a public Kubernetes API endpoint subnet, a private worker node subnet, public load balancer subnets, and a private bastion subnet. Access to the subnets is controlled by the seclist-KubernetesAPIendpoint, seclist-workernodes, seclist-loadbalancers, and seclist-Bastion security lists respectively. This cluster uses the flannel CNI plugin for pod networking. The Kubernetes API endpoint subnet is connected to the cluster control plane by a VNIC. Other features of this example configuration are described in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-flannel-eg1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-flannel-eg1.png)
### VCN
Resource | Example  
---|---  
**VCN** | 
  * **Name:** acme-dev-vcn
  * **CIDR Block:** 10.0.0.0/16
  * **DNS Resolution:** Selected

  
**Internet Gateway** | 
  * **Name:** internet-gateway-0

  
**NAT Gateway** | 
  * **Name:** nat-gateway-0

  
**Service Gateway** | 
  * **Name:** service-gateway-0
  * **Services:** All <region> Services in Oracle Services Network 

  
**DHCP Options** | 
  * **DNS Type** set to Internet and VCN Resolver 

  
### Subnets
Resource | Example  
---|---  
**Public Subnet for Kubernetes API Endpoint** |  **Name:** KubernetesAPIendpoint with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.0.0/30
  * **Route Table:** routetable-KubernetesAPIendpoint
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-KubernetesAPIendpoint

  
**Private Subnet for Worker Nodes** |  **Name:** workernodes with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.1.0/24
  * **Route Table:** routetable-workernodes
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-workernodes

  
**Public Subnet for Service Load Balancers** |  **Name:** loadbalancers with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.2.0/24
  * **Route Table:** routetable-serviceloadbalancers
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-loadbalancers

  
**Private Subnet for Bastion** |  **Name:** bastion with the following properties:
  * **Type:** Regional
  * **CIDR Block:** 10.0.3.0/24
  * **Subnet access:** Private
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-Bastion

  
### Route Tables
Resource | Example  
---|---  
**Route Table for Public Kubernetes API Endpoint Subnet** |  **Name:** routetable-KubernetesAPIendpoint, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target:** internet-gateway-0

  
**Route Table for Private Worker Nodes Subnet** |  **Name:** routetable-workernodes, with two route rules defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Public Load Balancers Subnet** |  **Name:** routetable-serviceloadbalancers, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target:** internet-gateway-0

  
### Security List Rules for Public Kubernetes API Endpoint Subnet
The seclist-KubernetesAPIendpoint security list has the ingress and egress rules shown here.
**Ingress Rules:**
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/12250 | Kubernetes worker to control plane communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 0.0.0.0/0, bastion subnet CIDR, or specific CIDR | TCP/6443 |  (optional) External access to Kubernetes API endpoint.
  * 0.0.0.0/0 when the source is Internet, subnet is public, and a public IP is assigned to the API endpoint
  * Bastion subnet CIDR when access is made through OCI Bastion
  * Specific CIDR when access is made from other specific CIDR 

  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow Kubernetes control plane to communicate with OKE.  
Stateful | All <region> Services in Oracle Services Network | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/ALL | Allow Kubernetes control plane to communicate with worker nodes.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
### Security List Rules for Private Worker Nodes Subnet
The seclist-workernodes security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/ALL | Allow Kubernetes control plane to communicate with worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | Bastion subnet CIDR, or specific CIDR | TCP/22 | (optional) Allow inbound SSH traffic to managed nodes.  
Stateful | Load balancer subnet CIDR | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | Load balancer subnet CIDR | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow worker nodes to communicate with OKE.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/12250 | Kubernetes worker to control plane communication.  
Stateful | 0.0.0.0/0 | TCP/ALL | (optional) Allow worker nodes to communicate with internet.  
### Security List Rules for Public Load Balancer Subnet
The seclist-loadbalancers security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  Application specific (Internet or specific CIDR) |  Application specific (for example, TCP, UDP - 443, 8080) | (optional) Load balancer listener protocol and port. Customize as required.   
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
### Security List Rules for Private Bastion Subnet
The seclist-Bastion security list has the ingress and egress rules shown here.
**Ingress Rules:** None
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/6443 |  (optional) Allow bastion to access the Kubernetes API endpoint.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/22 | (optional) Allow SSH traffic to worker nodes.  
## Example 2: Cluster with Flannel CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers 🔗 
This example assumes you want only load balancers accessible directly from the internet. The Kubernetes API endpoint and the worker nodes are accessible within the VCN.
[![This image shows an example cluster configuration with a private Kubernetes API endpoint subnet, a private worker node subnet, public load balancer subnets, and a private bastion subnet. Access to the subnets is controlled by the seclist-KubernetesAPIendpoint, seclist-workernodes, seclist-loadbalancers, and seclist-Bastion security lists respectively. This cluster uses the flannel CNI plugin for pod networking. The Kubernetes API endpoint subnet is connected to the cluster control plane by a VNIC. Other features of this example configuration are described in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-flannel-eg2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-flannel-eg2.png)
### VCN
Resource | Example  
---|---  
**VCN** | 
  * **Name:** acme-dev-vcn
  * **CIDR Block:** 10.0.0.0/16
  * **DNS Resolution:** Selected

  
**Internet Gateway** | 
  * **Name:** internet-gateway-0

  
**NAT Gateway** | 
  * **Name:** nat-gateway-0

  
**Service Gateway** | 
  * **Name:** service-gateway-0
  * **Services:** All <region> Services in Oracle Services Network 

  
**DHCP Options** | 
  * **DNS Type** set to Internet and VCN Resolver 

  
### Subnets
Resource | Example  
---|---  
**Private Subnet for Kubernetes API Endpoint** |  **Name:** KubernetesAPIendpoint with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.0.0/30
  * **Route Table:** routetable-KubernetesAPIendpoint
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-KubernetesAPIendpoint

  
**Private Subnet for Worker Nodes** |  **Name:** workernodes with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.1.0/24
  * **Route Table:** routetable-workernodes
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-workernodes

  
**Public Subnet for Service Load Balancers** |  **Name:** loadbalancers with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.2.0/24
  * **Route Table:** routetable-serviceloadbalancers
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-loadbalancers

  
**Private Subnet for Bastion** |  **Name:** bastion with the following properties:
  * **Type:** Regional
  * **CIDR Block:** 10.0.3.0/24
  * **Subnet access:** Private
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-Bastion

  
### Route Tables
Resource | Example  
---|---  
**Route Table for Private Kubernetes API Endpoint Subnet** |  **Name:** routetable-KubernetesAPIendpoint, with one route rule defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Private Worker Nodes Subnet** |  **Name:** routetable-workernodes, with two route rules defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Public Load Balancers Subnet** |  **Name:** routetable-serviceloadbalancers, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target:** internet-gateway-0

  
### Security List Rules for Private Kubernetes API Endpoint Subnet
The seclist-KubernetesAPIendpoint security list has the ingress and egress rules shown here.
**Ingress Rules:**
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/12250 | Kubernetes worker to control plane communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 0.0.0.0/0, bastion subnet CIDR, or specific CIDR | TCP/6443 |  (optional) External access to Kubernetes API endpoint.
  * 0.0.0.0/0 when the source is Internet, subnet is public, and a public IP is assigned to the API endpoint
  * Bastion subnet CIDR when access is made through OCI Bastion
  * Specific CIDR when access is made from other specific CIDR 

  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  All <region> Services in Oracle Services Network | TCP/ALL | Allow Kubernetes control plane to communicate with OKE.  
Stateful | All <region> Services in Oracle Services Network | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/ALL | Allow Kubernetes control plane to communicate with worker nodes.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
### Security List Rules for Private Worker Nodes Subnet
The seclist-workernodes security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/ALL | Allow Kubernetes control plane to communicate with worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | Bastion subnet CIDR, or specific CIDR | TCP/22 | (optional) Allow inbound SSH traffic to managed nodes.  
Stateful | Load balancer subnet CIDR | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | Load balancer subnet CIDR | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow pods on one worker node to communicate with pods on other worker nodes.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow worker nodes to communicate with OKE.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/12250 | Kubernetes worker to control plane communication.  
Stateful | 0.0.0.0/0 | TCP/ALL | (optional) Allow worker nodes to communicate with internet.  
### Security List Rules for Public Load Balancer Subnet
The seclist-loadbalancers security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  Application specific (Internet or specific CIDR) |  Application specific (for example, TCP, UDP - 443, 8080) | (optional) Load balancer listener protocol and port. Customize as required.   
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
### Security List Rules for Private Bastion Subnet
The seclist-Bastion security list has the ingress and egress rules shown here.
**Ingress Rules:** None
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/30 (Kubernetes API Endpoint CIDR) | TCP/6443 |  (optional) Allow bastion to access the Kubernetes API endpoint.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/22 | (optional) Allow SSH traffic to worker nodes.  
## Example 3: Cluster with OCI CNI Plugin, Public Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers 🔗 
This example assumes you want the Kubernetes API endpoint and load balancers accessible directly from the internet. The worker nodes are accessible within the VCN.
Note that the Kubernetes API endpoint is assigned a private IP address by default. To expose the Kubernetes API endpoint to the internet, do both of the following:
  * Select a public subnet to host the Kubernetes API endpoint.
  * Specify that you want a public IP address assigned to the Kubernetes API endpoint (as well as the private IP address).


[![This image shows an example cluster configuration with a public Kubernetes API endpoint subnet, a private worker node subnet, public load balancer subnets, a private pods subnet, and a private bastion subnet. Access to the subnets is controlled by the seclist-KubernetesAPIendpoint, seclist-workernodes, seclist-loadbalancers, seclist-pods, and seclist-Bastion security lists respectively. This cluster uses the OCI CNI plugin for pod networking. The Kubernetes API endpoint subnet is connected to the cluster control plane by a VNIC. Other features of this example configuration are described in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-oci-cni-eg1.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-oci-cni-eg1.png)
### VCN
Resource | Example  
---|---  
**VCN** | 
  * **Name:** acme-dev-vcn
  * **CIDR Block:** 10.0.0.0/16
  * **DNS Resolution:** Selected

  
**Internet Gateway** | 
  * **Name:** internet-gateway-0

  
**NAT Gateway** | 
  * **Name:** nat-gateway-0

  
**Service Gateway** | 
  * **Name:** service-gateway-0
  * **Services:** All <region> Services in Oracle Services Network 

  
**DHCP Options** | 
  * **DNS Type** set to Internet and VCN Resolver 

  
### Subnets
Resource | Example  
---|---  
**Public Subnet for Kubernetes API Endpoint** |  **Name:** KubernetesAPIendpoint with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.0.0/29
  * **Route Table:** routetable-KubernetesAPIendpoint
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-KubernetesAPIendpoint

  
**Private Subnet for Worker Nodes** |  **Name:** workernodes with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.1.0/24
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-workernodes

  
**Private Subnet for Pods** |  **Name:** pods with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.32.0/19 
  * **Route Table:** routetable-pods
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-pods

  
**Public Subnet for Service Load Balancers** |  **Name:** loadbalancers with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.2.0/24
  * **Route Table:** routetable-serviceloadbalancers
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-loadbalancers

  
**Private Subnet for Bastion** |  **Name:** bastion with the following properties:
  * **Type:** Regional
  * **CIDR Block:** 10.0.3.0/24
  * **Subnet access:** Private
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-Bastion

  
### Route Tables
Resource | Example  
---|---  
**Route Table for Public Kubernetes API Endpoint Subnet** |  **Name:** routetable-KubernetesAPIendpoint, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target:** internet-gateway-0

  
**Route Table for Private Pods Subnet** |  **Name:** routetable-pods, with two route rules defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Public Load Balancers Subnet** |  **Name:** routetable-serviceloadbalancers, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target:** internet-gateway-0

  
### Security List Rules for Public Kubernetes API Endpoint Subnet
The seclist-KubernetesAPIendpoint security list has the ingress and egress rules shown here.
**Ingress Rules:**
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.32.0/19 (Pods CIDR) | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | 10.0.32.0/19 (Pods CIDR) | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | 0.0.0.0/0, bastion subnet CIDR, or specific CIDR | TCP/6443 |  (optional) External access to Kubernetes API endpoint.
  * 0.0.0.0/0 when the source is Internet, subnet is public, and a public IP is assigned to the API endpoint
  * Bastion subnet CIDR when access is made through OCI Bastion
  * Specific CIDR when access is made from other specific CIDR 

  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow Kubernetes API endpoint to communicate with OKE.  
Stateful | All <region> Services in Oracle Services Network | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/10250 | Allow Kubernetes API endpoint to communicate with worker nodes.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow Kubernetes API endpoint to communicate with pods (when using VCN-native pod networking).  
### Security List Rules for Private Worker Nodes Subnet
The seclist-workernodes security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/10250 | Allow Kubernetes API endpoint to communicate with worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | Bastion subnet CIDR, or specific CIDR | TCP/22 | (optional) Allow inbound SSH traffic to managed nodes.  
Stateful | Load balancer subnet CIDR | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | Load balancer subnet CIDR | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow worker nodes to access pods.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow worker nodes to communicate with OKE.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
### Security List Rules for Private Pods Subnet
The seclist-pods security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow worker nodes to access pods.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | ALL/ALL | Allow Kubernetes API endpoint to communicate with pods.  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow pods to communicate with other pods.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow pods to communicate with other pods.  
Stateful | All <region> Services in Oracle Services Network |  ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network |  TCP/ALL | Allow pods to communicate with OCI services.  
Stateful | 0.0.0.0/0 |  TCP/443 | (optional) Allow pods to communicate with internet.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
### Security List Rules for Public Load Balancer Subnet
The seclist-loadbalancers security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  Application specific (Internet or specific CIDR) |  Application specific (for example, TCP, UDP - 443, 8080) | (optional) Load balancer listener protocol and port. Customize as required.   
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
### Security List Rules for Private Bastion Subnet
The seclist-Bastion security list has the ingress and egress rules shown here.
**Ingress Rules:** None
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 |  (optional) Allow bastion to access the Kubernetes API endpoint.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/22 | (optional) Allow SSH traffic to worker nodes.  
## Example 4: Cluster with OCI CNI Plugin, Private Kubernetes API Endpoint, Private Worker Nodes, and Public Load Balancers 🔗 
This example assumes you want only load balancers accessible directly from the internet. The Kubernetes API endpoint and the worker nodes are accessible within the VCN.
[![This image shows an example cluster configuration with a private Kubernetes API endpoint subnet, a private worker node subnet, public load balancer subnets, a private pods subnet, and a private bastion subnet. Access to the subnets is controlled by the seclist-KubernetesAPIendpoint, seclist-workernodes, seclist-loadbalancers, seclist-pods, and seclist-Bastion security lists respectively. This cluster uses the OCI CNI plugin for pod networking. The Kubernetes API endpoint subnet is connected to the cluster control plane by a VNIC. Other features of this example configuration are described in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-oci-cni-eg2.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-oci-cni-eg2.png)
### VCN
Resource | Example  
---|---  
**VCN** | 
  * **Name:** acme-dev-vcn
  * **CIDR Block:** 10.0.0.0/16
  * **DNS Resolution:** Selected

  
**Internet Gateway** | 
  * **Name:** internet-gateway-0

  
**NAT Gateway** | 
  * **Name:** nat-gateway-0

  
**Service Gateway** | 
  * **Name:** service-gateway-0
  * **Services:** All <region> Services in Oracle Services Network 

  
**DHCP Options** | 
  * **DNS Type** set to Internet and VCN Resolver 

  
### Subnets
Resource | Example  
---|---  
**Private Subnet for Kubernetes API Endpoint** |  **Name:** KubernetesAPIendpoint with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.0.0/29
  * **Route Table:** routetable-KubernetesAPIendpoint
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-KubernetesAPIendpoint

  
**Private Subnet for Worker Nodes** |  **Name:** workernodes with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.1.0/24
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-workernodes

  
**Private Subnet for Pods** |  **Name:** pods with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.32.0/19
  * **Route Table:** routetable-pods
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-pods

  
**Public Subnet for Service Load Balancers** |  **Name:** loadbalancers with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.2.0/24
  * **Route Table:** routetable-serviceloadbalancers
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-loadbalancers

  
**Private Subnet for Bastion** |  **Name:** bastion with the following properties:
  * **Type:** Regional
  * **CIDR Block:** 10.0.3.0/24
  * **Subnet access:** Private
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-Bastion

  
### Route Tables
Resource | Example  
---|---  
**Route Table for Private Kubernetes API Endpoint Subnet** |  **Name:** routetable-KubernetesAPIendpoint, with one route rule defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Private Pods Subnet** |  **Name:** routetable-pods, with two route rules defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** NAT Gateway
    * **Target:** nat-gateway-0
  * Rule for traffic to OCI services:
    * **Destination:** All <region> Services in Oracle Services Network
    * **Target Type:** Service Gateway
    * **Target:** service-gateway-0

  
**Route Table for Public Load Balancers Subnet** |  **Name:** routetable-serviceloadbalancers, with one route rule defined as follows:
  * **Destination CIDR block:** 0.0.0.0/0
  * **Target Type:** Internet Gateway
  * **Target Internet Gateway:** internet-gateway-0

  
### Security List Rules for Private Kubernetes API Endpoint Subnet
The seclist-KubernetesAPIendpoint security list has the ingress and egress rules shown here.
**Ingress Rules:**
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.32.0/19 (Pods CIDR) | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | 10.0.32.0/19 (Pods CIDR) | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | Bastion subnet CIDR, or specific CIDR | TCP/6443 |  (optional) External access to Kubernetes API endpoint.
  * Bastion subnet CIDR when access is made through OCI Bastion
  * Specific CIDR when access is made from other specific CIDR 

  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  All <region> Services in Oracle Services Network | TCP/ALL | Allow Kubernetes API endpoint to communicate with OKE.  
Stateful | All <region> Services in Oracle Services Network | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/10250 | Allow Kubernetes API endpoint to communicate with worker nodes.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ICMP 3,4 | Path Discovery.  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow Kubernetes API endpoint to communicate with pods.  
### Security List Rules for Private Worker Nodes Subnet
The seclist-workernodes security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/10250 | Allow Kubernetes API endpoint to communicate with worker nodes.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | Bastion subnet CIDR, or specific CIDR | TCP/22 | (optional) Allow inbound SSH traffic to managed nodes.  
Stateful | Load balancer subnet CIDR | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | Load balancer subnet CIDR | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow worker nodes to access pods.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network | TCP/ALL | Allow worker nodes to communicate with OKE.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 | Kubernetes worker to Kubernetes API endpoint communication.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/12250 | Kubernetes worker to Kubernetes API endpoint communication.  
### Security List Rules for Private Pods Subnet
The seclist-pods security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/ALL | Allow worker nodes to access pods.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | ALL/ALL | Allow Kubernetes API endpoint to communicate with pods.  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow pods to communicate with other pods.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.32.0/19 (Pods CIDR) | ALL/ALL | Allow pods to communicate with other pods.  
Stateful | All <region> Services in Oracle Services Network |  ICMP 3,4 | Path Discovery.  
Stateful | All <region> Services in Oracle Services Network |  TCP/ALL | Allow pods to communicate with OCI services.  
Stateful | 0.0.0.0/0 |  TCP/443 | (optional) Allow pods to communicate with internet.  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/12250 | Pod to Kubernetes API endpoint communication (when using VCN-native pod networking).  
### Security List Rules for Public Load Balancer Subnet
The seclist-loadbalancers security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  Application specific (Internet or specific CIDR) |  Application specific (for example, TCP, UDP - 443, 8080) | (optional) Load balancer listener protocol and port. Customize as required.   
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/30000-32767 | Load balancer to worker nodes node ports.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | ALL/10256 | Allow load balancer to communicate with kube-proxy on worker nodes.  
### Security List Rules for Private Bastion Subnet
The seclist-Bastion security list has the ingress and egress rules shown here.
**Ingress Rules:** None
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.0.0/29 (Kubernetes API Endpoint CIDR) | TCP/6443 |  (optional) Allow bastion to access the Kubernetes API endpoint.  
Stateful | 10.0.1.0/24 (Worker Nodes CIDR) | TCP/22 | (optional) Allow SSH traffic to worker nodes.  
Was this article helpful?
YesNo

