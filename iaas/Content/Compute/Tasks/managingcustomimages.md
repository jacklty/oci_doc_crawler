Updated 2025-03-05
# Managing Custom Images
You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.
Oracle Cloud Infrastructure uses [images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images) to launch instances. You specify an image to use when you [launch an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."). 
For details about Windows images, see [Creating Windows Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/windowsimages.htm#Creating_Windows_Custom_Images).
Custom images do not include the data from any attached block volumes. For information about backing up volumes, see [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/backingupavolume.htm).
## Custom Image Tasks 🔗 
Perform the following tasks with custom images.
  * [Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm#listing-custom-images "Get a list of the Compute custom images in an Oracle Cloud Infrastructure compartment.")
  * [Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.")
  * [Creating Windows Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/windowsimages.htm#Creating_Windows_Custom_Images)
  * [Image Import/Export](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#Image_ImportExport)
  * [Getting a Custom Image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm#listing-custom-images "Get the details of a Compute custom image in an Oracle Cloud Infrastructure compartment.")
  * [Editing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-edit.htm#listing-custom-images "Edit a Compute custom image in an Oracle Cloud Infrastructure compartment.")
  * [Launching Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm#listing-custom-images "Launch a Compute custom image in an Oracle Cloud Infrastructure compartment.")
  * [Deleting Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-delete.htm#listing-custom-images "Delete a Compute custom image in an Oracle Cloud Infrastructure compartment.")
  * [Configuring Image Capabilities for Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities)


## System Resilience 🔗 
Follow industry-wide hardware failure best practices to ensure the resilience of your solution in the event of a hardware failure. Some best practices include:
  * Design your system with redundant compute nodes in different availability domains to support failover capability.
  * Create a [custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") of your system drive each time you change the image.
  * [Back up](https://docs.oracle.com/iaas/Content/Block/Tasks/backingupavolume.htm) your data drives, or sync to spare drives, regularly.

If you experience a hardware failure and have followed these practices, you can terminate the failed instance, launch your custom image to create a new instance, and then apply the backup data. 
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let image admins manage custom images](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-custom-images) includes the ability to create, delete, and manage custom images.
The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to create an instance using any custom image. The policy in [Let users launch compute instances from a specific custom image](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances-custom-image) restricts the ability to create an instance from a custom image on an image-by-image basis.
**Tip** When users create a custom image from an instance or launch an instance from a custom image, the instance and image don't have to be in the same **compartment**. However, users must have access to both compartments.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
## Limitations and Considerations 🔗 
  * Certain IP addresses are reserved for Oracle Cloud Infrastructure use and may not be used in your address numbering scheme. See [IP Addresses Reserved for Use by Oracle](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Reserved) for more information.
  * Before you create a custom image of an instance, you must disconnect all iSCSI attachments and remove all iscsid node configurations from the instance. For steps, see [Disconnecting From a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/disconnectingfromavolume.htm).
  * When you create an image of a running instance, the instance shuts down and remains unavailable for several minutes. The instance restarts when the process completes.
  * You cannot create additional custom images of an instance while the instance is engaged in the image creation process. When you start to create a custom image, the system implements a 20-minute timeout, during which you cannot create another image of the same instance. You can, however, create images of different instances at the same time.
  * Custom images are available to all users authorized for the **compartment** in which the image was created. 
  * Custom images inherit the compatible shapes that are set by default from the base image.
  * The maximum size for importing a custom image is 400 GB. 
  * The maximum size for custom exported images is 400 GB.
  * You can create custom images from some Marketplace images, such as the Microsoft SQL Server Enterprise image. Marketplace and the image publisher decide which images are supported.
  * You cannot create an image of an Oracle Database instance.
  * If you use a custom image and update the OS kernel on your instance, you must also upload the update to the network drive. See [OS Kernel Updates for Legacy Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/updatingkernel.htm#top) for more information.
  * You are charged for stored images, as shown in the [Cloud Price List](https://www.oracle.com/cloud/price-list.html#compute-image-artifact).
  * [Cross region replication](https://docs.oracle.com/iaas/Content/Block/Concepts/volumereplication.htm) is not supported for custom images.


For information about how to deploy any version of any operating system that is supported by the Oracle Cloud Infrastructure hardware, see [Bring Your Own Image (BYOI)](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI).
## X5 and X7 Compatibility for Custom Images 🔗 
Oracle X5, X6, and X7 servers have different host hardware. As a result, using an X5 or X6 image on an X7 bare metal or virtual machine (VM) instance may not work without additional modifications. Oracle recommends for X7 hosts that you use the platform images for X7. See [Image Release Notes](https://docs.oracle.com/iaas/images/) for more information about which images support X7. These images have been explicitly created and tested with X7 hardware.
If you attempt to use an existing X5 image on X7 hardware, note the following:
  * No Windows versions are cross-compatible.
  * Oracle Autonomous Linux 7 and Oracle Linux 8 are cross-compatible.
  * Oracle Linux 7, Oracle Linux 8, Oracle Linux 9, Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, CentOS 7, and CentOS Stream 8 are cross-compatible. You may have to update the kernel, however, to the most recent version to install the latest device drivers. To update the kernel, run one of the following commands from a terminal session:
    * **Oracle Linux**
Copy
```
yum update
```

    * **CentOS 7** , **CentOS Stream 8**
Copy
```
yum update
```

    * **Ubuntu 18.04** , **Ubuntu 20.04** , **Ubuntu 22.04**
Copy
```
apt-get update
              apt-get dist-upgrade
```



If you attempt to use an X6 image on non-X6 hardware, then note the following:
  * All CentOS versions and all Windows versions are not cross-compatible.
  * Oracle Autonomous Linux 7 and Oracle Linux 8 are cross-compatible.
  * Oracle Linux 7, Ubuntu 22.04, Ubuntu 20.04, and Ubuntu 18.04 are cross-compatible. Use the platform images for X6.


The primary device drivers that are different between X5, X6, and X7 hosts are:
  * Network device drivers
  * NVMe drive device drivers
  * GPU device drivers


Additional updates might be required depending on how you have customized the image.
Was this article helpful?
YesNo

