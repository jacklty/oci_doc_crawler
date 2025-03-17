Updated 2024-10-07
# Mounting a File system On a Windows Instance Using NFS
**Prerequisites**
  * The file system must be created and have at least one export in a mount target. See [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances.").
  * The mount target must have correctly configured security rules or be assigned to an NSG. See [Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/configuring-vcn-security-rules-for-file-storage.htm#configuring-vcn-security-rules-for-file-storage "On Compute Cloud@Customer, you can add the required rules to a preexisting security list associated with a subnet, such as the default security list that is created along with the VCN.").
  * You must know the mount target's IP address. See [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address).
  * You must be able to log into the Microsoft Windows OS on the instance with superuser or administrator privileges.


**Before You Begin**
The following tasks are included in this procedure, and you might want to be aware of them before you begin.
  * **Installation of the Microsoft Windows NFS Client** – This service must be installed on the instance from which you want to mount the file system. Installing the client often requires a restart of the instance.
  * **The`AnonymousGid` and `AnonymousUid` identity values must be configured to allow write access.** – Access to NFS file systems requires UNIX user and group identities, which are not the same as Microsoft Windows user and group identities. By default, file systems write permissions are only granted to the root user. To enable user access to NFS shared resources, the Microsoft Windows client for NFS accesses file systems anonymously, using `AnonymousGid` and `AnonymousUid`. 
**Caution**
Updating the AnonymousGid and AnonymousUid values require registry changes to your instance.


Choose one the following methods:
## Using the Microsoft Windows Command Prompt 🔗 
  1. Log into your Microsoft Windows instance.
See [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
  2. Open Microsoft Windows PowerShell and run as Administrator:
    1. Go to Start and open PowerShell.
    2. In PowerShell, type the following to run as Administrator:
```
Start-Process powershell -Verb runAs
```

    3. In the User Account Control window, click Yes. A new Administrator: PowerShell window opens. You can close the standard PowerShell window to avoid confusing them. 
  3. In Administrator: PowerShell, get the NFS client and update the registry by typing the following:
```
Install-WindowsFeature -Name NFS-Client
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default -Name AnonymousUid -Value 0
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default -Name AnonymousGid -Value 0
Stop-Service -Name NfsClnt
Restart-Service -Name NfsRdr
Start-Service -Name NfsClnt
```

  4. Open a standard Command Prompt Window.
**Important**
NFS file systems mounted as Administrator are not available to standard users. 
  5. From the Command Prompt window, mount the file system.
See the cautions and notes below the example.
In the following example, replace:
     * `10.x.x.x` with the mount point IP address (see [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address))
     * `fs-export-path` with the file system export path (see [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances."))
     * `X` with the drive letter of any available drive you want to map the file system to.
Example:
```
mount **_10.x.x.x_**:/**_fs-export-path_** **_X_**:
```

  6. Verify that you can access and write to the file system.
    1. Access the file system.
In the example, replace `X` with the drive letter you used to mount the file system. 
```
X:
```

    2. Write a file.
```
echo > myfile.txt
```

    3. Verify that you can view the file.
```
dir
```



## Using the Microsoft Windows File Explorer 🔗 
  1. Log into your Microsoft Windows instance.
See [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
  2. Open Microsoft Windows PowerShell and run as Administrator:
    1. Go to Start and open PowerShell.
    2. In PowerShell, type the following to run as Administrator:
```
Start-Process powershell -Verb runAs
```

    3. In the User Account Control window, click Yes. A new Administrator: PowerShell window opens. You can close the standard PowerShell window to avoid confusing them. 
  3. In Administrator: PowerShell, get the NFS client by typing the following:
```
Install-WindowsFeature -Name NFS-Client
```

  4. If necessary, restart your system. 
  5. Open the registry editor (regedit) to map the AnonymousGid and AnonymousUid to the root user. 
**Caution**
User identity mapping requires changes to your system registry.
    1. Click Windows Search.
    2. Enter `regedit` in the Search field and press Enter. 
    3. Click Yes to allow changes to your device. 
    4. Click `HKEY_LOCAL_MACHINE`. Then, browse to: `Software\Microsoft\ClientForNFS\CurrentVersion\Default`.
  6. Add a new DWORD32 registry entry for `AnonymousGid`:
    1. Click Edit, and select New DWORD (32 bit) Value.
    2. In the Name field, enter `AnonymousGid`. Leave the value at `0`.
  7. Repeat the previous step to add a second DWORD32 registry entry named `AnonymousUid` with a value of `0`.
  8. Open Microsoft Windows Command Line (CMD) and run as Administrator:
    1. Go to Start and scroll down to Apps. 
    2. In the Windows System section, press CTRL+Shift and click Command Prompt. 
  9. In the Microsoft Windows Command Line (CMD) window, restart the NFS Client by typing the following:
```
nfsadmin client stop
```
```
nfsadmin client start
```

  10. Open File Explorer and select This PC. In the Computer tab, select Map network drive.
  11. Select the Drive letter that you want to assign to the file system. 
  12. In the Folder field, enter the following line, replacing:
     * `10.x.x.x` with the mount point IP address (see [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address))
     * `fs-export-path` with the file system export path (see [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances."))
Line:
```
\\**_10.x.x.x_**\**_fs-export-path_**
            
```

  13. Click Finish.


Was this article helpful?
YesNo

