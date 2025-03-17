Updated 2025-02-12
# Scenario A: Public Subnet
Scenario A consists of a virtual cloud network (VCN) with a regional **public subnet** , which are required for network connectivity to Compute instances in a tenancy. Public servers are created in separate **availability domains** (ADs) for redundancy, and the VCN uses regional subnets because they're more flexible and easier to efficiently divide a VCN into subnets while also accounting for potential failure. The VCN is directly connected to the internet by way of an **internet gateway**. The gateway is also used for connectivity to an on-premises network. Any resource in an on-premises network that needs to communicate with resources in this VCN must have a public IP address and access to the internet.
Getting started with Oracle Cloud Infrastructure is easy because the subnet uses an initial [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default). This list contains security rules that allow typical required access (for example, inbound SSH connections and any type of outbound connections). Remember that security list rules only _allow_ traffic and traffic not explicitly allowed by a security list rule is implicitly _denied_. The same is true for route rules, which also require that outbound traffic is explicitly allowed and that traffic to specific destinations is sent to the necessary gateway. Routing destinations outside the VCN must be reachable through a gateway you create and explicitly specify in a route table associated with the subnet a resource uses.
In this scenario, you add a new rule to the default security list. This rule is required to give the Compute instances access to the internet. You could instead create a custom security list for this rule and set up the subnet to use both the default security list and the custom security list, but that's outside the scope of this scenario.
**Tip** Security lists are one way to control traffic in and out of the VCN's resources. You can also use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)
In this scenario, the subnet also uses the default route table, which starts out with no rules when the VCN is created. The table only needs a single rule for the internet gateway. 
This scenario doesn't use a [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).
The following figure shows resources with public IP addresses in a regional public subnet, with redundant resources in the same subnet but in a different AD. The public subnet route table allows all incoming traffic to enter and leave the public subnet through the internet gateway, uses the default security list, and uses the local routing that's built in to the VCN. The on-premises hosts must have public IP addresses to communicate with VCN resources over the internet. 
[![This image shows Scenario A: a VCN with a regional public subnet and internet gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_scenario_a_regional.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_scenario_a_regional.svg)
Callout 1: Regional public subnet route table Destination CIDR | Route target  
---|---  
0.0.0.0/0 | Internet Gateway  
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're a member of the administrators group, you probably already have the required access to implement Scenario A. Otherwise, you need access to Networking, and you need the ability to create instances. See [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
## Setting Up Scenario A in the Console 🔗 
Setup is easy in the Console. 
**Note** If you haven't created a VCN before, the workflow discussed at [Create a VCN with Internet Connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartnetworking.htm#VCN_with_Internet_Connectivity) is an easy way to create a VCN with public and private subnets, gateways, and the route rules and security rules needed to provide internet access to instances and other resources in the VCN. If you use the workflow to perform this task, the workflow can handle Tasks 1 to 5 in this scenario.
[Task 1: Create the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
**Note** To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
  3. Select **Create VCN**.
  4. Enter the following:
     * **Name:** A descriptive name for the VCN. It doesn't have to be unique, and it can't be changed later in the Console (though you can change it with the API). Avoid entering confidential information.
     * **Create in Compartment:** Leave as is. 
     * **IPv4 CIDR Blocks:** Enter at least one and up to five IPv4 CIDR blocks for the VCN. The CIDR blocks aren't allowed to overlap. For example: 172.16.0.0/16. You can add or remove CIDR blocks later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **Use DNS hostnames in this VCN:** This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select this option you can specify a **DNS Label** for the VCN, or you can let the Console to generate one for you. The dialog box automatically displays the corresponding **DNS Domain Name** for the VCN (`<VCN_DNS_label>.oraclevcn.com`). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network).
     * **IPv6 prefixes:** You can request that a single Oracle-allocated IPv6 /56 prefix is assigned to this VCN. Alternately, you can assign a BYOIPv6 prefix or ULA prefix to the VCN. This option is available for all commercial and government regions. For more information on IPv6, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  5. Select **Create Virtual Cloud Network**.
The VCN is then created and displayed on the **Virtual Cloud Networks** page in the compartment you chose. 


[Task 2: Create the regional public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
  1. While still viewing the VCN, select **Create Subnet**.
  2. Enter the following:
     * **Name:** A friendly name for the subnet (for example, Regional Public Subnet). It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Regional or Availability Domain specific:** Select **Regional** (recommended), which means the subnet spans all availability domains in the region. Later when you create an instance, you can create it in any Availability domain in the region. For more information, see [Availability Domains and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Regions).
     * **IPv4 CIDR Block:** A single, contiguous CIDR block within the VCN's CIDR block. For example: 172.16.0.0/24. You _can't_ change this value later. For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **IPv6 Prefixes:** You can request an Oracle-allocated IPv6 /64 prefix, or enter BYOIPv6 or ULA prefixes. You can have a maximum of three IPv6 prefixes in a subnet. After you assign an IPv6 prefix to a VCN, it must always have at least one IPv6 prefix assigned to it. This option is available for VCNs in all commercial and government regions, if the VCN is already enabled for IPv6. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
     * **Route Table:** Select the default route table.
     * **Private or public subnet** : Select **Public subnet** , which means instances in the subnet can optionally have public IP addresses. For more information, see [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private).
     * **Use DNS Hostnames in this Subnet:** This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The dialog box automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
     * **DHCP Options:** Select the set of DHCP options to associate with the subnet. If you already enabled compartment selection, first specify the compartment that contains the set of DHCP options. 
     * **Security Lists:** Ensure that the default security list is selected.
     * **Show Tagging Options:** Select this link to display options for adding tags to the subnet. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  3. Select **Create Subnet**.
The subnet is then created and displayed on the **Subnets** page. 


[Task 3: Create the internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
  1. While still viewing the VCN, under **Resources** , select **Internet Gateways**.
  2. Select **Create Internet Gateway**.
  3. Enter the following:
     * **Name:** A friendly name for the internet gateway. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in Compartment:** Leave as is. 
     * You can select **Show advanced options** to set the following options: 
       * **Route Table Association:** (Advanced option) Leave as is. You can associate a specific VCN route table with this gateway. After you associate a route table, the gateway must always have a route table associated with it. You can change the rules in the current route table or replace it with another route table. 
       * **Tags:** (Advanced option) Leave as is. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  4. Select **Create Internet Gateway**.
The internet gateway is created and displayed on the **Internet Gateways** page. The gateway is already enabled, but you must add a route rule that allows traffic to flow to the gateway.


[Task 4: Update the default route table to use the internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
The default route table starts out with no rules. Here you add a rule that routes all traffic destined for addresses outside the VCN to the internet gateway. The existence of this rule also allows inbound connections to come from the internet to the subnet, through the internet gateway. You use security list rules to control the _types of traffic_ that are allowed in and out of the instances in the subnet (see the next task).
No route rule is required to route traffic within the VCN itself.
  1. Under **Resources** , select **Route Tables**.
  2. Select the default route table to view its details.
  3. Select **Add Route Rule**.
  4. Enter the following:
     * **Target Type:** Internet Gateway
     * **Destination CIDR block:** 0.0.0.0/0 (which means that all traffic from the VCN to a destination outside the VCN that's not already covered by other rules in the route table goes to the target specified in this rule).
     * **Compartment:** The compartment containing the internet gateway.
     * **Target:** The internet gateway you created.
     * **Description:** An optional description of the rule.
  5. Select **Add Route Rules**.


The default route table now has a rule for the internet gateway. Because the subnet was set up to use the default route table, the resources in the subnet can now use the internet gateway. The next step is to specify the types of traffic you want to allow in and out of the instances you later create in the subnet.
[Task 5: Update the default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
Earlier you set up the subnet to use the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default). Now you add security list rules that allow the types of connections that the instances in the VCN need. 
For example: For a public subnet with an internet gateway, the (web server) instances you create might need to receive inbound HTTPS connections from the internet. Here's how to add another rule to the default security list to enable that traffic:
  1. Under **Resources** , select **Security Lists.**
  2. Select the default security list to view its details. By default, you land on the **Ingress Rules** page. 
  3. Select **Add Ingress Rules**.
  4. To enable inbound connections for HTTPS (TCP port 443), enter the following:
     * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
     * **Source Type:** CIDR
     * **Source CIDR:** 0.0.0.0/0
     * **IP Protocol:** TCP
     * **Source Port Range:** All
     * **Destination Port Range** : 443
     * **Description:** An optional description of the rule.
  5. Select **Add Ingress Rule**.


**Important**
Security List Rule for Windows Instances
If you're going to create Windows instances, you need to add a security list rule to enable Remote Desktop Protocol (RDP) access. To enable RDP, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists). 
For a production VCN, you typically set up one or more _custom_ security lists for each subnet. Optionally, you can edit the subnet to [use different security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#change-rules-securitylist "Change which security lists are used in a particular subnet in a virtual cloud network \(VCN\)."). If you decide not to use the default security list, do so only after carefully assessing which of its default rules you want to duplicate in a custom security list. For example: the [default ICMP rules in the default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) are important for receiving connectivity messages.
[Task 6: Create instances in separate availability domains](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)
The next step is to create one or more instances in the subnet. The scenario's diagram shows instances in two different availability domains. When you create the instance, you select the AD, which VCN and subnet to use, and several other characteristics. 
Each instance automatically gets a private IP address. When you create an instance in a _public subnet_ , you decide whether the instance gets a public IP address. With this network setup in Scenario A, you _must_ give each instance a public IP address, or else you can't access them through the internet gateway. The default (for a public subnet) is for the instance to get a public IP address.
After creating an instance in this scenario, you can connect to it over the internet with SSH or RDP from an on-premises network or other location on the internet. For more information and instructions, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
## Setting Up Scenario A with the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations:
  1. [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn): Always include a DNS label for the VCN if you want the instances to have hostnames (see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network)). 
  2. [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet): Create one regional public subnet. Include a DNS label for the subnet if you want the instances to have hostnames. Use the default route table, default security list, and default set of DHCP options. 
  3. [CreateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/CreateInternetGateway)
  4. [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable): To enable communication with the internet gateway, update the default route table to include a route rule with destination = 0.0.0.0/0, and destination target = the internet gateway. This rule routes all traffic destined for addresses outside the VCN to the internet gateway. No route rule is required to route traffic within the VCN itself.
  5. [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList): To allow specific types of connections to and from the instances in the subnet. 


**Important**
Security List Rule for Windows Instances
If you're going to create Windows instances, you need to add a security list rule to enable Remote Desktop Protocol (RDP) access. To enable RDP, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists).
The next step is to create one or more instances in the subnet. The scenario's diagram shows instances in two different availability domains. When you create the instance, you select the AD, which VCN and subnet to use, and several other characteristics. 
Each instance automatically gets a private IP address. When you create an instance in a _public subnet_ , you decide whether the instance gets a public IP address. With this network setup in Scenario A, you _must_ give each instance a public IP address, or else you can't access them through the internet gateway. The default (for a public subnet) is for the instance to get a public IP address.
After creating an instance in this scenario, you can connect to it over the internet with SSH or RDP from an on-premises network or other location on the internet. For more information and instructions, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
Was this article helpful?
YesNo

