Updated 2024-12-16
# Creating an OKE VCN
On Compute Cloud@Customer, to configure OKE, create a VCN, and a public route and a private route.
Create the following resources in the order listed:
  1. [Create the VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule__configure-vcn)
  2. [Create a Private Route Table](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule__create-private-route)
  3. [Create a Public Route Table](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule__public-route)
  4. [Modify the VCN Default Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-vcn-gateway-route-rule.htm#creating-a-vcn-gateway-route-rule__vcn-default-sec-list)


## Create the VCN 🔗 
To create the VCN, follow the instructions in [Creating a VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm#creating-a-vcn "On Compute Cloud@Customer, a virtual cloud network \(VCN\) a virtual, private network that closely resembles a traditional network. VCNs can be further divided into IP subnets. VCNs can communicate with each other through various types of gateways, each type intended for a particular purpose."), and use the parameters listed in this section. For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
**Note** Subnets are created later, and described in subsequent sections.
For this example, use the following input to create the VCN. The VCN covers one contiguous CIDR block. The CIDR block can't be changed after the VCN is created.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: oketest-vcn
  * CIDR Block: `vcn_cidr`
  * DNS Label: oketest This label must be unique across all VCNs in the tenancy.

| 
  * `--display-name`: `oketest-vcn`
  * `--cidr-blocks`: `'["vcn_cidr"]'`
  * `--dns-label`: `oketest` This label must be unique across all VCNs in the tenancy.

  
Note the OCID of the new VCN for use later. In the examples in this guide, this VCN OCID is `ocid1.vcn.oke_vcn_id`.
## Create a Private Route Table 🔗 
Create a NAT gateway, and edit the default route table to reference the NAT gateway. This enables traffic to go outside the VCN but not to the internet (for example, to your data center). 

Create a NAT Gateway
    
To create the NAT gateway, use the instructions in [Configuring a NAT Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-a-nat-gateway.htm#configuring-a-nat-gateway "On Compute Cloud@Customer, you can configure NAT gateways for VCNs."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
Note the name and OCID of the NAT gateway for assignment to the private route rule. 

Create a Private Route Rule
    
Modify the default route table, using the following input to create a private route rule that references the NAT gateway that was created in the preceding step. See [Updating Route Table Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-route-table-rules.htm#updating-route-table-rules "On Compute Cloud@Customer, you can change the name of a route table and add, edit, or delete rules in a route table.").
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Display name: Default - private

Route rule
  * Target Type: NAT Gateway
  * NAT Gateway: Name of the NAT gateway that was created in the preceding step
  * CIDR Block: 0.0.0.0/0
  * Description: OKE private route rule

| 
  * `--rt-id`: `ocid1.routetable.default_routetable_id`
  * `--display-name`: Default - private

`--route-rules`
  * `networkEntityId`: OCID of the NAT gateway that was created in the preceding step
  * `destinationType`: `CIDR_BLOCK`
  * `destination`: `0.0.0.0/0`
  * `description`: OKE private route rule

  
Note the name and OCID of this route table for assignment to private subnets.
## Create a Public Route Table 🔗 
Create an Internet gateway and a route table with a route rule that references the Internet gateway. This enables internet access for OKE nodes. 

Create an Internet Gateway
    
To create the internet gateway, use the instructions in [Configuring an Internet Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-an-internet-gateway.htm#configuring-an-internet-gateway "On Compute Cloud@Customer, you can configure an Internet Gateway \(IGW\) which provides the VCN with outside access through the on-premises data center network."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
Note the name and OCID of the internet gateway for assignment to the public route rule. 

Create a Public Route Rule
    
Create a public route rule for the internet gateway you just created. To create a route table, use the instructions in [Creating a Route Table](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-route-table.htm#creating-a-route-table "On Compute Cloud@Customer, route rules are required to send traffic outside the VCN. If you don't need to send traffic outside the VCN, you can use the default route table that was created when the VCN was created. The default route table has no rules."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
For this example, use the following input to create the route table with a public route rule that references the internet gateway that was created in the preceding step.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
  * Name: public

Route rule
  * Target Type: Internet Gateway
  * Internet Gateway: Name of the internet gateway that was created in the preceding step
  * CIDR Block: 0.0.0.0/0
  * Description: OKE public route rule

| 
  * `--vcn-id`: `ocid1.vcn.oke_vcn_id`
  * `--display-name`: public

`--route-rules`
  * `networkEntityId`: OCID of the internet gateway that was created in the preceding step
  * `destinationType`: `CIDR_BLOCK`
  * `destination`: `0.0.0.0/0`
  * `description`: OKE public route rule

  
## Modify the VCN Default Security List 🔗 
To modify a security list, see [Updating a Security List](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-security-list.htm#updating-a-security-list "On Compute Cloud@Customer, you can edit the name of the security list and add, edit, or delete rules or tags in any security list, including the default security list."). For Terraform input, see [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
Delete all the default rules, then create the rules shown in the following table.
[Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") property |  CLI property  
---|---  
`--security-list-id`: `ocid1.securitylist.default_securitylist_id`  
**One egress security rule:**
  * Stateless: clear the box
  * Egress CIDR: 0.0.0.0/0
  * IP Protocol: All protocols
  * Description: "Allow all outgoing traffic."

|  **One egress security rule:** `--egress-security-rules`
  * `isStateless`: `false`
  * `destination`: `0.0.0.0/0`
  * `destinationType`: `CIDR_BLOCK`
  * `protocol`: `all`
  * `description`: "Allow all outgoing traffic."

  
**Three ingress security rules:** |  **Three ingress security rules:** `--ingress-security-rules`  
**Ingress Rule 1**
  * Stateless: clear the box
  * Ingress CIDR: `vcn_cidr`
  * IP Protocol: ICMP
    * Parameter Type: 8: Echo
  * Description: "Allow ping from VCN."

|  **Ingress Rule 1**
  * `isStateless`: `false`
  * `source`: `vcn_cidr`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `1`
  * `icmpOptions`
    * `type`: `8`
  * `description`: "Allow ping from VCN."

  
**Ingress Rule 2**
  * Stateless: clear the box
  * Ingress CIDR: 0.0.0.0/0
  * IP Protocol: ICMP
    * Parameter Type: 3: Destination Unreachable
  * Description: "Allow unreachables."

|  **Ingress Rule 2**
  * `isStateless`: `false`
  * `source`: `0.0.0.0/0`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `1`
  * `icmpOptions`
    * `type`: `3`
  * `description`: "Allow unreachables."

  
**Ingress Rule 3**
  * Stateless: clear the box
  * Ingress CIDR: 0.0.0.0/0
  * IP Protocol: ICMP
    * Parameter Type: 11: Time Exceeded
  * Description: "Allow time exceeded."

|  **Ingress Rule 3**
  * `isStateless`: `false`
  * `source`: `0.0.0.0/0`
  * `sourceType`: `CIDR_BLOCK`
  * `protocol`: `1`
  * `icmpOptions`
    * `type`: `11`
  * `description`: "Allow time exceeded."

  
Note the name and OCID of this default security list for assignment to subnets.
**What's Next:**
[Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.")
Was this article helpful?
YesNo

