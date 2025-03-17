Updated 2024-08-14
# Example Network Resource Configuration for Cluster with Virtual Nodes
_Find out about how you might configure network resources for a cluster with virtual nodes when using Kubernetes Engine (OKE)._
## VCN
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

  
## Subnets
Resource | Example  
---|---  
**Public Subnet for Kubernetes API Endpoint** |  **Name:** KubernetesAPIendpoint with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.0.0/28
  * **Route Table:** routetable-KubernetesAPIendpoint
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-KubernetesAPIendpoint

  
**Private Subnet for Virtual Nodes and Pods** |  **Name:** nodespods with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.10.0/19
  * **Route Table:** routetable-nodespods
  * **Subnet access:** Private 
  * **DNS Resolution:** Selected 
  * **DHCP Options:** Default
  * **Security List:** seclist-nodespods

  
**Public Subnet for Service Load Balancers** |  **Name:** loadbalancers with the following properties:
  * **Type****:** Regional
  * **CIDR Block:** 10.0.20.0/24
  * **Route Table:** routetable-serviceloadbalancers
  * **Subnet access:** Public 
  * **DNS Resolution:** Selected
  * **DHCP Options:** Default 
  * **Security List:** seclist-loadbalancers

  
## Route Tables
Resource | Example  
---|---  
**Route Table for Public Kubernetes API Endpoint Subnet** |  **Name:** routetable-KubernetesAPIendpoint, with one route rule defined as follows:
  * Rule for traffic to internet:
    * **Destination CIDR block:** 0.0.0.0/0
    * **Target Type:** Internet Gateway
    * **Target:** internet-gateway-0

  
**Route Table for Private Virtual Nodes and Pods Subnet** |  **Name:** routetable-nodespods, with two route rules defined as follows:
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

  
## Security List Rules for Public Kubernetes API Endpoint Subnet
The seclist-KubernetesAPIendpoint security list has the ingress and egress rules shown here.
**Ingress Rules:**
State | Source | Protocol/Dest. Port | Description  
---|---|---|---  
Stateful | 0.0.0.0/0 | TCP/6443 | External access to Kubernetes API endpoint.  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | TCP/6443 | Virtual node to Kubernetes API endpoint communication.  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | TCP/12250 | Virtual node to control plane communication.  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | ICMP 3,4 | Path Discovery.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | All <region> Services in Oracle Services Network | TCP/443 | Allow Kubernetes API endpoint to communicate with regional OCI service endpoints.  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | TCP/ALL | Allow Kubernetes API endpoint to communicate with virtual nodes.  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | ICMP 3,4 | Path Discovery.  
## Security List Rules for Private Nodes/Pods Subnet
The seclist-nodespods security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.10.0/19 | ALL/ALL | Pod-to-pod communication.  
Stateful | 10.0.10.0/19 | ALL / 30000-32767 | Traffic from load balancer to pod and health check node port traffic for external-traffic-policy=local  
Stateful | 10.0.10.0/19 | TCP/UDP / 10256 | Traffic from load balancer to health check port for external-traffic-policy=cluster  
Stateful | 10.0.0.0/28 | ICMP 3,4 | Path discovery from API server.  
Stateful | 10.0.0.0/28 | TCP/ALL | API server to virtual node communication.  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | ALL/ALL | Pod-to-pod communication.  
Stateful | 10.0.0.0/28 | TCP/6443 | Virtual node/pod to API server communication.  
Stateful | 10.0.0.0/28 | TCP/12250 | Virtual node/pod to API server communication.  
Stateful | 10.0.0.0/28 | ICMP 3,4 | Path discovery to API server.  
Stateful | All <region> Services in Oracle Services Network | TCP/443 | Virtual node/pod to regional OCI service endpoints communication.  
Stateful | 0.0.0.0/0 | ICMP 3,4 | Access from virtual node/pod to Kubernetes control plane.  
Stateful | 0.0.0.0/0 | ALL/ALL | Pod access to internet  
## Security List Rules for Public Load Balancer Subnet
The seclist-loadbalancers security list has the ingress and egress rules shown here.
**Ingress Rules:**
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful |  0.0.0.0/0 |  TCP / 443/80 | Incoming traffic to load balancer assuming listener port is 80/443  
**Egress Rules:**
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | ALL / 30000-32767 | Traffic to pod and health check node port traffic for external-traffic-policy=local  
Stateful | 10.0.10.0/19 (Nodes/Pods CIDR) | TCP/UDP / 10256 | Traffic to health check port for external-traffic-policy=cluster  
Was this article helpful?
YesNo

