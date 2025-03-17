Updated 2024-12-16
# Creating an OKE Control Plane Subnet
On Compute Cloud@Customer, part of configuring OKE requires creating external and internal access security lists and a control plane subnet.
Create the following resources in the order listed:
  1. [Create a Control Plane Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-subnet.htm#creating-a-control-plane-subnet__external-security-list-cp-subnet)
  2. [Create the Control Plane Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-subnet.htm#creating-a-control-plane-subnet__cp-subnet)


## Create a Control Plane Security List 🔗 
To create a security list, use the instructions in [Creating a Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm#creating-a-security-list "On Compute Cloud@Customer, you can create a security list for a VCN."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
For this example, use the following input for the control plane subnet security list.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: kmi-seclist

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `kmi-seclist`

  
**Six ingress security rules:** |  **Six ingress security rules:** `--ingress-security-rules`  
**Ingress Rule 1**
  * Stateless: clear the check box
  * Ingress CIDR: `kube_client_cidr`
  * IP Protocol: TCP
    * Destination Port Range: `kubernetes_api_port`
  * Description: "Allow inbound connections to the Kubernetes API server."

|  **Ingress Rule 1**
  * `isStateless`: `false`
  * `source`: `kube_client_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `kubernetes_api_port`
    * `min`: `kubernetes_api_port`
  * `description`: "Allow inbound connections to the Kubernetes API server."

  
**Ingress Rule 2**
  * Stateless: clear the check box
  * Ingress CIDR: `kmilb_cidr`
  * IP Protocol: TCP
    * Destination Port Range: `kubernetes_api_port`
  * Description: "Allow inbound connections from the control plane load balancer."

|  **Ingress Rule 2**
  * `isStateless`: `false`
  * `source`: `kmilb_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `kubernetes_api_port`
    * `min`: `kubernetes_api_port`
  * `description`: "Allow inbound connections from the control plane load balancer."

  
**Ingress Rule 3**
  * Stateless: clear the check box
  * Ingress CIDR: `worker_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 1024-65535
  * Description: "Allow inbound connections from worker nodes to the control plane."

|  **Ingress Rule 3**
  * `isStateless`: `false`
  * `source`: `worker_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `65535`
    * `min`: `1024`
  * `description`: "Allow inbound connections from worker nodes to the control plane."

  
**Ingress Rule 4**
  * Stateless: clear the check box
  * Ingress CIDR: `kmi_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 1024-65535
  * Description: "Allow inbound connections within the control plane."

|  **Ingress Rule 4**
  * `isStateless`: `false`
  * `source`: `kmi_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `65535`
    * `min`: `1024`
  * `description`: "Allow inbound connections within the control plane."

  
**Ingress Rule 5**
  * Stateless: clear the check box
  * Ingress CIDR: `worker_cidr`
  * IP Protocol: UDP
    * Destination Port Range: 8285-8472
  * Description: "Allow flannel traffic."

|  **Ingress Rule 5**
  * `isStateless`: `false`
  * `source`: `worker_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `17`
  * `udpOptions` `destinationPortRange`
    * `max`: `8472`
    * `min`: `8285`
  * `description`: "Allow flannel traffic."

  
**Ingress Rule 6**
  * Stateless: clear the check box
  * Ingress CIDR: `kmi_cidr`
  * IP Protocol: UDP
    * Destination Port Range: 8285-8472
  * Description: "Allow flannel traffic."

|  **Ingress Rule 6**
  * `isStateless`: `false`
  * `source`: `kmi_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `17`
  * `udpOptions` `destinationPortRange`
    * `max`: `8472`
    * `min`: `8285`
  * `description`: "Allow flannel traffic."

  
## Create the Control Plane Subnet 🔗 
To create a subnet, use the instructions in [Creating a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm#creating-a-subnet "On Compute Cloud@Customer, a subnet is a subdivision of a VCN. For each VCN, you create one or more subnets."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources."). 
Use the following input to create the control plane subnet. Use the OCID of the VCN that was created in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route."). Create the control plane subnet in the same compartment where you created the VCN.
**Important**
The name of this subnet must be exactly `control-plane`.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * **Name:** control-plane
  * **CIDR Block:** `kmi_cidr`
  * Route Table: Select "Default - private" from the list
  * **Private Subnet:** check the box
  * **DNS Hostnames:** **Use DNS Hostnames in this Subnet:** check the box
    * **DNS Label:** kmi
  * Security Lists: Select "kmi-seclist" and "Default Security List for oketest-vcn" from the list

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `control-plane`
  * `--cidr-block`: `kmi_cidr`
  * `--dns-label`: `kmi`
  * `--prohibit-public-ip-on-vnic`: `true`
  * `--route-table-id`: OCID of the "Default - private" route table
  * `--security-list-ids`: OCIDs of the "kmi-seclist" security list and the "Default Security List for oketest-vcn" security list

  
**What's Next:**
[Creating an OKE Control Plane Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-load-balancer-subnet.htm#creating-a-control-plane-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a control plane security list and a control plane load balancer subnet.")
Was this article helpful?
YesNo

