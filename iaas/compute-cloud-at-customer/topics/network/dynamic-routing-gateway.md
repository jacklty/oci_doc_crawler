Updated 2024-12-16
# Dynamic Routing Gateways (DRGs)
On Compute Cloud@Customer, a dynamic routing gateway, or DRG, provides a path for private network traffic between the VCN and an on-premises network. This traffic is routed to the data center network and on to its destination. 
The data center network is considered a public network because it's external to the Compute Cloud@Customer environment. However, no form of tunneling is required because traffic doesn't travel over the internet. This is a significant difference with public cloud environments.
For the purpose of access control, when creating a DRG, you must specify the compartment where you want the DRG to reside. If you aren't sure which compartment to use, put the DRG in the same compartment as the VCN.
A DRG is a standalone object. To use it, you must attach it to a VCN. In the API, the process of attaching creates a DRG Attachment object with its own OCID. To detach the DRG, you delete the attachment object.
A VCN can be attached to only one DRG at a time, though a DRG can be attached to multiple VCNs. You can detach a DRG and reattach it at any time. After attaching a DRG, you must update the routing in the VCN to use the DRG. Otherwise, traffic from the VCN will not flow to the DRG.
The basic routing scenario sends traffic from a subnet in the VCN to the DRG. When sending traffic from the subnet to your on-premises network, you set up a rule in the subnet route table. The rule's destination CIDR is the CIDR for the on-premises network or a subnet within, and the rule's target is the DRG.
Was this article helpful?
YesNo

