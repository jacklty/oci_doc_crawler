Updated 2024-05-30
# Configuring Attachments to Ultra High Performance Volumes
When you attach a volume configured for the **Ultra High Performance** level, to achieve the optimal performance, the volume attachment must be multipath-enabled.
The Block Volume service attempts to enable the attachment for multipath when the volume is being attached. If not all of the prerequisites have been addressed, the volume attachment will not be multipath-enabled.
To determine if the volume attachment is multipath-enabled, see [Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/multipathcheck.htm#multipathcheck "When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.").
This topic describes the prerequisites and the steps you can take to ensure the volume attachment is multipath-capable.
For iSCSI attachments, see [Multipath-Enabled iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#iSCSI_Attach). After you have confirmed that the iSCSI attachment is multipath-enabled, see [Working with Multipath-Enabled iSCSI-Attached Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtouhpvolumes.htm#connectingtouhpvolumes "When you attach a volume configured for the Ultra High Performance level, to optimize performance, the volume attachment must be enabled for multipath.") for steps you can use for connecting to and working with the volume.
For paravirtualized attachments, see [Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#pv_attach). 
## Multipath-Enabled iSCSI Attachments 🔗 
The section describes the prerequisites and steps required to configure multipath-enabled iSCSI volume attachments.
### Prerequisites 🔗 
Following is a list of prerequisites and requirements for multipath-enabled iSCSI attachments.
  1. The instance must be based on a supported shape. See [Supported Compute Shapes for Multipath-Enabled iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_shapes_iSCSI) for more information.
  2. The instance must be running a supported image, see [Supported Images for Multipath-Enabled iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_images_iSCSI) for more information.
  3. The maximum number of ultra high performance block volume attachments is 32.
     * Multiple ultra high performance volumes are supported on instances with Oracle Cloud Agent version 1.39 or later. Check the version with one of the following commands:
Oracle Linux: `yum info               oracle-cloud-agent`
Ubuntu: `snap info                 oracle-cloud-agent`
     * If an ultra high performance volume is already attached before using the multiple ultra high performance volumes feature, then we recommend that you reattach the volumes to achieve best performance. If you don't reattach the volumes, then you will not achieve best performance.
     * If an ultra high performance volume is attached to the instance, and if Oracle Cloud Agent is upgraded to version 1.39, or later, for the first time, then we recommend that you reboot the instance to achieve best performance. If you don't reboot the instance, then you will not achieve the best maximum performance per instance.
  4. The Block Volume Management plugin must be enabled for the instance. See [Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#enablingblockvolumemanagementplugin "Enable the Block Volume Management plugin on a Compute instance.") for more information.
  5. The compute instance must have either a public IP address or a service gateway for the Block Volume Management plugin to be able to connect to Oracle services, see [Service gateways or public IP addresses](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq__pre-req_servicegate).
  6. Permissions must be configured to allow the Block Volume Management plugin to report the iSCSI setup results for multipath-enabled iSCSI attachments, see [Configure Permissions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#blockplugin-prereq__perms).
  7. The volume attachment must be configured to use a consistent device path. See [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths) for more information.


**Important**
You can use `oci-utils` or `oci-iscsi-config` when configuring and working with iSCSI attached volumes, however you should ensure that you don't use both at the same time. If you've started using one of these tools to work with a volume, you should continue to use the same tool with that volume, and not switch to using the other tool. If you use both, you could encounter the behavior described in [Volume Attachment Incorrectly Reported as Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm#troubleshootingmultipathattachments_topic-Multipath_Incorrect).
### Supported Images for Multipath-Enabled iSCSI Attachments 🔗 
For multipath-enabled attachments, the attached instance must be running a Linux-based image.
**Note** Multipath-enabled attachments are not supported for Windows instances or Oracle Autonomous Linux instances.
#### Required Custom Image Configuration to Support Multipath-Enabled iSCSI Attachments
For a custom image to support multipath-enabled iSCSI attachments, the Unbreakable Enterprise Kernel (UEK) version must be UEK6U1 or higher. The UEK6U1 UEK is associated with the kernel major release version 5.4.17-2036, released in November, 2020.
After you have verified that the custom image UEK version is one that supports multipath-enabled attachments, you need to update the `Storage.Iscsi.MultipathDeviceSupported` property for the image to `true`. For more information, see [Configuring Image Capabilities for Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm).
### Supported Compute Shapes for Multipath-Enabled iSCSI Attachments 🔗 
This section identifies the Compute shapes that support multipath-enabled iSCSI attachments. For more details, such as performance characteristics and maximum number of attachments, see [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details). 
[VM Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm)
Current VM shapes configured for 16 cores or more support multipath-enabled attachments. See [VM Shapes for iSCSI and Paravirtualized Attached Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_vm_iscsi) for performance characteristics of volumes attached to VMs with iSCSI attachments. To verify that a shape supports multipath-enabled attachments look for the value **Yes** in the **Supports Ultra High Performance (UHP)** column in the VM Shapes table.
[Bare Metal Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm)
All current bare metal shapes support multipath-enabled iSCSI attachments. See for more information [Bare Metal Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_bm) for performance characteristics of block volumes attached to bare metal instances.
## Multipath-Enabled Paravirtualized Attachments 🔗 
The section describes the prerequisites and steps required to configure multipath-enabled paravirtualized volume attachments.
### Prerequisites 🔗 
Following is a list of prerequisites and requirements for multipath-enabled paravirtualized attachments.
  1. The instance must be based on a supported shape. See [Supported Compute Shapes for Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_shapes_pv) for more information.
  2. The instance must be running a supported image, see [Supported Images for Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_images_pv) for more information.
  3. Maximum number of ultra high performance block volume attachments is 32, with some exceptions as noted in [Block Volume Capabilities and Limits](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Capabil).
If an ultra high performance volume is already attached, then we recommend that you reattach the volumes to achieve best performance. If you do not reattach the volumes, then you will not achieve best maximum performance per instance.


### Supported Images for Multipath-Enabled Paravirtualized Attachments 🔗 
For multipath-enabled attachments, the attached instance must be running one of the following images or a custom image based on one of these images:
  * Oracle Linux
  * Ubuntu
  * CentOS
  * Windows


**Note** Multipath-enabled attachments are not supported for Oracle Autonomous Linux instances.
### Supported Compute Shapes for Multipath-Enabled Paravirtualized Attachments 🔗 
Current VM shapes configured for 16 cores or more support multipath-enabled attachments. See [VM Shapes for iSCSI and Paravirtualized Attached Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_vm_iscsi) for performance characteristics of volumes attached to VMs with paravirtualized attachments. To verify that a shape supports multipath-enabled attachments look for the value **Yes** in the **Supports Ultra High Performance (UHP)** column in the VM Shapes table.
**Note** Multipath-enabled attachments to bare metal instances only support iSCSI attachments.
For more details, such as performance characteristics and maximum number of attachments, see [Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details). 
Was this article helpful?
YesNo

