Updated 2025-01-15
# VPN Connection to Google
The Oracle Cloud Infrastructure (OCI) Site-to-Site VPN service offers a secure IPSec connection between an on-premises network and a Virtual Cloud Network (VCN). You can also use Site-to-Site VPN to connect OCI resources to other cloud service providers.
This topic provides a best practices configuration for an IPSec VPN tunnel between OCI and Google Cloud Platform (GCP) using the OCI Site-to-Site VPN service and the Google Cloud VPN service.
**Note** This document assumes you have already provisioned a VCN and [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) and also configured all [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) required for this scenario and all equivalents in Google Cloud.
## Considerations specific to GCP
**Routing Type:** This scenario uses Border Gateway Protocol (BGP) to exchange routes between GCP and OCI. BGP is preferred for Site-to-Site VPN whenever possible. Optionally, static routing can also be used between GCP and OCI.
## Verify OCI Site-to-Site VPN Version
You can verify the Site-to-Site VPN version used by your IPSec connection under the **IPSec Connection Information** tab on an IPSec connection page.
## Supported IPSec Parameters
For a vendor-neutral list of supported IPSec parameters for all OCI regions, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
## Configuration Process
[GCP - Start VPN Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
  1. From the main Google Cloud portal: 
    1. Expand the main menu from the top-left corner
    2. Scroll down to **Hybrid Connectivity**
    3. Click **VPN**
  2. On the next page, click the **Create VPN Connection** link to initiate the workflow to create a IPSec VPN connection.
  3. For **VPN Options** , select **High-availability (HA) VPN** then click the **Continue** button at the bottom.
  4. Create a Cloud HA VPN gateway. Enter the following details: 
     * **Name:** Give your VPN gateway a name.
     * **Network:** Select the VPC that your IPSec VPN connects to.
     * **Region:** Select the region for your VPN gateway
When you are finished configuring your VPN gateway, click the **Create & Continue** button to continue.
  5. The next page will expose the public IP of the GCP VPN endpoint.
Save the public IP of one of the interfaces, then open the OCI console in a separate window and continue the configuration process. You return later to complete the GCP configuration after the OCI IPSec connection as been provisioned.


[OCI - Create CPE Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Click **Create Customer-Premises Equipment**.
  3. Enter the following values:
     * **Create in Compartment:** select the compartment for the VCN you want.
     * **Name:** A descriptive name for the CPE object. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
This example uses "TO_GCP" as the name.
     * **IP Address:** Enter the public IP address of the GCP VPN gateway.
     * **CPE Vendor:** Select **Other**.
  4. Click **Create CPE**.


[OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier, named TO_GCP.
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Static Route CIDR:** Enter a default route, 0.0.0.0/0. Since BGP is used for the active tunnel, OCI ignores this route. This entry is required for the second tunnel of the IPSec connection which by default uses static routing and is unused in this scenario. If you plan to use static routing for this connection, input static routes representing your GCP virtual networks. Up to 10 static routes can be configured for each IPSec connection. 
     * Ensure that OCI supports the chosen /30 address for the inside tunnel IPs. OCI does not allow you to use the following IP ranges for inside tunnel IPs:
       * 169.254.10.0-169.254.19.255
       * 169.254.100.0-169.254.109.255
       * 169.254.192.0-169.254.201.255
  4. Enter the following details on the **Tunnel 1** tab (required):
     * **Name:** Enter a descriptive name for the tunnel (Example: GCP-TUNNEL-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret:** The pre-shared key used by IPSec for this tunnel. Select this checkbox if you would like to use a custom key. If left unselected one is generated for you. 
     * **IKE Version:** Select IKEv2.
     * **Routing Type:** Select **BGP Dynamic Routing**. Select **Static Routing** if you would like to use static routing.
     * **BGP ASN:** Input the BGP ASN used by GCP. The GCP BGP ASN is configured in future steps. This scenario uses a BGP ASN of 65000 for GCP.
     * **IPv4 Inside Tunnel Interface - CPE:** Enter the BGP IP address used by GCP. Use full CIDR notation for this IP address. This must be a link local address. This scenario uses the 169.254.20.0/30 CIDR for the BGP IP addresses.
     * **IPv4 Inside Tunnel Interface - Oracle:** Enter the BGP IP address used by OCI. Include this IP address in CIDR notation. This must be a link local address. This scenario uses the 169.254.20.0/30 CIDR for the BGP IP addresses.
  5. Click **Show advanced options** for the tunnel and modify the Phase 1 and Phase 2 lifetimes to match the GCP side as listed here <https://cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers>. 
Phase 1 and Phase 2 lifetimes will be different values on the GCP side depending on if you're using IKEv1 or IKEv2. These will be: 
     * Phase 1 IKE session key lifetime in seconds = 36,000 seconds
     * Phase 2 IPSec session key lifetime in seconds = 10,800 seconds
Leave all other settings at their default.
  6. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. The connection is in the Provisioning state for a short period.


[OCI - Save Oracle VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
After your IPSec connection has been provisioned, save the Site-to-Site VPN IP address to use as the CPE IP in the GCP portal and the shared secret for the tunnel.
  1. Browse to your IPSec connection in the OCI Console.
Choose which tunnel to use as your primary. Save the Site-to-Site VPN IP address of that tunnel. Next, click the tunnel name of that tunnel to be taken to the tunnel view.
  2. Under the tunnel, select the link to view the shared secret. Save it. The shared secret is used to complete the IPSec VPN configuration in GCP.


[GCP - Create a VPN Peer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
  1. Return to the GCP VPN configuration window.
  2. Under **Peer VPN Gateway** , select **On-prem or Non Google Cloud**.
  3. Expand the **Peer VPN gateway name** list and select **Create new VPN peer gateway**. 
  4. You are taken to the **Add a peer VPN gateway** page. Enter the following details:
     * **Name:** Give your peer VPN gateway a name.
     * **Interfaces:** Select **one interface**.
     * **Interface 0 IP address:** Input the Oracle VPN IP address here. This IP address was saved in [OCI - Save Oracle VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_save_oracle_vpn_ip_address_and_shared_secret).
  5. Click the **Create** button at the bottom to continue. You are taken back to the **Create a VPN** workflow.


[GCP - Create a Cloud Router](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
  1. Expand the **Cloud Router** list and select **Create new router**. 
  2. You are taken to the **Create a router** page. Enter the following details: 
     * **Name:** Give your cloud router a name.
     * **Google ASN:** Input the Google BGP ASN, also used when configuring the IPSec connection in OCI.
Leave all other options as default.
  3. When you are finished configuring your cloud router, click the **Create** button to continue. 
You are taken back to the **Create a VPN** workflow.


[GCP - Complete configuring VPN Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
Complete configuring your VPN tunnel. Enter the following details:
  * **Cloud Router:** Select the cloud router that was configured in the previous step.
  * **Associated Cloud VPN gateway IP:** Match the CPE object IP address configured in OCI.
  * **Associated peer VPN Gateway interface:** Match the Oracle VPN IP address of your OCI VPN tunnel. Refer to [OCI - Save Oracle VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_save_oracle_vpn_ip_address_and_shared_secret).
  * **Name:** Give your VPN tunnel a name.
  * **IKE version:** Select IKEv2 (recommended). If using IKEv1, ensure IKEv1 is also configured for the VPN tunnel under your IPSec connection in OCI.
  * **IKE pre-shared key:** Match the shared secret of the VPN tunnel in your IPSec connection in OCI. Refer to [OCI - Save Oracle VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_save_oracle_vpn_ip_address_and_shared_secret). Leave all other options as default.
When you finish configuring your VPN tunnel, click **Create & Continue**.


[GCP - Configure BGP Sessions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
This step involves configuring the BGP session for your IPSec tunnel. The BGP settings need to match the OCI side of the configuration configured in [OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_create_ipsec_connection).
  1. Click the **Configure** button under BGP Session for your VPN tunnel.
  2. You are taken to the **Create BGP Session** page for your tunnel. Enter the following details: 
     * **Name:** Give your BGP session a name.
     * **Peer ASN:** Enter the BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
     * **Cloud Router BGP IP:** Match the IP address configured for **IPV4 Inside Tunnel Interface - CPE** of tunnel 1 in [OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_create_ipsec_connection). Do not use CIDR notation in this field.
     * **BGP peer IP:** Match the IP address configured for **IPV4 Inside Tunnel Interface - Oracle** of tunnel 1 in [OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm#vpn_to_gcp_oci_create_ipsec_connection). Do not use CIDR notation in this field.
     * **BGP peer:** Select **Enabled**.
Leave all other options as default.
  3. When you are finished configuring your BGP session, click **Save & Continue** to go back to the **Configure BGP sessions** page.
  4. Click the **Save BGP configuration** button to continue.
  5. You are taken to the **Summary and reminder** page.
The **VPN tunnel status** and **BGP status** displays as "established."
  6. Click **OK** at the bottom to complete the configuration.


[Verification](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_gcp.htm)
Browse to your IPSec connection in OCI and the Site-to-Site VPN connections in GCP to verify status of the tunnel. 
Your OCI tunnel under IPSec connection displays **Up** for IPSec status to confirm an operational tunnel.
The IPV4 BGP Status also displays **Up** indicating an established BGP session.
Browse to your cloud VPN tunnels in the GCP console. Both VPN tunnel status and BGP session status should indicate **Established**.
A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from OCI to actively and passively monitor your cloud resources. For information about monitoring your OCI Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics) .
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

