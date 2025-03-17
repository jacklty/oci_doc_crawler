Updated 2024-04-19
# Configuring OKE Network Resources Individually
On Compute Cloud@Customer, you can create the required OKE network resources individually using the Compute Cloud@Customer Console, CLI, or API.
**Note**
Alternatively, you can create Terraform scripts to automate the process. See [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
Create the following network resources.
**Important**
Create all of these network resources in the same compartment.
  1. Configure a VCN with route tables and a security list. See [Creating an OKE VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule "On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route.").
  2. Create the following four subnets:
     * OKE Worker subnet, see [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.").
     * OKE Worker load balancer subnet, see [Creating an OKE Worker Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-load-balancer-subnet.htm#creating-a-worker-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a security list and a worker load balancer subnet.").
     * OKE Control plane subnet, see [Creating an OKE Control Plane Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-subnet.htm#creating-a-control-plane-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating external and internal access security lists and a control plane subnet.").
     * OKE Control plane load balancer subnet, see [Creating an OKE Control Plane Load Balancer Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-control-plane-load-balancer-subnet.htm#creating-a-control-plane-load-balancer-subnet "On Compute Cloud@Customer, part of configuring OKE requires creating a control plane security list and a control plane load balancer subnet.").


Was this article helpful?
YesNo

