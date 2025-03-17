Updated 2025-01-15
# VPN Connection to Azure
The Oracle Cloud Infrastructure (OCI) Site-to-Site VPN service offers a secure IPSec connection between your on-premises network and a virtual cloud network (VCN). You can also use Site-to-Site VPN to connect OCI resources to other cloud service providers.
This topic provides a best practices configuration for an IPSec VPN tunnel between OCI and Microsoft Azure using the OCI Site-to-Site VPN service and the Azure IPSec VPN service.
**Note** This document assumes you have already provisioned a [Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI.") and [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) as well as configured all [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) required for this scenario and all equivalents in Azure.
## Considerations specific to Microsoft Azure
**IKE Version:** An IPSec VPN connection between OCI and Microsoft Azure must use IKE version 2 for interoperability.
**Routing Type:** This scenario uses Border Gateway Protocol (BGP) to exchange routes between Azure and OCI. BGP is preferred for Site-to-Site VPN whenever possible. Optionally, static routing can also be used between Azure and OCI.
**Perfect Forward Secrecy:** With perfect forward secrecy (PFS) new Diffie-Hellman keys are generated in phase 2, and phase 2 rekeys instead of using the same key generated during phase 1. Both VPN peers must match the chosen PFS group setting for phase 2. By default, Azure (groups 1, 2, 14, and 24 for IKEv2 only) and OCI (group 5) have a PFS mismatch. The OCI side PFS group can be modified to match your CPE.
## Verify OCI Site-to-Site VPN Version
You can verify the Site-to-Site VPN version used by the IPSec connection under the **IPSec Connection Information** tab on your IPSec connection page.
## Supported IPSec Parameters
For a vendor-neutral list of supported IPSec parameters for all OCI regions, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
## Configuration Process
[Azure - Create VPN Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
  1. From the main Azure portal, search for **Virtual Network Gateway**. Select it from the search results.
  2. On the next page, click the **Create** button to create a new Virtual Network Gateway.
  3. You are taken to the **Create Virtual Network Gateway** page.
     * **Name:** Give your gateway a name.
     * **Region:** Select your Azure region. The region must be the same as your virtual network.
     * **Gateway Type:** Select **VPN**.
     * **VPN type:** Select **Route-based**.
     * **SKU** and **Generation:** Select a gateway SKU that supports IKEv2 and meets your throughput requirements. For more information on gateway SKUs, see the Azure documentation on [VPN Gateways](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-about-vpngateways#gwsku).
     * **Virtual network:** Choose the virtual network for your gateway. This virtual network also needs a gateway subnet.
     * **Gateway subnet address range:** If your virtual network already has a **GatewaySubnet** , select it. Otherwise, choose an unused address range.
     * **Public IP address:** Your Virtual Network Gateway needs a public IP address. If one has already been created, select it. Otherwise, choose **Create new** and give your Public IP address a name.
     * **Enable active-active mode:** Leave this option disabled.
     * **Configure BGP:** Select **Enabled**. Leave this option as disabled if you want to use static routing.
     * **Autonomous system number (ASN):** By default Azure uses BGP ASN 65515. Choose the default.
     * **Custom Azure APIPA BGP IP address:** Select a /30 subnet from within 169.254.21.0/24 or 169.254.22.0/24. These addresses are your BGP IP addresses for Azure and OCI. Enter one of the two available IPs from the chosen /30 here. This scenario uses 169.254.21.1 for OCI and 169.254.21.2 for Azure.
When you are finished configuring your Virtual Network Gateway, click the **Review + create** button, then the **Create** button on the following page.
  4. Browse to your newly created Virtual Network Gateway and save the public IP address. The IP address is used to create the IPSec connection in OCI.


[OCI - Create CPE Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Click **Create Customer-Premises Equipment**.
  3. Enter the following values:
     * **Create in Compartment:** select the compartment for the VCN you want.
     * **Name:** A descriptive name for the CPE object. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
This example uses "TO_Azure" as the name.
     * **IP Address:** Enter the public IP of your Azure Virtual Network Gateway. You can find this public IP in the Azure console by browsing to the overview page of the Virtual Network Gateway created in the previous task.
     * **CPE Vendor:** Select **Other**.
  4. Click **Create CPE**.


[OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** Enter a descriptive name for the IPSec connection. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier, named TO_Azure.
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Static Route CIDR:** input a default route, 0.0.0.0/0. Since BGP is used for the active tunnel, OCI ignores this route. This entry is required for the second tunnel of the IPSec connection which by default uses static routing and is unused in this scenario. If you plan to use static routing for this connection, input static routes representing your Azure virtual networks. Up to 10 static routes can be configured for each IPSec connection. 
  4. Enter the following details on the **Tunnel 1** tab (required):
     * **Name:** Enter a descriptive name for the tunnel (Example: Azure-TUNNEL-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret:** The pre-shared key used by IPSec for this tunnel. Select this checkbox if you would like to use a custom key. If left unselected one is generated for you. 
     * **IKE Version:** Select IKEv2.
     * **Routing Type:** Select **BGP Dynamic Routing**. Select **Static Routing** if you would like to use static routing.
     * **BGP ASN:** Input the BGP ASN used by Azure. The Azure BGP ASN is configured during Step 3 of section _Azure - Create VPN Gateway_. This scenario uses the default Azure BGP ASN of 65515.
     * **IPv4 Inside Tunnel Interface - CPE:** The BGP IP address used by Azure. Use full CIDR notation for this IP address. The Azure BGP IP address is configured during Step 3 of section _Azure - Create VPN Gateway_.
     * **IPv4 Inside Tunnel Interface - Oracle:** The BGP IP address used by OCI. Use full CIDR notation for this IP address. This IP address is the other leftover usable IP from the chosen /30. 
  5. Click **Show advanced options** and Expand **Phase Two (IPSec) Configuration**. Select a perfect forward secrecy Diffie-Hellman group. Chose from GROUP2, GROUP14, or GROUP24.
  6. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. The connection is in the Provisioning state for a short period.


[OCI - Change PFS](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
By default, OCI Site-to-Site VPN uses PFS group 5 for all IPSec VPN tunnels. For IKEv2, Azure sends proposals with PFS groups 1, 2, 14, and 24. 
You can use the OCI Console to set a tunnel's Phase 2 IPSec policy to use a custom PFS group value of 2, 14, or 24. OCI does not support PFS group 1.
[OCI - Save Site-to-Site VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
After your IPSec connection has been provisioned, save the Site-to-Site VPN IP address to use as the CPE IP in the Azure portal and the shared secret for the tunnel.
  1. Browse to your IPSec connection in the OCI Console.
Choose which tunnel to use as your primary. Save the Site-to-Site VPN IP address of that tunnel. Next, click the tunnel name of that tunnel to be taken to the tunnel view.
  2. Under the tunnel, select the link to view the shared secret. Save it. The shared secret is used to complete the IPSec VPN configuration in Azure.


[Azure - Create Local Network Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
  1. From the main Azure portal, search for **Local Network Gateway**. Select it from the search results.
  2. On the next page, click the **Create** button to create a Local Network Gateway.
  3. You are taken to the **Create Local Network Gateway** page. Enter the following details: 
     * **Region:** Select your Azure region. The region must be the same as your virtual network and Virtual Network Gateway.
     * **Name:** Give your local network gateway a name.
     * **IP Address:** Input the saved OCI VPN IP address for Tunnel 1. 
     * **Address space:** Leave blank if you're using static routing input the CIDRs of your OCI VCNs.
     * **Configure BGP Settings:** Select this checkbox. If using static routing, leave the option unselected.
     * **Autonomous system number (ASN):** Input the OCI BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
     * **BGP peer IP address:** The OCI BGP IP address. The same IP address used for**IPV4 Inside Tunnel Interface - Oracle** in Step 4 of [OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm#vpn_to_azure_oci_create_ipsec_connection).


[Azure - Create a VPN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
  1. Browse to your previously created Virtual Network Gateway. From the left-hand menu, click **Connections** , then the **Add** button to add a connection.
  2. You are taken to the **Add Connection** page. Enter the following details: 
     * **Name:** Give your connection a name.
     * **Connection type:** Select **Site-to-site (IPsec)**
     * **Local network gateway:** Select the previously created local network gateway.
     * **Shared key (PSK)** - Input the shared secret from your OCI tunnel. Refer to [OCI - Save Site-to-Site VPN IP Address and Shared Secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm#vpn_to_azure_oci_save_oracle_vpn_ip_address_and_shared_secret) if you need to identify where the shared key is found in the OCI Console.
     * **Enable BGP:** Select this checkbox. Leave unselected if using static routing.
     * **IKE Protocol:** Select IKEv2
Leave all other options as default. When you are finished configuring your VPN connection, click the **OK** button at the bottom of the page.
After a couple minutes, Azure will complete provisioning the new VPN connection and your IPSec VPN between Azure and OCI will come up.


[Verification](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_azure.htm)
Browse to your IPSec connection in OCI and the Virtual Network Gateway connection in Azure to verify status of the tunnel. 
Your OCI tunnel under IPSec connection displays **Up** for IPSec status to confirm an operational tunnel.
The IPV4 BGP Status also displays **Up** indicating an established BGP session.
The connection status under the Virtual Network Gateway for this tunnel displays **Connected** to confirm an operational tunnel.
A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from OCI to actively and passively monitor your cloud resources. For information about monitoring your OCI Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics) .
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

