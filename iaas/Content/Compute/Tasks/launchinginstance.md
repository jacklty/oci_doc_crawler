Updated 2025-02-27
# Creating an Instance
Create a bare metal or virtual machine (VM) compute instance by using Compute service.
**Tip** If this is your first time creating an instance, for a guided tutorial consider one the following: 
  * [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.")
  * [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/developer-tutorials/tutorials/apache-on-oracle-linux/01-summary.htm)
  * [Launching Your First Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute Windows instance. After your instance is up and running, optionally create and attach a block volume.")


**Tip** If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see: [Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
## Instance IP addresses
When you create an instance, the instance is automatically attached to a virtual network interface card (VNIC) in the cloud network's subnet and given a private IP address from the subnet's CIDR. You can let the system assign the IP address, or you can specify an address. The private IP address lets instances within the VCN communicate with each other. If you've [set up the cloud network for DNS](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm), instances can instead use fully qualified domain names (FQDNs).
If the subnet is public, you can optionally assign the instance a public IP address. A public IP address is required to [communicate with the instance over the internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private), and to establish a Secure Shell (SSH) or Remote Desktop Protocol (RDP) connection to the instance from outside the cloud network. You can also create SSH or RDP connections to instances without public IP addresses by using a [bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm).
## Capacity availability
To determine whether capacity is available for a specific shape before you create an instance, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
**Note** Partner images and pre-built Oracle enterprise images are not available in Government Cloud realms.
**Important** When a compartment is part of a security zone, you must follow security zone policies when creating a compute instance. This means failing to implement security zone policies might prevent instance creation in that compartment. See [security zone policies](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#security-zones) for a detailed list of default security zone policies.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Before You Begin 🔗 
Before you create an instance, you need these things:
  * (Optional) An existing VCN to create the instance in. Alternatively, you can create a new VCN while you create the instance. For information about setting up VCNs, see [Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm).
  * Public SSH key (Linux instances): If you want to use your own SSH key to connect to the instance using SSH, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
  * VCN security rule to enable RDP access (Windows instances): A VCN security rule that enables RDP access so that you can connect to your instance. Specifically, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).
You can implement this security rule either in a network security group (NSG) that you add this Windows instance to or, in a security list that's used by the instance's subnet.
For instructions for either method, see: [Enabling RDP Access to a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp).
  * (Optional) To create the instance by using a [host capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm#capacity_types) other than on-demand capacity, prepare the capacity as follows:
    * To create an instance and have it count against a [capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity), you must have a capacity reservation in the same availability domain as the instance.
    * To place an instance on a [dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#Dedicated_Virtual_Machine_Hosts), you must have a dedicated virtual machine host in the same availability domain and fault domain as the instance.
The capacity types are mutually exclusive.


[(Optional) Enabling RDP Access to a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
Create a VCN security rule that enables Remote Desktop Protocol (RDP) access so that you can connect to a Windows compute instance. You can implement this security rule either in a network security group (NSG) that you add the Windows instance to or, in a security list that's used by the instance's subnet. **To enable RDP access:**
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  2. Under **List Scope** , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
  3. Click the VCN you want to create the security rule in.
  4. Do one of the following:
     * Add the rule to a network security group that the instance belongs to:
       1. Under **Resources** , click **Network Security Groups**. 
       2. Click the network security group to add the rule to.
       3. Click **Add Rules**.
       4. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Direction:** Ingress
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** RDP (TCP/3389)
          * **Source Port Range:** All
          * **Destination Port Range:** 3389
          * **Description:** An optional description of the rule.
       5. Click **Add**.
     * To add the rule to a security list that is used by the instance's subnet:
       1. Under **Resources** , click **Security Lists**.
       2. Click the security list that you're interested in.
       3. Click **Add Ingress Rules**.
       4. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** RDP (TCP/3389)
          * **Source Port Range:** All
          * **Destination Port Range:** 3389
          * **Description:** An optional description of the rule.
       5. Click **Add Ingress Rules**.


## Create an Instance 🔗 
The following steps describe how to create an instance using the console, CLI, or API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)


  * [1. Define Instance Details ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
Navigate to the compute instances page and start the **Create Instance** workflow.
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click **Create instance**.
    3. Enter a name for the instance. You can add or change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
    4. Select the compartment to create the instance in.
The other resources that you choose can come from different compartments.
    5. In the **Placement** section, select the **Availability domain** that you want to create the instance in.
**Important** If you're creating an instance from a boot volume, you must create the instance in the same **Availability domain** as the boot volume.
    6. (Optional) If you want to choose a [capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm#capacity_types), click **Show advanced options** in the Placement section and select one of the following options under **Capacity Type**.
       * **On-demand capacity:** The instance is launched on a shared host using on-demand capacity. This is the default.
       * **Preemptible capacity** : This option lets you run the instance on a shared host using [preemptible capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#preemptible). The capacity is reclaimed when it's needed elsewhere, and the instances are terminated. Select whether to permanently delete the attached boot volume when the capacity is reclaimed and the instance is terminated.
       * **Capacity reservation:** This option lets you count the instance against a [capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity). Select a capacity reservation from the list.
       * **Dedicated host:** This option lets you run the instance in isolation, so that it is not running on shared infrastructure. Select a [dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#Dedicated_Virtual_Machine_Hosts) from the list. You can place an instance on a dedicated virtual machine host only when you create the instance.
       * **Compute cluster:** This option lets you place the instance on a [compute cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters), which is a high-bandwidth, ultra-low-latency remote direct memory access (RDMA) network for high-performance computing. Compute clusters let you manage instances in the cluster individually, and you can have different types of instances in the cluster. Select a cluster from the list.
**(Optional) Cluster Placement Groups**
**Note** If Cluster Placement Groups are not enabled for your tenancy, the control does not appear in the Console.
Turn on **Cluster Placement Group** to enable cluster placement groups for this instance. Select the cluster placement group using the following options:
       * Select a Cluster Placement Group, then select your cluster placement group from the list. 
       * Enter a Cluster Placement Group OCID, in the provided field.
To learn more about Cluster Placement Groups, see: [Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm).
To use Cluster Placement Groups, you must set the correct policies. For more information, see: [Cluster Placement Groups Policies](https://docs.oracle.com/iaas/Content/cluster-placement-groups/policy-reference.htm).
    7. (Optional) If you want to specify a [fault domain](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Fault), click **Show advanced options** in the **Placement** section if you have not already done so. Then, select the [fault domain](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Fault) to use for the instance. 
If you do not specify the fault domain, the system selects one for you. You can edit the fault domain after you create the instance.
    8. (Optional) In the **Security** section, you can create a shielded instance or enable confidential computing. Click **Edit** , and then select the options that you want to enable.
       * To create a [shielded instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded), turn on **Shielded instance**. Then, select the boot options that you want.
       * To enable [confidential computing](https://docs.oracle.com/en-us/iaas/Content/Compute/References/confidential_compute.htm#confidential_compute "Confidential computing encrypts and isolates in-use data and the applications processing that data.") for the instance, turn on **Confidential computing**.
**Tip** If you can't select the shielded or confidential computing settings that you want, first choose a shape and image that support shielded instances or confidential computing. Then, select the shielded instance or confidential computing settings that you want. An instance can either be shielded or enabled for confidential computing, but it can't be both simultaneously.
[2. Select an Image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Image and shape** section, select an **image** for the instance.
By default, an Oracle Linux image is used to boot the instance. To select a different image or a boot volume, click **Change image**. Then in the **Select an image** panel, select one of the following operating systems or image sources, and click **Select image**. 

Platform Images
    
    * To use a [platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images), select **Oracle Linux** , **Ubuntu** , **Windows** , or other Linux distribution. Select the compartment, and then select an OS version. To choose a different image build, or to see which shapes are compatible with an OS version and image build, click the down arrow for the image.
    * When selecting a Windows image there are two licensing options, either Oracle provided or Microsoft bring your own license (BYOL).
      * Images with the Price column set to **Additional license fee** are OCI provided Windows licenses. See the [Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os) for prices.
      * Images with the Price column set to **Bring your own license** require you to provide your own Windows license for that instance. Leveraging this license type requires you to activate your licenses.
For both types of license, you must agree to the Oracle and Microsoft license terms of use for the selected Windows version.
    * To use a Red Hat Enterprise Linux image, follow the steps in [Red Hat Enterprise Linux (RHEL) Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#ossupport__rhel).
    * To use a [Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/overview-marketplace.htm) image, select **Marketplace**.
      * For Oracle enterprise images and [partner images](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/workingwithlistings.htm), select the **Partner images** option, and then select an image. To view more details about an image or to change the image build, click the down arrow for the image. Images in this section include pre-built Oracle enterprise images and solutions enabled for OCI, and trusted third-party images published by Oracle partners.
      * For [community images](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/publishingcommunityapplications.htm), select the **Community images** option, and then select an image. You can filter by OS. To view more details about an image, click the down arrow for the image. Community images are custom images created and published by community members for use by other community members. Community images are not available for Windows. 

Custom Images
    
    * To use a [custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") that was created or imported into your OCI environment, select **My images**. Select the **Custom images** option. Select the compartment, and then select the image.
    * To use a Windows [custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") that was created or imported into your OCI environment, select **My images**. Select the **Custom images** option. Select the compartment, and then select the image.
Next select a Windows **License type**.
      * Select **Micrsosoft bring your own license** to provide your own Windows license for the instance. Leveraging this license type requires you to activate your licenses.
      * Select **OCI provided** to use OCI Windows licenses. See the [Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os) for prices.
For both types of license, you must agree to the Oracle and Microsoft license terms of use for the selected Windows version.
    * To use a [boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm), select **My images**. Select the **Boot volumes** option. Select the compartment, and then select the boot volume.
    * To use a specific version of an image by providing the image **OCID** , select **My images**. Select the **Image OCID** option, and then enter the image OCID. To determine the OCID for platform images, see the [image release notes](https://docs.oracle.com/iaas/images/).
[3. Select a Shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Image and shape** section, select a different shape for the instance, click **Change shape**. Then, in the **Browse all shapes** panel, follow these steps:
    1. In the **Instance type** section, select **Virtual machine** or **Bare metal machine**.
    2. If you're creating a virtual machine, in the **Shape series** section, select a processor group. 
       * **AMD:** (Flexible) Standard shapes that use current-generation AMD processors. AMD shapes are flexible shapes.
       * **Intel:** (Flexible) Standard and optimized shapes that use current-generation Intel processors. Intel shapes are flexible shapes.
       * **Ampere:** (Flexible) The OCI Ampere A1 Compute and OCI Ampere A2 Compute shapes use Arm-based processors. The Arm-based shapes are flexible shapes. These shapes are not supported for Windows.
       * **Specialty and previous generation:** Standard shapes with previous generation Intel and AMD processors, the [Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm) VM.Standard.E2.1.Micro shape, Dense I/O shapes, GPU shapes, and HPC shapes.
[Flexible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible) have a customizable number of OCPUs and amount of memory.
    3. Select a shape.
**Tip** If a shape is disabled, it means that the shape is either incompatible with the image that you selected previously, or not available in the current availability domain. If you don't see a shape, it means that you don't have service limits for the shape. You can [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
    4. If you selected a flexible shape, provide the following information:
       * For **Number of OCPUs** , choose the number of OCPUs that you want to allocate to this instance by dragging the slider. The other resources scale proportionately.
       * If you want this to be a [burstable instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances) and the shape supports bursting, select the **Burstable** option. Then, in the **Baseline utilization per OCPU** list, select the baseline OCPU utilization for the instance. This value is the percentage of OCPUs that you want to use most of the time.
       * For **Amount of memory (GB)** , choose the amount of memory that you want to allocate to this instance. The amount of memory allowed is based on the number of OCPUs selected.
       * If you want to allocate an [extended amount of memory](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-create-instance) or OCPUs to the instance, you can make this instance an extended memory VM by dragging the slider to **Extended OCPU** or **Extended memory**.
For more information about the minimum memory, maximum memory, and ratio of memory to OCPUs for each shape, see [Flexible Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible).
    5. For bare metal instances, optionally [configure advanced BIOS settings](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bios-settings.htm#bios-settings "When you create a bare metal compute instance, you can optionally configure advanced BIOS settings that let you optimize performance. For example, you can disable simultaneous multithreading to optimize the NUMA settings."), such as disabling simultaneous multithreading, disabling cores, or optimizing the NUMA settings. Click **Show advanced BIOS settings** , and then select the options that you want to configure. The settings that are available depend on the shape.
    6. For VM instances, if you want to disable simultaneous multithreading, click **Show advanced OCPU options** , and then uncheck **Enable simultaneous multithreading (SMT)**. Simultaneous multithreading is enabled by default. For more information on disabling SMT, see [Disabling Simultaneous Multithreading](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/disablesmt.htm#disablesmt "You can disable simultaneous multithreading \(SMT\) on your instances through the console or by using CLI commands.").
    7. Click **Select shape**.
[4. Configure Primary VNIC](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Primary VNIC information** section, configure the network details for the instance.
**Tip** If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see: [Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
**Tip** If you want the instance to have an IPv6 address assigned at launch, you must choose an existing VCN with at least one IPv6 prefix assigned and choose a subnet of that VCN that is enabled to use IPv6. Consider using the "Start VCN Wizard" workflow as described in the preceding note to create the VCN.
For **Primary network** and **Subnet** , specify the [virtual cloud network (VCN) and subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm) to create the instance in. Decide whether you want to use an existing VCN and subnet, create a new VCN or subnet, or enter an existing subnet's OCID:
[Select existing virtual cloud network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
Make the following selections:
    * **Virtual cloud network:** The VCN the instance uses to connect to other resources. Choose among the VCNs in the selected compartment. 
    * **Subnet:** A subnet within the VCN. Subnets are either public or private. Resources in a private subnet will not be reachable from external hosts on the internet. In the case of IPv4, resources in private subnets can't have public IP addresses. For more information, see [Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets can also be either AD-specific or regional (regional ones have "regional" after the name). We recommend using regional subnets. For more information, see [About Regional Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet). If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.
If you choose **Select existing subnet** , for **Subnet,** select the subnet. Choose among the subnets in the selected VCN.
If you choose **Create new public subnet** , enter the following information:
      * **New subnet name:** Avoid entering confidential information.
      * **Create in compartment:** The compartment where you want to put the subnet.
      * **CIDR block:** A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Make sure it's within the cloud network's CIDR block and doesn't overlap with any other subnets. You _cannot_ change this value later.. For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
[Create new virtual cloud network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
**Note** Creating an instance with IPv6 addresses assigned at launch is not available when you use this option.
Make the following selections:
    * **New virtual cloud network name:** A friendly name for the network. Avoid entering confidential information.
    * **Create in compartment:** The compartment where you want to put the new network.
    * **Create new subnet:** A subnet within the cloud network to attach the instance to. Subnets are either public or private. Resources in a private subnet will not be reachable from external hosts on the internet. In the case of IPv4, resources in private subnets can't have public IP addresses. For more information, see [Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets can also be either AD-specific or regional (regional ones have "regional" after the name). We recommend using regional subnets. For more information, see [About Regional Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet).
    * **New subnet name:** A friendly name for the subnet. It doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
    * **Create in compartment:** The compartment where you want to put the subnet.
    * **CIDR block:** A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Make sure it's within the cloud network's CIDR block and doesn't overlap with any other subnets. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
    * If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.
[Enter subnet OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
For **Subnet OCID** , enter the subnet OCID.
If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.
[5. Configure Primary IP Address](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In **Primary VNIC IP addresses** , configure the following: 
    * For all subnets, choose to either **Automatically assign private IPv4 address** (the default) or **Manually assign private IPv4 address**. When you choose **Manually assign private IPv4 address** , enter an IPv4 address in an IPv4 CIDR block assigned to the previously chosen subnet. For more information, see [Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). A private IP address is required for all VNICs.
    * For public IPv4 subnets only, you can **Automatically assign public IPv4 address** or uncheck the option and not configure a public IPv4 address at this time. [You can assign a public IPv4 address later if necessary](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top). A VNIC considers a public IPv4 address optional.
    * (IPv6-enabled subnets only) To add an IPv6 address, check **Assign IPv6 addresses from subnet prefixes** , select an IPv6 prefix configured for the subnet you selected, and then choose one of the following: 
      * **Automatically assign IPv6 addresses from prefix:** Choose this option to let the OCI select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix. 
      * **Manually assign IPv6 addresses from prefix:** Choose this option to select a specific address from an IPv6 prefix assigned to this subnet. Example: 0000:0000:1a1a:1a2b. 
If you click **+ Another subnet prefix** you can assign additional IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet).
[6. (Optional) Configure Advanced Network Settings](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
If you want to configure advanced networking settings, click **Show advanced options**. The following options are available:
    * **Use network security groups to control traffic:** Select this option if you want to add the instance's primary VNIC to one or more [network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). Then, specify the NSGs. This option is available only when you use an existing VCN. For more information, see [Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
    * **DNS record:** Select whether to assign the VNIC a private DNS record. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).
    * **Hostname:** Enter a hostname to use for DNS within the VCN. This field is available only if the VCN and subnet both have DNS labels, and you select the option to assign a private DNS record.
    * **Launch options:** Select the [networking launch type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm#top "When you create a VM instance, by default, Oracle Cloud Infrastructure chooses a recommended networking type for the VNIC based on the instance shape and OS image. The networking interface handles functions such as disk input/output and network communication."). This option is available only for VMs.
    * **VCN tags** and **Subnet tags** tabs: If you create a new VCN and subnet, these tabs are available. If you have permissions to create these resources, then you also have permissions to apply free-form tags to the resources. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask an administrator. 
    * **Security attributes** tabs: If you create a new VCN, this tab is available. If you have permissions to create a resource, then you might also have permissions to apply security attributes to that resource. To apply a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to apply security attributes, skip this option or ask an administrator. You can apply security attributes later.
[7. (Optional) Configure Secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In **Secondary VNIC** , click **Add VNIC** and enter the following information: 
    * **VNIC Name:** A friendly name for the secondary VNIC. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    * **Virtual cloud network:** The VCN that contains the subnet of interest.
    * **Subnet:** The subnet the secondary VNIC will be in, which must be in the same availability domain as the instance's primary VNIC. The subnet list includes any [regional subnets or AD-specific subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm) in the primary VNIC's availability domain. 
    * **Physical NIC:** Only relevant if this is a bare metal instance with two [active physical NICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). Select which one you want the secondary VNIC to use. When you later view the instance's details and the list of VNICs attached to the instance, they'll be grouped by NIC 0 and NIC 1. 
    * For all subnets, choose to either **Automatically assign private IPv4 address** (the default) or **Manually assign private IPv4 address**. When you choose **Manually assign private IPv4 address** , enter an IPv4 address in the CIDR block assigned to the previously chosen subnet. For more information, see [Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). A private IP address is required for all VNICs.
    * For public IPv4 subnets only, you can **Automatically assign public IPv4 address** or uncheck the option and not configure a public IPv4 address at this time. You can assign a public IPv4 address later if necessary. A VNIC considers a public IP address optional.
    * (IPv6-enabled subnets only) To add an IPv6 address, check **Assign IPv6 addresses from subnet prefixes** , select an IPv6 prefix configured for the subnet you selected, and then choose one of the following: 
      * **Automatically assign IPv6 addresses from prefix:** Choose this option to let the console select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix. 
      * **Manually assign IPv6 addresses from prefix:** Choose this option to select a specific address from an IPv6 prefix assigned to this subnet. Example: 2001:db8:1a1a:1a2b. 
If you click **+ Another subnet prefix** you can assign additional IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet). If this VNIC is being attached to an existing instance after its launch, keep in mind that your instance OS needs specific configuration to use IPv6 addressing. 
Adding a secondary VNIC is entirely optional and will require further configuration in the instance OS. 
[8. (Linux Instances) Add SSH Keys](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Add SSH keys** section, generate an SSH key pair or upload your own public key. Select one of the following options:
    * **Generate a key pair for me:** Oracle Cloud Infrastructure generates an RSA key pair for the instance. Select **Save Private Key** , and then save the private key on your computer. Optionally, select **Save Public Key** and then save the public key.
**Caution** Anyone who has access to the private key can connect to the instance. Store the private key in a secure location.
**Important** To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
    * **Upload public key files (.pub):** Upload the public key portion of your key pair. Either browse to the key file that you want to upload, or drag and drop the file into the box. To provide multiple keys, press and hold down the Command key (on Mac) or the Ctrl key (on Windows) while selecting files. 
    * **Paste public keys:** Paste the public key portion of your key pair in the box. 
    * **No SSH keys:** Select this option only if you do not want to connect to the instance using SSH. You can't provide a public key or save the key pair that is generated by Oracle Cloud Infrastructure after the instance is created. 
**Tip** If you try to upload or paste a private key, an error occurs.
[9. Configure Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Boot volume** section, configure the size and encryption options for the instance's boot volume:
    * To specify a [custom size for the boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom), select the **Specify a custom boot volume size** check box. Then, enter a custom size from 50 GB to 32 TB. The specified size must be larger than the default boot volume size for the selected image.
**Important** For Windows Server 2012 R2 Datacenter images and Windows platform images published before October 2021, the custom boot volume size must be larger than the image's default boot volume size or 256 GB, whichever is higher.
You can specify the [volume performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm) for boot volumes. The default performance is **Balanced**. You can [modify the performance setting](https://docs.oracle.com/iaas/Content/Block/Tasks/changingvolumeperformance.htm) after you create the instance.
    * For VM instances, you can optionally select the **Use in-transit encryption** check box. For bare metal instances that support in-transit encryption, it is enabled by default and is not configurable. See [Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption) for more information about in-transit encryption. If you are using your own Vault service encryption key for the boot volume, then this key is also used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.
    * Boot volumes are encrypted by default, but you can optionally use your own Vault service encryption key to encrypt the data in this volume. To use the [Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) for your encryption needs, select the **Encrypt this volume with a key that you manage** check box. Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key. If you select this option, this key is used to encrypt data at rest and in-transit.
**Important** The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This condition applies to block volumes and boot volumes. 
[10. (Optional) Attach Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Block volumes** section, select or create additional block volumes to attach to this instance:
**Important** A maximum of 10 block volumes can be attached during instance creation. You can attach more block volumes when instance creation is complete.
Click **Attach block volume**. Three options are available for selecting block volumes.
[Select volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
To select an existing volume, perform the following steps:
    1. Select a block volume from the list. Change the compartment if the block volume is in a different compartment.
    2. Select an **Attachment type** : 
Select **Recommended** or **Custom**. 

**Recommended** selected:
    
       * **Attachment Type:** iSCSI 
         * Select **Require CHAP credentials** to enable CHAP authentication.
         * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
       * **(Optional) Device Path:** Select a device path for the block volume. 

**Custom** selected:
    
       * Select one of the following options: 
         * **(Recommended) iSCSI:** A TCP/IP-based standard used for communication between a volume and attached instance. 
           * Select **Require CHAP credentials** to enable CHAP authentication.
           * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
         * **Paravirtualized:** A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images. 
           * Select **Use in-transit encryption** to encrypt transferred data.
       * **(Optional) Device Path:** Select a device path for the block volume.
    3. Select the **Access type** from one of three options: 
       * **Read/write**
       * **Read/write, shareable**
       * **Read only, shareable**
    4. Click **Attach**.
For detailed explanations of attachment options see: [Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
[Create new volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
To create a new block volume, perform these steps:
    1. In the **Volume information** section enter the requested information: 
       * **Name:** Enter a user-friendly name for the volume. Avoid entering confidential information.
       * (Optional) **Create in compartment:** Select a different compartment if needed.
       * **Availability domain:** The availability domain for the instance is selected by default.
    2. In the **Volume size and performance** section, selection an option: 
       * **Default:** Take the default values displayed in the dialog.
       * **Custom:** Change the available options as needed. Options include: 
         * Size
         * VPUs/GB
         * Default VPUs/GB
    3. In the **Encryption** section, select one of the two options: 
       * **Encrypt using Oracle-managed keys**
       * **Encrypt using customer-managed keys:** Use a key created in the Vault service.
    4. Select an **Attachment type** : 
Select **Recommended** or **Custom**. 

**Recommended** selected:
    
       * **Attachment Type:** iSCSI 
         * Select **Require CHAP credentials** to enable CHAP authentication.
         * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
       * **(Optional) Device Path:** Select a device path for the block volume. 

**Custom** selected:
    
       * Select one of the following options: 
         * **(Recommended) iSCSI:** A TCP/IP-based standard used for communication between a volume and attached instance. 
           * Select **Require CHAP credentials** to enable CHAP authentication.
           * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
         * **Paravirtualized:** A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images. 
           * Select **Use in-transit encryption** to encrypt transferred data.
       * **(Optional) Device Path:** Select a device path for the block volume.
    5. Select the **Access type** from one of three options: 
       * **Read/write**
       * **Read/write, shareable**
       * **Read only, shareable**
    6. Click **Create and attach**.
For detailed explanations of volume creation options see: [Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm).
[Enter volume OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
To select an existing volume using the OCID, perform the following steps:
    1. Enter the block volume OCID in the **Block volume OCID** text box.
    2. Select an **Attachment type** : 
Select **Recommended** or **Custom**. 

**Recommended** selected:
    
       * **Attachment Type:** iSCSI 
         * Select **Require CHAP credentials** to enable CHAP authentication.
         * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
       * **(Optional) Device Path:** Select a device path for the block volume. 

**Custom** selected:
    
       * Select one of the following options: 
         * **(Recommended) iSCSI:** A TCP/IP-based standard used for communication between a volume and attached instance. 
           * Select **Require CHAP credentials** to enable CHAP authentication.
           * Select **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** to enable automatic volume connections.
         * **Paravirtualized:** A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images. 
           * Select **Use in-transit encryption** to encrypt transferred data.
       * **(Optional) Device Path:** Select a device path for the block volume.
    3. Select the **Access type** from one of three options: 
       * **Read/write**
       * **Read/write, shareable**
       * **Read only, shareable**
    4. Click **Attach**.
For detailed explanations of attachment options see: [Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
[11. Configure Live Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In the **Live migration** area, select whether to live migrate the instance to a healthy physical VM host without any notification or disruption. We recommend using live migration.
    * If you select the **Live migration** option (the default) and live migration isn't successful, reboot migration is used. Some shapes do not support live migration.
    * If you don't select this option, a notification is sent for the maintenance event. The instance is live migrated if you do not proactively reboot the instance before the due date. 
By default, if an instance is running when a maintenance event affects the underlying infrastructure, the instance is rebooted after it is recovered. Clear the **Reboot after maintenance** check box if you want the instance to be recovered in the stopped state.
[Free tier live migration options](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
In a free tier account, live migration might appear under **Show advanced options** on the **Availability tab**. You can configure the following options for supported shapes:
    * In the **Live migration** section, select an option:
      * **Let Oracle Cloud Infrastructure choose the best migration option:** Select this option to let Oracle Cloud Infrastructure choose the best option to [migrate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host) to a healthy physical VM host if an underlying infrastructure component needs to undergo maintenance.
      * **Use live migration if possible** : Select this option to have the instance [live migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration) to a healthy physical VM host without any notification or disruption. If live migration isn't successful, [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) is used. Some shapes do not support live migration.
      * **Opt-out** : Select this option to have a notification sent for the maintenance event. The instance is live migrated if you do not proactively reboot the instance before the due date.
    * **Restore instance lifecycle state after infrastructure maintenance:** By default, if an instance is running when a maintenance event affects the underlying infrastructure, the instance is rebooted after it is recovered. Clear this check box if you want the instance to be recovered in the stopped state.
[12. (Optional) Configure Advanced Options](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
To configure advanced settings, click **Show advanced options**. The following options are available:
    * On the **Management** tab, you can configure the following options:
      * **Require an authorization header** : Select this check box to require that all [requests to the instance metadata service (IMDS)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#Getting_Instance_Metadata) use the version 2 endpoint and include an authorization header. Requests to IMDSv1 are denied. The image must support IMDSv2.
      * **Initialization script:** User data can be used by cloud-init to run custom scripts or provide custom cloud-init configuration. Cloudbase-init is used on Windows. Browse to the file that you want to upload, or drag the file into the box. The file or script does not need to be base64-encoded, because the Console performs this encoding when the information is submitted. For information about how to take advantage of user data, see the [cloud-init documentation](http://cloudinit.readthedocs.io/en/latest/topics/format.html) and the [cloudbase-init documentation](https://cloudbase-init.readthedocs.io/en/latest/). The total maximum size for user data and other metadata that you provide is 32,000 bytes.
**Caution** Do not include anything in the script that could trigger a reboot, because that could impact the instance launch and cause it to fail. Any actions that require a reboot should be performed only after the instance state is **Running**.
      * **Tagging:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
      * **Security Attributes:** If you have permissions to create a resource, then you might also have permissions to apply security attributes to that resource. To apply a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to apply security attributes, skip this option or ask an administrator. You can apply security attributes later.
    * On the **Oracle Cloud Agent** tab, choose which [plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins) you want to enable when the instance is launched. Plugins collect performance metrics, install OS updates, and perform other instance management tasks.
**Important** After you create the instance, you might need to perform additional configuration tasks before you can use each plugin.
[13. Create Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)
Click **Create**.
**Note**
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command and required parameters to create an instance:
Copy
```
oci compute instance launch --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * Use these API operations to create instances: 
    * [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
    * [LaunchInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstanceConfiguration): Create an instance from an instance configuration
    * [GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials)
You can also launch instances from images that are published by Oracle partners in the Partner Image catalog. Use these APIs to work with the Partner Image catalog listings:
    * [AppCatalogListing](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListing)
    * [AppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion)
    * [AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)
    * [AppCatalogListingResourceVersionSummary](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionSummary)
    * [AppCatalogListingSummary](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingSummary)
    * [AppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription)


## What's Next 🔗 
  * After the instance is provisioned, details about it appear in the instance list. To view more details, such as IP addresses and the initial password (for Windows instances), click the instance name.
  * When the instance is fully provisioned and running, you can connect to the instance. You [connect to a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") by using a Secure Shell (SSH) connection, and you [connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection.
  * To get messages when something happens with the instance, [set up contextual notifications for the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/contextual-notifications-compute.htm#top "You can get messages when something happens with a compute instance. Use contextual notifications in the Console to create event rules and alarms for an instance. Quick start templates are available.").
  * You can attach a [block volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) to the instance, if the volume is in the same availability domain.
  * You can [let additional users connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance).


Was this article helpful?
YesNo

