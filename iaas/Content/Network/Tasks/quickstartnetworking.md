Updated 2025-02-12
# Virtual Networking Wizards
To make it easier to set up a Virtual Cloud Network (VCN) and connect to it, the Console has the following wizards that walk you through network setup.
## Create a VCN with Internet Connectivity 🔗 
**What this wizard does:**
  * Checks for resource availability. To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
  * Creates a [VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure."). This wizard can support the creation of a VCN with IPv6 addresses. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
  * Creates an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway), [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway), and [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway) for the VCN.
  * Creates a regional public subnet with routing to the internet gateway. Instances in a public subnet may optionally have public IP addresses.
  * Creates a regional private subnet with routing to the NAT gateway and service gateway (and therefore the Oracle Services Network). Instances in a private subnet can't have public IP addresses.
  * Sets up basic security list rules for the two subnets, including SSH access.


This wizard supports the creation of a VCN with IPv6 addresses. IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
**Where to access this wizard:**
Option 1:
  1. Open the navigation menu, click ****Networking**** , and then click **Overview**.
  2. Click the **Start VCN wizard** button.


Option 2: 
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  2. Click **Start VCN Wizard**.
  3. Select **Create VCN with Internet Connectivity** , and then click **Start VCN Wizard**.


## Add Internet Connectivity and Site-to-Site VPN to a VCN  🔗 
**What this wizard does:**
  * Checks for resource availability. To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
  * Creates an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) for the VCN.
  * Creates a regional public subnet with access to the internet gateway. Instances in a public subnet may optionally have public IP addresses.
  * Sets up basic security list rules for the subnet, including SSH access.
  * Sets up all the Networking service resources required for a [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") between the VCN and an on-premises network. The wizard can optionally have the IPSec encrypted traffic use an existing FastConnect link between the VCN and an on-premises network. See [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) for details.


**Note** For the IPSec connection to work, a network engineer must also configure the customer-premises equipment (CPE) in the edge network.
**More information about this wizard:** [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart)
**Where to access this wizard:**
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


Was this article helpful?
YesNo

