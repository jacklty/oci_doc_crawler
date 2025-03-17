Updated 2025-01-27
# Creating an Instance Configuration by Entering Configuration Values
On Compute Cloud@Customer, you can create an instance configuration by entering values for individual instance configuration settings. 
**Note**
If you specify a boot volume size that's larger than the default, you need to extend the volume to take advantage of the larger size. See [Resizing Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-volumes.htm#resizing-volumes "On Oracle Cloud Infrastructure, the Block Volume service lets you expand the size of block volumes and boot volumes.").
Avoid entering confidential information in names and tags.
**Important Information About Using Marketplace Images to Create Instances**
The first time you create an instance using a Marketplace image, you must use the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") so that you can accept the user agreement. After that, you can use the Console, CLI, and API to create instances with a Marketplace image.
To maintain the integrity of Marketplace images, there are restrictions and permissible actions. For more information, see [Marketplace Image Restrictions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-marketplace-images.htm#using-marketplace-images__restrictions) and [Permissible Marketplace Image Administration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-marketplace-images.htm#using-marketplace-images__permissible).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-by-entering-configuration-values.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-by-entering-configuration-values.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-by-entering-configuration-values.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Configurations**.
    2. Click **Create Instance Configuration**.
    3. In the **Create Instance Configuration** dialog box, enter the following information:
       * **Name:** Enter a name for the instance configuration.
       * **Create in compartment:** Select the compartment where you want this instance configuration to be created.
       * **Compartment to create instances in** : Select the compartment where you want the instances to be created.
       * **Fault Domain** : (Optional) You can select a fault domain. By default, the system automatically selects the best fault domain for instances. If you specify a fault domain, and the requested fault domain can't accommodate the instance, instance launch fails. See more information about fault domains in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
       * **Source Image:** Select an image or boot volume.
         1. Select the **Source Type:**
            * **Platform Image** : Select to create an instance based on one of the Oracle Linux and Oracle Solaris images that are available in every compartment. See [Compute Cloud@Customer Platform Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-images-provided-with-compute-cloud-at-customer.htm#using-images-provided-with-compute-cloud-at-customer "You can use the platform images that are included with Oracle Compute Cloud@Customer to create instances. You can choose from Oracle Linux and Oracle Solaris images.").
            * **Custom Image** : Selectable if a custom image was created. You might need to select the compartment where the custom image is located. See [Managing Custom Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/managing-custom-images.htm#managing-custom-images "On Compute Cloud@Customer, you can edit, move, import, export, and delete custom images.").
            * **Boot Volume** : Select to create the instance based on an existing boot volume. You might need to select the compartment where the boot volume is located.
            * **Marketplace Image** : Selectable if Marketplace images are available on Compute Cloud@Customer. See [Marketplace Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-marketplace-images.htm#using-marketplace-images "Learn about Marketplace images that you can use on Compute Cloud@Customer.").
         2. Select an image or boot volume from the list.
If you selected **Platform Image** , you see a tabular list with columns **Operating System** , **OS Version** , and **Image Build** (the date the image was built). You can use the drop-down menu arrow to the right of the OS version to select a different version. For example, for the Oracle Linux OS, you can use the drop-down menu to select 9, 8, or 7.9.
If you selected **Custom Image** , you see a tabular list with columns **Name** , **Operating System** , and **OS Version**. You can use the arrows in the column headings to sort the list. You can filter the list by using the **Operating System** drop-down menu above the list of images.
If you selected **Boot Volume** , you see a tabular list with columns **Name** , **Size (GB)** , and **Created** (the date the boot volume was created). You can use the arrows in the column headings to sort the list. In the **Boot Volume** section (after the **Shape** section), you can customize the boot volume size.
If the list is too long to fit in one view, use the arrow buttons to view another page of the list.
To use a platform image that was previously available but is no longer listed, use the Console to create the instance and specify the OCID of the image.
If you selected a **Marketplace image** , select a Marketplace image. If this is the first time you've created an instance with this Marketplace image, an **Agreement Panel** is displayed. Before the instance is created, you must click **Accept Agreement** and confirm the agreement. 
       * **Shape:** If you're using a platform image, select the **VM.PCAStandard.E5.Flex** shape, and configure the number of **OCPUs** and **memory**.
For the **OCPU** and **memory** values, click inside each value field to see the minimum and maximum allowed values. The OCPU and memory configuration can be changed after the instance is created.
For a description of the supported shape, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
       * **Boot Volume:** (Optional) Check the box to specify a custom boot volume size or volume performance setting.
         * **Boot volume size (GB)** : The default boot volume size for the selected image is shown. To specify a larger size, enter an integer number of gigabytes up to 16384 (16 TB) or use the increment and decrement arrows. You can't enter a value smaller than the default size.
If you specify a custom boot volume size, you need to extend the partition to take advantage of the larger size. Oracle Linux platform images include the `oci-utils` package. Use the `oci-growfs` command from that package to extend the root partition and then grow the file system. For other OSs or for custom images, follow the instructions for that OS.
         * **Boot volume performance (VPUs)** : Use the increment and decrement arrows to toggle between balanced performance (10 VPUs/GB) and high performance (20 VPUs/GB). 
       * **Subnet:** Select a subnet.
         1. Select a VCN from the list. You might need to change the compartment to the compartment where the VCN is located.
         2. Select a subnet.
       * **Public IP Address:** To use SSH to connect to instances created with this instance configuration, check the **Assign Public IP** box to have a public IP address assigned to the instances. This box is checked by default if you specified a public subnet. If you don't check this box, or if you clear this box, and then want to assign a public IP address later, see [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.") for instructions.
       * **Secondary VNICs:** (Optional) Check the **Create Additional VNIC** box to create secondary VNICs for instances created with this instance configuration. For descriptions of the requested information requested, see [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance.").
       * **Private IP Address:** (Optional) Specify an available private IP address from the subnet CIDR. By default, a private IP address is automatically assigned. 
**Note**
Because the private IP address must be unique for each instance, don't specify a private IP address if you're going to use this instance configuration to create an instance pool.
       * **DNS Record:** (Optional) Check the **Assign a private DNS record** box to assign a DNS record to instances created with this instance configuration.
       * **Hostname:** (Optional) Enter a hostname if you're using DNS within the cloud network. The hostname must be unique across all VNICs in the subnet. 
**Note**
Don't specify a host name if you are going to use this instance configuration to create an instance pool.
By default, the instance name is used for the hostname. The hostname can also be configured in the OS after the instance is created.
If this is a UNIX instance, see [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.") and [Mounting File Systems on UNIX-based Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-uxix-based-instances.htm#mounting-file-systems-on-uxix-based-instances "On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.") for more information about setting the host name correctly for mounting file systems.
       * SSH Keys: To connect to the instance using SSH, provide a public SSH key.
**Note**
You can't provide this SSH key after the instance is created.
       * **Network Security Group:** (Optional) By default, instances aren't attached to any NSG. Check the **Enable Network Security Group** box to add the primary VNIC for this instance to one or more NSGs.
         1. Select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
         2. Click **Add Network Security Group** to attach to another NSG.
         3. To remove an NSG from the list, click the trash can to the right of that NSG. To remove the last NSG or all NSGs, clear the **Enable Network Security Groups** box.
See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).") for information about NSGs.
       * **Instance Options** : Check the box to disable Legacy Instance Metadata Service Endpoints. By default, legacy (`/v1`) Instance Metadata Service (IMDS) routes are enabled. If you have upgraded your applications to use `/v2` endpoints, check this box to disable `/v1` endpoints. For more information about the Instance Metadata Service, see [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks."). For more information about upgrading your applications, see [Upgrading to IMDS Version 2 Endpoints](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance__upgrade2-imdsv2).
       * **Availability configuration:** (Optional) By default, the system automatically selects the best instance availability option during a maintenance operation such as live migration. Check the **Restore instance lifecycle state after infrastructure maintenance** box to specify that running instances should be automatically restarted after a maintenance event. If this box isn't checked, the instance is recovered in the stopped state.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Instance Configuration**.
  * Use the [oci compute-management instance-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create.html) command and required parameters to create an instance configuration by entering configuration values.
```
oci compute-management instance-configuration create -c <compartment_OCID> --display-name <IC_name> --instance-details file://<custom_config_file>.json
```

The specified compartment is where this instance configuration is created. This compartment could be different from the compartment specified in the instance details JSON file, which is where the instances will be created.
The specified display name is the name of the instance configuration. If you don't provide a value for the `--display-name` option, the default name of the instance configuration is `instanceconfiguration** _YYYYMMDDhhmmss_ ** `, where` **  _YYYYMMDDhhmmss_ ** `is the creation date and time.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the following information:
       * The OCID of the compartment where you want to create this instance configuration.
       * The OCID of the compartment where you want instances that use this instance configuration to be created.
       * The name of the availability domain for instances that use this instance configuration.
       * The OCID of the image or boot volume for instances that use this instance configuration.
       * The name of the shape for instances that use this instance configuration.
       * The OCID of the subnet for instances that use this instance configuration.
    2. Create the configuration file that supplies input to the configuration create command.
The configuration file is a JSON file of property/value pairs.
       * Use the following command to generate the correct syntax of the configuration file and names of properties:
```
$ oci compute-management instance-configuration create --generate-param-json-input instance-details > instance_details.json
```

You don't need all the data that's output by this command. Copy only the information you need, being careful to keep each property in its correct context.
If you omit the fault domain specification, the system automatically selects the best fault domain. If you specify only a single fault domain, all instances are placed in only that fault domain.
If a fault domain that you specify doesn't have enough resources, instances might fail to launch:
         * When you create a single instance ([Using an Instance Configuration to Create an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm#using-an-instance-configuration-to-create-an-instance "On Compute Cloud@Customer, you can use an instance configuration to launch a compute instance.")), and you specify a fault domain in the instance configuration, only that specified fault domain is used to create the instance. Resource constraints might cause the instance launch to fail.
         * When you create instances in a pool, fault domains specified in the placement configuration override fault domains specified in the instance configuration. See [Creating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm#creating-an-instance-pool "On Compute Cloud@Customer, you can create an instance pool of instances that are within the same region.") for more information.
You can specify secondary VNICs and subnets. If you specify a hostname label for a secondary VNIC, the specified hostname label must be unique across all VNICs in the subnet. If you provide a value for the `hostnameLabel` property, you must also set the value of `assignPrivateDnsRecord` to `true`.
         * If the specified hostname label is already in use in the subnet, instance launch ([Using an Instance Configuration to Create an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm#using-an-instance-configuration-to-create-an-instance "On Compute Cloud@Customer, you can use an instance configuration to launch a compute instance.")) will fail with the error "Hostname ` _hostname_ `already in use for the subnet."
         * The `hostnameLabel` property is ignored when you use the instance configuration to create a pool of instances. By default, the instance name is used for the hostname.
If you omit the `assignPublicIp` property, a public IP address is assigned by default if you specify a public subnet. If you set this property to `false` and then decide to assign a public IP address later, see [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.") for instructions.
If users will use `ssh` to connect to the instance, specify the SSH public key as the value of the `ssh_authorized_keys` property in the `metadata` block. You can't add the SSH public key after the instance is created.
The `displayName` property is used for the instance name when you use the `launch-compute-instance` command as described in [Using an Instance Configuration to Create an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm#using-an-instance-configuration-to-create-an-instance "On Compute Cloud@Customer, you can use an instance configuration to launch a compute instance."). If you don't provide a value for the `displayName` property, the default name of instances is `instance** _YYYYMMDDhhmmss_ ** `, where` **  _YYYYMMDDhhmmss_ ** `is the creation date and time.
The `displayName` property is ignored when you create instances in a pool as described in [Creating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-pool.htm#creating-an-instance-pool "On Compute Cloud@Customer, you can create an instance pool of instances that are within the same region.").
       * The following command shows which properties are required to create an instance:
```
$ oci compute instance launch -h
```

Scroll to the Required Parameters section. Optional parameters are described below the required parameters.
The names of the properties in the configuration file are similar to, but different from, the names of the `instance launch` options. Also, some properties are organized into groups of properties, such as `createVnicDetails`, `shapeConfig`, and `sourceDetails`, as shown in the following example configuration file:
```
{
 "instanceType": "compute",
 "launchDetails": {
  "availabilityDomain": "AD-1",
  "compartmentId": "compartment_OCID",
  "createVnicDetails": {
   "assignPublicIp": true,
   "freeformTags": {
    "ConfigType": "Configuration for an XYZ instance."
   },
   "subnetId": "subnet_OCID"
  },
  "displayName": "instance_name",
  "instanceOptions": {
   "areLegacyImdsEndpointsDisabled": true
  },
  "metadata": {
   "ssh_authorized_keys": "public_SSH_key"
  },
  "shape": "shape_name",
  "shapeConfig": {
   "memoryInGBs": 512,
   "ocpus": 32
  },
  "sourceDetails": {
   "bootVolumeSizeInGBs": 100,
   "bootVolumeVpusPerGB": 20,
   "imageId": "image_OCID",
   "sourceType": "image"
  }
 }
}
```

Use `instanceOptions` if you need to disable IMDSv1 endpoints for this instance. See [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks.").
Specify the flexible shape, `VM.PCAStandard.E5.Flex`, and also specify the shape configuration. You must provide a value for `ocpus`. The `memoryInGBs` property is optional; the default value in gigabytes is 16 times the number of `ocpus`.
For information about `bootVolumeSizeInGBs`, see "Boot volume size" in [Creating an Instance Configuration from an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-from-an-instance.htm#creating-an-instance-configuration-from-an-instance "On Compute Cloud@Customer you can create an instance configuration by using the configuration information from an existing compute instance.") CLI tab.
For information about `bootVolumeVpusPerGB`, see "High Performance" in [Creating an Instance Configuration from an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-from-an-instance.htm#creating-an-instance-configuration-from-an-instance "On Compute Cloud@Customer you can create an instance configuration by using the configuration information from an existing compute instance.") CLI tab. When instances are launched, the value of `bootVolumeVpusPerGB` is `null` because this boot volume property isn't stored in the instance object after the instance is launched. To check the value, use the `get boot volume` command and see the value of `vpus-per-gb`.
To change the value of the `firmware` property, provide a value for the `launchOptions` property. The default value is BIOS. You can alternatively specify UEFI_64. Other properties in `launchOptions` can't be changed.
```
"launchOptions": {
 "bootVolumeType": "PARAVIRTUALIZED",
 "firmware": "UEFI_64",
 "isConsistentVolumeNamingEnabled": false,
 "isPvEncryptionInTransitEnabled": false,
 "networkType": "PARAVIRTUALIZED",
 "remoteDataVolumeType": "PARAVIRTUALIZED"
}
```

    3. Run the instance configuration create command.
Syntax:
```
oci compute-management instance-configuration create -c <compartment_OCID> --display-name <IC_name> --instance-details file://<custom_config_file>.json
```

The specified compartment is where this instance configuration is created. This compartment could be different from the compartment specified in the instance details JSON file, which is where the instances will be created.
The specified display name is the name of the instance configuration. If you don't provide a value for the `--display-name` option, the default name of the instance configuration is `instanceconfiguration** _YYYYMMDDhhmmss_ ** `, where` **  _YYYYMMDDhhmmss_ ** `is the creation date and time.
The output of this command is the same as the output of the `instance-configuration get` command.
  * Use the [CreateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/CreateInstanceConfiguration) operation to create an instance configuration entering configuration values.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

