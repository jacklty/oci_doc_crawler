Updated 2024-08-06
# Overview of Compute Cloud@Customer
Use Compute Cloud@Customer to deploy Oracle Cloud Infrastructure services on-premises, to meet data sovereignty and regulatory requirements, while using OCI's identity and governance services to manage access to them.
With a Compute Cloud@Customer subscription, you maintain absolute control over your data while leveraging the capabilities of Oracle Cloud Infrastructure managed by Oracle. The Compute Cloud@Customer rack is installed in your data center, connected to your Oracle Cloud Infrastructure tenancy, and fully managed by Oracle.
Compute Cloud@Customer is engineered to deliver a comprehensive suite of cloud infrastructure services within the secure environment of your on-premises data center. The system integrates all required hardware and software components, and has been tested, configured and tuned for the best performance by Oracle engineers. It's a flexible, general purpose IaaS (Infrastructure as a Service) solution in the sense that it supports a wide variety of workloads. Its pluggable platform provides an excellent foundation to layer PaaS (Platform as a Service) and SaaS (Software as a Service) solutions on top of the infrastructure. 
The cloud operations team uses best-in-class operational processes to secure and monitor the underlying cloud infrastructure. The cloud operations team is responsible for ongoing maintenance of the IaaS platform (upgrades and patching), incident management, and monitoring with OCI-native services.
Oracle installs and initializes the Compute Cloud@Customer infrastructure in your data center. Oracle continues to monitor and maintain the infrastructure over the lifespan of the service. 
The following diagram shows how Compute Cloud@Customer infrastructure is securely connected to your tenancy in an Oracle Cloud Infrastructure region over an uninterruptible network. The connection is persistent. The system can tolerate short interruptions in network connectivity, but such interruptions are treated as faults and must be resolved as quickly as possible.
![A diagram showing your tenancy in an OCI region, and how it connects to Compute Cloud@Customer in your data center.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/c3-overview-diagram.png)
**Authentication**
Compute Cloud@Customer uses the same federated identity provider that you use for Oracle Cloud Infrastructure to manage Console sign ins. See [Federated Identity Providers](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/federated-identity-providers.htm#federated-identity-providers "The Compute Cloud@Customer service uses the same federated identity provider that provides your identity services to Oracle Cloud Infrastructure. The identity provider manages usernames, passwords, and authentication to access the service.").
**IAM Resources**
Your Oracle Cloud Infrastructure IAM resources are regularly and securely cached in the Compute Cloud@Customer infrastructure. This enables you to manage IAM resources in one location. If you change IAM resources in the OCI tenancy, the changes are automatically applied to resources in Compute Cloud@Customer. See [IAM Overview](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/identify-learn.htm#identify-learn "On Compute Cloud@Customer, the Oracle Cloud Infrastructure Identity and Access Management \(IAM\) service lets you control who has access to the cloud resources within your tenancies.").
**User Interfaces**
You use the Oracle Cloud Infrastructure Console, CLI, and APIs to manage the following items:
  * Initial connection of the Compute Cloud@Customer infrastructure to your tenancy in Oracle Cloud Infrastructure.
  * Schedules for when Oracle can upgrade Compute Cloud@Customer.
  * Identity and Access Management (IAM), including users, groups, policies, compartments, and tags.
  * Billing and payment information.
  * Oracle's access to Compute Cloud@Customer using Oracle Operator Access Control.


To manage resources such as VCNs, instances, and storage, on Compute Cloud@Customer, use the following interfaces:
  * **OCI API** (Compute Cloud@Customer supports a subset of operations)
  * **OCI CLI** (Compute Cloud@Customer supports a subset of operations)
  * **Compute Cloud@Customer Console** – a browser UI that offers a similar user experience to the Oracle Cloud Console.


For information about accessing your resources, see [Signing in to Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/accessing.htm#accessing "Use the Compute Cloud@Customer Console, CLI, and API to create and manage resources on an infrastructure you have configured and connected to Oracle Cloud Infrastructure.").
**Cloud Resources**
When you sign in to Compute Cloud@Customer, you can create and manage the same types of resources that you can create in Oracle Cloud Infrastructure:
  * **Instances:** You can select the most appropriate type of instance for your applications based on characteristics such as the number of CPUs, amount of memory, and network resources. You can deploy the instance with any of the provided platform images, or bring your own image. See [Compute Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-instances.htm#compute-instances "Compute Cloud@Customer lets you provision and manage compute instances.") and [Images for Compute Cloud@Customer Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/images.htm#images "On Compute Cloud@Customer, an image is a template of a virtual hard drive. The image provides the OS and other software for a compute instance. You specify an image to use when you create a compute instance.").
  * **Virtual Cloud Networks (VCNs):** A virtual version of a traditional network, including subnets, route tables, and gateways, on which your instance runs. At least one cloud network must be set up before you create instances. For information about setting up cloud networks see [Virtual Cloud Networks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/virtual-cloud-networks.htm#networking "On Compute Cloud@Customer, networking enables you to set up virtual versions of traditional network components.").
  * **Block Volumes:** Lets you dynamically provision and manage block volumes that you can attach to one or more compute instances. See [Block Volume Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/block-volume-storage.htm#block-volume-storage "On Compute Cloud@Customer, Block Volumes provide high-performance network storage capacity that supports a broad range of I/O intensive workloads.").
  * **File Storage:** A durable, scalable, secure, enterprise-grade network file system that you can connect to from any compute instance in your virtual cloud network (VCN). See [File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/file-storage.htm#file-storage "On Compute Cloud@Customer, the File Storage service provides a durable, scalable, secure network file system. You can connect to a File Storage service file system from any Compute Cloud@Customer compute instance in your Virtual Cloud Network \(VCN\)."). 
  * **Object Storage:** A high-performance storage platform that lets you store unstructured data of any content type. This storage is regional and not tied to any specific compute instance. See [Object Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/object-storage.htm#object-storage "On Compute Cloud@Customer, the Object Storage service provides reliable and cost-efficient data durability."). 


**Upgrades**
System upgrades are designed for minimum disruption and maximum availability. Health checks are performed before an upgrade to ensure that all components are in an acceptable state. The upgrade process is modular and only upgrades components – such as firmware, OSs, containerized services, or the system's main database - as needed. Oracle performs all upgrades, but you can determine the upgrade time frame.
Was this article helpful?
YesNo

