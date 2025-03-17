Updated 2025-01-15
# Using the CPE Configuration Helper
After you set up Site-to-Site VPN, your network engineer must configure the customer-premises equipment (CPE) at your end of the connection (for example, a router). The configuration includes details about your virtual cloud network (VCN) and the IPSec tunnels in the Site-to-Site VPN. This topic describes how to use the _CPE Configuration Helper_ in the Oracle Console to generate information that a network engineer uses to configure the CPE. Notice that the CPE Configuration Helper is also referred to as the _Helper_.
## Overview of the Helper 🔗 
For the IPSec tunnels in a Site-to-Site VPN to work, your network engineer must configure your CPE with specific information. The information comes from different sources. Oracle provides some of it in several places within the Oracle Console. The Helper collects the necessary information in one place and then organizes it to make CPE configuration easier for the network engineer. You can copy or download the resulting content to a file. 
The configuration information that the network engineer needs depends on which vendor makes the CPE. To ensure that the Helper can produce vendor-specific content, you specify which vendor makes your CPE. See the one-time prerequisite in [Using the Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using).
In some cases, the Helper might ask for information about your network and include it in the content. If you don't know the answers, you can leave them blank. The resulting content then uses placeholder variables to show where the network engineer needs to provide the answers.
The content that the Helper produces includes these items:
  * The Oracle VPN headend for the tunnel (the IP address at the Oracle end) 
  * The shared secret (pre-shared key) for the tunnel
  * Your VCN's CIDR
  * Support for the [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) feature
  * BGP information (if you're using BGP dynamic routing for the tunnel)
  * The IPSec parameters that Oracle supports
  * Other relevant information


## Using the Helper 🔗 
[One-time prerequisite: Specify the CPE vendor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
Edit the CPE and select the vendor. If you're not sure which vendor makes your CPE, or it's not in the list, select **Other**.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Customer-premises equipment**.
  2. Select the CPE you're interested in, and then click **Edit**.
  3. For **Vendor** , select your CPE vendor from the list. If you're not sure which vendor makes your CPE, or it's not in the list, select **Other**.
  4. If prompted, select a value for **Platform/Version**. Here are guidelines:
     * Oracle recommends using a route-based configuration if possible.
     * If you do not see your specific CPE platform or version in the list, choose the closest platform/version that predates your CPE version.
  5. Click **Save Changes**. 


[Open the Helper from one of three locations](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
You can access the Helper from three different locations in the Oracle Console. Where you access the Helper controls the scope of the content it produces:
  * **The CPE page:** The Helper produces content for all IPSec connections that terminate on the CPE. Notice that there could be IPSec connections in **compartments** that you do not have access to. If you don't have permission to view a particular IPSec connection, it is not included in the content.
  * **An IPSec connection page:** The Helper produces content for one individual IPSec connection (all tunnels within the connection).
  * **A tunnel's page:** The Helper produces content for one tunnel in an IPSec connection.


  1. In the navigation menu, click ****Networking**** , and then navigate to the resource page you're interested in:
     * The CPE page
     * The IPSec connection page
     * The tunnel page
  2. Click **Open CPE Configuration Helper**.
The Helper opens on the right side of the page.
It shows basic information such as the CPE's public IP address and vendor.


[Generate the content](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
The Helper has a **Create Content** button at the bottom. After you click it and the content is produced, there are buttons to copy or download the content to a file. Give the content to your network engineer, along with the link to the configuration topic for your CPE type (see [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)). You can return to the Helper at any time and again generate the configuration content.
**Tip** For certain CPE vendors, the Helper displays fields for vendor-specific information that is used for CPE configuration. The fields might be blank or already have values. You can fill in the blank fields or leave them as is. For blank fields, the resulting content displays placeholder variables to show where the network engineer needs to fill in the values.
**Instructions:**
  1. Review the template of information in the Helper. Optionally fill in any blank fields.
  2. Click **Create Content** at the bottom of the Helper.
The Helper generates the content.
**Note** See this [known issue](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/known_issues_for_networking.htm#cpe-config-vendor) if you instead see an error that says _The CPE is missing the vendor information (the device type). Update the CPE and add the vendor information._
  3. Click either **Copy Configuration to Clipboard** or **Download Configuration** (to download it to a file).
  4. Click **Close**.
  5. Give the following items to your network engineer:
     * A link to the configuration topic for your CPE type. See [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices).
     * The Helper content that you generated.


## If You Update Your Site-to-Site VPN 🔗 
You could change aspects of your Site-to-Site VPN, and after you do, you might want to generate the Helper content again. For example, imagine that you have an IPSec connection that uses static routing, and you decide to change it to use BGP dynamic routing. After updating the Oracle Console with the new routing information, you can generate the Helper content again for the IPSec connection. You can then give that new content to your network engineer to configure the CPE accordingly.
If you want to use [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) you can't update a CPE object to add that functionality; support must be established at the CPE's initial setup. You also can't have the IPsec tunnels and virtual circuits for this connection use the same DRG route tables.
## Related Topics 🔗 
  * [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top)
  * [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart)
  * [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN)
  * [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters)
  * [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)
  * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
  * [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect)
  * [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
  * [Using the API for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Using_the_API_for_VPN_Connect)
  * [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec)


Was this article helpful?
YesNo

