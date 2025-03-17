Updated 2023-01-04
# Extending the Partition for a Boot Volume
When you create a new virtual machine (VM) instance or bare metal instance based on a [platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm) or [custom image](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm), you have the option of specifying a custom boot volume size. You can also expand the size of the boot volume for an existing instance; see [Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#Resizing_a_Volume) for more information. In order to take advantage of the larger size, you need to extend the partition for the boot volume. For block volumes, see [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume).
**Note** After a boot volume has been resized, the first backup on the resized boot volume will be a full backup. See [Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm#backuptypes) for more information about full versus incremental boot volume backups. 
## Required IAM Policy 🔗 
Extending a partition on an instance does not require a specific IAM policy. However, you may need permission to run the necessary commands on the instance's guest OS. Contact your system administrator for more information.
## Extending the Root Partition on a Linux-Based Image 🔗 
For instances running Linux-based images, you need to extend the root partition and then grow the file system using the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` operation from [OCI Utilities](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm).
## Extending the System Partition on a Windows-Based Image 🔗 
On Windows-based images, you can extend a partition using the Windows interface or from the command line using the DISKPART utility.
### Windows Server 2012 and Later Versions
The steps for extending a system partition on instances running Windows Server 2012, Windows Server 2016, Windows Server 2019, or Windows Server 2022 are the same, and are described in the following procedures.
[Extending the system partition using the Windows interface](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm)
  1. Open the [Disk Management](https://docs.microsoft.com/windows-server/storage/disk-management/overview-of-disk-management) system utility on the instance.
  2. Right-click the boot volume and select **Extend Volume**.
  3. Follow the instructions in the **Extend Volume Wizard** :
    1. Select the disk that you want to extend, enter the size, and then click **Next**.
    2. Confirm that the disk and size settings are correct, and then click **Finish**.
  4. Verify that the boot volume's system disk has been extended in Disk Management.


[Extending the system partition using the command line with DISKPART](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm)
  1. Open a command prompt as administrator on the instance.
  2. Run the following command to start the DISKPART utility:
Copy
```
diskpart
```

  3. At the `DISKPART` prompt, run the following command to display the instance's volumes:
Copy
```
list volume
```

  4. Run the following command to select the boot volume:
Copy
```
select volume <volume_number>
```

<volume_number> is the number associated with the boot volume that you want to extend the partition for.
  5. Run the following command to extend the partition:
Copy
```
extend size=<increased_size_in_MB>
```

<increased_size_in_MB> is the size in MB that you want to extend the partition to. 
**Caution** When using the DISKPART utility, do not overextend the partition beyond the current available space. Overextending the partition could result in data loss.
  6. To confirm that the partition was extended, run the following command and verify that the boot volume's partition has been extended:
Copy
```
list volume
```



Was this article helpful?
YesNo

