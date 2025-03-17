Updated 2025-02-12
# Creating a Subnet
Create a subnet in a VCN. A subnet is a logical subdivision of a Virtual Cloud Network (VCN). Each subnet consists of a contiguous range of IP addresses that don't overlap with other subnets in the VCN.
To create a subnet, you must have already created a VCN that this subnet will be part of.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to create the subnet in.
    3. Click **Create Subnet**.
    4. In the **Create Subnet** dialog box, specify the resources to associate with the subnet (for example, a route table). By default, the subnet is created in the current compartment, and you choose the resources from the same compartment. Click the **Click here** link in the dialog box to enable compartment selection for the subnet and each of those resources. Enter the following values:
       * **Name:** Enter a friendly name for the subnet. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** By default, the subnet is created in the current compartment, and you choose the resources from the same compartment. To enable compartment selection for the subnet and each of its resources, if it's not already enabled, click the **Click here** link. If compartment selection is enabled, specify the compartment where you want to put the subnet. 
       * **Regional or Availability Domain-specific:** Oracle recommends creating only [regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI."), which means that the subnet can contain resources in any of the region's availability domains. If you instead choose **Availability Domain-specific** (the only type of subnet that Oracle originally offered), you must also specify an availability domain. This choice means that any instances or other resources later created in this subnet must also be in that availability domain. 
       * **IPv4 CIDR Block:** Enter a single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Ensure that it's within the VCN's CIDR block and doesn't overlap with any other subnets. You can change the size of this CIDR block later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, use the [CIDR calculator](http://www.ipaddressguide.com/cidr).
       * **IPv6 Prefixes:** You can request an Oracle-allocated IPv6 /64 prefix, or enter BYOIPv6 or ULA prefixes. You can have a maximum of three IPv6 prefixes in a subnet. After you assign an IPv6 prefix to a VCN, it must always have at least one IPv6 prefix assigned to it. This option is available for VCNs in all commercial and government regions, if the VCN is already enabled for IPv6. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses).
       * **Route table:** Select the route table to associate with the subnet. If you've enabled compartment selection, first specify the compartment that contains the route table. 
       * **Private subnet** or **Public subnet:** If you want the VNICs in the subnet to have public IP addresses, select **Public subnet**. For more information, see [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private).
       * **Use DNS hostnames in this Subnet:** This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The dialog box automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
       * **DHCP Options:** Select the set of DHCP options to associate with the subnet. If you've enabled compartment selection, first specify the compartment that contains the set of DHCP options. 
       * **Security Lists:** Associate one or more security lists with the subnet. If you've enabled compartment selection, first specify the compartment that contains the security list. 
       * **Show Tagging Options:** Click this link to display options for adding tags to the subnet. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Click **Create Subnet**. 
The subnet is created and is displayed on the **Subnets** list on the details page of the VCN that you created it in.
  * Use the [network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html) command and required parameters to create a subnet:
Command
CopyTry It
```
oci network subnet create --cidr-block cidr-block --compartment-id ocid --vcn-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet) operation to create a subnet.


Was this article helpful?
YesNo

