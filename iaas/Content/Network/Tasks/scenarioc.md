Updated 2025-02-12
# Scenario C: Public and Private Subnets with a VPN
This topic explains how to set up Scenario C, which is a simple example of a multi-tier setup. It consists of a Virtual Cloud Network (VCN) with a regional **public subnet** to hold public servers (such as web servers), and a regional **private subnet** to hold private servers (such as database servers). Servers are in separate **availability domains** for redundancy. 
The VCN has a **dynamic routing gateway** (DRG) and Site-to-Site VPN for connectivity to your on-premises network. Instances in the public subnet have direct access to the internet by way of an **internet gateway**. Instances in the private subnet can initiate internet connections by way of a **NAT gateway** (for example, to get software updates), but cannot receive inbound connections from the internet through that gateway. 
Each subnet uses the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default), which has default rules that are designed to make it easy to get started with Oracle Cloud Infrastructure. The rules enable typical required access (for example, inbound SSH connections and any type of outbound connections). Remember that security list rules only _allow_ traffic. Any traffic not explicitly covered by a security list rule is denied.
**Tip** Security lists are one way to control traffic in and out of the VCN's resources. You can also use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)
This scenario can use a legacy or upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
Each subnet also has its own custom security list and custom route table with rules specific to the needs of the subnet's instances. In this scenario, the VCN's default route table (which is always empty to start with) is not used.
See the following figure. 
[![This image shows Scenario C: a VCN with both a public and private subnet, an internet gateway, NAT gateway, and a VPN IPSec connection.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_scenario_c_regional.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_scenario_c_regional.svg)
Callout 1: Regional private subnet route table Destination CIDR | Route target  
---|---  
0.0.0.0/0 | NAT Gateway  
10.0.0.0/16 | DRG  
Callout 2: Regional public subnet route table Destination CIDR | Route target  
---|---  
0.0.0.0/0 | Internet Gateway  
**Tip** The scenario uses Site-to-Site VPN for connectivity. However, you could instead use [Oracle Cloud Infrastructure FastConnect.](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")
## Prerequisites 🔗 
To set up the VPN in this scenario, you need to get the following information from a network administrator:
  * Public IP address of the **customer-premises equipment** (CPE) at your end of the VPN 
  * Static routes for your on-premises network (this scenario uses static routing for the VPN tunnels, but you could instead use [BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing))


You provide Oracle this information and in return receive the information your network administrator needs to configure the on-premises router at your end of the VPN.
### Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're a member of the Administrators group, you already have the required access to implement Scenario C. Otherwise, you need access to Networking, and you need the ability to launch instances. See [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
## Setting Up Scenario C 🔗 
Setup is easy in the Console. Alternatively, you can use the Oracle Cloud Infrastructure API, which lets you implement the individual operations yourself. 
**Important** Most of this process involves working with the Console or API (whichever you choose) for a short period to set up the required Networking components. There's also a critical step that requires a network administrator in your organization to take information you receive while setting up the components and use it to configure the on-premises router at your end of the VPN. Therefore you can't complete this process in one short session. Take a break while the network administrator completes the configuration and then confirm communication with your instances over the VPN.
### Using the Console
[Task 1: Set up the VCN and subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
  1. Create the VCN:
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    3. Click **Create Virtual Cloud Network**.
    4. Enter the following:
       * **Name:** A friendly name for the VCN. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
       * **CIDR Block:** One or more non-overlapping CIDR blocks for the VCN. For example: 172.16.0.0/16. You can add or remove CIDR blocks later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
       * **Enable IPv6 Address Assignment:** IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
       * **Use DNS Hostnames in this VCN:** This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select this option you can specify a **DNS Label** for the VCN, or you can let the Console to generate one for you. The dialog box automatically displays the corresponding **DNS Domain Name** for the VCN (`<VCN_DNS_label>.oraclevcn.com`). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
       * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Virtual Cloud Network**.
The VCN is then created and displayed on the **Virtual Cloud Networks** page in the compartment you chose. 
  2. Create an internet gateway for your VCN:
    1. Under **Resources** , click **Internet Gateways**.
    2. Click **Create Internet Gateway**.
    3. Enter the following:
       * **Name:** A friendly name for the internet gateway. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
       * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Internet Gateway**. 
The internet gateway is then created and listed on the page. 
  3. Create a NAT gateway for your VCN:
    1. Under **Resources** , click **NAT Gateways**.
    2. Click **Create NAT Gateway**.
    3. Enter the following:
       * **Name:** A friendly name for the NAT gateway. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
       * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create NAT Gateway**. 
The NAT gateway is then created and listed on the page. 
  4. Create the custom route table for the public subnet (which you create later):
    1. Under **Resources** , click **Route Tables**.
    2. Click **Create Route Table**.
    3. Enter the following:
       * **Name:** A friendly name for the route table (for example, _Public Subnet Route Table_). It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in). 
       * Click **+ Additional Route Rule** and enter the following:
         * **Target Type:** Internet Gateway.
         * **Destination CIDR Block:** 0.0.0.0/0 (which means that all non-intra-VCN traffic that is not already covered by other rules in the route table goes to the target specified in this rule).
         * **Compartment:** Leave as is.
         * **Target:** The internet gateway you created.
         * **Description:** An optional description of the rule.
    4. **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Route Table**. 
The route table is then created and listed on the page.
  5. Create the custom route table for the private subnet (which you create later):
    1. Click **Create Route Table**.
    2. Enter the following:
       * **Name:** A friendly name for the route table (for example, _Private Subnet Route Table_). It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in). 
       * Click **+ Additional Route Rule** and enter the following:
         * **Target Type:** NAT Gateway.
         * **Destination CIDR Block:** 0.0.0.0/0 (which means that all non-intra-VCN traffic that is not already covered by other rules in the route table goes to the target specified in this rule).
         * **Compartment:** Leave as is.
         * **Target:** The NAT gateway you created.
         * **Description:** An optional description of the rule.
    3. **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Route Table**. 
The route table is then created and listed on the page. After you set up Site-to-Site VPN, you update the Private Subnet Route Table so it routes traffic from the private subnet to the on-premises network by way of the DRG.
  6. Update the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) to include rules to allow the types of connections that your instances in the VCN need: 
    1. Under **Resources** , click **Security Lists**.
    2. Click the default security list to view its details. By default, you land on the **Ingress Rules** page. 
    3. Edit each of the existing stateful ingress rules so that the **Source CIDR** is the CIDR for your on-premises network (10.0.0.0/16 in this example) and not 0.0.0.0/0. To edit an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the rule, and then click **Edit**.
    4. If you plan to launch Windows instances, add a rule to enable RDP access:
  7. Create a custom security list for the public subnet:
    1. Return to the **Security Lists** page for the VCN.
    2. Click **Create Security List**.
    3. Enter the following:
       * **Name:** Enter a friendly name for the list (for example, _Public Subnet Security List)_. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in).
    4. Add the following ingress rules:
Example: Ingress HTTP access 
       * **Type:** Ingress
       * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
       * **Source Type:** CIDR
       * **Source CIDR:** 0.0.0.0/0
       * **IP Protocol:** TCP
       * **Source Port Range:** All
       * **Destination Port Range** : 80
       * **Description:** An optional description of the rule.
Example: Ingress HTTPS access 
       * **Type:** Ingress
       * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
       * **Source Type:** CIDR
       * **Source CIDR:** 0.0.0.0/0
       * **IP Protocol:** TCP
       * **Source Port Range:** All
       * **Destination Port Range** : 443
       * **Description:** An optional description of the rule.
    5. Add the following egress rule:
    6. Click **Create Security List**. 
The custom security list for the public subnet is then created and listed on the page.
  8. Create a custom security list for the _private_ subnet:
    1. Click **Create Security List**.
    2. Enter the following:
       * **Name:** Enter a friendly name for the list (for example, _Private Subnet Security List)_. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in).
    3. Add the following ingress rules:
Example: Ingress SQL*Net access from clients in the public subnet 
       * **Type:** Ingress
       * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
       * **Source Type:** CIDR
       * **Source CIDR:** CIDR for the public subnet (172.16.1.0/24 in this example)
       * **IP Protocol:** TCP
       * **Source Port Range:** All
       * **Destination Port Range** : 1521
       * **Description:** An optional description of the rule.
Example: Ingress SQL*Net access from clients in the private subnet 
       * **Type:** Ingress
       * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
       * **Source Type:** CIDR
       * **Source CIDR:** CIDR for the private subnet (172.16.2.0/24 in this example)
       * **IP Protocol:** TCP
       * **Source Port Range:** All
       * **Destination Port Range** : 1521
       * **Description:** An optional description of the rule.
    4. Add the following egress rules:
    5. Click **Create Security List**. 
The custom security list for the private subnet is then created and listed on the page.
  9. Create the subnets in the VCN:
    1. Under **Resources** , click **Subnets**.
    2. Click **Create Subnet**.
    3. Enter the following:
       * **Name:** A friendly name for the regional public subnet (for example, _Regional Private Subnet_). It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Regional or Availability Domain-Specific:** Select **Regional** (recommended), which means the subnet spans all availability domains in the region. Later when you launch an instance, you can create it any availability domain in the region. For more information, see [Overview of VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI.").
       * **CIDR Block:** A single, contiguous CIDR block within the VCN's CIDR block. For example: 172.16.1.0/24. You _cannot_ change this value later. For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
       * **Enable IPv6 Address Assignment:** This option is available only if the VCN is enabled for IPv6. IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
       * **Route Table:** Select the Private Subnet Route Table you created earlier.
       * **Private or****public subnet** : Select **Private Subnet** , which means VNICs in the subnet are not allowed to have public IP addresses. For more information, see [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private).
       * **Use DNS Hostnames in this Subnet:** This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The dialog box automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
       * **DHCP Options:** Select the default set of DHCP options.
       * **Security Lists:** Select two security lists: Both the default security list and the Private Subnet Security List you created earlier.
    4. Click **Create Subnet**. 
The private subnet is then created and displayed on the **Subnets** page.
    5. Repeat the preceding steps a-d to create the _regional public subnet_. Instead use a name such as _Regional Public Subnet_ , select **Public Subnet** instead of **Private Subnet** , use the Public Subnet Route Table, and use both the default security list and Public Subnet Security List you created earlier. 


[Example: Ingress RDP access required for Windows instances](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
  * **Type:** Ingress
  * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
  * **Source Type:** CIDR
  * **Source CIDR:** Your on-premises network (10.0.0.0/16 in this example)
  * **IP Protocol:** TCP
  * **Source Port Range:** All
  * **Destination Port Range** : 3389
  * **Description:** An optional description of the rule.


[Example: Egress SQL*Net access to Oracle databases](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
  * **Type:** Egress
  * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
  * **Destination Type:** CIDR
  * **Destination CIDR:** CIDR for the private subnet (172.16.1.0/24 in this example)
  * **IP Protocol:** TCP
  * **Source Port Range:** All
  * **Destination Port Range** : 1521
  * **Description:** An optional description of the rule.


[Example: Egress SQL*Net access to instances in the private subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
  * **Type:** Egress
  * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
  * **Destination Type:** CIDR
  * **Destination CIDR:** CIDR for the private subnet (172.16.1.0/24 in this example)
  * **IP Protocol:** TCP
  * **Source Port Range:** All
  * **Destination Port Range** : 1521
  * **Description:** An optional description of the rule.


[Task 2: Create instances in separate availability domains](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
You can now create one or more instances in the subnet (see [Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)). The scenario's diagram shows instances in two different availability domains. When you create the instance, you choose the AD, which VCN and subnet to use, and several other characteristics.
For each instance in the public subnet, you must assign the instance a public IP address. Otherwise, the instance isn't available from your on-premises network.
You can't yet reach the instances in the private subnet because there's no gateway connecting the VCN to your on-premises network. The next procedure walks you through setting up Site-to-Site VPN to enable that communication.
[Task 3: Add Site-to-Site VPN to your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
  1. Create a customer-premises equipment object:
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
    2. Click **Create Customer-Premises Equipment**.
    3. Enter the following:
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in). 
       * **Name:** A friendly name for the customer-premises equipment object. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **IP Address:** The IP address of the on-premises router at your end of the VPN (see [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Prerequi)).
    4. Click **Create**.
The CPE object is in the "Provisioning" state for a short period. 
  2. Create a Dynamic Routing Gateway (DRG):
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Click **Create Dynamic Routing Gateway**.
    3. For **Create in Compartment:** Leave the default value (the compartment you're currently working in). 
    4. Enter a friendly name for the DRG. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
    5. Click **Create**.
The DRG is in the "Provisioning" state for a short period. Wait until it is fully provisioned before continuing. 
  3. Attach the DRG to your VCN:
    1. Click the DRG that you created.
    2. Under **Resources** , click **Virtual Cloud Networks**. 
    3. Click **Attach to Virtual Cloud Network**.
    4. Select the VCN. Ignore the section for advanced options, which is only for an advanced routing scenario called _transit routing_ , which is not relevant here.
    5. Click **Attach**.
The attachment is in the "Attaching" state for a short period.
  4. Update the private subnet's route table (which already has one rule for the NAT gateway):
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click your VCN. 
    3. Click **Route Tables** , and then click the Private Subnet Route Table you created earlier. 
    4. Click **Add Route Rule**.
    5. Enter the following:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
       * **Destination CIDR Block:** 0.0.0.0/0 (which means that all non-intra-VCN traffic that is not already covered by other rules in the route table goes to the target specified in this rule).
       * **Description:** An optional description of the rule.
    6. Click **Add Route Rule**. 
The table is updated to route any traffic destined for your on-premises network to the DRG. The original rule for 0.0.0.0/0 routes any remaining traffic leaving the subnet to the NAT gateway.
  5. Create an IPSec Connection:
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
    2. Click **Create IPSec Connection**.
    3. Enter the following:
       * **Create in Compartment:** Leave the default value (the compartment you're currently working in). 
       * **Name:** Enter a friendly name for the IPSec connection. It doesn't have to be unique. Avoid entering confidential information.
       * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
       * **Customer-Premises Equipment:** Select the CPE object you created earlier.
       * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
       * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
       * **Static Route CIDR:** Enter at least one static route CIDR (see [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Prerequi)). If you need to add another, click **Add Static Route**. You can enter up to 10 static routes, and you can [change the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route) later. 
    4. Click **Show Advanced Options** and optionally provide the following items:
       * **CPE IKE Identifier:** Oracle defaults to using the public IP address of the CPE. But if your [CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or [change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id) later.
       * **Tunnel 1** and **Tunnel 2** : Leave as is. Later if you want to use BGP dynamic routing instead of static routing for the VPN tunnels, see [Changing from Static Routing to BGP Dynamic Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp).
       * **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. The connection is in the Provisioning state for a short period.
The displayed tunnel information includes the IP address of the VPN headend and the tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. To view the tunnel's shared secret, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View Shared Secret**. 
    6. Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who configures the on-premises router.
For more information, see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration). You can view this tunnel information here in the Console at any time. 


You have now created all the components required for Site-to-Site VPN. Next, your network administrator must configure the on-premises router before network traffic can flow between your on-premises network and VCN. 
[Task 4: Configure your on-premises router (CPE)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)
These instructions are for the network administrator.
  1. Get the tunnel configuration information that Oracle provided during VPN setup. See [Task 3: Add Site-to-Site VPN to your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#To_add_a_VPN_to_your_cloud_network).
  2. Configure your on-premises router according to the information in [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration).


If compute instances are already in one of the subnets, you can confirm the IPSec connection is up and running by connecting to the instances from your on-premises network. To connect to instances in the public subnet, you must connect to the instance's public IP address. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations:
  * [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn): Always include a DNS label if you want the VCN to use the VCN Resolver (see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network)). 
  * [CreateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/CreateInternetGateway)
  * [CreateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/CreateNatGateway)
  * [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable): Call it to create the Public Subnet Route Table. To enable communication by way of the internet gateway, add a route rule with destination = 0.0.0.0/0, and destination target = the internet gateway you created earlier.
  * [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable): Call it again to create the Private Subnet Route Table. To enable communication by way of the NAT gateway, add a route rule with destination = 0.0.0.0/0, and destination target = the NAT gateway you created earlier.
  * First call [GetSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/GetSecurityList) to get the default security list, and then call [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList):
    * Change the existing stateful ingress rules to use your on-premises network's CIDR as the source CIDR, instead of 0.0.0.0/0.
    * If you plan to launch Windows instances, add this stateful ingress rule: Source type = CIDR, source CIDR = your on-premises network on TCP, source port = all, destination port = 3389 (for RDP).
  * [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList): Call it to create the Public Subnet Security List with these rules:
    * Stateful ingress: Source type = CIDR, source 0.0.0.0/0 on TCP, source port = all, destination port = 80 (HTTP)
    * Stateful ingress: Source type = CIDR, source 0.0.0.0/0 on TCP, source port = all, destination port = 443 (HTTPS)
    * Stateful egress: Destination type = CIDR, destination CIDR blocks of private subnets on TCP, source port = all, destination port = 1521 (for Oracle databases)
  * [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList): Call it again to create the Private Subnet Security List with these rules: 
    * Stateful ingress: Source type = CIDR, source CIDR blocks of public subnets on TCP, source port = all, destination port = 1521 (for Oracle databases)
    * Stateful ingress: Source type = CIDR, source CIDR blocks of private subnets on TCP, source port = all, destination port = 1521 (for Oracle databases)
    * Stateful egress: Destination type = CIDR, destination CIDR blocks of private subnets on TCP, source port = all, destination port = 1521 (for Oracle databases)
  * [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet): Call it to create regional public subnet. Include a DNS label for the subnet if you want the [VCN Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network) to resolve hostnames for VNICs in the subnet. Use the Public Subnet Route Table you created earlier. Use both the default security list and the Public Subnet Security List that you created earlier. Use the default set of DHCP options.
  * [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet): Call it again to create regional private subnet. Include a DNS label for the subnet if you want the [VCN Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network) to resolve hostnames for VNICs in the subnet. Use the Private Subnet Route Table you created earlier. Use both the default security list and the Private Subnet Security List that you created earlier. Use the default set of DHCP options.
  * [CreateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/CreateDrg): Creates a dynamic routing gateway (DRG).
  * [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment): Attaches the DRG to the VCN.
  * [CreateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/CreateCpe): Here you provide the IP address of the router at your end of the VPN (see [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Prerequi)).
  * [CreateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/CreateIPSecConnection): Here you provide the static routes for your on-premises network (see [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Prerequi)). In return, you receive the configuration information your network administrator needs to configure your router. If you need that information later, you can get it with [GetIPSecConnectionDeviceConfig](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig). For more information about the configuration, see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration).
  * First call [GetRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/GetRouteTable) to get the Private Subnet Route Table. Then call [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) to add a route rule with destination = the on-premises network CIDR (10.0.0.0/16 in this example), and destination target = the DRG you created earlier.
  * [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance): Launch at least one instance in each subnet. By default, the instances in the public subnets are assigned public IP addresses. For more information, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).


You can now communicate from your on-premises network with the instances in the public subnet over the internet gateway. 
**Important** Although you can launch instances into the private subnets, you can't communicate with them from your on-premises network until your network administrator configures your on-premises router (see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)). After that, your IPSec connection is up and running. You can confirm its status by using [GetIPSecConnectionDeviceStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig). You can also confirm the IPSec connection is up by connecting to the instances from your on-premises network.
Was this article helpful?
YesNo

