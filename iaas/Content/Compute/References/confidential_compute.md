Updated 2025-01-10
# Confidential Computing
Confidential computing encrypts and isolates in-use data and the applications processing that data.
Confidential instances are Compute virtual machines (VMs) or bare metal instances where both the data and the application processing the data are encrypted and isolated while the application processes the data, preventing unauthorized access or modification of either the data or the application.
The confidential Compute solution is available on Oracle's AMD instances, which have the second and third generation AMD EPYC™ processors. Confidential VMs use AMD Secure Encrypted Virtualization (SEV) technology, while confidential bare metal instances use AMD Transparent Secure Memory Encryption (TSME) technology.
Confidential computing:
  * Improves isolation using real-time encryption. Data and applications are encrypted using a per-VM encryption key generated during the VM creation and resides solely in the AMD Secure Processor, which is part of the CPU. This key is not accessible from any applications, the VM or instance, the hypervisor, or Oracle Cloud Infrastructure.
  * Requires no change to the application to enable Confidential VMs.
  * Provides high performance while protecting data in-use with minimal performance impact. Many applications experience little to no performance impact with confidential computing enabled.


## Support and Limitations 🔗 
  * After you enable confidential computing on an instance, you can only edit the name of the instance. You cannot change the shape of the instance. Refer to [Changing the Shape of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance) for more information.
  * Confidential computing is available only in the following regions:
    * Germany Central (Frankfurt)
    * India South (Hyderabad)
    * India West (Mumbai)
    * Switzerland North (Zurich)
    * UK Gov West (Newport)
    * UK South (London)
    * US East (Ashburn)
    * US West (Phoenix)
  * The following features are not available with confidential computing:
    * Preemptible capacity
    * Capacity reservation
    * Dedicated virtual machine hosts
    * Shielded instances


## Compute Shapes that Support Confidential Computing 🔗 
The following Compute shapes support confidential computing: 

Virtual Machine Compute Shapes (on Oracle Linux 7.x or 8.x platform images)
    
  * VM.Standard.E4.Flex
  * VM.Standard.E3.Flex



Bare Metal Instance Compute Shapes (on any platform image)
    
  * BM.DenseIO.E5.128
  * BM.Standard.E5.192
  * BM.DenseIO.E4.128
  * BM.Standard.E4.128
  * BM.Standard.E3.128


To enable confidential computing, refer to [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
Was this article helpful?
YesNo

