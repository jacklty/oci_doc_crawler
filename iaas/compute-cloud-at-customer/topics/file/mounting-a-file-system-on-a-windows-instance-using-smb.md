Updated 2025-02-05
# Mounting a File System on a Windows Instance Using SMB
**General Prerequisites**
  * The file system must be created and have at least one export in a mount target. See [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances.").
  * The mount target must have correctly configured security rules or be assigned to an NSG. See [Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/configuring-vcn-security-rules-for-file-storage.htm#configuring-vcn-security-rules-for-file-storage "On Compute Cloud@Customer, you can add the required rules to a preexisting security list associated with a subnet, such as the default security list that is created along with the VCN.").
  * You must know the mount target's IP address. See [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address).
  * You must be able to log into the Microsoft Windows OS on the instance with superuser or administrator privileges.


**Specific Prerequisites for SMB Support**
Using the SMB protocol requires that the Microsoft Windows instances and Compute Cloud@Customer belong to the same Active Directory domain. 
This procedure assumes that the AD service is already configured in your data center infrastructure. 
To add a Microsoft Windows instance to your AD service, perform the necessary administrative tasks according to the documentation for your version of Microsoft Windows OS.
To add the Compute Cloud@Customer to your AD service, Oracle must add the AD domain name to the Oracle Cloud Infrastructure Active Directory Domain configuration. To request this administrative action, submit a support request. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
**Relaxing File System Permissions Before Network Mapping with SMB**
By default, write permissions to a file system are limited to the UNIX superuser and group identity. To provide write permission to AD domain users, the permissions need to be relaxed.
  1. Mount the network drive using NFS protocol.
See [Mounting a File system On a Windows Instance Using NFS](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-a-file-system-on-a-windows-instance-using-nfs.htm#mounting-a-file-system-on-a-windows-instance-using-nfs).
  2. Relax the file system permissions:
    1. Open File Explorer, select the mapped drive and right-click it, then select Properties.
    2. Select the NFS Attributes tab.
    3. Change File permissions by checking all RWX check boxes to relax the permissions for Owner, Group, and Other.
    4. Click OK.
  3. Disconnect the NFS-mounted drive.
Now that the file system permissions are relaxed, you can mount the file system using the SMB protocol.


**Mounting a File System Using SMB**
  1. Log into your Microsoft Windows instance.
  2. Open File Explorer and select This PC.
  3. In the Computer tab, select Map network drive.
  4. In the Folder field, enter the following line and replace these items:
     * `10.x.x.x` with the mount target IP address.
     * `fs-export-path-ID` with the file system export path (see [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.")).
**Note** – Do not include `\export` in the `fs-export-path-ID` string when mounting using SMB.
```
\\10.x.x.x\fs-export-path-ID
```

Example:
```
\\192.0.2.0\39u21btystm8x1axizezb9a3lfnpzjho98evi3ij450i96vj0a8jpf36au26
```

  5. select the 'Drive' letter of any available drive you want to map the file system to. 
  6. If needed, select the Connect using different credentials check box.
  7. Click Finish.
  8. When prompted, provide the user name and password of the AD domain user used for mapping the network drive.
  9. Click OK.
  10. In a Command Prompt window (cmd), verify that the drive is properly mapped using this command:
```
C:\>net use
New connections will be remembered.
Status    Local   Remote          Network
-------------------------------------------------------------------------------
OK      Z:    \\10.0.0.2\uvj1iw6ytyecqijcbdgpy7ec15mgsv044i7609giqx7ukfn6t2pwgfqot0ma
                        Microsoft Windows Network
The command completed successfully.
C:\>
```



Was this article helpful?
YesNo

