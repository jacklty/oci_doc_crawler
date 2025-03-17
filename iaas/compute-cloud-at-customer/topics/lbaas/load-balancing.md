Updated 2024-01-18
# Load Balancers
Load balancers improve resource usage, scaling ability, and help with instance availability on Compute Cloud@Customer.
Two major types of load balancers are available on Compute Cloud@Customer: 
  * [Load Balancer as a Service](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-as-a-service.htm#load-balancer-as-a-service "On Compute Cloud@Customer, you can configure the Load Balancing service \(LBaaS\) to automatically distribute network traffic.") – Provides Layer-7 routing, which sees all headers inserted before the message data, including information in the HTML part of the message.
  * [Network Load Balancing](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/network-load-balancing.htm#network-load-balancing "On Compute Cloud@Customer, you can configure the Network Load Balancing \(NLB\) feature to automatically distribute network traffic.") – Provides Layer-4 pass-through routing, meaning NLB sees only the IP and TCP headers on a packet.


Although the operational layers are the most obvious difference between LBaaS and NLBs, some features are shared while others differ. For example, both types of LBs require a public network load balancer to accept traffic from the internet, and a public LB can't be in a private subnet. 
The following table summarizes these major differences. 
LBaaS and NLB Major Characteristics Compared Major Characteristic | LBaaS | NLB  
---|---|---  
Visibility | Public or Private | Public or Private  
IP Address | Ephemeral or Reserved IP address | Ephemeral or Reserved IP address  
Policy Parameters | Weighted Round Robin, IP hash, Least Connections | IP hash mapped from 5, 3, or 2 header fields  
Layer 4 Functioning | Yes | Yes  
Layer 7 Functioning | Yes |  **No**  
TLS Support | Yes |  **No**  
If a VCN uses network security groups (NSGs), you can associate the load balancer with an NSG. An NSG has a set of security rules that controls allowed types of inbound and outbound traffic. The rules apply only to the resources in the group. An NSG isn't a security list, where the rules apply to all the resources in any subnet that uses the list. See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
If you prefer to use security lists for the VCN, see [Controlling Traffic with Security Lists](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-security-lists.htm#controlling-traffic-with-security-lists "On Compute Cloud@Customer, both security lists and network security groups \(NSGs\) are types of virtual firewalls for your compute instances. Both security lists and NSGs define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
We recommend that you distribute backend servers across all availability domains.
Other differences are of an operational nature, or involved in configuration limits. Many of the NLB limitations are because of the functioning at Layer 4 and no higher. These differences are listed in the following table.
Other LBaaS and NLB Characteristics Compared Characteristic | LBaaS | NLB  
---|---|---  
Routing of Requests | Yes | No  
Persistence of Sessions | Yes | No  
SSL Certificates  | Yes | No  
Cipher Suites | Yes | No  
Listener Protocol | HTTP, HTTP2, TCP, HTTPS | TCP  
Health Check Protocol | HTTP, TCP | HTTP, HTTPS, TCP  
IP Address Limit | 1 | 1  
Backend Set Limit | 16 | 4  
Backend Servers per Backend Set | 512 | 512  
Total Backend Servers Limit | 512 | 1024  
Maximum Listeners | 16 | 50  
Certificate Support | Yes | No  
Depending on the type of load balancer you want to use, see one of these sections:
  * [Load Balancer as a Service](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-as-a-service.htm#load-balancer-as-a-service "On Compute Cloud@Customer, you can configure the Load Balancing service \(LBaaS\) to automatically distribute network traffic.")
  * [Network Load Balancing](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/network-load-balancing.htm#network-load-balancing "On Compute Cloud@Customer, you can configure the Network Load Balancing \(NLB\) feature to automatically distribute network traffic.")


Was this article helpful?
YesNo

