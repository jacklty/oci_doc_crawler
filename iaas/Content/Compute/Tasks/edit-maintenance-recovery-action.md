Updated 2025-01-13
# Setting Instance Availability During Maintenance Events
When the underlying infrastructure for a compute instance needs to [undergo planned maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#planned-maintenance__vm-planned-maintenance) or [recover from an unexpected failure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#hardware-failure), Oracle Cloud Infrastructure automatically attempts to recover the instance by migrating it to healthy hardware.
For virtual machine (VM) instances, when applicable, Oracle Cloud Infrastructure live migrates [supported VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration__live-migration-support) from the physical VM host that needs maintenance to a healthy VM host with minimal disruption to running instances. If you do not want your instances live migrated, you can choose to receive a notification for the maintenance event. After you receive the notification, you have 14 days to [reboot migrate](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot) your instance. The instance is only live migrated if you do not reboot the instance before the due date. If the instance can't be live migrated, reboot migration (for standard VM shapes) or rebuild in place (for dense I/O VM shapes) is used instead.
After a migration, by default the instance is recovered to the same lifecycle state as before the maintenance event. If you have an alternate process to recover the instance after a reboot migration, you can optionally configure the instance to remain stopped after the maintenance is complete. You can then restart the instance on your own schedule.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Using the Console 🔗 
You can use the Console to configure live migration options as well as the lifecycle state of instances after a migration.
### Configuring Live Migration 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Availability configuration** tab.
  5. In the **Live migration** section, select an option:
     * **Let Oracle Cloud Infrastructure choose the best migration option** : Select this option to let Oracle Cloud Infrastructure choose the best option to [migrate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host) to a healthy physical VM host if an underlying infrastructure component needs to undergo maintenance.
     * **Use live migration if possible** : Select this option to have the instance [live migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration) to a healthy physical VM host without any notification or disruption. If live migration isn't successful, [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot) is used. Some shapes do not support live migration.
     * **Opt-out** : Select this option to have a notification sent for the maintenance event. The instance is live migrated if you do not proactively reboot the instance before the due date.
  6. Click **Save changes**.


### Configuring the Lifecycle State 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Availability configuration** tab.
  5. For the **Restore instance lifecycle state after infrastructure maintenance** check box, select an option:
     * To reboot a running instance after it is recovered, select the check box.
     * To recover the instance in the stopped state, clear the check box.
  6. Click **Save changes**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to edit the maintenance recovery action for an instance:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo

