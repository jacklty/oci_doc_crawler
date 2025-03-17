Updated 2025-02-13
# Overview of the Compute Service
Oracle Cloud Infrastructure [Compute](https://www.oracle.com/cloud/compute/) lets you provision and manage compute hosts, known as instances. You can create instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and terminate it when you're done with it. Any changes made to the instance's local drives are lost when you terminate it. Any saved changes to volumes attached to the instance are retained.
Oracle Cloud Infrastructure offers both bare metal and virtual machine instances:
  * **Bare metal:** A bare metal compute instance gives you dedicated physical server access for highest performance and strong isolation. 
  * **Virtual machine:** A virtual machine (VM) is an independent computing environment that runs on top of physical bare metal hardware. The virtualization makes it possible to run multiple VMs that are isolated from each other. VMs are ideal for running applications that do not require the performance and resources (CPU, memory, network bandwidth, storage) of an entire physical machine.
An Oracle Cloud Infrastructure VM compute instance runs on the same hardware as a bare metal instance, leveraging the same cloud-optimized hardware, firmware, software stack, and networking infrastructure.


Learn more about the [Compute service and related services](https://www.oracle.com/cloud/compute/).
Be sure to review [Best Practices for Your Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Best_Practices_for_Your_Compute_Instance) for important information about working with your Compute instances.
Linux instances on Oracle Cloud Infrastructure can use Oracle Ksplice to apply critical kernel patches without rebooting. Ksplice can maintain specific kernel versions for Oracle Linux, CentOS, and Ubuntu. For more information, see [Oracle Ksplice](https://docs.oracle.com/iaas/oracle-linux/ksplice/index.htm).
Compute is Always Free eligible. For more information about Always Free resources, including capabilities and limitations, see [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
## Instance Types 🔗 
When you create a compute instance, you can select the most appropriate type of instance for your applications based on characteristics such as the number of CPUs, amount of memory, and network resources.
### Instance Features 🔗 
Oracle Cloud Infrastructure offers features that let you customize your instances for specialized workloads and security requirements.
  * **Burstable instances** are virtual machine (VM) instances that provide a baseline level of CPU performance with the ability to burst to a higher level to support occasional spikes in usage. For more information, see [Burstable Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances).
  * **Shielded instances** harden the firmware security on bare metal hosts and virtual machines (VMs) to defend against malicious boot level software. For more information, see [Shielded Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded).
  * **Extended memory VMs** are VM instances that provide more memory and cores than available with standard shapes. For more information, see [Extended Memory VM Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-vm-instances "Extended memory virtual machine \(VM\) instances are VM instances that provide more memory and cores than available with standard shapes.").


### Shape Types 🔗 
Oracle Cloud Infrastructure offers a variety of shapes that are designed to meet a range of compute and application requirements:
  * **Standard shapes:** Designed for general purpose workloads and suitable for a wide range of applications and use cases. Standard shapes provide a balance of cores, memory, and network resources. Standard shapes are available with Intel, AMD, and Arm-based processors.
  * **DenseIO shapes:** Designed for large databases, big data workloads, and applications that require high-performance local storage. DenseIO shapes include locally-attached NVMe-based SSDs. 
  * **GPU shapes:** Designed for hardware-accelerated workloads. GPU shapes include Intel or AMD CPUs and NVIDIA graphics processors. Some bare metal GPU shapes support cluster networking.
  * **High performance computing (HPC) and optimized shapes:** Designed for high-performance computing workloads that require high frequency processor cores. Bare metal HPC and optimized shapes support cluster networking. 


For more information about the available bare metal and VM shapes, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes), [Bare Metal Instances](https://www.oracle.com/cloud/compute/bare-metal.html), [Virtual Machines](https://www.oracle.com/cloud/compute/virtual-machines.html), and [Virtual Machines and Bare Metal (GPU)](https://www.oracle.com/cloud/compute/gpu.html).
### Flexible Shapes 🔗 
[Flexible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible) let you customize the number of OCPUs and the amount of memory allocated to an instance. When you [create a VM instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") using a flexible shape, you select the number of OCPUs and the amount of memory that you need for the workloads that run on the instance. The network bandwidth and number of VNICs scale proportionately with the number of OCPUs. This flexibility lets you build VMs that match your workload, enabling you to optimize performance and minimize cost.
### Capacity Types 🔗 
You can choose the type of host capacity to use when launching compute instances. On-demand capacity is the default, but you can use preemptible capacity, capacity reservations, or dedicated capacity instead.
  * **On-demand capacity:** Pay for only the compute capacity that you use. With on-demand capacity, you pay for compute capacity by the second, and [depending on the shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm#top "When you stop an Oracle Cloud Infrastructure Compute instance, billing for the stopped instance depends on the shape that you used to create the instance."), you pay only for the seconds that your instances are running. Capacity availability is not guaranteed when launching large workloads.
  * **Preemptible capacity:** Preemptible capacity allows you to save money by using preemptible instances to run workloads that only need to run for brief periods or that can be interrupted when the capacity is reclaimed. Preemptible instances behave the same as regular compute instances, but the capacity is reclaimed when it's needed elsewhere, and the instances are terminated. For more information, see [Preemptible Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#preemptible).
  * **Reserved capacity:** Reserve capacity for future usage, and ensure that capacity is available to create Compute instances whenever you need them. The reserved capacity is used when you launch instances against the reservation. When these instances are terminated, the capacity is returned to the reservation, and the unused capacity in the reservation increases. Unused reserved capacity is metered differently than used reserved capacity. For more information, see [Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity).
  * **Dedicated capacity:** Run VM instances on dedicated servers that are a single tenant and not shared with other customers. This feature lets you meet compliance and regulatory requirements for isolation that prevent you from using shared infrastructure. You can also use this feature to meet node-based or host-based licensing requirements that require you to license an entire server. For more information, see [Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#Dedicated_Virtual_Machine_Hosts).


Service limits and compartment quotas apply to all types of host capacity. For reserved capacity, if your request for reserved capacity will exceed your service limits, request a service limit increase before you reserve the capacity. For more information, see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
## Components for Launching Instances 🔗 
The components required to launch an instance are: 

availability domain 
    The Oracle Cloud Infrastructure data center within your geographical region that hosts cloud resources, including your instances. You can place instances in the same or different availability domains, depending on your performance and redundancy requirements. For more information, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). 

virtual cloud network
    A virtual version of a traditional network—including subnets, route tables, and gateways—on which your instance runs. At least one cloud network has to be set up before you launch instances. For information about setting up cloud networks, see [Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). 

key pair (for Linux instances)
    A security mechanism required for Secure Shell (SSH) access to an instance. Before you launch an instance, you'll need at least one key pair. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances). 

password (for Windows instances)
    A security mechanism required to access an instance that uses a Windows platform image. The first time you launch an instance using a Windows image, Oracle Cloud Infrastructure will generate an initial, one-time password that you can retrieve using the console or API. This password must be changed after you initially log on. 

image
    
A template of a virtual hard drive that determines the operating system and other software for an instance. You can launch instances from these sources:
  * Oracle Cloud Infrastructure [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images).
  * Trusted third-party images published by Oracle partners from the Partner Image catalog. For more information about partner images, see [Overview of Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/overview-marketplace.htm) and [Working with Listings](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/workingwithlistings.htm).
  * Pre-built Oracle enterprise images and solutions enabled for Oracle Cloud Infrastructure.
  * [Custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image."), including [bring your own image scenarios](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI).
  * [Community images](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/publishingcommunityapplications.htm), created and published by community members for use by other community members.
  * [Boot volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm).



shape
    A template that determines the number of CPUs, amount of memory, and other resources allocated to a newly created instance. You choose the most appropriate shape when you launch an instance. See [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) for a list of available bare metal and VM shapes. 

tags
    
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
You can optionally attach volumes to an instance. For more information, see [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm).
**Note** Resources that are created and used by compute instances, such as boot volumes and network traffic, are billed separately from the compute instance.
## Creating Automation with Events 🔗 
You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
The following Compute resources emit events:
  * Autoscaling configurations and autoscaling policies
  * Cluster networks
  * Console histories
  * Images
  * Instances and instance attachments
  * Instance configurations
  * Instance console connections
  * Instance pools


## Resource Identifiers 🔗 
Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
## Work Requests 🔗 
Compute is one of the Oracle Cloud Infrastructure services that is integrated with the Work Requests API. For general information on using work requests in Oracle Cloud Infrastructure, see [Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm) in the user guide, and the [Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/).
## Ways to Access Oracle Cloud Infrastructure 🔗 
You can access Oracle Cloud Infrastructure (OCI) by using the [Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm) (a browser-based interface), [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or [OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To access the [Console](https://cloud.oracle.com/), you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You are prompted to enter your cloud tenant, your user name, and your password.
For general information about using the API, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).
## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
## Security 🔗 
In addition to creating IAM policies, follow these security best practices for Compute.
  * Encrypt boot volumes with a custom key, and rotate keys
  * Apply the latest security patches to instances
  * Use Oracle Cloud Guard to detect and respond to security problems
  * Perform a security audit


See [Securing Compute](https://docs.oracle.com/iaas/Content/Security/Reference/compute_security.htm).
**Tip** You can control network access to OCI **resources** by applying security attributes to them and creating policies to control communication among them. For more information, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
## Storage for Compute Instances 🔗 
You can expand the storage that's available for your compute instances with the following services:
  * **Block Volume:** Lets you dynamically provision and manage block volumes that you can attach to one or more compute instances. See [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) for more information. For steps to attach block volumes to compute instances, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm) and [Attaching a Volume to Multiple Instances](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm). 
  * **File Storage:** A durable, scalable, secure, enterprise-grade network file system that you can connect to from any compute instance in your virtual cloud network (VCN). See [Overview of File Storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm) for more information. 
  * **Object Storage:** An internet-scale, high-performance storage platform that lets you store an unlimited amount of unstructured data of any content type. This storage is regional and not tied to any specific compute instance. See [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm) for more information. 
  * **Archive Storage:** A storage platform that lets you store an unlimited amount of unstructured data of any content type that doesn't require instantaneous data retrieval. This storage is regional and not tied to any specific compute instance. See [Overview of Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) for more information. 


## Limits on Compute Resources 🔗 
For a list of applicable limits and [instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
Additional limits include:
  * To attach a volume to an instance, both the instance and volume must be within the same availability domain.
  * Many Compute operations are subject to [throttling](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#throttle).


A service limit is different from host capacity. A service limit is the quota or allowance set on a resource. Host capacity is the physical infrastructure that resources such as compute instances run on. If you get an "Out of host capacity" error when you try to create an instance or change the shape of an instance, [try the suggested workarounds](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#out-of-host-capacity-error-when-creating-compute-instances).
### Metadata Key Limits 🔗 
Custom metadata keys (any key you define that is not `ssh_authorized_keys` or `user_data`) have the following limits:
  * Max number of metadata keys: 128
  * Max size of key name: 255 characters
  * Max size of key value: 255 characters


`ssh_authorized_keys` is a special key that does not have these limits, but its value is validated to conform to a public key in the OpenSSH format.
`user_data` has a maximum size of 16KB. For Linux instances with cloud-init configured, you can populate the `user_data` field with a Base64-encoded string of cloud-init user data. For more information on formats that cloud-init accepts, see [cloud-init formats](http://cloudinit.readthedocs.io/en/latest/topics/format.html). 
Was this article helpful?
YesNo

