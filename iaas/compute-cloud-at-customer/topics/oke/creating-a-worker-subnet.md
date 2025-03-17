Updated 2024-12-16
# Creating an OKE Worker Subnet
On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.
Create the following resources in the order listed:
  1. [Create a Worker Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet__external-access-security-list).
  2. [Create the Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet__worker-subnet).


## Create a Worker Security List 🔗 
To create a security list, use the instructions in [Creating a Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm#creating-a-security-list "On Compute Cloud@Customer, you can create a security list for a VCN."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
This security list defines traffic that's allowed to contact worker nodes directly.
For this example, use the following input for the worker subnet security list.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") |  CLI property  
---|---  
  * Name: worker-seclist

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `worker-seclist`

  
**Seven ingress security rules:** |  **Seven ingress security rules:** `--ingress-security-rules`  
**Ingress Rule 1**
  * Stateless: clear the check box
  * Ingress CIDR: `vcn_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 22
  * Description: "Allow intra-VCN `ssh`."

|  **Ingress Rule 1**
  * `isStateless`: `false`
  * `source`: `vcn_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `22`
    * `min`: `22`
  * `description`: "Allow intra-VCN `ssh`."

  
**Ingress Rule 2**
  * Stateless: clear the check box
  * Ingress CIDR: `kube_client_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 30000-32767
  * Description: "Allow clients to contact the node port range."

|  **Ingress Rule 2**
  * `isStateless`: `false`
  * `source`: `kube_client_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `32767`
    * `min`: `30000`
  * `description`: "Allow clients to contact the node port range."

  
**Ingress Rule 3**
  * Stateless: clear the check box
  * Ingress CIDR: `workerlb_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 30000-32767
  * Description: "Allow the worker load balancer to contact the worker nodes."

|  **Ingress Rule 3**
  * `isStateless`: `false`
  * `source`: `workerlb_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `32767`
    * `min`: `30000`
  * `description`: "Allow the worker load balancer to contact the worker nodes."

  
**Ingress Rule 4**
  * Stateless: clear the check box
  * Ingress CIDR: `workerlb_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 10256
  * Description: "Allow the worker load balancer to contact the worker nodes."

|  **Ingress Rule 4**
  * `isStateless`: `false`
  * `source`: `workerlb_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `10256`
    * `min`: `10256`
  * `description`: "Allow the worker load balancer to contact the worker nodes."

  
**Ingress Rule 5**
  * Stateless: clear the check box
  * Ingress CIDR: `kmi_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 22-65535
  * Description: "Allow the control plane to contact the worker nodes."

|  **Ingress Rule 5**
  * `isStateless`: `false`
  * `source`: `kmi_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `65535`
    * `min`: `22`
  * `description`: "Allow the control plane to contact the worker nodes."

  
**Ingress Rule 6**
  * Stateless: clear the check box
  * Ingress CIDR: `worker_cidr`
  * IP Protocol: UDP
    * Destination Port Range: 8285-8472
  * Description: "Allow flannel traffic."

|  **Ingress Rule 6**
  * `isStateless`: `false`
  * `source`: `worker_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `17`
  * `udpOptions` `destinationPortRange`
    * `max`: `8472`
    * `min`: `8285`
  * `description`: "Allow flannel traffic."

  
**Ingress Rule 7**
  * Stateless: clear the check box
  * Ingress CIDR: `kmi_cidr`
  * IP Protocol: UDP
    * Destination Port Range: 8285-8472
  * Description: "Allow flannel traffic."

|  **Ingress Rule 7**
  * `isStateless`: `false`
  * `source`: `kmi_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `17`
  * `udpOptions` `destinationPortRange`
    * `max`: `8472`
    * `min`: `8285`
  * `description`: "Allow flannel traffic."

  
## Create the Worker Subnet 🔗 
To create a subnet, use the instructions in [Creating a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm#creating-a-subnet "On Compute Cloud@Customer, a subnet is a subdivision of a VCN. For each VCN, you create one or more subnets."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
For this example, use the following input for the worker subnet security list. Use the OCID of the VCN that was created in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route."). Create the worker subnet in the same compartment where you created the VCN.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: worker
  * CIDR Block: `worker_cidr`
  * Route Table: Select "Default - private" from the list
  * Private Subnet: check the box
  * DNS Hostnames: Use DNS Hostnames in this Subnet: check the box
    * DNS Label: worker
  * Security Lists: Select "worker-seclist" and "Default Security List for oketest-vcn" from the list

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `worker`
  * `--cidr-block`: `worker_cidr`
  * `--dns-label`: `worker`
  * `--prohibit-public-ip-on-vnic`: `true`
  * `--route-table-id`: OCID of the "Default - private" route table
  * `--security-list-ids`: OCIDs of the "worker-seclist" security list and the "Default Security List for oketest-vcn" security list

  
**What's Next:**
[Creating an OKE Worker Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a security list and a worker load balancer subnet.")
Was this article helpful?
YesNo

