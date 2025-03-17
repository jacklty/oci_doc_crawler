Updated 2024-03-22
# Connecting to iSCSI-Attached Block Volumes
Connect to an iSCSI-attached block volume. 
Connecting to an iSCSI-attached volume doesn't require a specific IAM policy. However, you might need permission to run the necessary commands on the attached instance's guest OS. Contact your system administrator for more information.
## Prerequisites
You must attach the volume to the instance before you can connect the volume to the instance's guest OS. For details, see [Attaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
To connect the volume, you need the following information:
  * iSCSI IP address
  * iSCSI port numbers 
  * CHAP credentials (if you enabled CHAP)
  * IQN 


The Console provides the commands required to configure, authenticate, and log on to iSCSI.
## Connecting to a Volume on a Linux Instance 🔗 
  1. Use the Console to obtain the iSCSI data that you need to connect the volume:
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. Under **List scope** , select the compartment that contains the instance. 
    3. Click the name of the instance to display the instance details.
    4. Under **Resources** , click **Attached block volumes** to view the attached block volume. 
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the volume that you're interested in, and then select **iSCSI Commands and Information**. 
The **iSCSI Commands and Information** dialog box displays specific identifying information about the volume and the iSCSI commands you need. The commands are ready to use with the appropriate information included. You can copy the commands and paste them into your instance session window for each of the following steps.
  2. Log in to the instance's guest OS.
  3. Register the volume with the `iscsiadm `tool.
Copy
```
iscsiadm -m node -o new -T <volume IQN> -p <iSCSI IP address>:<iSCSI port>
```

A successful registration response resembles the following example:
```
New iSCSI node [tcp:[hw=,ip=,net_if=,iscsi_if=default] 169.254.0.2,3260,-1 iqn.2015-12.us.oracle.com:c6acda73-90b4-4bbb-9a75-faux09015418] added
```

  4. Configure iSCSI to automatically connect to the authenticated block volumes after a reboot:
Copy
```
iscsiadm -m node -T <volume IQN> -o update -n node.startup -v automatic
```

**Note:** All command arguments are essential. Success returns no response.
  5. If you enabled CHAP when you attached the volume, authenticate the iSCSI connection by providing the volume's CHAP credentials as follows:
Copy
```
iscsiadm -m node -T <volume IQN> -p <iSCSI IP address>:<iSCSI port> -o update -n node.session.auth.authmethod -v CHAP
```

Copy
```
iscsiadm -m node -T <volume IQN> -p <iSCSI IP address>:<iSCSI port> -o update -n node.session.auth.username -v <CHAP user name>
```

Copy
```
iscsiadm -m node -T <volume's IQN> -p <iSCSI IP address>:<iSCSI port> -o update -n node.session.auth.password -v <CHAP password>
```

Success returns no response.
  6. Log in to iSCSI:
Copy
```
iscsiadm -m node -T <volume's IQN> -p <iSCSI IP Address>:<iSCSI port> -l
```

A successful login response resembles the following example:
```
Logging in to [iface: default, target: iqn.2015-12.us.oracle.com:c6acda73-90b4-4bbb-9a75-faux09015418, portal: 169.254.0.2,3260] (multiple)
Login to [iface: default, target: iqn.2015-12.us.oracle.com:c6acda73-90b4-4bbb-9a75-faux09015418, portal: 169.254.0.2,3260] successful.
```

  7. You can now format (if needed) and mount the volume. To get a list of mountable iSCSI devices on the instance, run the following command:
Copy
```
fdisk -l
```

The connected volume listing resembles the following example:
```
Disk /dev/sdb: 274.9 GB, 274877906944 bytes, 536870912 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```



**Tip**
If you have multiple volumes that don't have CHAP enabled, you can log in to them all at once by using the following commands:
Copy
```
iscsiadm -m discovery -t sendtargets -p <iSCSI IP address>:<iSCSI port>
iscsiadm -m node –l
iscsiadm -m node –l
```

## Connecting to a Volume on a Windows Instance 🔗 
**Caution** When you're connecting to a Windows boot volume as a data volume from a second instance, you need to append `-IsMultipathEnabled $True` to the `Connect-IscsiTarget` command. See [Attaching a Windows boot volume as a data volume to another instance fails](https://docs.oracle.com/iaas/Content/knownissues.htm#attachWin).
  1. Use the Console to obtain the iSCSI data that you need to connect the volume:
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. Under **List scope** , select the compartment that contains the instance.
    3. Click the name of the instance to display the instance details.
    4. Under **Resources** , click **Attached block volumes** to view the attached block volume.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the volume that you're interested in, and then select **iSCSI Commands and Information**. 
The **iSCSI Commands and Information** dialog box displays the volume's IP address and port, which you need to know later in this procedure.
  2. Log in to the instance by using a Remote Desktop client.
  3. On the Windows instance, open the iSCSI Initiator. The steps to open the iSCSI Initiator vary depending on the version of Windows.
For example: Open **Server Manager** , click **Tools** , and then select **iSCSI Initiator**.
  4. In the iSCSI Initiator Properties dialog box, click the **Discovery** tab, and then click **Discover Portal**.
  5. Enter the block volume **IP address** and **port** , and then click **OK**.
  6. Click the **Targets** tab.
  7. Under **Discovered targets** , select the volume IQN.
  8. Click **Connect**.
  9. Ensure that the **Add this connection to the list of favorite targets** check box is selected, and then click **OK**.
  10. You can now format (if needed) and mount the volume. To view a list of mountable iSCSI devices on your instance, in **Server Manager** , click **File and Storage Services** , and then click **Disks**.
The disk is displayed in the list.


Was this article helpful?
YesNo

