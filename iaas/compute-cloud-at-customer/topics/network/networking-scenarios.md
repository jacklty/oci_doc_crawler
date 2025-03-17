Updated 2024-10-07
# Networking Scenarios
Learn about various networking scenarios for Compute Cloud@Customer. 
The following sections describe basic networking scenarios to help you understand the networking service and how networking components operate together.
**Important**
Regardless of the selected networking scenario, always ensure that the IP address ranges configured as Compute Cloud@Customer public IPs don't conflict with IP addresses used within the data center network.
When configuring virtual cloud networks (VCNs) with a dynamic routing gateway (DRG), ensure that the VCN IP address ranges don't overlap with each other or with the on-premises network.
  * [Scenario A – Public Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/networking-scenarios.htm#public-subnet "This scenario describes a setup consisting of a VCN and a public subnet on Compute Cloud@Customer.") describes a setup consisting of a VCN and a public subnet on Compute Cloud@Customer. 
  * [Scenario B – Private Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/networking-scenarios.htm#private-subnet "This scenario describes a setup consisting of a VCN and a private subnet on Compute Cloud@Customer.") describes a setup consisting of a VCN and a private subnet on Compute Cloud@Customer. 
  * [Scenario C – Public and Private Subnets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/networking-scenarios.htm#public-and-private-subnets "This scenario describes a multitier setup consisting of a VCN with a public and a private subnet on Compute Cloud@Customer.") describes a multitier setup consisting of a VCN with a public and a private subnet on Compute Cloud@Customer.


## Scenario A – Public Subnet 🔗 
This scenario describes a setup consisting of a VCN and a public subnet on Compute Cloud@Customer.
For external connectivity the VCN needs an internet gateway. Your on-premises network also uses this gateway to communicate with resources inside the VCN. The IP addresses used in this scenario must be public. In a private cloud context, this means a unique address directly reachable from the on-premises network.
The subnet uses the default security list, which has default rules that are designed to simplify getting started. The rules enable typical required access; for example inbound SSH connections and any type of outbound connections. Remember that security list rules only allow traffic. Any traffic not explicitly covered by a security list rule is implicitly denied. In this scenario, you add more rules to the default security list. You could instead create a custom security list for those rules. You would then set up the subnet to use both the default security list and the custom security list.
The subnet uses the default route table, which contains no rules when the VCN is created. In this scenario, the table has only a single rule: to route traffic intended for all destinations (0.0.0.0/0) through the internet gateway.
To set up this networking scenario, you perform the following steps:
  1. Create the VCN.
Choose a compartment you have permission to work in. Specify one or more non-overlapping CIDR blocks for the VCN; for example: 172.16.0.0/16. Optionally, enable DNS and specify a DNS label for the VCN.
  2. Create the public subnet.
Specify a single, contiguous CIDR block within the VCN CIDR block; for example: 172.16.10.0/24. Select the default route table. Ensure the subnet is a public subnet, so that instances can obtain public IP addresses. If you enabled DNS at the VCN level, you can choose to assign host names in the subnet and specify a subnet DNS label as well.
  3. Create the internet gateway.
When you create the internet gateway, it's enabled immediately. However, you must add a route rule to allow traffic to flow to the gateway.
  4. Update the default route table to use the internet gateway.
The default route table starts out with no rules. No route rule is required to route traffic within the VCN itself. You must add a rule that routes all traffic destined for addresses outside the VCN to the internet gateway. Enter these parameters:
     * Target Type: Internet Gateway
     * Destination CIDR block: 0.0.0.0/0
This means that all non-intra-VCN traffic that's not already covered by other rules in the route table goes to the target specified in this rule.
     * Target: The internet gateway you created.
Because the subnet was set up to use the default route table, the resources in the subnet can now use the internet gateway. The existence of this rule also enables inbound connections to the subnet, through the internet gateway. The next step is to specify the types of traffic you want to allow into and out of the instances you later create in the subnet.
  5. Update the default security list.
You set up the subnet to use the VCN default security list. Now you add security list rules that allow the types of connections that the instances in the VCN need.
For example, if the instances in your subnet are web servers, they likely need to receive inbound HTTPS connections. To enable that traffic, add an ingress rule to the default security list using these parameters:
     * Source Type: CIDR
     * Source CIDR: 0.0.0.0/0
     * IP Protocol: TCP
     * Source Port Range: All
     * Destination Port Range: 443
  6. Create instances.
Your next step is to create one or more instances in the subnet. Each instance automatically gets a private IP address. With the network setup in this scenario, you must give each instance a public IP address, otherwise you can't access them through the internet gateway.


## Scenario B – Private Subnet 🔗 
This scenario describes a setup consisting of a VCN and a private subnet on Compute Cloud@Customer. 
For connectivity to your on-premises network, the VCN needs a dynamic routing gateway (DRG).
The subnet uses the default security list, which has default rules that are designed simplify getting started. The rules enable typical required access; for example inbound SSH connections and any type of outbound connections. Remember that security list rules only allow traffic. Any traffic not explicitly covered by a security list rule is implicitly denied. In this scenario, you add more rules to the default security list. You could instead create a custom security list for those rules. You would then set up the subnet to use both the default security list and the custom security list.
The subnet uses the default route table, which contains no rules when the VCN is created. In this scenario, the table has only a single rule: to route traffic intended for all destinations (0.0.0.0/0) through the DRG.
To set up this networking scenario, you perform the following steps:
  1. Create the VCN.
Choose a compartment you have permission to work in. Specify one or more non-overlapping CIDR blocks for the VCN; for example: 172.16.0.0/16. Optionally, enable DNS and specify a DNS label for the VCN.
  2. Create the private subnet.
Specify a single, contiguous CIDR block within the VCN CIDR block; for example: 172.16.10.0/24. Make the subnet private; the instances you create can't obtain a public IP address. Select the default route table. If you enabled DNS at the VCN level, you can choose to assign host names in the subnet and specify a subnet DNS label as well.
  3. Update the default security list.
You set up the subnet to use the VCN default security list. Now you add security list rules that allow the types of connections that the instances in the VCN will need.
For example, if your subnet contains Microsoft Windows instances and you intend to access them using RDP, add an ingress rule to the default security list using these parameters:
     * Source Type: CIDR
     * Source CIDR: 0.0.0.0/0
     * IP Protocol: TCP
     * Source Port Range: All
     * Destination Port Range: 3389
  4. Create a dynamic routing gateway (DRG) and attach it to your VCN.
When you create the DRG, it is in "Provisioning" state for a short period. Ensure provisioning is done before continuing. Next, attach the DRG you just created to your VCN. For this scenario you can ignore the advanced attachment options. The DRG attachment will be in "Attaching" state for a short period before it's ready.
To allow traffic to flow to the DRG, you must add a route rule.
  5. Update the default route table to use the DRG.
The default route table starts out with no rules. No route rule is required to route traffic within the VCN itself. You must add a rule that routes all traffic destined for addresses in your on-premises network to the DRG. Enter these parameters:
     * Target Type: Dynamic Routing Gateway.
The VCN attached DRG is automatically selected as the target.
     * Destination CIDR block: 0.0.0.0/0
This means that all non-intra-VCN traffic that is not already covered by other rules in the route table goes to the target specified in this rule.
Because the subnet was set up to use the default route table, the DRG now enables traffic between the resources in the subnet and in your on-premises network.
  6. Create instances.
Your next step is to create one or more instances in the subnet. Each instance automatically gets a private IP address. With the network setup in this scenario, no additional configuration is required to access the instances from your on-premises network.


## Scenario C – Public and Private Subnets 🔗 
This scenario describes a multitier setup consisting of a VCN with a public and a private subnet on Compute Cloud@Customer.
The public subnet holds public instances such as web servers, and the private subnet holds private instances such as database servers. The VCN has a dynamic routing gateway (DRG) for connectivity to your on-premises network. Instances in the public subnet have external access through an internet gateway.
**Note**
In a public cloud environment, instances in the private subnet could be allowed to initiate external connections using a NAT gateway, for example to get software updates. However, in Compute Cloud@Customer the NAT gateway would provide access to the on-premises network, which the DRG already enables for those instances. The combination of a NAT gateway and DRG could cause issues because of nondeterministic routing.
Each subnet uses the default security list, which has default rules that are designed to simplify getting started. The rules enable typical required access; for example inbound SSH connections and any type of outbound connections. Remember that security list rules only allow traffic. Any traffic not explicitly covered by a security list rule is implicitly denied.
Each subnet also has its own custom security list and custom route table with rules specific to the needs of the subnet's instances. In this scenario, the VCN default route table, which is always empty to start with, is not used.
To set up this networking scenario, you perform the following steps:
  1. Create the VCN.
Choose a compartment you have permission to work in. Specify one or more nonoverlapping CIDR blocks for the VCN; for example: 172.16.0.0/16. Optionally, enable DNS and specify a DNS label for the VCN.
  2. Add the necessary gateways to the VCN.
The instances in the public subnet need an internet gateway for incoming and outgoing public traffic. The instances in the private subnet need a NAT gateway to be able to reach the data center network and the internet. These gateways are enabled immediately upon creation, but you must add route rules to allow traffic to flow to them.
To reach the private instances in the VCN from your on-premises network, you create a DRG and attach it to the VCN. When you create the DRG, it's in "Provisioning" state for a short period. Ensure provisioning is done before attaching it to the VCN. For this scenario you can ignore the advanced attachment options. The DRG attachment will be in an "Attaching" state for a short period before it's ready. To allow traffic to flow to the DRG, you must also add a route rule.
  3. Create custom route tables for the subnets that you create later.
    1. For the public subnet, create a route table and add a rule that routes all traffic destined for addresses outside the VCN to the internet gateway. Enter these parameters:
       * Target Type: Internet Gateway
       * Destination CIDR block: 0.0.0.0/0
This means that all non-intra-VCN traffic that's not already covered by other rules in the route table goes to the target specified in this rule.
       * Target: The internet gateway you created.
    2. For the private subnet, create a route table and add two rules: one that routes traffic destined for the on-premises network to the DRG, and one that routes all other traffic leaving the VCN to the NAT gateway.
Create the route rule for the NAT gateway with these parameters:
       * Target Type: NAT Gateway
       * Destination CIDR block: 0.0.0.0/0
This means that all nonintra-VCN traffic that's not already covered by other rules in the route table goes to the target specified in this rule.
       * Target: The NAT gateway you created.
Create the route rule for the DRG with these parameters:
       * Target Type: Dynamic Routing Gateway.
The VCN's attached DRG is automatically selected as the target.
       * Destination CIDR block: 10.25.0.0/16
This means that traffic intended for an address in the on-premises network (10.25.x.y) goes to the DRG target specified in this rule.
  4. Update the default security list.
Add security list rules that allow the types of connections that the instances in the VCN will need.
Edit each of the existing stateful ingress rules so that the Source CIDR is **not** 0.0.0.0/0, but the CIDR for your on-premises network; in this example: 10.25.0.0/16.
  5. Create custom security lists for the subnets you will create later.
    1. Create a custom security list for the public subnet and add rules to allow the types of connections that the public instances need. For example, web servers likely need to receive HTTP and HTTPS ingress traffic. For HTTP, use the following settings. For HTTPS, add another similar rule for TCP port 443.
       * Source Type: CIDR
       * Source CIDR: 0.0.0.0/0
       * IP Protocol: TCP
       * Source Port Range: All
       * Destination Port Range: 80
    2. Create a custom security list for the private subnet and add rules to allow the types of connections that the private instances need. For example, database servers likely need to receive SQL*Net (TCP port 1521) ingress traffic from clients in the private and the public subnet. For clients in the public subnet, use the following settings. For clients in the private subnet, add another similar rule for the CIDR of the private subnet (172.16.1.0/24).
       * Source Type: CIDR
       * Source CIDR: 172.16.2.0/24
       * IP Protocol: TCP
       * Source Port Range: All
       * Destination Port Range: 1521
  6. Create the subnets in the VCN.
     * Public subnet:
Specify a single, contiguous CIDR block within the VCN CIDR block; for example: 172.16.2.0/24. Ensure the subnet is a public subnet, so that instances can obtain public IP addresses. Select the custom public subnet route table you created earlier.
Select two security lists: both the default security list and the public subnet security list you created earlier. If you enabled DNS at the VCN level, you can choose to assign host names in the subnet and specify a subnet DNS label as well.
     * Private subnet:
Specify a single, contiguous CIDR block within the VCN CIDR block; for example: 172.16.1.0/24. Make the subnet private; the instances you create in this subnet can't obtain a public IP address. Select the custom private subnet route table you created earlier.
Select two security lists: both the default security list and the private subnet security list you created earlier. If you enabled DNS at the VCN level, you can choose to assign host names in the subnet and specify a subnet DNS label as well.
  7. Create instances.
Your next step is to create instances in the subnets. Each instance automatically gets a private IP address. For each instance in the public subnet, ensure to assign the instance a public IP address. Otherwise, you won't be able to reach the instance from your on-premises network. The DRG you set up allows you to reach the instances in the private subnet from your on-premises network without any additional configuration.


Was this article helpful?
YesNo

