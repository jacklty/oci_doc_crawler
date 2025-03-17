Updated 2024-12-18
# Creating OKE Network Resources
Learn about the required network resources for Kubernetes Engine (OKE) on Compute Cloud@Customer.
The resource definitions in the following sections create a working example set of network resources for workload clusters. Use this configuration as a guide when you create these resources. You can change the values of properties such as CIDR blocks and IP addresses. Don't change the values of properties such as the network protocol, the stateful setting, or the private/public setting. 
See [Workload Cluster Network Ports](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-network-ports.htm#oke-network-ports "Learn about the required ports for OKE on Compute Cloud@Customer.") for specific ports that must be open for specific purposes.
## OKE Cluster Management Across Networks 🔗 
Compute Cloud@Customer admin and data networks are configured for your environment by Oracle, when Oracle installs the Compute Cloud@Customer infrastructure in your data center.
The OKE service runs on the management nodes in the admin network, while the OKE clusters are deployed in the data network as shown in the following diagram. 
![A diagram showing the relationship between the admin and compute networks.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/admin-network-oke-example.png)
The management interface of an OKE cluster is port 6443 on its load balancer public IP address. This address is assigned from the data center IP range you reserved and configured as public IPs during the Compute Cloud@Customer infrastructure installation.
Because of the network segregation, traffic from the OKE service must exit the infrastructure through the admin network, and reenter through the data network to reach the OKE cluster. 
**Important**
Your data center network infrastructure must allow traffic in both directions. Without the necessary firewall and routing rules, users can't deploy OKE clusters.
See [Workload Cluster Network Ports](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-network-ports.htm#oke-network-ports "Learn about the required ports for OKE on Compute Cloud@Customer.") for ports needed for OKE. For information about other network ports, see [Network Port and Protocol Matrix](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/network-port-and-protocol-matrix.htm#network-port-and-protocol-matrix "Compute Cloud@Customer requires access permissions to be granted for certain IP addresses, ports, and protocols.").
## Ways to Create the OKE Network Resources 🔗 
Create the OKE network resources in one of the following ways:
  * Use Terraform scripts, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
  * [Configuring OKE Network Resources Individually](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/configuring-network-resources-individually.htm#configuring-network-resources-individually "On Compute Cloud@Customer, you can create the required OKE network resources individually using the Compute Cloud@Customer Console, CLI, or API.")


Both methods result in the creation of the following resources in the same compartment:
  * VCN
  * Internet gateway
  * NAT gateway
  * Route rules
  * Security lists
  * Four subnets:
    * Worker
    * Worker load balancer
    * Control plane
    * Control plane load balancer


Was this article helpful?
YesNo

