Updated 2024-08-06
# Managing Mount Targets and Exports
On Compute Cloud@Customer, a mount target is an NFS endpoint assigned to a VCN subnet of your choice and provides network access for file systems. The mount target provides the IP address or DNS name that's used together with a unique export path to mount the file system.
For an instance to mount a file system, the instance's VCN must have a mount target.
You can reuse the same mount target to make as many file systems available on the network as you want. To reuse the same mount target for multiple file systems, create an export in the mount target for each file system.
**Important**
When more than one file system is exported to the same mount target, you must export to the mount target with the smallest network (largest CIDR number) first. For detailed information and instructions, refer to My Oracle Support [Doc ID 2823994.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2823994.1).
For instructions to create a mount target, see [Creating a File System, Mount Target, and Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-mount-target-and-export.htm#creating-a-file-system-mount-target-and-export "On Compute Cloud@Customer, you can use this task flow to perform all the tasks that are required to create a file system and make it available for instances.").
This section provides instructions for administering mount targets.
Was this article helpful?
YesNo

