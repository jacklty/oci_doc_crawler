Updated 2024-11-26
# Arm-Based Compute
OCI Ampere Compute is a general-purpose, Arm-based compute platform based on the Ampere processor. OCI Ampere A1 Compute (based on Ampere Altra processors) and OCI Ampere A2 Compute (based on AmpereOne processors) instances provide superior price-performance, near linear scaling, built-in security due to the single-threaded core architecture, and a broad developer ecosystem.
Arm processors, ubiquitous in mobile computing, are increasingly used in PCs, laptops, and servers. Arm processors use a reduced instruction set computing (RISC) architecture, which requires less power and less silicon for each core than x86 processors. Arm puts more cores in a CPU socket and provides more dedicated resources for each core. As a result, Arm processors provide predictable performance, provide the highest density of cores, and consume less power. [OCI Ampere Compute](https://www.oracle.com/cloud/compute/arm/) eases and optimizes server-side development on Arm by providing the performance, features, and scalability required for cloud-to-edge infrastructure on Arm
[OCI Ampere Compute](https://www.oracle.com/cloud/compute/arm/) instances are suitable for a wide range of applications and use cases. For example:
  * Containerized workloads (for example, Kubernetes)
  * CPU-based AI and machine learning (ML) inferencing
  * Databases and in-memory databases, including MySQL
  * Web and cloud native applications
  * Mobile apps and game development
  * Media services and video streaming


Oracle's development stack is available on OCI Ampere Compute, including Oracle Linux, Java, MySQL, GraalVM, and Oracle Cloud Infrastructure Kubernetes Engine. To make it easier to start developing on OCI Ampere Compute, you can use the pre-built [Oracle Linux Cloud Developer](https://blogs.oracle.com/linux/develop-arm-applications-quickly-using-oracle-linux-cloud-developer-image) platform image. For a full list of open source organizations and partners that have developed solutions for OCI Ampere Compute, see the [ product page](https://www.oracle.com/cloud/compute/arm/).
## Creating Arm-Based Compute Instances 🔗 
You can create Arm-based virtual machine (VM) instances using OCI A1 (Compute) and OCI A2 (Compute). If you require bare-metal instances, you can use OCI A1 (Compute). If you are an existing OCI A1 (Compute) customer interested in testing or migrating to OCI A1 (Compute) and OCI A2 (Compute), no re-architecting is required.
**Tip** If this is your first time creating an instance, for a complete guided workflow see: [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.").
If you're already familiar with Oracle Cloud Infrastructure and want to explore the full set of configuration options that are available when you create an instance, follow the [detailed steps to create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
**Flexible hardware specifications:** The OCI Ampere A1 Compute **shapes** include the BM.Standard.A1.160 shape for bare metal instances and the VM.Standard.A1.Flex shape for VMs. The OCI Ampere A2 Compute shapes include VM.Standard.A2.Flex for VMs. For information about the OCPU count, memory, storage, and networking details of these shapes, see [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).
Because the OCI Ampere Compute shapes for VMs are a [flexible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible), you can customize the number of OCPUs and amount of memory that are allocated to each instance. This flexibility lets you build VMs that match your workload, enabling you to optimize performance and minimize cost.
**Images:** We recommend the Oracle Linux Cloud Developer image, available as a [platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#images). [Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/developer/index.htm) provides the latest development tools, languages and Oracle Cloud Infrastructure software development kits (SDKs) to rapidly launch a comprehensive development environment. The Oracle Linux and Ubuntu platform images are also supported.
**Managing instances:** After you create an OCI Ampere Compute instance, you can use many of the features that are available for compute instances. For example:
  * [Monitor the health, capacity, and performance of your instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics) by using metrics, alarms, and notifications.
  * [Adjust the number of OCPUs, memory, and other resources that are allocated to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance). This lets you scale up your compute resources for increased performance, or scale down to reduce cost, without having to rebuild your instances or redeploy your applications.


## Getting Started with OCI Ampere A1 Compute for Free 🔗 
All tenancies on OCI A1 (Compute), including paid and trial accounts, get the first 3,000 OCPU hours and 18,000 GB hours per month for free for OCI Ampere A1 Compute. For more information see [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/).
## Developing on Arm-based Compute 🔗 
Oracle's developer stack for Arm includes the following resources:
  * [Oracle Java SE Embedded and JDK for ARM documentation](https://docs.oracle.com/java/)
  * [Get Started with GraalVM for Linux AArch64](https://www.graalvm.org/docs/getting-started/)
  * [Oracle Linux 7](https://docs.oracle.com/en/operating-systems/oracle-linux/7/), [Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/index.html), and [Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/index.html) documentation and release notes for Arm (aarch64)


## Tutorials and Reference Architectures 🔗 
To get started with OCI Ampere A1 Compute, follow the step-by-step instructions in these tutorials:
  * [Deploy Java applications on Oracle Cloud Infrastructure Ampere A1](https://docs.oracle.com/en/learn/java_app_ampere_oci/index.html)
  * [Get started with GraalVM on Oracle Cloud Infrastructure Ampere A1](https://docs.oracle.com/en/learn/oci_graalvm_ampere_a1/index.html)
  * [Deploy Nextcloud on Oracle Cloud Infrastructure Ampere A1](https://docs.oracle.com/en/learn/oci_nextcloud_ampere_a1/index.html)
  * [Get Started with Arm-Based Kubernetes Clusters in Oracle Cloud Infrastructure](https://docs.oracle.com/en/learn/arm_oke_cluster_oci/index.html)
  * [Set up WordPress with MySQL Database and Matomo Analytics using Arm-based Ampere A1 Compute resources](https://docs.oracle.com/en/solutions/wordpress-arm-based-oci/index.html)
  * [Deploy Apache Tomcat on Arm-based Ampere A1 compute connected to an Autonomous Database](https://docs.oracle.com/en/solutions/deploy-tomcat-adb/)


## Deploying Containerized Applications on OCI Ampere Compute 🔗 
OCI Ampere Compute is a native cloud platform designed for running containers to build native cloud workloads.
Use [Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm) to define and create Kubernetes clusters to enable the deployment, scaling, and management of containerized applications. For more information, see [Running Applications on Arm-based Nodes](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengrunningarmnodes.htm).
Use [Oracle Cloud Infrastructure Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm) to store, share, and manage development artifacts like Docker images in an Oracle-managed registry.
## Community and Other Resources 🔗 
To connect with other Arm developers, join the community:
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure+arm)
  * [Arm Compute Forum on Cloud Customer Connect](https://cloudcustomerconnect.oracle.com/resources/3de6cdb42f/summary)
  * [Apps for Arm on Marketplace](https://cloudmarketplace.oracle.com/marketplace/en_US/homePage.jspx)


Was this article helpful?
YesNo

