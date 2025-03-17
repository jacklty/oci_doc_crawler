Updated 2025-01-15
# FastConnect Requirements
This topic covers the requirements for implementing FastConnect.
For general information about FastConnect, see the articles listed for [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."). 
## Before Getting Started: Learn and Plan 🔗 
Here are basic things you need to do before getting started with FastConnect:
  * **FastConnect concepts:** Be familiar with the basic concepts covered in [FastConnect Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#concepts).
  * **Limits increase:** If you are colocated with Oracle, you must ask Oracle to increase your account limits for cross-connects. By default, these limits are initially set to 0, and a request to create a cross-connect will fail. For instructions, see [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti). In your request, indicate the region where you need the resources. It can take a couple of business days for the limit increase to take effect.
  * **Hardware and routing requirements:** Review the [hardware and routing requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements). 
  * **Tenancy setup and compartment design:** If you haven't yet, set up your tenancy. Think about who needs access to Oracle Cloud Infrastructure and how. For more information, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). Specifically for FastConnect, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#Required) to understand the policy required to work with FastConnect components.
  * **Cloud network design:** Design your Virtual Cloud Network (VCN), including how you want to allocate your VCN's [subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure."), define [security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists), define [route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2), set up [load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm), and so on. For more information, see [Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/landing.htm#top "Oracle Cloud Infrastructure Networking helps you set up virtual versions of traditional network components.").
  * **Redundancy:** Think through your overall redundancy model to ensure your network can handle planned maintenance by Oracle or your organization, and unexpected failures of the various components. For best practices, see [FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm#FastConnect_Redundancy_Best_Practices "This topic covers best practices for redundancy when implementing FastConnect.").
  * **Public IP prefixes:** If you plan to set up a public virtual circuit, get the list of the public IP prefixes that you want to use with the connection. Oracle must validate your organization's ownership of each of the prefixes before advertising each one over the connection.
  * **Cloud network setup:** Set up your VCN, subnets, DRG, security lists, IAM policies, and so on, according to your design.
  * See [FastConnect Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#fastconnect_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for limits-related information.


## General Requirements 🔗 
Before getting started with FastConnect, ensure that you meet the following requirements:
  * Oracle Cloud Infrastructure account, with at least one user with appropriate Oracle Cloud Infrastructure Identity and Access Management (IAM) permissions (for example, a user in the Administrators group).
  * Network equipment that supports Layer 3 routing using BGP.
  * For colocation with Oracle: Ability to connect using single mode fiber in the selected FastConnect location. Also see [Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).
  * For connection to an Oracle partner: At least one physical network connection with the partner. Also see [Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).
  * For connection to a third-party provider: At least one physical connection with the provider. Also see [Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).
  * For private peering only: At least one existing [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) set up for a VCN.
  * For public peering only: The list of public IP address prefixes that you want to use with the connection. Oracle validates ownership of each prefix.


**Important** If you intend to colocate with Oracle, you must ask Oracle to increase your account limits for cross-connects. These [default limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#fastconnect_limits) are initially set to 0, and a without a specific request for a limit increase you won't be able to create a valid cross-connect. For instructions on placing this request, see [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti). In your request, **indicate the region where you need the resources**. It can take a couple of business days for the limit increase to take effect.
## Hardware and Routing Requirements 🔗 
[If you're using an Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm)
Here are general routing requirements for FastConnect. These are relevant if the BGP session is [between your edge and Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams).
  * **IP addressing supported:** IPv4 and IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
  * **P2P IP addresses:**
    * For public virtual circuits, Oracle specifies the IP addresses. 
    * For private virtual circuits where the BGP session is [between your edge and Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams), you specify these addresses (using a subnet mask from /28 to /31, and one pair per virtual circuit). If you set up several private virtual circuits that go to the same DRG, you must use a different address on the edge router for each virtual circuit. 
  * **Maximum IP MTU:** 9000
  * **Routing protocol:** BGPv4
  * **BGP prefix limit:** For public virtual circuits: 200 prefixes. For private virtual circuits: 2000 IPv4 prefixes and 500 IPv6 prefixes.
  * **BGP ASN:** 2-byte or 4-byte ASNs are supported, except for those listed in [Special-Purpose Autonomous System (AS) Numbers](https://www.iana.org/assignments/iana-as-numbers-special-registry/iana-as-numbers-special-registry.xhtml). Public virtual circuits require a public ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the US Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). For the United Kingdom Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). BGP ASN 65534 isn't available for you to use with FastConnect and VPN. All other private ASNs in the 64512 - 65533 (inclusive) range defined in [RFC-6996](https://tools.ietf.org/html/rfc6996) can be used normally.
  * **BGP MD5 authentication:** Optional to use with a virtual circuit. Oracle supports up to 128-bit MD5 authentication
  * **BGP keep-alive interval:** Oracle's default is 10 seconds. This is how often Oracle sends keep-alive messages.
  * **BGP hold-time interval:** Oracle's default is 30 seconds. This is how long Oracle waits to receive a keep-alive message before declaring the BGP session has failed.


**Tip** If you need fast BGP convergence, you can use any value in these supported ranges: 6 to 60 seconds for keep-alive, and 18 to 180 seconds for hold-time. BGP timers are negotiated between the two BGP peers to the lower value used by one of the two sides. 
[If you're colocating in a FastConnect location or using a third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm)
For the cross-connect group and cross-connects:
  * **Bandwidth (three choices)** :
    * 1 Gbps:
      * 1000Base-LX, 10-km range, 1310 nm 
      * **You must configure your edge device so that auto-negotiation is OFF**
      * Minimum Rx level > - 15 dBm
    * 10 Gbps:
      * 10 Gbps, LR (10-km range), 1310 nm
      * Minimum Rx level > - 12 dBm
    * 100 Gbps: 
      * 100GBASE, LR4 QSFP28 (10-km range), WDM optics
      * Minimum Rx level > -12 dBm on each of four lanes 
    * 400 Gbps: 
      * 400GBASE-LR4 QSFP-DD (10-km range), WDM optics
      * Minimum Rx level > -12 dBm on each of four lanes 
  * **General:**
    * Single Mode Fiber
    * Duplex LC connectors
  * **Redundancy:**
    * Device redundancy highly recommended
    * In some regions, location redundancy is available and recommended 
  * **Capacity:**
    * 1 Gbps: Minimum 1, Maximum 8
    * 10 Gbps: Minimum 1, Maximum 8
    * 100 Gbps: Minimum 1, Maximum 8
    * 400 Gbps: Minimum 1, Maximum 8
  * **LAG protocol:** LACP with short timers (3 @ 1s). If your router doesn't support LAG, you can set up a single non-LAG cross-connect. 
  * **VLAN tagging:** 802.1q (single tag)
  * **VLAN range:** 100-4094 (you assign the VLANs)
  * **Maximum interface MTU:** 9196 (include 4-byte FCS trailer)


For routing:
  * **IP addressing supported:** IPv4 and IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
  * **P2P IP addresses:**
    * For public virtual circuits, Oracle specifies the IP addresses. 
    * For private virtual circuits, you specify the addresses (using a subnet mask from /28 to /31). You need one pair of IP addresses per private virtual circuit. If you set up multiple private virtual circuits that go to the same DRG, you must use a different address on your edge router for each virtual circuit. 
  * **Maximum IP MTU:** 9000
  * **Routing protocol:** BGPv4
  * **BGP prefix limit:** For public virtual circuits: 200 prefixes. For private virtual circuits: 2000 IPv4 prefixes and 500 IPv6 prefixes.
  * **BGP ASN:** 2-byte or 4-byte ASNs are supported, except for those listed in [Special-Purpose Autonomous System (AS) Numbers](https://www.iana.org/assignments/iana-as-numbers-special-registry/iana-as-numbers-special-registry.xhtml). Public virtual circuits require a public ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the US Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). For the United Kingdom Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govuksouth.htm#Regions__uk_bgp_asn)
BGP ASN 65534 is not available for you to use with FastConnect and VPN. All other private ASNs in the 64512 - 65533 (inclusive) range defined in [RFC-6996](https://tools.ietf.org/html/rfc6996) can be used normally.
  * **BGP MD5 authentication:** Optional to use with your virtual circuit. Oracle supports up to 128-bit MD5 authentication
  * **BGP keep-alive interval:** Oracle's default is 10 seconds. This is how often Oracle sends keep-alive messages.
  * **BGP hold-time interval:** Oracle's default is 30 seconds. This is how long Oracle waits to receive a keep-alive message before declaring the BGP session has failed.


**Tip** If you need fast BGP convergence, you can use any value in these supported ranges: 6 to 60 seconds for keep-alive, and 18 to 180 seconds for hold-time. BGP timers are negotiated between the two BGP peers to the lower value used by one of the two sides. 
## Required IAM Policy 🔗 
[If you're using an Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm)
To work with Networking resources such as dynamic routing gateways (DRGs), VCNs, and virtual circuits, you need to have a user sign-in to the Console, and the user sign-in needs to belong to a group with authority (by way of an [IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm)) to perform all the configuration tasks. If the user sign-in is in the [Administrators group](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The), you have the required authority. 
If the group exist but doesn't have a policy yet, then a policy like this would cover all the Networking resources:
Copy
```
Allow group NetworkAdmins to manage virtual-network-family in tenancy
```

To _only_ create and manage a virtual circuit, you would need a policy like this:
Copy
```
Allow group VirtualCircuitAdmins to manage drgs in tenancy
Allow group VirtualCircuitAdmins to manage virtual-circuits in tenancy
```

The first statement (to manage DRGs) is necessary only for private virtual circuits. 
For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
[If you're colocating in a FastConnect location or using a third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm)
To work with Networking resources such as dynamic routing gateways (DRGs), VCNs, virtual circuits, and cross-connects, you need to have a user sign-in to the Console, and the account needs to be part of a group with sufficient authority (by way of an [IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm)) to perform all the instructions that follow. If the user sign-in belongs to the [Administrators group](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The), you have the required authority. 
If the group is not already set up, then a policy like this would cover all the Networking resources:
Copy
```
Allow group NetworkAdmins to manage virtual-network-family in tenancy
```

To _only_ create and manage cross-connects, cross-connect groups, and virtual circuits, you would need a policy like this:
Copy
```
Allow group FastConnectAdmins to manage drgs in tenancy
Allow group FastConnectAdmins to manage cross-connects in tenancy
Allow group FastConnectAdmins to manage cross-connect-groups in tenancy
Allow group FastConnectAdmins to manage virtual-circuits in tenancy
```

The first statement (to manage DRGs) is necessary only for private virtual circuits. 
For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
## Identifiers for FastConnect Resources 🔗 
FastConnect resources have several identifiers:
  * **Name for the overall connection:** When you create a new FastConnect connection, you can give it a descriptive name of your choice. If you don't specify one, Oracle automatically assigns a name to the connection. 
  * **Reference name for each cross-connect:** Each cross-connect has an optional reference name. If you set up a cross-connect, Oracle recommends that you fill in the reference name with the identifier for the cross-connect's physical fiber cable. That makes it easier for Oracle to help if future troubleshooting is required for the connection. After cabling is done and you have the identifier from the data center, you can add it to the cross-connect's information in the Oracle Console.
  * **OCID for each resource:** Each cross-connect group, cross-connect, and virtual circuit has its own unique [Oracle-assigned identifier](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) called an OCID.


## What's Next? 🔗 
Connect an on premises network to OCI using one of the following connection types: 
  * [FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.")
  * [FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.")
  * [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location.")


Was this article helpful?
YesNo

