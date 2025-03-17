Updated 2025-01-15
#  FastConnect Security
Learn about using encryption with FastConnect for better network security.
Oracle Cloud Infrastructure FastConnect allows two major methods to encrypt traffic between your data center and Oracle Cloud Infrastructure: [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) and [MACsec Encryption](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#macsec). 
## IPSec over FastConnect 🔗 
IPSec over FastConnect lets you set up Site-to-Site VPN with secure IPSec tunnels on FastConnect virtual circuits, thereby providing added security to what is already a private connection. These IPSec tunnels protect network-to-network connections on Layer 3. 
IPSec over FastConnect is available for all three connectivity models ([partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner."), [colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location."), and [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.")) and supports the following capabilities:
  * Multiple IPSec tunnels can exist over a single FastConnect virtual circuit.
  * A mix of encrypted and unencrypted traffic can exist on the same virtual circuit, though you can require that all traffic is encrypted. 
  * IPSec tunnel endpoints can use public or private IP addresses, but if the addresses are public they're not reachable over the internet because the transport for this connectivity is a private connection and not on the internet.
  * You can aggregate several IPSec tunnels between the same endpoints using ECMP.


### Configuring IPSec over FastConnect
**Note** We recommend that you use BGP route-based IPSec connections for IPSec over FastConnect.
Configuring both FastConnect and Site-to-Site VPN to work as a single data connection requires setting up components in a specific order. Presuming you already have at least one VCN and DRG in your cloud tenancy, create services in the following order: 
  1. Create a FastConnect virtual circuit, or choose an existing private virtual circuit. This virtual circuit can use any of the three FastConnect connectivity models. No change is required to new or existing private virtual circuits to enable IPSec over FastConnect, but you can edit the virtual circuit to only allow traffic that uses IPSec over FastConnect. The DRG uses different route tables set up for VIRTUAL_CIRCUIT attachments and IPSEC_TUNNEL attachments, because these attachments aren't able to share a DRG route table. 
  2. Create a new customer premises equipment (CPE) object. This object is a virtual representation of the physical edge device of an on-premises network. The CPE object must have IPSec over FastConnect enabled. After creating the CPE object, configure the physical edge device to match the CPE settings as normal for Site-to-Site VPN. The IP address used as the CPE IKE identifier can be either private or public. A previously configured CPE object can not be used for IPSec over FastConnect since the representation won't include the option to use IPSec over FastConnect. Of course, you can still use your existing CPE object for traffic that traverses the internet.
  3. Create a Site-to-Site VPN IPSec connection, selecting the new CPE you just created. BGP routing is preferred for connections that use IPSec over FastConnect, and you must specify the FastConnect virtual circuit you plan to use. 


### Loopback Attachments 🔗 
IPSec over FastConnect requires an [upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions), which can have attachments with the following types:
  * VCN
  * VIRTUAL_CIRCUIT
  * IPSEC_TUNNEL
  * REMOTE_PEERING_CONNECTION
  * LOOPBACK


A loopback attachment allows encrypted traffic to flow between a virtual circuit attachment and an IPSec tunnel attachment, by providing the Oracle side of the tunnel's private IP address to the DRG. Without the loopback attachment, traffic directly between a virtual circuit attachment and an IPSec tunnel attachment is not allowed. When traffic loops back through the IPSec tunnel attachment, it is decrypted and then sent to the DRG. Only virtual circuit attachments and IPSec tunnel attachments can route to a loopback attachment. All routing to or from a loopback attachment is managed by Oracle and can't be managed by your tenancy admins.
IPSec over FastConnect involves both a virtual circuit and an IPSec tunnel, and those connections must end on a DRG attachment with the corresponding type. As shown in the following simplified diagram for inbound traffic, with IPSec over FastConnect the IPSec tunnel originates from the CPE (Callout 1). The virtual circuit originates on an on-premises edge router (Callout 2), and ends on a VIRTUAL_CIRCUIT attachment (Callout 3). Then IPSec tunnel traffic passes to a LOOPBACK attachment (Callout 4) and ends on an IPSEC_TUNNEL attachment (Callout 5). Unencrypted traffic then passes through a VCN attachment (Callout 6) and out to the final destination IP address in the VCN. The traffic could alternatively route to a REMOTE_PEERING_CONNECTION attachment bound to another DRG in the same region or another region, but that isn't shown in the diagram.
![Diagram showing the termination ends of both virtual circuit and IPSec tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_loopback.svg)
Callout | Function  
---|---  
1 | CPE device. Terminates the IPSec connection.  
2 | Edge router. Terminates the virtual circuit.**Note:** Callout 1 and 2 can potentially be the same physical device.  
3 | VIRTUAL_CIRCUIT attachment. Terminates the virtual circuit.  
4 | LOOPBACK attachment. Forwards IPSec traffic to IPSEC_TUNNEL attachment. This is also the VPN endpoint IP.  
5 | IPSEC_TUNNEL attachment. Terminates the IPSec connection.  
6 | VCN attachment  
**Note** When using IPSec over FastConnect, the IPSec tunnel attachment (Callout 5) and the virtual circuit attachment (Callout 3) must use different DRG route tables and import route distributions.
### TransportOnly Mode: Only Allowing Encrypted Traffic on a Virtual Circuit 🔗 
IPSec over FastConnect lets a FastConnect virtual circuit act as a transport medium for encrypted traffic on a private IPSec tunnel, allowing connectivity from an on-premises network into the VCN for both secured and unsecured traffic. 
If you want a strict security posture that only allows encrypted traffic over your virtual circuits, set the `transportOnly` mode flag on your virtual circuit and the virtual circuit's DRG attachment (in the Console, set the **IPSec over FastConnect traffic only** option, either when you create the virtual circuit or later on). 
Before you try to set the `transportOnly` mode flag: 
  1. Remove all static rules from the "Autogenerated Drg Route Table for RPC, VC, and IPSec attachments" route table, or whichever route table is currently the default for virtual circuit attachments. By default, the associated import route distribution for the autogenerated route table is the"Autogenerated Import Route Distribution for VCN Routes."
  2. Remove all route distribution statements from the "Autogenerated Import Route Distribution for VCN Routes" (or the manually created import route distribution associated with a custom route table for virtual circuits) that have a "Match attachment type Virtual Circuit" or "Match ALL" setting. 


If you attempt to enable `transportOnly` mode on a DRG that doesn't meet these requirements, you should get a detailed error message describing what settings need to be adjusted. After you make the required changes to your DRG, you will be able to set the virtual circuit and its attachment to `transportOnly` mode. After you set the `transportOnly` mode flag, Oracle enforces the following behaviors on your DRG's route tables and import route distributions: 
  1. The virtual circuit attachment's route table only allows a single route towards each of its associated loopback attachments and no other routes. 
  2. The virtual circuit attachment's route table can't have any static routes.
  3. The import route distribution of the route table associated with the virtual circuit attachment can only import routes from the loopback DRG attachments.
  4. None of the attachments in the DRG can import routes from the virtual circuit attachment except the loopback attachment. This means that no import route distribution for any other attachment can have a generic "Match ALL" or "Match attachment type - Virtual Circuit" setting. 


Any further changes to the import route distribution or changes to static route rules on this DRG will be validated to enforce the necessary routing behaviors.
## MACsec Encryption 🔗 
You can configure FastConnect to use **MACsec** (IEEE standard 802.1AE) to protect network-to-network connections on Layer 2. To enable MACsec, choose an advanced encryption standard (AES) encryption algorithm. The two connected networks exchange and verify security keys, and then establish a secure bidirectional link. The Oracle Cloud Infrastructure Vault service securely stores the actual encryption keys. 
Using MACsec has the following requirements:
  * Your customer premises equipment (CPE) device must also support MACsec.
  * The FastConnect selected port speed for single cross-connects or cross-connect groups must be 10 Gbps or greater.
  * Not all existing cross-connect or cross-connect group can support MACsec. To upgrade an existing cross-connect or cross-connect group, the details page for the cross-connect or cross-connect group has a **MACsec Encryption** field with settings for either **Capable** or **Incapable**. The connection must be capable of using MACsec. If the cross-connect or cross-connect group is Incapable of using MACsec, you need to reprovision before configuring MACsec.
  * Not all third-party providers can support MACsec on the type of circuit they provide. Please check with your provider to verify that the type of connectivity you purchase supports MACsec.


FastConnect with MACsec integrates with the Vault service. Here's an overview of the steps to fully configure FastConnect with MACsec. 
  1. [Create a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm). 
  2. [Create a master encryption key ](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm) in Vault. 
  3. [Create two secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm) to represent the Connectivity Association Key (CAK) and Connectivity association Key Name (CKN) in your Vault. The CAK and CKN must be hexadecimal strings with a length of 32–64 characters. 
  4. Configure MACsec in a [Third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_cc__macsec) or [colocation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#task_set_up_cc__macsec) cross-connect using the CKN and CAK secrets created for the FastConnect circuit.
  5. Give your on-premises network administrator the original CAK and CKN keys to use when configuring the customer premises equipment (CPE) device.
  6. Activate the cross-connects for the [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_activate_cc) or [colocation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#task_activate_cc) virtual circuits.


If you decide to add MACsec encryption to an existing FastConnect cross-connect, remember that changing the encryption settings requires restarting the BGP session, which briefly suspends BGP traffic. 
### MACsec Parameters
When configuring MACsec on your CPE, refer to the table for various required parameters.
Parameter | Possible Values  | Description  
---|---|---  
CAK | 32-64 hexadecimal characters | Minimum of 32 hexadecimal characters (0-9, A-F).  
Cipher Suites |  aes128-gcm-xpn aes256-gcm-xpn | Configure your CPE to match the cipher suite configured in OCI.  
CKN | 32-64 hexadecimal characters | Minimum of 32 hexadecimal characters (0-9, A-F).  
Confidentiality Offset | 0 | The OCI side is always 0, meaning the whole frame is encrypted. If required as part of your CPE configuration, match the OCI side.  
Interface |  Single physical interface link aggregation group (LAG) | MACsec for FastConnect supports configuration of MACsec on either a single FastConnect connection or a LAG. Match this configuration option on your CPE.  
Key-server | 1 or higher | Use any value higher than 0 on your CPE. The OCI FastConnect edge device always uses 0.  
MKA Include SCI | include SCI | Configure your CPE to include an SCI (Secure Channel Identifier) tag. Configure the "Include SCI" tag on the OCI side.  
MKA Policy Option |  must-secure | This requires that all traffic sent on the MACsec-enabled network segment is secure (the Fail Close option in the Console). Match this configuration option on your CPE. The `should-secure` option (the Fail Open option in the Console) is available but is not recommended by Oracle.  
SAK Rekey time | 3600 seconds (1 hour) | CPE configuration must match the OCI SAK rekey time of 1 hour.  
### MACsec Hitless Key Rollover 🔗 
When you're ready to rotate your keys, MACsec for FastConnect supports hitless key rollover. To ensure no loss in communication when rotating keys, always update both the CKN and CAK at the same time. Change the CKN and CAK pair on the OCI side of the FastConnect link first, and then update your CPE. 
Perform the following tasks in the order described. Doing these steps out of order might result in a temporary disruption in communication.
[Task 1: Update the CKN and CAK Pair](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm)
  1. Open the **navigation menu** , select ****Identity & Security****, and then select ****Vault****.
  2. Choose a compartment that you have permission to work in (on the left side of the page). The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
  3. Click the name of the Vault that includes your CKN and CAK secrets.
  4. Under **Resources** , click **Secrets**.
  5. Click the name of the secret that represents your CKN.
  6. Click **Create Secret Version**.
  7. Under **Secret Contents** , enter the new value for your CKN.
  8. Click **Create Secret Version**.


Repeat these steps to also change the value of your CAK secret.
When performing hitless key rollover, always update both the CKN and CAK.
[Task 2: Update the Cross-Connect CKN and CAK Secret Versions](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **FastConnect**.
  2. Click the name of the FastConnect that uses the Vault secrets modified in Task 1. You see the cross-connect representing your FastConnect.
  3. Click **Edit**.
  4. Under **Connectivity Association Key Name (CKN)** select **Use current version in Vault: <number>** where <number> matches the latest secret version of your CKN secret in the Vault.
  5. Under **Connectivity Association Key (CAK)** select **Use current version in Vault: <number>** where <number> matches the latest secret version of your CAK secret in the Vault. 
  6. After both CKN and CAK versions update, click **Save Changes**.
  7. A new pop-up appears to confirm changes. Click **Confirm**.


After the cross-connect updates to use the new CKN and CAK values, you have a 1 hour rekey period to update the CKN and CAK on your CPE before the session drops.
[Task 3: Update the CKN and CAK on Your CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm)
After the cross-connect updates to use the new CKN and CAK values, you have a 1 hour rekey period to update the CKN and CAK on your CPE before the session drops. Refer to the appropriate documentation for your device.
Was this article helpful?
YesNo

