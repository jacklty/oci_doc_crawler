Updated 2025-02-21
# DHCP Options
This topic describes how to manage the Dynamic Host Configuration Protocol (DHCP) options in a Virtual Cloud Network (VCN).
## Overview of DHCP Options 🔗 
The Networking service uses DHCP to automatically provide configuration information to instances when they boot up. Although DHCP lets you change some settings dynamically, others are static and never change. For example, when you launch an instance, either you or Oracle specifies the instance's private IP address. Each time the instance boots up or the instance's DHCP client restarts, DHCP passes that same private IP address to the instance. The address never changes during the instance's lifetime. 
The Networking service provides _DHCP options_ to let you control certain types of configuration on the instances in your VCN. You can change the values of these options at your discretion, unlike the static information that DHCP provides to the instance. The changes take effect the next time the instance's DHCP client restarts or the instance reboots. For more details, see [Important Notes about Your Instances and DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#Importan).
Each subnet in a VCN can have a single set of DHCP options associated with it. That set of options applies to all instances in the subnet. Each VCN comes with a _default set of DHCP options_ with initial values that you can change. If you don't specify otherwise, every subnet uses the VCN's default set of DHCP options.
The following table summarizes the available DHCP options you can configure. 
DHCP Option | Possible Values | Initial Value in the Default DHCP Options | Notes  
---|---|---|---  
Domain Name Server |  [DNS Type](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#Choices):
  * Internet and VCN Resolver
  * Custom Resolver

| DNS Type = Internet and VCN resolver. For more information, see [Choices for DNS in Your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#Choices). |  If you set DNS Type = Custom Resolver, you can specify up to three DNS servers of your choice. For more information, see [Choices for DNS in Your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#Choices). By default, the **Internet and VCN resolver** listens on 169.254.169.254. (IPv4) and fd00:00c1::a9fe:a9fe (IPv6).  
Search Domain | A single search domain |  If you've set up your VCN with a DNS label, the default value for the Search Domain option is the [VCN domain name](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About) (` <VCN  DNS label>.oraclevcn.com`). Otherwise, the Search Domain option is not present in the default set of DHCP options.  |  In general, when _any_ set of DHCP options is initially created (the default set or a custom set you create), the Networking service automatically adds the Search Domain option and sets it to the VCN domain name (`             <VCN-DNS-label>.oraclevcn.com`)_if all of these are true_ :
  * The VCN has a DNS label
  * DNS Type = Internet and VCN Resolver 
  * You did NOT specify a search domain of your choice during creation of the set of DHCP options

After the set of DHCP options is created, you can always remove the Search Domain option or set it to a different value. You can specify only a single search domain in a set of DHCP options.  
## Working with DHCP Options 🔗 
When you create a subnet, you specify which set of DHCP options to associate with the subnet. If you don't, the default set of DHCP options for the VCN is used. You can [change which set of DHCP options the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#change_subnet_dhcp_options) at any time.
When creating a new set of DHCP options, you may optionally assign it a friendly name. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the set of options a unique identifier called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
You can change the values of an individual DHCP option in a set, but notice that when you use the REST API to update a single option in a set, the new set of options replaces the entire existing set.
To delete a set of DHCP options, it must not be associated with a subnet yet. You can't delete a VCN's default set of DHCP options.
See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Important Notes about Your Instances and DHCP Options 🔗 
Whenever you change the value of one of the DHCP options, you must do one of the following for the change to take effect on existing instances in the subnets associated with that set of DHCP options: either restart the DHCP client on the instance, or reboot the instance.
Make sure to keep the DHCP client running so you can always access the instance. If you stop the DHCP client manually or disable NetworkManager (which stops the DHCP client on Linux instances), the instance can't renew its DHCP lease and will become inaccessible when the lease expires (typically within 24 hours). Do not disable NetworkManager unless you use another method to ensure renewal of the lease. 
Stopping the DHCP client might remove the host route table when the lease expires. Also, loss of network connectivity to your iSCSI connections might result in loss of the boot drive. 
Any changes you make to the `/etc/resolv.conf` file are overwritten whenever the DHCP lease is renewed or the instance is rebooted. 
Changes you make to the `/etc/hosts` file are overwritten whenever the DHCP lease is renewed or the instance is rebooted. To persist your changes to the `/etc/hosts` file in Oracle Linux or CentOS instances, add the following line to `/etc/oci-hostname.conf`:
Copy
```
PRESERVE_HOSTINFO=2
```

If the `/etc/oci-hostname.conf` file does not exist, create it.
## Using the Console 🔗 
[To view a VCN's set of default DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**.
The default set and its details are displayed in the list.


[To update options in an existing set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**. 
  4. For the set you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit:**
     * For **DNS Type** : If want instances in the subnet to resolve internet hostnames and hostnames of instances in the VCN, select **Internet and VCN Resolver**. Or to use a DNS server of your choice, select **Custom Resolver** and then enter the server's IP address (three servers maximum). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
     * For **Search Domain** : If you want instances in the subnet to append a particular search domain when resolving DNS queries, enter it here. If the Search Domain option is already set to the [VCN domain name](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About) and you're not sure why, see the details in [Overview of DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#overview).
  5. When you're done, click **Save Changes**.
  6. If you have any existing instances in a subnet that uses this set of DHCP options, make sure to restart the DHCP client on each affected instance, or reboot the instance itself so that it picks up the new setting. 


[To create a new set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**. 
  4. Click **Create DHCP Options**. 
  5. Enter the following:
     * **Name** : A friendly name for the set of options. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Create in Compartment:** The compartment where you want to create the set of DHCP options, if different from the compartment you're currently working in. 
     * **DNS Type** : If want instances in the subnet to resolve internet hostnames and hostnames of instances in the VCN, select **Internet and VCN Resolver**. Or to use a DNS server of your choice, select **Custom Resolver** and then enter the server's IP address (three servers maximum). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
     * **Search Domain** : If you want instances in the subnet to append a particular search domain when resolving DNS queries, enter it here. Be aware that the Networking service automatically sets the Search Domain option in certain situations. See the details in [Overview of DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm#overview).
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  6. When you're done, click **Create DHCP Options**.


The set of options is created and then displayed on the **DHCP Options** page of the compartment you chose. You can now specify this set of options when creating or updating a subnet.
[To change which set of DHCP options a subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Click **Subnets**.
  4. Click the subnet you're interested in.
  5. Click **Edit**.
  6. In the **DHCP Options** section, select the new set of DHCP options you want the subnet to use.
  7. Click **Save Changes**.
The changes take effect within a few seconds.


[To delete a set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
Prerequisite: To delete a set of DHCP options, it must not be associated with a subnet yet. You can't delete the default set of DHCP options in a VCN.
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**. 
  4. For the set you want to delete, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Terminate**. 
  5. Confirm when prompted.


[To manage tags for a set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**. 
  4. For the set you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View Tags**. From there you can view the existing tags, edit them, and apply new ones. 


For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
[To move a set of DHCP options to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)
You can move a set of DHCP options from one compartment to another. When you move a set of DHCP options to a new compartment, inherent policies apply immediately. 
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Click the VCN you're interested in. 
  3. Under **Resources** , click **DHCP Options**.
  4. For the set you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**. 
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.


For more information about using compartments and policies to control access to your cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To manage a VCN's DHCP options, use these operations:
  * [ListDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/ListDhcpOptions)
  * [GetDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/GetDhcpOptions)
  * [UpdateDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/UpdateDhcpOptions)
  * [CreateDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/CreateDhcpOptions)
  * [DeleteDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/DeleteDhcpOptions)
  * [ChangeDhcpOptionsCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/ChangeDhcpOptionsCompartment)


Was this article helpful?
YesNo

