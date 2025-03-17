Updated 2024-10-07
# Customer Site Network Requirements
Review the topics in this section to prepare your network environment before the arrival of the Oracle Compute Cloud@Customer rack.
**Note**
In addition to the network requirements listed here, an Oracle representative works with you to ensure that your data center network configuration is prepared to accommodate Compute Cloud@Customer before the rack arrives.
Use the network information in this section with the [Networking Checklist](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/networking-checklist.htm#initial-installation-checklist "This section helps you plan for the configuration information that's required when Oracle installs the Oracle Compute Cloud@Customer rack in your data center.") to prepare your network.
Oracle Compute Cloud@Customer network architecture relies on physical high speed Ethernet connectivity.
The networking infrastructure in Oracle Compute Cloud@Customer is integral and must not be altered. The networking doesn't integrate into any data center management or provisioning frameworks such as Cisco ACI, Network Director, or the like, except for the ability to query the switches using SNMP in read-only mode. 
**Caution**
No changes to the networking switches in the Compute Cloud@Customer rack are supported unless directed by an Oracle KM note or Oracle personnel.
## Network Overview 🔗 
**Note** Additional network overview concepts are described in [Network Infrastructure](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/network-infrastructure.htm#network-infrastructure "For network connectivity, Compute Cloud@Customer relies on a physical layer that provides the necessary high-availability, bandwidth and speed. On top of this, a distributed network fabric composed of software-defined switches, routers, gateways, and tunnels enables secure and segregated data traffic – both internally between cloud resources, and externally to and from resources outside of Compute Cloud@Customer.").
The Compute Cloud@Customer infrastructure uses these networks.
  * **Data Network:** The infrastructure's data connectivity is built on redundant 100-Gbit switches in two-layer design similar to a leaf-spine topology. An infrastructure contains two leaf and two spine switches. The leaf switches interconnect the rack hardware components, while the spine switches form the backbone of the network and provide a path for external traffic.
  * **Uplinks:** Uplinks are the connections between the infrastructure and the customer data center. For external connectivity, 5 ports are reserved on each spine switch. Four ports are available to establish the uplinks between the infrastructure and the data center network; one port is used to segregate the administration network from the data traffic. 
  * **Administration Network:** This required network is configured as a physically separated network from the data network. This isolates configuration and management traffic from the operational activity on the data network by providing dedicated secured network paths for administration operations. This network includes all component management interfaces.
Setting up a segregated administration network involves the following actions:
    * Extra Ethernet connections from the next-level data center network devices to port 5 on each of the spine switches in the rack.
    * Inside the administration network, the spine switches must each have one IP address and a virtual IP shared between the two.
    * A default gateway is required to route traffic, and NTP and DNS services must be enabled.
    * The management nodes must be assigned host names and IP addresses in the administration network, one each individually, and one shared between all three.
A separate administration network can be used with both static and dynamic routing. The use of a VLAN is supported, but when combined with static routing the VLAN ID must be different from the one configured for the data network.
  * **Reserved Network Resources:** infrastructure requires many IP addresses and several VLANs for internal operation.


## Network Configuration Requirements 🔗 
On each spine switch, ports 1-4 can be used for uplinks to the data center network. For speeds of 10-Gbps or 25-Gbps, the spine switch port must be split using a 4-way splitter or breakout cable. For higher speeds of 40-Gbps or 100-Gbps each switch port uses a single direct cable connection. 
The uplinks are configured during system initialization, based on information you provide. Unused spine switch uplink ports, including unused breakout ports, are disabled for security reasons.
It is critical that **both** spine switches have the same connections to the next-level data center switches. This configuration provides redundancy and load splitting at the level of the spine switches, the ports and the data center switches. This outbound cabling depends on the network topology you deploy. The cabling pattern is essential to the continuation of service during failover scenarios.
  * Before installation, you must run network cables from your existing network infrastructure to the Oracle Compute Cloud@Customer rack installation site. 
  * Plan to connect at least 1 high-speed Ethernet port on each _spine_ switch to your data center public Ethernet network.
  * Configuring the required Administration network requires 2 more cable connections (one each from port 5 on the two spine switches) to a pair of next-level data center switches. 
  * Uplink connectivity is based on layer 3 of the OSI model.
  * If you have security policies requiring the use of proxies for all internet connections,you can use an `HTTP` proxy. This is a passive/corporate proxy supported for the connection from Compute Cloud@Customer to Oracle Cloud Infrastructure. Customer `HTTPS`, challenge proxy, and traffic inspection aren't supported.
  * A corporate HTTP proxy between the Compute Cloud@Customer infrastructure and Oracle Cloud Infrastructure isn't recommended with FastConnect because FastConnect is already a dedicated network. If a corporate proxy is required, then the proxy needs to have additional routing to ensure that Compute Cloud@Customer network traffic is sent over FastConnect. 


## DNS Configuration 🔗 
Review the Oracle Compute Cloud@Customer DNS information to choose the configuration that best suits your network environment.
To integrate the data of the infrastructure's dedicated DNS zone into the data center DNS configuration, two options are supported: 
  * [Zone Delegation (Preferred)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/network-requirements.htm#dns-configuration__zone-delegation)
  * [Manual Configuration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/network-requirements.htm#dns-configuration__manual-configuration)


If you select manual configuration, it's good practice to register network host names and IP addresses for the management network, client network, and more public networks in the data center Domain Name System (DNS) before the initial configuration. In particular, all public addresses, VIP addresses, and infrastructure services endpoints must be registered in DNS before the installation.
All addresses registered in DNS must be configured for forward resolution; reverse resolution isn't supported in the services zone.
### Zone Delegation (Preferred) 🔗 
For zone delegation to work, the data center's recursive caches must be able to reach TCP/UDP port 53 on the virtual IP address shared by the Compute Cloud@Customer management nodes. It might be necessary to change your firewall configuration.
Configure the data center DNS server so that it operates as the parent zone of the Compute Cloud@Customer DNS zone. Thus, all DNS requests for the child zone are delegated to the Compute Cloud@Customer internal DNS server. In the data center DNS configuration, add a name server record for the child zone and an address record for the authoritative server of that zone.
In the example it is assumed that the data center DNS domain is `example.com`, that the Compute Cloud@Customer rack is named `myccc`, and that the management node cluster virtual IP address is 192.0.2.102. The Compute Cloud@Customer internal DNS server host name is `ns1`.
```
$ORIGIN example.com.
[...]
myccc    IN  NS  ns1.myccc.example.com.
ns1.myccc  IN  A   192.0.2.102
           
```

### Manual Configuration 🔗 
Manually add DNS records for all labels or host names required by Compute Cloud@Customer. Many of the DNS entries are required for maintenance performed by Oracle personnel.
In the examples, the data center DNS domain is `example.com`, that the Compute Cloud@Customer rack is named `myccc`, and that the management node cluster virtual IP address is 192.0.2.102.
**Note**
For object storage, you must point the DNS label to the Object Storage Public IP. This is the public IP address assigned for this purpose when setting up the data center public IP ranges during Initial Setup.
Compute Cloud@Customer Infrastructure Service |  Compute Cloud@Customer DNS Label and Data Center DNS Records  
---|---  
Console `console.myccc.example.com ` |  ```
console        A 192.0.2.102
                  
```
  
DNS service `dns.myccc.example.com ` |  ```
dns      A 192.0.2.102
                  
```
  
File storage `filestorage.myccc.example.com ` |  ```
filestorage      A 192.0.2.102
                  
```
  
Identity and Access Management service `identity.myccc.example.com ` |  ```
identity      A 192.0.2.102
                  
```
  
Networking, Compute, Block Storage, Work Requests services `iaas.myccc.example.com ` |  ```
iaas      A 192.0.2.102
                  
```
  
Object storage `objectstorage.myccc.example.com ` **Note:** Use the Object Storage Public IP from the Initial Setup. |  ```
objectstorage      A 198.51.100.33
                  
```
  
Resource Principal Service `rps.myccc.example.com ` |  ```
rps      A 192.0.2.102
                  
```
  
## Data Center Switch Configuration Notes 🔗 
When configuring the data center switches to accept incoming Compute Cloud@Customer uplinks (default uplinks as well as any custom uplinks you define) take these notes into account. 
  * All uplinks, default and customer, are configured to use link aggregation (LACP). All switch ports included in an uplink configuration must belong to the same link aggregation group (LAG). The switch ports on the data center side of the uplinks must be configured accordingly. 
  * The spine switches operate with the Virtual Port Channel (vPC) feature enabled in static routing configurations. 
  * Compute Cloud@Customer supports layer 3 based uplink connectivity to the customer data center. Static routing and BGP4-based dynamic routing are supported in layer 3.
  * Autonegotiation isn't available for uplink ports. Transfer speed must be specified on the customer switches' end. 


For more information, see [Uplinks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/uplinks.htm#uplinks "The connections between the Compute Cloud@Customer and the customer data center are called uplinks. They're physical cable connections between the spine switches in the rack and one or, preferably, two next-level network devices in the data center.") and [Uplink Protocols](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/uplink-protocols.htm#uplink-protocols_0 "On Compute Cloud@Customer, the uplinks to the data center run various protocols to provide redundancy and reduce link failure detection and recovery times on these links. These protocols work with the triangle, square, or mesh topologies.").
Was this article helpful?
YesNo

