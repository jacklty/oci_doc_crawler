Updated 2023-08-29
# iSCSI Commands and Information
Block volumes attached with the [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI) attachment type use the **iSCSI** protocol to connect a volume to an instance. See [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype) for more information about volume attachment options.
Once the volume is **attached** , you need to log on to the instance and use the `iscsiadm` command-line tool to configure the iSCSI connection. After you configure the volume, you can mount it and use it like a normal hard drive. 
To enhance security, Oracle enforces an iSCSI security protocol called **CHAP** that provides authentication between the instance and volume. 
**Note**
You do not need to run the iSCSI commands for attachments to volumes configured for the **Ultra High Performance** level. The Block Volume Management plugin runs the iSCSI commands to configure the iSCSI connection.
For these volumes, you need to ensure that you have configured the required prerequisites and that the Block Volume Management plugin is installed and enabled. For more information, see the following topics: 
  * [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.")
  * [Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#enablingblockvolumemanagementplugin "Enable the Block Volume Management plugin on a Compute instance.")
  * [Troubleshooting Ultra High Performance Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm#troubleshootuhp "This topic covers troubleshooting steps you can take as well as prerequisites to verify for volumes configured for the Ultra High Performance level where either the volume fails to attach or the volume attachment is not multipath-enabled.")


## Accessing a Volume's iSCSI Information 🔗 
When you successfully attach a volume to an instance, Block Volume provides a list of iSCSI information. You need the following information from the list when you **connect** the instance to the volume.
  * IP address
**Note** When an IP address is assigned to a volume attachment, it is a valid IP address and an iSCSI connection can be made to it. Block Volume does not guarantee the order the IP address is assigned.
  * Port
  * CHAP user name and password (if enabled)
  * IQN


**Note** The CHAP credentials are auto-generated by the system and cannot be changed. They are also unique to their assigned volume/instance pair and cannot be used to authenticated another volume/instance pair.
The Console provides this information on the details page of the volume's attached instance. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) on your volume's row, and then click **iSCSI Information**. The system also returns this information when the `AttachVolume[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/AttachVolume)` API operation completes successfully. You can re-run the operation with the same parameter values to review the information.
See [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.") and [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance.") for step-by-step instructions. 
## Recommended iSCSI Initiator Parameters for Linux-based Images 🔗 
iSCSI attached volumes for Linux-based images are managed by the Linux iSCSI initiator service, **iscsid**. Oracle Cloud Infrastructure images use iSCSI default settings for the **iscsid** service's parameters, with the exception of the following parameters: 
  * `node.startup = automatic`
  * `node.session.timeo.replacement_timeout = 6000`
  * `node.conn[0].timeo.noop_out_interval = 0`
  * `node.conn[0].timeo.noop_out_timeout = 0`
  * `node.conn[0].iscsi.HeaderDigest = None`


If you are using custom images, you should update the **iscsid** service configuration by modifying the `/etc/iscsi/iscsid.conf` file. 
## Additional Reading 🔗 
There is a wealth of information on the internet about iSCSI and CHAP. If you need more information on these topics, try the following pages:
  * [Oracle Linux 8 Managing Storage Devices - Working With Linux I-O Storage](https://docs.oracle.com/en/operating-systems/oracle-linux/8/stordev/stordev-WorkingWithLinuxIOStorage.html)
  * [Oracle Linux Administrator's Guide for Release 7 - About iSCSI Storage](https://docs.oracle.com/cd/E52668_01/E54669/html/ol7-s15-storage.html)
  * [Oracle Linux Administrator's Guide for Release 6 - About iSCSI Storage](https://docs.oracle.com/cd/E37670_01/E41138/html/ch18s07.html)
  * [Troubleshooting iSCSI Configuration Problems](https://docs.oracle.com/cd/E23824_01/html/821-1459/fpjwy.html)


Was this article helpful?
YesNo

