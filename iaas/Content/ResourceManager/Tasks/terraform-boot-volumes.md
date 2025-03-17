Updated 2024-06-26
# Managing Volumes
Use Resource Manager and Terraform configurations to manage boot volumes.
This guide details the following scenarios:
  1. Preserving boot volumes when performing compute instance scaling
  2. Boot volume troubleshooting and repair
  3. Replicating volumes to another availability domain


To read more about boot volumes, see [Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm).
## Preserving Boot Volumes 🔗 
You might want to change compute instance shape while using the same boot volume. When you terminate your instance, you can keep the associated boot volume and use it to create a new instance using a different instance type or shape. This approach is useful for scenarios where instance shape can't be changed [while resizing instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).
To achieve this, you need to detach the boot volume from the running instance. This can be performed by either terminating the instance while preserving the boot volume or by stopping the instance and detaching the boot volume,
All Terraform resources of type `oci_core_instance` have the parameter `preserve_boot_volume` set as `true` by default. This parameter ensures that upon termination of the instance, the attached boot volume isn't terminated.
```
resource "oci_core_instance" "TFInstance" {
 ...
 state = "STOPPED"         // set this state to stop the instance
 preserve_boot_volume = true
}
output "bootVolumeFromInstance" {
 value = [oci_core_instance.TFInstance.boot_volume_id]
}
```

After the boot volume is detached, the OCID of the boot volume can be referred as the source of the new instance, as the following example illustrates:
```
resource "oci_core_instance" "TFScaleInstance" {
 ...
 source_details {
  source_type = "bootVolume"
  // reference the original boot volume id here
  source_id  = "ocid1.bootvolume.oc1.phx.exampleuniqueID"  
 }
}
```

## Detaching Boot Volumes for Troubleshooting and Repair 🔗 
If you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume. Then you can attach it to another instance as a data volume to troubleshoot it. After resolving the issue, you can then reattach it to the original instance or use it to launch a new instance. 
After the boot volume has been detached, the OCID of the boot volume can be referred as the block volume parameter for another instance.
```
resource "oci_core_volume_attachment" "TFBlockAttach" {
 ...
 attachment_type = "iscsi"
 compartment_id = "ocid1.compartment.oc1..exampleuniqueID"
 // new instance
 instance_id   = "ocid1.instance.oc1.phx.exampleuniqueID"  
 // attach the boot volume as a block volume
 volume_id    = "ocid1.bootvolume.oc1.phx.exampleuniqueID"                                          
}
```

After you have resolved the issue, detach this volume from the second instance and attach it as a boot volume to the original instance.
```
resource "oci_core_instance" "TFScaleInstance" {
 ...
 source_details {
  source_type = "bootVolume"
  // attach back as boot volume
  // reference the volume id here
  source_id  = "ocid1.bootvolume.oc1.phx.exampleuniqueID"    
 }
}
```

## Replicate a Volume to an Availability Domain within the Region 🔗 
You can use Terraform to replicate existing compute instance boot and block volumes to another availability domain within the same region.
To replicate a volume:
  1. Create a data source for the volume using `oci_core_boot_volume` or `oci_core_volume`.
  2. Use the `oci_core_boot_volume_backup` or `oci_core_volume_backup` resource to create a backup of the source volume.
  3. Define the target volume resource to be created from the backup.


The following example Terraform configuration replicates both a boot volume and a block volume:
```
provider "oci" {
 region = "us-ashburn-1"
}
 
locals {
 compartment_id = "ocid1.compartment.oc1..exampleuniqueID"
 target_ad = "ilMx:US-ASHBURN-AD-2"
 source_boot_id = "ocid1.bootvolume.oc1.iad.exampleuniqueID"
 source_volume_id = "ocid1.volume.oc1.iad.exampleuniqueID"
}
 
# Boot Volume Clone
data "oci_core_boot_volume" "source" {
 boot_volume_id = local.source_boot_id
}
 
resource "oci_core_boot_volume_backup" "backup" {
 boot_volume_id = data.oci_core_boot_volume.source.id
 type   = "FULL"
}
 
resource "oci_core_boot_volume" "target" {
 availability_domain = local.target_ad
 compartment_id   = local.compartment_id
 source_details {
  id  = oci_core_boot_volume_backup.backup.id
  type = "bootVolumeBackup"
 }
 display_name = "Test Cloned Boot Volume"
}
 
# Block Volume Clone
data "oci_core_volume" "source" {
 volume_id = local.source_volume_id
}
resource "oci_core_volume_backup" "backup" {
 volume_id = data.oci_core_volume.source.id
 type   = "FULL"
}
 
resource "oci_core_volume" "target" {
 availability_domain = local.target_ad
 compartment_id   = local.compartment_id
 source_details {
  id  = oci_core_volume_backup.backup.id
  type = "volumeBackup"
 }
 display_name = "Test Cloned Block Volume"
}
```

You can use these steps to move an instance to the second availability domain or to create a disaster recovery deployment in the second availability domain. 
If this method is used for a pure retargeting scenario where the source volumes (and the backups) are removed after the duplication, then the Terraform configuration must be refactored after the source volumes are removed to avoid destroying the target instances on the next apply.
If using this scenario for disaster recovery cold standby, you can regularly use the Terraform `taint` command to mark the volume for destruction and recreation on the next application of the configuration.
Was this article helpful?
YesNo

