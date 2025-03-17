Updated 2024-11-07
# Networking Checklist
This section helps you plan for the configuration information that's required when Oracle installs the Oracle Compute Cloud@Customer rack in your data center.
Work with your network and site administrators to plan the integration of Oracle Compute Cloud@Customer into your data center. You can choose either a dynamic network or static network configuration. This checklist contains information for both options, but you only need data for the implementation that you choose.
For more information about network requirements, see [Customer Site Network Requirements](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/network-requirements.htm#customer-network-requirements "Review the topics in this section to prepare your network environment before the arrival of the Oracle Compute Cloud@Customer rack.").
**Note**
**Checklist Legend**
***** -- required fields for all configurations.
**†** -- required for static network configurations
**‡** -- required for dynamic network configurations
## Checklist – General Configuration Choices 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
(If required) Proxies for internet connections |  you can use a `HTTP` proxy (not HTTPS). This is a passive/corporate proxy supported for the connection from Compute Cloud@Customer to Oracle Cloud Infrastructure.  
Administrator user name and password  |  The rack doesn't ship with a default administrative user account. You create an administrator account during the initial installation.  Passwords must contain at least 12 characters with at least one of each: uppercase character, lowercase character, digit, punctuation character, and no double quote ('"').  
## Checklist – Compute Cloud@Customer Rack Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Region***** |  Specify the Oracle Cloud Infrastructure region name that Compute Cloud@Customer will be connect to. See [Public Cloud Regions](https://www.oracle.com/cloud/public-cloud-regions/).  
Availability Domain***** |  Specify the Oracle Cloud Infrastructure availability domain that Compute Cloud@Customer will be connected to.  
System Name***** |  Name for the rack, and used as the Compute Cloud@Customer short name.  This attribute has a maximum length of 24 characters. Acceptable characters are "a" to "z", "A" to "Z", "0" to "9", and "-". **Once set, this parameter can't be changed.**  
Domain***** |  Domain name for your system which is used as the base domain for the internal network, and by Compute Cloud@Customer public facing services. This attribute has a maximum length of 190 characters. Acceptable characters are "a" to "z", "A" to "Z", "0" to"9", "-" Example: ```
us.example.com
```
**Once set this parameter can't be changed.**  
Rack Name  | Provide a unique name for this Compute Cloud@Customer infrastructure.  
Description |  Provide an optional description for Compute Cloud@Customer.  
## Checklist – Static Routing Network Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Routing Type***** |  Choose static or dynamic routing based on your network topology.  
Uplink Gateway**†** |  IP address for the uplink switch to the default gateway in your data center. Chose a valid IP address in the customer data center subnet that the rack uplink switches are attached to. Example: ```
10.68.48.86
```
  
Spine switch virtual IP**†** |  Virtual IP address which acts as the public VIP for the spine switches in your company network. Chose a valid IP address in the data center subnet that the rack uplink switches are attached to. Example: ```
10.68.49.103
```
  
Uplink VLAN |  VLAN used to connect to an uplink switch. Chose a VLAN value between 2 and 3899. VLANs 3900 to 4095 are reserved. Example: ```
322
```
  
Uplink HSRP Group |  Assign an HSRP group number to the rack. Acceptable values are 0 to 255, and the default value is 151. If there are multiple racks connected to the same data center infrastructure switches, ensure they use _different_ HSRP groups.  
Management node 1 IP addresses and host name***** |  10/25/40/100G***** : 1G: host name: |  Static IP addresses for management node 1 in your company network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management node 2 IP addresses and host name***** |  10/25/40/100G***** : 1G: host name: |  Static IP addresses for management node 2 in your company network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management node 3 IP addresses and host name***** |  10/25/40/100G***** : 1G: host name: |  Static IP addresses for management node 3 in your company network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management virtual IP address and host name***** |  10/25/40/100G***** : 1G: host name***** : |  Virtual IP addresses of the management node cluster in your company network. This is the IP used to DNAT to the internal management node VIP. Compute Cloud@Customer DNS will resolve Compute Cloud@Customer endpoints to this IP.  Chose a valid IP address in the data center CIDR. Example: ```
10.68.49.170
```
Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Spine switch 1 IP address***** |  IP address for the spine switch 1 in your company network. Chose a valid IP address in the data center subnet that the rack uplink switches are attached to. Example: ```
10.68.49.101
```
  
Spine switch 2 IP address***** |  IP address for the spine switch 2 in your company network. Chose a valid IP address in the data center subnet that the rack uplink switches are attached to. Example: ```
10.68.49.102
```
  
## Checklist – Dynamic Routing Network Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Peer 1 IP**‡** |  Neighbor BGP IP - IP address of customer data center router-1 that the rack uplink switches are attached to. Example: ```
10.68.48.86
```
  
Peer 1 ASN**‡** |  BGP ASN of customer data center router-1. Example: ```
64512-65533 or 4200000000-4294967294 
```
(Note: Oracle Spine switch default ASN is 136025.)  
Peer 2 IP**‡** |  Neighbor BGP IP - IP address of customer data center router-2 that the rack uplink switches are attached to. Example: ```
10.68.48.88
```
  
Peer 2 ASN**‡** |  BGP ASN of customer data center router-2 Example: ```
64512-65533 or 4200000000-4294967294
```
(Note: Oracle Spine switch default ASN is 136025.)  
Uplink Gateway***** |  IP address for the uplink switch to the default gateway in your data center. Chose a valid IP address in customer data center subnet that the rack uplink switches are attached to. Example: ```
10.68.48.86
```
  
Oracle ASN |  The default is 136025.  
BGP Topology |  Options are triangle, square, or mesh. The default is mesh.  
BGP Authentication (Optional) Admin BGP Authentication |  Enable BGP authentication for your network, and admin network if used.  
BGP Authentication Password (Required) Admin BGP Authentication Password (Required if admin network used) |  Enter the BGP authentication password for your network, and admin network if used.  
BGP KeepAlive Timer |  The default is 60.  
BGP Holddown Timer |  The default is 180.  
Enable MDA Authentication |  The default is false.  
## Checklist – Uplink Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Uplink Port Speed***** |  All uplink ports must have the identical speed. The options are 10, 25, 40, 100. The default is 100.  
Uplink Port Count***** |  The number of uplink ports per spine switch. Connectivity must be identical on both spine switches to provide redundancy and load-splitting. For 100G and 40G speeds, valid values are 1, 2 and 4. For 10G and 25G ports, valid values are 1, 2, 4, 8 and 16. The default for both is 4.  
Uplink VLAN MTU***** |  MTU size determines the maximum packet size that can be transmitted over your uplink connection. The valid range is 68 to 9216. The default is 9216.  
Uplink Netmask***** |  Netmask of the subnet rack is connected to in your data center. Example: ```
255.255.252.0
```
  
Uplink Port FEC |  Configure Forward Error Correct (FEC) for the uplink port. The default option is auto, with on and off as other valid options.  
## Checklist – NTP Server Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
NTP servers***** |  At least one valid IP address for an NTP server in your data center. You can enter multiple IP addresses in a comma-separated list. Example: ```
10.147.24.1,10.211.17.1
```
  
## Checklist – Administration Network Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Admin Networking |  enable |  Enable a separate Administration network to transport administrative traffic.  
Admin Port Speed |  Port speed options are 10, 25, 40, 100. The port speed of your administration port can be different from the data port speed.   
Admin Port Count |  For 100G and 40G speeds, valid value is 1. For 10G and 25G ports, valid values are 1 to 4.  
Admin HSRP Group |  Assign an HSRP group number to your Administration network. Acceptable values are 0 to 255, and the default value is 152. If there are multiple racks connected to the same data center infrastructure switches, ensure they use _different_ HSRP groups.  
Admin VLAN |  VLAN used to connect to the Administration network (only access mode supported). The valid range for users to select is 2 to 3899. The default is 3915, in the Oracle-reserved range.  
Admin VLAN MTU |  MTU size determines the maximum packet size that can be transmitted over your administration connection. The valid range is 68 to 9216. The default is 9216.  
Admin Port FEC |  Configure Forward Error Correct (FEC) for the administration port. The default option is auto, with on and off as other valid options.  
Admin Gateway IP |  IP address of the default gateway in your Administration network.  Example: ```
10.168.141.1
```
  
Admin Netmask |  Netmask of the subnet the Administration network is connected to.  
Admin CIDR |  CIDR range for which the default route is the Administration gateway IP.  
Management node 1 IP addresses and host name |  10/25/40/100G: 1G: host name: |  Static IP addresses for management node 1 in the administration network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management node 2 IP addresses and host name |  10/25/40/100G: 1G: host name: |  Static IP addresses for management node 2 in the administration network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management node 3 IP addresses and host name |  10/25/40/100G: 1G: host name: |  Static IP addresses for management node 3 in the administration network.  Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Management virtual IP address and host name***** |  10/25/40/100G***** : 1G: host name***** : |  Virtual IP address of the management node cluster in the administration network. This is the IP used to DNAT to the internal management node VIP. Compute Cloud@Customer DNS will resolve Compute Cloud@Customer endpoints to this IP.  Chose a valid IP address in the administration network CIDR. Example: ```
10.168.141.170
```
Provide a valid host name. An appended domain name is used if you don't provide a host name.  
Admin DNS servers |  IP addresses for 1-3 DNS servers providing name resolution in the administration network. Example: ```
10.168.20.31,10.168.20.32,10.147.36.60
```
  
Admin Spine 1 IP |  Public IP address of spine switch 1. Needed for HSRP configuration or the spine virtual IP.  
Admin Spine 2 IP |  Public IP address of spine switch 2. Needed for HSRP configuration or the spine virtual IP.  
Admin Spine VIP |  Public virtual IP of the spine switches.  
## Checklist – DNS Server Details 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
DNS server 1 |  IP address for primary DNS server. Example: ```
10.68.50.60
```
  
DNS server 2 |  IP address for secondary DNS server. Example: ```
10.147.36.60
```
  
DNS server 3 |  IP address for tertiary DNS server. Example: ```
206.233.27.1
```
  
## Checklist – Compute Cloud@Customer Public IP Addresses 🔗 
Item  |  Your Configuration  |  Description and Example   
---|---|---  
Public IP Addresses |  A range of customer data center IP addresses can be used for Compute Cloud@Customer components that require public IP addresses. Note: In this context, public IP addresses refer to IP addresses that have access to the data center network from the Compute Cloud@Customer subnet. You must specify IP addresses or ranges that are routed to the Compute Cloud@Customer from the data center. Route tables must be correct and consistent. Enter a string containing a comma separated list of valid CIDRs. Example: ```
"10.68.49.249","10.68.50.32/32","10.68.51.4/31"
```
Partial CIDR deletion isn't supported.  
Object Storage IP address |  Valid IP address for an `objectstorage` endpoint that is outside the public IP range.  
## Checklist – Important Endpoints 🔗 
Compute Cloud@Customer infrastructures need to access the following endpoints from your network. Depending on your Firewall configuration, you might need to explicitly enable access to the following endpoints. 
Service Name | **Your Value** | **Endpoint FQDN**  
---|---|---  
Management plane***** |  `**ccc-mp.${region}.oci.${oraclecloud}**` Example:  ```
https://ccc-mp.us-ashburn-1.oci.oraclecloud.com
```
  
Websocket***** |  `**connect.ws.ccc.${region}.oci.${oraclecloud}**` Example:  ```
https://connect.ws.ccc.us-ashburn-1.oci.oraclecloud.com
```
  
Stunnel***** |  `**connect.se.ccc.${region}.oci.${oraclecloud}**` Example:  ```
https://connect.ws.ccc.us-ashburn-1.oci.oraclecloud.com
```
  
OCI Object Storage***** |  `**objectstorage.${region}.${oraclecloud}**` Example:  ```
https://objectstorage.us-ashburn-1.oraclecloud.com
```
  
OCI Identity***** |  `**identity.${region}.oci.${oraclecloud}**````
Example: https://identity.us-ashburn-1.oci.oraclecloud.com
```
  
OCI Authentication***** |  `**auth.${region}.${oraclecloud}**````
Example: https://auth.us-ashburn-1.oraclecloud.com
```
  
Was this article helpful?
YesNo

