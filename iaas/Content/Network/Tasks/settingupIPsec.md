Updated 2025-02-12
# Setting Up Site-to-Site VPN
This topic gives instructions for constructing a Site-to-Site VPN IPSec connection from an on-premises network to a VCN. For general information about Site-to-Site VPN, see [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top).
## Before You Get Started 🔗 
To prepare, do these things first:
  * Read this section: [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing)
  * Answer these questions:
Question | Answer  
---|---  
What is the VCN's CIDR?  
What is the public IP address of the CPE device? If you have several devices for redundancy, get the IP address for each.  **Note:** If the CPE device is behind a NAT device, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components) and also [Requirements and Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#reqs).  
Do you want to use port address translation (PAT) between each CPE device and the VCN?  
What type of routing do you plan to use? If you want BGP dynamic routing, list the BGP session IP addresses to use and the ASN of the on-premises network. The IP addresses must be part of Site-to-Site VPN's encryption domain.  If you want static routing, what are the static routes for the on-premises network? See [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).  Do you plan to use policy based routing or multiple encryption domains? See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel).  
Do you want to provide each tunnel's shared secret or let Oracle assign them? See [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components).  
  * Draw a diagram of the network layout (for examples, see the first task in [Example: Setting Up a Proof of Concept Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_poc)). Think about which parts of the on-premises network need to communicate with the VCN, and the reverse. Map out the [routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that you need for the VCN.


**Tip** If you have an existing Site-to-Site VPN that uses static routing, you can [change the tunnels to instead use BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp). 
The following link local IP ranges aren't valid for use with Site-to-Site VPN inside tunnel interfaces:
  * 169.254.10.0 to 169.254.19.255
  * 169.254.100.0 to 169.254.109.255
  * 169.254.192.0 to 169.254.201.255


## Overall Process 🔗 
Here's the overall process for setting up Site-to-Site VPN:
  1. **Complete the tasks listed in[Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before).**
  2. **Set up Site-to-Site VPN components**(instructions in [Example: Setting Up a Proof of Concept Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_poc)): 
    1. Create a VCN.
    2. Create a DRG.
    3. Attach the DRG to the VCN.
    4. Create a route table and route rule for the DRG.
    5. Create a security list and required rules.
    6. Create a subnet in the VCN.
    7. Create a CPE object and provide the CPE device's public IP address.
    8. Create an IPSec connection to the CPE object and provide required routing information.
  3. **Use the CPE Configuration Helper:** A network engineer must configure the CPE device with information that Oracle provides during the previous steps. The CPE Configuration Helper generates the information for the network engineer. For more information, see [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) and also [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration). 
  4. **Have a network engineer configure the CPE device.**
  5. **Validate connectivity.**


If you plan to set up redundant connections, see the [Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf).
## Example: Setting Up a Proof of Concept Site-to-Site VPN 🔗 
**Tip** Oracle offers a quickstart workflow to make it easier to set up Site-to-Site VPN. For more information, see [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart).
This example scenario shows how to set up a Site-to-Site VPN with a layout that you might use for a proof of concept (POC). It follows tasks 1 and 2 in [Overall Process](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Overall) and shows each component in the layout being created. For more complex layouts, see [Example Layout with Multiple Geographic Areas](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_multi_geo) or [Example Layout with PAT](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_pat).
[Task 1: Gather information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
Question | Answer  
---|---  
What is the VCN's CIDR? | 172.16.0.0/16  
What is the public IP address of the CPE device? If you have several devices for redundancy, get the IP address for each.  **Note:** If the CPE device is behind a NAT device, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components) and also [Requirements and Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#reqs). | 142.34.145.37  
Will you be doing port address translation (PAT) between each CPE device and the VCN? | No  
What type of routing do you plan to use? There are three mutually exclusive choices: If you plan to use BGP dynamic routing, list the BGP session IP addresses to use and the ASN of the on-premises network.  If you plan to use static routing, list the static routes for the on-premises network. See [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).  If you plan to use policy-based routing or require multiple encryption domains, list the IPv4 CIDR or IPv6 prefix blocks used on each end of the connection. See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel). |  **BGP dynamic routing example:** Tunnel 1:
  * BGP Inside tunnel interface - CPE: 10.0.0.16/31
  * BGP Inside tunnel interface - Oracle: 10.0.0.17/31

Tunnel 2:
  * BGP Inside tunnel interface - CPE: 10.0.0.18/31
  * BGP Inside tunnel interface - Oracle: 10.0.0.19/31

Network ASN: 12345 **Static routing example:** Use 10.0.0.0/16 for the static route for a POC. **Policy-based routing example:** Use ??? for a simple POC.  
Do you want to provide each tunnel's shared secret or let Oracle assign them? See [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components). | Let Oracle assign.  
Here's an example diagram for task 1 that uses BGP dynamic routing: 
[![This image shows a basic VPN layout when using BGP dynamic routing.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_bgp.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_bgp.svg)
Callout 1: Default subnet route table Destination CIDR | Route target  
---|---  
10.0.0.0/16 | DRG  
Callout 2: security list Destination CIDR | Permission  
---|---  
10.0.0.0/16 | Allowed  
Callouts 3 to 6 Callout | Function | IP   
---|---|---  
3 | CPE public IP address | 142.34.145.37  
4a | Tunnel 1 BGP: Inside Tunnel Interface |  CPE - 10.0.0.16/31 Oracle - 10.0.0.17/31  
4b | Tunnel 2 BGP: Inside Tunnel Interface |  CPE - 10.0.0.18/31 Oracle - 10.0.0.19/31  
5 |  Tunnel 1 Oracle VPN IP Address:  | 129.213.240.50  
6 |  Tunnel 2 Oracle VPN IP Address:  | 129.213.240.53  
Here's an example diagram for task 1 that uses static routing: 
[![This image shows a basic VPN layout when using static routing.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_static.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_static.svg)
Callout 1: Default subnet route table Destination CIDR | Route target  
---|---  
10.0.0.0/16 | DRG  
Callout 2: security list Destination CIDR | Permission  
---|---  
10.0.0.0/16 | Allowed  
Callouts 3 to 6 Callout | Function | IP   
---|---|---  
3 | CPE public IP address | 142.34.145.37  
4 | Static route for IPSec Connection | 10.0.0.0/16  
5 |  Tunnel 1 Oracle VPN IP Address:  | 129.213.240.50  
6 |  Tunnel 2 Oracle VPN IP Address:  | 129.213.240.53  
[Task 2a: Create the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
If you already have a VCN, skip to the next task.
**Tip** When you use the Console to create a VCN, you can create only the VCN, or you can create the VCN with several related resources. This task creates only the VCN, and the next tasks create the other required resources. 
[![This image shows creation of the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_vcn.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_vcn.svg)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
  3. Select **Create Virtual Cloud Network**.
  4. Enter the following values:
     * **Create in Compartment:** Leave as is. 
     * **Name:** A descriptive name for the cloud network. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **CIDR Block:** A single, contiguous CIDR block for the cloud network (for example, 172.16.0.0/16). You _can't_ change this value later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, use a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **Enable IPv6 Address Assignment:** This option is available only if the VCN is enabled for IPv6. IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
  5. You can provide values for the rest of the options, or you can ignore them:
     * **DNS Resolution:** This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select this option you can specify a **DNS Label** for the VCN, or you can let the Console to generate one for you. The dialog box automatically displays the corresponding **DNS Domain Name** for the VCN (`<VCN_DNS_label>.oraclevcn.com`). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  6. Select **Create Virtual Cloud Network**.


The VCN is created and displayed on the page. Ensure that it's done being provisioned before continuing.
[Task 2b: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
[![This image shows creation of the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_drg.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_drg.svg)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Select **Create Dynamic Routing Gateway**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** A descriptive name for the DRG. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  4. Select **Create Dynamic Routing Gateway**.


The DRG is created and displayed on the page. Ensure that it's done being provisioned before continuing.
**Tip** You could also use this DRG as the gateway for [Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."), which is another way to connect an on-premises network to a VCN.
[Task 2c: Attach the DRG to the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
[![This image shows attachment of the DRG to the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_attach_drg.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_attach_drg.svg)
  1. Select the name of the DRG you created.
  2. Under **Resources** , select **Virtual Cloud Networks**. 
  3. Select **Attach to Virtual Cloud Network**.
  4. Select the VCN. Ignore the section for advanced options, which is only for an advanced routing scenario called transit routing, which is not relevant here.
  5. Select **Attach**.


The attachment is in the Attaching state for a short period before it's ready.
[Task 2d: Create a route table and route rule for the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
Although the VCN comes with a default route table (without any rules), in this task you create a custom route table with a route rule for the DRG. In this example, the on-premises network is 10.0.0.0/16. You create a route rule that takes any traffic destined for 10.0.0.0/16 and routes it to the DRG. When you create a subnet in task 2f, you associate this custom route table with the subnet.
**Tip** If you already have an existing VCN with a subnet, you don't need to create a route table or subnet. Instead you can update the existing subnet's route table to include the route rule for the DRG.
[![This image shows creation of the route table and route rule for the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_routing.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_routing.svg)
Callout 1: VCN Route Table MyExampleRouteTable Destination CIDR | Route Table  
---|---  
10.0.0.0/16 | DRG  
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Select the VCN.
  3. Select **Route Tables** to see the VCN's route tables.
  4. Select **Create Route Table**.
  5. Enter the following values:
     * **Name:** A descriptive name for the route table (for example, MyExampleRouteTable). The name doesn't have to be unique, and it can't be changed later in the Console (but you can change it in the API). Avoid entering confidential information.
     * **Create in compartment:** Leave as is.
     * Select **+ Additional Route Rule** , and enter the following:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
       * **Destination CIDR Block:** The CIDR for the on-premises network (10.0.0.0/16 in this example). 
       * **Description:** An optional description of the rule.
     * **Tags:** Leave the tag information as is.
  6. Select **Create Route Table**.


The route table is created and displayed on the page. However, the route table doesn't do anything unless you associate it with a subnet during subnet creation (see task 2f).
[Task 2e: Create a security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
By default, incoming traffic to the instances in a VCN is set to DENY on all ports and all protocols. In this task, you set up two ingress rules and one egress rule to allow basic required network traffic. A VCN comes with a default security list with a set of default rules. However, in this task you create a separate security list with a more restrictive set of rules focused on traffic with an on-premises network. When you create a subnet in task 2f, you associate this security list with the subnet.
**Tip** Security lists are one way to control traffic in and out of the VCN's resources. You can also use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)
[![This image shows creation of the security list](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_security_list.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_security_list.svg)
Callout 1: VCN Route Table MyExampleRouteTable Destination CIDR | Route Table  
---|---  
10.0.0.0/16 | DRG  
Callout 2: Security List MyExampleSecurityList Ingress/Egress  | CIDR | Protocol: Port  
---|---|---  
Ingress | 10.0.0.0/16 | TCP: 22  
Ingress | 10.0.0.0/16 | ICMP: All  
Egress | 10.0.0.0/16 | TCP: All  
**Important** In the following procedure, ensure that the on-premises CIDR that you specify in the security list rules is the same (or smaller) than the CIDR that you specified in the route rule in the preceding task. Otherwise, traffic is blocked by the security lists.
  1. While still viewing the VCN, select **Security Lists** on the left side of the page.
  2. Select **Create Security List**.
  3. Enter the following values:
     * **Name:** A descriptive name for the security list. The name doesn't have to be unique, and it can't be changed later in the Console (but you can change it in the API). Avoid entering confidential information.
     * **Create in compartment:** Leave as is.
  4. In the **Allow Rules for Ingress** section, select **Add Ingress Rule** and enter the following values for the ingress rule, which allows incoming SSH on TCP port 22 from an on-premises network:
     * **Source Type:** CIDR
     * **Source CIDR:** The CIDR for an on-premises network (10.0.0.0/16 in this example) 
     * **IP Protocol:** TCP.
     * **Source Port Range:** Leave as is (the default All).
     * **Destination Port Range:** 22 (for SSH traffic).
     * **Description:** An optional description of the rule.
  5. In the **Allow Rules for Egress** section, select **Add Egress Rule** enter the following values for the egress rule, which allows outgoing TCP traffic on all ports to an on-premises network:
     * **Destination Type:** CIDR
     * **Destination CIDR:** The CIDR for an on-premises network (10.0.0.0/16 in this example). 
     * **IP Protocol:** TCP.
     * **Source Port Range:** Leave as is (the default All).
     * **Destination Port Range:** Leave as is (the default All).
     * **Description:** An optional description of the rule.
  6. Leave the tag information as is.
  7. Select **Create Security List**.


The security list is created and displayed on the page. However, the security list doesn't do anything unless you associate it with a subnet during subnet creation (see task 2f).
[Task 2f: Create a subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
In this task, you create a subnet in the VCN. Typically a subnet has a CIDR block smaller than the VCN's CIDR. Any instances that you create in this subnet have access to an on-premises network. We recommend using [regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI."). Here you create a regional private subnet.
[![This image shows creation of the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_subnet.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_subnet.svg)
Callout 1: VCN Route Table MyExampleRouteTable Destination CIDR | Route Table  
---|---  
10.0.0.0/16 | DRG  
Callout 2: Security List MyExampleSecurityList Ingress/Egress  | CIDR | Protocol: Port  
---|---|---  
Ingress | 10.0.0.0/16 | TCP: 22  
Ingress | 10.0.0.0/16 | ICMP: All  
Egress | 10.0.0.0/16 | TCP: All  
  1. While still viewing the VCN, select **Subnets** on the left side of the page.
  2. Select **Create Subnet**.
  3. Enter the following values:
     * **Name:** A descriptive name for the subnet. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Regional or AD-specific subnet:** Select the radio button for **Regional**. We recommend using [regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI."). 
     * **CIDR Block:** A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). It must be within the cloud network's CIDR block and can't overlap with any other subnets. You _can't_ change this value later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, use a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **Enable IPv6 Address Assignment:** This option is available only if the VCN is already enabled for IPv6. IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
     * **Route Table:** The route table that you created earlier.
     * **Private Subnet** : Select this option. For more information, see [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private).
     * **Use DNS Hostnames in this Subnet:** Leave as is (selected). 
     * **DHCP Options:** The set of DHCP options to associate with the subnet. Select the default set of DHCP options for the VCN.
     * **Security Lists:** The security list that you created earlier.
     * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  4. Select **Create Subnet**.


The subnet is created and displayed on the page. The basic VCN in this example is now set up, and you're ready to create the remaining components for Site-to-Site VPN.
[Task 2g: Create a CPE object and provide the CPE device's public IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
In this task, you create the CPE object, which is a virtual representation of an actual CPE device. The CPE object exists in a compartment in a tenancy. When you configure Site-to-Site VPN you need to change the configuration of the actual edge device for the on-premises network to match the configuration of the CPE object. 
[![This image shows creation of the CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_cpe.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_cpe.svg)
Callout 1: VCN Route Table MyExampleRouteTable Destination CIDR | Route Table  
---|---  
10.0.0.0/16 | DRG  
Callout 2: Security List MyExampleSecurityList Ingress/Egress  | CIDR | Protocol: Port  
---|---|---  
Ingress | 10.0.0.0/16 | TCP: 22  
Ingress | 10.0.0.0/16 | ICMP: All  
Egress | 10.0.0.0/16 | TCP: All  
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Select **Create Customer-Premises Equipment**.
  3. Enter the following values:
     * **Name:** A descriptive name for the CPE object. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **IP Address:** The public IP address of the actual CPE/edge device at the on-premises end of the VPN (see the list of information to gather in [Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)).
     * **Enable IPSec over FastConnect:** (Optional) Check this option only when configuring the [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) feature. When this option is enabled, the label of the next field changes to **IP Address** because the IP address used as the CPE IKE identifier can be either public or private. Checking this option signals to Oracle that the CPE IP address isn't reachable over the internet and is reachable over private peering only.
     * **Public IP Address:** The public IP address of the actual CPE/edge device at the on-premises end of the VPN (see the list of information to gather in [Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)).
     * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  4. Select **Create CPE**.


The CPE object is created and displayed on the page.
[Task 2h: Create an IPSec connection to the CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
In this task, you create the IPSec tunnels and configure the type of routing for them (BGP dynamic routing or static routing).
**Tip** If you have an existing Site-to-Site VPN that uses static routing, you can [change the tunnels to instead use BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp). 
[For BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
**Note** Oracle recommends that you use BGP route-based IPSec connections for IPSec over FastConnect.
In this example, you configure both tunnels to use BGP dynamic routing.
[![This image shows a basic VPN layout when using BGP dynamic routing.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_bgp.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_bgp.svg)
Callout 1: Default subnet route table Destination CIDR | Route target  
---|---  
10.0.0.0/16 | DRG  
Callout 2: security list Destination CIDR | Permission  
---|---  
10.0.0.0/16 | Allowed  
Callouts 3 to 6 Callout | Function | IP   
---|---|---  
3 | CPE public IP address | 142.34.145.37  
4a | Tunnel 1 BGP: Inside Tunnel Interface |  CPE - 10.0.0.16/31 Oracle - 10.0.0.17/31  
4b | Tunnel 2 BGP: Inside Tunnel Interface |  CPE - 10.0.0.18/31 Oracle - 10.0.0.19/31  
5 |  Tunnel 1 Oracle VPN IP Address:  | 129.213.240.50  
6 |  Tunnel 2 Oracle VPN IP Address:  | 129.213.240.53  
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Name:** Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier. If you are configuring[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec), the CPE you choose must have a label confirming that IPSec over FastConnect is enabled for that CPE. BGP routing is preferred for connections that use IPSec over FastConnect. If necessary, select the checkbox to indicate that the CPE is behind a NAT device. If the checkbox is selected, provide the following information:
       * **CPE IKE Identifier Type:** Select the type of identifier that internet key exchange (IKE) uses to identify the CPE device. Either an FQDN or an IPv4 address can be an identifier.Oracle defaults to using the public IP address of the CPE. If your [CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or [change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id) later.
       * **CPE IKE Identifier:** Enter the information that IKE uses to identify the CPE device. 
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Routes to your on-premises Network:** Leave empty because this IPSec connection uses BGP dynamic routing. You configure the two tunnels to use BGP in subsequent steps.
  4. For **Tunnel 1** (required):
     * **Name:** Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret** (optional): By default, Oracle provides the shared secret for the tunnel. If you want to provide it instead, select this checkbox and enter the shared secret. You can [change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
     * **IKE Version:** The Internet Key Exchange (IKE) version to use for this tunnel. Only select [IKEv2](https://tools.ietf.org/html/rfc7296) if your CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
     * **Routing Type:** Select **BGP Dynamic Routing**.
     * If your selected CPE supports [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec), the following settings are required:
       * **Oracle tunnel headend IP:** Enter the IP address of the Oracle IPSec tunnel endpoint (the VPN headend). Oracle will advertise the VPN IP as a /32 host route via the FastConnect BGP session. If there is any address overlap with a VCN route this will take precedence due to longest prefix match.
       * **Associated virtual circuit:** Select a virtual circuit that was enabled for IPSec over FastConnect when it was created. The tunnel will be mapped to the chosen virtual circuit and the defined headend IP will only be reachable from on-premises via the associated virtual circuit.
       * **DRG route table:** Choose or create a DRG route table. To prevent any issues with recursive routing, the virtual circuit attachment and the IPSec tunnel attachment used for IPsec over FC must use different DRG route tables.
     * **BGP ASN:** Enter your network's ASN.
     * **IPv4 Inside Tunnel Interface - CPE:** Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the CPE end of the tunnel. For example: 10.0.0.16/31. The IP address must be part of Site-to-Site VPN's encryption domain.
     * **IPv4 Inside Tunnel Interface - Oracle:** Enter the BGP IPv4 address with subnet mask (either /30 or /31) for the Oracle end of the tunnel. For example: 10.0.0.17/31. The IP address must be part of Site-to-Site VPN's encryption domain.
     * If you plan to use both IPv6 and IPv4, click **Enable IPv6** and enter the following details:
       * **IPv6 Inside Tunnel Interface - CPE:** Enter the BGP IPv6 address with subnet mask (/126) for the CPE end of the tunnel. For example: 2001:db2::6/126. The IP address must be part of Site-to-Site VPN's encryption domain.
       * **IPv6 Inside Tunnel Interface - Oracle:** Enter the BGP IP address with subnet mask (/126) for the Oracle end of the tunnel. For example: 2001:db2::7/126. The IP address must be part of Site-to-Site VPN's encryption domain.
       * If you click **Show Advanced Options** you can change the following settings for Tunnel 1: 
         * **Oracle Initiation:** This setting indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel. The default is **Initiator or Responder**. You can also choose to set the Oracle end to be a responder only which would require the CPE device to initiate the IPSec tunnel. Oracle recommends leaving this option at the default setting.
         * **NAT-T Enabled:** This setting indicates whether the CPE device is behind a NAT device. The default is **Auto**. The other options are **Disabled** and **Enabled**. Oracle recommends leaving this option at the default setting.
         * **Enable Dead Peer Detection Timeout:** Clicking this option allows you to periodically check the stability of the connection to the CPE, and detect that the CPE has gone down. If you select this option you can also select the longest interval between CPE device health messages before the IPSec connection indicates that it has lost contact with the CPE. The default is 20 seconds. Oracle recommends leaving this option at the default setting.
       * If you expand the **Phase One (ISAKMP) Configuration** section and click **Set custom options** , you can set the following optional settings (you must select one of each option): 
         * **Custom Encryption Algorithms:** You can choose from the options provided in the pull-down menu. 
         * **Custom Authentication Algorithms:** You can choose from the options provided in the pull-down menu. 
         * **Diffie-Hellman Groups:** You can choose from the options provided in the pull-down menu. 
If the **Set custom configurations** checkbox is not selected, the default settings are proposed. 
To understand these options in more detail including the default proposals, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
       * **IKE Session Key Lifetime in Seconds:** The default is **28800** which is equivalent to 8 hours. 
       * If you expand the **Phase Two (IPSec) Configuration** options and click **Set custom options** , you can set the following optional settings for Tunnel 1 (you must select an encryption algorithm): 
         * **Custom Encryption Algorithms:** You can choose from the options provided in the pull-down menu. If you select an AES-CBC encryption algorithm, you must also select an authentication algorithm.
         * **Custom Authentication Algorithms:** You can choose from the options provided in the pull-down menu. The encryption algorithm you chose might have built-in authentication, in which case there is no selectable option.
If the **Set custom configurations** checkbox is not selected, the default settings are proposed. 
For all Phase Two options, if you select a single option that option overrides the default set and be the only option proposed to the CPE device.
       * **IPSec Session Key Lifetime in Seconds:** The default is **3600** which is equivalent to 1 hour. 
       * **Enable Perfect Forward Secrecy:** By default, this option is on. It allows you to choose the **Perfect Forward Secrecy Diffie-Hellman Group**. You can choose from the options provided in the pull-down menu. If you don't make a selection, **GROUP5** is proposed. 
  5. On the **Tunnel 2** tab you can use the same options described for Tunnel 1. You can also choose different options or choose to leave the tunnel unconfigured because your CPE device only supports a single tunnel.
  6. You can click **Show Tagging Options** to add tags for the IPSec connection now, or add them later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  7. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. It is in the Provisioning state for a short period.
The displayed tunnel information includes:
     * The Oracle VPN IPv4 or IPv6 address (for the Oracle VPN headend).
     * The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. Your network engineer must configure your CPE device before the tunnel or tunnels can be established.
     * The tunnel's BGP status. At this point, the status is Down. Your network engineer must configure your CPE device.
To view the tunnel's shared secret, click the tunnel to view its details, and then click **Show** next to **Shared Secret**. 
You can also click the **Phase Details** tab to see the Phase One (ISAKMP) and Phase Two (IPSec) details for the tunnel.
  8. Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who configures your CPE device.
You can view this tunnel information here in the Console at any time. 


You have now created all the components required for Site-to-Site VPN. Next, your network engineer must configure your CPE device before network traffic can flow between your on-premises network and VCN.
[For static routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
**Note** Oracle recommends that you use BGP route-based IPSec connections for IPSec over FastConnect.
[![This image shows creation of the IPSec connection with static routing.Click to enlarge](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_ipsec_static.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_ipsec_static.svg)
Callout 1: VCN Route Table MyExampleRouteTable Destination CIDR | Route Table  
---|---  
10.0.0.0/16 | DRG  
Callout 2: Security List MyExampleSecurityList Ingress/Egress  | CIDR | Protocol: Port  
---|---|---  
Ingress | 10.0.0.0/16 | TCP: 22  
Ingress | 10.0.0.0/16 | ICMP: All  
Egress | 10.0.0.0/16 | TCP: All  
Callout 3: IPSec Connection details with Static Route 10.0.0.0/16 Tunnel | Oracle Side IP Address | On-premises Side IP Address  
---|---|---  
Tunnel 1 | 10.0.0.17/31 |  10.0.0.16/31  
Tunnel 2 | 10.0.0.19/31 |  10.0.0.18/31  
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier. If you are configuring[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec), the CPE you choose must have a label confirming that IPSec over FastConnect is enabled for that CPE. IPSec over FastConnect is available for connections that use static routing, but is not recommended. 
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Static Route CIDR:** Enter at least one static route CIDR (see the list of information to gather in [Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)). For this example, enter 10.0.0.0/16. You can enter up to 10 static routes, and you can [change the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route) later. 
  4. Click **Show Advanced Options**.
  5. On the **CPE IKE Identifier** tab (optional): Oracle defaults to using the public IP address of the CPE. If your [CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or [change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id) later.
  6. On the **Tunnel 1** tab (optional): 
     * **Tunnel Name:** Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret** (optional): By default, Oracle provides the shared secret for the tunnel. If you want to provide it instead, select this checkbox and enter the shared secret. You can [change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
     * **IKE Version:** The Internet Key Exchange (IKE) version to use for this tunnel. Only select [IKEv2](https://tools.ietf.org/html/rfc7296) if your CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
     * **Routing Type:** Leave the radio button for **Static Routing** selected.
     * **Inside Tunnel Interface - CPE** (optional): You can provide an IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.16/31. The IP address must be part of Site-to-Site VPN's encryption domain.
     * **Inside Tunnel Interface - Oracle**(optional): You can provide an IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.17/31. The IP address must be part of Site-to-Site VPN's encryption domain.
  7. On the **Tunnel 2** tab (optional): 
     * **Tunnel Name:** Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret** (optional): By default, Oracle provides the shared secret for the tunnel. If you want to provide it instead, select this checkbox and enter the shared secret. You can [change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
     * **IKE Version:** The Internet Key Exchange (IKE) version to use for this tunnel. Only select [IKEv2](https://tools.ietf.org/html/rfc7296) if your CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
     * **Routing Type:** Leave the radio button for **Static Routing** selected.
     * **Inside Tunnel Interface - CPE** (optional): You can provide an IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel for the purposes of tunnel troubleshooting or monitoring. Use a different IP address than for tunnel 1. For example: 10.0.0.18/31. The IP address must be part of Site-to-Site VPN's encryption domain.
     * **Inside Tunnel Interface - Oracle** (optional): You can provide an IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel for the purposes of tunnel troubleshooting or monitoring. Use a different IP address than for tunnel 1. For example: 10.0.0.19/31. The IP address must be part of Site-to-Site VPN's encryption domain.
  8. **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  9. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. It will be in the Provisioning state for a short period.
The displayed tunnel information includes: 
     * The Oracle VPN IP address (for the Oracle VPN headend).
     * The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. Your network engineer still must configure your CPE device.
To view the tunnel's shared secret, click the tunnel to view its details, and then click **Show** next to **Shared Secret**. 
  10. Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location so you can deliver it to the network engineer who will configure the CPE device.
You can view this tunnel information here in the Console at any time. 


You have now created all the components required for Site-to-Site VPN. Next, your network engineer must configure the CPE device before network traffic can flow between your on-premises network and VCN.
For more information, see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration).
[For policy-based routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
**Note** Oracle recommends that you use BGP route-based IPSec connections for IPSec over FastConnect.
**Note** The policy-based routing option is not available in all ADs, and may require creating a new IPSec tunnel.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier. If you are configuring[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec), the CPE you choose must have a label confirming that IPSec over FastConnect is enabled for that CPE. IPSec over FastConnect is available for connections that use policy-based routing, but is not recommended. 
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Static Route CIDR:** Enter at least one static route CIDR (see the list of information to gather in [Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before)). For this example, enter 10.0.0.0/16. You can enter up to 10 static routes, and you can [change the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route) later. 
  4. Click **Show Advanced Options**.
  5. On the **CPE IKE Identifier** tab (optional): Oracle defaults to using the public IP address of the CPE. If your [CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or [change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id) later.
  6. On the **Tunnel 1** tab (optional): 
     * **Tunnel Name:** Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret** (optional): By default, Oracle provides the shared secret for the tunnel. If you want to provide it instead, select this checkbox and enter the shared secret. You can [change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
     * **IKE Version:** The Internet Key Exchange (IKE) version to use for this tunnel. Only select [IKEv2](https://tools.ietf.org/html/rfc7296) if your CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
     * **Routing Type:** Select the radio button for **Policy-based** routing.
     * **On-premises:** You can provide multiple IPv4 CIDR or IPv6 prefix blocks used by resources in your on-premises network, with routing determined by the CPE device policies. 
**Note** See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for limitations on how many IPv4 CIDR or IPv6 prefix blocks can be used. 
     * **Oracle Cloud:** You can provide multiple IPv4 CIDR or IPv6 prefix blocks used by resources in your VCN. 
**Note** See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for limitations on how many IPv4 CIDR or IPv6 prefix blocks can be used. 
     * **Inside Tunnel Interface - CPE** (optional): You can provide an IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.16/31. The IP address must be part of one of Site-to-Site VPN's encryption domains. 
     * **Inside Tunnel Interface - Oracle**(optional): You can provide an IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.17/31. The IP address must be part of one of Site-to-Site VPN's encryption domains.
  7. On the **Tunnel 2** tab (optional): 
     * **Tunnel Name:** Enter a descriptive name for the tunnel. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret** (optional): By default, Oracle provides the shared secret for the tunnel. If you want to provide it instead, select this checkbox and enter the shared secret. You can [change the shared secret later](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
     * **IKE Version:** The Internet Key Exchange (IKE) version to use for this tunnel. Only select [IKEv2](https://tools.ietf.org/html/rfc7296) if your CPE supports it. You must also then configure the CPE to use only IKEv2 for this tunnel.
     * **Routing Type:** Select the radio button for **Policy-based** routing.
     * **On-premises:** You can provide multiple IPv4 CIDR or IPv6 prefix blocks used by resources in your on-premises network, with routing determined by the CPE device policies. 
**Note** See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for limitations. 
     * **Oracle Cloud:** You can provide multiple IPv4 CIDR or IPv6 prefix blocks used by resources in your VCN. 
**Note** See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for limitations. 
     * **Inside Tunnel Interface - CPE** (optional): You can provide an IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.16/31. The IP address must be part of one of Site-to-Site VPN's encryption domains.
     * **Inside Tunnel Interface - Oracle**(optional): You can provide an IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel for the purposes of tunnel troubleshooting or monitoring. For example: 10.0.0.17/31. The IP address must be part of one of Site-to-Site VPN's encryption domains.
  8. **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  9. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. It will be in the Provisioning state for a short period.
The displayed tunnel information includes: 
     * The Oracle VPN IP address (for the Oracle VPN headend).
     * The tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. Your network engineer still must configure your CPE device.
To view the tunnel's shared secret, click the tunnel to view its details, and then click **Show** next to **Shared Secret**. 
  10. Copy the Oracle VPN IP address and shared secret for each of the tunnels to an email or other location, then deliver it to the network engineer who configures the CPE device.
You can view this tunnel information here in the Console at any time. 


You have now created all the components required for Site-to-Site VPN. Next, your network engineer must configure the CPE device before network traffic can flow between your on-premises network and VCN.
For more information, see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration).
[Task 3: Use the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
Use the CPE Configuration Helper to generate configuration content that the network engineer can use to configure the CPE.
The content includes these items:
  * For each IPSec tunnel, the Oracle VPN IP address and shared secret.
  * The supported IPSec parameter values.
  * Information about the VCN.
  * CPE-specific configuration information.


For more information, see [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper).
[Task 4: Have the network engineer configure the CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
Provide the network engineer with the following items:
  * The content generated by the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper).
  * The [general IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) that Oracle supports.


**Important** Be sure to have the network engineer configure a CPE device to support both of the tunnels in case one fails or Oracle takes one down for maintenance. If you're using BGP, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing). 
[Task 5: Validate connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
After the network engineer configures the CPE device, you can confirm that the tunnel's IPSec status is Up and green. Next, you can create a Linux instance in the subnet in a VCN. Then use SSH to connect to the instance's private IP address from a host in the on-premises network. For more information, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). 
## Example Layout with Multiple Geographic Areas 🔗 
The following diagram shows a different example with the following configuration:
  * Two networks in separate geographical areas that each connect to a VCN
  * A single CPE device in each area
  * Two IPSec VPNs (one for each CPE device)


Be aware that each Site-to-Site VPN has two routes associated with it: one for the particular geographical area's subnet, and a default 0.0.0.0/0 route. Oracle learns about the available routes for each tunnel either through BGP (if the tunnels use BGP), or because you set them as static routes for the IPSec connection (if the tunnels use static routing).
[![This image shows a layout with two geographical areas and two routers](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_multiple_geo.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_multiple_geo.svg)
Callout 1: Site-to-Site VPN 1 route table Destination CIDR | Route target  
---|---  
10.20.0.0/16 | DRG  
0.0.0.0/0 | DRG  
Callout 2: Site-to-Site VPN 2 route table Destination CIDR | Route target  
---|---  
10.40.0.0/16 | DRG  
0.0.0.0/0 | DRG  
Following are some examples of situations in which the 0.0.0.0/0 route can provide flexibility:
  * Assume that the CPE 1 device goes down (see the next diagram). If Subnet 1 and Subnet 2 can communicate with each other, the VCN could still reach the systems in Subnet 1 because of the 0.0.0.0/0 route that goes to CPE 2. 
[![This image shows a layout where one of the CPE routers goes down](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_router_issue.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_router_issue.svg)
  * If an organization adds a new geographical area with Subnet 3 and initially connects it to Subnet 2 (see the next diagram). If you added a route rule to the VCN's route table for Subnet 3, the VCN could reach systems in Subnet 3 because of the 0.0.0.0/0 route that goes to CPE 2. 
[![This image shows a layout with a new subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_new_geo.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_new_geo.svg)
Callout 1: VCN route table Destination CIDR | Route target  
---|---  
10.20.0.0/16 | DRG  
10.40.0.0/16 | DRG  
10.60.0.0/16 | DRG  


## Example Layout with PAT 🔗 
The following diagram shows an example with this configuration:
  * Two networks in separate geographical areas that each connect to a VCN
  * Redundant CPE devices (two in each geographical area)
  * Four IPSec VPNs (one for each CPE device)
  * Port address translation (PAT) for each CPE device


For each of the four connections, the route that Oracle needs to know about is the PAT IP address for the specific CPE device. Oracle learns about the PAT IP address route for each tunnel either through BGP (if the tunnels use BGP), or because you set the relevant address as a static route for the IPSec connection (if the tunnels use static routing).
When you set up the route rules for the VCN, you specify a rule for each PAT IP address (or an aggregate CIDR that covers them all) with the DRG as the rule's target.
[![This image shows a scenario with several IPSec VPNs, routers, and PAT](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_pat.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_example_pat.svg)
Callout 1: VCN route table Destination CIDR | Route target  
---|---  
PAT IP 1 | DRG  
PAT IP 2 | DRG  
PAT IP 3 | DRG  
PAT IP 4 | DRG   
## What's Next? 🔗 
See these related topics and procedures:
  * [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart)
  * [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)
  * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
  * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
  * [Changing from Static Routing to BGP Dynamic Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp)
  * [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect)
  * [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
  * [Using the API for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Using_the_API_for_VPN_Connect)
  * [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics)
  * [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting)


Was this article helpful?
YesNo

