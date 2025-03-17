Updated 2025-02-28
# Platform Images
An image is a template of a virtual hard drive. The image determines the operating system and other software for an instance. The following table lists the platform images that are available in Oracle Cloud Infrastructure. For specific image and kernel version details, along with changes between versions, see the [Image Release Notes](https://docs.oracle.com/iaas/images/).
Image | Name[1](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images__footnote-image-names) | Description  
---|---|---  
Oracle Autonomous Linux 9 Unbreakable Enterprise Kernel Release 7 | Oracle-Autonomous-Linux-9.x-date-number |  [Oracle Autonomous Linux](https://www.oracle.com/cloud/compute/autonomous-linux.html) provides autonomous capabilities such as automated patching with zero downtime, and known exploit detection, to help keep the operating system highly secure and reliable. Oracle Autonomous Linux is based on Oracle Linux. x86 shapes and GPU shapes are supported with this image.  
Oracle Autonomous Linux 8 Unbreakable Enterprise Kernel Release 7 | Oracle-Autonomous-Linux-8.x-date-number |  [Oracle Autonomous Linux](https://www.oracle.com/cloud/compute/autonomous-linux.html) provides autonomous capabilities such as automated patching with zero downtime, and known exploit detection, to help keep the operating system highly secure and reliable. Oracle Autonomous Linux is based on Oracle Linux. x86 shapes and GPU shapes are supported with this image.  
Oracle Autonomous Linux 7 Unbreakable Enterprise Kernel Release 6 | Oracle-Autonomous-Linux-7.x-date-number |  [Oracle Autonomous Linux](https://www.oracle.com/cloud/compute/autonomous-linux.html) provides autonomous capabilities such as automated patching with zero downtime, and known exploit detection, to help keep the operating system highly secure and reliable. Oracle Autonomous Linux is based on Oracle Linux. x86 shapes and GPU shapes are supported with this image.  
Oracle Linux 9 Unbreakable Enterprise Kernel Release 7 | Oracle-Linux-9.x-date-number |  The Unbreakable Enterprise Kernel (UEK) is Oracle's optimized operating system kernel for demanding Oracle workloads. x86 shapes, Arm-based shapes, and GPU shapes are supported with this image.  
Oracle Linux 8 Unbreakable Enterprise Kernel Release 7 | Oracle-Linux-8.x-date-number |  The Unbreakable Enterprise Kernel (UEK) is Oracle's optimized operating system kernel for demanding Oracle workloads. x86 shapes, Arm-based shapes, and GPU shapes are supported with this image.  
Oracle Linux 7 Unbreakable Enterprise Kernel Release 6 | Oracle-Linux-7.x-date-number |  The Unbreakable Enterprise Kernel (UEK) is Oracle's optimized operating system kernel for demanding Oracle workloads. x86 shapes, Arm-based shapes, and GPU shapes are supported with this image.  
Oracle Linux Cloud Developer 8 Unbreakable Enterprise Kernel Release 6 | Oracle-Linux-Cloud-Developer-8.x-date-number |  [Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/developer/index.htm) provides the latest development tools, languages and Oracle Cloud Infrastructure software development kits (SDKs) to rapidly launch a comprehensive development environment. x86 shapes and Arm-based shapes are supported with this image.  
Ubuntu 24.04 LTS | Canonical-Ubuntu-24.04-date-number |  [Ubuntu](https://www.ubuntu.com/) is a free, open-source Linux distribution that is suitable for use in the cloud. [Minimal Ubuntu](https://wiki.ubuntu.com/Minimal) is designed for automated use at scale. It uses a smaller boot volume, boots faster, and has a smaller surface for security patches than standard Ubuntu images. x86 shapes and Arm-based shapes are supported with this image. For Arm-based shapes, use the Ubuntu image, not Minimal Ubuntu.  
Ubuntu 22.04 LTS | Canonical-Ubuntu-22.04-date-number |  [Ubuntu](https://www.ubuntu.com/) is a free, open-source Linux distribution that is suitable for use in the cloud. [Minimal Ubuntu](https://wiki.ubuntu.com/Minimal) is designed for automated use at scale. It uses a smaller boot volume, boots faster, and has a smaller surface for security patches than standard Ubuntu images. x86 shapes and Arm-based shapes are supported with this image. For Arm-based shapes, use the Ubuntu image, not Minimal Ubuntu.  
Ubuntu 20.04 LTS | Canonical-Ubuntu-20.04-date-number |  [Ubuntu](https://www.ubuntu.com/) is a free, open-source Linux distribution that is suitable for use in the cloud. [Minimal Ubuntu](https://wiki.ubuntu.com/Minimal) is designed for automated use at scale. It uses a smaller boot volume, boots faster, and has a smaller surface for security patches than standard Ubuntu images. x86 shapes and Arm-based shapes are supported with this image. For Arm-based shapes, use the Ubuntu image, not Minimal Ubuntu.  
Windows Server 2022 | Windows-Server-2022-<edition>-<gen>-<date>-<number> |  Windows Server 2022 supports running production Windows workloads on Oracle Cloud Infrastructure.  [Server Core](https://docs.microsoft.com/windows-server/administration/server-core/what-is-server-core) is a minimal installation option that has a smaller disk footprint and therefore a smaller attack surface. x86 shapes and GPU shapes are supported with this image. You must install the appropriate GPU drivers from NVIDIA.  
Windows Server 2019  | Windows-Server-2019-edition-gen-date-number |  Windows Server 2019 supports running production Windows workloads on Oracle Cloud Infrastructure.  [Server Core](https://docs.microsoft.com/windows-server/administration/server-core/what-is-server-core) is a minimal installation option that has a smaller disk footprint and therefore a smaller attack surface. x86 shapes and GPU shapes are supported with this image. You must install the appropriate GPU drivers from NVIDIA.  
Windows Server 2016  | Windows-Server-2016-edition-gen-date-number |  Windows Server 2016 supports running production Windows workloads on Oracle Cloud Infrastructure.  [Server Core](https://docs.microsoft.com/windows-server/administration/server-core/what-is-server-core) is a minimal installation option that has a smaller disk footprint and therefore a smaller attack surface. x86 shapes and GPU shapes are supported with this image. You must install the appropriate GPU drivers from NVIDIA.  
1: Image names can include additional information about the processor architecture, operating system, or supported shapes. For example:
  * Images with "aarch64" in the name, such as Oracle-Linux-8.x-aarch64-edition, are for shapes that use Arm-based processors. Images without "aarch64" in the name are for shapes that use x86 processors.
  * Images with "GPU" in the name, such as Oracle-Linux-8.x-Gen2-GPU-edition, are for GPU shapes. Some images, such as Windows Server, have a single image build that supports both GPU shapes and non-GPU shapes.

  
You also can [create custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") of your boot disk OS and software configuration for launching new instances.
## Essential Firewall Rules 🔗 
All platform images include rules that allow only "root" on Linux instances or "Administrators" on Windows Server instances to make outgoing connections to the iSCSI network endpoints (169.254.0.2:3260, 169.254.2.0/24:3260) that serve the instance's boot and block volumes.
  * We recommend that you do not reconfigure the firewall on your instance to remove these rules. Removing these rules allows non-root users or non-administrators to access the instance's boot disk volume.
  * We recommend that you do not create custom images without these rules unless you understand the security risks.
  * Do not use Uncomplicated Firewall (UFW) to edit firewall rules on an Ubuntu image. Using UFW to edit rules might cause an instance not to boot. Therefore, we recommend you edit UFW rules using the method described in this note: [Ubuntu instance fails to reboot after enabling Uncomplicated Firewall (UFW)](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#ufw).


## User Data 🔗 
Platform images give you the ability to run custom scripts or supply custom metadata when the instance launches. To do this, you specify a custom user data script in the **Initialization script** field when you [create the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."). For more information about startup scripts, see [cloud-init](https://cloudinit.readthedocs.io/en/latest/) for Linux-based images and [cloudbase-init](http://cloudbase-init.readthedocs.io/en/latest/) for Windows-based images.
## OS Updates for Linux Images 🔗 
Oracle Linux and CentOS images are preconfigured to let you install and update packages from the repositories on the Oracle public yum server. The repository configuration file is in the `/etc/yum.repos.d` directory on your instance. You can install, update, and remove packages by using the yum utility. 
On Oracle Autonomous Linux images, Oracle Ksplice is installed and configured by default to run automatic updates.
**Note**
OS Security Updates for Oracle Linux and CentOS images
After you launch an instance using an Oracle Linux image, Oracle Linux Cloud Developer image, or CentOS image, you are responsible for applying the required OS security updates published through the Oracle public yum server. For more information, see [Installing and Using the Yum Security Plugin](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_security_yum.html).
The Ubuntu image is preconfigured with suitable repositories to allow you to install, update, and remove packages.
**Note**
OS Security Updates for the Ubuntu image
After you launch an instance using the Ubuntu image, you are responsible for applying the required OS security updates using the `sudo apt-get upgrade` command.
### Linux Kernel Updates Using Ksplice 🔗 
Linux instances on Oracle Cloud Infrastructure can use Oracle Ksplice to apply critical kernel patches without rebooting. Ksplice can maintain specific kernel versions for Oracle Linux, CentOS, and Ubuntu. For more information, see [Oracle Ksplice](https://docs.oracle.com/iaas/oracle-linux/ksplice/index.htm).
### Configuring Automatic Package Updating on Instance Launch 🔗 
You can configure your instance to automatically update to the latest package versions when the instance first launches using a cloud-init startup script. To do this, add the following code to the startup script:
Copy
```
package_upgrade: true
```

The upgrade process starts when the instance launches and runs in the background until it completes. To verify that it completed successfully, check the cloud-init logs in `/var/log`.
See [User Data](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#User) and [Cloud config examples - Run apt or yum upgrade](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#run-apt-or-yum-upgrade) for more information.
## Linux Image Details 🔗 
See [Lifetime Support Policy: Coverage for Oracle Open Source Service Offerings](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf) for details about the Oracle Linux support policy.
### Users 🔗 
For instances created using Oracle Linux and CentOS images, the username `opc` is created automatically. The `opc` user has `sudo` privileges and is configured for remote access over the SSH v2 protocol using RSA keys. The SSH public keys that you specify while creating instances are added to the `/home/opc/.ssh/authorized_keys` file.
For instances created using the Ubuntu image, the username `ubuntu` is created automatically. The `ubuntu` user has `sudo` privileges and is configured for remote access over the SSH v2 protocol using RSA keys. The SSH public keys that you specify while creating instances are added to the `/home/ubuntu/.ssh/authorized_keys` file.
Note that `root` login is disabled.
### Remote Access 🔗 
[Access to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") is permitted only over the SSH v2 protocol. All other remote access services are disabled.
### Firewall Rules 🔗 
Instances created using platform images have a default set of firewall rules that allow only SSH access. Instance owners can modify those rules as needed, but must not restrict link local traffic to address 169.254.0.2 in accordance with the warning in [Essential Firewall Rules](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#image-firewall-rules). 
Be aware that the Networking service uses [network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) and [security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) to control packet-level traffic in and out of the instance. When troubleshooting access to an instance, make sure all of the following items are set correctly: the network security groups that the instance is in, the security lists associated with the instance's subnet, and the instance's firewall rules.
### Disk Partitions 🔗 
Starting with Oracle Linux 8.x, the main disk partition is managed using Logical Volume Management (LVM). This gives you increased flexibility to create and resize partitions to suit your workloads. In addition, there is no dedicated swap partition. Swap is now handled by a file on the file system, giving you more detailed control over swap.
### Cloud-init Compatibility 🔗 
Instances created using platform images are compatible with cloud-init. When launching an instance with the Core Services API, you can pass cloud-init directives with the metadata parameter. For more information, see [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance).
### Oracle Autonomous Linux 🔗 
Oracle Autonomous Linux is a managed service for reducing the complexity and overhead of common operating system management tasks. For more information, see [Oracle Autonomous Linux](https://docs.oracle.com/iaas/oracle-linux/autonomous-linux/index.htm).
### Oracle Linux Cloud Developer 🔗 
[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/developer/index.htm) provides the latest development tools, languages and Oracle Cloud Infrastructure software development kits (SDKs) to rapidly launch a comprehensive development environment.
### OCI Utilities 🔗 
Instances created with Oracle Linux include preinstalled utilities that make it easier to work with Oracle Linux images. For more information, see [OCI Utilities](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm).
## OS Updates for Windows Images 🔗 
Windows images include the Windows Update utility, which you can run to get the latest Windows updates from Microsoft. You have to configure the instance's [network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) or the [security list](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) used by the instance's subnet to allow instances to access Windows update servers. 
## Windows Image Details 🔗 
### Windows Editions 🔗 
Depending on whether you create a bare metal instance or a virtual machine (VM) instance, different editions of Windows Server are available as platform images. Windows Server Standard edition is available only for VMs. Windows Server Datacenter edition is available only for bare metal instances.
### Users 🔗 
For instances created using Windows platform images, the username `opc` is created automatically. When you launch an instance using the Windows image, Oracle Cloud Infrastructure will generate an initial, one-time password that you can retrieve using the console or API. This password must be changed after you initially log on.
### Remote Access 🔗 
[Access to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") is permitted only through a Remote Desktop connection.
### Firewall Rules 🔗 
Instances created using the Windows image have a default set of firewall rules that allow Remote Desktop protocol or RDP access on port 3389. Instance owners can modify these rules as needed, but must not restrict link local traffic to 169.254.169.253 for the instance to activate with Microsoft Key Management Service (KMS). This is how the instance stays active and licensed.
Be aware that the Networking service uses [network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) and [security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) to control packet-level traffic in and out of the instance. When troubleshooting access to an instance, make sure all of the following items are set correctly: the network security groups that the instance is in, the security lists associated with the instance's subnet, and the instance's firewall rules.
### User Data on Windows Images 🔗 
On Windows images, custom user data scripts are executed using [cloudbase-init](http://cloudbase-init.readthedocs.io/en/latest/), which is the equivalent of [cloud-init](https://cloudinit.readthedocs.io/en/latest/) on Linux-based images. All Windows platform images on Oracle Cloud Infrastructure include cloudbase-init installed by default. When an instance launches, cloudbase-init runs PowerShell, batch scripts, or additional user data content. See [cloudbase-init Userdata](http://cloudbase-init.readthedocs.io/en/latest/userdata.html) for information about supported content types. 
You can use user data scripts to perform various tasks, such as:
  * Enable GPU support using a custom script to install the applicable GPU driver. 
  * Add or update local user accounts.
  * Join the instance to a domain controller.
  * Install certificates into the certificate store.
  * Copy any required application workload files from the Object Storage service directly to the instance.


**Caution** Do not include anything in the script that could trigger a reboot, because this could impact the instance launch, causing it to fail. Any actions requiring a reboot should only be performed after the instance state is **running**.
### Windows Remote Management 🔗 
[Windows Remote Management](https://docs.microsoft.com/windows/desktop/winrm/portal) (WinRM) is enabled by default on Windows platform images. WinRM provides you with the capability to remotely manage the operating system. 
To use WinRM you need to add a stateful ingress [security rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm) for TCP traffic on destination port 5986. You can implement this security rule in either a [network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) that the instance belongs to, or a [security list](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) that is used by the instance's subnet.
**Caution** The following procedure allows WinRM connections from 0.0.0.0/0, which means any IP address, including public IP addresses. To allow access only from instances within the VCN, change the source CIDR value to the VCN's CIDR block. For more information, see [Securing Networking](https://docs.oracle.com/iaas/Content/Security/Reference/networking_security.htm).
[To enable WinRM access](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  2. Click the virtual cloud network (VCN) that you're interested in.
  3. Do one of the following things:
     * To add the rule to a network security group that the instance belongs to:
       1. Under **Resources** , click **Network Security Groups**. Then click the network security group that you're interested in.
       2. Click **Add Rules**.
       3. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Direction:** Ingress
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** TCP
          * **Source Port Range:** All
          * **Destination Port Range:** 5986
          * **Description:** An optional description of the rule.
       4. Click **Add**.
     * To add the rule to a security list that is used by the instance's subnet:
       1. Under **Resources** , click **Security Lists**. Then click the security list you're interested in.
       2. Click **Add Ingress Rules**.
       3. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** TCP
          * **Source Port Range:** All
          * **Destination Port Range:** 5986
          * **Description:** An optional description of the rule.
       4. Click **Add Ingress Rules**.


[To use WinRM on an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm)
  1. [Get the instance's public IP address](https://docs.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm#Getting). 
  2. Open Windows PowerShell on the Windows client that you're using to connect to the instance.
  3. Run the following command:
Copy
```
# Get the public IP from the running Windows instance
$ComputerName = <public_IP_address>
# Store your username and password credentials (default username is opc)
$c = Get-Credential
# Options
$opt = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
# Create new PSSession (Prerequisite: ensure network security group or security list has ingress rule for port 5986) 
$PSSession = New-PSSession -ComputerName $ComputerName -UseSSL -SessionOption $opt -Authentication Basic -Credential $c
# Connect to Instance PSSession
Enter-PSSession $PSSession
# To close connection use: Exit-PSSession 

```

<public_IP_address> is the [instance's public IP address](https://docs.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm#Getting).


You can now remotely manage the Windows instance from your local PowerShell client.
## Operating System Lifecycle and Support Policy 🔗 
When an operating system reaches the end of its support lifecycle, the OS vendor (such as Microsoft) no longer provides security updates for the OS. Upgrade to the latest version to remain secure.
Here's what to expect when an OS version reaches the end of its support lifecycle:
  * Oracle Cloud Infrastructure no longer provides new images for the OS version. Images that were previously published are deprecated, and are no longer updated.
  * Although you can continue to run instances that use deprecated images, Oracle Cloud Infrastructure does not provide any support for operating systems that have reached the end of the support lifecycle.
  * If you have an instance that runs an OS version that is being deprecated, and you want to create instances with this OS version after the end of support, then you can create a custom image of the instance and then use the custom image to create instances in the future. For custom Linux images, you must purchase extended support from the OS vendor. For custom Windows images, see [Can I purchase Microsoft Extended Security Updates for end-of-support Windows OSs?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#generalquestions__extended-security) Oracle Cloud Infrastructure does not provide any support for custom images that use end-of-support operating systems.


**Important** Oracle Cloud customers using Oracle Linux are entitled to both Premier Support and Extended Support (when offered). For more information, see [Oracle Linux on Oracle Cloud Infrastructure: Frequently Asked Questions](https://www.oracle.com/a/ocom/docs/oracle-linux-for-cloud-infrastructure-faq.pdf). See [Lifetime Support Policy: Coverage for Oracle Open Source Service Offerings](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf) for support coverage dates for Oracle Linux.
Be aware of these end-of-support dates:
  * **Oracle Linux 6:** Extended Support ended on December 31, 2024.
  * **Oracle Linux 7:** Premier Support ended on December 31, 2024.
  * **CentOS 6:** Support ended on November 30, 2020.
  * **CentOS 7:** Support ended on June 30, 2024.
  * **CentOS 8:** Support ended on December 31, 2021.
  * **CentOS Stream 8:** Support ended on May 31, 2024.
  * **Ubuntu 14.04:** Support ended on April 19, 2019.
  * **Ubuntu 16.04:** Support ended in April 2021.
  * **Ubuntu 18.04:** Support ended in June 2023.
  * **Windows Server 2008 R2:** Support ended on January 14, 2020.
  * **Windows Server 2012 R2:** Support ended on Oct 10, 2023


Was this article helpful?
YesNo

