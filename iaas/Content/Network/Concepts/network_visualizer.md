Updated 2025-02-18
# Network Visualizer
Learn about the Network Visualizer tool in Network Command Center.
## Overview
An Oracle virtual network is composed of virtual cloud networks (VCNs), subnets, gateways, and other resources. These entities are related and connected through routing that's often complex. These resources can also have complex relationships with other Oracle Cloud Infrastructure (OCI) services. The ability to have a concise picture of these entities and their relationships is essential for understanding the design and operation of a virtual network. 
The Network Visualizer provides a diagram of the implemented topology of all VCNs in a selected region and tenancy. This tool in the OCI Console can provide the following levels of granularity:
**Regional Network Topology**
You can see a **high-level layout and routing topology** of the entire virtual network configuration within a region. This topology includes DRGs, VCNs, CPEs, and various types of gateway.
In this view, a limit is enforced on the number of resources shown to enable the generation of larger maps. If the limit is exceeded, a partial topology is displayed with an error message. Network Visualizer applies the following limits irrespective of whether the compartment selected is a root or child compartment. You might see more or less resources than the limit for each depending on the number of resources you have and display logic. You can [request a limit increase](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) which is evaluated by the service team and accepted or rejected based on the required scale.
Resource | Display Limit  
---|---  
VCN | 25  
Internet Gateways | 1 for each VCN. Limit increase not supported.  
Local Peering Gateways (LPGs) | 25 for each VCN  
Network Address Translation Gateways (NAT) | 10 for each VCN  
Service Gateways | 5 for each VCN  
Dynamic Routing Gateways (DRGs) | 5  
DRG attachments and Cross Tenancy DRG attachments | 30 for each DRG, 150 global limit (30*5 DRG)  
Customer Premises Equipment (CPE) | 10  
IPSec Connections | 10  
IPSec Tunnels | 20  
FastConnect Virtual Circuits | 10  
Remote Peering Connections | 10  
DRG Route Tables | 30 for each DRG  
DRG Route Rules | 100 for each route table  
**Virtual Cloud Network Topology**
You can see the **organization of a single VCN** including its subnets and routing configuration. This topology includes subnets, VLANs, and gateways to other resources.
**Subnet Topology**
You can see **resource information** about instances, load balancers, FSS, and OKE clusters in the subnet. 
## Required Permissions
You need to set the following policy to have access to Network Visualizer.
```
Allow group <your_admin_group> to READ all-resources in tenancy

```

Network Visualizer doesn't belong to the `virtual-network-family` and doesn't belong to a specific group with more granular permission.
## Working with Regional Routing Maps
The Network Visualizer tool diagram helps you view a high-level structure of network configuration and helps quick navigation between its core components. It provides a view of all resources in a particular combination of region and compartment.
You can view and understand the following from this diagram:
  * How VCNs are interconnected
  * How on-premises networks are connected (using FastConnect or Site-to-Site VPN)
  * Which routing entities (DRGs and so on) control traffic routing
  * How transit routing is configured


When you open a diagram for a compartment, it shows resources for all compartments nested underneath. You can also filter out objects from the compartments that you don't want to see.
You can see cross-region connections between network resources and you can also quickly change regions in the Console and see the VCNs in another region.
The **Regional Map** view uses the following symbols and conventions: 
External resources | External devices such as a CPE are shown in the left side of the canvas, which is shaded and separated by a dashed line.  
---|---  
Customer-Premises Equipment (CPE) | ![CPE Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_CPE.svg)  
Oracle cloud resources | Oracle cloud resources are shown in the main area of the canvas.  
Virtual Private Network (IPSec) connection | ![VPN Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_VPN.svg)  
Dynamic Routing Gateway (DRG) | ![DRG Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_DRG.svg)  
Connection | ![Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Connection.svg)  
Link | ![Link Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_link.svg)  
FastConnect connection | ![FastConnect Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_FastConnect.svg)  
Virtual Cloud Network (VCN) | ![VCN Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_VCN.svg)  
Remote Peering Connection (RPC) | ![Remote Peering Connection Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_RPC.svg)  
NAT Gateway (NAT) | ![NAT Gateway Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_NAT-Gateway.svg)  
Service Gateway (SGW) | ![Service Gateway Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Service-Gateway.svg)  
Internet gateway (IGW) | ![Internet Gateway Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Internet-Gateway.svg)  
Local Peering Gateway (LPG) | ![LPG Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Local-Peering-Gateway.svg)  
Oracle region | ![Oracle Region Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Region.svg)  
Resource outside the region or compartment or filtered because of a service limit (details aren't visible) | ![Details Not Visible Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_not-visible.svg)  
## Working with VCN Topologies
The VCN topology routing diagram helps visualize the networking components that are part of the selected VCN up to the subnet level. With such visualization, you can focus on cross-AD deployment, routing and network security configurations. VCNs can also be viewed in Security mode that shows relationships with security lists and network security groups (NSGs) with other virtual network resources. When you view a VCN in one of these modes you can easily switch to the other mode. 
You can view and understand the following from this diagram and information panel:
  * Which subnets and VLANs belong to the VCN
  * How subnets and VLANs are organized across availability domains
  * How Security lists are applied within the VCN
  * How NSGs are applied within the VCN
  * Whether subnets in a VCN are public or private
  * How subnets and VLANs are organized across compartments
  * Which gateways (RPG, LPG, NGW, SGW, IGW) are part of the VCN
  * Which routes are defined between subnets and gateways


The **Virtual Network Map** uses the following symbols and conventions: 
Regional resources | Routable resources not internal to the VCN but routable from the VCN are shown in the left side of the canvas, which is shaded and separated by a dashed line.  
---|---  
DRG | ![DRG Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_DRG.svg)  
Other directly connected VCNs | ![VCN Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_VCN.svg)  
VCN resources | VCN resources such as subnets and VLANs are shown in the main area of the canvas. Gateways connecting the VCN to other resources in the region are shown on the dashed line defining the border of the VCN.  
Link | ![Link Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_link.svg)  
LPG | ![LPG Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Local-Peering-Gateway.svg)  
SGW | ![Service Gateway Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Service-Gateway.svg)  
IGW | ![Internet Gateway Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Internet-Gateway.svg)  
Public Subnet (S) | ![Public Subnet Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Public-Subnet.svg)  
Private Subnet (S) | ![Private Subnet Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_Private-Subnet.svg)  
VLAN (V) | ![VLAN Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_VLAN.svg)  
VPN | ![VPN icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_VPN.svg)  
**Note** Load balancers and Compute instances in a subnet aren't shown in this view. That level of detail is shown in the subnet maps.
## Working with subnet routing and security maps
When you select a Subnet in either the **VCN routing map** or **VCN security map** , you can access a **Subnet inventory map** or a **Subnet security map**.
The Subnet inventory map lists resources in the subnet such as network load balancers, load balancers, and Compute instances. A resource summary and more details are available for each of these resources.
The Subnet Security map also lists the resources in the subnet, but you can use this mode to select a resource and see what security lists and network security groups are associated with a specified resource.
You can view and understand the following from these diagrams and information panel:
  * What Compute instances and VLANs belong to the subnet
  * How security lists are applied to Compute instances and load balancers within the subnet
  * How network security groups are applied to VNICs associated with Compute instances
  * Whether instances in a subnet have public or private VNICs
  * How network security groups and security lists are organized across compartments


The Subnet Inventory map and Subnet Security map use the following symbols and conventions: 
Public Network Load Balancer (NLB) | ![public NLB icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_NLB_pub.svg)  
---|---  
Private Network Load Balancer (NLB) | ![private NLB icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_NLB_pri.svg)  
Public Load Balancer (LB) | ![public LB icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_LB_pub.svg)  
Private Load Balancer (LB) | ![private LB icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_LB_pri.svg)  
Mount Target (MT) | ![Mount target icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_mount-target.svg)  
Kubernetes Cluster (OKE) | ![OKE icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_oke.svg)  
Compute instance (I) | ![compute instance icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_inst.svg)  
Security list (SL) | ![security list icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_SL.svg)SLs are shown the left side of the resource list while in Security mode.  
Network security groups (NSG) | ![network security group icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_NSG.svg)NSGs are shown on the right side of the resource list while in Security mode.  
## Network Visualizer Tasks 🔗 
  * [Viewing a Regional Network Topology Map](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-network-topology-map.htm#top "Use Network Visualizer to view a map that shows a visual representation of the network topology in an Oracle Cloud Infrastructure region.")
  * [Viewing a VCN Topology Map](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-vcn-topology-map.htm#top "Use Network Visualizer to view a map that shows a visual representation of the topology of a single virtual cloud network \(VCN\).")
  * [Viewing a Subnet Topology Map](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-subnet-topology-map.htm#top "Use Network Visualizer to view a map that shows a visual representation of the topology of a subnet.")


Was this article helpful?
YesNo

