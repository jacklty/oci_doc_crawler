Updated 2025-02-22
# Known Issues for Compute
Known issues have been identified in Compute.
## Known Issues
## Windows systems stuck on loading screen 🔗  

Details
    
After restarting a Windows Compute instance, the systems fails to boot and remains stuck on the loading screen. 

Workaround
    Perform a diagnostic reboot as documented here: [Performing a Diagnostic Reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/diagnostic-reboot.htm#diagnostic-reboot). A diagnostic reboot stops an instance, rebuilds the instance, and then restarts the instance.
## Windows VMs Boot into Repair Dialog 🔗  

Details
    
A Windows Compute virtual machine instance boots into the repair dialog after starting. Additional reboots also boot into the repair dialog.
**Note** This issue occurs in both shielded and non-shielded instances. 

Workaround 1
    Perform a diagnostic reboot as documented here: [Performing a Diagnostic Reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/diagnostic-reboot.htm#diagnostic-reboot). A diagnostic reboot stops an instance, rebuilds the instance, and then restarts the instance.  

Workaround 2
    
If workaround 1 doesn't work, try modifying the instance configuration. For example:
  * Change the shape of an instance, see: [Changing the Shape of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance).
  * Change the fault domain, see: [Editing the Fault Domain for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm#edit-fault-domain)


Then, if necessary, repeat workaround 1.
## Oracle Cloud Agent updater needs restart on Oracle Linux 8 on ARM shapes 🔗  

Details
    
Customers that use Oracle Linux 8 on ARM shapes and run version 1.43.2-18 of Oracle Cloud Agent (OCA) need to restart the updater service on their instances. An OCA updater known issue prevents the updater from polling for future upgrades and a restart resolves the issue.  

Workaround
    To check the current version of OCA on your instance, run the following command: ```
yum info oracle-cloud-agent
```
To restart the updater, run the following command: ```
sudo systemctl restart oracle-cloud-agent-updater
```

## ClamAV identified Oracle Cloud Agent as a virus 🔗  

Details
    
ClamAV signature marked legitimate binaries as viruses because of a bad signature database (virus definition 26931). This issue caused ClamAV to identify Oracle Cloud Agent and its plugins as viruses. By default, ClamAV doesn't quarantine infected files. Therefore, despite the false detection, the agent and its plugins continue to function normally. Even if a quarantine action was taken on an instance, the agent and plugins remain unaffected and functionalities, like Updater and heartbeat, operate as expected. However, a restart of the agent or instance will break the functionality. 

Workaround
    
If your instance is impacted, see [Installing the Oracle Cloud Agent Software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent) to install new package of Oracle Cloud Agent.
## Host network bandwidth is limited to 60 Gbps 🔗  

Details
    An existing limitation in virtual network attachments limits total host network bandwidth to 60 Gbps on BM.Standard.E5.192. 

Workaround
    No workaround exists. We're working on a software fix that will not impact any live network workloads when deployed.
## Unable to edit confidential computing for an instance 🔗  

Details
    After you create a compute instance, you cannot enable or disable confidential computing for that instance at a later time. 

Workaround
    We're working on a resolution.
## Kernel panic during boot when SMEE is enabled 🔗  

Details
    Confidential computing is not supported on Oracle Linux 9. 

Workaround
    We're working on a resolution.
## Soft lockup when booting large SEV guest 🔗  

Details
    
On older generation AMD systems, (E2/E3 using AMD Rome processors), a guest using Secure Encrypted Virtualization (SEV) memory encryption (not enabled by default) with more than 350 GB of memory can result in a CPU soft-lockup warning on the host/hypervisor during guest boot/shutdown, due to the time taken to flush the pinned memory being encrypted being proportional to the amount of memory, and with larger amounts of memory in excess of 350 GB the time taken on the CPU is excessive and results in the warning. After the memory is flushed, the hypervisor returns to regular operation.
Newer systems, such as E4 (based on AMD Milan processors), have hardware support that minimizes the time spent flushing the memory so that no CPU soft-hang occurs. 

Workaround
    If you require an SEV-enabled guest with more than 350 GB of memory, then create it on an E4 system (based on AMD Milan processors). On systems with AMD Rome processors (E2/E3), limit the memory to less than 350 GB, if using SEV memory encryption.
## Multiple shape names are used for some GPU shapes 🔗  

Details
    
For the following list of Compute shapes, multiple names are used for the same shape.
  * **BM.GPU.A10.4:** The name appears as both BM.GPU.A10.4 and BM.GPU.GU1.4.
  * **BM.GPU.A100-v2.8:** The name appears as both BM.GPU.A100-v2.8 and BM.GPU.GM4.8.
  * **VM.GPU.A10.1:** The name appears as both VM.GPU.A10.1 and VM.GPU.GU1.1.
  * **VM.GPU.A10.2:** The name appears as both VM.GPU.A10.2 and VM.GPU.GU1.2.



Workaround
    Disregard the different names. For each shape, the underlying hardware is the same.
## SSH connection issues with macOS Ventura using OpenSSH 9.0 🔗  

Details
    
When you attempt to connect to an instance on Oracle Cloud Infrastructure using a client running macOS Ventura (version 13) or a client running OpenSSH 9.0, you might encounter connection issues resulting in errors similar to the following:
```
Unable to negotiate with 192.0.2.181 port 22: no matching host key type found. Their offer: ssh-rsa
kex_exchange_identification: Connection closed by remote host
```


Workaround
    
Add the following to the `~/.ssh/config` file:
```
Host *
 PubkeyAcceptedKeyTypes +ssh-rsa
 HostkeyAlgorithms +ssh-rsa
```

## Instances running September 2022 platform image for CentOS 7 lose connection to boot volumes after 24 hours 🔗  

Details
    Instances that run the September 2022 platform image for CentOS 7 (image name `CentOS-7-2022.09.20-0`) lose connection to iSCSI-attached boot volumes after 24 hours. The issue happens because the instance loses its DHCP lease after 24 hours. 

Workaround
    
We recommend that you [terminate (delete)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.") any existing instances that use this image, and recreate the instances using a different CentOS 7 platform image.
If you cannot terminate any existing instances that use the September 2022 CentOS 7 platform image, you can obtain a new 24-hour DHCP lease by [rebooting the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
## Error when creating a new external vSwitch on previous generation bare metal shapes running Windows Server 2016 🔗  

Details
    
This issue affects bare metal instances that use previous generation shapes (for the purposes of this known issue, shapes with an end of orderability date before October 2022) and that run Windows Server 2016 Datacenter edition.
When you open the Hyper-V Virtual Switch Manager and try to create a new external virtual switch (vSwitch), an error message similar to the following is displayed: "Error applying Virtual Switch Properties changes: Failed while adding virtual Ethernet switch connections."
The error happens because a Broadcom driver that is installed after running Microsoft Windows Update is not certified by Oracle. 

Workaround
    Broadcom driver version 20.8.24.0 is certified by Oracle. Install version 20.8.24.0.
## Kernel panic when running containers on Ubuntu 20.04, kernel 5.13.0-1033.39~20.04.1 🔗  

Details
    When you run containers on a Compute instance that uses Ubuntu 20.04, kernel version linux-oracle-5.13 5.13.0-1033.39~20.04.1, a kernel panic occurs. The instance crashes and is inaccessible. For more information, see [Docker container creation causes kernel oops on linux-aws 5.13.0.1028.31~20.04.22](https://bugs.launchpad.net/ubuntu/+source/linux-aws-5.13/+bug/1977919). 

Workaround
    
Upgrade the kernel to a higher version by running the following commands:
Copy
```
sudo apt-get update
```

Copy
```
sudo apt-get upgrade -y linux-image-oracle
```

## Older E3/E4 flex shape VM instances fail to start after resizing memory to more than 1,010 GB 🔗  

Details
    E3/E4 flex shape VM instances created before April 5, 2021 fail to start if the memory is resized to more than 1,010 GB. In this case, you see an error that reads "failed to start." 

Workaround 1
    Reduce the size of memory to less than 1,010 GB. 

Workaround 2
    Create the instance again, and then resize the instance memory up to 1,024 GB.
## Console shows Oracle Autonomous Linux available as an Always Free image 🔗  

Details
    Oracle Autonomous Linux is not supported for Always Free compute instances, but in the Console, Oracle Autonomous Linux appears in the list of supported images for Always Free shapes. 

Workaround
    We're working on a resolution.
## DNS not working as expected on Oracle Linux instances 🔗  

Details
    In the US East (Ashburn) region, when Oracle Linux instances first boot after provisioning, DNS might not work as expected, and the `search` field in the `/etc/resolv.conf` file might be incomplete. 

Workaround
    Either reboot the instance or wait for the next DHCP lease renewal. After the DHCP lease renewal, the issue resolves automatically. The standard DHCP lease time is 24 hours but varies depending on network settings.
## PCR values change after reboot on Linux 7.x 🔗  

Details
    When you create a shielded instance using Linux 7.x and then reboot the instance, PCR values might change, causing the red shield to appear. 

Workaround
    Some PCR values change at runtime. That change is expected. As a workaround, [reset the golden measurements](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#reset-measurements).
## BM.Standard.A1.160 instances experience degraded network performance to applications running on socket 1 CPUs 🔗  

Details
    Bare metal instances that use the BM.Standard.A1.160 shape experience reduced network performance for workloads running on socket 1 CPUs. 

Workaround
    For applications responsible for processing packets from the network, bind them to CPUs from socket 0.
## Oracle Cloud Agent doesn't post metrics on Windows instances in private subnets with only a service gateway attached 🔗  

Details
    When you provision a compute instance on Windows in a private subnet with a service gateway attached, the Oracle Cloud Agent plugins might not emit metrics. 

Workaround
    Follow the steps in the Microsoft known issue article: [Connectivity issues if the DigiCert Global Root G2 root certificate is not installed](https://learn.microsoft.com/en-us/troubleshoot/mem/configmgr/setup-migrate-backup-recovery/connectivity-issues-digicert-global-root-g2-not-installed).
## VM.Standard.A1.Flex instances support only the paravirtualized networking launch option 🔗  

Details
    
Instances that use the VM.Standard.A1.Flex shape with hardware-assisted (SR-IOV) networking might face performance issues, and in rare cases, data corruption. To prevent this, platform images for OCI Ampere A1 Compute (aarch64) are configured to use paravirtualized networking only. If you create an instance using a platform image and specify hardware-assisted networking, the launch will fail with a message similar to `Failed to validate instance launch options`.
For custom images compatible with OCI Ampere A1 Compute, the launch will succeed, but we strongly recommend not selecting hardware-assisted networking to avoid potential performance and data corruption issues. 

Workaround
    When you create a VM.Standard.A1.Flex instance using a platform image, let Oracle choose the recommended networking launch type. For custom images, do not use hardware-assisted (SR-IOV) networking.
## Limit on size of VM.Standard.A1.Flex shape using the SR-IOV network type 🔗  

Details
    
Instances that use the VM.Standard.A1.Flex shape with hardware-assisted (SR-IOV) networking and have a large number of cores have improved performance over using paravirtualized networking. SR-IOV networking, however, limits the number of cores to 76 and the amount of memory to 456 GB.
If you try to create an instance that exceeds either of those limits, then an error occurs stating that there is insufficient capacity to create the instance. 

Workaround
    We're working on a resolution.
## Invalid shape and image error when creating Intel and AMD instances using Terraform 🔗  

Details
    
When you use Terraform to create an Intel or AMD compute instance using a Linux platform image, the operation might fail with the error code `InvalidParameter` and a message similar to `Shape <shape_name> is not valid for image <image_OCID>`.
This happens if Terraform identifies the latest image based on the image `display_name`. Images for Intel and AMD shapes (x86 processor architecture) have similar names to the images for Arm-based shapes (aarch64 processor architecture), but the images are not cross-compatible across processor architectures. If the latest image is an aarch64 image, Terraform selects an aarch64 image for an x86 shape, causing the operation to fail. 

Workaround
    
Modify the following Terraform files:
  * `/home/opc/JDERefArch_InfraProvisioning/TerraformScripts/global/global.datasources.tf`
  * `/home/opc/JDERefArch_InfraProvisioning/TerraformScripts/pd/pd.datasources.tf`
  * `/home/opc/JDERefArch_InfraProvisioning/TerraformScripts/nonpd/nonpd.datasources.tf`
  * `/home/opc/JDERefArch_InfraProvisioning/TerraformScripts/globalDR/globalDR.datasources.tf`
  * `/home/opc/JDERefArch_InfraProvisioning/TerraformScripts/pdDR/pdDR.datasources.tf`


In the files, update the regular expression that identifies the image to filter out all images for Arm-based shapes. Images for Arm-based shapes include "aarch" in the image name.
For example, for Oracle Linux 8 images, make the following update:
  * **Current regular expression:** `values = ["^.*Oracle-Linux-8[.]*[\\d]*-[^G].*$"]`
  * **Updated regular expression:** `values = ["^.*Oracle-Linux-8[.][0-9]*-[\\d]{4}.[\\d]{2}.[\\d]{2}-[\\d]*$"]`


## Oracle Linux Cloud Developer images cannot be managed by the OS Management service 🔗  

Details
    Instances that use the Oracle Linux Cloud Developer image cannot be managed by the OS Management service. 

Workaround
    Do not install the OS Management Service Agent (`osms-agent`) on Oracle Linux Cloud Developer instances.
## Invalid bucketName error when importing or exporting a custom image 🔗  

Details
    
When you try to import or export a custom image from an Object Storage bucket, an error similar to the following might occur:
`Invalid bucketName: Specified namespace or bucket to export image does not exist`
This error happens for [federated users](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm) and for users authenticating with instance principals tied to a dynamic group. 

Workaround
    Create a pre-authenticated request, and then use the pre-authenticated request to import or export the image. Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials. For detailed steps explaining how to create and use pre-authenticated requests, see [Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) and [Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs__PAR).
## Unable to create instance from boot volume backup 🔗  

Details
    
When you try to create an instance from a boot volume backup in the Console, an error similar to the following might occur:
"There was an error loading the source image for creating an instance. You might not have permission to access this image, or it might be in a different region. If the image is in a different region, you should still be able to launch your instance."
This error can occur when the compartment that contained the deleted image metadata used for the boot volume backup has also been deleted. 

Workaround
    
If the compartment has been deleted, use the CLI to create the instance. For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
To create an instance from a boot volume using the CLI, open a command prompt and run the [launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command. To launch an instance using an image or a boot volume, include the `--source-details` parameter.
Command
CopyTry It
```
oci compute instance launch --availability-domain <availability_domain> --compartment-id, -c <compartment_ocid> --shape <shape> --subnet-id <subnet_id> --source-details <file://path/to/file>
```

## Unable to remove instance from capacity reservation using Terraform 🔗  

Details
    It is not possible to remove an instance from a capacity reservation using Terraform. 

Workarounds
    Use either of the following workarounds:     
  * Use the Console, CLI, or SDK to remove the instance from the capacity reservation.
  * Using Terraform, to enable you to remove an instance, set the `capacity_reservation_id` to a space, as in the following Terraform script example:```
capacity_reservation_id = " "
```



## Creating more than 50 capacity configurations results in an internal error 🔗  

Details
    When you create more than 50 capacity configurations in a [capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity), an internal error occurs. After the error occurs, it's not possible to launch instances against the capacity reservation. 

Workaround
    To avoid this issue, do not add more than 50 capacity configurations to your capacity reservation.
## Capacity reservation service limits are inaccurate 🔗  

Details
    The `<shape>-core-reserved-count` service limit numbers are inaccurate. The number in the **Service Limit** column might show _1,000,000,000_ or _N/A_. The number in the **Available** column might show 1,000,000,000 less the number in the **Usage** column or _N/A_. The 1,000,000,000 value represents a maximum value and might vary. 

Workaround
    For accurate service limits, see [Compute Capacity Reservations](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#computecapacityreservations).
## No service category for capacity reservations when requesting service limit increases 🔗  

Details
    When you request a service limit increase, the **Service Category** menu does not include a category for capacity reservations. 

Workaround
    
In the **Request Service Limit Updates** form:
  * For **Service Category** , select **Others**. 
  * For **Resource** , select **Other Limits**.
  * In the **Reason for Request** field, enter the specific limit to be increased.


## Instance pool creation fails when resources include default tags 🔗  

Details
    When you try to create an instance pool, the instance pool creation fails with the error `"Authorization failed or requested resource not found"`. This happens because resources used by the instance pool contain default tags, and the user does not have permission to the tag namespace. 

Workaround
    
Add a policy statement granting the instance pool user group permission to the tag namespace `Oracle-Tags`:
```
Allow group InstancePoolUsers to use tag-namespaces in tenancy where target.tag-namespace.name = 'oracle-tags'
```

For more information about policies, see [Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools). For more information about default tags, see [Understanding Automatic Tag Defaults](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingautomaticdefaulttags.htm).
## Out of host capacity error when creating compute instances 🔗  

Details
    When you try to create an instance, the instance launch fails with the error code `InternalError` and a message similar to `Out of host capacity`. This happens because of a lack of physical infrastructure capacity for the shape in the requested fault domain and availability domain. 

Workaround
    
Capacity usually becomes available soon for most shapes. To work around this issue, do the following things:
  * To determine whether capacity is available for a specific shape before you create an instance, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
  * If you're using a [previous generation shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#previous-generation-shapes), create the instance using a [current generation shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) instead. Capacity is limited for previous generation shapes.
  * Create the instance in a different availability domain.
  * Create the instance without specifying a fault domain.
  * Create the instance using a smaller shape, or using a shape in a different series.
  * Wait a few minutes and try again.


## In-transit encryption for a boot volume attachment can be edited when unsupported by the image 🔗  

Details
    When the in-transit encryption value for an image is null, the in-transit encryption value for an instance that's created from the image can be set to a non-null value. 

Workaround
    We're working on a resolution.
## Oracle Cloud Agent plugins are not available on domain controllers 🔗  

Details
    When you use a Windows Server instance as a domain controller, features that depend on Oracle Cloud Agent, such as the Monitoring service and the OS Management service, are not available. This happens because the services installed by Oracle Cloud Agent on Windows run with virtual accounts, but virtual accounts are not supported in the domain controller scope. 

Workaround
    
  1. Disable the Oracle Cloud Agent updater by running the following PowerShell command as an administrator:
Copy
```
net stop OCAU
```

**Note** Disabling the Oracle Cloud Agent updater prevents the instance from receiving automatic Oracle Cloud Agent updates in the future. You can [update Oracle Cloud Agent manually](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent__manual-windows), but you must repeat this workaround after updating.
  2. For each Oracle Cloud Agent feature that you want to use, update the service's running user for the applicable NT service to use a domain user account.
Ensure the domain account is a member of Performance Monitor Users or Administrators Group according to the following table. Use **Active Directory Users and Computers** to find an appropriate user account from your domain and ensure the user is a member of the target domain local group, as shown in the following table.
Oracle Cloud Agent Feature | Target Account Type | Target Domain Local Group  
---|---|---  
Oracle Cloud Agent NT service (including the Compute Instance Monitoring plugin) | Domain service account or user account | Performance Monitor Users  
Compute Instance Run Command plugin | Domain service account or a domain user account that has local administrative privileges | Administrators Group  
Oracle Cloud Unified Monitoring Installer Service (Custom Logs Monitoring plugin) | Domain service account or a domain user account that has local administrative privileges | Administrators Group  
OS Management Service Agent plugin | Domain service account or a domain user account that has local administrative privileges | Administrators Group  
Oracle Cloud Agent updater | Domain service account or a domain user account that has local administrative privileges | Administrators Group  
  3. Use `services.msc` to update the service's running user to the domain user account with appropriate domain groups.


## Boot volume backup size larger than expected 🔗  

Details
    Due to a change in how the Compute service handles images, when you create a boot volume backup, the backup is larger than expected. In some cases the boot volume backup might be larger than the boot volume size. 

Workaround
    We're working on a resolution.
## Intermittent issues with SSH access, DNS lookups, and access to the metadata service 🔗  

Details
    
You might experience intermittent errors with any of the following tasks for your compute instance:
  * Connecting to the instance using SSH.
  * Performing a DNS lookup
  * Accessing the metadata service at `http://169.254.169.254/*`.



Workaround
    
To temporarily work around this issue, run the following command on the instance:
```
sudo ethtool -G ens3 tx 513 && sudo ethtool -G ens3 tx 512
```

## iSCSI-attached volumes do not connect on reboot 🔗  

Details
    If you performed a yum update on your instance using the Oracle Linux 7 yum repos between March 22, 2019 and April 9, 2019, you might encounter an issue where iSCSI-attached block volumes are not available after you reboot the instance. 

Workaround
    
This issue occurs when the instance is not configured to automatically login to iSCSI nodes on reboot. To configure automatic login, update the version of the `iscsi-initiator-utils` package by running the following command:
Copy
```
sudo yum update -y iscsi-initiator-utils-6.2.0.874-10.0.7.el7
```

## iscsid service should be configured to restart automatically 🔗  

Details
    Oracle Cloud Infrastructure supports iSCSI attached remote boot and block volumes to compute instances. These iSCSI attached volumes are managed by the `iscsid` service. In scenarios where this service is stopped for any reason, such as the service crashes or a system administrator inadvertently stops the service, it's important that the `iscsid` service is automatically restarted to increase the stability of your infrastructure. 

Workaround
    
For steps to configure the `iscsid` service to restart automatically, see [Updating the Linux iSCSI Service to Restart Automatically](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatingiscsidservice.htm#Updating_the_Linux_iSCSI_Service_to_Restart_Automatically).
## VM instances launch with an iSCSI attached boot volume when you specify a value for the ipxeScript attribute 🔗  

Details
    When you specify a value for the `ipxeScript` attribute of the [Instance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/) for a virtual machine (VM) instance, the instance launches with an iSCSI attachment for the boot volume instead of a paravirtualized attachment. 

Workaround
    We're working on a resolution.
## Instances experience system hang after running firewall-cmd --reload 🔗  

Details
    
A compute instance might experience a system hang after you run the following command to reload the firewall:
```
firewall-cmd --reload
```

Reloading the firewall using this command on a running instance might cause the instance's boot volume to lose its iSCSI connection and crash, based on the order in which firewall rules are reloaded.  

Workaround
    
To prevent this from happening, do not use the `reload` parameter for `firewall-cmd`. Instead, run the `firewall-cmd` command twice, using the `permanent` parameter the first time you call it to ensure you do not lose iSCSI connectivity.
For example:
```
firewall-cmd --permanent
firewall-cmd
```

## Network icon on Windows 2016 instances displays incorrect status 🔗  

Details
    On instances running Windows 2016, a red "x" is displayed on the network connection icon in the taskbar even though there is no issue with the instance's network connectivity. 

Workaround
    If you recycle the `explorer.exe` process the icon will display the correct status. However, this is not a permanent fix; the red "x" will reappear when you reboot the instance.
## Instances running October 2018 release of Ubuntu 18.04 experience system hang 🔗  

Details
    iSCSId is disabled by default in the October 2018 release of the Ubuntu 18.04 platform image, so instances using this operating system might experience a system hang if there is a momentary break in the iSCSI communication. 

Workaround
    
Run the following command to enable iSCSId on the instance:
```
sudo systemctl enable iscsid && sudo systemctl start iscsid
```

## kmsKeyId attribute is null 🔗  

Details
    When calling the [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance) operation or the [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation, the `kmsKeyId` attribute of [InstanceSourceViaImageDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/InstanceSourceViaImageDetails) is null. 

Workaround
    Call the [GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume) operation and retrieve the value from the `kmsKeyId` attribute of [BootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume).
## Ubuntu instance fails to reboot after enabling Uncomplicated Firewall (UFW) 🔗  

Details
    After you enable UFW on a compute instance running Ubuntu, the instance fails to reboot successfully. 

Workaround
    
Do not use UFW to edit firewall rules. Platform images are preconfigured with firewall rules to enable instances to make outgoing connections to the instance's boot and block volumes. For more information, see [Essential Firewall Rules](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Essentia). UFW may remove these rules so that during a reboot the instance is not able to connect to the boot and block volumes. 
To modify or add new firewall rules, update the `/etc/iptables/rules.v4` file instead. Modifications to firewall rules here will take effect after a reboot. To have the rules take effect immediately, run the following:
```
$ sudo su -
# iptables-restore < /etc/iptables/rules.v4
```

## Unable to log in to instance launched from new generalized Windows custom image 🔗  

Details
    You are unable to log in to an instance launched from a newly created custom Windows image. This issue is the result of the image generalization process failing due to a problem with **Sysprep** after upgrading to WMF 5.0. 

Workaround
    Perform the steps described in [Sysprep fails after WMF 5.0 installation](https://docs.microsoft.com/powershell/scripting/windows-powershell/wmf/known-issues/known-issues-50#sysprep-fails-after-wmf-50-installation). 
## Instances launched from Ubuntu 16 custom images require custom network configuration 🔗  

Details
    When importing Ubuntu 16 LTS and newer releases of Ubuntu, DHCP fails to get the gateway configuration, and thus fails to set up a default route to the gateway on the VNIC. 

Workaround
    
Statically configure the default route after import. To do this:
  1. Create the following script:
```
#! /bin/bash -e
								ROUTER_IP=$(/usr/bin/curl --silent http://169.254.169.254/opc/v1/vnics/ | grep "virtualRouterIp" | grep -oP "\d+\.\d+\.\d+\.\d+" | head -n 1)
								echo "Found Router IP $ROUTER_IP"
							ip route add default via $ROUTER_IP
```

and save it to: `/usr/local/bin/configure_default_route.sh`
  2. Run the following command to make the script executable:
```
sudo chmod +x /usr/local/bin/configure_default_route.sh
```

  3. Add the following to `/etc/network/interfaces` so that it is launched each time the system boots up:
```
# OCI Emulated boot network interface
								auto ens3
								iface ens3 inet dhcp
							post-up /usr/local/bin/configure_default_route.sh
```



## Secondary VNIC detachment times out for some instances launched from imported custom images 🔗  

Details
    When you detach a secondary VNIC from instances launched from imported custom images, the operation might time out. 

Workaround
    
The hot plug module, `acpiphp`, needs to be loaded for secondary VNICs to detach correctly in Linux. If a VNIC fails to detach, run the `lsmod` command to display the list of loaded modules, and check the list for `acpiphp`. If you don't see it in the list, load the module by running the following command:
Copy
```
modprobe acpiphp
```

Retry the detachment operation for the secondary VNIC. You might need to reboot the system for the operation to complete successfully.
## Secondary VNIC might be non-functional for older CentOS, Oracle Linux, and RHEL images 🔗  

Details
    
The secondary VNIC feature is not supported for the following operating systems due to a bug in the kernel:
  * CentOS 4, 5
  * Oracle Linux 4, 5
  * RHEL 4, 5 


Secondary VNICs will fail to work after a reboot. 

Workaround
    We're working on a resolution.
## Invalid image error when exporting an image 🔗  

Details
    When you try to export an image, the export fails with an error indicating that the image is invalid. This error only occurs in the US West (Phoenix) region. 

Workaround
    
To work around this issue:
  1. Launch a new instance based on the image you're trying to export, and specify one of the following shapes for the image:
     * BM.Standard1.36
     * BM.DenseIO1.36
     * VM.DenseIO1.4
     * VM.DenseIO1.8
     * VM.DenseIO1.16
  2. Create a custom image using the steps described in [Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.").


After you have created the custom image, you can export this new image.
## Authentication error occurs when connecting to the serial console for a bare metal instance 🔗  

Details
    
When establishing an SSH connection to a bare metal instance, your SSH client must send the correct key the first time. If you have more than one SSH key configured under `~/.ssh` or in your `~/.ssh/config` file, your client may not send the correct key on the first authorization attempt, and you might encounter the following error message: 
```
Received disconnect from UNKNOWN port 65535:2: Too many authentication failures.
```


Workaround
    
Modify the connection string in the SSH command to use the configfile flag `-F` to override the default configuration file, the `-o IdentitiesOnly=yes` option to force the SSH client to use the specified key, and the identity file flag `-i` to specify the SSH key to use, as shown in the following example:
```
ssh -F /dev/null -o IdentitiesOnly=yes -i /<path>/<ssh_key> -o ProxyCommand='ssh -i /<path>/<ssh_key> -W %h:%p -p 443...
```

## Serial console connections do not work for older instances 🔗  

Details
    
**VM instances:** You can only create serial console connections to virtual machine (VM) instances launched on August 26, 2017 or later.
**Bare metal instances:** You can only create serial console connections to bare metal instances launched on October 21, 2017 or later. 

Workaround
    If you need serial console access to an instance launched prior to the dates specified for VM and bare metal instances, you can work around this issue by creating a custom image of the instance. When you launch a new instance based on the custom image, the new instance will have serial console access. For information about creating a custom image, see [Managing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.").
## Inactive listImage parameters and missing Image response fields 🔗  

Details
    The [ListImages](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages) API operation includes parameters for server-side filtering on `operatingSystem` and `operatingSystemVersion`. However, these parameters are currently inactive. Also, the [Image](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/) response object documentation includes the `operatingSystem` and `operatingSystemVersion` attributes, but the object currently does not return these fields. 

Workaround
    
Refer to the display name for platform images. The display name for platform images includes the operating system and operating system version. For example, with the platform image "Oracle-Linux-7.2-2016.09.18-0", "Oracle Linux" is the operating system and the version is "7.2".
We are aware of the omission and plan to support these parameters and attributes.
## Instance reboot fails if the Network Manager service is installed 🔗  

Details
    If the Network Manager service is installed, an instance can fail to reboot. 

Workaround
    
If the Network Manager service is not required, you can uninstall it. If the Network Manager service is required, modify the network interface configuration file before you reboot the instance. Set the NM_CONTROLLED configuration key to "no":
```
NM_CONTROLLED="no"
```

Usually, the network interface configuration file is located in:
```
/etc/sysconfig/network-scripts/ifcfg-<interface_name>
```

## Automatic updates using Oracle Ksplice fail with some FastConnect networking setups 🔗  

Details
    Some FastConnect networking setups prevent automatic patch updates for utilities such as Oracle Ksplice. 

Workaround
    
In the `/etc/uptrack/uptrack.conf` file, replace all instances of:```
oraclecloud-updates-ksplice.oracle.com
```
with:```
updates.ksplice.<region>.oci.oraclecloud.com 
```

For example, if your home region is the US West (Phoenix), replace: ```
oraclecloud-updates-ksplice.oracle.com
```
with:```
updates.ksplice.us-phoenix-1.oci.oracle.com
```

This workaround applies to [service gateways](https://docs.oracle.com/iaas/Content/Network/Concepts/privateaccess.htm#service-gateways). It does not apply to [private endpoints](https://docs.oracle.com/iaas/Content/Network/Concepts/privateaccess.htm#private-endpoints).
## Missing flag is required for the OS Management service for instances created before September 2019 🔗  

Details
    
When using the OS Management service on Oracle Linux instances that were created before September 2019, the Instance Details page might incorrectly indicate that the OS Management service is enabled (Oracle Cloud Management Agent: Enabled) when the service is not enabled.
This issue affects instances that were created before the `isManagementDisabled` flag was defined in the metadata for compute instances. Because this flag is not present, the metadata for these instances is not set properly for the OS Management service. 

Workaround
    
To resolve this issue, set the `isManagementDisabled` flag to false:
  1. In the agent configuration for the instance, set the `isManagementDisabled` option to false:
Copy
```
oci compute instance update --instance-id <instance_OCID> --agent-config '{"isManagementDisabled": false, "isMonitoringDisabled": false}'
```

  2. Use the CLI to verify that the flag has been updated:
Copy
```
oci compute instance get --instance-id <instance_OCID>
```

In the output, the updated flag appears as `"is-management-disabled": false`.
```
{
 "data":
  "agent-config": {
   "is-management-disabled": false,
   "is-monitoring-disabled": false
  },
...
}
```

  3. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") using SSH, and then use cURL to call the instance metadata service and verify that the flag has been updated within the compute instance:
Copy
```
curl http://169.254.169.254/opc/v1/instance/
```

In the output, the updated flag appears as ` "managementDisabled" : false`.
```
{
 ...
 "agentConfig" : {
  "monitoringDisabled" : false,
  "managementDisabled" : false
 }
}
```



## Resolved Issues 🔗 
The are currently no resolved known issues in Compute.
Was this article helpful?
YesNo

