Updated 2023-09-30
# BIOS Settings for Bare Metal Instances
When you create a bare metal compute instance, you can optionally configure advanced BIOS settings that let you optimize performance. For example, you can disable simultaneous multithreading to optimize the NUMA settings.
**Tip** These settings are for advanced users.
**Important** Disabling cores by configuring advanced BIOS settings isn't a valid means for determining or limiting the number of Oracle software licenses required for a bare metal instance in a bring your own license scenario.
The settings that are available depend on the shape. To see which settings are available for a given shape, refer to [LaunchInstancePlatformConfig](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/LaunchInstancePlatformConfig) in the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation. You can also see which settings are available when you [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bios-settings.htm#configuring__console) using the Console.
## Core Disabling 🔗 
You can disable cores to use fewer cores than the full size of the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes). The instance itself is billed for the full shape, regardless of whether all cores are enabled.
The following options are available:
  * Use 25% of available cores
  * Use 50% of available cores
  * Use 75% of available cores
  * Use 100% of available cores


The system rounds up the number of cores across processors and provisions an instance with a whole number of cores.
## NUMA Settings 🔗 
Used to optimize performance for workloads that are highly tuned for performance and have significant memory access. Non-uniform memory access (NUMA) configures how the memory is interleaved between cores and memory channels in the CPU.
NUMA is a computer memory design used in multi-core CPUs. With NUMA, the time it takes to access the memory depends on the physical location of the memory relative to the CPU. CPUs have memory channels that are connected to the memory modules (called DIMMs). The NUMA setting configures how the processor cores access the memory channels, and thereby the memory, on the CPU.
With the default NUMA setting, memory is interleaved across all channels of the CPU. Because of the location of the memory channels relative to the cores, this results in different access times for different memory locations. For most workloads, the difference does not have an effect: the difference is typically in nanoseconds, and is negligible compared to the software running on the CPU.
For high-performance computing (HPC) applications that are memory sensitive and highly tuned for performance, you can get predictable performance by configuring the NUMA settings. For example, you can choose a NUMA setting that uses only the memory that's closer to the core, resulting in higher memory bandwidth and lower memory latency.
The NUMA settings that are available depend on the processor type.
### Intel shapes 🔗 
On Intel CPUs, you can enable or disable sub-NUMA clustering (SNC). Intel CPUs have eight memory channels, divided into four groups of two channels each. When SNC is enabled, the cores are split into two separate clusters, each with four memory channels, resulting in two NUMA domains within a physical processor socket. The following options are available:
  * **NPS1:** Disables sub-NUMA clustering. This is the default.
  * **NPS2:** Enables sub-NUMA clustering.


### AMD shapes 🔗 
On AMD CPUs, you can configure the number of NUMA nodes per socket (NPS). AMD CPUs have 64 cores divided into eight chiplets, and each chiplet has eight cores. The chiplets are grouped into four groups, with two chiplets in each group. The CPU has eight memory channels. The following options are available:
  * **NPS0:** One NUMA domain across two CPUs in a dual-socket system. For a shape with 128 cores, this means that memory for all 128 cores is interleaved across all 16 memory channels.
  * **NPS1:** One NUMA domain per CPU. Memory for a CPU uses only the memory channels of that CPU, and does not perform cross-socket memory access. For a shape with 128 cores, this means that memory for all 64 cores is interleaved across all eight memory channels. This is the default.
  * **NPS2:** Two NUMA domains. For a shape with 128 cores, this means that memory from 32 cores is interleaved across four memory channels.
  * **NPS4:** Four NUMA domains. For a shape with 128 cores, this means that memory from 16 cores is interleaved across two memory channels.


## Simultaneous Multithreading 🔗 
Lets you configure whether a single core (OCPU) allows multiple independent hardware execution threads. Simultaneous multithreading (SMT) is also called symmetric multithreading or Intel Hyper-Threading.
Intel and AMD processors have two hardware execution threads per core. SMT permits multiple independent threads of execution per core. In many cases, multithreading lets the instance better use the resources and increase the efficiency of the CPU.
When you disable multithreading, only one thread can run on each core. This can provide higher or more predictable performance for some workloads, such as high-performance computing (HPC) workloads with many floating-point operations. Disabling multithreading can also provide better performance for some older versions of Windows that have issues with larger core counts.
## Access Control Service 🔗 
Access control service lets the platform enforce PCIe device isolation, required for VFIO device pass-through. You can enable or disable access control service.
## Virtualization Instructions 🔗 
Virtualization instructions include Secure Virtual Machine for AMD shapes or VT-x for Intel shapes. You can enable or disable virtualization instructions.
## Input-Output Memory Management Unit 🔗 
Lets you control whether I/O memory access goes through the input-output memory management unit (IOMMU). You can enable or disable the IOMMU.
When the IOMMU is enabled, the IOMMU can isolate user space applications from untrusted code running on the physical host. For bare metal shapes with remote direct memory access (RDMA) networks, by default, I/O memory access that travels over the RDMA network bypasses the IOMMU, going directly to the cluster network interface card (NIC) for higher performance.
## Configuring BIOS Settings 🔗 
You can customize the BIOS settings when you create a bare metal instance. The settings cannot be changed after you create the instance.
### Using the Console 🔗 
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the **Image and shape** section.
  2. Click **Change shape**.
  3. Select a bare metal shape, and then click **Show advanced BIOS settings**. Select the options that you want to configure. The settings that are available depend on the shape.
  4. Click **Select shape**.
  5. Finish creating the instance, and then click **Create**.


### Using the API 🔗 
Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation, specifying the BIOS settings in the `platformConfig` object.
Was this article helpful?
YesNo

