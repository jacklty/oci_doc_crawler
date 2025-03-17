Updated 2025-01-15
# Connection Over Oracle Network
This topic describes one way to set up a connection between an Oracle Cloud Infrastructure Classic IP network and an Oracle Cloud Infrastructure Virtual Cloud Network (VCN). The connection runs over Oracle's network.
Another option is to connect the two clouds with Site-to-Site VPN. For more information, see [Connection Over Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm#Connection_Over_IPSec_VPN).
## Highlights 🔗 
  * You can run a hybrid workload between your Oracle Cloud Infrastructure Classic and Oracle Cloud Infrastructure environments.
  * Oracle connects the IP network's private gateway to the VCN's attached Dynamic Routing Gateway (DRG). The connection runs over the Oracle network. You configure routing and security rules in the environments to enable traffic.
  * The two environments must belong to the same company and not have overlapping CIDRs. The cloud resources can communicate over the connection only with private IP addresses. 
  * The two environments must both be in the Ashburn area, the London area, or the Sydney area, and in specific regions listed in the next section. Connectivity to other regions is not supported.
  * The connection is free of charge.


## Overview 🔗 
You can request Oracle to provision a connection between your Oracle Cloud Infrastructure environment and your Oracle Cloud Infrastructure Classic environment. The connection facilitates a hybrid deployment with application components that are set up across the two environments. You can also use the connection to migrate workloads from Oracle Cloud Infrastructure Classic to Oracle Cloud Infrastructure. Compared to Site-to-Site VPN: the resources in the two environments have a more reliable and consistent network connection, with better throughput, because the traffic uses Oracle's internal links. Compared to FastConnect: you don't incur the additional cost and operational overhead of working with a FastConnect partner. 
The following diagram shows an example of a hybrid deployment. Oracle Analytics Cloud is running in an Oracle Cloud Infrastructure Classic IP network and accessing the Database service in Oracle Cloud Infrastructure over the connection.
[![This diagram shows the connection between an IP network and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_basic_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_basic_layout.svg)
Here are other important details to know: 
  * The connection is supported only between these regions:
    * Oracle Cloud Infrastructure Australia East (Sydney) region and the Sydney Classic region
    * Oracle Cloud Infrastructure US East (Ashburn) region and the Ashburn Classic region
    * Oracle Cloud Infrastructure UK South (London) region and the Slough Classic region
  * The connection enables communication that uses private IP addresses only.
  * The CIDR blocks of the IP network and VCN subnets that need to communicate must not overlap.
  * The IP network and VCN must belong to the same company. Oracle validates this when setting up the connection.
  * This connection enables communication only between resources in the Oracle Cloud Infrastructure Classic IP network and Oracle Cloud Infrastructure VCN. It does not enable traffic between your on-premises network through the IP network to the VCN, or from your on-premises network through the VCN to the IP network. 
  * The connection also does not enable traffic to flow from the IP network through the connected VCN to a peered VCN in the same Oracle Cloud Infrastructure region, or a different region.


The following table lists the comparable networking components required on each side of the connection.
Component | Oracle Cloud Infrastructure Classic  | Oracle Cloud Infrastructure   
---|---|---  
Cloud network | IP network | VCN  
Gateway | private gateway | Dynamic Routing Gateway (DRG)  
Routing | routes | route tables with route rules  
Security rules | security rules | network security groups, security lists  
## Connecting Your IP Network and VCN 🔗 
The following flow chart shows the overall process of connecting your IP network and VCN.
[![This flow chart shows the steps for connecting your IP network and VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_setup_flow.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_classic_setup_flow.svg)
**Prerequisites:**
You must already have:
  * An Oracle Cloud Infrastructure Classic [IP network](https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsg/managing-ip-networks.html#GUID-10F880AD-5D84-48A6-99EF-9A47FF573883).
  * An Oracle Cloud Infrastructure[ VCN with subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.").


[Task 1: Set up a private gateway for your IP network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
If you do not already have a private gateway for your IP network, [create one](https://docs.oracle.com/en/cloud/iaas-classic/compute-iaas-cloud/stcsg/managing-private-gateways.html#GUID-23614347-4E1E-4F57-A357-91235AE5E2CD).
[Task 2: Set up a Dynamic Routing Gateway (DRG) for your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
If you do not already have a DRG attached to your VCN, create a DRG and attach it:
  * [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#drg-create "Create a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\).")


[Task 3: Configure route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
[For the IP network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
When you create the private gateway and attach an IP network to it, traffic from cloud resources in the IP network uses the private gateway as the next hop. You do not need to update any routes for the IP network. 
[For the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
You must add a route rule that directs traffic from the VCN's subnets to the DRG:
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
[Task 4: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
To ensure traffic flows between the IP network and VCN, the IP network security rules and the VCN's security rules must be set to allow traffic.
Here are the types of rules to add:
  * Ingress rules for the types of traffic you want to allow into one cloud from the other, specifically from the other cloud's CIDR block.
  * Egress rule to allow outgoing traffic from one cloud to the other. If the VCN's subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the IP network.


[For the IP network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
[Configure the network security rules](https://docs.oracle.com/en/cloud/iaas-classic/compute-iaas-cloud/stcsg/managing-security-rules-ip-networks.html#GUID-92B69BF3-A1BF-4988-8550-2A8E3977BA97) for the IP network to allow traffic.
[For the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
**Note** The following procedure uses security lists, but you could instead implement the security rules in one or more [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then place the VCN's resources in NSGs. 
  1. Determine which subnets in your VCN need to communicate with the IP network.
  2. Update the security list for each of those subnets to include rules to allow egress or ingress traffic specifically with the CIDR block of the IP network: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in.
Under **Resources** , you can click **Ingress Rules** or **Egress Rules** to switch between the different types of rules. 
    3. Add one or more rules, each for the specific type of traffic you want to allow.


For more information about setting up security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
**Important** The VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) does not allow ICMP echo reply and echo request (ping). You must add rules to enable that traffic. See [Rules to Enable Ping](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#ping)
[Example:](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
Let's say you want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the IP network's CIDR. Here are the basic steps you take when adding a rule: 
  1. On the **Ingress Rules** page, click **Add Ingress Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source CIDR:** Enter the same CIDR block that the route rules use (see [Task 3: Configure route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm#set_up_routing)).
  4. **IP Protocol:** Leave as TCP. 
  5. **Source Port Range:** Leave as All.
  6. **Destination Port Range** : Enter 443.
  7. **Description:** Optionally enter a description of the rule.
  8. Click **Add Ingress Rule**.


[Task 5: Create a My Oracle Support ticket](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
To have Oracle set up the connection, create a ticket at [My Oracle Support](http://support.oracle.com/) and provide the following information:
  * Ticket name: Create IP Network - VCN Connection - <your_company_name> - Ashburn
  * OCI-C identity domain
  * OCI-C private gateway name
  * Region
  * OCI tenancy OCID
  * OCI DRG OCID


For example:
  * Ticket name: Create IP Network - VCN Connection - ACME - Ashburn
  * OCI-C identity domain: 123456789, uscom-east-1
  * OCI-C private gateway name: Compute-acme/jack.jones@example.com/privategateway1
  * Region: uscom-east-1 (OCI-C) / us-ashburn-1 (OCI)
  * OCI tenancy OCID: ocid1.tenancy.oc1..examplefbpnk5cmdl7gkr6kcakfqmvhvbpcv
  * OCI DRG OCID: ocid1.drg.oc1.iad.exampleutg6cmd3fqwqbea7ctadcatm


**It can take three to four business days before your My Oracle Support ticket is complete and the connection is ready to test.**
[Task 6: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm)
After you receive confirmation from your support person that the connection is ready, test the connection. Depending on how you've set up your IP network's security rules and VCN security rules, you should be able to [launch an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) in your VCN and access it from an instance in the IP network. Or you should be able to connect from the VCN instance to an instance in the IP network. If you can, your connection is ready to use.
## Terminating the Connection 🔗 
If you want to terminate the connection, file a ticket at [My Oracle Support](http://support.oracle.com/). 
Was this article helpful?
YesNo

