Updated 2025-02-12
# Creating a VCN
Create a VCN that instances, load balancers, and other resources can use to connect to each other and the internet. After you create a VCN, you must then manually create subnets, gateways, routing rules, and security settings before the VCN can connect to the internet or your on-premises network.
A **virtual cloud network** (VCN) is a software-defined network that you set up in the Oracle Cloud Infrastructure data centers in a particular **region**. 
For more information about VCNs, refer to [Overview of VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI."). 
After you create a VCN, see [Creating a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm#top "Create a subnet in a VCN. A subnet is a logical subdivision of a Virtual Cloud Network \(VCN\). Each subnet consists of a contiguous range of IP addresses that don't overlap with other subnets in the VCN.").
**Note**
For a quick procedure that creates a VCN that you can try out immediately (that is, with subnets and an internet gateway), see the information about the "VCN with Internet Connectivity" wizard in [Virtual Networking Wizards](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartnetworking.htm#Virtual_Networking_Quickstart) or see [Scenario A: Public Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm#Scenario_A_Public_Subnet). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
**Note** To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
    3. Click **Create VCN**.
    4. Enter the following information:
       * **Name:** A descriptive name for the VCN. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API or CLI). Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
       * **IPv4 CIDR Blocks:** Specify up to five but at least one nonoverlapping IPv4 CIDR blocks for the VCN. For example: 172.16.0.0/16. You can add or remove CIDR blocks later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). If necessary, use a [CIDR calculator](http://www.ipaddressguide.com/cidr).
       * **Use DNS Hostnames in this VCN:** This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select this option you can specify a **DNS Label** for the VCN, or you can let the Console to generate one for you. The dialog box automatically displays the corresponding **DNS Domain Name** for the VCN (`<VCN_DNS_label>.oraclevcn.com`). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network).
       * **IPv6 prefixes:** You can request that a single Oracle-allocated IPv6 /56 prefix is assigned to this VCN. Alternately, you can assign a BYOIPv6 prefix or ULA prefix to the VCN. This option is available for all commercial and government regions. For more information on IPv6, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
       * **Add tags to organize your resources:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
       * **Add Security Attributes to lock down your resources:** If you have permissions to create a resource, then you might also have permissions to apply security attributes to that resource. To apply a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to apply security attributes, skip this option or ask an administrator. You can apply security attributes later. 
    5. Click **Create VCN**.
The VCN is then created and displayed on the **Virtual Cloud Networks** list page in the compartment that you chose. 
  * Use the [network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html) command and required parameters to create a VCN:
Command
CopyTry It
```
oci network vcn create --compartment-id compartment_id [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn) operation to create a VCN.


Was this article helpful?
YesNo

