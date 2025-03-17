Updated 2025-01-15
# Connection Over Site-to-Site VPN
This topic describes one way to set up a connection between an Oracle Cloud Infrastructure Classic IP network and an Oracle Cloud Infrastructure Virtual Cloud Network (VCN). The connection runs over Site-to-Site VPN.
Another option is to have Oracle set up a connection over the Oracle network. For more information, see [Connection Over Oracle Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm#Connection_Over_Oracle_Network).
## Highlights 🔗 
  * You can run a hybrid workload between your Oracle Cloud Infrastructure Classic and Oracle Cloud Infrastructure environments.
  * You set up Site-to-Site VPN between the IP network's VPN as a Service (VPNaaS) gateway and the VCN's attached Dynamic Routing Gateway (DRG). The connection runs over the internet. You configure routing and security rules in the environments to enable traffic.
  * The two environments must not have overlapping CIDRs. The cloud resources can communicate over the connection only with private IP addresses. 
  * The two environments do not have to be in the same geographical area or region. 
  * The connection is free of charge.


## Overview 🔗 
You can connect your Oracle Cloud Infrastructure environment and your Oracle Cloud Infrastructure Classic environment with Site-to-Site VPN. The connection facilitates a hybrid deployment with application components that are set up across the two environments. You can also use the connection to migrate workloads from Oracle Cloud Infrastructure Classic to Oracle Cloud Infrastructure. Compared to using the Oracle network for the connection: you can set up Site-to-Site VPN yourself in a matter of minutes. Compared to FastConnect: you don't incur the additional cost and operational overhead of working with a FastConnect partner. 
The following diagram shows an example of a hybrid deployment. Oracle Analytics Cloud is running in an Oracle Cloud Infrastructure Classic IP network and accessing the Database service in Oracle Cloud Infrastructure over the connection.
[![This diagram shows the connection between an IP network and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_basic_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_basic_layout.svg)
Here are other important details to know: 
  * The connection is supported in any of the Oracle Cloud Infrastructure and Oracle Cloud Infrastructure Classic regions. The two environments do not need to be in the same geographical area.
  * The connection enables communication that uses private IP addresses only.
  * The CIDR blocks of the IP network and VCN subnets that need to communicate must not overlap.
  * This connection enables communication only between resources in the Oracle Cloud Infrastructure Classic IP network and Oracle Cloud Infrastructure VCN. It does not enable traffic between your on-premises network through the IP network to the VCN, or from your on-premises network through the VCN to the IP network. 
  * The connection also does not enable traffic to flow from the IP network through the connected VCN to a peered VCN in the same Oracle Cloud Infrastructure region, or a different region.


The following table lists the comparable networking components required on each side of the connection.
Component | Oracle Cloud Infrastructure Classic  | Oracle Cloud Infrastructure   
---|---|---  
Cloud network | IP network | VCN  
Gateway | VPNaaS gateway | Dynamic Routing Gateway (DRG)  
Security rules | security rules | network security groups, security lists  
## Setting Up Site-to-Site VPN Between Your IP Network and VCN 🔗 
The following flow chart shows the overall process of connecting your IP network and VCN with Site-to-Site VPN.
[![This flow chart shows the steps for connecting your IP network and VCN with VPN Connect](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_ipsec_setup_flow.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_ipsec_setup_flow.svg)
**Prerequisites:**
You must already have:
  * An Oracle Cloud Infrastructure Classic [IP network](https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsg/managing-ip-networks.html#GUID-10F880AD-5D84-48A6-99EF-9A47FF573883).
  * An Oracle Cloud Infrastructure[ VCN with subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.").


[Task 1: Set up a VPNaaS gateway for your IP network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
  1. Use these values when [setting up the VPNaaS gateway](https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsg/setting-vpn-connection-using-vpnaas.html#GUID-B5FD021A-C450-45EC-AF87-AE37A3AE816E):
     * **IP Network:** The Oracle Cloud Infrastructure Classic IP network you want to connect to your VCN. You can only specify a single IP network.
     * **Customer Gateway:** A placeholder value such as 129.213.240.51. Using this placeholder value lets you move forward in the process. You update the value later with the Oracle Cloud Infrastructure VPN router's IP address.
     * **Customer Reachable Routes:** The CIDR block for the VCN. You can specify only a single VCN.
     * **Specify Phase 2 ESP Proposal:** Checkbox selected.
     * **ESP Encryption:** AES 256
     * **ESP Hash:** SHA1
     * **IPSec Lifetime:** 1800
     * **Require Perfect Forward Secrecy:** Checkbox selected.
  2. Record the resulting public IP address of the VPNaaS gateway.


[Task 2: Set up the VCN's components and IPSec tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
[Task 2a: Set up a Dynamic Routing Gateway (DRG) for your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
If you do not already have a DRG attached to your VCN, create a DRG and attach it:
  * [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#drg-create "Create a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\).")


[Task 2b: Configure routing to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
Add a route rule that directs traffic from the VCN's subnets to the DRG. Use the IP network's CIDR block as the destination for the rule.
  1. Determine which subnets in your VCN need to communicate with the IP network.
  2. Update the route table for each of those subnets to include a new rule that directs traffic destined for the IP network's CIDR to your DRG: 
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in. 
    3. Under **Resources** , click **Route Tables**. 
    4. Click the route table you're interested in.
    5. Click **Add Route Rule** and enter the following:
       * **Destination CIDR Block:** The IP network's CIDR block.
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
       * **Description:** An optional description of the rule.
    6. Click **Add Route Rule**.


Any subnet traffic with a destination that matches the rule is routed to your DRG. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
Later, if you no longer need the connection and want to delete your DRG, you must first delete all the route rules in your VCN that specify the DRG as the target.
[Task 2c: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
To ensure traffic flows between the IP network and VCN, set the IP network security rules and the VCN's security rules to allow the wanted traffic.
Here are the types of rules to add:
  * Ingress rules for the types of traffic you want to allow into one cloud from the other, specifically from the other cloud's CIDR block.
  * Egress rule to allow outgoing traffic from one cloud to the other. If the VCN's subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the IP network.


[For the IP network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
[Configure the network security rules](https://docs.oracle.com/en/cloud/iaas-classic/compute-iaas-cloud/stcsg/managing-security-rules-ip-networks.html#GUID-92B69BF3-A1BF-4988-8550-2A8E3977BA97) for the IP network to allow the wanted traffic.
[For the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
**Note** The following procedure uses security lists, but you could instead implement the security rules in one or more [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then place the VCN's resources in NSGs. 
  1. Determine which subnets in your VCN need to communicate with the IP network.
  2. Update the security list for each of those subnets to include rules to allow the wanted egress or ingress traffic specifically with the CIDR block of the IP network: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in.
Under **Resources** , you can click **Ingress Rules** or **Egress Rules** to switch between the different types of rules. 
    3. Add one or more rules, each for the specific type of traffic you want to allow.
For more information about setting up security list rules, see [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists).
**Important** The VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) does not allow ICMP echo reply and echo request (ping). Add rules to enable that traffic. See [Rules to Enable Ping](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#ping)


[Example](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
Let's say you want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the IP network's CIDR. Here are the basic steps you take when adding a rule: 
  1. On the **Ingress Rules** page, click **Add Ingress Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source CIDR:** Enter the same CIDR block that the route rules use (see [Task 2b: Configure routing to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm#set_up_routing)).
  4. **IP Protocol:** Leave as TCP. 
  5. **Source Port Range:** Leave as All.
  6. **Destination Port Range** : Enter 443.
  7. Click **Add Ingress Rule**.
  8. **Description:** Optionally enter a description of the rule.


[Task 2d: Create a CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
[Create a CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#create_cpe). An IP address is required. Use the VPNaaS gateway's public IP address.
[Task 2e: Create the IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
[From your DRG, create an IPSec connection to the CPE object.](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#create_ipsec) You must provide one or more static routes. The values must match the IP network's subnets or aggregate.
The resulting IPSec connection consists of two tunnels. Record the IP address and shared secret for one of those tunnels. In the next task, you will provide those values.
[Task 3: Update the VPNaaS connection with the tunnel information](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
[Update the VPNaaS connection.](https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsg/setting-vpn-connection-using-vpnaas.html#GUID-AD90B301-D3EF-4901-A1FA-B576ADEBA24C) Use these values:
  * **Customer Gateway:** The tunnel's IP address from the preceding task.
  * **Pre-shared Key:** The tunnel's shared secret from the preceding task.


After the IPsec connection is updated and provisioned, the state of your IPSec tunnel should change to Available. Provisioning might take a few minutes. 
[Task 4: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm)
After the tunnel state changes to Available, test the connection. Depending on how you've set up your IP network's security rules and VCN security rules, you should be able to [launch an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) in your VCN and access it from an instance in the IP network. Or you should be able to connect from the VCN instance to an instance in the IP network. If you can, your connection is ready to use.
## Terminating the Connection 🔗 
If you want to terminate the connection, delete the IPSec connection:
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the IPSec connection you're interested in.
  3. Select **Terminate**.
  4. Confirm the deletion when prompted.


The IPSec connection is in the Terminating state for a short period while it's being deleted.
Was this article helpful?
YesNo

