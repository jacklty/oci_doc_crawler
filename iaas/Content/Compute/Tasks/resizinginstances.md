Updated 2025-01-13
# Changing the Shape of an Instance
You can change the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) of a virtual machine (VM) instance without having to rebuild the instance or redeploy your applications. Changing shapes lets you scale up your Compute resources for increased performance or scale down to reduce costs.
Changing the shape of an instance affects the number of **OCPUs** , amount of memory, network bandwidth, and maximum number of VNICs for the instance. In addition, you can select a shape that uses a different processor. The instance's public and private IP addresses, volume attachments, and VNIC attachments remain the same.
Optionally, you can change a regular instance to a burstable instance, or change a burstable instance to a regular instance. Similarly, you can change a regular instance to an extended memory VM instance, or change an extended memory VM instance to a regular instance.
To determine whether capacity is available for a specific shape before you change the shape of an instance, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
## Supported Shapes 🔗 
The instance's current shape and image determine available new shape targets. You can resize instances that use these shapes:
  * **VM Standard and Optimized shapes:** Includes the following shapes:
    * VM.Standard1 series
    * VM.Standard.B1 series
    * VM.Standard2 series
    * VM.Standard3.Flex
    * VM.Standard.E2 series
    * VM.Standard.E3.Flex
    * VM.Standard.E4.Flex
    * VM.Standard.E5.Flex
    * VM.Optimized3.Flex
    * VM.Standard.A1.Flex
    * VM.Standard.A2.Flex
For both Linux and Windows images, you can change the number of OCPUs and the amount of memory allocated to a [flexible shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible). You can also change a standard shape in one series to a standard shape in another series. For example, you can change a fixed shape to a flexible shape.
**Important** For Windows Server 2019 instances running on shapes in the VM.Standard2 series, you can change the shape to a new shape only within the same series.
  * **VM.GPU3 series:** You can change to any shape in the VM.GPU3 or VM.GPU.A10 series.
  * **VM.GPU.A10 series:** You can change to any shape in the VM.GPU.A10 or VM.GPU3 series.


These shapes cannot be edited:
  * VM.Standard.E2.1.Micro
  * VM.DenseIO.E4.Flex
  * VM.DenseIO.E5.Flex
  * VM.GPU2 series


## Limitations and Considerations 🔗 
Be aware of the following information:
  * The image that was used to create the instance must be compatible with the new shape. To see which shapes are compatible, do either of the following things:
    * In the Console, on the Instance Details page, click the name of the image. Then, refer to the list of compatible shapes.
    * Using the API, call the [ListShapes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Shape/ListShapes) operation and pass the image OCID as a parameter.
  * Some Marketplace images cannot be resized because of licensing constraints. If you want to resize a Microsoft SQL Server image, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  * You must have sufficient [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for the new shape. If you don't have service limits, the instance retains the original shape.
  * Different shapes are billed at different rates. When you change the shape of an instance, you are billed to the nearest second of usage for each shape that you use. For more information, see [Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html) and [Resource Billing for Stopped Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm#top "When you stop an Oracle Cloud Infrastructure Compute instance, billing for the stopped instance depends on the shape that you used to create the instance.").
  * If the instance has secondary VNICs configured, you might need to reconfigure them after the instance is rebooted. For more information, see [VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
  * If the instance is running when you change the shape, it is rebooted as part of the change shape operation. If the applications that run on the instance take a long time to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, [shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#operatingsystem) before you change the shape.
  * When you change the shape from one hardware series to a different series, some hardware details such as the network interface name might change. This might cause problems for some guest OSs, particularly if the OS has been customized. If the OS fails to boot after you change the shape, then you should change the instance back to the original shape.
  * If you created a regular instance using SR-IOV networking (the default for some regular instances), and want to change the instance to a [burstable instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances), you must also [change the networking type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#edit-launch-options) to paravirtualized.


## Before You Begin 🔗 
  * If you want to change the instance to a smaller shape that supports fewer VNICs, [detach the extra VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).


## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click **More Actions** , and then click **Edit**.
  4. Click **Edit shape**.
  5. In the **Shape series** section, select a processor group. The following options are available: 
     * **AMD:** (Flexible) Standard shapes that use current-generation AMD processors. AMD shapes are flexible shapes.
     * **Intel:** (Flexible) Standard and optimized shapes that use current-generation Intel processors. Intel shapes are flexible shapes.
     * **Ampere:** (Flexible) The OCI Ampere A1 Compute and OCI Ampere A2 Compute shapes use Arm-based processors. The Arm-based shapes are flexible shapes. These shapes are not supported for Windows.
     * **Specialty and previous generation:** Standard shapes with previous generation Intel and AMD processors, the [Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm) VM.Standard.E2.1.Micro shape, Dense I/O shapes, GPU shapes, and HPC shapes.
  6. Select the shape that you want to scale to.
The instance's current shape and image determine which shapes you can select as a target for the new shape.
  7. If you selected a flexible shape, provide the following information:
     * For **Number of OCPUs** , choose the number of OCPUs that you want to allocate to this instance by dragging the slider. The other resources scale proportionately.
     * If you want this to be a [burstable instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances) and the shape supports bursting, select the **Burstable** option. Then, in the **Baseline utilization per OCPU** list, select the baseline OCPU utilization for the instance. This value is the percentage of OCPUs that you want to use most of the time.
     * For **Amount of memory (GB)** , choose the amount of memory that you want to allocate to this instance. The amount of memory allowed is based on the number of OCPUs selected.
     * If you want to allocate an [extended amount of memory](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-create-instance) or OCPUs to the instance, you can make this instance an extended memory VM by dragging the slider to **Extended OCPU** or **Extended memory**.
For more information about the minimum memory, maximum memory, and ratio of memory to OCPUs for each shape, see [Flexible Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#flexible).
  8. Click **Save changes**.
If the instance is running, it is rebooted. Confirm when prompted.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to change the shape of an instance:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo

