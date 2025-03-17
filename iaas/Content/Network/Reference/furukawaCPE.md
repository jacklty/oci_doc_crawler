Updated 2025-01-17
# Furukawa Electric
Learn how to configure a Furukawa Electric router for Site-to-Site VPN between your on-premises network and cloud network.
This configuration was validated using a Furukawa Electric series FITELnet-F220/F221 running Firmware 01.00(00)[0]00.00.0 [2019/07/05 15:00].
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
**Important** Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
## Before Starting 🔗 
Before configuring your CPE, ensure that you:
  * Configure your internet provider settings.
  * Configure firewall rules to open UDP port 500, UDP port 4500, and ESP.


### Supported Encryption Domain or Proxy ID
The values for the encryption domain (also known as a proxy ID, security parameter index (SPI), or traffic selector) depend on whether your CPE supports route-based tunnels or policy-based tunnels. For more information about the correct encryption domain values to use, see [Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#Supported_Encryption_Domain_or_Proxy_ID).
## Parameters from API or Console 🔗 
Get the following parameters from the Oracle Cloud Infrastructure Console or API.
**${vpn-ip#}**
  * Oracle VPN headend IPSec tunnel endpoints. There is one value for each tunnel.
  * Example values: 129.146.12.52, 129.146.13.52


**${sharedSecret#}**
  * The IPSec ISAKMP pre-shared-key. There is one value for each tunnel.
  * Example value: EXAMPLEDPfAMkD7nTH3SWr6OFabdT6exXn6enSlsKbE


**${cpePublicIpAddress}**
  * The public IP address for the CPE (previously made available to Oracle via the Console).


**${VcnCidrBlock}**
  * When creating the VCN, your company selected this CIDR to represent the IP aggregate network for all VCN hosts.
  * Example Value: 10.0.0.0/20


## Parameters Based on Current CPE Configuration and State 🔗 
The following parameters are based on your current CPE configuration.
**${tunnelNumber#}**
  * An interface number to identify the specific tunnel. You need one unused unit number per tunnel.
  * Example value: 1, 2


**${isakmpPolicy}**
  * The ISAKMP policy name.
  * Example value: isakmp-policy


**${ipsecPolicy#}**
  * The IPSec policy name.
  * Example value: ipsec-policy


**${isakmpProfile#}**
  * The ISAKMP profile name. You need one unused ISAKMP profile name per tunnel.
  * Example values: OCI-VPN-profile1, OCI-VPN-profile2


**${selector}**
  * The selector name.
  * Example value: OCI-VPN-selector


**${map#}**
  * The map name. You need one unused map name per tunnel.
  * Example values: OCI-VPN-MAP1, OCI-VPN-MAP2


**${customer-bgp-asn}**
  * Your BGP ASN.
  * Example value: 65000


**${oracle-bgp-asn#}**
  * Oracle's BGP ASN.
  * Example value: 31898


**${customer-interface-ip#}**
  * The inside tunnel interface for CPE.
  * Example value: 10.0.0.16/31


**${oracle-interface-ip#}**
  * The inside tunnel interface for ORACLE.
  * Example value: 10.0.0.17/31


**${router-id}**
  * The BGP router ID.
  * Example value: 10.0.0.16


## Config Template Parameter Summary 🔗 
Each region has multiple Oracle IPSec headends. The following template allows you to set up multiple tunnels on your CPE, each to a corresponding headend. In the following table, "User" is you/your company.
Parameter | Source | Example Value  
---|---|---  
`${vpn-ip1}` | Console/API | 129.146.12.52  
`${sharedSecret1}` | Console/API | (long string)  
`${vpn-ip2}` | Console/API | 129.146.13.52  
`${sharedSecret2}` | Console/API | (long string)  
`${cpePublicIpAddress``}` | User | 203.0.113.1  
`${VcnCidrBlock}` | User | 10.0.0.0/20  
`${tunnelNumber1}` | User | 1  
`${tunnelNumber1}` | User | 2  
`${isakmpPolicy}` | User | isakmp-policy  
`${ipsecPolicy}` | User | ipsec-policy  
`${isakmpProfile1}` | User | OCI-VPN-profile1  
`${isakmpProfile2}` | User | OCI-VPN-profile2  
`${selector}` | User | OCI-VPN-selector  
`${map1}` | User | OCI-VPN-MAP1  
`${map2}` | User | OCI-VPN-MAP2  
`${customer-bgp-asn}` | Console/API/User | 65000  
`${oracle-bgp-asn1}` | Console/API | 31898 *  
`${oracle-bgp-asn2}` | Console/API | 31898 *  
`${customer-interface-ip1}` | Console/API/User | 10.0.0.16/31  
`${customer-interface-ip2}` | Console/API/User | 10.0.0.18/31  
`${oracle-interface-ip1}` | Console/API/User | 10.0.0.17  
`${oracle-interface-ip2}` | Console/API/User | 10.0.0.19  
`${router-id}` | User | 10.0.0.16  
* Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.  
**Important** The following ISAKMP and IPSec policy parameter values are applicable to Site-to-Site VPN in the commercial cloud. For the [Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm), you must use the values listed in [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params).
## ISAKMP Policy Options 🔗 
Parameter | Recommended Value  
---|---  
ISAKMP protocol version | Version 1  
Exchange type  | Main mode  
Authentication method | Pre-shared keys  
Encryption | AES-256-cbc  
Authentication algorithm | HMAC-SHA1-96  
Diffie-Hellman Group | Group 5  
IKE session key lifetime | 28,800 seconds (8 hours)  
## IPSec Policy Options 🔗 
Parameter | Recommended Value  
---|---  
IPSec protocol | ESP, tunnel-mode  
Encryption | AES-CBC/256  
Authentication algorithm | HMAC-SHA1-96/160  
Diffie-Hellman Group | Group 5  
Perfect Forward Secrecy  | Enabled  
IPSec session key lifetime | 3600 seconds (1 hour)  
## CPE Configuration 🔗 
### ISAKMP and IPSec Configuration
Copy
```
crypto ipsec policy ${ipsecPolicy}
 set pfs group5
 set security-association transform-keysize aes 256 256 256
 set security-association transform esp-aes esp-sha-hmac
exit
!
crypto ipsec selector ${selector}
 src 1 ipv4 any
 dst 1 ipv4 any
exit
!
crypto isakmp policy ${isakmpPolicy}
 authentication pre-share
 encryption aes
 encryption-keysize aes 256 256 256
 group 5
 hash sha
exit
!
crypto isakmp profile ${isakmpProfile1}
 local-address ${cpePublicIpAddress}
 set isakmp-policy ${isakmpPolicy}
 set ipsec-policy ${ipsecPolicy}
 set peer ${vpn-ip1}
 ike-version 1
 local-key ascii ${sharedSecret1}
exit
!
crypto isakmp profile ${isakmpProfile2}
 local-address ${cpePublicIpAddress}
 set isakmp-policy ${isakmpPolicy}
set ipsec-policy ${ipsecPolicy}
set peer ${vpn-ip2}
ike-version 1
 local-key ascii ${sharedSecret2}
exit
!
crypto map ${map1} ipsec-isakmp
 match address ${selector}
set isakmp-profile ${isakmpProfile1}
exit
!
crypto map ${map2} ipsec-isakmp
 match address ${selector}
 set isakmp-profile ${isakmpProfile2}
exit
!
interface Tunnel ${tunnelNumber1}
 tunnel mode ipsec map ${map1}
ip address ${customer-interface-ip1}
exit
!
interface Tunnel ${tunnelNumber2}
 tunnel mode ipsec map ${map2}
 ip address ${customer-interface-ip2}
exit
```

### BGP Configuration
Copy
```
ip route ${vcnCidrBlock} Tunnel ${tunnelNumber1}
ip route ${vcnCidrBlock} Tunnel ${tunnelNumber2}
```

### Static Routes Configuration
Copy
```
router bgp ${customer-bgp-asn}
 bgp router-id ${router-id}
 bgp log-neighbor-changes
 neighbor ${oracle-interface-ip1} ebgp-multihop 10
 neighbor ${oracle-interface-ip1} enforce-multihop
 neighbor ${oracle-interface-ip1} remote-as ${oracle-bgp-asn1}
 neighbor ${oracle-interface-ip1} update-source tunnel ${tunnelNumber1}
 neighbor ${oracle-interface-ip2} ebgp-multihop 10
 neighbor ${oracle-interface-ip2} enforce-multihop
 neighbor ${oracle-interface-ip2} remote-as ${oracle-bgp-asn2}
 neighbor ${oracle-interface-ip2} update-source tunnel ${tunnelNumber2}
 !
 address-family ipv4 unicast
 redistribute connected
exit
```

Was this article helpful?
YesNo

