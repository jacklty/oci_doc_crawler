Updated 2025-01-15
# Working with Site-to-Site VPN
This topic contains some details about working with Site-to-Site VPN and the related components. Also see these topics:
  * [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top)
  * [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart)
  * [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN)
  * [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)
  * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
  * [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
  * [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics)
  * [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting)


## Migrating to Policy-Based VPN 🔗 
Oracle Cloud Infrastructure's Site-to-Site VPN v2 service fully supports policy-based IPSec VPNs with up to 50 encryption domains per tunnel.
To prevent potential traffic disruptions, if you have been migrated from the Site-to-Site VPN v1 service to Site-to-Site VPN v2, and have configured a CPE with several encryption domains, change the tunnel configurations on the OCI side of the connection to match the CPE configuration. This article explains why this modification is so important, and the required steps to configure OCI to use policy-based IPSec VPNs.
**Why migrate to the Policy-Based VPN feature**
The Site-to-Site VPN v1 service is always configured as a route-based VPN and uses an any/any encryption domain for both BGP and static routing types. For policy-based VPN interoperability, Site-to-Site VPN v1 supports a CPE configured for policy-based VPNs if the CPE acts as the initiator, and only a single encryption domain is sent to OCI. Configuring multiple encryption domains in this scenario results in instability of the tunnel where you might observe the tunnel flapping or that the traffic traversing the tunnel has unsteady reachability.
The Site-to-Site VPN v2 service uses a policy-based routing type option in addition to BGP and static routing types. Site-to-Site VPN v2's BGP and static routing types remain route-based and support a single any/any encryption domain. These options work with a single encryption domain policy-based CPE configuration, however this isn't recommended and sending more than one encryption domain results in tunnel instability.
The policy-based routing type available for Site-to-Site VPN v2 is a fully featured policy-based VPN that lets you configure the OCI side to fully match a CPE's policy-based configuration and accept all the individual security associations (SAs) required for a stable IPSec VPN tunnel.
For more information on encryption domains and the different IPSec VPN tunnel types, see [Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#Supported_Encryption_Domain_or_Proxy_ID).
After the tunnels have been migrated from Site-to-Site VPN v1 to v2, they continue to use the same routing type (BGP or static) as configured before migration. This section details the step-by-step process to change existing route-based tunnels to use policy-based routing.
  1. Sign-in to the OCI Console.
  2. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  3. Select the IPSec connection whose tunnels need to be changed to use policy-based routing.
  4. The tunnels are listed in the details for the IPSec connection, and the routing type for each tunnel is shown. The routing type is listed as either BGP dynamic routing or static routing. Select the tunnel name to view its details.
  5. Select **Edit** to change the settings of the tunnel you're viewing.
  6. Under **Routing type** check the box for policy based routing. This presents an extra configuration option for **Associations**.
  7. Under **Associations** configure all relevant encryption domains. Each entry under **On-premises CIDR blocks** generates an encryption domain with all possible entries configured under **Oracle Cloud CIDR blocks**. 
For more information see [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel).
    1. For **On-premises CIDR blocks** add all on-premises CIDR blocks that require connectivity to OCI over the IPSec tunnel.
    2. For **Oracle Cloud CIDR blocks** add all OCI CIDR blocks that must be reachable from the on-premises network.
  8. The values for **IPv4 inside tunnel interface - CPE** and **IPv4 inside tunnel interface - Oracle** can be retained as you changed the tunnel's routing type. No changes are required for these values.
  9. Select **Save Changes**.
  10. Navigate back to the parent IPSec connection and repeat the process for the other IPSec tunnel.


## Viewing Tunnel Status and Configuration 🔗 
When you successfully create the IPSec connection, Oracle produces important configuration information for each of the resulting IPSec tunnels. For an example, see [task 2h](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#create_ipsec) in the overall setup process. You can view that information and the status of the tunnels at any time. This includes the BGP status if the tunnel is configured to use BGP dynamic routing. 
[To view the status and configuration information for the IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the IPSec connection you're interested in.
Each tunnel's details are displayed, including the IPSec status, the BGP status (if the tunnel uses BGP dynamic routing), and the Oracle VPN IP address (the VPN headend).
  3. To view a tunnel's shared secret:
    1. Select the tunnel you're interested in.
    2. Next to the **Shared Secret** field, select **Show**.
  4. To view a tunnel's BGP advertised and received routes (including the AS PATH for each route): 
    1. Select the tunnel you're interested in.
    2. Under **Resources** , select either **BGP Routes Received** or **BGP Routes Advertised**. 


## Using the CPE Configuration Helper 🔗 
After you set up Site-to-Site VPN, a network engineer must configure the customer-premises equipment (CPE) at the on-premises end of the connection. The configuration includes details about the Virtual Cloud Network (VCN) and the IPSec tunnels in the Site-to-Site VPN. The CPE Configuration Helper generates the information for the network engineer. For more information, see [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper).
## Changing the Static Routes 🔗 
You can change the static routes for an existing IPSec connection. You can provide up to 10 static routes.
Remember that an IPSec connection can use either static routing or BGP dynamic routing. You associate the static routes with the overall IPSec connection and not the individual tunnels. If an IPSec connection has static routes associated with it, Oracle uses them for routing a tunnel's traffic _only_ if the tunnel itself is configured to use static routing. If it's configured to use BGP dynamic routing, the IPSec connection's static routes are ignored.
**Important** The IPSec connection goes down while it's reprovisioned with the static route changes.
[To edit the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. For the IPSec connection you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
The current static routes are displayed.
  3. Make the changes and select **Save Changes**.


## Changing the CPE IKE Identifier That Oracle Uses 🔗 
If the [CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to give Oracle the CPE IKE identifier. You can either specify it when you create the IPSec connection, or later edit the IPSec connection and change the value. Oracle expects the value to be an IP address or fully qualified domain name (FQDN). When you specify the value, you also specify which type it is. 
**Important** The IPSec connection goes down while it's reprovisioned to use the CPE IKE identifier.
[To change the CPE IKE identifier that Oracle uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**. 
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. For the IPSec connection you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
The current CPE IKE identifier that Oracle is using is displayed at the bottom of the dialog.
  3. Enter new values for **CPE IKE Identifier Type** and **CPE IKE Identifier** , and then select **Save Changes**.


## Using IKEv2 🔗 
Oracle supports Internet Key Exchange (IKE) version 1 and [version 2](https://tools.ietf.org/doc/html/rfc7296) (IKEv2).
To use IKEv2 with a CPE that supports it, you must:
  * Configure each IPSec tunnel to use IKEv2 in the Oracle Console. See the following procedures.
  * Configure the CPE to use IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).


[New IPSec connection: using IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
**Note**
If you [create a new IPSec connection manually](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_poc), you can specify IKEv2 when you create the IPSec connection in the Oracle Console. See the procedure that immediately follows.
If you instead use the [VPN quickstart workflow](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart), the IPSec connection is configured to use IKEv1 only. However, after the workflow is complete, you can edit the resulting IPSec tunnels in the Oracle Console and change them to use IKEv2. 
To manually set up a new IPSec connection that uses IKEv2:
  1. While [creating the IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#create_cpe) in the Oracle Console, in the **Advanced Options** section, select the **Tunnel 1** tab.
  2. From the **IKE Version** menu, select**IKEv2**. 
  3. Repeat the preceding step for the **Tunnel 2** tab.
  4. Later when configuring the CPE, configure it to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. 


[Existing IPSec connection: upgrading to IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
**Important** We recommend performing the following process for one tunnel at a time to avoid disruption in an IPSec connection. If the connection isn't redundant (for example, doesn't have redundant tunnels), expect downtime while you upgrade to IKEv2.
  1. Change the tunnel's IKE version in the Oracle Console: 
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
    2. Select the IPSec connection you're interested in.
    3. Select the tunnel to view its details.
    4. Select **Edit**.
    5. From the **IKE Version** menu, select **IKEv2**. 
    6. Select **Save Changes**.
  2. Update the CPE configuration for the tunnel to use IKEv2 and the related encryption parameters that the CPE supports. For a list of parameters that Oracle supports, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
  3. If the security associations didn't rekey immediately, force a rekey for that tunnel on the CPE. To do this, clear the phase 1 and phase 2 security associations and don't wait for them to expire. Some CPE devices wait for the SAs to expire before rekeying. Forcing the rekey lets you confirm immediately that the IKE version configuration is correct.
  4. To verify, ensure that the security associations for the tunnel rekey correctly. If they don't, confirm that the correct IKE version is set in the Oracle Console and on the CPE, and that the CPE is using the appropriate parameters.


After you confirm the first tunnel is up and running again, repeat the preceding steps for the second tunnel.
## Changing the Shared Secret That an IPSec Tunnel Uses 🔗 
When you set up Site-to-Site VPN, by default Oracle provides each tunnel's shared secret (also called the pre-shared key). You might have a particular shared secret that you want to use instead. You can specify each tunnel's shared secret when you create the IPSec connection, or you can edit the tunnels and provide each new shared secret then. For the shared secret, only numbers, letters, and spaces are allowed. We recommend using a different shared secret for each tunnel.
**Important** When you change a tunnel's shared secret, both the overall IPSec connection and the tunnel go into the Provisioning state while the tunnel is reprovisioned with the new shared secret. The other tunnel in the IPSec connection remains in the Available state. However, while the first tunnel is being reprovisioned, you can't change the second tunnel's configuration.
[To change the shared secret that an IPSec tunnel uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the IPSec connection you're interested in.
  3. Select the tunnel you're interested in.
  4. Next to the **Shared Secret** field, select **Edit**.
  5. Enter a new value. Only numbers, letters, and spaces are allowed. 
  6. Select **Save Changes**. 


## Changing from Static Routing to BGP Dynamic Routing 🔗 
To change an existing Site-to-Site VPN from using static routing to using BGP dynamic routing, follow the process in this section.
**Caution** When you change a tunnel's routing type, the tunnel's IPSec status doesn't change during reprovisioning. However, routing through the tunnel is affected. Traffic is temporarily disrupted until a network engineer configures the CPE device in accordance with the routing type change.**If an existing Site-to-Site VPN is configured to only use a single tunnel, this process disrupts the connection to Oracle.** If a Site-to-Site VPN instead uses several tunnels, we recommend reconfiguring one tunnel at a time to avoid disrupting the connection to Oracle.
[To change from static routing to BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
Prerequisites:
  * Read [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing)
  * Gather the necessary BGP routing information:
    * The network's ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn).
    * For each tunnel: The BGP IP address for each end of the tunnel (the two addresses for a particular tunnel must be a pair from a /30 or /31 subnet, and they must be part of Site-to-Site VPN's encryption domain)


Repeat the following process for each tunnel in the IPSec connection:
  1. Reconfigure the tunnel's routing type from static routing to BGP dynamic routing:
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
    2. Select the IPSec connection you're interested in.
The tunnels are listed, and the status for each tunnel is shown. When the **BGP Status** for the tunnel you're interested in shows only a hyphen (no value) that means that the tunnel is configured to use static routing. 
    3. Select the tunnel to view all its details.
    4. Select **Edit**.
    5. Do the following:
       * **Routing Type:** Select the radio button for **BGP Dynamic Routing**.
       * **BGP ASN:** Enter the network's BGP ASN.
       * **Inside Tunnel Interface - CPE:** Enter the BGP IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel. For example: 10.0.0.16/31. 
       * **Inside Tunnel Interface - Oracle:** Enter the BGP IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel. For example: 10.0.0.17/31.
    6. Select **Save Changes**.
The tunnel's **BGP Status** changes to Down.
  2. Have a network engineer update the CPE device's tunnel configuration to use BGP.
  3. On the on-premises side of the connection, confirm that the tunnel's BGP session is in an established state. If it's not, ensure the configuration of the IP addresses for the tunnel is correct in the Oracle Console and also for the CPE device.
  4. In the Oracle Console, confirm that the tunnel's **BGP Status** is now Up. 
  5. Confirm that the CPE device is learning routes from Oracle, and the CPE device is advertising routes to Oracle. To readvertise the Oracle routes from BGP back to the on-premises network, ensure the CPE device is configured to accept that. An existing policy to advertise the static routes to an on-premises network might not work for the BGP learned routes.
  6. Ping the Oracle BGP IP address from an side of the connection to confirm that traffic is flowing. 


After confirming the first tunnel is up and running with BGP, repeat the process for the second tunnel.
**Important**
As noted in [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing), the static routes that are still configured for the overall IPSec connection **don't** override the BGP routing. Those static routes are ignored when Oracle routes traffic through a tunnel configured to use BGP. 
Also, you can change a tunnel's routing type back to static routing. You might do this if the scheduled downtime window for the CPE device is ending soon and you're having trouble establishing the BGP session. When you switch back to static routing, ensure the overall IPSec connection still has appropriate static routes configured.
## Monitoring Site-to-Site VPN 🔗 
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
For information about monitoring a connection, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
## Viewing Site-to-Site VPN Log Messages 🔗 
You can view the log messages generated for various operational aspects of Site-to-Site VPN such as the negotations that occur in bringing an IPSec tunnel UP. Enabling and accessing the Site-to-Site VPN log messages can be done by using Site-to-Site VPN or the Logging Service.
  * For an overview of the Logging service in general, see [Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).
  * For details on enabling and accessing the Site-to-Site VPN log messages by using the Logging service, see [Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm).
  * For details on the Site-to-Site VPN log message schema, see [Details for Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vpn_connect.htm).


[To enable message logging](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
  2. A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  3. For the IPSec connection you're interested in, select the name of the connection.
The details page for the connection is displayed.
  4. On the left side of the screen under Resources, select on **Logs**. 
If you don't see this option, the connection has the older Site-to-Site VPN v1 type. Message logging requires Site-to-Site VPN v2.
  5. On the **Logs** details page, set the Enable Log field to **Enabled**. A new screen appears.
Details for the options on the screen are at [Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm). Logs are handled the same regardless of the resource type generating the log.
  6. Select **Enable Log**. 


The Log detail page is displayed, and the log is in the process of being created (a "Creating log" message is displayed). 
[To view log messages](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
You must already have logging enabled to view the message log. To view the message log: 
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**. 
  2. A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  3. On the left side of the screen under Resources, select on **Logs**. 
If you don't see this option, the connection has the older Site-to-Site VPN v1 type. Message logging requires Site-to-Site VPN v2.
  4. Select on the **Log Name** of the log you're interested in. This opens a new browser tab showing the requested log.


See [Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm) for details on using the log screen.
## Disabling or Terminating Site-to-Site VPN 🔗 
To disable Site-to-Site VPN between an on-premises network and VCN, you can detach the DRG from the VCN instead of deleting the IPSec connection. If you're also using the DRG with [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."), detaching the DRG would also interrupt the flow of traffic over FastConnect.
You can delete the IPSec connection. However, if you later want to reestablish it, a network engineer must configure the CPE device again with a new set of tunnel configuration information from Oracle. 
To permanently delete Site-to-Site VPN, you must first terminate the IPSec connection. Then you can delete the CPE object. If you're not using the DRG for another connection to an on-premises network, you can detach it from the VCN and then delete it. 
[To delete an IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the IPSec connection you're interested in.
  3. Select **Terminate**.
  4. Confirm the deletion when prompted.


The IPSec connection is in the Terminating state for a short period while it's being deleted.
[To delete a CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
**Prerequisite:** There must not be an IPSec connection between the CPE object and a DRG.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
A list of the CPE objects in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. For the CPE object that you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**. 
  3. Confirm the deletion when prompted.


The object is in the Terminating state for a short period while it's being deleted.
## Managing Tags for an IPSec Connection or CPE Object 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
[To manage tags for an IPSec connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the IPSec connection you're interested in.
  3. Select the **Tags** tab to view or edit the existing tags. Or select **Add tags** to add new ones.


[To manage tags for a CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
A list of the CPE objects in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the CPE object you're interested in. 
  3. Select the **Tags** tab to view or edit the existing tags. Or select **Apply tag** to add new ones.


## Moving an IPSec Connection or CPE Object to a Different Compartment 🔗 
You can move resources from one compartment to another. After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. Moving the CPE object to a different compartment doesn't affect the connection between an on-premises data center and Oracle Cloud Infrastructure. For more information, see [Working with Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#Working).
[To move a CPE object to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Find the CPE object in the list, select the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Resource**.
  3. Select the destination compartment from the list. 
  4. Select **Move Resource**.


## Managing DRGs 🔗 
For tasks related to DRGs, see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).
## Maintaining IPSec Tunnels 🔗 
To ensure the security, stability, and performance of our system, Oracle regularly updates software across the OCI platform. These updates include critical fixes such as vulnerability patches, new features, and bug fixes, which improves the overall functionality and reliability. During the update process, an IPSec tunnel is moved from one VPN headend to another headend, which leads to the IPSec connection getting reset when only one tunnel is used. Only one IPSec tunnel in an IPSec connection is moved. While we can't prevent this brief interruption to the tunnel, we have optimized the update mechanism to minimize the downtime. When the Customer Premise Equipment (CPE) continuously tries to reestablish the connection, normal IPSec tunnel downtime is under a minute. This design lets Oracle maintain a balance between keeping the system secure and reliable while minimizing the disruption to connectivity. Sometimes restoring the IPSec tunnel can take up to 10 minutes:
  * When the tunnel is set as a responder only on the OCI side and the CPE isn't trying to bring the tunnel up immediately
  * When the CPE fails to respond to the IKE negotiation started by the OCI side


While the IPSec tunnel flap during software updates is unavoidable, OCI provides redundant tunnels. These redundant tunnels are designed to maintain continuous traffic flow, even during the brief period when one tunnel experiences downtime. If redundancy has been set up correctly, all traffic routed through the primary tunnel seamlessly switches to the redundant tunnel during a tunnel flap. This failover mechanism ensures that services remain uninterrupted, and the traffic flow is preserved without significant delays. OCI ensures that the redundant tunnels land on two distinct VPN headends. During our software updates only one tunnel is impacted at a time.
We recommend and expect that you test redundancy by taking down the primary VPN tunnel, both during the initial setup and on a regular cadence thereafter. Confirm that VCN instances remain reachable while the primary tunnel is offline, and the traffic is shifting to the redundant tunnel. The VPN Redundancy section in this [Redundancy Guide](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf) provides more insight into setting up the redundancy for VPN tunnels in different use cases.
You can use the following steps to temporarily disable a tunnel yourself to test redundancy failover from a primary IPSec tunnel to a secondary IPSec tunnel:
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Site-to-Site VPN**.
A list of the IPSec connections in the compartment that you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the name of the IPSec connection you're interested in.
Each tunnel's details are displayed, including the IPSec status, the BGP status (if the tunnel uses BGP dynamic routing), and the Oracle VPN IP address (the VPN headend).
  3. Select the name of the primary (or secondary) IPSec tunnel.
  4. To temporarily disable a tunnel:
    1. In the displayed **Tunnel information** tab, next to the **Shared Secret** field, select **Edit**.
    2. Cut the text in the shared secret field, and replace it with a few random letters or numbers. This causes the BGP session to go down and traffic can failover to the other tunnel. This field can't be empty.
Paste the original string in the shared secret field into a text file. You need this to reestablish the BGP session after confirming redundancy is working as expected.
    3. Select **Save changes**.
    4. Confirm that traffic is still flowing on the secondary IPSec tunnel in the connection. 
  5. To restore a temporarily disabled tunnel:
    1. In the displayed **Tunnel information** tab, next to the **Shared Secret** field, select **Edit**.
    2. Paste in the original text in the shared secret field.
    3. Select **Save changes**.
    4. Wait for the BGP session to reestablish.


## Using the API for Site-to-Site VPN 🔗 
These are the Networking service API operations for managing Site-to-Site VPN components. 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To [manage your VCN and subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure."), use these operations:
  * [ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns)
  * [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn)
  * [GetVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/GetVcn)
  * [UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn)
  * [DeleteVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/DeleteVcn)
  * [ChangeVcnCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ChangeVcnCompartment)
  * [ListSubnets](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ListSubnets)
  * [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet)
  * [GetSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/GetSubnet)
  * [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet)
  * [DeleteSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/DeleteSubnet)
  * [ChangeSubnetCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ChangeSubnetCompartment)


To [manage your DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs), use these operations:
  * [ListDrgs](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/ListDrgs)
  * [CreateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/CreateDrg)
  * [GetDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetDrg)
  * [UpdateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/UpdateDrg)
  * [DeleteDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/DeleteDrg)
  * [ListDrgAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/ListDrgAttachments)
  * [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment): This operation attaches a DRG to a VCN and results in a `DrgAttachment` object with its own OCID.
  * [GetDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/GetDrgAttachment)
  * [UpdateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/UpdateDrgAttachment)
  * [DeleteDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/DeleteDrgAttachment): This operation detaches a DRG from a VCN by deleting the `DrgAttachment` object.


To [manage routing for your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2), use these operations: 
  * [ListRouteTables](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ListRouteTables)
  * [GetRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/GetRouteTable)
  * [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable)
  * [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable)
  * [DeleteRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/DeleteRouteTable)


To [manage security lists for your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists), use these operations:
  * [ListSecurityLists](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/ListSecurityLists)
  * [GetSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/GetSecurityList)
  * [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)
  * [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList)
  * [DeleteSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/DeleteSecurityList)


To manage CPEs, use these operations:
  * [ListCpes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/ListCpes)
  * [CreateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/CreateCpe)
  * [GetCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/GetCpe)
  * [UpdateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/UpdateCpe)
  * [DeleteCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/DeleteCpe)
  * [ChangeCpeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/ChangeCpeCompartment)


To manage IPSec connections, use these operations:
  * [ListIPSecConnections](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/ListIPSecConnections)
  * [CreateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/CreateIPSecConnection): Use this operation to set the configuration information for each tunnel, including the IP address of the DRG (the VPN headend) and the shared secret. See [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration). Creating a tunnel has added flexibility if you use [CreateIPSecConnectionTunnelDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateIPSecConnectionTunnelDetails).
  * [GetIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/GetIPSecConnection)
  * [UpdateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/UpdateIPSecConnection) : Updating a tunnel has added flexibility if you use [UpdateIPSecConnectionTunnelDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails).
  * [DeleteIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/DeleteIPSecConnection)
  * [ChangeIPSecConnectionCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/ChangeIPSecConnectionCompartment)
  * [GetIPSecConnectionDeviceStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceStatus/GetIPSecConnectionDeviceStatus): Use this operation to find the status of the IPSec tunnels (up or down). 
  * [GetIPSecConnectionDeviceConfig](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig): Use this operation to get the configuration information for each tunnel.


Was this article helpful?
YesNo

