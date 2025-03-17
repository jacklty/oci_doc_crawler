Updated 2025-02-20
# Sending a Diagnostic Interrupt
You can send a diagnostic interrupt to troubleshoot an unresponsive or unreachable Compute virtual machine (VM) instance.
**Caution** This feature is for advanced users. Sending a diagnostic interrupt to a live system can cause data corruption or system failure.
A diagnostic interrupt causes the instance's OS to crash and reboot. Before you send a diagnostic interrupt, you must configure the OS to generate a crash dump (also called a memory dump file) when it crashes. The crash dump captures information about the state of the OS at the time of the crash. After the OS restarts, you can analyze the crash dump to identify and debug the issue.
**Tip** For more information about troubleshooting using crash dumps, see: [Collecting Crash Dumps Using Kdump Utility](https://docs.oracle.com/iaas/oracle-linux/diagnostics/diagnostics-kdump.htm).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to send a diagnostic interrupt to an instance. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only `manage instance-family`, and remove the statements involving `volume-family` and `virtual-network-family`.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
## Before You Begin 🔗 
  * The instance's OS must be [configured to generate a crash dump file](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm#configuring-os-to-generate-crash-dump).
  * The instance must be in the **Running** state. For more information, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
  * There are no in-progress actions affecting the instance, such as block volumes or secondary VNICs in the process of being attached or detached.


## Configuring the OS to Generate a Crash Dump 🔗 
Before you send a diagnostic interrupt to an instance, you must configure the OS to generate a crash dump when it crashes. The diagnostic interrupt is received as a non-maskable interrupt (NMI) on the target instance.
The steps depend on the OS.
### Linux 🔗 
**Note**
On Oracle Linux [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images), the OS is either fully configured or partially configured to generate a crash dump, depending on the image release date.
[Oracle Linux 8](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm)
  * **Images released in August 2020 or later:** The image is fully configured to generate a crash dump.
  * **Earlier images:** The dump-capture kernel is installed and configured, but you must perform the other configuration steps.


[Oracle Linux 7](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm)
  * **Images released in August 2020 or later:** The image is fully configured to generate a crash dump.
  * **Earlier images:** The dump-capture kernel is installed and configured, but you must perform the other configuration steps.


  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.").
  2. Install and configure the dump-capture kernel:
    1. Install `kdump` and `kexec` by running the following command:
Copy
```
sudo yum install kexec-tools
```

    2. Reserve memory on the kernel to save the crash dump. Do the following:
      1. Open the `etc/default/grub` file in a text editor.
      2. In the line that starts with `GRUB_CMDLINE_LINUX_DEFAULT`, add the parameter `crashkernel=<memory-to-reserve>`. For example, to reserve 100 MB, add `crashkernel=100M`.
      3. Save the changes and close the file.
      4. Rebuild the GRUB file by running the following command:
Copy
```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

  3. Configure the kernel to crash when it receives a diagnostic interrupt. To do this, open the `/etc/sysctl.conf` file in a text editor and add the following line:
Copy
```
kernel.unknown_nmi_panic=1
```

  4. Apply the change to `/etc/sysctl.conf` by running the following command:
Copy
```
sysctl -p
```



### Windows Server - Platform Image 🔗 
If you use a Windows Server [platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images) that was released in April 2020 or later, the image is already configured to generate a crash dump.
If you use an image that was released before April 2020, do the following:
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.").
  2. [Download the Oracle VirtIO Drivers for Microsoft Windows](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html).
  3. [Install the drivers](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindows.html) and then restart the instance.


### Windows Server - Customer-Provided Image 🔗 
Refer to the third-party documentation for your operating system for more information.
## Sending a Diagnostic Interrupt 🔗 
After you configure the instance's OS to generate a crash dump when it crashes, use the following procedures to send a diagnostic interrupt.
### To send a diagnostic interrupt using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click **More Actions** , and then click **Send diagnostic interrupt**.
**Caution** Sending a diagnostic interrupt to a live system can cause data corruption or system failure.
  4. Review the confirmation message and then click **Send diagnostic interrupt**.
The lifecycle state that appears in the Console remains **Running** while the instance's OS crashes and restarts. Do not send multiple diagnostic interrupts.
  5. Wait several minutes for the instance's OS to restart, and then [connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection."). You can now retrieve and analyze the crash dump.


### To send a diagnostic interrupt using the API 🔗 
Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation, passing the value `SENDDIAGNOSTICINTERRUPT` as the action to perform.
## Analyzing a Crash Dump 🔗 
The crash dump is saved locally on the instance's OS.
  * **Linux instances:** The default location where the crash dump is saved depends on the operating system.
    * **Oracle Linux 8:** Saved in `/var/oled/crash`.
    * **Oracle Linux 7:** For platform images released in March 2021 or later, saved in `/var/crash`. For older platform images, saved in `/var/oled/crash`.
    * **Other Linux and UNIX-like operating systems:** Saved in `/var/crash/`.
To change the location, modify the `/etc/kdump.conf` file.
  * **Windows instances:** The crash dump is saved in `%SystemRoot%memory.dmp`. On most Windows systems, this is `C:\Windows\memory.dmp`.


To analyze the crash dump, use a third-party tool such as the [crash](http://manpages.org/crash/8) utility on Linux instances or [WinDbg](https://docs.microsoft.com/windows-hardware/drivers/debugger/crash-dump-files) on Windows instances.
Was this article helpful?
YesNo

