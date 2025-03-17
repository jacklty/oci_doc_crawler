Updated 2025-02-12
# Site-to-Site VPN Wizard
The Site-to-Site VPN wizard is the quickest way to set up a site-to-site VPN between your on-premises network and your **virtual cloud network (VCN)**. The wizard is a guided, step-by-step process in the Console that sets up the VPN plus related Networking service components.
Other secure VPN solutions include OpenVPN, a Client VPN solution that can be accessed in the [Oracle Marketplace](https://cloudmarketplace.oracle.com/marketplace/listing/67830324). OpenVPN connects individual devices to your VCN, but not whole sites or networks.
## Purpose of the Wizard 🔗 
Site-to-Site VPN involves setting up and configuring several Networking service components. The wizard sets up those components for you. In general, the wizard does the following:
  * Uses a template with [assumptions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#assumptions) that will help you get started.
  * Asks you for some basic network information.
  * Sets up the Networking service components for you.
  * Lets you generate configuration content for a network engineer to use when configuring your customer-premises equipment (CPE) device.


The wizard is a task within the overall process of setting up Site-to-Site VPN, which is illustrated in the following diagram. The wizard is the shaded box.
[![This image shows a flow diagram of the overall Site-to-Site VPN setup process.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_workflow_process_flow.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_workflow_process_flow.svg)
Notice that the overall process includes work by a network engineer in your organization. That engineer provides information that you, in turn, must supply when running the wizard. The wizard returns information that the network engineer needs when configuring your CPE device. You can use the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) to consolidate the necessary information into an organized template for the network engineer.
The following short sections summarize each task.
Task 1: Information to get from your network engineer 
  * CPE device's public IP address. (The address must be IPv4, but IPv6 traffic is supported)
  * CPE vendor. model, and version
  * CPE IKE identifier. For more information, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components).
  * On-premises network routes.
  * If you use BGP dynamic routing with the VPN:
    * Your network's BGP ASN
    * For each of the two IPSec tunnels that will be created, the pair of BGP IP addresses (with subnet mask) that you want to use for the inside tunnel interfaces at the ends of each tunnel. For example:
      * Tunnel 1: Inside tunnel interface - CPE: 10.0.0.16/31
      * Tunnel 1: Inside tunnel interface - Oracle: 10.0.0.17/31
      * Tunnel 2: Inside tunnel interface - CPE: 10.0.0.8/31
      * Tunnel 2: Inside tunnel interface - Oracle: 10.0.0.9/31


Task 2: Wizard 
You walk through the wizard in the Console. For more information, see these sections:
  * [Where to Access the Wizard in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#location)
  * [What the Wizard Creates for You](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#results)


Task 3: Information to give to your network engineer 
You use the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) to generate configuration content that your network engineer can use to configure the CPE.
The content includes these items:
  * The Oracle VPN IP address and shared secret for each IPSec tunnel.
  * The supported IPSec parameter values.
  * Information about the VCN.
  * CPE-specific configuration information.


Task 4: CPE configuration 
Your network engineer takes the information you provide and configures your CPE device.
Task 5: Testing 
You and the network engineer test the connection and confirm that traffic is flowing.
## Alternative to the Wizard 🔗 
If you prefer, you can manually set up Site-to-Site VPN yourself. For step-by-step instructions, see [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN).
## What the Wizard Creates for You 🔗 
Most Oracle customers who set up Site-to-Site VPN already have a VCN to connect to their on-premises network. In that case, the wizard creates the numbered components in the following diagram. The table describes each component.
[![This image shows the Networking service components that are created for you.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_workflow_results.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_workflow_results.svg)
Number | Component | Description | Can Use Existing One or Create New One?  
---|---|---|---  
1 | CPE | A CPE is a _virtual representation_ of your actual CPE device. This virtual representation contains basic information such as the CPE device's public IP address.  | Yes, you can either use an existing CPE or the wizard creates a new one.  
2 | IPSec tunnels |  The wizard creates two [IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top), each with specific configuration information that you must provide to your network engineer. **Note:** The wizard uses IKEv1 or IKEv2 for the tunnels. For more information on IKEv2, see [Using IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2). | No. The wizard automatically creates the tunnels.  
3 | Dynamic Routing Gateway (DRG) | A [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) is a _virtual representation_ of the actual router at the Oracle end of your Site-to-Site VPN. | Yes.  
4 | Internet Gateway |  If the VCN you select does not already have an [Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway), you can choose to let the wizard create one to enable direct connectivity to the internet.  | Yes, you can either use an existing internet gateway or choose to let the wizard create a new one.  
5 | Subnet Route table |  | Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | DRG  
**Note** To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
In addition, during the wizard you specify which subnets in your VCN should be configured with access to the on-premises network. The wizard updates each subnet's route table and security rules as follows:
  * **Route rules:** The wizard adds one or more rules to route VCN traffic to your on-premises network by way of the DRG. There's one rule per on-premises network route that you provide in the wizard. If the VCN has an internet gateway (or you choose to create one) and a public subnet is selected, the wizard also adds a rule to send remaining traffic (not destined for the on-premises network) to the internet gateway.
  * **Security list rules:** The wizard also adds one or more rules to allow all types of traffic from your on-premises network. There's one rule per on-premises network route that you provide in the wizard. If the VCN has an internet gateway (or you choose to create one) and a public subnet is selected, the wizard also adds a rule to allow SSH over port 22 from the internet.


You can edit the rules and add more if you want.
After the wizard completes, you can use the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) to generate configuration content that your network engineer can use to configure the CPE.
## Where to Access the Wizard in the Console 🔗 
Option 1:
  1. Open the navigation menu, click ****Networking**** , and then click **Overview**.
  2. Click the **Start VPN wizard** button.


Option 2:
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  2. Click **Start VCN Wizard**.
  3. Select **Add Site-to-Site VPN and Internet Connectivity to a VCN** , and then click **Start VCN Wizard**.


Option 3:
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Start VPN Wizard**.


## Related Topics 🔗 
  * [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top)
  * [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN)
  * [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters)
  * [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)
  * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
  * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
  * [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect)
  * [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
  * [Using the API for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Using_the_API_for_VPN_Connect)


Was this article helpful?
YesNo

