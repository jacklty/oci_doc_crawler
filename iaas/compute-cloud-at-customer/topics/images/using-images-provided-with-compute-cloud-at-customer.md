Updated 2024-08-06
# Compute Cloud@Customer Platform Images
You can use the platform images that are included with Oracle Compute Cloud@Customer to create instances. You can choose from Oracle Linux and Oracle Solaris images.
**Note** The platform images provided with Compute Cloud@Customer have been specifically configured for use on Compute Cloud@Customer only. The following restrictions apply:
  * Compute Cloud@Customer images can't be used to create other Oracle Cloud Infrastructure instances that aren't on Compute Cloud@Customer.
  * Oracle Cloud Infrastructure Platform images can't be used to create instances on Compute Cloud@Customer.


**Note**
Only the three most recently published versions of each major distribution are listed in the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") and by the `compute image list` command. After an upgrade, older versions might no longer be listed, but they're still accessible. To use an older image version, use the CLI and specify the OCID of the image. One way to get the OCID of an older image is from the output of the `compute instance get` command of an instance that's using the image.
To see the Compute Cloud@Customer platform images, see [Listing Images and Viewing Details](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm#listing-images-and-viewing-details "On Compute Cloud@Customer, in both the Compute Cloud@Customer Console and CLI, Oracle provided images are listed first, followed by custom images.").
To create an instance using an image provided with Compute Cloud@Customer, see:
  * [Tutorial: Launching Your First Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/tutorial-launching-your-first-instance.htm#tutorial-launching-your-first-instance "In this tutorial, you'll learn the basic features of Compute Cloud@Customer by performing some guided steps to create and connect to an instance. After your instance is up and running, this tutorial steps you through creating and attaching a block volume to your instance.")
  * [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.")


## Initial User Account 🔗 
After you create an instance from a platform image, you initially connect to the instance using `ssh` with the user account `opc`. The `opc` user has `sudo` privileges.
The SSH connection is authenticated using your SSH key pair that's used during instance creation. For more information, see [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
## Remote Access 🔗 
Access to the instance is permitted only over SSH v2 protocol. All other remote access services are disabled.
## Image OS Administration 🔗 
After an image is used to create an instance, the instance OS administration is managed according to the OS type and version. For OSs provided in the platform images, refer to the Oracle Linux and Oracle Solaris documentation available on Oracle Help Center's [Operating Environments](https://docs.oracle.com/en/operating-environments/) page.
Was this article helpful?
YesNo

