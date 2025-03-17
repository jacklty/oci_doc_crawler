Updated 2025-01-15
# Access to Microsoft Azure
Oracle and Microsoft have created a cross-cloud connection between Oracle Cloud Infrastructure and Microsoft Azure in certain regions. This connection lets you set up cross-cloud workloads without the traffic between the clouds going over the internet. This topic describes how to set up virtual networking infrastructure resources to enable this kind of cross-cloud deployment.
For information about multicloud Oracle Database deployments that use Oracle Cloud Infrastructure and Microsoft Azure, see [Oracle Database@Azure](https://docs.oracle.com/iaas/Content/multicloud/oaa.htm). This service hosts Oracle Exadata Databases in Azure data centers for the lowest possible latency.
## Highlights 🔗 
  * You can connect a Microsoft Azure virtual network (VNet) with an Oracle Cloud Infrastructure (OCI) Virtual Cloud Network (VCN) and run a cross-cloud workload. In the typical use case, you deploy your Oracle Database on OCI, and deploy an Oracle, .NET, or custom application in Microsoft Azure. 
  * The two virtual networks must belong to the same company and not have overlapping CIDRs. The connection requires you to create an Azure ExpressRoute circuit and an OCI FastConnect virtual circuit.


## Availability 🔗 
The cross-cloud connection between OCI and Azure is only available in the regions and ExpressRoute locations shown below. For more information on Azure region locations and Azure ExpressRoute, see [ExpressRoute peering locations and connectivity partners](https://docs.microsoft.com/azure/expressroute/expressroute-locations-providers) in the Azure documentation.
The following image shows regions with interconnect.
[![Map showing which regions interconnect with Azure ExpressRoute.](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/network-fc-markets.svg)](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/network-fc-markets.svg)
### Asia Pacific (APAC)
OCI location - key | Azure ExpressRoute location ![Microsoft logo](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/msft-logo.svg)  
---|---  
Japan East (Tokyo) NRT | Tokyo  
Singapore (Singapore) - SIN | Singapore  
South Korea Central (Seoul) - ICN | Seoul  
### Europe, Middle East, Africa (EMEA)
OCI location | Azure ExpressRoute location ![Microsoft logo](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/msft-logo.svg)  
---|---  
Germany Central (Frankfurt) - FRA | Frankfurt and Frankfurt2  
Netherlands Northwest (Amsterdam) - AMS | Amersterdam2  
UK South (London) - LHR | London  
South Africa Central (Johannesburg) - JNB | Johannesburg  
### Latin America (LATAM)
OCI location | Azure ExpressRoute location ![Microsoft logo](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/msft-logo.svg)  
---|---  
Brazil Southeast (Vinhedo) - VCP | Campinas  
### North America (NA)
OCI location | Azure ExpressRoute location ![Microsoft logo](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/msft-logo.svg)  
---|---  
Canada Southeast (Toronto) - YYZ | Toronto and Toronto2  
US East (Ashburn) - IAD | Washington DC and Washington DC2  
US West (Phoenix) - PHX | Phoenix  
US West (San Jose) - SJC | Silicon Valley  
## Overview of Supported Traffic 🔗 
Here are more details about the supported types of traffic.
### VNet-to-VCN Connection: Extension from One Cloud to Another
You can connect your VNet and VCN so that traffic that uses private IP addresses goes over the cross-cloud connection.
For example, the following diagram shows a VNet that is connected to a VCN. Resources in the VNet are running a .NET application that access an Oracle database that runs on Database service resources in the VCN. The traffic between the application and database uses a logical circuit that runs on the cross-cloud connection between Azure and Oracle Cloud Infrastructure.
[![This diagram shows the connection between an Azure VNet and Oracle VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_basic_diagram.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_basic_diagram.svg)
To enable the connection between the VNet and VCN, you set up an Azure ExpressRoute circuit and an Oracle Cloud Infrastructure FastConnect virtual circuit. The connection has built-in redundancy, which means you need to set up only a single ExpressRoute circuit and single FastConnect virtual circuit. The bandwidth for the connection is the bandwidth value you choose for the ExpressRoute circuit.
For instructions, see [Setting Up a VNet-to-VCN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#set_up_cxn). 
### Peered VCNs
The connection enables traffic to flow from the VNet through the connected VCN to a peered VCN in the same Oracle Cloud Infrastructure region, or a different region.
### Types of Traffic Not Supported by the Connection
This cross-cloud connection does not enable traffic between your on-premises network through the VCN to the VNet, or from your on-premises network through the VNet to the VCN. 
## Important Implications of Connecting Clouds 🔗 
This section summarizes some access control, security, and performance implications of connecting your VCN to a VNet. In general, you can control access and traffic by using IAM policies, route tables in the VCN, and security rules in the VCN. 
The sections that follow discuss implications from the perspective of your VCN. Similar implications affect your VNet. As with your VCN, you can use Azure resources such as route tables and network security groups to secure your VNet. 
### Controlling the Establishment of a Connection
With Oracle Cloud Infrastructure IAM policies, you can control:
  * Who in your organization has the authority to create a FastConnect virtual circuit (see [Setting Up a VNet-to-VCN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#set_up_cxn)). Deletion of the relevant IAM policy does not affect any existing connections to a VNet, only the ability for a future connection to be created.
  * Who can manage [route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2), [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups), and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists). 


### Controlling Traffic Flow Over the Connection
Even if a connection has been established between your VCN and VNet, you can control the packet flow over the connection with route tables in your VCN. For example, you can restrict traffic to only specific subnets in the VNet. 
Without terminating the connection, you can stop traffic flow to the VNet by simply removing route rules that direct traffic from your VCN to the VNet. You can also effectively stop the traffic by removing any security rules that enable ingress or egress traffic with the VNet. This doesn't stop traffic flowing over the connection, but stops it at the [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) level. 
### Controlling the Specific Types of Traffic Allowed
It's important that you ensure that all outbound and inbound traffic with the VNet is intended or expected and well defined. Implement Azure network security group and Oracle security rules that explicitly state the types of traffic one cloud can send to the other and accept from the other. 
**Important**
Your Oracle Cloud Infrastructure instances running Linux or Windows [platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm) also have firewall rules that control access to the instance. When troubleshooting access to an instance, ensure that the following items are set correctly: the network security groups that the instance is in, the security lists associated with the instance's subnet, and the instance's firewall rules.
If your instance is running Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7, Oracle Linux 8, Oracle Linux 7, or Oracle Linux Cloud Developer 8, you need to use [firewalld](https://oracle-base.com/articles/linux/linux-firewall-firewalld) to interact with the iptables rules. For your reference, here are commands for opening a port (1521 in this example):
Copy
```
sudo firewall-cmd --zone=public --permanent --add-port=1521/tcp
								
sudo firewall-cmd --reload
```

For instances with an iSCSI boot volume, the preceding `--reload` command can cause problems. For details and a workaround, see [Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).
In addition to security rules and firewalls, you should evaluate other OS-based configuration on the instances in your VCN. There could be default configurations that don't apply to your own VCN's CIDR, but inadvertently apply to the VNet's CIDR. 
### Using Default Security List Rules with Your VCN
If your VCN's subnets use the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) with the default rules, two rules in that list allow ingress traffic from anywhere (that is, 0.0.0.0/0, and thus the VNet):
  * Stateful ingress rule that allows TCP port 22 (SSH) traffic from 0.0.0.0/0 and any source port
  * Stateful ingress rule that allows ICMP type 3, code 4 traffic from 0.0.0.0/0 and any source port


Evaluate these rules and whether you want to keep or update them. As stated earlier, you should ensure that all permitted inbound or outbound traffic is intended or expected and well defined. 
### Preparing for Performance Impact and Security Risks
In general, you should prepare your VCN for the ways it could be affected by the VNet. For example, the load on your VCN or its instances could increase. Or your VCN could experience a malicious attack directly from or by way of the VNet. 
Regarding performance: If your VCN is providing a service to the VNet, be prepared to scale up your service to accommodate the demands of the VNet. This might mean being prepared to launch more instances as necessary. Or if you're concerned about high levels of network traffic coming to your VCN, consider using [stateless security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful) to limit the level of connection tracking your VCN must perform. Stateless security rules can also help slow the impact of a denial-of-service (DoS) attack. 
Regarding security risks: If the VNet is connected to the internet, your VCN can be exposed to bounce attacks. A bounce attack involves a malicious host on the internet sending traffic to your VCN that looks like it's coming from the VNet. To guard against this, as mentioned earlier, use your security rules to carefully limit the inbound traffic from the VNet to expected and well-defined traffic.
## Setting Up a VNet-to-VCN Connection 🔗 
This section describes how to set up the logical connection between a VNet and VCN (for background, see [Overview of Supported Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#supported_traffic)).
### Prerequisites: Resources You Need
You must already have:
  * An [Azure VNet](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview) with subnets and virtual network gateway 
  * An Oracle Cloud Infrastructure[ VCN with subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.") and an [attached Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs). It's easy to forget to [attach the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\).") to your VCN after you create it. If you already have Site-to-Site VPN or FastConnect between your on-premises network and VCN, then your VCN already has an attached DRG. You use that same DRG here when setting up the connection to Azure.


As a reminder, here is a table that lists the comparable networking components involved in each side of the connection.
Component | Azure | Oracle Cloud Infrastructure   
---|---|---  
Virtual network | VNet | VCN  
Virtual circuit | ExpressRoute circuit | FastConnect private virtual circuit  
Gateway | virtual network gateway | Dynamic Routing Gateway (DRG)  
Routing | route tables | route tables  
Security rules | network security groups (NSGs) | network security groups (NSGs), security lists  
### Prerequisites: BGP Information You Need 🔗 
The connection between the VNet and VCN uses BGP dynamic routing. When you set up the Oracle virtual circuit, you provide the BGP IP addresses that will be used for the two redundant BGP sessions between Oracle and Azure:
  * A primary pair of BGP addresses (one IP address for the Oracle side, one IP address for the Azure side)
  * A separate, secondary pair of BGP addresses (one IP address for the Oracle side, one IP address for the Azure side)


**For each pair, you must provide a separate block of addresses with a subnet mask from /28 to /31**. 
The second and third addresses in each address block are used for the BGP IP address pair. Specifically: 
  * The second address in the block is for the Oracle side of the BGP session
  * The third address in the block is for the Azure side of the BGP session


The first and last addresses in the block are used for other internal purposes.
For example, if the CIDR is 10.0.0.20/30, then the addresses in the block are:
  * 10.0.0.20
  * 10.0.0.21: Use this for the Oracle side (in the Oracle Console, enter the address as 10.0.0.21/30)
  * 10.0.0.22: Use this for the Azure side (in the Oracle Console, enter the address as 10.0.0.22/30, and notice that this address is referred to as the "Customer" side in the Console)
  * 10.0.0.23


Remember that you must also provide a second block with the same size for the secondary BGP addresses. For example: 10.0.0.24/30. In this case, 10.0.0.25 is for the Oracle side, and 10.0.0.26 is for the Azure side. In the Oracle Console, you must enter these as 10.0.0.25/30 and 10.0.0.26/30. 
### Prerequisites: Required IAM Policy 🔗 
It's assumed that you have the necessary Azure Active Directory access and Oracle Cloud Infrastructure IAM access to create and work with the relevant Azure and Oracle networking resources. Specifically for IAM: If your user is in the [Administrators group](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The), you have the required authority. 
If your user is not, then a policy like this one generally covers all the Networking resources:
Copy
```
Allow group NetworkAdmins to manage virtual-network-family in tenancy
```

To _only_ create and manage a virtual circuit, you must have a policy like this:
Copy
```
Allow group VirtualCircuitAdmins to manage drgs in tenancy
Allow group VirtualCircuitAdmins to manage virtual-circuits in tenancy
```

For more information, see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
### Overall Process
The following diagram shows the overall process of connecting your VNet and VCN.
[![This swimlane diagram shows the steps for connecting your Azure VNet and Oracle VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_setup_flow.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_setup_flow.svg)
[Task 1: Configure the network security groups and security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The first task is to determine what traffic needs to flow between the relevant subnets within the VNet and VCN, and then configure the VNet security groups and VCN security rules accordingly. Here are the general types of rules to add:
  * Ingress rules for the types of traffic you want to allow into one cloud from the other, specifically from the other cloud's relevant subnets.
  * Egress rule to allow outgoing traffic from one cloud to the other. If the VCN's subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the traffic to the VNet. The VCN's default security list includes a broad default egress rule like this.


More specifically, here are recommended types of traffic to allow between the VNet and VCN:
  * [Ping traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) in both directions for testing the connection from each side
  * SSH (TCP port 22)
  * Client connections to an Oracle database (SQL*NET on TCP port 1521)


Only allow traffic to and from specific address ranges of interest (for example, the other cloud's relevant subnets). 
**For the VNet:** Determine which subnets in your VNet need to communicate with the VCN. Then configure the network security groups for those subnets to allow traffic.
**For the VCN:**
**Note** The following procedure uses security lists, but you could instead implement the security rules in one or more [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then place the VCN's relevant resources in NSGs. 
  1. Determine which subnets in your VCN need to communicate with the VNet.
  2. Update the security list for each of those subnets to include rules to allow egress or ingress traffic specifically with the VNet's CIDR block or a subnet of the VNet: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in. 
    3. Click **Edit All Rules** and create one or more rules, each for the specific type of traffic you want to allow. 
    4. Click **Save Security List Rules** at the bottom of the dialog box.
For more information about setting up security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).


[Example: Outgoing ping from VCN to VNet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The following egress security rule lets an instance initiate a ping request to a host outside the VCN (echo request ICMP type 8). This is a stateful rule that automatically allows the response. No separate ingress rule for echo reply ICMP type 0 is required.
  1. In the **Allow Rules for Egress** section, click **+Add Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Destination CIDR:** The relevant subnet in the VNet (10.0.0.0/16 in the preceding diagram)
  4. **IP Protocol:** ICMP
  5. **Type and Code:** 8
  6. **Description:** An optional description of the rule.


[Example: Incoming ping to VCN from VNet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The following ingress security rule lets an instance receive a ping request from a host in the VNet (echo request ICMP type 8). This is a stateful rule that automatically allows the response. No separate egress rule for echo reply ICMP type 0 is required.
  1. In the **Allow Rules for Ingress** section, click **+Add Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source CIDR:** The relevant subnet in the VNet (10.0.0.0/16 in the preceding diagram)
  4. **IP Protocol:** ICMP
  5. **Type and Code:** 8
  6. **Description:** An optional description of the rule.


[Example: Incoming SSH to VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The following ingress security rule lets an instance receive an SSH connection (TCP port 22) from a host in the VNet.
  1. In the **Allow Rules for Ingress** section, click **+Add Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source CIDR:** The relevant subnet in the VNet (10.0.0.0/16 in the preceding diagram)
  4. **IP Protocol:** TCP
  5. **Source Port Range:** All
  6. **Destination Port Range** : 22
  7. **Description:** An optional description of the rule.


[Example: SQL*Net connections to database](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The following ingress security rule allows SQL*Net connections (TCP port 1521) from hosts in the VNet.
  1. In the **Allow Rules for Ingress** section, click **+Add Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source CIDR:** The relevant subnet in the VNet (10.0.0.0/16 in the preceding diagram)
  4. **IP Protocol:** TCP
  5. **Source Port Range:** All
  6. **Destination Port Range** : 1521
  7. **Description:** An optional description of the rule.


[Task 2: Set up Azure ExpressRoute circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
[Set up an ExpressRoute circuit](https://docs.microsoft.com/azure/expressroute/expressroute-howto-circuit-portal-resource-manager) to _Oracle Cloud Infrastructure FastConnect_. During the circuit setup, you receive a service key from Microsoft. Record that service key, because you must provide it to Oracle in the next task. 
In the next task, you set up a FastConnect private virtual circuit to _Microsoft Azure: ExpressRoute_. When that virtual circuit finishes being provisioned, your ExpressRoute circuit updates to show that private peering is enabled.
[Task 3: Set up an Oracle Cloud Infrastructure FastConnect virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
  1. In the Console, confirm you're viewing the **compartment** that you want to work in. If you're not sure which one, use the compartment that contains the DRG that you'll connect to. This choice of compartment, along with a corresponding [IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm), controls who can access the virtual circuit you're about to create. 
  2. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **FastConnect**.
The resulting **FastConnect** page is where you create a new virtual circuit and later return to when you need to manage the virtual circuit.
  3. Click **Create Connection**.
  4. Select **FastConnect partner** and choose **Microsoft Azure: ExpressRoute** from the list. 
  5. Enter the following for your virtual circuit:
     * **Name:** A friendly name of your choice. The value does not need to be unique across your virtual circuits, and you can change it later. Avoid entering confidential information.
     * **Create in Compartment:** Leave as is (the compartment you're currently working in). 
     * **Virtual Circuit Type:** Select **Private Virtual Circuit**. 
     * **Dynamic Routing Gateway Compartment:** Select the compartment where the DRG resides (it should already be selected).
     * **Dynamic Routing Gateway:** Select the DRG.
     * **Provisioned Bandwidth:** Choose the same bandwidth level you chose for the ExpressRoute circuit (or the closest value available). 
     * **Partner Service Key:** Enter the service key you received from Microsoft when you set up the ExpressRoute circuit. 
     * **Customer Primary BGP IP Address:** This field is the Azure primary BGP IP address. Enter the third address in the primary CIDR block (with a subnet mask from /28 to /31) that you provide, and include the subnet mask at the end. For example: 10.0.0.22/30. For more information about this field and the next ones, see [Setting Up a VNet-to-VCN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#set_up_cxn).
     * **Oracle Primary BGP IP address (optional):** You can leave this field blank and Oracle infers the address based on the CIDR block you provided for the Azure BGP IP address. In this example, the correct value would be 10.0.0.21/30. 
     * **Customer Secondary BGP IP Address:** This field is the Azure secondary BGP IP address. Enter the third address in the secondary CIDR block (with a subnet mask from /28 to /31) that you provide, and include the subnet mask at the end. For example: 10.0.0.26/30. 
     * **Oracle Primary BGP IP Address (optional):** You can leave this field blank and Oracle infers the address based on the CIDR block you provided for the Azure BGP IP address. In this example, the correct value would be 10.0.0.25/30. 
  6. Click **Continue**. 
The virtual circuit is created.
  7. Click **Close**.


After you create the Oracle virtual circuit, you do not need to contact Azure to request provisioning of the circuit. It happens automatically.
[Task 4: Confirm that both circuits are provisioned](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
Within a few minutes, both circuits should be provisioned. To verify:
  * For the ExpressRoute circuit, confirm that private peering is provisioned.
  * For the FastConnect virtual circuit, confirm that its status is UP. See [To get the status of your FastConnect virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#vc_status). 


[Task 5: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
**For the VNet:** Determine which subnets in your VNet need to communicate with the VCN. Then [configure the route tables](https://docs.microsoft.com/azure/virtual-network/virtual-networks-udr-overview) for those subnets to route traffic to the VNet gateway.
**For the VCN:**
  1. Determine which subnets in your VCN need to communicate with the VNet.
  2. Update the route table for each of those subnets to include a new rule that directs traffic destined for the VNet's CIDR to your DRG: 
    1. In the Console, while viewing the VCN you're interested in, click **Route Tables**. 
    2. Click the route table you're interested in.
    3. Click **Edit Route Rules**. 
    4. Click **+ Another Route Rule** and enter the following:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
       * **Destination CIDR Block:** The relevant subnet in the VNet (10.0.0.0/16 in the preceding diagram).
       * **Description:** An optional description of the rule.
    5. Click **Save**.


Any subnet traffic with a destination that matches the rule is routed to your DRG. The DRG then knows to route the traffic to the VNet based on the virtual circuit's BGP session information. 
Later, if you no longer need the connection and want to delete your DRG, you must first delete all the route rules in your VCN that specify the DRG as the target.
For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
[Task 6: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
Depending on how you've set up your VNet security groups and VCN security rules, you should be able to [create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) in your VCN and access it from a host in the VNet. Or you should be able to connect from the instance to a host in the VNet. If you can, your connection is ready to use.
**Important** If you decide to terminate the connection, you must follow a particular process. See [To terminate the connection to Azure](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#terminate_connection).
## Managing a VNet-to-VCN Connection 🔗 
[To get the status of your FastConnect virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **FastConnect**.
  2. Select the compartment where the connection resides, and then click the connection you're interested in. If the icon for the virtual circuit is green and says UP, the virtual circuit is provisioned and BGP has been correctly configured.The virtual circuit is ready to use. 


[To edit a FastConnect virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
You can change these items for your virtual circuit:
  * The name
  * Which DRG it uses


**Caution** If your virtual circuit is in the PROVISIONED state, changing which DRG it uses switches the state to PROVISIONING and **may cause the connection to go down.** After Oracle reprovisions the virtual circuit, its state returns to PROVISIONED. Confirm that the connection is back up and working.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **FastConnect**.
  2. Select the compartment where the connection resides, and then click the connection. 
  3. Click the virtual circuit. 
  4. Click **Edit** and make your changes. Avoid entering confidential information.
  5. Click **Save**.


[To terminate the connection to Azure](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
The following diagram shows the overall process of terminating a VNet-to-VCN connection.
[![This flow chart shows the steps for terminating the VNet-to-VCN connection](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_terminate_flow.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_azure_terminate_flow.svg)
  1. In the Azure portal, view the ExpressRoute circuit, and then view its **Connections**. Confirm that there are no **Connections** still in existence for the ExpressRoute circuit. [Delete all **Connections**](https://docs.microsoft.com/azure/expressroute/expressroute-howto-linkvnet-portal-resource-manager#delete-a-connection-to-unlink-a-vnet) before proceeding. 
  2. In the Oracle portal, delete your FastConnect virtual circuit:
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **FastConnect**.
    2. Select the compartment where the connection resides, and then click the connection. 
    3. Click the virtual circuit. 
    4. Click **Delete**.
    5. Confirm when prompted.
The virtual circuit's Lifecycle State switches to TERMINATING.
  3. In the Azure portal, confirm that the private peering for the ExpressRoute circuit has been deleted. Also confirm that the ExpressRoute circuit's status has changed to "Not Provisioned".
  4. In the Azure portal, [delete the ExpressRoute circuit](https://docs.microsoft.com/azure/expressroute/expressroute-howto-circuit-portal-resource-manager#delete).


The connection between Azure and Oracle Cloud Infrastructure is terminated. 
Was this article helpful?
YesNo

