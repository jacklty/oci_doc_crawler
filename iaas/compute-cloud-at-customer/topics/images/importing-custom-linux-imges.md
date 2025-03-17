Updated 2024-10-07
# Importing Custom Linux Images
You can bring your own Linux image to Compute Cloud@Customer as long as the image meets specific requirements.
**Linux Source Image Requirements**
Custom images must meet the following requirements:
  * The maximum image size is 400 GB.
  * The image must be set up for BIOS boot.
  * Only one disk is supported, and it must be the boot drive with a valid master boot record (MBR) and boot loader. You can migrate additional data volumes after you import the image's boot volume.
  * The boot process must not require more data volumes to be present for a successful boot.
  * The boot loader must use LVM or a UUID to locate the boot volume.
  * The disk image can't be encrypted.
  * The disk image must be a VMDK or QCOW2 file. These images can be converted to `.oci` type images.
    * Create the image file by cloning the source volume, not by creating a snapshot.
    * VMDK files must be either the "single growable" (monolithicSparse) type or the "stream optimized" (streamOptimized) type, both of which consist of a single VMDK file. All other VMDK formats, such as those that use multiple files, split volumes, or contain snapshots, are not supported.
  * The network interface must use DHCP to discover the network settings. When you import a custom image, existing network interfaces are not re-created. Any existing network interfaces are replaced with a single NIC after the import process is complete. You can attach more VNICs after you create the imported instance.
  * The network configuration must not hard code the MAC address for the network interface.
  * Oracle recommends that you enable certificate-based SSH, however this recommendation is optional.


## Preparing Linux VMs for Import 🔗 
Before you import a custom Linux image, you must prepare the image to ensure that instances created from the image can boot correctly and that network connections will work. 
Perform these steps.
  1. Ensure that the source image meets the requirements.
See [Importing Custom Linux Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-linux-imges.htm#importing-custom-linux-imges "You can bring your own Linux image to Compute Cloud@Customer as long as the image meets specific requirements.").
  2. Create a backup of the root volume.
  3. If the VM has remotely attached storage, such as NFS or block volumes, configure any services that rely on this storage to start manually. Remotely attached storage isn't available the first time an imported instance boots.
  4. Ensure that all network interfaces use DHCP, and that the MAC address and IP addresses aren't hardcoded. See your system documentation for steps to perform network configuration for your system.
  5. Stop the VM.
  6. Clone the stopped VM as a VMDK or QCOW2 file, and then export the image from your virtualization environment.
Refer to the tools documentation for your virtualization environment.


## Importing a Linux Image 🔗 
After you prepare a Linux image for import, follow these steps to import the image:
  1. Upload the image file to an Object Storage bucket. 
Ensure that you select a bucket where you have read and write access. See [Exporting an Image to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm#exporting-an-image-to-object-storage "On Compute Cloud@Customer, you can export an image to an Object Storage bucket.").
  2. Import the image from the bucket to your tenancy.
See [Importing an Image from an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm#importing-an-image-from-an-object-storage-bucket_0 "On Compute Cloud@Customer, you can import an image into a compartment from an Object Storage bucket.")
  3. Complete the post import tasks.
See [Post Import Tasks for Linux Images](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-custom-linux-imges.htm#post-import-tasks-for-linux-images).


## Post Import Tasks for Linux Images 🔗 
After you import a custom Linux image, perform these steps.
  1. Use the imported image to create an instance.
For the image source, select Custom Images, and then select the image that you imported. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
  2. If the instance requires any remotely attached storage, such as block volumes, create and attach the storage.
See [Creating and Attaching Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-and-attaching-block-volumes.htm#creating-and-attaching-block-volumes "You can create and attach a block volume to an instance to expand the available storage on the instance. The topics in this section describe how to administer the Block Volume Storage service for Compute Cloud@Customer.").
  3. Create and attach any required secondary VNICs.
See [Configuring VNICs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vnics.htm#configuring-vnics-and-ip-adresses "On Compute Cloud@Customer, the compute nodes have physical network interface cards \(NICs\). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network.").
  4. Test that all applications are working as expected.
  5. Reconfigure any services that were set to start manually.


Was this article helpful?
YesNo

