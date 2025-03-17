Updated 2024-06-01
# Moving a Dedicated Virtual Machine Host with Manual Migration
To manually migrate a dedicated virtual machine host, you manually move each instance that is placed on the unhealthy dedicated virtual machine host to a healthy host. This method requires that you create a new dedicated virtual machine host, delete (terminate) any instances that are placed on the original dedicated virtual machine host, and then launch new instances from the retained boot volumes. Instances that have additional VNICs, secondary IP addresses, remote attached block volumes, the Trusted Platform Module (TPM) enabled, or that belong to a backend set of a load balancer require additional steps.
**Tip** You now have the option to migrate Dedicated Virtual Machine Hosts using reboot migration which automates many of the steps that follow in this section. For more information, see: 
  * [Managing On-Demand Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm#migrate-on-demand "You can migrate instances on an OCI dedicated virtual machine host on-demand using the console, CLI, or API. First, select an existing dedicated virtual machine host or set up a new dedicated virtual machine host to serve as the destination host for migrating instances. Then, using the desired method, start the migration process.")
  * [Managing Maintenance Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm#dvmh-maintenance "Dedicated virtual machine host instances might require migration because of scheduled or unscheduled maintenance for the host. Customers are notified by a notification message or by a console message when viewing the dedicated virtual machine host. In this case, you can migrate all the instances from a source host to a destination host. Depending on the type of planned maintenance, you might be able to extend the maintenance due date. The notification indicates whether you can extend the maintenance due date.")


## Limitations and Warnings for Manual Migration 🔗 
Be aware of the following limitations and warnings when performing a manual migration:
  * Any public IP addresses assigned to your instance from a [reserved public pool](https://docs.oracle.com/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm) are retained. Any that were not assigned from a reserved public IP address pool will change. Private IP addresses do not change.
  * MAC addresses, CPUIDs, and other unique hardware identifiers do change during the move. If any applications running on the instance use these identifiers for licensing or other purposes, be sure to take note of this information before moving the instance to help you manage the change.
  * Shielded instances have additional limitations. See [Migrating Shielded Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#migrate).


## Prerequisites for Manual Migration 🔗 
Perform the following steps for each instance that is placed on the dedicated virtual machine host.
  1. Before moving the instance, document all critical details:
     * The instance's region, availability domain, and fault domain.
     * The instance's display name.
     * All private IP addresses, names, and subnets. Note that the instance can have multiple VNICs, and each VNIC can have multiple secondary IP addresses. 
     * All private DNS names. The instance can have multiple VNICs, and each VNIC can have multiple secondary IP addresses. Each private IP address can have a DNS name.
     * Any [public IP addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm) assigned from a reserved public pool. Note that the instance can have multiple VNICs, and each VNIC can have multiple secondary private IP addresses. Each VNIC and secondary private IP address can have an attached public IP address.
     * Any block volumes attached to the instance.
     * Any tags on the instance or attached resources.
  2. Prepare the instance for manual migration:
     * Ensure that any block volumes defined in `/etc/fstab` use the [recommended options](https://docs.oracle.com/iaas/Content/Block/References/fstaboptions.htm).
     * Ensure that any File Storage service (NFS) mounts use the `nofail` option.
     * If you have statically defined any network interfaces belonging to secondary VNICs using their MAC addresses, such as those defined in `/etc/sysconfig/network-scripts/ifcfg*`, those interfaces will not start due to the change in the MAC address. Remove the static mapping.
     * If you use the [Oracle-provided script](https://github.com/oracle/terraform-examples/blob/master/examples/oci/connect_vcns_using_multiple_vnics/scripts/secondary_vnic_all_configure.sh) to configure secondary VNICs, ensure it runs automatically at startup.


## Moving a Dedicated Virtual Machine Host Instance Manually 🔗 
After you complete the prerequisites, [create a new dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm#creating-dvmh "You must create a dedicated virtual machine host in Compute before you can place any instances on it."). Use the same [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#dedicatedvmhost) as the original dedicated virtual machine host and create the dedicated virtual machine host in the same fault domain.
For each instance that is placed on the dedicated virtual machine host, perform the following steps.
**Note** Start with the largest instance first. Moving the largest instance first helps you to [optimize capacity on the dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#ocpu).
  1. Stop any running applications.
  2. Ensure that those applications will not start automatically.
**Caution** When the relocated instance starts for the first time, any block volumes, secondary VNICs, or any resource that relies on them, will not be attached. The absence of these resources can cause application issues.
  3. If the instance uses a dense I/O [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes), back up the locally-attached NVMe-based SSD:
    1. [Create](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm) and [attach](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm) one or more block volumes to the instance.
    2. Copy the data from the NVMe devices to the block volumes.
  4. Unmount any [block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/disconnectingfromavolume.htm) or File Storage [service (NFS) mounts](https://docs.oracle.com/iaas/Content/File/Tasks/mountingfilesystems.htm).
  5. [Back up all block volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm).
  6. [Create a backup of the boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm).
**Important** Do not generalize or specialize Windows instances.
  7. Terminate (delete) the instance, preserving the attached boot volume:
[Using the Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm)
Follow the steps in [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances."), ensuring that the **Permanently delete the attached boot volume** check box is cleared. This preserves the boot volume that is associated with the instance.
[Using the API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm)
Use the [TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance) operation and pass the `preserveBootVolume` parameter set to `true` in the request. 
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm)
Use the [instance terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/terminate.html) operation and set the `preserve-boot-volume` option to `true`.
  8. [Create a new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") using the boot volume from the terminated instance.
(Optional) If the instance is on a new dedicated virtual machine host:
     * In the **Placement** section, click **Show advanced options**.
     * For **Capacity type** , select **Dedicated host**.
     * Select the dedicated virtual machine host that you want to place the instance on.
In the create instance flow, specify the private IP address that was attached to the primary VNIC. If the public IP address was assigned from a reserved IP address pool, be sure to assign the same IP address.
  9. When the instance state changes to **Running** , [stop the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
  10. Recreate any [secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) and [secondary IP addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipaddressesanddns.htm).
  11. [Attach any block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
**Note** This step includes any volumes used to back up local NVMe devices. Copy the data onto the NVMe storage on the new instance, and then detach the volumes.
  12. [Start the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
  13. Start and test any applications on the instance.
  14. Configure the applications to start automatically, as required.
  15. [Recreate the required tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  16. (Optional) After you confirm that the instance and applications are healthy, you can delete the volume backups.


Repeat the steps for each instance that is placed on the dedicated virtual machine host.
**Note** After you move all instances to the new dedicated virtual machine host, [delete the original dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Deleting_a_Dedicated_Virtual_Machine_Host.htm#deleting-dvmh "You can delete a dedicated virtual machine host after you terminate \(delete\) the instances that are placed on it.").
Was this article helpful?
YesNo

