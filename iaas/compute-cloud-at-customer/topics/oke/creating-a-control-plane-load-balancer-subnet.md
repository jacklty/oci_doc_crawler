Updated 2024-12-16
# Creating an OKE Control Plane Load Balancer Subnet
On Compute Cloud@Customer, part of configuring OKE requires creating a control plane security list and a control plane load balancer subnet.
Create the following resources in the order listed:
  1. [Create a Control Plane Load Balancer Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-load-balancer-subnet.htm#creating-a-control-plane-load-balancer-subnet__cp-lb-security-list).
  2. [Create the Control Plane Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-load-balancer-subnet.htm#creating-a-control-plane-load-balancer-subnet__cp-lb-subnet).


## Create a Control Plane Load Balancer Security List 🔗 
To create a security list, use the instructions in [Creating a Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm#creating-a-security-list "On Compute Cloud@Customer, you can create a security list for a VCN."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
The control plane load balancer accepts traffic on port 6443, which is also called `kubernetes_api_port` in these instructions. Adjust this security list to only accept connections from where you expect the network to run. Port 6443 must accept connections from the cluster control plane instances and worker instances.
For this example, use the following input for the control plane load balancer subnet security list.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: kmilb-seclist

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: kmilb-seclist

  
**Three ingress security rules:** |  **Three ingress security rules:** `--ingress-security-rules`  
**Ingress Rule 1:**
  * Stateless: clear the check box
  * Ingress CIDR: `253.255.0.0/16` This value is required. Do not change this CIDR value.
  * IP Protocol: TCP
    * Destination Port Range: `kubernetes_api_port`
  * Description: "Allow inbound connections to the control plane load balancer."

|  **Ingress Rule 1:**
  * `isStateless`: `false`
  * `source`: `253.255.0.0/16` This value is required. Do not change this CIDR value.
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `kubernetes_api_port`
    * `min`: `kubernetes_api_port`
  * `description`: "Allow inbound connections to the control plane load balancer."

  
**Ingress Rule 2:**
  * Stateless: clear the check box
  * Ingress CIDR: `kube_client_cidr`
  * IP Protocol: TCP
    * Destination Port Range: `kubernetes_api_port`
  * Description: "Allow inbound connections to the control plane load balancer."

|  **Ingress Rule 2:**
  * `isStateless`: `false`
  * `source`: `kube_client_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `kubernetes_api_port`
    * `min`: `kubernetes_api_port`
  * `description`: "Allow inbound connections to the control plane load balancer."

  
**Ingress Rule 3:**
  * Stateless: clear the check box
  * Ingress CIDR: `vcn_cidr`
  * IP Protocol: TCP
    * Destination Port Range: `kubernetes_api_port`
  * Description: "Allow inbound connections to the control plane load balancer."

|  **Ingress Rule 3:**
  * `isStateless`: `false`
  * `source`: `vcn_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `kubernetes_api_port`
    * `min`: `kubernetes_api_port`
  * `description`: "Allow inbound connections to the control plane load balancer."

  
## Create the Control Plane Load Balancer Subnet 🔗 
To create a subnet, use the instructions in [Creating a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm#creating-a-subnet "On Compute Cloud@Customer, a subnet is a subdivision of a VCN. For each VCN, you create one or more subnets."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources."). 
For this example, use the following input to create the control plane load balancer subnet. Use the OCID of the VCN that was created in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route."). Create the control plane load balancer subnet in the same compartment where you created the VCN.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: control-plane-endpoint
  * CIDR Block: `kmilb_cidr`
  * Route Table: Select "public" from the list
  * Public Subnet: check the box
  * DNS Hostnames: Use DNS Hostnames in this Subnet: check the box
    * DNS Label: kmilb
  * Security Lists: Select "kmilb-seclist" and "Default Security List for oketest-vcn" from the list

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `control-plane-endpoint`
  * `--cidr-block`: `kmilb_cidr`
  * `--dns-label`: `kmilb`
  * `--prohibit-public-ip-on-vnic`: `false`
  * `--route-table-id`: OCID of the "public" route table
  * `--security-list-ids`: OCIDs of the "kmilb-seclist" security list and the "Default Security List for oketest-vcn" security list

  
**What's Next:**
[Creating an OKE Cluster](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-cluster.htm#creating-a-kubernetes-cluster "Learn how to create OKE Clusters on Compute Cloud@Customer.")
Was this article helpful?
YesNo

