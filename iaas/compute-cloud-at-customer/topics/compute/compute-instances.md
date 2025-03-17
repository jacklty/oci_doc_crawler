Updated 2025-01-27
# Compute Instances
Compute Cloud@Customer lets you provision and manage compute instances. 
A compute instance is a virtual machine (VM), which is an independent computing environment that runs on top of physical hardware. The virtualization makes it possible to run multiple compute instances that are isolated from each other.
When you create a compute instance, you can select the most appropriate type of compute instance for your applications based on characteristics such as the number of CPUs, amount of memory, and network resources. See [Tutorial: Launching Your First Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/tutorial-launching-your-first-instance.htm#tutorial-launching-your-first-instance "In this tutorial, you'll learn the basic features of Compute Cloud@Customer by performing some guided steps to create and connect to an instance. After your instance is up and running, this tutorial steps you through creating and attaching a block volume to your instance.") and [Working with Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instances.htm#working-with-instances "On Compute Cloud@Customer, you can create compute instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and delete it.").
After you create a compute instance, you can access it securely from your computer, restart it, attach and detach volumes, and delete it when you're done with it. 
With an instance configuration, you can create a single instance or pool of instances quickly. You can create an instance configuration from an existing instance to replicate that instance more quickly. See [Working with Instance Configurations](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-configurations.htm#working-with-instance-configurations "On Compute Cloud@Customer, an instance configuration contains settings that are used to create compute instances. Instance configurations enable you to consistently create instances with the same configuration without reentering configuration values. You can use an instance configuration to create a single instance or to create an instance pool.").
You can attach instances to a pool or detach instances from a pool manually, or you can configure autoscaling to automatically grow or shrink the pool on a predefined schedule. See [Working with Instance Pools](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-pools.htm#working-with-instance-pools "On Compute Cloud@Customer, instance pools simplify the management of compute instances. An instance pool defines a set of compute instances that's managed as a group. Managing instances as a group enables you to efficiently provision instances and manage the state of instances.").
You can create a pool of compute instances (nodes) in a Kubernetes cluster. See [Kubernetes Engine (OKE) on Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/container-engine-for-kubernetes.htm#container-engine-for-kubernetes "The Kubernetes Engine \(OKE\) is a scalable, highly available service that can be used to deploy any containerized application to Compute Cloud@Customer.").
You can connect to a compute instance. See [Connecting to a Compute Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/connecting-to-a-compute-instance.htm#connecting-to-a-compute-instance "On Compute Cloud@Customer, you can connect to a running instance by using a Secure Shell \(SSH\) or Remote Desktop connection the same way you connect to instances in Oracle Cloud Infrastructure \(OCI\).").
You can back up an instance and restore the instance from backup. See [Backing Up and Restoring an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/backing-up-and-restoring-an-insance.htm#backing-up-and-restoring-an-insance "On Compute Cloud@Customer, supports backing up and restoring instances. The instance backup is created in an Object Storage bucket. From there, you can copy it to another server in your data center for safekeeping. When needed, you can import the backup into any Compute Cloud@Customer Object Storage bucket, and use it to create instances.").
## Components for Creating Instances 🔗 
These components are required to create a compute instance:
**Compartment**
A collection of related resources that are only accessible by certain groups that have been given permission by an administrator in your organization. Compute instances are created in compartments. All compartments exist in a tenancy, which is the root compartment.
**Virtual Cloud Network (VCN)**
A virtual version of a traditional network—including subnets, route tables, and gateways—on which your compute instance runs. At least one cloud network must be set up before you create compute instances.
**SSH Key Pair**
If the image that's used to create the instance is configured to require Secure Shell (SSH) for authentication, then you need an SSH key pair before creating the instance. This requirement applies to instances created from Compute Cloud@Customer platform images and by most UNIX type images. If the image is configured to use passwords instead, you need the password instead of the key pair.
**Image**
A template of a virtual hard drive that determines the OS and other software for a compute instance. You can also create compute instances using these images: 
  * Compute Cloud@Customer platform images
  * Custom images created from other instances
  * Import your own image


For more information about images, see [Images for Compute Cloud@Customer Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/images.htm#images "On Compute Cloud@Customer, an image is a template of a virtual hard drive. The image provides the OS and other software for a compute instance. You specify an image to use when you create a compute instance.").
**Shape**
A template that determines the number of CPUs, amount of memory, and other resources allocated to a newly created compute instance. See [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
## Boot Volumes 🔗 
When you launch a compute instance based on an Compute Cloud@Customer platform image or custom image, a new boot volume for the compute instance is created in the same compartment. That boot volume is associated with that compute instance until you delete the compute instance. 
When you delete the compute instance, you can preserve the boot volume and its data. This feature gives you more control and management options for your compute instance boot volumes, and enables:
  * **Instance scaling:** When you delete your compute instance, you can keep the associated boot volume and use it to launch a new compute instance using a different compute instance type or shape. This flexibility enables you to easily scale up or down the number of cores for a compute instance. 
  * **Troubleshooting and repair:** If you think a boot volume issue is causing a compute instance problem, you can stop the compute instance and detach the boot volume. Then you can attach it to another compute instance as a data volume to troubleshoot it. After resolving the issue, you can then reattach it to the original compute instance or use it to launch a new compute instance.


**Boot volume Encryption**
Boot volumes are encrypted by default, the same as other block storage volumes.
**Important**
In most cases, encryption isn't supported for compute instances launched from custom images imported for "bring your own image" (BYOI) scenarios.
For more information about Compute Cloud@Customer boot volumes, see [Managing Boot Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-boot-volumes.htm#managing-boot-volumes "On Oracle Cloud Infrastructure, when you launch an instance, a new boot volume for the instance is created in the same compartment and attached to the instance.")
For information about backing up boot volumes, see [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
## Storage for Instances 🔗 
You can expand the storage that's available for your compute instances with the following services:
  * **Block Volume:** Lets you dynamically provision and manage block volumes that you can attach to one or more compute instances. See [Block Volume Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage "On Compute Cloud@Customer, Block Volumes provide high-performance network storage capacity that supports a broad range of I/O intensive workloads.").
  * **File Storage:** A durable, scalable, secure, enterprise-grade network file system that you can connect to from any compute instance in your virtual cloud network (VCN). See [File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/file-storage.htm#file-storage "On Compute Cloud@Customer, the File Storage service provides a durable, scalable, secure network file system. You can connect to a File Storage service file system from any Compute Cloud@Customer compute instance in your Virtual Cloud Network \(VCN\).").
  * **Object Storage:** An internet-scale, high-performance storage platform that lets you store a large amount of unstructured data of any content type. This storage not tied to any specific compute instance. See [Object Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/object-storage.htm#object-storage "On Compute Cloud@Customer, the Object Storage service provides reliable and cost-efficient data durability.").


## Simplifying Compute Instance Management 🔗 
You can simplify the management of your compute instances using these features:
  * **[Instance Configurations](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-configurations.htm#working-with-instance-configurations "On Compute Cloud@Customer, an instance configuration contains settings that are used to create compute instances. Instance configurations enable you to consistently create instances with the same configuration without reentering configuration values. You can use an instance configuration to create a single instance or to create an instance pool."):** Are templates that define the settings to use when creating compute instances.
  * **[Instance Pools](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instance-pools.htm#working-with-instance-pools "On Compute Cloud@Customer, instance pools simplify the management of compute instances. An instance pool defines a set of compute instances that's managed as a group. Managing instances as a group enables you to efficiently provision instances and manage the state of instances."):** are a group of compute instances that are created from the same compute instance configuration and managed as a group.


## **Calling Services from an Instance** 🔗 
A Compute Cloud@Customer instance can be configured to enable applications running on the instance to call services and manage resources similar to the way users call services to manage resources. 
An instance that can perform actions on service resources is called an _instance principal_. 
You can authorize an instance to make API calls in Compute Cloud@Customer services. After you set up the required resources and policies, an application running on an instance can callCompute Cloud@Customer public services, removing the need to configure user credentials or a configuration file.
See [Configuring Instances for Calling Services](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/configuring-instances-for-calling-services.htm#configuring-instances-for-calling-services "A Compute Cloud@Customer compute instance can be configured to enable applications running on the instance to call services and manage resources similar to the way Compute Cloud@Customer users call services to manage resources.").
## Metadata Key Restrictions 🔗 
Metadata keys have the following restrictions, with the noted exceptions:
  * Metadata can have a maximum of 128 keys.
  * Key names can have a maximum of 255 characters.
  * Most key values can have a maximum of 255 characters.


The value of the `ssh_authorized_keys` metadata key can be more than 255 characters. This value must be a valid public key in OpenSSH format. Use a newline character to separate multiple keys.
The value of the `user_data` metadata key can be a maximum of 16KB. This value is data that cloud-init can use to run custom scripts or provide custom cloud-init configuration. For Linux instances with cloud-init configured, the `user_data` value is a Base64-encoded string of cloud-init user data. For more information, see [cloud-init data formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html).
Was this article helpful?
YesNo

