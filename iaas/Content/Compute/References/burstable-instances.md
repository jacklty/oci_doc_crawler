Updated 2024-04-15
# Burstable Instances
A burstable instance is a virtual machine (VM) instance that provides a baseline level of CPU performance with the ability to burst to a higher level to support occasional spikes in usage.
Burstable instances are designed for scenarios where an instance is typically idle, or has low CPU utilization with occasional spikes in usage. They're also ideal for scaled-down workloads that don't require a full core. For example:
  * Microservices
  * Development and test environments
  * Continuous integration and continuous delivery (CI/CD) tools
  * Monitoring systems
  * Static websites


## How Burstable Instances Work 🔗 
Burstable instances can sustain workloads running at a fraction of CPUs most of the time and can burst up to the full CPUs for a maximum 1 hour continuous burst. Depending on the burst pattern (continuous burst or not) and how long the instance is underutilized, the burst allowance might be more or less than 1 hour.
When you create a burstable instance, you specify the total OCPU count (or CPU cores) and the baseline CPU utilization. The baseline utilization is a fraction of each CPU core, either 12.5% or 50%. The baseline provides the minimum CPUs that can be used constantly.
When needed, the instance can use more than the baseline CPU, all the way up the total OCPUs that you provision. This usage above the baseline is called bursting because it happens automatically and for a maximum 1 hour continuous burst.
For example, for an instance with 1 OCPU, a baseline of 12.5% means that 12.5% of the CPU core is available for baseline usage, with a maximum burst of 100% of 1 CPU core. For an instance with 64 OCPUs, the same 12.5% baseline means that 12.5% of 64 CPU cores are available for baseline usage, with a maximum burst of 100% of all 64 CPU cores.
The ability to burst depends on the instance's CPU usage pattern and the underlying server resource usage. If the instance's CPU utilization is below the baseline for a given period, the system allows the instance to burst above the baseline approximately equivalent to that period. The burst is limited to a maximum 1 hour continuous burst to ensure that resources are managed fairly. Because burstable instances are oversubscribed compute resources, there is no guarantee that an instance will be able to burst exactly when needed.
After the burst is finished by the system, the instance is limited to the baseline CPU.
You can [monitor CPU utilization](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics) using the `CpuUtilization` metric.
### Supported Shapes 🔗 
You can use the following [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) to create burstable instances:
  * VM.Standard3.Flex
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex
  * VM.Standard.E5.Flex


### OCPU, Memory, Network Bandwidth, and VNICs 🔗 
Because burstable instances use [flexible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible), you can customize the number of OCPUs and the amount of memory that are allocated to a burstable instance.
  * **OCPUs:** You can select the same range of OCPUs for a burstable instance as you can select for a regular instance that uses the same shape.
  * **Memory:** The amount of memory is based on the total number of OCPUs. For each OCPU, you can select the same ratio of memory for a burstable instance as you can select for a regular instance that uses the same shape, regardless of which baseline OCPU you configure. For example, if you create a 1-OCPU instance using the VM.Standard.E4.Flex shape, you can allocate up to 64 GB of memory.
The minimum amount of memory for a burstable instance is the same as for a regular instance that uses the same shape. The maximum amount of memory is smaller for a burstable instance than it is for a regular instance.
The default amount of memory assigned depends on the number of OCPUs and the baseline that you select. The default memory assigned to burstable instances is not the same as the default amount of memory assigned to regular instances.
Memory does not burst.
  * **Network bandwidth:** The maximum network bandwidth is defined in relation to the baseline OCPU. Network bandwidth does burst.
  * **VNICs:** The minimum number of VNICs, maximum number of VNICs, and ratio of VNICs to OCPUs for a burstable instance are the same as those for a regular instance that uses the same shape.


Shape | OCPU | Memory (GB) | Max Network Bandwidth | VNICs  
---|---|---|---|---  
VM.Standard3.Flex | 1 minimum, 32 OCPU maximum | 1 GB minimum, 384 GB maximum | 0.5 Gbps for each 12.5% baseline OCPU, overall maximum 32 Gbps |  VM with 1 OCPU: 2 VNICs. VM with 2 or more OCPUs: 1 VNIC per OCPU. Maximum 24 VNICs.  
VM.Standard.E3.Flex | 1 OCPU minimum, 64 OCPU maximum | 1 GB minimum, 768 GB maximum | 0.5 Gbps for each 12.5% baseline OCPU, overall maximum 40 Gbps |  VM with 1 OCPU: 2 VNICs. VM with 2 or more OCPUs: 1 VNIC per OCPU. Maximum 24 VNICs.  
VM.Standard.E4.Flex | 1 OCPU minimum, 64 OCPU maximum | 1 GB minimum, 768 GB maximum | 0.5 Gbps for each 12.5% baseline OCPU, overall maximum 40 Gbps |  VM with 1 OCPU: 2 VNICs. VM with 2 or more OCPUs: 1 VNIC per OCPU. Maximum 24 VNICs.  
VM.Standard.E5.Flex | 1 OCPU minimum, 94 OCPU maximum | 1 GB minimum, 1049 GB maximum | 0.5 Gbps for each 12.5% baseline OCPU, overall maximum 40 Gbps |  VM with 1 OCPU: 2 VNICs. VM with 2 or more OCPUs: 1 VNIC per OCPU. Maximum 24 VNICs.  
The flexibility of burstable instances means that you can create instances that are optimized for small or low-utilization applications. For example, with the VM.Standard.E4.Flex [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#vm-standard), you can create a subcore or burstable instance as small as 12.5% or 50% of an OCPU, with a minimum of 1 GB of memory, and have the ability to burst up to 1 OCPU for a limited amount of time. (One OCPU is equivalent to two hardware execution threads or vCPUs on Intel and AMD processors.) For larger workloads, you can create a burstable instance as large as 64 OCPUs (using the VM.Standard.E4.Flex shape) with 12.5% baseline, with a maximum memory of 768GB, and have the ability to burst up to 64 OCPUs for a limited amount of time.
### Burstable Instances Compared to Regular Instances 🔗 
With both burstable instances and regular flexible instances, you can optimize the instance for your workload. However, burstable instances and regular instances have several differences.
Burstable Instances | Regular Flexible Instances  
---|---  
What they're for | Let you optimize your costs for workloads that require minimal resource utilization most of the time. The physical VM host is oversubscribed, so there is no guarantee that an instance will be able to burst. | Let you customize the number of OCPUs and amount of memory for workloads that require guaranteed access to the total amount of OCPUs. The physical VM host is not oversubscribed.  
How they scale | The instance dynamically scales the available OCPUs between a baseline and a maximum that you define. | You must [resize the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance) when you want to scale the OCPUs and memory.  
How fast they scale | Rapidly scale up and scale down to handle temporary spikes in workload. | Take longer to scale up and scale down, but can handle high resource utilization for a sustained period of time.  
Compare burstable instances with regular instances: If you create a regular instance with 1 OCPU, you are required to provision an entire core. If you create a subcore instance using the [Always Free VM.Standard.E2.1.Micro shape](https://docs.oracle.com/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm), the instance would be allocated less than a full OCPU, but it would not have a flexible amount of memory and would not be able to burst.
**Note** **Cloud Advisor** can recommend converting a regular instance to a burstable instance, as described in [Change Compute Instances to Burstable](https://docs.oracle.com/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#burstable).
### Limitations and Considerations 🔗 
Be aware of the following information:
  * Because the physical VM host is oversubscribed, there is no guarantee that an instance will be able to burst. For critical or production workloads that require full OCPU utilization, you should use a regular instance instead.
  * Network bandwidth is oversubscribed, so there is no guarantee that the instance can use the maximum bandwidth.
  * Memory does not burst.
  * [Custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") are supported if the baseline OCPU meets the minimum requirements for the image.
  * Each burstable instance can have one ephemeral public IP address. If you need additional public IPs, [assign reserved public IPs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm) to the instance.
  * You can attach four [block volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) for each 12.5% baseline OCPU, up to the [maximum limit](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#Capabil).
  * Burstable instances must use [paravirtualized networking](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm#top "When you create a VM instance, by default, Oracle Cloud Infrastructure chooses a recommended networking type for the VNIC based on the instance shape and OS image. The networking interface handles functions such as disk input/output and network communication."). If you create a regular instance using SR-IOV networking (the default for some regular instances), and want to change the instance to a burstable instance, you must also [change the networking type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#edit-launch-options) to paravirtualized.
  * Burstable instances are not supported on dedicated virtual machine hosts, capacity reservations, or preemptible capacity.
  * [Service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) and [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm) for a burstable instance count the baseline OCPUs that are configured for the instance, regardless of actual usage. Burstable instances and regular instances share the same service limits and compartment quotas based on the instance's shape.
  * [Extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-vm-instances "Extended memory virtual machine \(VM\) instances are VM instances that provide more memory and cores than available with standard shapes.") do not burst.


### Billing 🔗 
Burstable instances cost less than regular instances with the same total OCPU count. Burstable instances are charged according to the baseline OCPU. The charge for a burstable instance is the same regardless of whether the actual CPU utilization is at the baseline, below the baseline, or bursts above the baseline. Contrast this with regular instances, which are charged for the total OCPU count, even if your usage is lower.
For example, if you create a VM.Standard.E4.Flex instance with 1 OCPU and a 12.5% baseline, you are charged for 12.5% of a [Standard E4 OCPU](https://www.oracle.com/cloud/compute/pricing.html) each hour, regardless of whether your actual CPU utilization is below 12.5% of 1 OCPU or bursts to the full 1 OCPU.
Windows Server license costs are also charged according to the baseline OCPU.
Memory is charged based on the amount of memory configured for the instance, the same as regular instances.
For more information about billing, see the Oracle Compute Cloud Services section of [Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).
## Creating a Burstable Instance 🔗 
When you [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), you specify whether the instance is a burstable instance. You can also [edit an existing, regular instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance) to make it a burstable instance.
**Using the Console:**
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the **Shape** section.
  2. Click **Change shape**.
  3. Select a [shape that supports bursting](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#supported-shapes).
  4. For **Number of OCPUs** , choose the maximum number of OCPUs for the instance to burst to.
  5. Select the **Burstable** option.
  6. In the **Baseline utilization per OCPU** list, select the baseline OCPU utilization for the instance. This value is the percentage of OCPUs that you want to use most of the time.
For example, a 12.5% baseline means that the instance has up to 12.5% of the total OCPU count available for baseline usage (that is, normal usage when the instance isn't bursting). For an instance with 1 OCPU, a 12.5% baseline means that up to 1/8 of an OCPU is available for baseline usage.
  7. For **Amount of memory** , choose the amount of memory that you want to allocate to this instance by dragging the slider. The maximum memory you can choose depends on the number of OCPUs and the baseline that you select. The default amount of memory assigned depends on the number of OCPUs and the baseline that you select. The default memory assigned to burstable instances is not the same as the default amount of memory assigned to regular instances. Memory does _not_ burst.
  8. Click **Select shape**.
  9. Finish creating the instance, and then click **Create**.


**Using the API:** Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation, specifying the baseline OCPU in the `baselineOcpuUtilization` attribute.
Was this article helpful?
YesNo

