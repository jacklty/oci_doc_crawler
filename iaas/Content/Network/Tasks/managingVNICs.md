Updated 2025-03-04
# Virtual Network Interface Cards (VNICs)
This topic describes how to manage the **virtual network interface cards** (VNICs) in a Virtual Cloud Network (VCN).
## Overview of VNICs and Physical NICs 🔗 
The servers in Oracle Cloud Infrastructure data centers have physical network interface cards (NICs). When you create an instance on one of these servers, the instance communicates using Networking service _virtual_ NICs (VNICs) associated with the physical NICs. The next sections talk about VNICs and NICs, and how they're related. 
### About VNICs
A VNIC lets an instance to connect to a VCN and decides how the instance connects with endpoints inside and outside the VCN. Each VNIC resides in a subnet in a VCN and includes these items:
  * One _primary_ private IPv4 address from the subnet the VNIC is in, chosen by either you or Oracle. The primary IP address can be an IPv6 address if an IPv6 prefix is assigned to the subnet. 
  * Up to 64 optional [_secondary_ private IPv4 addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses) from the same subnet the VNIC is in, chosen by either you or Oracle.
  * Up to 32 optional secondary IPv6 addresses. IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses) and [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#network_limits). 
  * An optional [public IPv4 address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses) for each private IP, chosen by Oracle but assigned by you. 
  * An optional hostname for DNS for each private IP address (see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network)).
  * A MAC address.
  * A VLAN tag assigned by Oracle and available when attachment of the VNIC to the instance is complete (relevant only for bare metal instances).
  * A flag to enable or disable the source/destination check on the VNIC's network traffic (see [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview)).
  * Optional membership in one or more [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) you select. NSGs have [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that apply only to the VNICs in that NSG.
  * Optional association of the VNIC with a custom route table. This is called [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing) and lets you define routing decisions for the VNIC that override the subnet route tables.


Each VNIC also has a friendly name you can assign, and an Oracle-assigned OCID (see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
Each instance has a _primary VNIC_ that's automatically created and attached during instance creation. That VNIC resides in the subnet you specify. The primary VNIC can't be removed from the instance. A secondary VNIC can be removed or detached from an instance, but it's always immediately deleted and can't exist when no longer attached to an instance.
### How VNICs and Physical NICs Are Related  🔗 
This section is relevant to bare metal instances.
The OS on a bare metal instance recognizes two physical network devices and configures them as two physical NICs, 0 and 1. Whether they're both active depends on the underlying hardware. You can decide which NICs are active for a shape by reviewing the [network bandwidth specifications for bare metal shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#baremetalshapes). If the network bandwidth is listed as "2 x <bandwidth> Gbps," it means that both NIC 0 and NIC 1 are active, and each physical NIC has the indicated amount of bandwidth. If the network bandwidth is listed as "1 x <bandwidth> Gbps," it means that only NIC 0 is active. On current generation Standard and DenseIO shapes, typically both NIC 0 and NIC 1 are active.
NIC 0 is automatically configured with the primary VNIC's IP configuration (the IP addresses, DNS hostname, and so on). 
If you add a _secondary VNIC_ to an instance, you must specify which physical NIC the secondary VNIC uses. You must also configure the OS so that the physical NIC has the secondary VNIC's IP configuration. For Linux instances, see [Oracle Linux: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Linux). For Windows instances, see [Windows: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Windows). 
### About Secondary VNICs 🔗 
You can add secondary VNICs to an instance after it's created. Each secondary VNIC can be in a subnet in the same VCN as the primary VNIC, or in a different subnet either in the same VCN or a different one. However, all the VNICs must be in the same availability domain as the instance.
Here are some reasons why you might use secondary VNICs:
  * **Use a hypervisor on a bare metal instance:** The virtual machines on the bare metal instance each have their own secondary VNIC, giving direct connectivity to other instances and services in the VNIC's VCN. 
  * **Connect an instance to subnets in several VCNs:** For example, you might set up a firewall to protect traffic between VCNs, so the instance needs to connect to subnets in different VCNs. 


Here are more details about secondary VNICs:
  * They're supported for these types of instances:
    * **Linux:** Both VM and bare metal instances. Also see [Oracle Linux: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Linux).
    * **Windows:** Both VM and bare metal instances (except for instances that use previous generation Standard1 and StandardB1 [shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)). For bare metal instances, secondary VNICs are supported only on the second physical NIC. Remember that the first physical NIC is NIC 0, and the second is NIC 1. Also see [Windows: Configuring the OS for Secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Windows).


  * The limit to how many VNICs can be attached to an instance varies by shape. For those limits, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
  * They can be added only after the instance is created.
  * They must always be attached to an instance and can't be moved. The process of creating a secondary VNIC automatically attaches it to the instance. The process of detaching a secondary VNIC automatically deletes it. 
  * They're automatically detached and deleted when you terminate the instance. 
  * The instance's bandwidth is fixed regardless of the number of VNICs attached. You can't specify a bandwidth limit for a particular VNIC on an instance.
  * Attaching several VNICs from the same subnet CIDR block to an instance can introduce asymmetric routing, especially on instances using a variant of Linux. If you need this type of configuration, We recommend assigning several [private IP addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses) to one VNIC, or using policy-based routing as shown in the script later in this topic.
  * Adding several VNICs might route **iSCSI** traffic away from the primary VNIC, which breaks the iSCSI volume attachments. To avoid this issue, add specific routes for the new VNICs, and use the primary VNIC router address as the gateway. iSCSI boot volumes use the 169.254.0.2/32 address and block volumes use the 169.254.2.0/24 network.


### Source/Destination Check 🔗 
By default, every VNIC performs the source/destination check on its network traffic. The VNIC looks at the source and destination listed in the header of each network packet. If the VNIC isn't the source or destination, then the packet is dropped. 
If the VNIC needs to forward traffic (for example, if it needs to perform Network Address Translation (NAT)), you must disable the source/destination check on the VNIC. For instructions, see [Updating a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm#vnic_tasks_update "Update a specified VNIC."). For information about the general scenario, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). 
### VNIC Information in the Instance Metadata 🔗 
The [instance metadata service (IMDS)](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm) includes information about the VNICs at these URLs:
  * IMDS version 2:
Copy
```
http://169.254.169.254/opc/v2/vnics/
```

  * Legacy IMDS version 1:
Copy
```
http://169.254.169.254/opc/v1/vnics/
```



Here's an example response that shows the VNICs that are attached to an instance:
Copy
```
[ {
  "vnicId" : "ocid1.vnic.oc1.phx.exampleuniqueID",
  "privateIp" : "10.0.3.6",
  "vlanTag" : 11,
  "macAddr" : "00:00:00:00:00:01",
  "virtualRouterIp" : "10.0.3.1",
  "subnetCidrBlock" : "10.0.3.0/24",
  "nicIndex" : 0
}, {
  "vnicId" : "ocid1.vnic.oc1.phx.exampleuniqueID",
  "privateIp" : "10.0.4.3",
  "vlanTag" : 12,
  "macAddr" : "00:00:00:00:00:02",
  "virtualRouterIp" : "10.0.4.1",
  "subnetCidrBlock" : "10.0.4.0/24",
  "nicIndex" : 0
} ]
```

### Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
VNICs reside in a subnet but attach to an instance. The VNIC's _attachment to the instance_ is a separate object from the VNIC or the instance itself. Be aware that the VNIC and subnet always exist together in the same compartment, but the VNIC's _attachment to the instance_ always exists in the instance's compartment. This distinction isn't important if you have an access control scenario where all the cloud resources are in the same compartment (for example, for a proof-of-concept). When you move to a production implementation, you might decide to have network administrators manage the network, and other personnel administer instances. That means you might put instances in a different compartment than the subnet. 
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
### Monitoring VNICs
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
For information about monitoring the traffic coming in and out of VNICs, see [VNIC Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm#VNIC_Metrics).
## Oracle Linux: Configuring the OS for Secondary VNICs 🔗 
Use the [oci-network-config](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-network-config) utility to perform the OS configuration required for secondary VNICs on instances that run Oracle Linux.
## Windows: Configuring the OS for Secondary VNICs 🔗 
Secondary VNICs are supported on VM and bare metal instances (except for instances that use previous generation Standard1 and StandardB1 [shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)). For bare metal instances, secondary VNICs are supported **only on the second physical NIC**. 
**Tip** The first physical NIC is NIC 0, and the second is NIC 1.
You must configure the secondary VNIC within the OS. Oracle suggests you write a PowerShell script to perform the configuration. When running the script, you can optionally provide the secondary VNIC's OCID (which you can get from the [instance's VNIC metadata](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview)).
Otherwise, the script should show a list of the secondary VNICs on the instance and ask you to select the one you want to configure. Here's what the script needs to do:
  1. Check if the network interface has an IP address and a default route.
  2. Enable the OS to recognize the secondary VNIC, the **script must overwrite the IP address and default route with static settings (which effectively disables DHCP).** The script should prompt you with a choice: to overwrite with the static settings, or exit.


The overall process for configuration varies slightly depending on the type of instance (VM or bare metal) and how many secondary VNICs you add to the instance. 
[Windows VM instances](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm)
Here's the overall process:
  1. [Add one or more secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm#vnic_tasks_attach "Create a secondary VNIC and attach it to a specified instance.") to the instance. Keep each VNIC's OCID handy so you can provide it later when you run the configuration script. You can also get the OCID from the instance's [VNIC metadata](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  2. [Connect to the instance](https://docs.oracle.com/iaas/Content/GSG/Tasks/testingconnectionWindows.htm) with Remote Desktop.
  3. Run the script as an administrator. Repeat as needed for any of the additional secondary VNICs.


[Windows bare metal instances: adding the first secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm)
If you're adding only a single secondary VNIC to the bare metal instance, here's the overall process:
  1. [Add the secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm#vnic_tasks_attach "Create a secondary VNIC and attach it to a specified instance.") to the instance. Keep the VNIC's OCID handy so you can provide it when later running a configuration script. You can also get the OCID from the instance's [VNIC metadata](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  2. [Connect to the instance](https://docs.oracle.com/iaas/Content/GSG/Tasks/testingconnectionWindows.htm) with Remote Desktop.
  3. Enable the second physical NIC on the instance:
    1. Open the Device Manager, and then select **Network adapters**. 
    2. Select the adapter that corresponds to the instance's second physical NIC, and select **Enable**.
  4. Run the PowerShell script as an administrator.


[Windows bare metal instances: adding more secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm)
If you have one secondary VNIC on the second physical NIC of a bare metal instance, and you want to one or more extra VNICs, here's the overall process. It includes a task for setting up NIC teaming, which is required if the instance has more than one VNIC on the second physical NIC.
**Note** If you increase the number of secondary VNICs on the second physical NIC from one to two or more, you must enable _NIC teaming_ for the second physical NIC (see instructions that follow). In the NIC "team," you create a separate interface for _each_ secondary VNIC on that physical NIC, including the initial one. This means that the original interface for that first secondary VNIC no longer works, and any later configuration you want to do for that VNIC must be done instead on the VNIC's new interface that's part of the "team". 
  1. [Add one or more additional secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm#vnic_tasks_attach "Create a secondary VNIC and attach it to a specified instance.") to the instance. Keep each VNIC's OCID and VLAN tag handy so you can provide them when later running the configuration script. You can also get the values from the instance's [VNIC metadata](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  2. [Connect to the instance](https://docs.oracle.com/iaas/Content/GSG/Tasks/testingconnectionWindows.htm) with Remote Desktop.
  3. Set up NIC teaming on the instance:
    1. Open the Server manager, and then select **Local Server**.
    2. In the list of properties, find **NIC Teaming** , and then select **Disabled** to enable and set up NIC teaming.
    3. In the **Teams** section on the lower-left side of the screen, select **Tasks** , and then select **New Team**.
    4. Enter a name for the team, select the second physical NIC on the instance, and select **OK**. 
The new team is created and appears in the list of teams in the **Teams** section.
    5. Select the new team so it's selected, and then in the **Adapters and Interfaces** section on the right side of the screen, select the **Team Interfaces** tab.
    6. Select **Tasks** , and then select **Add Interface** (you create a separate interface for each secondary VNIC on the second physical NIC).
    7. Select the radio button for **Specific VLAN** , and then enter the Oracle-assigned VLAN tag number for the VLAN (for example, 1). You can get the VLAN tag from the Console or the instance's [VNIC metadata](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
    8. Select **OK**.
    9. Repeat the four preceding steps (e-h) for each of the other secondary VNICs. You create a separate interface for each secondary VNIC.
  4. Run the script as an administrator. Repeat as needed for any of the additional secondary VNICs.


## Managing VNICs 🔗 
The following management actions are available for VNICs:
  * [Listing an Instance's VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm#vnic_tasks_list "List the VNICs attached to a Compute instance.")
  * [Getting a VNIC's properties](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm#vnic_tasks_get "Get a VNIC's VLAN tag and other properties.")
  * [Creating and attaching a secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm#vnic_tasks_attach "Create a secondary VNIC and attach it to a specified instance.")
  * [Updating a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm#vnic_tasks_update "Update a specified VNIC.")
  * [Adding or Removing a VNIC from a Network Security Group](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm#managingvnics_tasks_nsg "Learn to add or remove a VNIC from a network security group.")
  * [Managing Tags for a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm#managingvnics_tasks_tags "Learn to manage resource tags for a VNIC.")
  * [Managing Security Attributes for a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-sec_att.htm#managingvnics_tasks_sec_att "Learn to manage security attributes for a VNIC.")
  * [Detaching and Deleting a Secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-detatch.htm#vnic_tasks_detatch "Detach and delete a specified secondary VNIC.")


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Was this article helpful?
YesNo

