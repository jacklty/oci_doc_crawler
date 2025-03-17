Updated 2024-08-21
# Supported IPSec Parameters
This topic lists the supported phase 1 (ISAKMP) and phase 2 (IPSec) configuration parameters for Site-to-Site VPN. Oracle chose these values to maximize security and to cover a wide range of CPE devices. If your CPE device is not on the [list of verified devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices), use the information here to configure your device. 
You can also use the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) to gather information that a network engineer uses when configuring the CPE device.
**Important** Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
## Supported Encryption Domain or Proxy ID
The values for the encryption domain (also known as a proxy ID, security parameter index (SPI), or traffic selector) depend on whether your CPE supports route-based tunnels or policy-based tunnels. For more information about the correct encryption domain values to use, see [Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#Supported_Encryption_Domain_or_Proxy_ID).
## Custom IKE and IPSec Parameters
When using custom internet key exchange (IKE) or IPSec parameters, if you select custom phase 1 proposals the CPE must be configured to accept the exact proposal. A mismatch prevents IKE from setting up the IPSec tunnel phase one security association.
For custom phase 2 IPSec proposals, expect the following behavior:
  * When Oracle initiates a new phase 2 IPSec security association, IKE only proposes the custom values.
  * When the CPE initiates a new phase 2 IPSec security association, the phase 2 security association is established as long as Oracle supports the parameters.


## Oracle IKE Initiation and IP Fragments 
The default set of Oracle IKE parameter proposals is too large to fit into a single UDP packet, so the Oracle end of the IPSec connection fragments the initiation request. To successfully initiate a new IKE security association, any firewall or security list between the Oracle VPN Public IP and the CPE must allow IP fragments.
## Supported Parameters for the Commercial Cloud 🔗 
This section lists the supported parameters if your Site-to-Site VPN is for the commercial cloud. For a list of the commercial cloud regions, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
For some parameters, Oracle supports multiple values, and the recommended one is noted.
Oracle supports the following parameters for IKEv1 or IKEv2. Check the documentation for your particular CPE to confirm which parameters the CPE supports for IKEv1 or IKEv2.
### Phase 1 (ISAKMP)
Parameter | Options  
---|---  
ISAKMP Protocol |  Version 1  
Exchange type |  Main mode  
Authentication method |  Pre-shared keys *  
Encryption algorithm |  **AES-256-CBC**(recommended) AES-192-CBC AES-128-CBC  
Authentication algorithm |  **SHA-2 384** (recommended) SHA-2 256 SHA-1 (also called SHA or SHA1-96) **   
Diffie-Hellman group |  group 2 (MODP 1024-bit) group 5 (MODP 1536-bit) group 14 (MODP 2048-bit) group 19 (ECP 256-bit random) **group 20 (ECP 384-bit random)** (recommended)  
IKE session key lifetime |  28800 seconds (8 hours)  
* Only numbers, letters, and spaces are allowed characters in pre-shared keys. ** Oracle strongly recommends against the use of SHA-1. NIST formally deprecated use of SHA-1 in 2011 and disallowed its use for digital signatures in 2013.  
### Phase 2 (IPSec)
Parameter | Options  
---|---  
IPSec Protocol |  ESP, tunnel mode  
Encryption algorithm |  **AES-256-GCM** (recommended) AES-192-GCM AES-128-GCM AES-256-CBC AES-192-CBC AES-128-CBC  
Authentication algorithm |  If using GCM, no authentication algorithm is required because authentication is included with GCM encryption. If not using GCM, the following options are supported: **HMAC-SHA-256-128** (recommended) HMAC-SHA1-128 *  
IPSec session key lifetime |  3600 seconds (1 hour)  
Perfect Forward Secrecy (PFS) |  **Enabled, group 5** (default, recommended) Supports disabled as well as enabled for group 2, 5, 14, 19, 20, 24.  
* Oracle strongly recommends against the use of SHA-1. NIST formally deprecated use of SHA-1 in 2011 and disallowed its use for digital signatures in 2013.  
## Supported Parameters for the Government Cloud 🔗 
This section lists the supported parameters if your Site-to-Site VPN is for the Government Cloud. For more information, see [For All US Government Cloud Customers](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm).
For some parameters, Oracle supports multiple values, and the recommended one is highlighted in **bold text**.
Oracle supports the following parameters for IKEv1 or IKEv2. Check the documentation for your particular CPE to confirm which parameters the CPE supports for IKEv1 or IKEv2.
### Phase 1 (ISAKMP)
Parameter | Options  
---|---  
ISAKMP protocol |  Version 1  
Exchange type |  Main mode  
Authentication method |  Pre-shared keys *  
Encryption algorithm |  **AES-256-CBC** (recommended) AES-192-CBC AES-128-CBC  
Authentication algorithm |  **SHA-2 384** (recommended) SHA-2 256 SHA-1 (also called SHA or SHA1-96)   
Diffie-Hellman group |  group 14 (MODP 2048) group 19 (ECP 256) **group 20 (ECP 384)** (recommended)  
IKE session key lifetime |  28800 seconds (8 hours)  
* Only numbers, letters, and spaces are allowed characters in pre-shared keys.  
### Phase 2 (IPSec)
Parameter | Options  
---|---  
IPSec protocol |  ESP, tunnel mode  
Encryption algorithm |  **AES-256-GCM** (recommended) AES-192-GCM AES-128-GCM AES-256-CBC AES-192-CBC AES-128-CBC  
Authentication algorithm |  If using GCM (Galois/Counter Mode), no authentication algorithm is required because authentication is included with GCM encryption. If not using GCM, use HMAC-SHA-256-128.  
IPSec session key lifetime |  3600 seconds (1 hour)  
Perfect Forward Secrecy (PFS) |  **Enabled, group 14** (default, recommended)  Supports disabled as well as enabled for group 2, 5, 14, 19, 20, 24.  
## References 🔗 
If you're not already familiar with the parameters mentioned previously, Links to relevant standards are provided in the following tables.
Option | Relevant Standard  
---|---  
Advanced Encryption Standard (AES)  | [FIPS PUB 197 standard](https://csrc.nist.gov/publications/detail/fips/197/final)  
Cipher Block Chaining (CBC) | [SP 800-38A standard](https://csrc.nist.gov/publications/detail/sp/800-38a/final)  
Secure Hash Algorithm (SHA) | [FIPS PUB 180-4 standard](https://csrc.nist.gov/publications/detail/fips/180/4/final)  
Diffie-Hellman (DH) groups |  [RFC 2631](https://tools.ietf.org/html/rfc2631): Diffie-Hellman Key Agreement Method [RFC 3526](https://tools.ietf.org/html/rfc3526): More Modular Exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE) [RFC 4306](https://tools.ietf.org/html/rfc4306): Internet Key Exchange (IKEv2) Protocol  
DH group type: Modular Exponential (MODP) or Elliptic Curve Prime (ECP) |  **MODP** [RFC 3526](https://tools.ietf.org/html/rfc3526): More Modular Exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE) **ECP** [RFC 5114](https://datatracker.ietf.org/doc/html/rfc5114): Additional Diffie-Hellman Groups for Use with IETF Standards  
Galois Counter Mode (GCM) |  [RFC 5288](https://datatracker.ietf.org/doc/html/rfc5288): AES Galois Counter Mode (GCM) Cipher Suites for TLS  
Perfect Forward Secrecy (PFS) | [RFC 2412](https://datatracker.ietf.org/doc/html/rfc2412): The OAKLEY Key Determination Protocol  
Was this article helpful?
YesNo

