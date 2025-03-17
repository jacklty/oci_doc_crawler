Updated 2024-10-07
# Importing Custom Microsoft Windows Images
When you bring your own Microsoft Window image to Compute Cloud@Customer, it must meet specific requirements.
**Microsoft Windows Source Image Requirements**
  * The maximum image size is 400 GB.
  * The image must be set up for a BIOS boot.
  * Only one disk is supported, and it must be the boot drive with a valid master boot record (MBR) and boot loader. You can migrate additional data volumes after you import the image's boot volume. 
  * The minimum boot volume size is 256 GB.
  * The boot process must not require other data volumes to be present for a successful boot. 
  * The disk image can't be encrypted.
  * The disk image must be a VMDK or QCOW2 file. Create the image file by cloning the source volume, not by creating a snapshot. VMDK files must be either the "single growable" (monolithicSparse) type or the "stream optimized" (streamOptimized) type, both of which consist of a single VMDK file. All other VMDK formats, such as those that use multiple files, split volumes, or contain snapshots, are not supported.
  * The network interface must use DHCP to discover the network settings. When you import a custom image, existing network interfaces are not re-created. Any existing network interfaces are replaced with a single NIC after the import process is complete. You can attach additional VNICs after you launch the imported instance.
  * The network configuration must not hard code the MAC address for the network interface.


## Preparing Microsoft Windows Systems for Import 🔗 
The configuration described in this section is required so that Compute instances that are created from the Microsoft Windows system image can boot correctly and network connections will work.
**Important**
The system drive configuration where the Microsoft Windows source instance (virtual machine or physical system) is installed will be imported to the image. All partitions on the drive will follow through the imported image. Any other drives will not be imported, and you must re-create them on the instance after the instance is created from the image. Then manually move the data on the noninstance drives to storage on the instance.
You can perform this configuration on the running source system or after you have launched the Compute instance.
  * **Preparing the Source System Prior to Creating the Image**. This is the recommended method.
  * **Preparing the Compute Instance After Instance Launch**. If you have concerns about modifying the live source system, you can use this method. If you use this method, your Compute instance is not initially viable. After you launch your Compute instance, connect to the VNC console and use the VNC window to make the changes described in **Preparing the Source System Prior to Creating the Image**.


### Preparing the Source System Prior to Creating the Image 🔗 
  1. Review the requirements.
See [Importing Custom Microsoft Windows Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#importing-custom-microsoft-windows-images "When you bring your own Microsoft Window image to Compute Cloud@Customer, it must meet specific requirements.").
  2. Clone the existing instance, using the procedures specific to the current platform. Then perform all changes on the clone to prevent disrupting the production instance.
  3. Follow your organization's security guidelines to ensure that the Microsoft Windows system is secured. This can include, but is not limited to the following tasks:
     * Install the latest security updates for the OS and installed applications.
     * Enable the firewall, and configure it so that you only enable the rules that are needed.
     * Disable unnecessary privileged accounts.
     * Use strong passwords for all accounts.
  4. Configure Remote Desktop Protocol (RDP) access.
    1. Enable Remote Desktop connections to the image. See [To connect to a Windows instance from a Remote Desktop Client](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm#Connecti__make-connection).
    2. Modify the Microsoft Windows Firewall inbound port rule to allow RDP access for both Private and Public network location types. When you import the image, the Microsoft Windows Network Location Awareness service will identify the network connection as a Public network type.
  5. Determine whether the current Microsoft Windows license type is a volume license by running the following command in PowerShell:
```
Get-CimInstance -ClassName SoftwareLicensingProduct | where {$_.PartialProductKey} | select ProductKeyChannel
```

If the license is not a volume license, after you import the image, you will update the license type.
  6. If you plan to use the custom image to create more than one instance, create a generalized image of the boot disk. A generalized image is cleaned of computer-specific information, such as unique identifiers. When you create instances from a generalized image, the unique identifiers are regenerated. This prevents two instances that are created from the same image from colliding on the same identifiers.
  7. Create a backup of the root volume.
  8. If the Windows instance has remotely attached storage, such as NFS or block volumes, configure any services that rely on this storage to start manually. Remotely attached storage is not available the first time an instance that was created from a custom image boots on Oracle Cloud Infrastructure.
  9. Ensure that all network interfaces use DHCP, and that the MAC address and IP addresses are not hardcoded. See your system documentation for steps to perform network configuration for your system.
  10. Download the Oracle Windows VirtIO drivers:
    1. Sign in to the [Oracle Software Delivery Cloud site](https://edelivery.oracle.com/osdc/faces/Home.jspx). 
    2. In the All Categories drop-down, select Release. 
    3. Type Oracle Linux 7.9 in the search box and click Search.
    4. Click REL: Oracle Linux 7.9.0.0.0.
    5. At the top right of the page, to the right of your cart, click Continue.
    6. In the Platforms/Languages list, select x86 64 bit. Click Continue.
    7. Accept the license agreement and then click Continue.
    8. Select the check box next to Oracle VirtIO Drivers Version for Microsoft Windows 1.1.x. Clear the other check boxes.
    9. Click Download and then follow the prompts.
  11. Install the Oracle VirtIO drivers for Windows:
    1. Follow the prompts in the installation workflow. On the Installation Type page, select Custom.
    2. Reboot the Windows instance.
  12. Perform the [Creating and Exporting an Image](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#preparing-microsoft-windows-systems-for-import__export-image) procedure.


### Creating and Exporting an Image 🔗 
  1. Stop the system.
  2. Clone the stopped system as a VMDK or QCOW2 file. Refer to the tools documentation for your OS.
  3. Export the image from your physical system or virtualization environment.
  4. Perform the [Importing a Microsoft Windows Image](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#importing-a-microsoft-windows-image) procedure to import the image into Oracle Cloud Infrastructure.


### Preparing the Compute Instance After Instance Launch 🔗 
  1. Perform as many of the **Preparing the Source System Prior to Creating the Image** steps as you are comfortable performing.
  2. Perform the **Creating and Exporting an Image** procedure above.
After importing the image, do _not_ perform the [Post Import Tasks for Microsoft Windows Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#post-import-tasks-for-microsoft-windows-images) procedure.
  3. Use the imported image to launch an instance.
For the image source, select Custom Images, and then select the image that you imported. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
  4. Connect to the console as described in [Connecting to a Compute Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/connecting-to-a-compute-instance.htm#connecting-to-a-compute-instance "On Compute Cloud@Customer, you can connect to a running instance by using a Secure Shell \(SSH\) or Remote Desktop connection the same way you connect to instances in Oracle Cloud Infrastructure \(OCI\).").
  5. Perform the [Preparing Microsoft Windows Systems for Import](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#preparing-microsoft-windows-systems-for-import) procedure.
  6. Perform the [Post Import Tasks for Microsoft Windows Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#post-import-tasks-for-microsoft-windows-images) procedure.


## Importing a Microsoft Windows Image 🔗 
After you prepare a Microsoft Windows image for import, follow these steps to import the image:
  1. Upload the image file to an Object Storage bucket. 
Ensure that you select a bucket where you have read and write access. See [Exporting an Image to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm#exporting-an-image-to-object-storage "On Compute Cloud@Customer, you can export an image to an Object Storage bucket.").
  2. Import the image from the bucket to your tenancy.
See [Importing an Image from an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm#importing-an-image-from-an-object-storage-bucket_0 "On Compute Cloud@Customer, you can import an image into a compartment from an Object Storage bucket.") and [Importing an Image from a URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-a-url.htm#importing-an-image-from-a-url "On Compute Cloud@Customer, you can import an image into a compartment by specifying the URL of the image file."). Use the CLI procedure and specify the `--operating-system` option. Ensure the value of the `--operating-system` option includes the case-insensitive string "Windows".
  3. Complete the post-import tasks.
See [Post Import Tasks for Microsoft Windows Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-microsoft-windows-images.htm#post-import-tasks-for-microsoft-windows-images).


## Post Import Tasks for Microsoft Windows Images 🔗 
After you import a custom Microsoft Windows image, perform these steps.
  1. Use the imported image to create an instance.
For the image source, select Custom Images, and then select the image that you imported. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
  2. Enable Remote Desktop Protocol (RDP) access to the Compute instance.
See [To connect to a Windows instance from a Remote Desktop Client](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm#Connecti__make-connection).
  3. Connect to the instance using RDP.
See [To connect to a Windows instance from a Remote Desktop Client](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm#Connecti__make-connection).
  4. If the instance requires any remotely attached storage, such as block volumes, create and attach the storage.
See [Creating and Attaching Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-and-attaching-block-volumes.htm#creating-and-attaching-block-volumes "You can create and attach a block volume to an instance to expand the available storage on the instance. The topics in this section describe how to administer the Block Volume Storage service for Compute Cloud@Customer.").
  5. Create and attach any required secondary VNICs.
See [Configuring VNICs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vnics.htm#configuring-vnics-and-ip-adresses "On Compute Cloud@Customer, the compute nodes have physical network interface cards \(NICs\). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network.").
  6. Test that all applications are working as expected.
  7. Reconfigure any services that were set to start manually.
  8. Configure your instance to use the Network Time Protocol (NTP).


To avoid performing this configuration every time you create an instance using this custom image, consider creating a new image from the fully configured instance. See [Creating an Image from an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm#creating-an-image-from-an-instance "On Compute Cloud@Customer, you can create a custom image of a compute instance's boot disk and use that custom image to create other compute instances. Instances that you create from this image include the customizations, configuration, and software that were installed on the boot disk when you created the image.").
Was this article helpful?
YesNo

