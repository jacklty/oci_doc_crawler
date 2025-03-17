Updated 2025-03-10
# Network Connectivity Issues With Private DNS Resolution Between VCNs or Between a VCN and an On-premises Network
Network connectivity issues for DNS resolution between VCNs or between a VCN and an on-premises network.
  * Ensure that if using a local peering gateway (**LPG**), that it's set up correctly between **VCNs** , and that the remote peering connection, **IPSec** tunnel, or FastConnect is set up correctly between resolvers. See [Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm), [FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm), and [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm) for more information.
  * Check all VCN configurations when troubleshooting connectivity issues for ingress and egress.
  * DNS transactions are short-lived, so we recommend that you use stateless **security rules** for both **UDP** and **TCP** DNS traffic. Although stateful rules often work, it's possible that during heavy load the connection tracking table fills up, preventing new connections. As a result, it can appear as if a DNS outage has occurred. See [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm) for more information. 
If the VCN uses forwarding endpoints to send queries, two pairs of rules are required to enable a stateless configuration. Create an egress rule for destination port 53 for both UDP and TCP, and an ingress rule that allows responses from source port 53. See [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm) for more information. 
If the VCN uses listening endpoints to receive queries, create an egress rule for source port 53 for both UDP and TCP that allows responses. Then, create an ingress rule for source port 53 to allow external queries. Be as restrictive as possible on the source and destination CIDRs to prevent unintended access to DNS services. See [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm) for more information. 


Was this article helpful?
YesNo

