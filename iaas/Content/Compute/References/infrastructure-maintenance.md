Updated 2025-01-24
# Infrastructure Maintenance
Oracle Cloud Infrastructure performs routine data center maintenance on the physical infrastructure for compute instances. This maintenance includes tasks such as upgrading and replacing hardware or performing maintenance that halts power to the host. This topic provides details about infrastructure maintenance, migration options, and status metrics that you can use to monitor infrastructure maintenance.
You can use compute infrastructure health metrics to monitor the status of your instances during maintenance.
**Note** For dedicated virtual machine hosts, see [Managing Maintenance Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm#dvmh-maintenance "Dedicated virtual machine host instances might require migration because of scheduled or unscheduled maintenance for the host. Customers are notified by a notification message or by a console message when viewing the dedicated virtual machine host. In this case, you can migrate all the instances from a source host to a destination host. Depending on the type of planned maintenance, you might be able to extend the maintenance due date. The notification indicates whether you can extend the maintenance due date.").
## Maintenance Actions 🔗 
Oracle Cloud Infrastructure supports a variety of maintenance actions for compute instances including live migration, scheduled maintenance, rebuild in place, and manual migration. The maintenance action depends on characteristics such as the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) that the instance uses.
### Live Migration (No Downtime) 🔗 
[Live Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration) is a mechanism for moving a VM from one physical server to another while the VM is still running. During a live migration, the source VM instance continues to run as the Compute service copies memory and all virtual components to the new target VM instance. When the copy is complete, there is only a slight pause, typically measured in tens of milliseconds, when the system switches to the new VM. Disruption is minimal.
### Scheduled Maintenance (Short Downtime) 🔗 
With scheduled maintenance, a date is set for when an instance is moved to a new host. Using [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot), the instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration. You can control when the downtime occurs by proactively reboot migrating the instance before the maintenance due date. In rare cases reboot migration is not possible and the instance is terminated.
### Rebuild in Place (Long Downtime) 🔗 
This maintenance action doesn't move the instance. At the scheduled time, the instance is stopped, rebuilt on the same physical hardware, and restarted. A downtime of several hours occurs during the maintenance process.
A rebuild in place preserves instance properties that are tied to the physical hardware, such as the MAC address or universal identification number. A rebuild in place also lets you retain the locally-attached NVMe-based SSD on a dense I/O instance.
For VMs, if you want to minimize downtime and can delete the locally-attached NVMe-based SSD, you can proactively reboot the instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be permanently deleted. A short downtime occurs during the migration.
### Manual Migration 🔗 
For VM instances where the preceding actions are not available, you must [move the instance manually](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#manual). This method requires that you delete (terminate) the instance, and then launch a new instance from the retained boot volume. Instances that have additional VNICs, secondary IP addresses, remote attached block volumes, the Trusted Platform Module (TPM) enabled, or that belong to a backend set of a load balancer require additional steps.
In rare cases, recovering a VM instance on the same physical host isn't possible. Oracle Cloud Infrastructure notifies you to delete (terminate) the instance within 14 days. If you don't delete the instance before the deadline, Oracle Cloud Infrastructure disables the instance on the deadline and deletes it within the next seven days. The boot volume and remote attached data volume are preserved.
## Planned Maintenance 🔗 
### Identifying Instances with Planned Maintenance 🔗 
If an instance supports reboot migration or rebuild in place, click the **Maintenance** tab. The maintenance details page indicates when the planned maintenance is scheduled to start. The maintenance start and end time are shown in the **Scheduled to Start** column. For instances that only support manual migration, Oracle Cloud Infrastructure sends you a notification and a maintenance event is shown in the maintenance details page.
To identify the instances that are scheduled for maintenance, do any of the following things:
[Using the Console: To see which instances in the current compartment are scheduled for maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm)
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Maintenance**. 
A list of instances scheduled for maintenance is displayed.
  2. Click the instance that you're interested in, and then click the **Maintenance** tab for the instance. This start and stop date and times are displayed for any maintenance events.


[Using the API: To see which instances in a compartment are scheduled for maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm)
Use the `InstanceMaintenanceEvents` operation to list events. Provide a compartment field to list all the instances with maintenance events in a given compartment. Filter results using options like instanceAction or lifecycleState to narrow down the search.
[Using Search: To find all instances that are scheduled for maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm)
  1. In the top navigation bar, select **Search for resources, services, documentation, and Marketplace** , and then select **Advanced resource query**.
  2. Click **Select Sample Query** , and then click **Query for all instances which have an upcoming scheduled maintenance reboot**. 
The following is an example query:
```
query
 instancemaintenanceevent resources
  where (timeWindowStart > 'Now' && lifecycleState = 'SCHEDULED')
```

  3. Click **Search**.


A list of matching instances are displayed.
An instance is no longer impacted by a maintenance event when the **Maintenance** tab is empty.
### Extending Maintenance Deadline 🔗 
You can extend the maintenance due date for instances that are scheduled for maintenance or termination. Extending the deadline is supported for reboot migration maintenance, which is typically scheduled on VM and bare metal instances that use standard or flex shapes. OCI determines the latest possible time that the due date can be extended to.
[Using the Console: To extend the maintenance due date for an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in, click the **Maintenance** tab, then click **Reschedule**. 
  3. Click **Extend deadline**.
  4. In the **New deadline** box, select a new date and time.
  5. Click **Save changes**.
The maintenance due date is extended. Within 24 hours after the maintenance due date, the instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration.


[Using the API: To extend the maintenance due date for an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm)
  1. Check the latest possible time that the due date can be extended to by using the [GetInstanceMaintenanceReboot](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceMaintenanceReboot/GetInstanceMaintenanceReboot/) operation.
  2. Extend the maintenance due date by doing either of the following things:
     * **VMs and bare metal instances:** Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation, passing the value `REBOOTMIGRATE` as the action to perform. In the `timeScheduled` attribute, provide the updated due date.
     * **VMs:** Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation, passing the updated due date in the `timeMaintenanceRebootDue` attribute.
The maintenance due date is extended. Within 24 hours after the maintenance due date, the instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration.


### Recovering an Instance 🔗 
When the underlying infrastructure for an instance is unhealthy, Oracle Cloud Infrastructure automatically attempts to recover the instance. The maintenance action depends on the type of instance.
  * **Virtual machine (VM) instances:** When possible, the instance is live migrated to a healthy physical host. If live migration isn't possible, the instance is reboot migrated or rebuilt in place, depending on the shape.
  * **Bare metal instances:** When possible, the instance is reboot migrated to a healthy physical host. If reboot migration isn't possible, you must manually migrate the instance.


### Planned Maintenance for VM Instances 🔗 
When an infrastructure maintenance event affects VM instances, Oracle Cloud Infrastructure [live migrates](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration) supported VM instances from the physical VM host that needs maintenance to a new VM host with minimal disruption to running instances.
If a VM instance can't be live migrated or doesn't support live migration, Oracle Cloud Infrastructure schedules a maintenance due date within 14 to 16 days and sends you a notification describing the type of [maintenance action](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#maintenance-actions) that is required, such as reboot migration. A live migration might not succeed if any of the following events happen during the migration: there is too much activity on the instance, a change to the instance is made using the API, or an internal error unrelated to the instance occurs.
If a VM instance is scheduled for maintenance, you can proactively reboot migrate the instance at any time before the scheduled maintenance due date. Proactively reboot migrating lets you control how and when your applications experience downtime. If you don't proactively reboot migrate the instance before the due date, the instance is either [reboot migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) or [rebuilt in place](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#maintenance-actions__rebuild-in-place-defined) for you, depending on the shape.
Customer-managed maintenance for VM instances is supported on standard and dense I/O instance [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes), including platform images and custom images that were imported from outside of Oracle Cloud Infrastructure.
For standard and DenseIO shapes, you can [extend the maintenance due date](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#planned-maintenance__extending-deadline).
**Note** In some cases, like a security related maintenance event, you might not be able to extend the date.
After a migration, by default the instance is recovered to the same lifecycle state as before the maintenance event. If you have an alternate process to recover the instance, you can optionally [configure the instance to remain stopped](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#edit-maintenance-recovery-action) after it is reboot migrated to healthy hardware.
### Planned Maintenance for Bare Metal Instances 🔗 
When an infrastructure maintenance event affects bare metal instances, Oracle Cloud Infrastructure [reboot migrates](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) supported bare metal instances from the physical host that needs maintenance to a healthy host. Oracle Cloud Infrastructure schedules a maintenance due date within 14 to 16 days and sends you a notification describing the type of [maintenance action](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#maintenance-actions) that is required, such as reboot migration. Within 24 hours after the maintenance due date, the bare metal instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration.
If a bare metal instance is scheduled for maintenance, you can proactively reboot the instance at any time before the scheduled maintenance due date. Proactively rebooting lets you control how and when your applications experience downtime. If you do not proactively reboot the instance before the due date, the instance is [reboot migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) for you.
Reboot migration for bare metal instances is supported on standard instance [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) that use Linux-based platform images. Reboot migration for bare metal instances is not supported for instances that use Windows or custom images, shielded instances, instances which have secondary VNICs created and configured on physical NIC with index 1, or for instances that don't use the standard `sanboot` command in the iPXE script.
For standard shapes, you can [extend the maintenance due date](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#maintenance-actions).
If you choose not to reboot before the scheduled time, then Oracle Cloud Infrastructure migrates or rebuilds the instance. After a migration, by default the instance is recovered to the same lifecycle state as before the maintenance event. If you have an alternate process to recover the instance, then you can optionally configure the instance to remain stopped after it is reboot migrated to healthy hardware.
## VM Recovery Due to Infrastructure Failure 🔗 
When the underlying infrastructure of a VM instance fails because of software or hardware issues, Oracle Cloud Infrastructure automatically attempts to recover the instance. 
Standard VM instances are recovered using a [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot), which automatically restores the VM on a healthy host, whether that's the original physical host or a different physical host. The VM failure is detected within one minute of occurrence. If the host cannot be recovered immediately, a healthy move occurs, whereby the VM is moved to a different host. In this scenario, the process of migrating to and restarting on a healthy host automatically begins within five minutes. During the reboot, instance properties such as private and ephemeral public IP addresses, attached block volumes, and VNICs are preserved.
DenseIO VM instances are recovered by rebooting the instance on the same physical host. If recovering a DenseIO instance on the same physical host isn't possible, Oracle Cloud Infrastructure notifies you to reboot migrate or delete (terminate) the instance within 14 days. If reboot migration is used, local NVMe data is still lost. If you don't delete the instance before the deadline, Oracle Cloud Infrastructure disables the instance on the deadline and deletes it within the next seven days. The boot volume and remote attached data volume are preserved.
Oracle Cloud Infrastructure notifies you by email or [announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm) of any VM infrastructure failure events, with the status of the recovery action that was taken. You can also monitor the [instance status metric](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics) to stay aware of any unexpected reboots.
You can choose not to have your VMs automatically restart by [configuring your instances to remain stopped](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#edit-maintenance-recovery-action) after they are recovered.
## Infrastructure Health Metrics 🔗 
You can use [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm) to monitor the maintenance status of the infrastructure that your compute instances run on. The primary metrics to consider for infrastructure maintenance are the [infrastructure health metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics):
  * **Instance health (up/down) status:** The `instance_status` metric lets you check whether a VM instance is available (up) or unavailable (down) when in the running state. If the instance is unavailable for more than 30 minutes, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  * **Instance maintenance status:** The `maintenance_status` metric lets you monitor whether a VM or bare metal instance is scheduled for [planned infrastructure maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#planned-maintenance__vm-planned-maintenance).
  * **Bare metal infrastructure health status:** The `health_status` metric helps you monitor the [health of the infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm#Compute_Health_Monitoring_for_Bare_Metal_Instances) for bare metal instances, including hardware components such as the CPU and memory.


### Viewing Instance Status and Maintenance Notifications in the Console 🔗 
You can view the instance status and maintenance reboot notifications in the Console on the Instance Details page. To see these fields:
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. On the **Instance information** tab, in the **Instance details** section, see the **Instance status** field and the **Maintenance reboot** field.
**Note** The Instance status field only displays if the instance was unavailable in the past month.


Was this article helpful?
YesNo

