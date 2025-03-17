Updated 2024-10-16
# Redundancy Remedies
Oracle recommends setting up a _redundant_ connection between your on-premises network and Virtual Cloud Network (VCN) for high availability. This topic gives background and links to other topics that describe how to resolve some common redundancy issues with that connection.
## About the DRG and Redundant Connections 🔗 
When you connect your on-premises network to a virtual cloud network (VCN) in Oracle Cloud Infrastructure, you use a _dynamic routing gateway_ (DRG). A DRG is a virtual representation of highly available hardware (physical routers) on the edge of the Oracle Cloud Infrastructure network. You attach a DRG to the VCN, and the DRG is the termination point for the connections from your on-premises network to that VCN. If you have multiple VCNs in your tenancy, each has a DRG. You can attach multiple VCNs to a single DRG. Each VCN can be in the same or different tenancies as the DRG. 
A single DRG can have multiple connections to it from your on-premises network, which allows redundancy. Those connections could be the same type or different types. Here are the two types:
  * FastConnect 
  * Site-to-Site VPN 


For example, you might use FastConnect, but also set up Site-to-Site VPN to use as backup when FastConnect is temporarily unavailable because of maintenance. Or, you might have two VPN tunnels, with one as primary and the second as failover.
For high availability, the multiple connections to a DRG _must not terminate on a single physical router_ in Oracle's edge network. If they do, your overall connection to Oracle Cloud Infrastructure is disrupted whenever Oracle performs maintenance on that router.
## How to Identify and Fix a Redundancy Issue 🔗 
You might have a redundancy issue in which a DRG in your tenancy has multiple on-premises connections that terminate on a single physical Oracle router. Or you might have only a single connection with no redundancy.
If you do, the Console displays an alert message when you view the DRG's details, or when you view the details of one of the connections (for example, the IPSec connection). The alert message includes a link to one of the following topics, which explain how to fix the particular issue: 
  * [Case 1: Multiple FastConnect virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancycase1.htm#Redundancy_Remedy_Case_1)
  * [Case 2: FastConnect and Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancycase2.htm#Redundancy_Remedy_Case_2)
  * [Case 3: Multiple IPSec connections](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancycase3.htm#Redundancy_Remedy_Case_3)
  * [Case 4: Single FastConnect virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancycase4.htm#Redundancy_Remedy_Case_4)


Was this article helpful?
YesNo

