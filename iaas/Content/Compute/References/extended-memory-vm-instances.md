Updated 2023-05-12
# Extended Memory VM Instances
Extended memory virtual machine (VM) instances are VM instances that provide more memory and cores than available with standard shapes.
## How Extended Memory VM Instances Work 🔗 
Extended Memory VM is designed for demanding workloads that need more memory and cores than available with standard shapes. Extended memory VM instances let you to create virtual machines with cores and memory that exceed the amount that a single physical socket carries. Extended Memory VM is available for certain standard shapes.
You can select shapes for extended memory VM in the same way that you select standard shapes. When you create an instance, you can allocate an extended amount of memory and the required number of cores to the instance, similar to how you allocate the number of OCPUs and memory for a regular flexible shape.
## Supported Shapes and Images 🔗 
[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm)
You can allocate additional cores and memory on the following [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes):
  * VM.Standard3.Flex
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex


### OCPU, Memory, and Network Bandwidth 🔗 
You can allocate an extended number of OCPUs and amount of memory to an extended memory VM instance.
Standard Shapes | Extended Memory VM | Network  
---|---|---  
Shape | OCPU | Memory (GB) | OCPU | Max Memory (GB) | Max Network Bandwidth  
VM.Standard3.Flex | 1 OCPU, 32 OCPU maximum | 1 GB minimum, 512 GB maximum | 14 OCPU minimum, 56 OCPU maximum | 896 GB | 32 Gbps  
VM.Standard.E3.Flex | 1 OCPU, 64 OCPU maximum | 1 GB minimum, 1024 GB maximum | 28 OCPU minimum, 114 OCPU maximum | 1760 GB | 40 Gbps  
VM.Standard.E4.Flex | 1 OCPU, 64 OCPU maximum | 1 GB minimum, 1024 GB maximum | 28 OCPU minimum, 114 OCPU maximum | 1760 GB | 40 Gbps  
To change an existing instance to an extended memory configuration, you can [change the shape of an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance). You can change the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) of a virtual machine (VM) instance without having to rebuild your instances or redeploy your applications.
### Non-Uniform Memory Access (NUMA) Awareness at Application Layer 🔗 
Because extended memory VM instances use resources from across the physical sockets of the underlying host, the application layer must be made aware of the underlying virtual machine topology. After you change the shape of an instance to use extended memory VM, you should optimize the application stack make the instance NUMA aware.
How you make the instance NUMA aware varies based on which software the application uses. For example, applications running in a Java Virtual Machine (JVM) can use command line options.
## Limitations and Considerations 🔗 
Be aware of the following information:
  * [Capacity reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity) are not available with extended memory VM instances.
  * [Preemptible instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#preemptible) do not support extended memory VM instances.
  * [Burstable instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances) are not available with extended memory VM instances.


## Creating an Extended Memory VM Instance 🔗 
When you [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), you specify whether the instance is an extended memory VM instance. You can also [edit an existing, regular instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance) to make it an extended memory VM instance.
**Using the Console:**
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the **Shape** section.
  2. Click **Change shape**.
  3. Select a shape that supports extended memory VM.
  4. For **Number of OCPUs** , choose the number of OCPUs that you want to allocate to this instance by dragging the slider. The other resources scale proportionately.
**Note** The **Burstable** option is not supported when you select an extended amount of memory or OCPUs.
  5. For **Amount of memory (GB)** , choose the amount of memory that you want to allocate to this instance by dragging the slider. The amount of memory allowed is based on the number of OCPUs selected.
  6. To allocate an extended amount of memory or OCPUs to the instance, drag the slider to **Extended OCPU** or **Extended memory**.
  7. Click **Select shape**.
  8. Finish creating the instance, and then click **Create**.


**Using the API:** To create an instances, use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation. You can specify the number of cores and amount of memory with the `LaunchInstanceShapeConfigDetails` parameter.
Was this article helpful?
YesNo

