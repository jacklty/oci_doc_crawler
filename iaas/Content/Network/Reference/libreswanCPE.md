Updated 2025-01-17
# Libreswan
[Libreswan](https://libreswan.org/) is an open source IPSec implementation based on FreeS/WAN and Openswan. Most Linux distributions include Libreswan or make it easy to install. You can install it on hosts in either an on-premises network or a cloud provider network. For an example of setting up a Libreswan host in another cloud provider to connect to an Oracle Cloud Infrastructure virtual cloud network (VCN), see [Access to Other Clouds with Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/libreswan.htm#Access_to_Other_Clouds_with_Libreswan). 
This topic provides configuration for a CPE running Libreswan. Virtual tunnel interface (VTI) support for this route-based configuration requires minimum Libreswan version 3.18 and a recent Linux 3.x or 4.x kernel. This configuration was validated using Libreswan version 3.29.
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
Oracle Cloud Infrastructure offers Site-to-Site VPN, a secure IPSec connection between an on-premises network and a virtual cloud network (VCN).
The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are an example only.
[![This image summarizes the general layout of an on-premises network, Site-to-Site VPN IPSec tunnels, and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)
## Best Practices 🔗 
This section covers general best practices and considerations for using Site-to-Site VPN.
### Configure All Tunnels for Every IPSec Connection
Oracle deploys two IPSec headends for connections to provide high availability for mission-critical workloads. On the Oracle side, these two headends are on different routers for redundancy purposes. We recommend configuring all available tunnels for maximum redundancy. This is a key part of the "Design for Failure" philosophy.
### Have Redundant CPEs in On-Premises Network Locations
We recommend that each site that connects with IPSec to Oracle Cloud Infrastructure has redundant edge devices (also known as customer-premises equipment (CPE)). You add each CPE to the Oracle Console and create a separate IPSec connection between a **dynamic routing gateway (DRG)** and each CPE. For each IPSec connection, Oracle provisions two tunnels on geographically redundant IPSec headends. For more information, see the [Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf).
### Routing Protocol Considerations
When you create a Site-to-Site VPN IPSec connection, it has two redundant IPSec tunnels. Oracle encourages you to configure the CPE to use both tunnels (if the CPE supports it). In the past, Oracle created IPSec connections that had up to four IPSec tunnels.
The following three routing types are available, and you select the routing type separately for each tunnel in the Site-to-Site VPN:
  * **BGP dynamic routing:** The available routes are learned dynamically through BGP. The DRG dynamically learns the routes from the on-premises network. On the Oracle side, the DRG advertises the VCN's subnets. 
  * **Static routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically.
  * **Policy-based routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically. 


For more information about routing with Site-to-Site VPN, including Oracle recommendations on how to manipulate the BGP best path selection algorithm, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
### Other Important CPE Configurations
Ensure that access lists on the CPE are configured correctly to not block necessary traffic from or to Oracle Cloud Infrastructure.
If you have several tunnels up simultaneously, you might experience asymmetric routing. To account for asymmetric routing, ensure that the CPE is configured to handle traffic coming from the VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass . For more details about the appropriate configuration, contact the CPE vendor's support. To configure routing to be symmetric, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
## Caveats and Limitations 🔗 
This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Asymmetric Routing
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably. 
When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.
For specific Oracle routing recommendations about how to force symmetric routing, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing). 
### Route-Based or Policy-Based Site-to-Site VPN
The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet. 
**Note** Other vendors or industry documentation might use the term _proxy ID, security parameter index (SPI)_ , or _traffic selector_ when referring to SAs or encryption domains.
There are two general methods for implementing IPSec tunnels:
  * **Route-based tunnels:** Also called _next-hop-based tunnels_. A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel. 
  * **Policy-based tunnels:** The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.


The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections. 
### Libreswan 3.25 Caveat
If a CPE device uses Libreswan 3.25 or earlier and you try to set up an IKEv1 connection with a CPE as a responder, you need to explicitly set the phase 2 parameter in a CPE configuration for the IPSec tunnel to come up. For example, using the current recommended encryption algorithm AES-256-gcm and PFS group5, you must configure the phase 2 parameter `phase2alg="aes_gcm256;modp1536"` on the CPE device.
This problem isn't seen in later Libreswan releases.
[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend. 
Route-based IPSec uses an encryption domain with the following values:
  * **Source IP address:** Any (0.0.0.0/0)
  * **Destination IP address:** Any (0.0.0.0/0)
  * **Protocol:** IPv4


If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.
[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
When you use policy-based tunnels, every policy entry (a CIDR block on one side of the IPSec connection) that you define generates an IPSec security association (SA) with every eligible entry on the other end of the tunnel. This pair is referred to as an _encryption domain_. 
In this diagram, the Oracle DRG end of the IPSec tunnel has policy entries for three IPv4 CIDR blocks and one IPv6 CIDR block. The on-premises CPE end of the tunnel has policy entries two IPv4 CIDR blocks and two IPv6 CIDR blocks. Each entry generates an encryption domain with all possible entries on the other end of the tunnel. Both sides of an SA pair must use the same version of IP. The result is a total of eight encryption domains.
[![Diagram showing several encryption domains and how to find their number.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)
**Important**
If the CPE only supports policy-based tunnels, be aware of the following restrictions.
  * Site-to-Site VPN supports multiple encryption domains, but has an upper limit of 50 encryption domains.
  * If you had a situation similar to the prior example and only configured three of the six possible IPv4 encryption domains on the CPE side, the link would be listed in a "Partial UP" state because all possible encryption domains are always created on the DRG side.
  * Depending on when a tunnel was created you might not be able to edit an existing tunnel to use policy-based routing and might need to replace the tunnel with a new IPSec tunnel.
  * The CIDR blocks used on the Oracle DRG end of the tunnel can't overlap the CIDR blocks used on the on-premises CPE end of the tunnel. 
  * An encryption domain must always be between two CIDR blocks of the same IP version.


### If The CPE Is Behind a NAT Device 🔗 
In general, the CPE IKE identifier configured on the on-premises end of the connection must match the CPE IKE identifier that Oracle is using. By default, Oracle uses the CPE's _public_ IP address, which you provide when you create the CPE object in the Oracle Console. However, if a CPE is behind a NAT device, the CPE IKE identifier configured on the on-premises end might be the CPE's _private_ IP address, as shown in the following diagram.
[![This image shows the CPE behind a NAT device, the public and private IP addresses, and the CPE IKE identifier.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)
**Note** Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as _cpe.example.com_. For instructions, see [Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id).
## Supported IPSec Parameters 🔗 
For a vendor-neutral list of supported IPSec parameters for all regions, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
The Oracle BGP ASN for the commercial cloud realm is 31898. If you're configuring Site-to-Site VPN for the US Government Cloud, see [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params) and also [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). For the United Kingdom Government Cloud, see [Regions](https://docs.oracle.com/iaas/Content/General/Concepts/govuksouth.htm#Regions).
## CPE Configuration 🔗 
**Important**
The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.
The following figure shows the basic layout of the IPSec connection. 
[![This image summarizes the general layout of the IPSec connection and tunnels.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)
### Default Libreswan Configuration Files
The default Libreswan installation creates the following files:
  * `etc/ipsec.conf`: The root of the Libreswan configuration.
  * `/etc/ipsec.secrets`: The root of the location where Libreswan looks for secrets (the tunnel pre-shared keys).
  * `/etc/ipsec.d/`: A directory for storing the `.conf` and `.secrets` files for the Oracle Cloud Infrastructure tunnels (for example: `oci-ipsec.conf` and `oci-ipsec.secrets`). Libreswan encourages you to create these files in this folder.


The default `etc/ipsec.conf` file includes this line:
Copy
```
include /etc/ipsec.d/*.conf
```

The default `etc/ipsec.secrets` file includes this line:
Copy
```
include /etc/ipsec.d/*.secrets
```

The preceding lines automatically merge all the`.conf` and `.secrets` files in the `/etc/ipsec.d` directory into the main configuration and secrets files that Libreswan uses.
### About Using IKEv2
Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you [configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure the CPE to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
You specify the IKE version when setting up the IPSec configuration file in [task 3](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm#task3) in the next section. That example file shows a comment showing how to configure IKEv1 compared with IKEv2.
### Configuration Process
Libreswan supports both route-based and policy-based tunnels. The tunnel types can coexist without interfering with each other. The Oracle VPN headends use route-based tunnels. We recommend that you configure Libreswan with the [Virtual Tunnel Interface (VTI) configuration syntax](https://libreswan.org/wiki/Route-based_VPN_using_VTI).
For details about the specific parameters used in this document, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
[Task 1: Prepare the Libreswan instance](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
Depending on the Linux distribution you're using, you might need to enable IP forwarding on an interface to allow clients to send and receive traffic through Libreswan. In the `/etc/sysctl.conf` file, set the following values and apply the updates with `sudo sysctl -p`.
If you're using an interface other than eth0, change `eth0` in the following example to the interface (lines 5 and 7).
Copy
```
net.ipv4.ip_forward=1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.eth0.send_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.eth0.accept_redirects = 0
```

[Task 2: Decide the required configuration values](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
The Libreswan configuration uses the following variables. Decide the values before proceeding with the configuration. 
  * `${cpeLocalIP}`: The IP address of the Libreswan device.
  * `${cpePublicIpAddress}`: The public IP address for Libreswan. This is the IP address of the outside interface. Depending on the network topology, the value might be different from `${cpeLocalIP}`.
  * `${oracleHeadend1}`: For the first tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
  * `${oracleHeadend2}`: For the second tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
  * `${vti1}`: The name of the first VTI used. For example, vti1.
  * `${vti2}`: The name of the second VTI used. For example, vti2.
  * `${sharedSecret1}`: The pre-shared key for the first tunnel. You can use the default Oracle-provided pre-shared key, or provide one when you set up the IPSec connection in the Oracle Console.
  * `${sharedSecret2}`: The pre-shared key for the second tunnel. You can use the default Oracle-provided pre-shared key, or provide one when you set up the IPSec connection in the Oracle Console.
  * `${vcnCidrNetwork}`: The VCN IP range.


[Task 3: Set up the configuration file](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
Libreswan configuration uses the concept of _left_ and _right_ to define the configuration parameters for a local CPE device and the remote gateway. Either side of the connection (the _conn_ in the Libreswan configuration) can be left or right, but the configuration for that connection must be consistent. In this example:
  * **left:** The local Libreswan CPE
  * **right:** The Oracle VPN headend


Use the following template for the `/etc/ipsec.d/oci-ipsec.conf` file. The file defines the two tunnels that Oracle creates when you set up the IPSec connection. 
**Important**
If the CPE is behind a 1-1 NAT device, uncomment the `leftid` parameter and set it equal to the `${cpePublicIpAddress}`.
Copy
```
conn oracle-tunnel-1
   left=${cpeLocalIP}
   # leftid=${cpePublicIpAddress} # See preceding note about 1-1 NAT device
   right=${oracleHeadend1}
   authby=secret
   leftsubnet=0.0.0.0/0 
   rightsubnet=0.0.0.0/0
   auto=start
   mark=5/0xffffffff # Needs to be unique across all tunnels
   vti-interface=${vti1}
   vti-routing=no
   ikev2=no # To use IKEv2, change to ikev2=insist 
   ike=aes_cbc256-sha2_384;modp1536
   phase2alg=aes_gcm256;modp1536
   encapsulation=yes
   ikelifetime=28800s
   salifetime=3600s
conn oracle-tunnel-2
   left=${cpeLocalIP}
   # leftid=${cpePublicIpAddress} # See preceding note about 1-1 NAT device
   right=${oracleHeadend2}
   authby=secret
   leftsubnet=0.0.0.0/0
   rightsubnet=0.0.0.0/0
   auto=start
   mark=6/0xffffffff # Needs to be unique across all tunnels
   vti-interface=${vti2}
   vti-routing=no
   ikev2=no # To use IKEv2, change to ikev2=insist 
   ike=aes_cbc256-sha2_384;modp1536
   phase2alg=aes_gcm256;modp1536 
   encapsulation=yes
   ikelifetime=28800s
   salifetime=3600s
```

[Task 4: Set up the secrets file](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
Use the following template for the `/etc/ipsec.d/oci-ipsec.secrets` file. It contains two lines per IPSec connection (one line per tunnel).
Copy
```
${cpePublicIpAddress} ${oracleHeadend1}: PSK "${sharedSecret1}"
${cpePublicIpAddress} ${oracleHeadend2}: PSK "${sharedSecret2}"
```

[Task 5: Restart the Libreswan configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
After setting up the configuration and secrets files, you must restart the Libreswan service. 
**Important** Restarting the Libreswan service might impact existing tunnels.
The following command rereads the config file and restarts the Libreswan service. 
```
service ipsec restart
```

[Task 6: Configure IP routing](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm)
Use the following `ip` command to create static routes that send traffic to a VCN through the IPSec tunnels. If you're logged in with an unprivileged user account, you might need to use `sudo` before the command.
**Important** Static routes created with the `ip route` command don't persist through a reboot. To decide how to make the routes persist, see the documentation of the Linux distribution of choice.
Copy
```
ip route add ${VcnCidrBlock} nexthop dev ${vti1} nexthop dev ${vti2}
ip route show
```

## Verification 🔗 
A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
### Verifying the Libreswan Status
Verify the current state of Libreswan tunnels by using the following command.
```
ipsec status
```

The tunnel is established if you see a line that includes the following:
```
STATE_MAIN_I4: ISAKMP SA established
```

If you're using IKEv2, you see the following:
```
STATE_V2_IPSEC_I (IPsec SA established)
```

In the future, if you need to open a support ticket with Oracle about a Libreswan tunnel, include the output of the preceding `ipsec status` command. 
### Verifying the Tunnel Interface Status
Verify that the virtual tunnel interfaces are up or down by using the `ifconfig` command or the `ip link show` command. You can also use applications such as [tcpdump](https://www.tcpdump.org/) with the interfaces. 
Here's an example of the `ifconfig` output with a working Libreswan implementation that shows the available VTIs.
```
ifconfig
<output trimmed>
				
vti01: flags=209<UP,POINTOPOINT,RUNNING,NOARP> mtu 8980
   inet6 fe80::5efe:a00:2 prefixlen 64 scopeid 0x20<link>
   tunnel txqueuelen 1000 (IPIP Tunnel)
   RX packets 0 bytes 0 (0.0 B)
   RX errors 0 dropped 0 overruns 0 frame 0
   TX packets 0 bytes 0 (0.0 B)
   TX errors 10 dropped 0 overruns 0 carrier 10 collisions 0
vti02: flags=209<UP,POINTOPOINT,RUNNING,NOARP> mtu 8980
   inet6 fe80::5efe:a00:2 prefixlen 64 scopeid 0x20<link>
   tunnel txqueuelen 1000 (IPIP Tunnel)
   RX packets 0 bytes 0 (0.0 B)
   RX errors 0 dropped 0 overruns 0 frame 0
   TX packets 0 bytes 0 (0.0 B)
   TX errors 40 dropped 0 overruns 0 carrier 40 collisions 0

```

Here's an example of the `ip link show` output:
```
ip link show
<output trimmed>
9: vti01@NONE: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 8980 qdisc noqueue
state UNKNOWN mode DEFAULT group default qlen 1000
  link/ipip 10.0.0.2 peer 129.213.240.52
10: vti02@NONE: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 8980 qdisc noqueue
state UNKNOWN mode DEFAULT group default qlen 1000
  link/ipip 10.0.0.2 peer 129.213.240.51
```

Also, in the Oracle Console, each IPSec tunnel should now be in the UP state.
Was this article helpful?
YesNo

