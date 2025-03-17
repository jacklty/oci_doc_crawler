Updated 2025-01-13
# Editing the Launch Options for an Instance
You can tune the compatibility and performance of virtual machine (VM) instances by changing the networking type or the boot volume attachment type.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Networking Launch Types 🔗 
The networking interface handles functions such as disk input/output and network communication.
The following networking types are available:
  * **Paravirtualized networking** : For general purpose workloads such as enterprise applications, microservices, and small databases. Paravirtualized networking also provides increased flexibility to use the same image across different hardware platforms. Linux images with paravirtualized networking support live migration during infrastructure maintenance.
  * **Hardware-assisted (SR-IOV) networking** : Single root input/output virtualization. For low-latency workloads such as video streaming, real-time applications, and large or clustered databases. Hardware-assisted (SR-IOV) networking uses the VFIO driver framework.


**Important** To use a particular networking type, both the shape and the image must support that networking type.
**Shapes:** The following table lists the default and supported networking types for [VM shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#vmshapes).
Shape | Default Networking Type | Supported Networking Types  
---|---|---  
VM.Standard1 series | SR-IOV | Paravirtualized, SR-IOV  
VM.Standard2 series | Paravirtualized | Paravirtualized, SR-IOV  
VM.Standard3.Flex | Paravirtualized | Paravirtualized, SR-IOV  
VM.Standard.E2 series | Paravirtualized | Paravirtualized only  
VM.Standard.E3.Flex |  Paravirtualized | Paravirtualized, SR-IOV  
VM.Standard.E4.Flex |  Paravirtualized | Paravirtualized, SR-IOV  
VM.Standard.E5.Flex |  Paravirtualized | Paravirtualized, SR-IOV  
VM.Standard.A1.Flex[1](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#fntarg_1) | Paravirtualized | Paravirtualized, SR-IOV  
VM.DenseIO1 series | SR-IOV | Paravirtualized, SR-IOV  
VM.DenseIO2 series | Paravirtualized | Paravirtualized, SR-IOV  
VM.DenseIO.E4.Flex | Paravirtualized | Paravirtualized, SR-IOV  
VM.GPU2 series | SR-IOV | Paravirtualized, SR-IOV  
VM.GPU3 series | SR-IOV | Paravirtualized, SR-IOV  
VM.GPU.A10 series | SR-IOV | Paravirtualized, SR-IOV  
VM.Optimized3.Flex |  Paravirtualized | Paravirtualized, SR-IOV  
**Images:** Paravirtualized networking is supported on these [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images):
  * **Oracle Linux 9, Oracle Linux 8, Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7.x, Oracle Linux Cloud Developer 8:** All images.
  * **Oracle Linux 7:** Images published in March 2019 or later.
  * **CentOS Stream 8, CentOS 7:** Images published in July 2019 or later.
  * **Ubuntu 22.04, Ubuntu 20.04:** All images.
  * **Ubuntu 18.04:** Images published in March 2019 or later.
  * **Windows Server 2022, Windows Server 2019:** All images.
  * **Windows Server 2016, Windows Server 2012 R2:** Images published in August 2019 or later.


SR-IOV networking is supported on all platform images, with the following exceptions:
  * Images for Arm-based shapes do not support SR-IOV networking.
  * On Windows Server 2019 and Windows Server 2022, when launched using a shape in the VM.Standard2 series, SR-IOV networking is not supported.
  * On Windows Server 2012 R2, SR-IOV networking is supported on platform images released in April 2021 or later.
  * The Server Core installation option for Windows Server does not support SR-IOV networking.


## Boot Volume Attachment Types 🔗 
The following boot volume attachment types are available:
  * **iSCSI:** A TCP/IP-based standard used for communication between a volume and attached instance.
  * **Paravirtualized:** A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images.


## Supported Shapes 🔗 
You can edit the launch options for instances that use these shapes:
  * VM.Standard1 series
  * VM.Standard.B1 series
  * VM.Standard2 series
  * VM.Standard3.Flex
  * VM.Standard.E2 series
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex
  * VM.Standard.E5.Flex
  * VM.Standard.A1.Flex
  * VM.DenseIO1 series
  * VM.DenseIO2 series
  * VM.GPU3 series
  * VM.GPU.A10 series
  * VM.Optimized3.Flex


These shapes cannot be edited:
  * VM.Standard.E2.1.Micro
  * VM.DenseIO.E4.Flex
  * VM.GPU2 series
  * VM instances that run on dedicated virtual machine hosts


## Limitations and Considerations 🔗 
**Caution** Some instances might not function properly if you change the networking type or the boot volume attachment type. This happens due to shape and image compatibility and driver support. After the instance reboots and is running, [connect to it](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection."). If the connection fails or the OS doesn't behave as expected, the changes are not supported. Revert the instance to the original settings.
Before you change the networking type or the boot volume attachment type, you must ensure that paravirtualized drivers are installed on the image. The steps depend on the image:
[Oracle Linux 7.x, CentOS 7.x, CentOS Stream 8, Ubuntu 20.04, Ubuntu 18.04](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm)
Paravirtualized drivers are installed on platform images.
[Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm)
The Oracle VirtIO Drivers for Microsoft Windows must be installed on platform images.
  1. To determine whether the drivers are installed, [connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") using a Remote Desktop connection. Then, do either of the following things:
     * Open **Control Panel** , and then open **Program and Features**. If **Oracle Windows VirtIO Drivers** is installed, note the version number.
     * In Registry Editor, go to**HKEY_LOCAL_MACHINE\\\Software\\\Wow6432Node\\\Oracle Corporation\\\Oracle Windows VirtIO Drivers**. If the drivers are installed, note the version number.
  2. If the drivers are not installed, do the following:
    1. [Download the Oracle VirtIO Drivers for Microsoft Windows](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html).
    2. [Install the drivers](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindows.html) and then restart the instance.


[Images that are not platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm)
To verify that your system has paravirtualized drivers installed, run the following command:
Copy
```
lsinitrd | grep virtio
```

  * If paravirtualized drivers are installed, you will see multiple files listed with paths similar to `lib/modules/4.4.21-69-default/kernel/drivers/block/virtio_blk.ko`.
  * If no files are listed, your system either does not support paravirtualized drivers, or does not have paravirtualized drivers installed. Refer to the documentation for your operating system for more information.


## Before You Begin 🔗 
  * [Detach (delete) all secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#To3) and [detach all block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/detachingavolume.htm). The primary VNIC and boot volume should remain attached.


## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options**. The **Launch options** tab displays.
  5. To change the networking type, in the **Networking type** section, select from the following options:
     * **Hardware-assisted (SR-IOV) networking:** Single root input/output virtualization. For low-latency workloads such as video streaming, real-time applications, and large or clustered databases.
     * **Paravirtualized networking:** For general purpose workloads such as enterprise applications, microservices, and small databases. The image must have paravirtualized drivers, as described in [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#limitations-and-considerations).
  6. To change the boot volume attachment type, in the **Boot volume attachment type** section, select from the following options:
     * **iSCSI:** A TCP/IP-based standard used for communication between a volume and attached instance.
     * **Paravirtualized:** A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images.
  7. Click **Save changes**.
If the instance is running, it is rebooted. Confirm when prompted.
  8. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") after it reboots and is running. If the connection fails or the OS doesn't behave as expected, the changes are not supported. Revert the instance to the original settings.
  9. If necessary, reattach any [secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#create_sec_vnic) and [block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to edit the launch options for an instance:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


[1](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm#fnsrc_1) See [Limit on size of VM.Standard.A1.Flex shape using the SR-IOV network type](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#a1-VFIO-networking)
Was this article helpful?
YesNo

