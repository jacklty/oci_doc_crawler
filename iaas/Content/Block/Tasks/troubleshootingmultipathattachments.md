Updated 2024-11-22
# Troubleshooting Ultra High Performance Volume Attachments
This topic covers troubleshooting steps you can take as well as prerequisites to verify for volumes configured for the **Ultra High Performance** level where either the volume fails to attach or the volume attachment is not multipath-enabled.
## Troubleshooting Volume Attachment Failures 🔗 
The Block Volume Management plugin is required for volumes configured for **Ultra High Performance** , attached using the iSCSI attachment type. If the volume fails to attach to the instance, the issue is likely caused by incorrect configuration for the Block Volume Management plugin. See the troubleshooting suggestions in this section for these issues.
[Block Volume Management Plugin Log Error: Volume Attachment Not Authorized or Not Found Error](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
If you have not configured permissions correctly for the Block Volume Management plugin, the volume will fail to attach to the instance.
#### Details
The volume will not show up as attached in the Console and you will see a `NotAuthorizedOrNotFound` error message in the Block Volume Management plugin log.
The Block Volume Management plugin log is located in:
```
"/var/log/oracle-cloud-agent/plugins/oci-blockautoconfig/oci-blockautoconfig.log
```

The following is an sample error log entry for this issue:
```
2021/08/13 09:14:25.864932 compute_client_command.go:255: Updating volume attachment to the state LOGIN_SUCCEEDED ...
2021/08/13 09:14:26.155473 compute_client_command.go:260: Service error:NotAuthorizedOrNotFound.
volume attachment ocid1.volumeattachment.oc1.iad.<volume-attachment_ID> not found.
http status code: 404. Opc request id: <request_ID>
```

#### Cause
The Block Volume Management plugin does not have sufficent permissions to send the iSCSI login status notification to the service.
#### Resolution
To configure permissions for the Block Volume Management plugin:
  1. **Create Dynamic Group** : Create a dynamic group with the matching rules in the following code sample, to include all instances in the specified compartments:
```
ANY {instance.compartment.id = 'ocid1.tenancy.oc1..<tenancy_ID>', instance.compartment.id = 'ocid1.compartment.oc1..<compartment_OCID>'
```

  2. **Configure Policy for Dynamic Group** : Configure a policy granting permissions to the dynamic group created in the previous step to enable the instance agent access to call the Block Volume service to retrieve the attachment configuration.:
```
Allow dynamic-group InstantAgent to use instances in tenancy
Allow dynamic-group InstantAgent to use volume-attachments in tenancy
```



#### Resources
  * [Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#enablingblockvolumemanagementplugin "Enable the Block Volume Management plugin on a Compute instance.")


[Block Volume Management Plugin Log Error: User Agent Can Not Be Blank](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
The compute instance must have either a public IP address or a service gateway to be able to connect to Oracle services or the volume will fail to attach.
#### Details
The volume will not show up as attached in the Console and you will see a `user agent can not be blank` error message in the Block Volume Management plugin log.
The Block Volume Management plugin log is located in:
```
"/var/log/oracle-cloud-agent/plugins/oci-blockautoconfig/oci-blockautoconfig.log
```

The following is an sample error log entry for this issue:
```
2021/10/15 22:16:07.881953 compute_client_command.go:255: Updating volume attachment to the state LOGIN_SUCCEEDED ...
2021/10/15 22:16:07.882185 compute_client_command.go:260: user agent can not be blank
2021/10/15 22:16:07.882204 iscsi_commands_helper.go:302: user agent can not be blank
2021/10/15 22:16:07.882212 iscsi_commands_helper.go:310: user agent can not be blank
```

#### Cause
The Block Volume Management plugin cannot send the iSCSI login status notification to the service due to the network configuration.
#### Resolution
If the instance does not have a public IP address, set up a service gateway on the virtual cloud network (VCN). The service gateway lets your instance privately access Oracle services without exposing the data to the public internet. Here are special notes for setting up the service gateway for the Block Volume Management plugin: 
  * When creating the service gateway, enable the service label called **All <region> Services in Oracle Services Network**.
  * When setting up routing for the subnet that contains the instance, set up a route rule with **Target Type** set to **Service Gateway** , and the **Destination Service** set to **All <region> Services in Oracle Services Network**.


For detailed instructions, see [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
#### Resources
  * [Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#enablingblockvolumemanagementplugin "Enable the Block Volume Management plugin on a Compute instance.")
  * [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)


## Volume Attachment is not Multipath-Enabled 🔗 
When you attach a volume configured for the **Ultra High Performance** level, to achieve the optimal performance, the volume attachment must be multipath-enabled. The Block Volume service attempts to enable the attachment for multipath when the volume is being attached. If not all of the prerequisites have been addressed, the volume attachment will not be multipath-enabled.
[Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
To check whether a volume attachment is multipath-enabled in the Console from the **Volume Details** page:
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to check the volume attachment for.
  3. Click **Attached Instances** in the **Resources** section.
  4. Check the value displayed in the **Multipath** column. 
     * **Yes** : The volume is configured for the **Ultra High Performance** level and the volume attachment is multipath-enabled. No further action is required.
     * **No** : The volume is not configured for the **Ultra High Performance** level, the volume does not need to be multipath-enabled. No further action is required.
     * **No** with a warning icon: The volume is configured for the **Ultra High Performance** level, but the volume attachment is not multipath-enabled. To achieve optimal performance, you need to ensure the volume is attached to a supported instance shape, and that the required prerequisites are configured.


If the volume is configured for the **Ultra High Performance** level, but not configured for multipath as required, the **Multipath** column will contain **No** with a warning triangle, as shown for the first row in the following screenshot: 
[![Multipath column values in the Console.](https://docs.oracle.com/en-us/iaas/Content/Block/Images/multipathcolumn.png)](https://docs.oracle.com/en-us/iaas/Content/Block/Images/multipathcolumn.png)
For additional procedures to verify whether a volume is multipath enabled, including using the CLI or API, see [Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/multipathcheck.htm#multipathcheck "When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.").
If your volume is not configured for multipath, to troubleshoot the issue, review the information covered in this section and address any issues raised.
[Instance must be based on a supported Compute Shape](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
You must attach a volume configured for the **Ultra High Performance** level to an instance based on a supported shape, configured for at least 16 cores.
#### Supported Shapes
All current bare metal shapes support multipath-enabled iSCSI attachments. See for more information [Bare Metal Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_bm) for performance characteristics of block volumes attached to bare metal instances.
Current VM shapes configured for 16 cores or more support multipath-enabled attachments. See [VM Shapes for iSCSI and Paravirtualized Attached Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_vm_iscsi) for performance characteristics of volumes attached to VMs.
#### Resolution
If the volume isn't attached to an instance with a supported shape configuration, you need to detach the volume and attach it to an instance with a supported shape configuration.
You can also edit the existing instance so that it has the correct shape configuration, but you need to ensure that you detach and reattach the volume after you edit the instance.
**Warning** If the instance has less than 8 OCPUs, you might see an issue, where after you edit the instance to support multipath-enabled attachments, the volume attachment is still not multipath-enabled, even after you detach and reattach the volume. In this scenario, you need to re-create the instance from a [supported shape](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_shapes_pv), and then attach the volume to the new instance. For more information, see [Paravirtualized volume attachment not multipath-enabled after instance is resized](https://docs.oracle.com/iaas/Content/knownissues.htm#noMultipathResizedInstance).
#### Resources
  * [Multipath-Enabled iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#iSCSI_Attach)
  * [Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#pv_attach)
  * [Changing the Shape of an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm)
  * [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.")
  * [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.")


[Compute Image Must Support Multipath Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
You must attach a volume configured for the **Ultra High Performance** level to an instance running an image that supports multipath attachments. This includes custom images.
#### Supported Images for iSCI Attachments
Only platform images running Oracle Linux or custom images based on an Oracle Linux image support multipath attachments. 
Use one of the latest platform Oracle Linux images, with an Unbreakable Enterprise Kernel (UEK) version of UEK6U1 or higher.
For custom images, the Unbreakable Enterprise Kernel (UEK) version must also be UEK6U1 or higher. The UEK6U1 UEK is associated with the kernel major release version 5.4.17-2036, released in November, 2020. You also need to update the `Storage.Iscsi.MultipathDeviceSupported` property for the custom image to `true` and launch the instance again. For more information, see [Configuring Image Capabilities for Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm)
#### Supported Images for Paravirtualized Attachments 🔗 
For multipath-enabled attachments, the attached instance must be running one of the following images or a custom image based on one of these images:
  * Oracle Linux
  * Ubuntu
  * CentOS
  * Windows


**Note** Multipath-enabled attachments are not supported for Oracle Autonomous Linux instances.
Use one of the latest platform Oracle Linux images, with an Unbreakable Enterprise Kernel (UEK) version of UEK6U1 or higher.
#### Resources
  * [Multipath-Enabled iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#iSCSI_Attach)
  * [Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#pv_attach)
  * [Configuring Image Capabilities for Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm)
  * [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)
  * [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.")


[Reattach the Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
If you have updated the shape configuration or the image for an instance to one that supports multipath attachments, you need to detach the volume from the instance and then attach it again to the instance.
#### Resources
  * [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.")
  * [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.")
  * [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.")


[Generate a Diagnostic File for iSCSI Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
For iSCSI attachments, if you have taken all the steps described in this topic and you are still encountering an issue with the volume attachment, use the steps described in [Step 4: Generate a Diagnostic File for Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic) to generate a diagnostic file and contact Oracle support. This step does not apply to paravirtualized attachments.
#### Resources
  * [Troubleshooting Ultra High Performance Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm#troubleshootuhp "This topic covers troubleshooting steps you can take as well as prerequisites to verify for volumes configured for the Ultra High Performance level where either the volume fails to attach or the volume attachment is not multipath-enabled.")
  * [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.")


[Volume Attachment Incorrectly Reported as Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
In certain scenarios, a volume attachment shows as multipath-enabled in the Console, however the attachment isn't actually multipath-enabled, and the volume doesn't achieve the performance expected for the **Ultra High Performance** level. This issue can occur when you use both the `oci-utils` and `oci-iscsi-config` tools at the same time to configure a volume.
Use one of the following methods to check to see if you're encountering this issue.
[Option 1: Linux multipath command](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
Use the `multipath` command to confirm whether a volume attachment is actually multipath-enabled on a Linux instance. Log in to the instance and run the `multipath` command with the `ll` tag, as follows:```
# multipath -ll
```
If the command output returns nothing, this confirms that the instance doesn't have any multipath-enabled attachments.
[Option 2: Check node.startup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm)
Check the node records in `/var/lib/iscsi/nodes/{IQN} ` for `node.startup`, as follows:```
#cd /var/lib/iscsi/nodes/{IQN}
#grep -Hrn 'node.startup' 
```
If any of them have `node.startup=automatic`, the volume attachment isn't multipath-enabled. They must all show `node.startup=manual`.
#### Resolution
If you determine that the attachment isn't multipath-enabled, you can work around this issue using the `/etc/fstab` file. Update the `/etc/fstab` file to tell the `systemd` service to wait until the `multipathd` service is running before mounting the file system. To do this, add `x-systemd.requires=multipathd.service` for the volume. For example:```
UUID={$AFFECTED_VOLUME_UUID} /test ext4 defaults,_netdev,nofail,x-systemd.requires=multipathd.service 0 2 
```

Reboot the instance after you update the `/etc/fstab` file.
For more information about the `/etc/fstab` file, see [Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm#Traditional_fstab_Options) and [fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm#fstab_Options_for_Block_Volumes_Using_Consistent_Device_Paths).
Was this article helpful?
YesNo

