Updated 2024-08-06
# Creating a File System, Mount Target, and Export
On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances.
## Task Flow 🔗 
No. | Description | Links to Procedures  
---|---|---  
1. |  Ensure that a mount target exists for the subnet that the instance where you want to mount a file system will use and the backing store pool that the file system will use. **Note** The file system and mount target must be in the same compartment and the same backing store pool when you create an export. |  [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.")  
2. |  Create the file system. |  [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.")  
3. |  Create a file system export in the mount target. |  [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.")  
4. |  Enable Security Rules for File Storage. |  [Controlling Access to File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/controlling-access-to-file-storage.htm#controlling-access-to-file-storage "On Compute Cloud@Customer, before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports.")  
5. |  Change NFS export options to control access to the file system. |  [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.")  
After the file system is exported, on the NFS client, perform these tasks to mount the file system:
  1. (If needed) Install NFS client software.
  2. Create a mount point.
  3. On the client, mount the file system to the mount point.
  4. On the client, add whatever files, directories, and data that you want in the file system.


For more information about mounting file systems, see [Mounting File Systems on UNIX-based Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-uxix-based-instances.htm#mounting-file-systems-on-uxix-based-instances "On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.").
Was this article helpful?
YesNo

