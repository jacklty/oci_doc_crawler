Updated 2025-02-05
# Limits on Resources Provided by Compute Cloud@Customer
Review the limits on the resources provided to customers by a Compute Cloud@Customer infrastructure and request new limits.
Review the following sections:
  * [Resource Limits per Infrastructure](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/resource-limits.htm#limits-on-resources__limits-per-infrastructure)
  * [Limits on Concurrent Operations](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/limits-on-concurrent-operations.htm#limits-on-concurrent-operations "Find out how many concurrent operations of a specific type Compute Cloud@Customer can manage at any particular time. These limits assume that no other operations of any kind are running at the same time. When a limit is exceeded, an error with code 409 or 429 is displayed.")
  * [Identity and Access Management (IAM) Limits](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/identity-and-access-management-iam-limits.htm#identity-and-access-management-iam-limits "On Compute Cloud@Customer, IAM services are provided by Oracle Cloud Infrastructure \(OCI\).")


## Resource Limits per Infrastructure 🔗 
The numbers provided here apply to any Compute Cloud@Customer infrastructure, regardless of its hardware configuration.
For some services, you can request a limit increase for a particular resource. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
Service |  Resource Type |  Limit  
---|---|---  
Networking Service |  VCNs |  80 with up to 16 SR-IOV VCNs  
Networking Service |  Subnets |  40 per VCN 320 in total  
Networking Service |  Dynamic routing gateways (DRG) |  32 with up to 16 SR-IOV DRGs  
Networking Service |  DRG attachments |  10 per DRG 80 in total  
Networking Service |  Internet gateways |  1 per VCN  
Networking Service |  Local peering gateways |  5 per VCN 150 in total  
Networking Service |  NAT gateways |  1 per VCN  
Networking Service |  Service gateways |  1 per VCN  
Networking Service |  Storage gateways |  2 per VCN 80 in total, standard and high-performance combined  
Networking Service |  Reserved public IPs |  The range specified on the Compute Cloud@Customer Network Spreadsheet  
Networking Service |  Ephemeral public IPs |  2 per compute instance 3336 in total  
Networking Service |  DHCP options |  30 per VCN 500 in total  
Networking Service |  Route tables |  20 per VCN 500 in total  
Networking Service |  Route rules |  50 per route table 10000 in total  
Networking Service |  VNICs |  5000 in total  
Networking Service |  Network security groups |  100 per VCN 5 per VNIC 600 in total  
Networking Service |  VNICs in network security group |  As many VNICs as are in the VCN A VNIC can belong to max. 5 network security groups  
Networking Service |  Security rules |  50 per network security group 12000 in total  
Networking Service |  Security lists |  20 per VCN 5 per subnet 600 in total  
Networking Service |  Ingress rules |  30 per security list 12000 in total  
Networking Service |  Egress rules |  30 per security list 12000 in total  
Networking Service |  DNS zones |  1000 (in addition to any internal zones)  
Networking Service |  DNS records |  25000 per zone 8000000 in total  
Compute Service |  Custom images |  100  
Block Storage Service |  Aggregated size of block volumes |  100 TB (with default storage capacity)  
Block Storage Service |  Block volume backups |  100000  
File Storage Service |  File systems |  100  
File Storage Service |  Mount targets |  PCA_POOL 80  PCA_POOL_HIGH 80  
File Storage Service |  File system size |  3.3 PB  
Object Storage Service |  Buckets |  10000  
(Network) Load Balancing Service |  Load balancers (Network LB and LBaaS combined) |  20 in a single VCN up to 144 in total, depending on system compute capacity  
(Network) Load Balancing Service |  IP address |  1 per load balancer  
(Network) Load Balancing Service |  Network security groups |  5 per load balancer  
(Network) Load Balancing Service |  Listeners |  16 per load balancer  
(Network) Load Balancing Service |  Backend sets |  4 per load balancer  
(Network) Load Balancing Service |  Backend servers |  512 per load balancer and per backend set  
Kubernetes Engine (OKE) |  Clusters |  20 per tenancy  
Kubernetes Engine (OKE) |  Worker nodes |  128 per cluster (across all pools)  
Kubernetes Engine (OKE) |  Nodes per node pool/group | 128  
Kubernetes Engine (OKE) |  Pods |  110 per node (Kubernetes default)   
Was this article helpful?
YesNo

