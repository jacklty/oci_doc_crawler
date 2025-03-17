Updated 2025-01-15
# VPN Connection to AWS
The Oracle Cloud Infrastructure (OCI) Site-to-Site VPN service offers a secure IPSec connection between an on-premises network and a Virtual Cloud Network (VCN). You can also use Site-to-Site VPN to connect Oracle Cloud Infrastructure resources to other cloud service providers.
This topic provides a best practices configuration for an IPSec VPN tunnel between OCI and AWS using the OCI Site-to-Site VPN service and the AWS Site-to-Site VPN service.
**Note** This document assumes you have already provisioned a [Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI.") and [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) and also configured all [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) required for this scenario and all equivalents in AWS.
## Considerations specific to AWS
**Pre-Shared Key:** If you rely on AWS to auto generate a pre-shared key for a tunnel, the generated key might contain period or underscore (. or _ ) characters. OCI doesn't support these characters in a pre-shared key. If the AWS auto generated password contains these characters, change the pre-shared key for the relevant tunnel before completing the VPN configuration.
**Routing Type:** This scenario uses Border Gateway Protocol (BGP) to exchange routes between AWS and OCI. Use BGP for IPSec tunnels whenever possible. Optionally, static routing can also be used between AWS and OCI.
## Verify OCI Site-to-Site VPN Version
You can verify the Site-to-Site VPN version used by your IPSec connection under the **IPSec Connection Information** tab on an IPSec connection page.
## Supported IPSec Parameters
For a vendor-neutral list of supported IPSec parameters for all OCI regions, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
## Configuration Process
[AWS - Create Temporary Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
The first step in the configuration process is to create a temporary customer gateway. This temporary customer gateway is used to initially provision the AWS Site-to-Site VPN, exposing the AWS VPN endpoint for your tunnel. OCI requires the public IP of the remote VPN peer before creating a IPSec connection. After this process has been completed, a new customer gateway is configured representing the actual OCI VPN endpoint public IP. 
  1. From the main AWS portal, expand the **Services** menu at the top left of the screen. Browse to **VPC** under **Networking & Content Delivery**.
  2. From the left-hand menu, scroll down and click **Customer Gateways** under **Virtual Private Network** **(VPN)**.
  3. Click **Create Customer Gateway** to create a Customer Gateway.
  4. You are taken to the **Create Customer Gateway** page. Enter the following details:
     * **Name:** Give this customer gateway an obviously temporary name. In this example, the name **TempGateway** is used.
     * **Routing:** Select **Dynamic**.
     * **BGP ASN:** Enter the OCI BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
     * **IP Address:** Use any valid IPv4 address for the temporary gateway. This example uses 1.1.1.1.
When you are finished configuring your temporary customer gateway, click **Create Customer Gateway** to complete provisioning.


[AWS - Create and Attach Virtual Private Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
  1. From the AWS left-hand menu, scroll down and click **Virtual Private Gateways** under **Virtual Private Network** **(VPN)**.
  2. Click the **Create Virtual Private Gateway** button to create a new virtual private gateway.
  3. You are taken to the **Create Virtual Private Gateway** page. Enter the following details:
     * **Name:** Give your Virtual Private Gateway (VPG) a name.
     * **ASN:** Select **Amazon default ASN**.
When you are finished configuring your virtual private gateway, click the **Create Virtual Private Gateway** button to complete provisioning.
  4. After the VPG has been created, you need to attach it to your VPC of choice.
While still on the Virtual Private Gateway page, ensure that your VPG is selected, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then **Attach to VPC**.
  5. You are taken to the **Attach to VPC** page for your selected Virtual Private Gateway.
Select your VPC from the list, then click the **Yes, Attach** button to complete attaching your VPG to your VPC.


[AWS - Create VPN Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
  1. From the left-hand menu, scroll down and click **Site-to-Site VPN Connections** under **Virtual Private Network (VPN)**.
  2. Click **Create VPN Connection** to create a new virtual private gateway.
  3. You are taken to the **Create VPN Connection** page. Enter the following details: 
     * **Name tag:** Give your VPN connection a name.
     * **Target Gateway Type:** Select **Virtual Private Gateway** , then select the previously created Virtual Private Gateway from the list.
     * **Customer Gateway:** Select **Existing** , then select the temporary Customer Gateway from the list.
     * **Routing Options:** Select **Dynamic (requires BGP)**.
     * **Tunnel inside Ip Version:** Select **IPv4**.
     * **Local/Remote IPv4 Network Cidr:** Leave both of these fields blank, creating an any/any route-based IPSec VPN.
Proceed to the next step. **DO NOT** click the **Create VPN Connection** button yet.
  4. While still on the **Create VPN Connection** page, scroll down to **Tunnel Options**.
Choose a /30 CIDR from within the link local 169.254.0.0/16 range. Input the full CIDR in the **Inside IPv4 CIDR for Tunnel 1** field. 
Ensure that OCI supports the chosen /30 address for the inside tunnel IPs. OCI does not allow you to use the following IP ranges for inside tunnel IPs:
     * 169.254.10.0-169.254.19.255
     * 169.254.100.0-169.254.109.255
     * 169.254.192.0-169.254.201.255
Proceed to the next step. **DO NOT** click the **Create VPN Connection** button yet.
  5. Under **Advanced Options for Tunnel 1** , click the radio button for **Edit Tunnel 1 Options**. An extra set of options expands.
If you would like to be restrictive with the cryptography algorithms used for this tunnel, configure the wanted Phase 1 and Phase 2 options here. Oracle recommends using IKEv2 for this connection. Disable the IKEv1 checkbox to prevent IKEv1 from being used. To refer to what Phase 1 and Phase 2 options OCI supports, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
After you have finished configuring all wanted options, click the **Create VPN Connection** button at the bottom to finish provisioning your VPN connection.


[AWS - Download Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
While your VPN connection is provisioning, download the configuration of all tunnel information. This text file is required to complete configuring the tunnel in the OCI Console.
  1. Ensure that your VPN connection is selected, then click the **Download Configuration** button.
  2. Select the **Vendor** and **Platform** setting "Generic" then click the **Download** button to save a text copy of the configuration to your local hard drive. 
  3. Open the downloaded configuration file in your text editor of choice.
Look under **IPSec Tunnel #1** , section **#1 Internet Key Exchange Configuration**. Here you find your automatically generated pre-shared key for your tunnel. Save this value.
AWS might generate a pre-shared key using the period or underscore characters (. or _). OCI does not support using those characters in a pre-shared key. A key that includes these values must be changed. To change your pre-shared key in AWS for a tunnel, select your VPN connection, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), then **Modify VPN Tunnel Options**. 
  4. While still under Tunnel 1 in the downloaded configuration, scroll down to section **#3 Tunnel Interface Configuration**.
Note down the following values to complete the Site-to-Site VPN configuration in OCI:
     * Outside IP address of the Virtual Private Gateway
     * Inside IP for the Customer Gateway
     * Inside IP for the Virtual Private Gateway
     * Virtual Private Gateway BGP ASN. The default ASN is 64512.


[OCI - Create CPE Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Click **Create Customer-Premises Equipment**.
  3. Enter the following values:
     * **Create in Compartment:** select the compartment for the VCN you want.
     * **Name:** A descriptive name for the CPE object. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
This example uses "TO_AWS" as the name.
     * **IP Address:** Enter the outside IP address of the Virtual Private Gateway shown in the configuration downloaded from AWS.
     * **CPE Vendor:** Select **Other**.
  4. Click **Create CPE**.


[OCI - Create IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. Click **Create IPSec Connection**.
  3. Enter the following values:
     * **Create in Compartment:** Leave as is (the VCN's compartment).
     * **Name:** Enter a descriptive name for the IPSec connection (Example: OCI-AWS-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Customer-Premises Equipment Compartment:** Leave as is (the VCN's compartment).
     * **Customer-Premises Equipment:** Select the CPE object that you created earlier, named TO_AWS.
     * **Dynamic Routing Gateway Compartment:** Leave as is (the VCN's compartment).
     * **Dynamic Routing Gateway:** Select the DRG that you created earlier.
     * **Static Route CIDR:** Enter a default route, 0.0.0.0/0. Since the active tunnel uses BGP, OCI ignores this route. An entry is required for the second tunnel of the IPSec connection, which by default uses static routing, but the address not used in this scenario. If you plan to use static routing for this connection, input static routes representing your AWS virtual networks. Up to 10 static routes can be configured for each IPSec connection.
  4. Enter the following details on the **Tunnel 1** tab (required):
     * **Name:** Enter a descriptive name for the tunnel (Example: AWS-TUNNEL-1). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Provide custom shared secret:** Enter the pre-shared key used by IPSec for this tunnel. Select this checkbox and input the pre-shared key from the AWS VPN configuration file. 
     * **IKE Version:** Select IKEv2. 
     * **Routing Type:** Select **BGP Dynamic Routing**.
     * **BGP ASN:** Input the BGP ASN used by AWS as found in the AWS VPN configuration file. The default AWS BGP ASN is 64512.
     * **IPv4 Inside Tunnel Interface - CPE:** Enter the Virtual Private Gateway inside IP address from the AWS VPN configuration file. Use full CIDR notation for this IP address.
     * **IPv4 Inside Tunnel Interface - Oracle:** Enter the inside IP address used by OCI. Referring to the AWS VPN configuration file, enter the inside IP address for the Customer Gateway. Use full CIDR notation for this IP address.
  5. Click **Create IPSec Connection**.
The IPSec connection is created and displayed on the page. the connection is in the Provisioning state for a short period.
  6. After your IPSec connection is provisioned, make note of the **Oracle VPN IP Address** of your tunnel. This address will be used to create a new customer gateway in the AWS portal.
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
    2. Click the IPSec connection you're interested in (Example: OCI-AWS-1).
    3. Find the **Oracle VPN IP Address** of AWS-TUNNEL-1. 


[AWS - Create New Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
In the AWS console, browse to Customer Gateways and create a Customer Gateway using the following details:
  * **Name:** Give this customer gateway a name.
  * **Routing:** Select **Dynamic**.
  * **BGP ASN:** Enter the OCI BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
  * **IP Address:** Enter the Oracle VPN IP address for tunnel 1. Use the IP saved in the previous task.
Click **Create Customer Gateway** to complete provisioning.


[AWS - Modify VPN Connection for New Customer Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
This task replaces the temporary Customer Gateway with one that uses the OCI VPN IP address.
  1. Browse to **Site-to-Site VPN Connections** in the AWS console and select your VPN connection.
  2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), then **Modify VPN Connection**.
  3. You are taken to the **Modify VPN Connection** page. Enter the following details:
     * **Target Type:** Select **Customer** **Gateway** from the list.
     * **Target Customer Gateway ID:** Select the new Customer Gateway with the OCI VPN IP address from the list.
Click the **Save** button to save the configuration when you are done.
After a couple minutes, AWS will complete provisioning the VPN connection and your IPSec VPN between AWS and OCI will come up.
  4. At this point you can delete the temporary customer gateway.


[Verification](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vpn_to_aws.htm)
Browse to your IPSec connection in OCI and the Site-to-Site VPN connections in AWS to verify tunnel status. 
  * Your OCI tunnel under IPSec connection displays **Up** for IPSec status to confirm an operational tunnel.
  * The IPv4 BGP Status also displays **Up** indicating an established BGP session.
  * The tunnel status under the **Tunnel Details** tab for your Site-to-Site VPN connection in AWS displays **Up**.


A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from OCI to actively and passively monitor your cloud resources. For information about monitoring your OCI Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics) .
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

