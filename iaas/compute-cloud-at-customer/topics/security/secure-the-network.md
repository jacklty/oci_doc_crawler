Updated 2023-08-15
# Guidelines for Securing the Network
During initialization, the core network components are integrated with your existing data center network design. Uplink ports in the Compute Cloud@Customer switches connect to your next-level data center switches to provide a redundant high-speed and high-bandwidth physical connection that carries all traffic into and out of Compute Cloud@Customer. 
This environment has several consequences when it comes to securing Compute Cloud@Customer networking:
  * The rack us set up inside your data center, and connected directly to your on-premises network. There is no need for a secure tunnel over the internet to allow your cloud resources and your on-premises network to communicate. Access is enabled through a gateway between your virtual cloud network (VCN) and your on-premises network.
  * When it comes to internet access, inbound or outbound, resources in your cloud environment have no direct internet access. In contrast with a public cloud environment, no gateway is capable of enabling direct internet connectivity for a VCN. The configuration of the networking components in the data center determines how cloud resources can connect to the internet and whether they can be reached from the internet.
  * Generally, this environment means that the Compute Cloud@Customer virtual network is well-isolated from public internet threats. However, It's possible to use public IP addresses inside this private network. A public IP makes a resource reachable from outside the VCN it resides in. The IP addresses that are considered "public" are really part of the data center's private range.


Nevertheless, there are steps you can take to control cloud network security and access to compute instances:
  * Use private subnets if instances don't require a public IP address.
  * Configure firewall rules on the instance to control traffic into and out of an instance at the packet level. However, Compute Cloud@Customer-provided images that run Oracle Linux automatically include default rules that allow ingress on TCP port 22 for SSH traffic. In addition, the Microsoft Windows images include default rules that allow ingress on TCP port 3389 for Remote Desktop access.
  * Configure gateways and route tables to allow only required connectivity. This can control traffic flow to "outside" destinations such as your on-premises network or another VCN.
  * Use IAM policies to control access to Compute Cloud@Customer interfaces. You can control which cloud resources can be accessed and which type of access is allowed. For example, you can control who can set up your network and subnets, or who can update route tables, network security groups, or security lists. 


For more network security information, see [Network Security Guidelines](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/network-security.htm#network-security-sec-guide "Secure network access to your resources in Compute Cloud@Customer.").
Was this article helpful?
YesNo

