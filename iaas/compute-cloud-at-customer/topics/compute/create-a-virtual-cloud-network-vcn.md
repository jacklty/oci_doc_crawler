Updated 2024-08-06
# Task 2: Create a Virtual Cloud Network (VCN)
Before you can launch an instance, you need a virtual cloud network (VCN) and a subnet.
A VCN is a software-defined equivalent of a traditional network, with firewall rules and various types of communication gateways.
In a production environment, a VCN that you can use for the instance might already exist, and you could use it instead of creating a new VCN. However, in this tutorial, you create a new VCN to learn how to do it.
**Important**
This tutorial creates a simple cloud network to make it easy to launch an instance for learning purposes. When you create your production instances, ensure that you create appropriate security lists and route table rules to restrict network traffic to your instances.
For more information, see [Managing VCNs and Subnets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-vcns-and-subnets.htm#managing-vcns-and-subnets "On Compute Cloud@Customer,").
Avoid entering confidential information in names and tags.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
  2. Click **Create Virtual Cloud Network**.
  3. In the **Create Virtual Cloud Network** dialog box, enter the following information:
     * **Name:** Enter a descriptive name for the cloud network.
     * **Create in Compartment:** Select the Sandbox compartment.
     * **CIDR Block:** Enter a valid CIDR block for the VCN. For example 10.0.0.0/16.
     * **Use DNS hostnames in this VCN:** Indicate whether you want to use DNS host names in the VCN.
     * **DNS Label:** If you selected to use DNS, enter a DNS label or leave the field blank to let the system generate a DNS name for you.
     * **Tagging:** Leave blank. This tutorial doesn't use tags.
  4. Click **Create Virtual Cloud Network**.


**Perform the next task:**
[Task 3: Create a Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-a-subnet.htm#create-a-subnet "A subnet is a subdivision of your VCN. The subnet directs traffic according to a route table.")
Was this article helpful?
YesNo

