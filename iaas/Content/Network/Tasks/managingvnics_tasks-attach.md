Updated 2025-01-15
# Creating and attaching a secondary VNIC
Create a secondary VNIC and attach it to a specified instance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm)


  *     1. Confirm you're viewing the compartment that contains the Compute instance you're interested in. 
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Click the name of the instance to view its details.
    4. Under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed. 
    5. Click **Create VNIC**. 
    6. In the **Create VNIC** dialog box, specify which VCN and subnet to put the VNIC in. By default, the VNIC is created in the current compartment. You can select a VCN and subnet from the same compartment or a different compartment.
Enter the following:
       * **Name:** A friendly name for the secondary VNIC. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
       * **Virtual cloud network:** The VCN that contains the subnet of interest.
       * **Network:** Select **Normal Setup: Subnet**.
       * **Subnet:** The subnet of interest. The secondary VNIC must be in the same availability domain as the instance's primary VNIC, so the subnet list includes any [regional subnets or AD-specific subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI.") in the primary VNIC's availability domain. 
       * **Physical NIC:** Only relevant if this is a bare metal instance with two [active physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview). Select which one you want the secondary VNIC to use. When you later view the instance's details and the list of VNICs attached to the instance, VNICs are grouped by NIC 0 and NIC 1. 
       * **Use network security groups to control traffic:** Select this checkbox to add the secondary VNIC to at least one [network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSG) of your choice. NSGs have security rules that apply only to the VNICs in that NSG.
       * **Skip source/destination check:** By default, this checkbox is NOT selected, which means the VNIC performs the source/destination check. Only select this checkbox if you want the VNIC to be able to forward traffic. See [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview). 
       * **Private IPv4 address:** Optional. An available private IPv4 address of your choice from the subnet's CIDR (otherwise the private IP address is automatically assigned).
       * **Public IPv4 address:** Whether to assign a public IPv4 address to the VNIC's primary private IP. Available only if the subnet is public. Choose this option to specify an existing [reserved public IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph) by name, or to create a new reserved IP address by assigning a name and selecting a source [IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#ip_pools) for the address. If you don't select an IP pool you've created, the default Oracle IP pool is used.
       * (IPv6-enabled subnets only) **Assign IPv6 address from subnet:** Choose one of the following: 
         * **Automatically assign IPv6 addresses from prefix:** Choose this option to let the console select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix. 
         * **Manually assign IPv6 addresses from prefix:** Choose this option to select a specific address from an IPv6 prefix assigned to this subnet. Example: 0000:0000:1a1a:1a2b. 
If you click **+ Another subnet prefix** you can assign additional IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet). If this VNIC is being attached to an existing instance after its creation, remember that the instance OS needs specific configuration to use IPv6 addressing. 
       * **DNS record:** Whether to assign the VNIC a private IPv4 DNS record. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network).
       * **Hostname:** Optional. A hostname to be used for IPv4 DNS within the cloud network. Available only if the VCN and subnet both have DNS labels, and the option to assign a private DNS record is selected.
       * **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
       * **Add Security Attributes to lock down your resources:** If you have permissions to create a resource, then you might also have permissions to apply security attributes to that resource. To apply a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to apply security attributes, skip this option or ask an administrator. You can apply security attributes later.
    7. Click **Save Changes**. The secondary VNIC is created and then displayed on the **Attached VNICs** page for the instance. It can take several seconds before the secondary VNIC appears on the page. 
    8. Configure the OS to use the VNIC. See [Oracle Linux: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Linux) or [Windows: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Windows).
  * Use the `oci compute instance attach-vnic` command and required parameters to create a secondary VNIC and attach it to the specified instance:
Command
CopyTry It
```
oci compute instance attach-vnic --instance-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [AttachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/AttachVnic) operation to create a secondary VNIC and attach it to a specified instance.


Was this article helpful?
YesNo

