Updated 2024-12-16
# Creating an OKE Worker Load Balancer Subnet
On Compute Cloud@Customer, part of configuring OKE requires creating a security list and a worker load balancer subnet.
Create the following resources in the order listed:
  1. [Create a Worker Load Balancer Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet__section_o44_zcp_qyb)
  2. [Create the Worker Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet__section_idh_s4z_qzb)


## Create a Worker Load Balancer Security List 🔗 
Create a security list and a worker load balancer subnet. To create a security list, use the instructions in [Creating a Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm#creating-a-security-list "On Compute Cloud@Customer, you can create a security list for a VCN."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
This security list defines traffic, such as applications, that's allowed to contact the worker load balancer.
For this example, use the following input for the worker load balancer subnet security list. These sources and destinations are examples; adjust these for your applications.
**Note**
When you create an external load balancer for your containerized applications (see [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.")), remember to add that load balancer service front-end port to this security list.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: workerlb-seclist

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `workerlb-seclist`

  
**Two ingress security rules:** |  **Two ingress security rules:** `--ingress-security-rules`  
**Ingress Rule 1**
  * Stateless: clear the check box
  * Ingress CIDR: `kube_client_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 80
  * Description: "Allow inbound traffic for applications."

|  **Ingress Rule 1**
  * `isStateless`: `false`
  * `source`: `kube_client_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `80`
    * `min`: `80`
  * `description`: "Allow inbound traffic for applications."

  
**Ingress Rule 2**
  * Stateless: clear the check box
  * Ingress CIDR: `kube_client_cidr`
  * IP Protocol: TCP
    * Destination Port Range: 443
  * Description: "Allow inbound traffic for applications."

|  **Ingress Rule 2**
  * `isStateless`: `false`
  * `source`: `kube_client_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `6`
  * `tcpOptions` `destinationPortRange`
    * `max`: `443`
    * `min`: `443`
  * `description`: "Allow inbound traffic for applications."

  
## Create the Worker Load Balancer Subnet 🔗 
To create a subnet, use the instructions in [Creating a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-subnet.htm#creating-a-subnet "On Compute Cloud@Customer, a subnet is a subdivision of a VCN. For each VCN, you create one or more subnets.") For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources."). 
For this example, use the following input to create the worker load balancer subnet. Use the OCID of the VCN that was created in [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route."). Create the worker load balancer subnet in the same compartment where you created the VCN.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: service-lb
  * CIDR Block: `workerlb_cidr`
  * Route Table: Select "public" from the list
  * Public Subnet: check the box
  * DNS Hostnames: Use DNS Hostnames in this Subnet: check the box
    * DNS Label: servicelb
  * Security Lists: Select "workerlb-seclist" and "Default Security List for oketest-vcn" from the list

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: `service-lb`
  * `--cidr-block`: `workerlb_cidr`
  * `--dns-label`: `servicelb`
  * `--prohibit-public-ip-on-vnic`: `false`
  * `--route-table-id`: OCID of the "public" route table
  * `--security-list-ids`: OCIDs of the "workerlb-seclist" security list and the "Default Security List for oketest-vcn" security list

  
**What's Next:**
[Creating an OKE Control Plane Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-subnet.htm#creating-a-control-plane-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating external and internal access security lists and a control plane subnet.")
Was this article helpful?
YesNo

