Updated 2023-08-15
# Mounting File Systems on UNIX-based Instances
On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.
Mount targets serve as network access points for file systems. After your mount target is assigned an IP address, you can use it together with the export path to mount the file system. 
On the instance from which you want to mount the file system, you need to install an NFS client package and create a mount point. When you mount the file system, the mount point effectively represents the root directory of the File Storage file system, allowing you to write files to the file system from the instance. 
**Prerequisites**
  * The file system must be created and have at least one export in a mount target. See [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances.").
  * The mount target must have correctly configured security rules or be assigned to an NSG. See [Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/configuring-vcn-security-rules-for-file-storage.htm#configuring-vcn-security-rules-for-file-storage "On Compute Cloud@Customer, you can add the required rules to a preexisting security list associated with a subnet, such as the default security list that is created along with the VCN.").


**Note**
**Only for NFSv4 Mounts in Oracle Linux instances** – If you find that the file system owner is assigned as `nobody` instead of the actual user who mounts the file system, and if you haven't set identity squash, you might need to edit the `/etc/idmapd.conf` file. In the file, set the DOMAIN entry to either `localdomain` or to the Active Directory domain name, if applicable. After the change, run `service rpcidmapd      restart` to restart the `rpcidmapd` service. 
Defining settings in the `/etc/idmapd.conf` file is specific to Oracle Linux, and there are other ways to configure the domain depending on the OS in use. Consult your OS documentation.
Was this article helpful?
YesNo

