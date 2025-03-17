Updated 2025-01-13
# Importing Custom Linux Images
The Compute service lets you import Linux-based images that were created outside of Oracle Cloud Infrastructure (OCI). For example, you can import images running on your on-premises physical or virtual machines (VMs), or VMs running in Oracle Cloud Infrastructure Classic. You can then launch your imported images on compute virtual machines.
## Launch Modes 🔗 
As part of the import process, a launch mode is applied to the image. An image's launch mode is a pre-defined set of launch options. You can launch imported Linux VMs in either paravirtualized mode or emulated mode. On AMD and Arm-based shapes, Oracle Linux Cloud Developer images, and Red Hat Enterprise Linux images, imported images are supported in paravirtualized mode only.
Paravirtualized mode offers better performance than emulated mode. We recommend that you use paravirtualized mode if your OS supports it. Linux-based operating systems running the kernel version 3.4 or later support paravirtualized drivers. You can verify your system's kernel version using the [uname](http://www.linfo.org/uname.html) command.
[To verify the kernel version using the uname command](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm)
Run the following command:
Copy
```
uname -a
```

The output should look similar to this sample:
```
Linux ip_bash 4.14.35-1818.2.1.el7uek.x86_64 #2 SMP Mon Aug 27 21:16:31 PDT 2018 x86_64 x86_64 x86_64 GNU/Linux
```

The kernel version is the number at the first part of output string. In the sample output shown previously, the version is 4.14.35.
If your image supports paravirtualized drivers, you can convert your existing emulated mode instances into paravirtualized instances. After you complete the conversion, instances created from the image are launched in paravirtualized mode.
[To convert emulated mode instances into paravirtualized instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm)
  1. [Create a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.") of your instance.
  2. [Edit the image capabilities for the custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities) to use the following settings:
     * For **Firmware** and **Preferred firmware** , select **BIOS**.
     * For the following fields, select **Paravirtualized**.
       * **Launch mode**
       * **Preferred launch mode**
       * **NIC attachment type**
       * **Preferred network attachment type**
       * **Boot volume type**
       * **Preferred boot volume type**
       * **Local data volume**
       * **Preferred local data volume type**
       * **Remote data volume**
       * **Preferred remote data volume type**


## Supported Operating Systems 🔗 
The Linux and UNIX-like operating systems in the following table support custom image import.
**Support details:**
  * Oracle Cloud Infrastructure has tested the operating systems listed in the following table and supports customers in ensuring that instances launched from these images and built according to the guidelines in this topic are accessible using SSH.
  * For any OS version other than those covered by an official support service from Oracle (for example, Oracle Linux with Premier Support), Oracle Cloud Infrastructure provides commercially reasonable support limited to getting an instance launched and accessible through SSH. 
  * Support from Oracle Cloud Infrastructure in creating an instance from a custom OS does not ensure that the operating system vendor also supports the instance. Customers running [Oracle Linux](https://www.oracle.com/linux/index.html) on Oracle Cloud Infrastructure automatically have access to [Oracle Linux Premier Support](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf).


Linux or UNIX-like Operating System | Supported Versions  
---|---  
CentOS | 6.9, 7, Stream 8 or later  
Debian | 5.0.10, 6.0, 7, 8 or later  
Flatcar Container Linux | 2345.3.0 or later  
FreeBSD | 8, 9, 10, 11, 12 or later  
openSUSE Leap  | 15.1  
Oracle Linux | 5.11, 6.x, 7.x, 8.x, 9.x  
RHEL |  Support from Red Hat and OCI through the Red Hat Certified Cloud and Service Provider (CCSP) program: for versions and shapes, see [Red Hat Ecosystem Catalog - Oracle Cloud Infrastructure](https://catalog.redhat.com/cloud/detail/216977) Limited support from OCI: 4.5, 5.5, 5.6, 5.9, 5.11, 6.5, 6.9, 7 or later  
SUSE | 11, 12.1, 12.2 or later  
Ubuntu | 12.04, 13.04 or later  
### Red Hat Enterprise Linux (RHEL) Images 🔗 
Certain versions of Red Hat Enterprise Linux (RHEL) images are supported through the Red Hat Certified Cloud and Service Provider (CCSP) program. To create an instance using a supported RHEL image:
  1. Identify the RHEL versions and Compute shapes that are supported by reviewing [Red Hat Ecosystem Catalog - Oracle Cloud Infrastructure](https://catalog.redhat.com/cloud/detail/216977).
  2. Download a supported version of RHEL from the [Red Hat Customer Portal](https://access.redhat.com/downloads/). The image format must be the KVM guest image.
  3. [Upload the image to a bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm) in Object Storage. We recommend that you create a separate bucket dedicated to RHEL images.
  4. [Import the image as a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#linux). Use the following settings:
     * **Image type:** QCOW2
     * **Launch mode:** Paravirtualized mode
  5. [Set the custom image to be compatible with the shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks) that are supported for the image.
  6. [Create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks) that uses the RHEL custom image and a supported shape.
  7. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection."). The default username is `cloud-user`.


## Linux Source Image Requirements 🔗 
Custom images must meet the following requirements:
  * The maximum image size is 400 GB.
  * The image must be set up for BIOS boot.
  * Only one disk is supported, and it must be the boot drive with a valid master boot record (MBR) and boot loader. You can migrate additional data volumes after you import the image's boot volume.
  * The boot process must not require additional data volumes to be present for a successful boot.
  * The boot loader should use LVM or a UUID to locate the boot volume.
  * The disk image cannot be encrypted.
  * The disk image must be a VMDK or QCOW2 file.
    * Create the image file by cloning the source volume, not by creating a snapshot.
    * VMDK files must be either the "single growable" (monolithicSparse) type or the "stream optimized" (streamOptimized) type, both of which consist of a single VMDK file. All other VMDK formats, such as those that use multiple files, split volumes, or contain snapshots, are not supported.
  * The network interface must use DHCP to discover the network settings. When you import a custom image, existing network interfaces are not recreated. Any existing network interfaces are replaced with a single NIC after the import process is complete. You can attach additional VNICs after you launch the imported instance.
  * The network configuration must not hardcode the MAC address for the network interface.


We recommend that you enable certificate-based SSH, however this is optional. If you want the image to automatically use SSH keys supplied from an initialization script when you launch an instance, you can install [cloud-init](https://launchpad.net/cloud-init) when preparing the image. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") for more information about providing user data.
## Preparing Linux VMs for Import 🔗 
Before you import a custom Linux image, you must prepare the image to ensure that instances launched from the image can boot correctly and that network connections will work. Do the following:
  1. Optionally, [configure your Linux image to support serial console connections](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingserialconsoleaccess.htm#Enabling_Serial_Console_Access_for_Imported_Linux_Images). A console connection can help you remotely troubleshoot malfunctioning instances, such as an imported image that does not complete a successful boot.
  2. Create a backup of the root volume.
  3. If the VM has remotely attached storage, such as NFS or block volumes, configure any services that rely on this storage to start manually. Remotely attached storage is not available the first time that an imported instance boots on Oracle Cloud Infrastructure.
  4. Ensure that all network interfaces use DHCP, and that the MAC address and IP addresses are not hardcoded. See your system documentation for steps to perform network configuration for your system.
  5. Stop the VM.
  6. Clone the stopped VM as a VMDK or QCOW2 file, and then export the image from your virtualization environment. See the tools documentation for your virtualization environment for steps.


## Importing a Linux-Based VM 🔗 
After you prepare a Linux image for import, follow these steps to import the image:
  1. [Upload the image file to an Object Storage bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm). You can upload the file using the Console or using the [command line interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). If you use the CLI, use the following command:
Command
CopyTry It
```
oci os object put -bn <destination_bucket_name> --file <path_to_the_VMDK_or_QCOW2_file>
```

  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  3. Click **Import image**.
  4. In the **Create in compartment** list, select the compartment that you want to import the image to.
  5. Enter a **Name** for the image. Avoid entering confidential information.
  6. For the **Operating system** , select **Linux**.
  7. Select the **Import from an Object Storage bucket** option.
  8. Select the **Bucket** that you uploaded the image to. 
  9. In the **Object name** list, select the image file that you uploaded.
  10. For the **Image type** , select the file type of the image, either **VMDK** or **QCOW2**.
  11. Depending on your image's version of Linux, in the **Launch mode** area, select **Paravirtualized mode** or **Emulated mode**. If your [image supports paravirtualized drivers](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#ossupport), we recommend that you select paravirtualized mode.
  12. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  13. Click **Import image**.
The imported image appears in the **Custom images** list for the compartment, with a state of **Importing**. When the import completes successfully, the state changes to **Available**.
If the state doesn't change, or no entry appears in the **Custom images** list, the import failed. Ensure that you have read access to the Object Storage object, and that the object contains a supported image.
  14. Complete the post-import tasks.


## Post-Import Tasks for Linux Images 🔗 
After you import a custom Linux-based image, do the following:
  1. If you want to use the image on AMD or X6-based [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes), then add the shapes to the image's [list of compatible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks).
  2. [Create an instance based on the custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."). For the image source, select **Custom Images** , and then select the image that you imported.
  3. [Connect to the instance using SSH](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.").
  4. If the instance requires any remotely attached storage, such as [block volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) or [file storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm), then create and attach it. If you are using [iSCSI](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#iSCSI) attachments, then refer to [Recommended iSCSI Initiator Parameters for Linux-based Images](https://docs.oracle.com/iaas/Content/Block/Concepts/iscsiinformation.htm#iscsid). 
  5. [Create and attach any required secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#create_sec_vnic).
  6. Test that all applications are working as expected.
  7. Reset any services that were set to start manually.
  8. If you enabled serial console access to the image, test it by [creating a serial console connection to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections).


See the [current issues and workarounds](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#known-issues "Known issues have been identified in Compute.") for known issues with imported custom images.
Was this article helpful?
YesNo

