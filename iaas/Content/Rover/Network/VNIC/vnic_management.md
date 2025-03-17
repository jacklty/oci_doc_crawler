Updated 2024-11-26
# Virtual Network Interface Cards (VNICs) for Roving Edge Infrastructure
Learn how to manage virtual network interface cards (VNICs) in a virtual cloud network (VCN) on Roving Edge Infrastructure devices.
A VNIC enables an instance to connect to a VCN and determines how the instance connects with endpoints inside and outside the VCN.
Each instance has a _primary VNIC_ that's automatically created and attached during instance creation. That VNIC resides in the subnet you specify when you create the instance. The primary VNIC can't be removed from the instance. 
You can add secondary VNICs to an instance. The number of secondary VNICs you can add depends on the number of OCPUs in the instance shape as shown in the following table. To identify an instance shape, view the Instances page. See [Listing Instances for a Roving Edge Infrastructure Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list_instance.htm#ListInstance "Describes how to list the compute instances on your Roving Edge Infrastructure device.").
Shape Name | Number of OCPUs | Maximum Total VNICs  | Number of Primary VNICs | Maximum Number of Secondary VNICs  
---|---|---|---|---  
**RED1:** VM.Standard.RED1.1 VM.GPU.1.RED1.1 **RED2:** VM.Standard.EDGE.1 VM.GPU.EDGE.1 **Ultra:** VM.Standard.RX2.1 VM.USB.1.RX2.1 | 1 | 2 | 1 | 1  
**RED1:** VM.Standard.RED1.2 VM.GPU.1.RED1.2 **RED2:** VM.Standard.EDGE.2 VM.GPU.EDGE.2 **Ultra:** VM.Standard.RX2.2 VM.USB.1.RX2.2 | 2 | 2 | 1 | 1  
**RED1:** VM.Standard.RED1.4 VM.GPU.1.RED1.4 **RED2:** VM.Standard.EDGE.4 VM.GPU.EDGE.4 **Ultra:** VM.Standard.RX2.4 VM.USB.1.RX2.4 | 4 | 4 | 1 | 3  
**RED1:** VM.Standard.RED1.8 VM.GPU.1.RED1.8 **RED2:** VM.Standard.EDGE.8 VM.GPU.EDGE.8 **Ultra:** VM.Standard.RX2.8 VM.USB.1.RX2.8 | 8 | 8 | 1 | 7  
**RED1:** VM.Standard.RED1.16 VM.GPU.1.RED1.16 **RED2:** VM.Standard.EDGE.16 VM.GPU.EDGE.16 | 16 | 16 | 1 | 15  
After a secondary VNIC is attached to an instance, you need to configure the instance OS to recognize the secondary VNIC.
See [Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) in the Oracle Cloud Infrastructure documentation for more information about VNICs.
You can perform the following VNIC tasks:
  * [Creating and attaching a VNIC](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm#top "Describes how to create and attach a secondary VNIC to your Roving Edge Infrastructure devices.")
  * [Getting a VNIC's details](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic.htm#top "Describes how to get the details of a VNIC on your Roving Edge Infrastructure devices.")
  * [Editing a VNIC](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm#top "Describes how to edit a VNIC on your Roving Edge Infrastructure devices.")
  * [Getting a VNIC attachement's details](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic-attachment.htm#top "Describes how to get the details of a VNIC attachment on your Roving Edge Infrastructure devices.")
  * [Detaching and Deleting a VNIC](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm#top "Describes how to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices.")


Was this article helpful?
YesNo

