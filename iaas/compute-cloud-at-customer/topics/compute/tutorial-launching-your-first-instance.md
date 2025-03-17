Updated 2024-10-07
# Tutorial: Launching Your First Instance
In this tutorial, you'll learn the basic features of Compute Cloud@Customer by performing some guided steps to create and connect to an instance. After your instance is up and running, this tutorial steps you through creating and attaching a block volume to your instance.
This tutorial also includes optional instructions for deleting all the resources you create.
## Prerequisites 🔗 
To successfully perform this tutorial, you must have the following prerequisites in place.
  * You must be able to sign in to the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") using your Oracle Cloud Infrastructure (OCI) account.
  * You must be able to sign in to Oracle Cloud Console using your Oracle Cloud Infrastructure (OCI) account. Or have access to a compartment where you can create resources.
  * An SSH key pair that's used for user authentication in the instance. If you want to create a key pair for this tutorial, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).


## Tutorial Tasks 🔗 
[Task 1: Create a Compartment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-a-compartment.htm#create-a-compartment "On Compute Cloud@Customer, compartments help you organize and control access to your resources. A compartment is a collection of resources \(such as cloud networks, compute instances, and block volumes\) that can be accessed only by those groups that have been given permission by an administrator in your organization.")
[Task 2: Create a Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-a-virtual-cloud-network-vcn.htm#create-a-virtual-cloud-network-vcn)
[Task 3: Create a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-a-subnet.htm#create-a-subnet "A subnet is a subdivision of your VCN. The subnet directs traffic according to a route table.")
[Task 4: Create an Internet Gateway and Configure Route Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-an-internet-gateway-and-configure-route-rules.htm#create-an-internet-gateway-and-configure-route-rules "An internet gateway is an optional virtual router you can add to your VCN to enable access to your data center network.")
[Task 5: Launch an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/5-launch-an-instance.htm#_5-launch-an-instance "In this task, launch an instance with an image and a shape.")
[Task 6: Get the Instance IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/6-get-the-instance-ip-address.htm#_6-get-the-instance-ip-address "You connect to the instance using SSH with the instance IP address.")
[Task 7: Connect to Your Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/7-connect-to-your-instance.htm#_7-connect-to-your-instance "Connect to your instance using SSH.")
[Task 8: Add a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/8-add-a-block-volume.htm#add-a-block-volume "Add additional storage by adding a block volume to your instance.")
[Task 9: Attach the Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/9-attach-the-block-volume-to-an-instance.htm#attach-the-block-volume-to-an-instance "Attach the block volume to an instance.")
[Task 10: (Optional) Clean Up Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#clean-up-resources "After you've finished with the resources you created for this tutorial, you can delete and release the resources you no longer plan to use.")
Was this article helpful?
YesNo

