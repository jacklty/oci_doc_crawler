Updated 2025-01-08
# Recommended Networking Launch Types for Compute Instances
When you create a VM instance, by default, Oracle Cloud Infrastructure chooses a recommended networking type for the VNIC based on the instance shape and OS image. The networking interface handles functions such as disk input/output and network communication.
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
VM.Standard.A1.Flex[1](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm#fntarg_1) | Paravirtualized | Paravirtualized, SR-IOV  
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


[1](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm#fnsrc_1) See [Limit on size of VM.Standard.A1.Flex shape using the SR-IOV network type](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#a1-VFIO-networking)
Was this article helpful?
YesNo

