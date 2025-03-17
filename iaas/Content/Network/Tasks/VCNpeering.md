Updated 2024-10-16
# Access to Other VCNs: Peering
VCN peering is the process of connecting multiple virtual cloud networks (VCNs). There are four types of VCN peering: 
  * [Local VCN peering (within region)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region) using LPGs 
  * [Remote VCN peering (across regions)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions) using RPCs
  * [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.")
  * [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.")


You can use VCN peering to divide your network into multiple VCNs (for example, based on departments or lines of business), with each VCN having direct, private access to the others. There's no need for traffic to flow over the internet or through your on-premises network by way of an [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") or [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."). You can also place shared resources into a single VCN that all the other VCNs can access privately. 
Each VCN can have up to 10 local peering gateways and can attach to only one DRG. A single DRG supports up to 300 VCN attachments, allowing traffic between them to flow as directed by the DRG's route tables. We recommend using the DRG if you need to peer with a large number of VCNs. If you want extremely high bandwidth and super low-latency traffic between two VCNs in the same region, use the scenario described in [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region). [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") gives you more flexibility in your routing due to the greater number of attachments.
Because remote VCN peering crosses regions, you can use it (for example) to mirror or back up your databases in one region to another.
## Overview of Local VCN Peering
_Local VCN peering_ is the process of connecting two VCNs in the same region so that their resources can communicate using private IP addresses without routing the traffic over the internet or through your on-premises network. The VCNs can be in the same Oracle Cloud Infrastructure **tenancy** or different ones. Without peering, a given VCN would need an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) and public IP addresses for the instances that need to communicate with another VCN.
[Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") gives you more flexibility in your routing and simplified management but comes at the cost of an increase in latency (by microseconds) due to routing traffic through a virtual router, the DRG. 
## Important Implications of Peering 🔗 
This section summarizes some access control, security, and performance implications for peered VCNs. In general, you can control access and traffic between two peered VCNs by using IAM policies, route tables in each VCN, and security lists in each VCN. 
### Controlling the Establishment of Peerings
With IAM policies, you can control:
  * Who can [subscribe your tenancy to another region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm) (required for remote VCN peering)
  * Who in your organization has the authority to establish VCN peerings (for example, see the IAM policies in [Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting) and [Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting)). Deletion of these IAM policies does not affect any existing peerings, only the ability for future peerings to be created.
  * Who can [manage route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists)


### Controlling Traffic Flow Over the Connection
Even if a peering connection has been established between your VCN and another, you can control the packet flow over the connection with route tables in your VCN. For example, you can restrict traffic to only specific subnets in the other VCN. 
Without terminating the peering, you can stop traffic flow to the other VCN by simply removing route rules that direct traffic from your VCN to the other VCN. You can also effectively stop the traffic by removing any security list rules that enable ingress or egress traffic with the other VCN. This doesn't stop traffic flowing over the peering connection, but stops it at the [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) level. 
For more information about the routing and security lists, see the discussions in these sections:
Local VCN peering using local peering groups:
  * [Important Local Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan)
  * [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4)
  * [Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step5)


Remote VCN peering using a remote peering connection:
  * [Important Remote Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)
  * [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4)
  * [Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step5)


Local VCN peering using a Dynamic Routing Gateway (DRG) :
  * [Important Local Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod__lp_concepts)
  * [Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_d_dita)
  * [Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_e_dita)
  * [Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_f_dita)


Remote VCN peering using a dynamic routing gateway (DRG):
  * [Summary of Networking Components for Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e__remote_components)
  * [Task D: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e_task_e)
  * [Task E: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e_task_f)


### Controlling the Specific Types of Traffic Allowed
It's important that each VCN administrator ensures all outbound and inbound traffic with the other VCN is intended or expected and well defined. In practice, this means implementing security list rules that explicitly state the types of traffic your VCN can send to the other and accept from the other. 
**Important**
Your instances running [platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm) also have OS firewall rules that control access to the instance. When troubleshooting access to an instance, ensure that all of the following items are set correctly:
  * The rules in the network security groups that the instance is in
  * The rules in the security lists associated with the instance's subnet
  * The instance's OS firewall rules


If your instance is running Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7, Oracle Linux 8, Oracle Linux 7, or Oracle Linux Cloud Developer 8, you need to use [firewalld](https://oracle-base.com/articles/linux/linux-firewall-firewalld) to interact with the iptables rules. For your reference, here are commands for opening a port (1521 in this example):
Copy
```
sudo firewall-cmd --zone=public --permanent --add-port=1521/tcp
								
sudo firewall-cmd --reload
```

For instances with an iSCSI boot volume, the preceding `--reload` command can cause problems. For details and a workaround, see [Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).
In addition to security lists and firewalls, you should evaluate other OS-based configuration on the instances in your VCN. There could be default configurations that don't apply to your own VCN's CIDR, but inadvertently apply to the other VCN's CIDR. 
### Using Default Security List Rules
If your VCN's subnets use the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) with the default rules it comes with, be aware that there are two rules that allow ingress traffic from anywhere (that is, 0.0.0.0/0, and thus the other VCN):
  * Stateful ingress rule that allows TCP port 22 (SSH) traffic from 0.0.0.0/0 and any source port
  * Stateful ingress rule that allows ICMP type 3, code 4 traffic from 0.0.0.0/0 and any source port


Evaluate these rules and whether you want to keep or update them. As stated earlier, ensure that all inbound or outbound traffic that you permit is intended/expected and well-defined. 
### Preparing for Performance Impact and Security Risks
In general, prepare your VCN for the ways it could be affected by the other VCN. For example, the load on your VCN or its instances could increase. Or your VCN could experience a malicious attack directly from or by way of the other VCN. 
Regarding performance: If your VCN is providing a service to another, be prepared to scale up your service to accommodate the demands of the other VCN. This might mean being prepared to launch more instances as necessary. Or if you're concerned about high levels of network traffic coming to your VCN, consider using [stateless security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful) to limit the level of connection tracking your VCN must perform. Stateless security list rules can also help slow the impact of a denial-of-service (DoS) attack. 
Regarding security risks: You can't necessarily control whether the other VCN is connected to the internet. If it is, your VCN can be exposed to bounce attacks in which a malicious host on the internet can send traffic to your VCN but make it look like it's coming from the VCN you're peered with. To guard against this, as mentioned earlier, use your security lists to carefully limit the inbound traffic from the other VCN to expected and well-defined traffic.
Was this article helpful?
YesNo

