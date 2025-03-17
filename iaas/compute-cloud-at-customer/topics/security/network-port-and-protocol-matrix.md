Updated 2024-12-16
# Network Port and Protocol Matrix
Compute Cloud@Customer requires access permissions to be granted for certain IP addresses, ports, and protocols.
The default security posture for almost all firewalls is to deny access. This applies to the firewalls used between the Compute Cloud@Customer rack and the customer data center. 
To allow certain Compute Cloud@Customer features to operate correctly, access must be granted for certain IP address and related services. An "allow all" rule such as `0.0.0.0/0` is too broad for security purposes, so the best practice is to explicitly list addresses, ports, and protocols to allow.
Compute Cloud@Customer is installed with connections to different networks for different purposes (see [Customer Site Network Requirements](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/network-requirements.htm#customer-network-requirements "Review the topics in this section to prepare your network environment before the arrival of the Oracle Compute Cloud@Customer rack.")). For security purposes, Compute Cloud@Customer isolates the administration network from the customer data network.
During the Compute Cloud@Customer installation, Oracle configures the isolated networks, and works with your network administrator to configure the network ports so they work within your environment.
The following table lists the access permissions for certain IP addresses, ports, and protocols that are granted for data center and admin network isolation.
**Table key:**
  * Customer – Customer administrator access for Compute Cloud@Customer resource management
  * Oracle – Oracle administrator access, which is only accessible by Oracle when granted access by the customer using [Oracle Operator Access Control](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/managed-access.htm#architectural-overview "Compute Cloud@Customer supports the use of Oracle Operator Access Control to manage requests for temporary access to your organization's cloud resources from OCI authorized operators.").


Source IP Address |  Destination IP Address |  Port |  Protocol |  Description  
---|---|---|---|---  
All customer networks | Customer VIP  | ICMP | Type 0/Echo reply  
Oracle administrators | Oracle VIP | ICMP | Type 0/Echo reply  
All customer networks | Management Nodes  | ICMP | Type 0/Echo reply  
All customer networks | Object Storage IP  | ICMP | Type 0/Echo reply  
All customer networks | Customer VIP  | ICMP | Type 3/Unreachable  
Oracle administrators | Oracle VIP | ICMP  | Type 3/Unreachable  
All customer networks | Management Nodes  | ICMP | Type 3/Unreachable  
All customer networks | Object Storage IP  | ICMP | Type 3/Unreachable  
All customer networks | Customer VIP  | ICMP | Type 8/ping to VIP  
Oracle administrators | Oracle VIP | ICMP | Type 8/ping to VIP  
Oracle administrators | Management Nodes | ICMP | Type 8/ping to node  
All customer networks | Object Storage IP  | ICMP | Type 8/ping to VIP  
Oracle administrators | Oracle VIP | 22 | TCP | SSH to Active Management Node  
Oracle administrators | Management Nodes | 22 | TCP | SSH to Specific Management Node  
Initial installation DNS IPs | Customer VIP | 53 | UDP | Authoritative Zones  
Initial installation DNS IPs | Customer VIP | 53 | TCP | Authoritative Zones  
Initial installation DNS IPs | Oracle VIP | 53 | UDP | Administrative Zone  
Initial installation AdminDNS IPs | Oracle VIP | 53 | TCP | Administrative Zone  
Management Nodes | Initial installation DNS IPs | 53 | UDP | External DNS Resolution for Data Network  
Management Nodes | Initial installation DNS IPs | 53 | TCP | External DNS Resolution for Data Network  
Management Nodes | Initial installation AdminDNS IPs | 53 | UDP | External DNS Resolution for Admin Network  
Management Nodes | Initial installation AdminDNS IPs | 53 | TCP | External DNS Resolution for Admin Network  
Oracle administrators | Oracle VIP | 443 | TCP | Oracle API Endpoints and BUI  
All Compute Cloud@Customer users | Customer VIP | 443 | TCP | Compute Cloud@Customer API Endpoints and BUI  
All Compute Cloud@Customer users | Customer VIP | 8079 | TCP | Image download repository  
Oracle administrators | Oracle VIP | 30006 | TCP | Admin CLI  
Oracle administrators | Management Nodes | 30006 | TCP | Admin CLI  
Customer VIP | DNS Recursive Servers | 53 | UDP | DNS Forwarding  
Customer VIP | DNS Recursive Servers | 53 | TCP | DNS Forwarding  
Oracle VIP | DNS Recursive Servers | 53 | UDP | DNS Forwarding  
Oracle VIP | DNS Recursive Servers | 53 | TCP | DNS Forwarding  
Oracle VIP | Customer NTP Servers | 123 | UDP | NTP  
Oracle VIP | Usually _transport.oracle.com_ | 443 | TCP | ASR Targets  
Oracle VIP | Oracle Grafana Notification Targets | 443 | TCP | Grafana Notification Targets   
Oracle VIP | Oracle Local ULN Mirror | 443 | TCP | patching  
Customer VIP | Local image repository | 443 | TCP | Custom image import from-object-uri  
Management Nodes | Load balancer public IP address | 6443 | TCP | Load balancer public IP address endpoint  
All customer networks | Instance console | 1443 | TCP | [Instance console connections](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/connecting-to-a-compute-instance.htm#connecting-to-a-compute-instance "On Compute Cloud@Customer, you can connect to a running instance by using a Secure Shell \(SSH\) or Remote Desktop connection the same way you connect to instances in Oracle Cloud Infrastructure \(OCI\).")  
Was this article helpful?
YesNo

