Updated 2023-12-19
# Managing Maintenance Reboot Migration for Dedicated Virtual Machine Hosts
Dedicated virtual machine host instances might require migration because of scheduled or unscheduled maintenance for the host. Customers are notified by a notification message or by a console message when viewing the dedicated virtual machine host. In this case, you can migrate all the instances from a source host to a destination host. Depending on the type of planned maintenance, you might be able to extend the maintenance due date. The notification indicates whether you can extend the maintenance due date.
**Warning** Reboot migration for Dedicated Virtual Machine Hosts is not supported across different availability domains.
**Tip** Some downtime is associated with a dedicated virtual machine host as each instance must be stopped and rebooted on the new destination host. You can see the migration process using the work request feature.
**Important** If no action is taken in the time indicated in the notification message, OCI terminates (deletes) all instances running on the dedicated virtual machine host as part of the repair. The dedicated virtual machine host is also deleted.
## Migrating during Planned Maintenance
When a planned maintenance event affects a dedicated virtual machine host, OCI schedules a maintenance due date within 7 to 14 days and sends you a notification by email or [announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm).
At the time listed in the notification, OCI disables all instances running on the dedicated virtual machine host. After 7 days, OCI terminates (deletes) all instances running on the dedicated virtual machine host as part of the repair. The dedicated virtual machine host is also deleted.
To avoid disruption to your workloads, you must migrate all affected instances using [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm#dvmh-maintenance__reboot-migration) or [manual migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm#manual-migration "To manually migrate a dedicated virtual machine host, you manually move each instance that is placed on the unhealthy dedicated virtual machine host to a healthy host. This method requires that you create a new dedicated virtual machine host, delete \(terminate\) any instances that are placed on the original dedicated virtual machine host, and then launch new instances from the retained boot volumes. Instances that have additional VNICs, secondary IP addresses, remote attached block volumes, the Trusted Platform Module \(TPM\) enabled, or that belong to a backend set of a load balancer require additional steps.") to another dedicated virtual machine host before the scheduled time.
## Migrating during Unplanned Maintenance
When the underlying infrastructure for a dedicated virtual machine host fails because of software or hardware issues, you must migration all affected instances to another dedicated virtual machine host as soon as possible using [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm#dvmh-maintenance__reboot-migration) or [manual migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm#manual-migration "To manually migrate a dedicated virtual machine host, you manually move each instance that is placed on the unhealthy dedicated virtual machine host to a healthy host. This method requires that you create a new dedicated virtual machine host, delete \(terminate\) any instances that are placed on the original dedicated virtual machine host, and then launch new instances from the retained boot volumes. Instances that have additional VNICs, secondary IP addresses, remote attached block volumes, the Trusted Platform Module \(TPM\) enabled, or that belong to a backend set of a load balancer require additional steps.").
OCI notifies you by email or [announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm) to move the instances to a healthy dedicated virtual machine host within 7 to 14 days, depending on the type of infrastructure failure. If you don't move the instances, OCI disables the instances, and then terminates (deletes) the instances within the next 7 days. The dedicated virtual machine host is also deleted. The boot volumes and remote attached data volumes are preserved.
If there aren't any VMs placed on the dedicated virtual machine host, OCI deletes the dedicated virtual machine host within 2 days.
You cannot extend the deadline to migrate a dedicated virtual machine host that experiences infrastructure failure.
## Moving Instances with Reboot Migration 🔗 
Using reboot migration, you can move instances to a new dedicated virtual machine host with a reboot. Move the instances using the console, CLI, or API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm)


  * When maintenance migration is needed for a dedicated virtual machine host, follow these steps to migrate the instances using the console.
    1. From the main menu, select **Compute** then **Dedicated Virtual Machine Hosts.**
    2. Select a compartment.
    3. Select the source dedicated virtual machine host. Note the **Action Required** message for the host.
    4. Click **Migrate instances**.
    5. Select the destination dedicated virtual machine host using the host list provided or by specifying the host OCID.
    6. Click **Migrate**.
**Important** If the selected instance has local NVME on a dense I/O shape, the local storage is deleted during the migration process. In this case, a prompt is provided to confirm the deletion of local resources.
To monitor the migration process, click **Work Requests** in the left menu. A job is created for each instance. The progress for each instance migration is shown in the console.
When the migration is complete, a message is displayed in the console. The destination host shows the new instances, while the old instances don't show up in the source host. All instances are on the destination host.
  * Use the [instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html) command and required parameters to update an instance.
```
oci compute instance update --instance-id <ocid1> --dedicated-vm-host-id <ocid1> --fault-domain FAULT-DOMAIN-# --from-json <file://path/to/file.json>
```

`file://path/to/file.json` is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute Service CLI commands, see the [Compute command line reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation to update an instance.


Was this article helpful?
YesNo

