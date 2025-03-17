Updated 2024-12-11
# Bring Your Own Image (BYOI)
The Bring Your Own Image (BYOI) feature enables you to bring your own versions of operating systems to the cloud as long as the underlying hardware supports it. The services do not depend on the OS you run.
The BYOI feature does the following things:
  * Enables virtual machine cloud migration projects.
  * Supports both old and new operating systems.
  * Encourages experimentation.
  * Increases infrastructure flexibility.


**Note**
Licensing Requirements
You must comply with all licensing requirements when you upload and start instances based on OS images that you supply.
## Bringing Your Own Image 🔗 
A critical part of any lift-and-shift cloud migration project is the migration of on-premises virtual machines (VMs) to the cloud. You can import your on-premises virtualized root volumes to Oracle Cloud Infrastructure (OCI) using the custom image import feature, and then create compute instances using those images.
You can import Windows and Linux-based custom images and use them to create VMs on Oracle Cloud Infrastructure. Bringing your own image to a bare metal instance is not supported.
For instructions describing how to import your own image:
  * [Importing Custom Windows Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagewindows.htm#Importing_Custom_Windows_Images)
  * [Importing Custom Linux Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#Importing_Custom_Linux_Images)


### Limitations and Considerations 🔗 
Be aware of the following information:
  * **Licensing requirements** : You must comply with all licensing requirements when you upload and start instances based on OS images that you supply.
  * The maximum image size is 400 GB.
  * Service limits and compartment quotas apply to custom images. For more information, see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Other_Compute_Resources). You can [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).


### Launch Modes 🔗 
You can launch imported Linux VMs in either paravirtualized mode or emulated mode. On AMD and Arm-based shapes, Oracle Linux Cloud Developer images, and Red Hat Enterprise Linux images, imported images are supported in paravirtualized mode only.
Windows imported images are supported in paravirtualized mode only.
Paravirtualized mode offers better performance than emulated mode. We recommend that you use paravirtualized mode if your OS supports it. Linux-based operating systems running the kernel version 3.4 or later support paravirtualized drivers. You can verify your system's kernel version using the [uname](http://www.linfo.org/uname.html) command.
[To verify the kernel version using the uname command](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm)
Run the following command:
Copy
```
uname -a
```

The output should look similar to this sample:
```
Linux ip_bash 4.14.35-1818.2.1.el7uek.x86_64 #2 SMP Mon Aug 27 21:16:31 PDT 2018 x86_64 x86_64 x86_64 GNU/Linux
```

The kernel version is the number at the first part of output string. In the sample output shown previously, the version is 4.14.35.
If your image supports paravirtualized drivers, you can convert your existing emulated mode instances into paravirtualized instances. After you complete the conversion, instances created from the image are launched in paravirtualized mode.
[To convert emulated mode instances into paravirtualized instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm)
  1. [Create a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.") of your instance.
  2. [Edit the image capabilities for the custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities) to use the following settings:
     * For **Firmware** and **Preferred firmware** , select **BIOS**.
     * For the following fields, select **Paravirtualized**.
       * **Launch mode**
       * **Preferred launch mode**
       * **NIC attachment type**
       * **Preferred network attachment type**
       * **Boot volume type**
       * **Preferred boot volume type**
       * **Local data volume**
       * **Preferred local data volume type**
       * **Remote data volume**
       * **Preferred remote data volume type**


### Windows Images 🔗 
These Windows versions support custom image import:
  * Windows Server 2016: Datacenter, Standard, Standard Core
  * Windows Server 2019: Datacenter, Standard, Standard Core
  * Windows Server 2022: Datacenter, Standard, Standard Core


For steps to import a Windows image, see [Importing Custom Windows Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagewindows.htm#Importing_Custom_Windows_Images).
Bring your own license (BYOL) for Windows Server is not permitted when launching a VM instance on a shared host. For more information about BYOL and the licensing requirements for Windows images, [Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#Microsoft_Licensing_on_Oracle_Cloud_Infrastructure).
### Linux Images 🔗 
The Linux and UNIX-like operating systems in the following table support custom image import.
**Support details:**
  * Oracle Cloud Infrastructure has tested the operating systems listed in the following table and supports customers in ensuring that instances launched from these images and built according to the guidelines in this topic are accessible using SSH.
  * For any OS version other than those covered by an official support service from Oracle (for example, Oracle Linux with Premier Support), Oracle Cloud Infrastructure provides commercially reasonable support limited to getting an instance launched and accessible through SSH. 
  * Support from Oracle Cloud Infrastructure in creating an instance from a custom OS does not ensure that the operating system vendor also supports the instance. Customers running [Oracle Linux](https://www.oracle.com/linux/index.html) on Oracle Cloud Infrastructure automatically have access to [Oracle Linux Premier Support](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf).


Linux or UNIX-like Operating System | Supported Versions  
---|---  
CentOS | 6.9, 7, Stream 8 or later  
Debian | 5.0.10, 6.0, 7, 8 or later  
Flatcar Container Linux | 2345.3.0 or later  
FreeBSD | 8, 9, 10, 11, 12 or later  
openSUSE Leap  | 15.1  
Oracle Linux | 5.11, 6.x, 7.x, 8.x, 9.x  
RHEL |  Support from Red Hat and OCI through the Red Hat Certified Cloud and Service Provider (CCSP) program: for versions and shapes, see [Red Hat Ecosystem Catalog - Oracle Cloud Infrastructure](https://catalog.redhat.com/cloud/detail/216977) Limited support from OCI: 4.5, 5.5, 5.6, 5.9, 5.11, 6.5, 6.9, 7 or later  
SUSE | 11, 12.1, 12.2 or later  
Ubuntu | 12.04, 13.04 or later  
Certain versions of Red Hat Enterprise Linux (RHEL) images are supported through the Red Hat Certified Cloud and Service Provider (CCSP) program. For requirements and steps to create an instance using a supported RHEL image, see [Red Hat Enterprise Linux (RHEL) Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#ossupport__rhel).
You might also have success importing other distributions of Linux.
For steps to import a Linux-based image, see [Importing Custom Linux Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#Importing_Custom_Linux_Images).
## Bringing Your Own Hypervisor Guest OS 🔗 
You can bring your own hypervisor guest OS using Kernel-based Virtual Machine (KVM) or Hyper-V.
**Note** Bring your own hypervisor deployment of ESXi on bare metal compute instances is not supported. ESXi is supported only by provisioning an Oracle Cloud VMware Solution software-defined data center (SDDC). See [VMware Solution](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm) for more information.
### Bringing Your Own KVM 🔗 
You can bring your own operating system images or older operating systems, such as Ubuntu 6.x, RHEL 3.x, and CentOS 5.4, using KVM on bare metal instances.
To bring your own KVM, first [create a bare metal instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") using the KVM image from Marketplace. Then, copy your on-premises guest OS to KVM on the bare metal instance. For more information, see [Oracle Linux KVM](https://docs.oracle.com/iaas/oracle-linux/kvm/index.htm).
### Bringing Your Own Hyper-V 🔗 
You can bring your own operating system images or older operating system, such as Windows Server 2016 using Hyper-V on bare metal instances.
To bring your own Hyper-V, first [create a bare metal instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") using the [Windows Server Datacenter platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images). Oracle Cloud Infrastructure will issue a license for Windows Server when the instance is launched. Then, copy your on-premises guest OS to Hyper-V on the bare metal instance. No additional license is required because Windows Server Datacenter includes unlimited virtual machines.
Be aware of the following considerations:
  * Oracle Cloud Infrastructure will issue a license when you launch an instance using a custom image. If you want to bring your own license (BYOL) for Windows Server, you must activate Windows Server with your own license. For steps, see [Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#Microsoft_Licensing_on_Oracle_Cloud_Infrastructure).
  * Importing your own ISO image is not supported.


For a list of supported Hyper-V guests, see the following resources:
  * [Supported Windows guest operating systems for Hyper-V on Windows Server](https://docs.microsoft.com/windows-server/virtualization/hyper-v/supported-windows-guest-operating-systems-for-hyper-v-on-windows)
  * [Supported Linux and FreeBSD virtual machines for Hyper-V on Windows](https://docs.microsoft.com/windows-server/virtualization/hyper-v/supported-linux-and-freebsd-virtual-machines-for-hyper-v-on-windows)


## NTP Service 🔗 
Oracle Cloud Infrastructure offers a fully managed, secure, and highly available NTP service that you can use to set the date and time of your compute and Database instances from within your virtual cloud network (VCN). We recommend that you configure your instances to use the Oracle Cloud Infrastructure NTP service. For information about how to configure instances to use this service, see [Configuring the Oracle Cloud Infrastructure NTP Service for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm#Configuring_the_Oracle_Cloud_Infrastructure_NTP_Service_for_an_Instance).
Was this article helpful?
YesNo

