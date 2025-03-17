Updated 2025-02-21
# Creating an Instance
On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.
**Before You Begin**
See [Tutorial: Launching Your First Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/tutorial-launching-your-first-instance.htm#tutorial-launching-your-first-instance "In this tutorial, you'll learn the basic features of Compute Cloud@Customer by performing some guided steps to create and connect to an instance. After your instance is up and running, this tutorial steps you through creating and attaching a block volume to your instance.") for information about input you need to create an instance.
The following list describes the minimum information that you must provide to create an instance:
  * A name for the instance
  * The compartment where you want to create the instance
  * An [image](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/images.htm#images "On Compute Cloud@Customer, an image is a template of a virtual hard drive. The image provides the OS and other software for a compute instance. You specify an image to use when you create a compute instance.") or boot volume
  * A [shape](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.") – If you're using a platform image, specify the VM.PCAStandard.E5.Flex shape for generic workloads and applications. For GPU-accelerated workloads, select a dedicated GPU shape.
  * A subnet
  * A public SSH key
To log in to the instance, users need either an SSH key or a password, depending on how the image was built. If the instance requires SSH keys for authentication, you must provide the public key when you create the instance. You can't provide the public SSH key after the instance is created.


To create an instance using the CLI, you need the same information as previously listed for the Compute Cloud@Customer Console except that you don't need an instance name. If you don't provide a name for the instance, the default name will be `instance**_YYYYMMDDhhmmss_**`, where`** _YYYYMMDDhhmmss_**`is the creation date and time.
To modify launch options, use the CLI. You can't change launch options or boot volume VPUs per GB after the instance is created.
Instance metadata options enable you to attach important information to instances such as an SSH key, information for cloud-init to use, and labels and proxies for nodes in a Kubernetes Engine cluster node pool. There are metadata key restrictions. See [Metadata Key Restrictions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-instances.htm#compute-instances__metadata-key-restrictions). To configure metadata, create the instance using the CLI `--metadata` or `--extended-metadata` option.
An alternative way to create an instance is to create an instance configuration and use that configuration to launch an instance, as described in [Working with Instance Configurations](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-configurations.htm#working-with-instance-configurations "On Compute Cloud@Customer, an instance configuration contains settings that are used to create compute instances. Instance configurations enable you to consistently create instances with the same configuration without reentering configuration values. You can use an instance configuration to create a single instance or to create an instance pool."). When you use an instance configuration to create an instance, you can specify `blockVolumes` and `secondaryVnics`, as shown in the OCI CLI procedure in [Creating an Instance Configuration by Entering Configuration Values](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-by-entering-configuration-values.htm#updating-an-instance-configuration-by-entering-configuration-values "On Compute Cloud@Customer, you can create an instance configuration by entering values for individual instance configuration settings.").
After you create an instance, you can optionally attach additional VNICs and assign private and public IP addresses. See [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance."), [Managing Private IP Addresses](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-private-ip-addresses.htm#managing-private-ip-addresses "On Compute Cloud@Customer, a private IP address enables communication with resources on the VCN."), and [Managing Public IP Addresses](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-public-ip-addresses.htm#managing-public-ip-addresses "On Compute Cloud@Customer, a public IP address enables communication outside the VCN, including to the data center network.").
**Note**
If you specify a boot volume size that's larger than the default, you need to extend the volume to take advantage of the larger size. See [Resizing Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-volumes.htm#resizing-volumes "On Oracle Cloud Infrastructure, the Block Volume service lets you expand the size of block volumes and boot volumes.").
Avoid entering confidential information in names and tags.
**Important Information About Using Marketplace Images to Create Instances**
The first time you create an instance using a Marketplace image, you must use the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") so that you can accept the user agreement. After that, you can use the Console, CLI, and API to create instances with a Marketplace image.
To maintain the integrity of Marketplace images, there are restrictions and permissible actions. For more information, see [Marketplace Image Restrictions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-marketplace-images.htm#using-marketplace-images__restrictions) and [Permissible Marketplace Image Administration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/using-marketplace-images.htm#using-marketplace-images__permissible).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm)


  *     1. Create or get the following resources and information:
       * An image or boot volume and the compartment where the image or boot volume is located. See [Listing Images and Viewing Details](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm#listing-images-and-viewing-details "On Compute Cloud@Customer, in both the Compute Cloud@Customer Console and CLI, Oracle provided images are listed first, followed by custom images.") and [Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volumes.htm#listing-boot-volumes "On Oracle Cloud Infrastructure, you can list all the boot volumes in a compartment.").
       * A virtual cloud network (VCN) and subnet and the compartment where the VCN and subnet are located. See [Creating a VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm#creating-a-vcn "On Compute Cloud@Customer, a virtual cloud network \(VCN\) a virtual, private network that closely resembles a traditional network. VCNs can be further divided into IP subnets. VCNs can communicate with each other through various types of gateways, each type intended for a particular purpose.").
       * A public Secure Shell (SSH) key if users will connect to the instance using SSH
    2. On the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") **Dashboard** , do one of the following to open the **Create Instance** dialog box:
       * Click **Create Instance** in the top-left corner.
       * In the **Compute** block, click **Instances**. At the top of the instances list on the right side, click **Create Instance**.
       * In the **Compute** block, click **Custom Images**. For the image that you want to use to create the instance, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click the **Create Instance From Image**. You might have to change the compartment at the top of the image list to see the image you want.
When you use the **Create Instance From Image** option, the image name is already entered in the **Create Instance** dialog box and you can't change it. You don't need to enter any of the information described in "Source Image" in the following step.
    3. In the **Create Instance** dialog box, enter the following information:
       * **Name** : Enter a name for the instance. Instance names have the following characteristics:
         * Can be changed after the instance is created.
         * Doesn't need to be unique.
         * Can contain only alphanumeric characters and the hyphen (-) character.
         * Can be a maximum of 63 characters.
       * **Create in Compartment:** Select the compartment where you want to create the instance.
       * **Fault Domain:** (Optional) Select a fault domain. By default, the system automatically selects the best fault domain for the instance when the instance is created. If you specify a fault domain, and the requested fault domain can't accommodate the instance, instance launch fails. The fault domain can be changed after the instance is created.
       * **Source Image:** Select an image or boot volume.
         1. Select the **Source Type:** **Platform Image** , **Custom Image** , or **Boot Volume**.
         2. If you selected **Custom Image** or **Boot Volume** , select the compartment where the image or boot volume that you want to use is located.
         3. Select an image or boot volume from the list.
If you selected **Platform Image** , you see a tabular list with columns **Operating System** , **OS Version** , and **Image Build** (the date the image was built). You can use the drop-down menu arrow to the right of the OS Version to select a different version. For example, for the Oracle Linux operating system, you can use the drop-down menu to select 9, 8, or 7.9.
If you selected **Custom Image** , you see a tabular list with columns **Name** , **Operating System** , and **OS Version**. You can use the arrows in the column headings to sort the list. You can filter the list by using the **Operating System** drop-down menu above the list of images.
If you selected **Boot Volume** , you see a tabular list with columns **Name** , **Size (GB)** , and **Created** (the date the boot volume was created). You can use the arrows in the column headings to sort the list. In the **Boot Volume** section (after the Shape section), you can customize the boot volume size.
If the list is too long to fit in one view, use the arrow to view another page of the list.
To use a platform image that was previously available but is no longer listed, use the CLI to create the instance and specify the OCID of the image.
The source image can't be changed after the instance is created.
       * **Shape** : If you're using a platform image, select the appropriate shape for the intended use: 
         * Generic workloads and applications: Select the **VM.PCAStandard.E5.Flex** shape and configure the number of OCPUs and memory.
For the OCPU and memory values, click inside each value field to see the minimum and maximum allowed values. The OCPU and memory configuration can be changed after the instance is created.
         * GPU-accelerated workloads: Select a **VM.GPU.L40S.x** shape, where x represents the number of GPUs (1-4).
GPU shapes are not flexible. The OCPU and memory values depend on the selected number of GPUs.
For a description of the supported shapes, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
       * **Boot Volume:** (Optional) Check the box to specify a custom boot volume size or volume performance setting.
         * **Boot volume size (GB)** : The default boot volume size for the selected image is shown. To specify a larger size, enter an integer of gigabytes up to 16384 GB (16 TB) or use the increment and decrement arrows. You can't enter a value smaller than the default.
If you specify a custom boot volume size, you need to extend the partition to take advantage of the larger size. Oracle Linux platform images include the `oci-utils` package. Use the `oci-growfs` command from that package to extend the root partition and then grow the file system. For other OSs or for custom images, follow the instructions for that OS.
         * **Boot volume performance (VPUs)** : Use the increment and decrement arrows to toggle between balanced performance (10 VPUs/GB) and high performance (20 VPUs/GB). For more information see [Block Volume Performance Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage__block-volume-performance-options).
If you specify the high performance option and a high performance pool exists but the specified image doesn't exist in the high performance pool (the high performance pool was created after the image was imported), the specified image is copied from the capacity pool to the high performance pool. This operation can take 20-30 minutes, depending on the image size, network configuration, and load.
This copy operation is a one-time operation for each image. Future requests to create an instance specifying this image and the high performance pool won't incur this image copy delay.
You receive an error message from the image copy if the image is larger than 200 gigabytes. Platform images aren't larger than 200 gigabytes.
       * **Subnet:** Select a subnet.
         1. Select a VCN from the list. You might need to change the compartment to the compartment where the VCN is located.
         2. Select a subnet.
       * **Public IP Address:** To connect to the instance using SSH, check the **Assign Public IP** box to have a public IP address assigned to the instance. This box is checked by default if you specified a public subnet. If you don't check this box, or if you clear this box, and then want to assign a public IP address later, see [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.") for instructions.
       * **Private IP Address:** (Optional) Specify an available private IP address from the subnet's CIDR. By default, a private IP address is automatically assigned.
       * **Hostname:** (Optional) Enter a hostname if you're using DNS within the cloud network. The hostname must be unique across all VNICs in the subnet.
By default, the instance name is used for the hostname. The hostname can also be configured in the OS after the instance is created.
If this is a UNIX instance, see [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.") and [Mounting File Systems on UNIX-based Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-uxix-based-instances.htm#mounting-file-systems-on-uxix-based-instances "On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.") for more information about setting the host name correctly for mounting file systems.
       * **SSH Keys:** To connect to the instance using SSH, provide a public SSH key.
**Note**
You can't provide this SSH key after the instance is created.
       * **Initialization Script:** (Optional) Provide an initialization script. This is a file of data to be used for custom instance initialization.
       * **Network Security Group:** (Optional) By default, the new instance isn't attached to any NSG. Check the box labeled Enable Network Security Group to add the primary VNIC for this instance to one or more NSGs.
         1. Select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
         2. Click Add Another NSG if you want to attach to another NSG.
         3. To remove an NSG from the list, click the trash can to the right of that NSG. To remove the last NSG or all NSGs, clear the **Enable Network Security Groups** box.
To update NSG attachments for this instance later, see [Updating a VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm#updating-a-vnic "On Compute Cloud@Customer, you can update the VNIC name, the host name, and whether to disable source/destination checks. You can add the VNIC to an NSG and remove the VNIC from an NSG.").
See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).") for information about NSGs.
       * **Instance Options** : Check the box to disable Legacy Instance Metadata Service Endpoints. By default, legacy (`/v1`) Instance Metadata Service (IMDS) routes are enabled. If you have upgraded your applications to use `/v2` endpoints, check this box to disable `/v1` endpoints. For more information about the Instance Metadata Service, see [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks."). For more information about upgrading your applications, see [Upgrading to IMDS Version 2 Endpoints](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance__upgrade2-imdsv2).
       * **Availability configuration:** (Optional) Specify how to handle this instance during compute node maintenance"
         * **Let Oracle Cloud infrastructure choose the best migration option**
This option is selected by default to allow the system to choose the best option to handle this instance during compute node maintenance. The best option typically is live migration to a healthy compute node. You can't change this setting. If this instance should not be live migrated, for example live migration isn't supported for instances in a Microsoft Windows cluster, then set the `PCA_no_lm` free-form tag to True to prevent live migration for this instance.
         * **Restore instance lifecycle state after infrastructure maintenance**
This option is selected by default to specify that running instances should be automatically restarted after a maintenance operation such as live migration. If this box isn't checked, the instance is recovered in the stopped state.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Instance**.
On success, the instance details page is displayed. On the **Configuration** tab, the **Shape Configuration** column shows the shape, the number of OCPUs, the network bandwidth, and the total memory. On the **Networking** tab, the **VNIC** column shows the VCN and subnet, and the **Instance Access** column shows the primary private IP address and any assigned public IP address.
To check the status of the instance launch, scroll to the **Resources** section and click **Work Request(s)**.
If instance launch fails because of resource constraints, try remedies such as the following:
       * Specify a different fault domain, or don't specify any fault domain and allow the system to choose it.
       * Specify a less resource-intensive shape.
       * Stop an instance that you no longer need.
       * Terminate an instance that you no longer need.
If the status of the work request is Failed, and no reason is listed for the failure, the cause of the failure might be temporary. Wait a short time and then retry the instance create.
  * Use the [oci compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command and required parameters to create an instance.
Copy
```
oci compute instance launch --availability-domain availability_domain --compartment-id compartment_OCID --shape shape --subnet-id subnet_OCID --source-details file://image_info.json [OPTIONS]
```

For a complete list of required and optional parameters, use the following command:
```
oci compute instance launch -h
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Create or get the following resources and information:
       * The name of the availability domain that you want to use: `oci iam                availability-domain list`
       * The OCID of the compartment where you want to create the instance: `oci iam compartment list`
       * The name of the shape for this instance. Select the appropriate shape for the intended use: 
         * Generic workloads and applications:
```
VM.PCAStandard.E5.Flex
```

You must also specify the shape configuration, as shown in the following example. You must provide a value for `ocpus`. The `memoryInGBs` property is optional; the default value in GBs is 16 times the number of `ocpus`.
```
--shape-config '{"ocpus": 32, "memoryInGBs": 512}'
```

         * GPU-accelerated workloads:
```
VM.GPU.L40S.1 | VM.GPU.L40S.2 | VM.GPU.L40S.4
```

GPU shapes are not flexible. There are no custom configuration parameters.
See [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
The shape configuration can be changed after the instance is created.
       * The OCID of the subnet where the VNIC that is attached to this instance will be created: `oci compute vnic-attachment list`
       * If you provide a value for the `--hostname-label` option, see the description of Hostname in the Console tab.
       * Gather one of the following values to specify the image source – either an image or a boot volume.
         * The OCID of the image used to boot the instance: ```
oci compute image list
```

**Note**
Don't select an image that has "`-OKE-`" in its display name. The "`-OKE-`" images can only be used withKubernetes Engine (OKE).
         * The OCID of the boot volume used to boot the instance: ```
oci compute boot-volume-attachment list
```

       * A public Secure Shell (SSH) key to connect to the instance using SSH.
**Note**
You can't provide this SSH key after the instance is created.
For a complete list of required and optional parameters, use the following command:
```
$ oci compute instance launch -h
```

For information about `--display-name` and `--hostname-label` values, see descriptions in the Console tab on this page.
    2. Construct an argument for the `--source-details` option.
The `--source-details` argument can be a JSON file or a command-line string. Use the following command to show the correct format of the JSON properties and values:
```
oci compute instance launch --generate-param-json-input source-details

```

For information about `bootVolumeSizeInGBs`, see "Boot volume size" in the Console tab.
For information about `bootVolumeVpusPerGB`, see "High Performance" in the Console tab.
**Note**
When you later `list` or `get` this instance, the value of `bootVolumeVpusPerGB` is `null` because this boot volume property isn't stored in the instance object after the instance is created. To check the value after instance launch, use the `bv boot-volume` `list` or `get` command and check the value of `vpus-per-gb`.
    3. (Optional) Construct an argument for the `--launch-options` option.
Only the `firmware` property can be changed. The default value is BIOS. You can alternatively specify UEFI_64. If you don't provide a correct value for `firmware`, the instance might not launch. You can't update the value of the `firmware` property with the `instance update` command.
The following shows the default values:
```
{
 "bootVolumeType": "PARAVIRTUALIZED",
 "firmware": "BIOS",
 "isConsistentVolumeNamingEnabled": false,
 "is-pv-encryption-in-transit-enabled": false,
 "networkType": "PARAVIRTUALIZED",
 "remoteDataVolumeType": "PARAVIRTUALIZED"
}
```

To change the value of the `firmware` property, specify the following option:
```
--launch-options file://launch_options.json
```

Where the following is the content of the `launch_options.json` file:
```
{
 "bootVolumeType": "PARAVIRTUALIZED",
 "firmware": "UEFI_64",
 "isConsistentVolumeNamingEnabled": false,
 "is-pv-encryption-in-transit-enabled": false,
 "networkType": "PARAVIRTUALIZED",
 "remoteDataVolumeType": "PARAVIRTUALIZED"
}
```

    4. (Optional) Construct an argument for the `--metadata` or `--extended-metadata` option.
Custom user data can be attached to the instance using the `--metadata` and `--extended-metadata` options. Metadata key/value pairs are string/string maps in JSON format. Extended metadata can be nested JSON objects. Extended metadata can be nested JSON objects.
The combined size of the metadata and extended metadata can be a maximum of 32,000 bytes. 
SSH keys can alternatively be provided in the file argument of the `--ssh-authorized-keys-file` option. User data can alternatively be provided in the file argument of the `--user-data-file` option. Use the `-h` option for more information.
In the example in the next step, the authorized keys file contains one or more public SSH keys in the format required by the SSH `authorized_keys` file. Use a newline character to separate multiple keys. SSH public keys can be provided as the value of the `ssh_authorized_keys` key in the `--metadata` option, or in the file argument of the `--ssh-authorized-keys-file` option. Use `-h` for more information.
    5. Run the instance launch command.
Syntax:
```
oci compute instance launch --availability-domain **_availability_domain_name_** \
--compartment-id **_compartment_OCID_** --shape **_shape_** --subnet-id **_subnet_OCID_** \
--source-details file://**_image_info_**.json
```

**Example:**
If you're using a public subnet, a public IP address is assigned by default, or you can set the `--assign-public-ip` option value to `true`. If you need to assign a public IP address later, see [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.") for instructions.
If you have upgraded your applications to use `/v2` Instance Metadata Service (IMDS) endpoints, use the `--instance-options` option to set `areLegacyImdsEndpointsDisabled` to `true`. By default, legacy (`/v1`) Instance Metadata Service routes are enabled. For more information about the Instance Metadata Service, see [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks."). 
```
$ oci compute instance launch --availability-domain AD-1 --compartment-id <compartment_OCID> --display-name ops1 --shape VM.PCAStandard.E5.Flex --subnet-id <subnet_OCID> --source-details '{"bootVolumeSizeInGBs":100,"bootVolumeVpusPerGB":20,"imageId":"<image_OCID>","sourceType":"image"}' --assign-public-ip true --ssh-authorized-keys-file ./.ssh/<ssh_key_file> --instance-options '{"areLegacyImdsEndpointsDisabled": true}'
{
 "data": {
  "agent-config": null,
  "availability-config": {
   "is-live-migration-preferred": null,
   "recovery-action": "RESTORE_INSTANCE"
  },
  "availability-domain": "AD-1",
  "capacity-reservation-id": null,
  "compartment-id": "ocid1.compartment.unique_ID",
  "dedicated-vm-host-id": null,
  "defined-tags": {},
  "display-name": "ops1",
  "extended-metadata": null,
  "fault-domain": "FAULT-DOMAIN-1",
  "freeform-tags": {},
  "id": "ocid1.instance.unique_ID",
  "image-id": "ocid1.image.unique_ID",
  "instance-options": {
   "are-legacy-imds-endpoints-disabled": true
  },
  "ipxe-script": null,
  "launch-mode": "PARAVIRTUALIZED",
  "launch-options": {
   "boot-volume-type": "PARAVIRTUALIZED",
   "firmware": "BIOS",
   "is-consistent-volume-naming-enabled": false,
   "is-pv-encryption-in-transit-enabled": false,
   "network-type": "PARAVIRTUALIZED",
   "remote-data-volume-type": "PARAVIRTUALIZED"
  },
  "lifecycle-state": "PROVISIONING",
  "metadata": {
   "ssh_authorized_keys": <public_ssh_key>"
  },
  "platform-config": null,
  "preemptible-instance-config": null,
  "region": "region_name",
  "shape": "VM.PCAStandard.E5.Flex",
  "shape-config": {
   "baseline-ocpu-utilization": null,
   "gpu-description": null,
   "gpus": null,
   "local-disk-description": null,
   "local-disks": null,
   "local-disks-total-size-in-gbs": null,
   "max-vnic-attachments": 16,
   "memory-in-gbs": 256.0,
   "networking-bandwidth-in-gbps": 24.6,
   "ocpus": 16.0,
   "processor-description": null
  },
  "source-details": {
   "boot-volume-size-in-gbs": 100,
   "bootVolumeVpusPerGB": 20,
   "image-id": "ocid1.image.unique_ID",
   "kms-key-id": null,
   "source-type": "image"
  },
  "system-tags": null,
  "time-created": "2021-09-22T20:20:04.715304+00:00",
  "time-maintenance-reboot-due": null
 },
 "etag": "92180faa-3660-446c-9559-c12a6e6111f9",
 "opc-work-request-id": "ocid1.workrequest.unique_ID"
}
```

Use the `work-requests work-request get` command to monitor the status of the instance launch:
```
$ oci work-requests work-request get --work-request-id ocid1.workrequest.**_unique_ID_**
```

If the status of the work request is Failed, and no reason is given for the failure, the cause of the failure might be temporary. If no reason is given for the failure, wait a short time and then retry the instance create.
  * Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation to create an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

