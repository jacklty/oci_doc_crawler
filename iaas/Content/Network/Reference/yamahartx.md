Updated 2025-01-17
# Yamaha RTX Series
This configuration was validated using an RTX1210 running Firmware Rev.14.01.28 and RTX830 running Firmware Rev.15.02.03.
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
**Important** Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
## Before Starting 🔗 
Before configuring your CPE:
  * Configure your internet provider settings.
  * Configure firewall rules to open UDP port 500, UDP port 4500, and ESP.


### Supported Encryption Domain or Proxy ID
The values for the encryption domain (also known as a proxy ID, security parameter index (SPI), or traffic selector) depend on whether your CPE supports route-based tunnels or policy-based tunnels. For more information about the correct encryption domain values to use, see [Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#Supported_Encryption_Domain_or_Proxy_ID).
## Parameters from API or Console 🔗 
Get the following parameters from the Oracle Cloud Infrastructure Console or API.
**${ipAddress#}**
  * Oracle VPN headend IPSec tunnel endpoints. There is one value for each tunnel.
  * Example value: 129.146.12.52


**${sharedSecret#}**
  * The IPSec IKE pre-shared-key. There is one value for each tunnel.
  * Example value: EXAMPLEDPfAMkD7nTH3SWr6OFabdT6exXn6enSlsKbE


**${cpePublicIpAddress}**
  * The public IP address for the CPE (previously made available to Oracle via the Console).


**${VcnCidrBlock}**
  * When creating the VCN, your company selected this CIDR to represent the IP aggregate network for all VCN hosts.
  * Example Value: 10.0.0.0/20


## Parameters Based on Current CPE Configuration and State 🔗 
The following parameters are based on your current CPE configuration.
**${tunnelInterface#}**
  * An interface number to identify the specific tunnel.
  * Example value: 1


**${ipsecPolicy#}**
  * The SA policy to be used for the selected inline interface. 
  * Example value: 1


**${localAddress}**
  * The public IP address of your CPE.
  * Example value: 146.56.2.52


## Config Template Parameter Summary 🔗 
Each region has multiple Oracle IPSec headends. The following template allows you to set up multiple tunnels on your CPE, each to a corresponding headend. In the table, "User" is you/your company.
Parameter | Source | Example Value  
---|---|---  
`${ipAddress1}` | Console/API | 129.146.12.52  
`${sharedSecret1}` | Console/API | (long string)  
`${ipAddress2}` | Console/API | 129.146.13.52  
`${sharedSecret2}` | Console/API | (long string)  
`${cpePublicIpAddress``}` | User | 1.2.3.4  
`${VcnCidrBlock}` | User | 10.0.0.0/20  
**Important** The following ISAKMP and IPSec policy parameter values are applicable to Site-to-Site VPN in the commercial cloud. For the [Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm), you must use the values listed in [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params).
## ISAKMP Policy Options 🔗 
Parameter | Recommended Value  
---|---  
ISAKMP protocol version | Version 1  
Exchange type  | Main mode  
Authentication method | Pre-shared keys  
Encryption | AES-256-cbc  
Authentication algorithm | SHA-256  
Diffie-Hellman Group | Group 5  
IKE session key lifetime | 28800 seconds (8 hours)  
## IPSec Policy Options 🔗 
Parameter | Recommended Value  
---|---  
IPSec protocol | ESP, tunnel-mode  
Encryption | AES-256-cbc  
Authentication algorithm | HMAC-SHA1-96  
Diffie-Hellman Group | Group 5  
Perfect Forward Secrecy  | Enabled  
IPSec session key lifetime | 3600 seconds (1 hour)  
## CPE Configuration 🔗 
### ISAKMP and IPSec Configuration
Copy
```
tunnel select 1
description tunnel OCI-VPN1 
ipsec tunnel 1
 ipsec sa policy 1 1 esp aes256-cbc sha-hmac
 ipsec ike duration ipsec-sa 1 3600
 ipsec ike duration isakmp-sa 1 28800
 ipsec ike encryption 1 aes256-cbc
 ipsec ike group 1 modp1536
 ipsec ike hash 1 sha256
 ipsec ike keepalive log 1 off
 ipsec ike keepalive use 1 on dpd 5 4
 ipsec ike local address 1 ${cpePublicIpAddress}
 ipsec ike local id 1 0.0.0.0/0
 ipsec ike nat-traversal 1 on
 ipsec ike pfs 1 on
 ipsec ike pre-shared-key 1 text ${sharedSecret1}
 ipsec ike remote address 1 ${ipAddress1}
 ipsec ike remote id 1 0.0.0.0/0
ip tunnel tcp mss limit auto
tunnel enable 1
tunnel select 2
description tunnel OCI-VPN2
ipsec tunnel 2
 ipsec sa policy 2 2 esp aes256-cbc sha-hmac
 ipsec ike duration ipsec-sa 2 3600
 ipsec ike duration isakmp-sa 2 28800
 ipsec ike encryption 2 aes256-cbc
 ipsec ike group 2 modp1536
 ipsec ike hash 2 sha256
 ipsec ike keepalive log 2 off
 ipsec ike keepalive use 2 on dpd 5 4
 ipsec ike local address 2 ${cpePublicIpAddress}
 ipsec ike local id 2 0.0.0.0/0
 ipsec ike nat-traversal 2 on
 ipsec ike pfs 2 on
 ipsec ike pre-shared-key 2 text ${sharedSecret2}
 ipsec ike remote address 2 ${ipAddress2}
 ipsec ike remote id 2 0.0.0.0/0
ip tunnel tcp mss limit auto
tunnel enable 2
ipsec auto refresh on

```

### Static Routes Configuration
Copy
```
ip route ${VcnCidrBlock} gateway tunnel 1 hide gateway tunnel 2 hide
```

Was this article helpful?
YesNo

